"""Module 3, « L'apprentissage profond » : le dropout, à trois étapes de l'entraînement, puis à l'utilisation."""
import random
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module3"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
COUCHES = [4, 6, 6, 3]
W, H = 760, 330
lp, e, x0, y0, hp = 170, 12, 20, 56, 214
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Le dropout</title>",
     "<desc>Quatre fois le même réseau, de quatre couches. Dans les trois premiers panneaux, trois étapes successives de "
     "l'entraînement : à chaque étape, environ la moitié des neurones des couches cachées, tirés au hasard, sont éteints, marqués "
     "d'une croix, et leurs connexions disparaissent ; ce ne sont pas les mêmes neurones d'une étape à l'autre. Dans le quatrième "
     "panneau, à l'utilisation, tous les neurones et toutes les connexions sont présents.</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Le dropout{NB}: éteindre des neurones au hasard, à chaque étape</text>']
rnd = random.Random(11)


def reseau(px, titre, sous, eteints, coul_titre):
    o.append(f'<rect x="{px}" y="{y0}" width="{lp}" height="{hp + 46}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
    pos = []
    for c, n in enumerate(COUCHES):
        x = px + 24 + c * (lp - 48) / (len(COUCHES) - 1)
        pos.append([(x, y0 + 26 + (k + 0.5) * (hp - 36) / n) for k in range(n)])
    for c in range(len(COUCHES) - 1):
        for a, pa in enumerate(pos[c]):
            for b, pb in enumerate(pos[c + 1]):
                if (c, a) in eteints or (c + 1, b) in eteints:
                    continue
                o.append(f'<line x1="{pa[0]:.1f}" y1="{pa[1]:.1f}" x2="{pb[0]:.1f}" y2="{pb[1]:.1f}" stroke="{AXE}" stroke-width="0.9"/>')
    for c, couche in enumerate(pos):
        for k, (x, y) in enumerate(couche):
            if (c, k) in eteints:
                o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{FOND}" stroke="{AXE}" stroke-width="1.4" stroke-dasharray="2 2"/>')
                o.append(f'<path d="M{x - 4:.1f} {y - 4:.1f} L{x + 4:.1f} {y + 4:.1f} M{x + 4:.1f} {y - 4:.1f} L{x - 4:.1f} {y + 4:.1f}" stroke="{ROUGE}" stroke-width="1.8"/>')
            else:
                coul = BLEU if c in (0, len(COUCHES) - 1) else TEAL
                o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{coul}" stroke="{FOND}" stroke-width="1.5"/>')
    o.append(f'<text x="{px + lp / 2}" y="{y0 + hp + 18}" font-size="13" fill="{coul_titre}" text-anchor="middle" font-weight="700">{titre}</text>')
    o.append(f'<text x="{px + lp / 2}" y="{y0 + hp + 36}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">{sous}</text>')


for k in range(3):
    eteints = {(c, n) for c in (1, 2) for n in rnd.sample(range(COUCHES[c]), COUCHES[c] // 2)}
    reseau(x0 + k * (lp + e), f"Entraînement, étape {k + 1}", "des neurones éteints au hasard", eteints, BRUN)
reseau(x0 + 3 * (lp + e) + 10, "À l'utilisation", "tous les neurones", set(), TEAL)
o.append(f'<line x1="{x0 + 3 * (lp + e) + 2}" y1="{y0 + 10}" x2="{x0 + 3 * (lp + e) + 2}" y2="{y0 + hp + 36}" stroke="{AXE}" stroke-width="1.4" stroke-dasharray="5 4"/>')
o.append("</svg>")
(OUT / "dropout.svg").write_text("\n".join(o) + "\n")
print("dropout.svg écrit")
