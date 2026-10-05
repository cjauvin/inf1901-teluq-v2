"""Module 4, « Générer » : la variété des vraies images (une feuille enroulée dans l'espace des pixels) et l'espace
latent (la même feuille déroulée à plat), reliés par le décodeur et l'encodeur.

Les points sont de vrais chiffres de MNIST, placés selon leurs coordonnées dans l'espace latent à deux dimensions de
l'autoencodeur variationnel de l'applet (static/html/applets/data/espace-latent.json) ; la feuille enroulée est un
dessin, l'espace des pixels réel ayant 784 dimensions.

    uv run --with numpy --with pillow python scripts/gen_variete.py
"""
import base64, io, json, math
from pathlib import Path
import numpy as np
from PIL import Image

RACINE = Path(__file__).resolve().parent
OUT = RACINE.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
COUL = ['#c4564a', '#3a6ea5', '#2f6f6a', '#9a5b33', '#7b5ea7', '#d18f2f', '#4f8f3a', '#b5487f', '#5b7d8a', '#8a7a2e']
NB = " "

d = json.loads((RACINE.parent / "static" / "html" / "applets" / "data" / "espace-latent.json").read_text())
pts = np.array([p[:2] for p in d["points"]]); lab = np.array([p[2] for p in d["points"]]); idx = np.array(d["indices"])
lo, hi = -2.8, 2.8
# coordonnées sur la feuille, entre 0 et 1 : le VAE range ses points selon une loi normale centrée réduite, que sa
# fonction de répartition étale uniformément sur le carré (les voisins restent voisins)
from math import erf
uv = np.clip(np.vectorize(lambda z: 0.5 * (1 + erf(z / math.sqrt(2))))(pts), 0.04, 0.96)
garde = (np.abs(pts) < 1.7).all(1)
rng = np.random.default_rng(3)
nuage = rng.choice(np.where(garde)[0], 420, replace=False)
vignettes = []                                               # pour chaque chiffre, le point le plus proche de sa médiane
for c in range(10):
    k = np.where((lab == c) & garde)[0]
    med = np.median(pts[k], 0)
    vignettes.append(k[np.argmin(((pts[k] - med) ** 2).sum(1))])
cache = Path.home() / ".cache" / "inf1901" / "mnist" / "MNIST" / "raw"
imgs = np.frombuffer((cache / "t10k-images-idx3-ubyte").read_bytes(), np.uint8, offset=16).reshape(-1, 28, 28)


def png(k, coul):                                            # le chiffre, à l'encre de sa couleur, sur fond transparent
    r, g, b = (int(coul[i:i + 2], 16) for i in (1, 3, 5))
    a = imgs[idx[k]]
    rgba = np.zeros((28, 28, 4), np.uint8); rgba[..., 0], rgba[..., 1], rgba[..., 2], rgba[..., 3] = r, g, b, a
    buf = io.BytesIO(); Image.fromarray(rgba).save(buf, "PNG")
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


W, H = 760, 400
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>La variété et l'espace latent</title>",
     "<desc>Deux panneaux. À gauche, l'espace des pixels, dessiné en trois dimensions : une feuille enroulée sur elle-même comme un "
     "parchemin, sur laquelle sont posés de vrais chiffres manuscrits, de petits points de couleur, un par chiffre, et dix chiffres "
     "dessinés, de 0 à 9. C'est la variété des vraies images. À droite, l'espace latent : la même feuille déroulée à plat, un carré où "
     "les mêmes chiffres occupent les mêmes places, chaque chiffre dans sa région. Une flèche va du carré vers la feuille enroulée : "
     "le décodeur. Une autre va de la feuille vers le carré : l'encodeur.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">La variété appartient aux données, l\'espace latent au modèle</text>']
# panneaux
PG, PD = (20, 52, 390, 330), (500, 52, 240, 330)            # x, y, largeur, hauteur
for x, y, w, h in (PG, PD):
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
o.append(f'<text x="{PG[0] + PG[2] / 2}" y="{PG[1] + 24}" font-size="13" fill="{BRUN}" text-anchor="middle" font-weight="700">L\'espace des pixels (784{NB}dimensions)</text>')
o.append(f'<text x="{PD[0] + PD[2] / 2}" y="{PD[1] + 24}" font-size="13" fill="{BRUN}" text-anchor="middle" font-weight="700">L\'espace latent (2{NB}dimensions)</text>')

# ── la feuille enroulée : u le long de la spirale, v le long de l'axe ──
T0, T1, LONG = 1.5 * math.pi, 4.2 * math.pi, 16.0
PSI, PHI = math.radians(38), math.radians(18)              # rotation autour de la verticale, puis inclinaison


def brut(u, v):
    t = T0 + u * (T1 - T0)
    X, Y, Z = t * math.cos(t), t * math.sin(t), (v - 0.5) * LONG   # Z : l'axe du rouleau, vers l'observateur
    X, Z = X * math.cos(PSI) + Z * math.sin(PSI), -X * math.sin(PSI) + Z * math.cos(PSI)
    Y, Z = Y * math.cos(PHI) - Z * math.sin(PHI), Y * math.sin(PHI) + Z * math.cos(PHI)
    return X, -Y, -Z                                          # écran, et profondeur (grand = loin)


_g = np.array([brut(u, v)[:2] for u in np.linspace(0, 1, 60) for v in (0, 1)])
_zone = (PG[0] + 24, PG[1] + 40, PG[0] + PG[2] - 24, PG[1] + PG[3] - 60)
S = min((_zone[2] - _zone[0]) / np.ptp(_g[:, 0]), (_zone[3] - _zone[1]) / np.ptp(_g[:, 1]))
CX = (_zone[0] + _zone[2]) / 2 - S * (_g[:, 0].min() + _g[:, 0].max()) / 2
CY = (_zone[1] + _zone[3]) / 2 - S * (_g[:, 1].min() + _g[:, 1].max()) / 2


def roule(u, v):
    X, Y, prof = brut(u, v)
    return CX + S * X, CY + S * Y, prof


objets = []                                                   # (profondeur, svg), dessinés du plus loin au plus près
NU, NV = 120, 8
for i in range(NU):
    for j in range(NV):
        u0, u1, v0, v1 = i / NU, (i + 1) / NU, j / NV, (j + 1) / NV
        q = [roule(u0, v0), roule(u1, v0), roule(u1, v1), roule(u0, v1)]
        prof = sum(p[2] for p in q) / 4
        teinte = 0.80 + 0.14 * math.cos(T0 + (u0 + u1) / 2 * (T1 - T0) - 0.8)   # face éclairée ou dans l'ombre
        c = tuple(int(v * teinte) for v in (251, 244, 228))
        bord = "#c9b994" if j in (0, NV - 1) or i in (0, NU - 1) else f"rgb{c}"
        chemin = " ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in q)
        objets.append((prof, f'<polygon points="{chemin}" fill="rgb{c}" stroke="rgb{c}" stroke-width="0.6"/>'))
# bords de la feuille, pour la lisibilité
for j in (0, NV):
    for i in range(NU):
        a, b = roule(i / NU, j / NV), roule((i + 1) / NU, j / NV)
        objets.append(((a[2] + b[2]) / 2 - 0.01, f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#b9a77f" stroke-width="1.2"/>'))
for k in nuage:
    X, Y, prof = roule(*uv[k])
    objets.append((prof - 0.4, f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="2.2" fill="{COUL[lab[k]]}" fill-opacity="0.85"/>'))
for k in vignettes:
    X, Y, prof = roule(*uv[k])
    objets.append((prof - 0.5, f'<image x="{X - 12:.1f}" y="{Y - 12:.1f}" width="24" height="24" xlink:href="{png(k, COUL[lab[k]])}"/>'))
for _, s in sorted(objets, key=lambda e: -e[0]):
    o.append(s)
o.append(f'<text x="{PG[0] + PG[2] / 2}" y="{PG[1] + PG[3] - 34}" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">les vraies images se trouvent près d\'une feuille</text>')
o.append(f'<text x="{PG[0] + PG[2] / 2}" y="{PG[1] + PG[3] - 18}" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">repliée sur elle-même{NB}: la <tspan font-weight="700" fill="{TEAL}">variété</tspan></text>')

# ── la carte plane ──
C = 190
mx, my = PD[0] + (PD[2] - C) / 2, PD[1] + 52
o.append(f'<rect x="{mx}" y="{my}" width="{C}" height="{C}" fill="rgb(242,234,214)" stroke="#b9a77f" stroke-width="1.2"/>')
for k in nuage:
    u, v = uv[k]
    o.append(f'<circle cx="{mx + u * C:.1f}" cy="{my + (1 - v) * C:.1f}" r="1.9" fill="{COUL[lab[k]]}" fill-opacity="0.75"/>')
for k in vignettes:
    u, v = uv[k]
    o.append(f'<image x="{mx + u * C - 12:.1f}" y="{my + (1 - v) * C - 12:.1f}" width="24" height="24" xlink:href="{png(k, COUL[lab[k]])}"/>')
o.append(f'<text x="{PD[0] + PD[2] / 2}" y="{PD[1] + PD[3] - 34}" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">la même feuille, déroulée{NB}:</text>')
o.append(f'<text x="{PD[0] + PD[2] / 2}" y="{PD[1] + PD[3] - 18}" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">une carte plane, faite par le modèle</text>')

# ── décodeur et encodeur ──
xa, xb = PG[0] + PG[2] + 8, PD[0] - 8
ym = PD[1] + PD[3] / 2
o.append(f'<line x1="{xb}" y1="{ym - 30}" x2="{xa}" y2="{ym - 30}" stroke="{GRIS}" stroke-width="1.8" marker-end="url(#p)"/>')
o.append(f'<text x="{(xa + xb) / 2}" y="{ym - 40}" font-size="11.5" fill="{ENCRE}" text-anchor="middle" font-weight="600">décodeur</text>')
o.append(f'<line x1="{xa}" y1="{ym + 30}" x2="{xb}" y2="{ym + 30}" stroke="{GRIS}" stroke-width="1.8" marker-end="url(#p)"/>')
o.append(f'<text x="{(xa + xb) / 2}" y="{ym + 50}" font-size="11.5" fill="{ENCRE}" text-anchor="middle" font-weight="600">encodeur</text>')
o.append("</svg>")
(OUT / "variete-espace-latent.svg").write_text("\n".join(o) + "\n")
print("variete-espace-latent.svg écrit")
