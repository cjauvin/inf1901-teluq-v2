# /// script
# requires-python = ">=3.10"
# ///
"""Module 4, « Passer à l'échelle » : la distillation (Hinton, Vinyals et Dean, 2015). Le même 2 manuscrit, deux
façons de l'enseigner. À gauche, l'étiquette seule : toute la probabilité sur le 2. À droite, la réponse d'un grand
réseau, le professeur : surtout 2, mais un peu de 3 et de 7, ce qui dit à quoi ce 2 ressemble. L'élève apprend à
reproduire la distribution de droite. Valeurs schématiques."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4" / "distillation.svg"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "

W, H = 920, 450
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>La distillation</title>",
     "<desc>Deux panneaux, avec le même chiffre 2 manuscrit, À gauche, "
     "l'étiquette seule : un diagramme en barres sur les dix chiffres, avec une seule barre, toute la probabilité sur le 2. "
     "À droite, la réponse d'un grand réseau, le professeur : la barre du 2 domine, avec 0,80, mais le 3 reçoit 0,12 et "
     "le 7, 0,05, les autres chiffres presque rien. En bas : l'élève, un réseau plus petit, apprend à reproduire la "
     "distribution de droite, et y apprend aussi que ce 2 ressemble un peu à un 3.</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Ce que le professeur sait de plus que l\'étiquette</text>']


def texte(x, y, t, taille=10.5, coul=ENCRE, ancre="middle", gras=False, ital=False):
    g = ' font-weight="700"' if gras else ""
    i = ' font-style="italic"' if ital else ""
    o.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{taille}" fill="{coul}" text-anchor="{ancre}"{g}{i}>{t}</text>')


def deux(x, y):
    """Un 2 manuscrit dans une case de 84 px, coin supérieur gauche (x, y)."""
    o.append(f'<rect x="{x}" y="{y}" width="84" height="84" rx="4" fill="{ENCRE}"/>')
    o.append(f'<path d="M{x + 24} {y + 32} C{x + 24} {y + 12} {x + 60} {y + 12} {x + 60} {y + 32} '
             f'C{x + 60} {y + 46} {x + 40} {y + 56} {x + 22} {y + 68} L{x + 64} {y + 68}" '
             f'fill="none" stroke="#ffffff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>')


def barres(x0, base, valeurs, coul, etiquettes):
    hmax, pas, larg = 130, 36, 24
    o.append(f'<line x1="{x0 - 8}" y1="{base}" x2="{x0 + 10 * pas - 4}" y2="{base}" stroke="{AXE}" stroke-width="1.2"/>')
    for k, v in enumerate(valeurs):
        x = x0 + k * pas
        h = max(v * hmax, 1.5)
        c = coul if v >= 0.04 else AXE
        o.append(f'<rect x="{x}" y="{base - h:.1f}" width="{larg}" height="{h:.1f}" rx="2" fill="{c}" fill-opacity="0.85"/>')
        texte(x + larg / 2, base + 16, str(k), 11, ENCRE_PALE)
        if k in etiquettes:
            texte(x + larg / 2, base - h - 7, etiquettes[k], 10.5, c, gras=True)


for x0, titre, l1, l2, coul, vals, etq in (
        (20, "L'étiquette seule", "une seule information :", "« c'est un 2 »", GRIS,
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], {2: "1"}),
        (470, "La réponse du professeur", "un grand réseau entraîné répond", "par une probabilité par chiffre", TEAL,
         [0.003, 0.004, 0.80, 0.12, 0.003, 0.004, 0.003, 0.05, 0.008, 0.005],
         {2: "0,80", 3: "0,12", 7: "0,05"})):
    o.append(f'<rect x="{x0}" y="50" width="430" height="330" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
    texte(x0 + 215, 76, titre, 12.5, coul, gras=True)
    deux(x0 + 40, 88)
    texte(x0 + 146, 128, l1, 10.5, ENCRE_PALE, "start")
    texte(x0 + 146, 144, l2, 10.5, ENCRE_PALE, "start", ital=(x0 == 20))
    barres(x0 + 40, 336, vals, coul, etq)

texte(W / 2, 408, "L'élève, un réseau plus petit, apprend à reproduire la distribution de droite :", 11.5, ENCRE, ital=True)
texte(W / 2, 426, "il y apprend aussi que ce 2 ressemble un peu à un 3, et un peu à un 7.", 11.5, ENCRE, ital=True)
texte(W - 34, 370, "valeurs schématiques", 9.5, GRIS, "end", ital=True)
o.append("</svg>")
OUT.write_text("\n".join(o) + "\n")
print(OUT.name, "écrit")
