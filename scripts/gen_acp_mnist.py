"""Module 2, « Trois façons d'apprendre » : les chiffres de MNIST réduits à deux nombres par l'analyse en composantes
principales (ACP), calculée sur les 60 000 images d'entraînement ; 2 000 images de test sont placées sur la carte.

MNIST est lu dans le cache de torchvision (~/.cache/inf1901/mnist), rempli par gen_espace_latent.py.

    uv run --with numpy python scripts/gen_acp_mnist.py
"""
from pathlib import Path
import numpy as np

RACINE = Path(__file__).resolve().parent
OUT = RACINE.parent / "static" / "images" / "module2"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#b8a888", "#fbf7ee")
COUL = ['#c4564a', '#3a6ea5', '#2f6f6a', '#9a5b33', '#7b5ea7', '#d18f2f', '#4f8f3a', '#b5487f', '#5b7d8a', '#8a7a2e']
NB = " "

brut = Path.home() / ".cache" / "inf1901" / "mnist" / "MNIST" / "raw"
lire = lambda f, off: np.frombuffer((brut / f).read_bytes(), np.uint8, offset=off)
X = lire("train-images-idx3-ubyte", 16).reshape(-1, 784) / 255
Xt = lire("t10k-images-idx3-ubyte", 16).reshape(-1, 784) / 255
Yt = lire("t10k-labels-idx1-ubyte", 8)
moy = X.mean(0)
val, vec = np.linalg.eigh(np.cov((X - moy).T))
ordre = np.argsort(val)[::-1]
val, vec = val[ordre], vec[:, ordre]
part = val[:2].sum() / val.sum()
rng = np.random.default_rng(0)
k = rng.choice(len(Xt), 2000, replace=False)
Z = (Xt[k] - moy) @ vec[:, :2]
lab = Yt[k]

W, H = 760, 560
C = 440                                                      # côté de la carte
x0, y0 = (W - C) / 2 - 40, 64
lo, hi = np.percentile(Z, 0.5, 0), np.percentile(Z, 99.5, 0)
marge = 0.06 * (hi - lo); lo, hi = lo - marge, hi + marge
vers = lambda z: (x0 + (z[0] - lo[0]) / (hi[0] - lo[0]) * C, y0 + C - (z[1] - lo[1]) / (hi[1] - lo[1]) * C)
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Les chiffres manuscrits réduits à deux nombres par l'ACP</title>",
     "<desc>Une carte en deux dimensions : 2 000 chiffres manuscrits de la base MNIST, chacun réduit de 784 pixels à deux nombres, ses "
     "positions le long des deux premières composantes principales. Chaque point est coloré selon le chiffre qu'il représente. Les 0 "
     "et les 1 occupent des régions assez distinctes, de part et d'autre de la carte ; les autres chiffres se chevauchent largement au "
     f"centre. Les deux composantes conservent environ {round(part * 100)} % de l'étalement des données.</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">2 000 chiffres manuscrits, de 784{NB}pixels à 2{NB}nombres</text>',
     f'<rect x="{x0}" y="{y0}" width="{C}" height="{C}" fill="{PANNEAU}" stroke="{BORD}"/>']
for i in rng.permutation(len(Z)):
    X_, Y_ = vers(Z[i])
    if x0 + 2 < X_ < x0 + C - 2 and y0 + 2 < Y_ < y0 + C - 2:
        o.append(f'<circle cx="{X_:.1f}" cy="{Y_:.1f}" r="2.3" fill="{COUL[lab[i]]}" fill-opacity="0.7"/>')
for c in range(10):
    X_, Y_ = vers(np.median(Z[lab == c], 0))
    X_ += {7: 14, 9: -14}.get(c, 0)                          # le 7 et le 9 tombent presque au même endroit
    o.append(f'<text x="{X_:.1f}" y="{Y_ + 10:.1f}" font-size="28" fill="{COUL[c]}" text-anchor="middle" font-weight="700" '
             f'stroke="{PANNEAU}" stroke-width="5" paint-order="stroke">{c}</text>')
o.append(f'<text x="{x0 + C / 2}" y="{y0 + C + 24}" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle">1re composante principale</text>')
o.append(f'<text x="{x0 - 14}" y="{y0 + C / 2}" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle" transform="rotate(-90 {x0 - 14} {y0 + C / 2})">2e composante principale</text>')
# légende
xl, yl = x0 + C + 30, y0 + 20
o.append(f'<text x="{xl}" y="{yl}" font-size="12" fill="{ENCRE}" font-weight="700">chiffre</text>')
for c in range(10):
    o.append(f'<circle cx="{xl + 6}" cy="{yl + 22 + c * 22}" r="5" fill="{COUL[c]}"/>')
    o.append(f'<text x="{xl + 18}" y="{yl + 26 + c * 22}" font-size="12" fill="{ENCRE}">{c}</text>')
o.append(f'<text x="{xl}" y="{yl + 266}" font-size="11" fill="{ENCRE_PALE}">étalement</text>')
o.append(f'<text x="{xl}" y="{yl + 280}" font-size="11" fill="{ENCRE_PALE}">conservé{NB}: {round(part * 100)}{NB}%</text>')
o.append("</svg>")
OUT.mkdir(exist_ok=True)
(OUT / "acp-mnist.svg").write_text("\n".join(o) + "\n")
print("acp-mnist.svg écrit ; part conservée", round(part, 3))
