"""Module 4, « Générer : imiter une distribution » : le portrait des maisons, et des maisons tirées dedans.

Plan distance × année du jeu canonique (gen_maisons.py). Le « relief » est une estimation par noyaux
(une petite cloche autour de chaque maison, additionnées), dessinée en bandes de densité. Les maisons
nouvelles sont tirées exactement de ce portrait : on choisit une maison au hasard, puis on la déplace
d'un écart tiré dans sa cloche.
"""
import math
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_maisons import BRUN, ENCRE, ENCRE_PALE, FOND, MAISONS, TEAL, entete, points  # noqa: E402
from gen_maisons import pa, pd  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
NB = " "
SIGMA = 30.0                                   # largeur des cloches, en pixels
CENTRES = [(pd(m[2]), pa(m[1])) for m in MAISONS]


def densite(x, y):
    return sum(math.exp(-((x - cx) ** 2 + (y - cy) ** 2) / (2 * SIGMA ** 2)) for cx, cy in CENTRES)


H = 450
x0, x1, y0, y1, pas = 80, 630, 40, 380, 4
grille = [[densite(x + pas / 2, y + pas / 2) for x in range(x0, x1, pas)] for y in range(y0, y1, pas)]
dmax = max(max(r) for r in grille)
SEUILS = [0.12, 0.3, 0.5, 0.72]               # fractions du maximum : quatre bandes de plus en plus foncées
bandes = []
for j, rangee in enumerate(grille):
    niveaux = [sum(v / dmax >= s for s in SEUILS) for v in rangee]
    i = 0
    while i < len(niveaux):                    # fusionne les cases voisines de même niveau
        k = i
        while k < len(niveaux) and niveaux[k] == niveaux[i]:
            k += 1
        if niveaux[i]:
            bandes.append(f'<rect x="{x0 + i * pas}" y="{y0 + j * pas}" width="{(k - i) * pas}" height="{pas}" '
                          f'fill="{TEAL}" fill-opacity="{0.085 * niveaux[i]:.3f}"/>')
        i = k

rnd = random.Random(7)
nouvelles = []
while len(nouvelles) < 10:
    cx, cy = rnd.choice(CENTRES)
    x, y = rnd.gauss(cx, SIGMA), rnd.gauss(cy, SIGMA)
    libre = all((x - a) ** 2 + (y - b) ** 2 > 16 ** 2 for a, b in CENTRES + nouvelles)   # lisibilité : pas de chevauchement
    if x0 + 8 < x < x1 - 8 and y0 + 8 < y < y1 - 8 and libre:
        nouvelles.append((x, y))

desc = ("Le plan distance du centre × année de construction. Les vingt maisons du Module 2 forment deux amas, "
        "proches et récentes en haut à gauche, éloignées et anciennes en bas à droite. Autour d'elles, des bandes "
        "de plus en plus foncées dessinent le relief du portrait : deux collines, une par amas. Dix maisons nouvelles, "
        "dessinées en anneaux bruns, sont tirées de ce portrait ; elles tombent presque toutes sur les collines, "
        "et aucune n'est la copie d'une maison existante.")
o = [entete(H, "Le portrait des maisons, et des maisons tirées dedans", desc, plan="annee")]
o.append("\n".join(bandes))
o.append(points(TEAL, 6.5, plan="annee"))
o.append(f'<g fill="none" stroke="{BRUN}" stroke-width="3">' +
         "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7"/>' for x, y in nouvelles) + "</g>")
# légende, en haut à droite, dans la zone vide du plan
lx, ly = 420, 62
o.append(f'<rect x="{lx - 14}" y="{ly - 20}" width="210" height="96" rx="8" fill="{FOND}" fill-opacity="0.92"/>')
o.append(f'<circle cx="{lx}" cy="{ly}" r="6.5" fill="{TEAL}" stroke="{FOND}" stroke-width="1.5"/>')
o.append(f'<text x="{lx + 16}" y="{ly + 4.5}" font-size="13" fill="{ENCRE}">les vingt maisons connues</text>')
o.append(f'<rect x="{lx - 7}" y="{ly + 22}" width="14" height="14" fill="{TEAL}" fill-opacity="0.24"/>')
o.append(f'<text x="{lx + 16}" y="{ly + 33.5}" font-size="13" fill="{ENCRE}">le relief du portrait</text>')
o.append(f'<circle cx="{lx}" cy="{ly + 58}" r="7" fill="none" stroke="{BRUN}" stroke-width="3"/>')
o.append(f'<text x="{lx + 16}" y="{ly + 62.5}" font-size="13" fill="{ENCRE}">dix maisons tirées au hasard</text>')
o.append("</svg>")
(OUT / "portrait-maisons.svg").write_text("\n".join(o) + "\n")
print("portrait-maisons.svg écrit,", len(bandes), "bandes")
