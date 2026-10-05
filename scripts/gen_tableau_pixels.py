"""Module 3, accueil : mélanger les colonnes d'un tableau, ou les pixels d'une image.

À gauche, les quatre maisons des tables du Module 2 (jeu canonique de gen_maisons.py), puis le même tableau avec
ses colonnes dans un autre ordre. À droite, le premier 0 du jeu de test de MNIST (cache de gen_espace_latent.py),
puis les mêmes 784 pixels mélangés au hasard.

    uv run --with numpy python scripts/gen_tableau_pixels.py
"""
import random
import sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_maisons import MAISONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module3"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "
cache = Path.home() / ".cache" / "inf1901" / "mnist" / "MNIST" / "raw"
imgs = np.frombuffer((cache / "t10k-images-idx3-ubyte").read_bytes(), np.uint8, offset=16).reshape(-1, 28, 28)
etiq = np.frombuffer((cache / "t10k-labels-idx1-ubyte").read_bytes(), np.uint8, offset=8)
zero = imgs[int(np.argmax(etiq == 0))] / 255
melange = zero.flatten().copy()
random.Random(4).shuffle(melange)
melange = melange.reshape(28, 28)

maisons = [m for m in MAISONS if (m[0], m[1]) in {(130, 1972), (150, 1980), (180, 1995), (220, 2010)}]
COLS = [("superficie (m²)", 0), ("année", 1), ("distance (km)", 2), ("prix (k$)", 3)]
ORDRE = [3, 2, 0, 1]                                   # le même tableau, colonnes réordonnées

W, H = 760, 470
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Mélanger un tableau, mélanger une image</title>",
     "<desc>Deux colonnes. À gauche, un tableau de quatre maisons, avec leur superficie, leur année de construction, leur distance "
     "au centre et leur prix ; en dessous, le même tableau avec ses colonnes dans un autre ordre : l'information est intacte. À droite, "
     "un zéro écrit à la main, de 28 pixels sur 28 ; en dessous, les mêmes 784 pixels mélangés au hasard : on ne voit plus qu'une "
     "neige grise, et le chiffre a disparu, alors qu'aucun pixel n'a changé de valeur.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<rect x="20" y="20" width="420" height="{H - 40}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>',
     f'<rect x="460" y="20" width="280" height="{H - 40}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>',
     f'<text x="230" y="48" font-size="14.5" fill="{TEAL}" text-anchor="middle" font-weight="700">Un tableau</text>',
     f'<text x="600" y="48" font-size="14.5" fill="{TEAL}" text-anchor="middle" font-weight="700">Une image</text>']


def tableau(y0, ordre):
    lc, hl, x0 = 96, 26, 38
    for j, c in enumerate(ordre):
        x = x0 + j * lc
        o.append(f'<rect x="{x}" y="{y0}" width="{lc}" height="{hl}" fill="{FOND}" stroke="{AXE}" stroke-width="0.8"/>')
        o.append(f'<text x="{x + lc / 2}" y="{y0 + 17}" font-size="11.5" fill="{ENCRE}" text-anchor="middle" font-weight="600">{COLS[c][0]}</text>')
        for i, m in enumerate(maisons):
            y = y0 + hl * (i + 1)
            o.append(f'<rect x="{x}" y="{y}" width="{lc}" height="{hl}" fill="{PANNEAU}" stroke="{AXE}" stroke-width="0.8"/>')
            o.append(f'<text x="{x + lc / 2}" y="{y + 17}" font-size="12" fill="{ENCRE}" text-anchor="middle">{m[COLS[c][1]]}</text>')


def grille(img, x0, y0, c=5):
    o.append(f'<rect x="{x0}" y="{y0}" width="{28 * c}" height="{28 * c}" fill="#ffffff" stroke="{AXE}"/>')
    for i in range(28):
        for j in range(28):
            if img[i, j] > 0.02:
                o.append(f'<rect x="{x0 + j * c}" y="{y0 + i * c}" width="{c + 0.15:.2f}" height="{c + 0.15:.2f}" fill="{ENCRE}" fill-opacity="{img[i, j]:.2f}"/>')


tableau(66, [0, 1, 2, 3])
o.append(f'<line x1="230" y1="206" x2="230" y2="246" stroke="{GRIS}" stroke-width="2" marker-end="url(#p)"/>')
o.append(f'<text x="244" y="231" font-size="12" fill="{ENCRE_PALE}">mélanger les colonnes</text>')
tableau(254, ORDRE)
o.append(f'<text x="230" y="{H - 52}" font-size="13" fill="{TEAL}" text-anchor="middle" font-weight="700">Rien n\'est perdu{NB}: chaque colonne</text>')
o.append(f'<text x="230" y="{H - 34}" font-size="13" fill="{TEAL}" text-anchor="middle" font-weight="700">garde son nom et son sens.</text>')
grille(zero, 530, 62)
o.append(f'<line x1="600" y1="206" x2="600" y2="246" stroke="{GRIS}" stroke-width="2" marker-end="url(#p)"/>')
o.append(f'<text x="614" y="231" font-size="12" fill="{ENCRE_PALE}">mélanger les pixels</text>')
grille(melange, 530, 254)
o.append(f'<text x="600" y="{H - 52}" font-size="13" fill="{ROUGE}" text-anchor="middle" font-weight="700">Le chiffre a disparu, alors que</text>')
o.append(f'<text x="600" y="{H - 34}" font-size="13" fill="{ROUGE}" text-anchor="middle" font-weight="700">les 784 valeurs sont toujours là.</text>')
o.append("</svg>")
(OUT / "tableau-ou-pixels.svg").write_text("\n".join(o) + "\n")
print("tableau-ou-pixels.svg écrit")
