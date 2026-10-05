# /// script
# requires-python = ">=3.10,<3.13"
# dependencies = ["torch", "numpy", "svgpathtools", "matplotlib"]
# ///
"""Module 4, « Quatre façons de générer » : un modèle de diffusion en deux dimensions.

Les données sont des points tirés uniformément dans la feuille d'érable du drapeau du Canada
(Wikimedia Commons, domaine public ; scripts/data/diffusion/drapeau-canada.svg). Un petit réseau
(position + étape → 128 → 128 → 128 → bruit estimé) est entraîné comme un modèle de diffusion
(DDPM, 100 étapes) à retrouver le bruit ajouté. Exporte pour l'applet `diffusion.html` :
- le calendrier de bruit (betas) ;
- les poids du réseau, en float16 encodés en base64 ;
- 1 500 points de données (pour le brouillage) et le contour de la feuille.

    uv run scripts/gen_diffusion.py
"""
import base64, json, math, re
from pathlib import Path
import numpy as np
import torch
from torch import nn
from matplotlib.path import Path as Chemin
from svgpathtools import parse_path

torch.manual_seed(0)
rng = np.random.default_rng(0)
RACINE = Path(__file__).resolve().parent
SORTIE = RACINE.parent / "static" / "html" / "applets" / "data" / "diffusion.json"

# ── La feuille : second sous-chemin du tracé blanc du drapeau ─────────────────
svg = (RACINE / "data" / "diffusion" / "drapeau-canada.svg").read_text()
d = re.findall(r'd="([^"]+)"', svg)[1]
feuille = max(parse_path(d).continuous_subpaths(), key=len)   # la feuille a bien plus de segments que le carré
contour = np.array([[p.real, p.imag] for p in (feuille.point(t) for t in np.linspace(0, 1, 600))])
centre = (contour.max(0) + contour.min(0)) / 2
echelle = (contour.max(0) - contour.min(0)).max() / 2
contour = (contour - centre) / echelle * 1.6              # la feuille occupe [-1,6 ; 1,6]
contour[:, 1] *= -1                                        # l'axe y du SVG pointe vers le bas
poly = Chemin(contour)
cand = rng.uniform(-1.7, 1.7, size=(200_000, 2))
donnees = cand[poly.contains_points(cand)][:40_000].astype(np.float32)
print(len(donnees), "points dans la feuille")

# ── Diffusion ─────────────────────────────────────────────────────────────────
T = 100
betas = np.linspace(1e-4, 0.1, T).astype(np.float32)
abar = np.cumprod(1 - betas)
print("part du signal à la dernière étape :", float(np.sqrt(abar[-1])))


def plonge(t):                                             # l'étape, codée par des sinus et des cosinus
    f = torch.exp(torch.arange(8, dtype=torch.float32) * (-math.log(100) / 7))
    a = t[:, None].float() * f[None, :]
    return torch.cat([torch.sin(a), torch.cos(a)], 1)


class Debruiteur(nn.Module):
    def __init__(self):
        super().__init__()
        self.r = nn.Sequential(nn.Linear(18, 128), nn.ReLU(), nn.Linear(128, 128), nn.ReLU(),
                               nn.Linear(128, 128), nn.ReLU(), nn.Linear(128, 2))

    def forward(self, x, t):
        return self.r(torch.cat([x, plonge(t)], 1))


X = torch.tensor(donnees)
AB = torch.tensor(abar)
m = Debruiteur()
opt = torch.optim.Adam(m.parameters(), lr=2e-3)
sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, 30_000)
for pas in range(30_000):
    x0 = X[torch.randint(len(X), (1024,))]
    t = torch.randint(T, (1024,))
    eps = torch.randn_like(x0)
    xt = AB[t].sqrt()[:, None] * x0 + (1 - AB[t]).sqrt()[:, None] * eps
    perte = ((m(xt, t) - eps) ** 2).mean()
    opt.zero_grad(); perte.backward(); opt.step(); sched.step()
    if pas % 5000 == 0:
        print(f"pas {pas:5d} : perte {perte.item():.4f}")

# ── Contrôle : générer 4 000 points et mesurer la part qui tombe dans la feuille ──
with torch.no_grad():
    x = torch.randn(4000, 2)
    for t in range(T - 1, -1, -1):
        tt = torch.full((4000,), t)
        e = m(x, tt)
        x = (x - betas[t] / math.sqrt(1 - abar[t]) * e) / math.sqrt(1 - betas[t])
        if t > 0:
            x = x + math.sqrt(betas[t]) * torch.randn_like(x)
gen = x.numpy()
print(f"points générés dans la feuille : {poly.contains_points(gen).mean():.0%}")


def couche(l):
    w = l.weight.detach().numpy().T.astype(np.float16)
    b = l.bias.detach().numpy().astype(np.float16)
    return {"entrees": w.shape[0], "sorties": w.shape[1],
            "w": base64.b64encode(w.tobytes()).decode(), "b": base64.b64encode(b.tobytes()).decode()}


SORTIE.write_text(json.dumps({
    "betas": [round(float(b), 6) for b in betas],
    "couches": [couche(l) for l in m.r if isinstance(l, nn.Linear)],
    "donnees": [[round(float(a), 3), round(float(b), 3)] for a, b in donnees[:1500]],
    "contour": [[round(float(a), 3), round(float(b), 3)] for a, b in contour[::3]],
}, separators=(",", ":")))
print(SORTIE.name, "écrit,", SORTIE.stat().st_size // 1024, "Ko")

