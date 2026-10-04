"""Module 4, « Générer : imiter une distribution » : 784 pixels au hasard, et un vrai chiffre.

Le chiffre vient du jeu de test de MNIST, téléchargé par gen_espace_latent.py dans
~/.cache/inf1901/mnist (à lancer d'abord).
"""
import random
from pathlib import Path
import numpy as np

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, TEAL, PANNEAU = "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#2f6f6a", "#fbf7ee"
NB = " "
brut = (Path.home() / ".cache" / "inf1901" / "mnist" / "MNIST" / "raw" / "t10k-images-idx3-ubyte").read_bytes()
images = np.frombuffer(brut, np.uint8, offset=16).reshape(-1, 28, 28)
chiffre = images[0] / 255                       # le premier chiffre du jeu de test (un 7)
rnd = random.Random(3)
bruit = np.array([[rnd.random() for _ in range(28)] for _ in range(28)])

W, H, c = 660, 330, 7.5


def grille(img, x0, y0):
    o = [f'<rect x="{x0}" y="{y0}" width="{28 * c}" height="{28 * c}" fill="{PANNEAU}" stroke="{BORD}"/>']
    for i in range(28):
        for j in range(28):
            v = img[i, j]
            if v > 0.02:
                o.append(f'<rect x="{x0 + j * c:.1f}" y="{y0 + i * c:.1f}" width="{c + 0.2:.1f}" height="{c + 0.2:.1f}" '
                         f'fill="{ENCRE}" fill-opacity="{v:.2f}"/>')
    return "\n".join(o)


o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Du bruit, ou un chiffre</title>",
     "<desc>Deux grilles de 28 sur 28 pixels. À gauche, chaque pixel a reçu une teinte de gris tirée au hasard : on ne voit "
     "qu'une neige uniforme. À droite, un vrai chiffre manuscrit, un 7 : quelques pixels foncés forment un trait, tous "
     "les autres sont blancs.</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     grille(bruit, 75, 40), grille(chiffre, 375, 40),
     f'<text x="{75 + 14 * c}" y="{40 + 28 * c + 32}" font-size="14" fill="{TEAL}" text-anchor="middle" font-weight="700">784 pixels tirés au hasard</text>',
     f'<text x="{375 + 14 * c}" y="{40 + 28 * c + 32}" font-size="14" fill="{TEAL}" text-anchor="middle" font-weight="700">un vrai chiffre manuscrit</text>',
     f'<text x="{W / 2}" y="{H - 16}" font-size="12.5" fill="{ENCRE_PALE}" text-anchor="middle">Les deux sont des points du même espace de 784{NB}dimensions.</text>',
     "</svg>"]
(OUT / "bruit-ou-chiffre.svg").write_text("\n".join(o) + "\n")
print("bruit-ou-chiffre.svg écrit")
