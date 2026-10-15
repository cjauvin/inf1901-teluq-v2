# /// script
# requires-python = ">=3.10,<3.13"
# dependencies = ["torch", "numpy", "scikit-learn"]
# ///
"""Module 4, « Relier les mots et les images » : une petite expérience réelle d'apprentissage contrastif, dans l'esprit de
SimCLR. Un petit réseau apprend, sans aucune étiquette, à donner des vecteurs proches à deux versions modifiées d'un même
chiffre manuscrit (décalée, bruitée, en partie effacée), et des vecteurs éloignés aux autres. On applique ensuite k-means
(k = 10) aux pixels bruts, puis aux vecteurs appris, et l'on mesure à quel point les groupes trouvés correspondent aux vrais
chiffres, que le réseau n'a jamais vus.

Les chiffres sont ceux de scikit-learn (8 × 8 pixels, livrés avec la bibliothèque).

    uv run scripts/gen_contrastif.py
"""
from pathlib import Path
import numpy as np
import torch
from torch import nn
import torch.nn.functional as Fn
from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import adjusted_rand_score

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
torch.manual_seed(0); np.random.seed(0)
X, y = load_digits(return_X_y=True)
X = (X / 16.0).astype(np.float32)
img = torch.tensor(X).view(-1, 1, 8, 8)


def modifier(b):
    """Une version modifiée de chaque image : décalée d'au plus un pixel, assombrie ou éclaircie, bruitée, un coin effacé."""
    n = len(b)
    out = torch.zeros_like(b)
    p = Fn.pad(b, (1, 1, 1, 1))
    dx, dy = np.random.randint(0, 3, n), np.random.randint(0, 3, n)
    for k in range(n):
        out[k] = p[k, :, dy[k]:dy[k] + 8, dx[k]:dx[k] + 8]
    out = out * torch.empty(n, 1, 1, 1).uniform_(0.7, 1.2) + 0.1 * torch.randn_like(out)
    masque = torch.ones_like(out)
    for k in range(n):
        i, j = np.random.randint(0, 6, 2)
        masque[k, :, i:i + 3, j:j + 3] = 0 if np.random.rand() < 0.5 else 1
    return (out * masque).clamp(0, 1.2)


class Encodeur(nn.Module):
    def __init__(self):
        super().__init__()
        self.f = nn.Sequential(nn.Conv2d(1, 32, 3, padding=1), nn.ReLU(), nn.Conv2d(32, 64, 3, padding=1), nn.ReLU(),
                               nn.AdaptiveAvgPool2d(2), nn.Flatten(), nn.Linear(256, 64))
        self.g = nn.Sequential(nn.ReLU(), nn.Linear(64, 32))          # la tête de projection, jetée après l'entraînement

    def forward(self, x):
        h = self.f(x)
        return h, self.g(h)


def contrastive(z1, z2, t=0.2):
    """La perte de SimCLR : chaque vecteur doit reconnaître son jumeau parmi tous les autres du lot."""
    z = Fn.normalize(torch.cat([z1, z2]), dim=1)
    s = z @ z.T / t
    n = len(z1)
    s.fill_diagonal_(-1e9)
    cible = torch.cat([torch.arange(n, 2 * n), torch.arange(0, n)])
    return Fn.cross_entropy(s, cible)


m = Encodeur()
opt = torch.optim.Adam(m.parameters(), lr=3e-3)
for epoque in range(60):
    perm = torch.randperm(len(img))
    for k in range(0, len(img), 256):
        b = img[perm[k:k + 256]]
        _, z1 = m(modifier(b)); _, z2 = m(modifier(b))
        perte = contrastive(z1, z2)
        opt.zero_grad(); perte.backward(); opt.step()
with torch.no_grad():
    H = Fn.normalize(m(img)[0], dim=1).numpy()


def regrouper(Z):
    g = KMeans(10, n_init=20, random_state=0).fit_predict(Z)
    purete = sum(np.bincount(y[g == c]).max() for c in range(10)) / len(y)
    return g, purete, adjusted_rand_score(y, g)


g0, p0, a0 = regrouper(X)
g1, p1, a1 = regrouper(H)
print(f"perte finale {float(perte):.3f}")
print(f"pixels bruts : pureté {p0:.2f}, ARI {a0:.2f}")
print(f"vecteurs appris : pureté {p1:.2f}, ARI {a1:.2f}")

# ── la figure : quelques images de chaque groupe, avant et après ──
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = "\u00a0"
pc = lambda v: f"{v * 100:.0f}{NB}%"
NI, CS = 9, 3.4                                                   # images par groupe, taille d'un pixel
TW = 8 * CS
W, H = 840, 580
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Regrouper sans étiquettes</title>",
     "<desc>Deux panneaux, chacun formé de dix rangées : les dix groupes trouvés par k-means parmi 1 797 chiffres manuscrits, "
     "sans aucune étiquette. Chaque rangée montre neuf images du groupe tirées au hasard ; une image qui n'est pas le chiffre "
     f"majoritaire du groupe est encadrée en rouge. À gauche, k-means appliqué directement aux pixels : plusieurs groupes "
     f"mélangent des chiffres différents, et {pc(p0)} des images tombent dans le groupe de leur chiffre. À droite, k-means "
     f"appliqué aux vecteurs appris par apprentissage contrastif, sans étiquettes : les groupes sont plus nets, et {pc(p1)} des "
     "images tombent dans le groupe de leur chiffre.</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Regrouper les chiffres sans étiquettes{NB}: les pixels, ou des vecteurs appris</text>']
rng = np.random.default_rng(1)


def panneau(x0, titre, sous, g, purete, coul):
    o.append(f'<rect x="{x0}" y="50" width="400" height="{H - 70}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
    o.append(f'<text x="{x0 + 200}" y="72" font-size="13" fill="{coul}" text-anchor="middle" font-weight="700">{titre}</text>')
    o.append(f'<text x="{x0 + 200}" y="89" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">{sous}</text>')
    groupes = sorted(range(10), key=lambda c: np.bincount(y[g == c], minlength=10).argmax())
    for r, c in enumerate(groupes):
        membres = np.flatnonzero(g == c)
        major = np.bincount(y[membres], minlength=10).argmax()
        part = (y[membres] == major).mean()
        yy = 102 + r * 42
        o.append(f'<text x="{x0 + 16}" y="{yy + 19}" font-size="11" fill="{ENCRE}">surtout des <tspan font-weight="700">{major}</tspan></text>')
        o.append(f'<text x="{x0 + 16}" y="{yy + 33}" font-size="10" fill="{ENCRE_PALE}">{pc(part)} du groupe</text>')
        for k, i in enumerate(rng.choice(membres, NI, replace=False)):
            tx = x0 + 104 + k * (TW + 4)
            intrus = y[i] != major
            o.append(f'<rect x="{tx - 1.5:.1f}" y="{yy + 1.5:.1f}" width="{TW + 3:.1f}" height="{TW + 3:.1f}" fill="#111" '
                     + (f'stroke="{ROUGE}" stroke-width="2.4"' if intrus else 'stroke="none"') + '/>')
            for a in range(8):
                for b in range(8):
                    v = X[i, a * 8 + b]
                    if v > 0.05:
                        gr = int(255 * min(1, v))
                        o.append(f'<rect x="{tx + b * CS:.1f}" y="{yy + 3 + a * CS:.1f}" width="{CS:.1f}" height="{CS:.1f}" fill="rgb({gr},{gr},{gr})"/>')
    o.append(f'<text x="{x0 + 200}" y="{H - 36}" font-size="12" fill="{coul}" text-anchor="middle" font-weight="700">'
             f'{pc(purete)} des images dans un groupe dominé par leur chiffre</text>')


panneau(20, "k-means sur les pixels", "chaque image : 64 nombres, ses pixels", g0, p0, BRUN)
panneau(420, "k-means sur les vecteurs appris", "appris par apprentissage contrastif, sans étiquettes", g1, p1, TEAL)
o.append(f'<text x="{W / 2}" y="{H - 8}" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">encadrée en rouge{NB}: une image qui n\'est pas le chiffre majoritaire de son groupe{NB}; neuf images tirées au hasard par groupe</text>')
o.append("</svg>")
(OUT / "regrouper-sans-etiquettes.svg").write_text("\n".join(o) + "\n")
print("regrouper-sans-etiquettes.svg écrit", (OUT / "regrouper-sans-etiquettes.svg").stat().st_size // 1024, "Ko")
