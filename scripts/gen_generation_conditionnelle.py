# /// script
# requires-python = ">=3.10,<3.13"
# dependencies = ["torch", "torchvision", "numpy", "pillow"]
# ///
"""Module 4, « Quatre façons de générer » : la génération conditionnelle.

Entraîne un petit autoencodeur variationnel conditionnel (CVAE) sur MNIST : l'encodeur et le décodeur reçoivent, en plus
de l'image ou du code, l'étiquette du chiffre. Puis produit une grille : chaque rangée reçoit une étiquette (0 à 9),
chaque colonne le même tirage au hasard. La figure (SVG) place à gauche un schéma, à droite cette grille.

MNIST est lu dans ~/.cache/inf1901/mnist (téléchargé au besoin).

    uv run scripts/gen_generation_conditionnelle.py
"""
import base64, io
from pathlib import Path
import numpy as np
import torch
from torch import nn
from torchvision import datasets
from PIL import Image

torch.manual_seed(0)
RACINE = Path(__file__).resolve().parent
OUT = RACINE.parent / "static" / "images" / "module4"
CACHE = Path.home() / ".cache" / "inf1901" / "mnist"
dev = "mps" if torch.backends.mps.is_available() else "cpu"
LAT, COLS = 4, 7

train = datasets.MNIST(CACHE, train=True, download=True)
X = train.data.float().div(255).view(-1, 784).to(dev)
Y = nn.functional.one_hot(train.targets, 10).float().to(dev)


class CVAE(nn.Module):
    def __init__(self):
        super().__init__()
        self.enc = nn.Sequential(nn.Linear(794, 512), nn.ReLU(), nn.Linear(512, 256), nn.ReLU())
        self.mu, self.logvar = nn.Linear(256, LAT), nn.Linear(256, LAT)
        self.dec = nn.Sequential(nn.Linear(LAT + 10, 256), nn.ReLU(), nn.Linear(256, 512), nn.ReLU(), nn.Linear(512, 784))

    def forward(self, x, y):
        h = self.enc(torch.cat([x, y], 1))
        mu, logvar = self.mu(h), self.logvar(h)
        z = mu + torch.randn_like(mu) * (0.5 * logvar).exp()
        return self.dec(torch.cat([z, y], 1)), mu, logvar


m = CVAE().to(dev)
opt = torch.optim.Adam(m.parameters(), lr=1e-3)
for epoque in range(30):
    perm = torch.randperm(len(X), device=dev)
    total = 0.0
    for i in range(0, len(X), 128):
        k = perm[i:i + 128]
        logits, mu, logvar = m(X[k], Y[k])
        rec = nn.functional.binary_cross_entropy_with_logits(logits, X[k], reduction="sum")
        kl = -0.5 * (1 + logvar - mu ** 2 - logvar.exp()).sum()
        perte = (rec + kl) / len(k)
        opt.zero_grad(); perte.backward(); opt.step()
        total += perte.item() * len(k)
    print(f"époque {epoque + 1:2d} : perte {total / len(X):.1f}")

m = m.cpu().eval()
g = torch.Generator().manual_seed(3)
z = torch.randn(COLS, LAT, generator=g) * 0.9                  # un tirage par colonne, le même pour toutes les rangées
with torch.no_grad():
    rangees = [torch.sigmoid(m.dec(torch.cat([z, nn.functional.one_hot(torch.full((COLS,), c), 10).float()], 1))) for c in range(10)]

# ── la grille, en une seule image ──
T, E = 40, 4
grille = Image.new("RGB", (COLS * T + (COLS - 1) * E, 10 * T + 9 * E), (239, 231, 211))
f, e = np.array([251, 247, 238]), np.array([58, 53, 49])
for c, r in enumerate(rangees):
    for j in range(COLS):
        x = r[j].view(28, 28).numpy()
        im = Image.fromarray((f * (1 - x[..., None]) + e * x[..., None]).astype(np.uint8)).resize((T, T), Image.LANCZOS)
        grille.paste(im, (j * (T + E), c * (T + E)))
buf = io.BytesIO(); grille.save(buf, "PNG")
url = "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()

FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
GW, GH = grille.size
W, H = 800, 108 + GH + 70
gx, gy = W - 40 - GW, 108
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>La génération conditionnelle</title>",
     "<desc>Deux volets. À gauche, un schéma : deux entrées, le hasard (quelques nombres tirés) et une consigne (l'étiquette 7), "
     "entrent dans le générateur, qui produit un 7. À droite, une grille de chiffres produits par un vrai générateur conditionnel "
     "entraîné sur les chiffres de MNIST : dix rangées, une par étiquette de 0 à 9, et sept colonnes, une par tirage au hasard. "
     "Chaque rangée ne contient que le chiffre demandé. Dans chaque colonne, les dix chiffres partagent le même style : même "
     "inclinaison, même épaisseur de trait.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Générer sur demande{NB}: le hasard, plus une consigne</text>']


def fleche(x1, y1, x2, y2):
    o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')


# ── le schéma, à gauche ──
yc = gy + GH / 2
o.append(f'<rect x="30" y="{yc - 98}" width="140" height="46" rx="7" fill="{PANNEAU}" stroke="{BLEU}" stroke-width="1.6"/>')
o.append(f'<text x="100" y="{yc - 79}" font-size="12" fill="{ENCRE}" text-anchor="middle" font-weight="700">le hasard</text>')
o.append(f'<text x="100" y="{yc - 63}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">quelques nombres tirés</text>')
o.append(f'<rect x="30" y="{yc + 52}" width="140" height="46" rx="7" fill="{PANNEAU}" stroke="{ROUGE}" stroke-width="1.6"/>')
o.append(f'<text x="100" y="{yc + 71}" font-size="12" fill="{ROUGE}" text-anchor="middle" font-weight="700">la consigne</text>')
o.append(f'<text x="100" y="{yc + 87}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">«{NB}un 7{NB}»</text>')
o.append(f'<rect x="200" y="{yc - 30}" width="104" height="60" rx="8" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="1.8"/>')
o.append(f'<text x="252" y="{yc + 5}" font-size="12.5" fill="{ENCRE}" text-anchor="middle" font-weight="700">générateur</text>')
fleche(172, yc - 70, 198, yc - 14)
fleche(172, yc + 70, 198, yc + 14)
c7 = rangees[7][0].view(28, 28).numpy()
im7 = Image.fromarray((f * (1 - c7[..., None]) + e * c7[..., None]).astype(np.uint8)).resize((60, 60), Image.LANCZOS)
b = io.BytesIO(); im7.save(b, "PNG")
fleche(306, yc, 326, yc)
o.append(f'<image x="330" y="{yc - 30}" width="60" height="60" xlink:href="data:image/png;base64,{base64.b64encode(b.getvalue()).decode()}"/>')
o.append(f'<rect x="330" y="{yc - 30}" width="60" height="60" fill="none" stroke="{BORD}" stroke-width="1.5"/>')
o.append(f'<text x="210" y="{yc + 136}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">la consigne décide quel chiffre{NB};</text>')
o.append(f'<text x="210" y="{yc + 151}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">le hasard décide comment il est écrit</text>')

# ── la grille, à droite ──
o.append(f'<image x="{gx}" y="{gy}" width="{GW}" height="{GH}" xlink:href="{url}"/>')
o.append(f'<text x="{gx + GW / 2}" y="{gy - 30}" font-size="12" fill="{BLEU}" text-anchor="middle" font-weight="700">le même tirage dans chaque colonne →</text>')
for c in range(10):
    o.append(f'<text x="{gx - 12}" y="{gy + c * (T + E) + T / 2 + 5}" font-size="13" fill="{ROUGE}" text-anchor="end" font-weight="700">«{NB}{c}{NB}»</text>')
o.append(f'<text x="{gx - 12}" y="{gy - 12}" font-size="11" fill="{ROUGE}" text-anchor="end" font-weight="700">consigne</text>')
o.append(f'<text x="{W - 40}" y="{gy + GH + 24}" font-size="11" fill="{ENCRE_PALE}" text-anchor="end">un vrai générateur conditionnel, entraîné sur les chiffres de MNIST</text>')
o.append("</svg>")
(OUT / "generation-conditionnelle.svg").write_text("\n".join(o) + "\n")
print("generation-conditionnelle.svg écrit", W, H)
