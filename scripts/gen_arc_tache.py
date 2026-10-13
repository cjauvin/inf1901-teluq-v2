"""Module 4, « Le défi ARC » : une vraie tâche du corpus ARC (0ca9ddb6, jeu d'entraînement, licence Apache 2.0). Trois
exemples, entrée et sortie, puis une entrée de test dont la sortie est à trouver. La règle n'est écrite nulle part : chaque
case rouge reçoit quatre voisines jaunes en diagonale, chaque case bleue quatre voisines orange en croix, et les autres
couleurs ne changent pas."""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
ARC = ["#000000", "#0074D9", "#FF4136", "#2ECC40", "#FFDC00", "#AAAAAA", "#F012BE", "#FF851B", "#7FDBFF", "#870C25"]
TACHE = json.loads('{"train":[{"input":[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,2,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],"output":[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,4,0,4,0,0,0,0,0],[0,0,2,0,0,0,0,0,0],[0,4,0,4,0,0,0,0,0],[0,0,0,0,0,0,7,0,0],[0,0,0,0,0,7,1,7,0],[0,0,0,0,0,0,7,0,0],[0,0,0,0,0,0,0,0,0]]},{"input":[[0,0,0,8,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,2,0,0],[0,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0],[0,2,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],"output":[[0,0,0,8,0,0,0,0,0],[0,0,0,0,0,4,0,4,0],[0,0,7,0,0,0,2,0,0],[0,7,1,7,0,4,0,4,0],[0,0,7,0,0,0,0,0,0],[0,0,0,0,0,0,7,0,0],[4,0,4,0,0,7,1,7,0],[0,2,0,0,0,0,7,0,0],[4,0,4,0,0,0,0,0,0]]},{"input":[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,2,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,6,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],"output":[[0,0,0,0,0,0,0,0,0],[0,4,0,4,0,0,0,0,0],[0,0,2,0,0,0,0,0,0],[0,4,0,4,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,6,0,0],[0,0,0,7,0,0,0,0,0],[0,0,7,1,7,0,0,0,0],[0,0,0,7,0,0,0,0,0]]}],"test":[{"input":[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0],[0,0,2,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,8,0,0,0],[0,0,0,0,0,0,0,0,0],[0,6,0,0,0,0,0,2,0],[0,0,0,0,0,0,0,0,0]],"output":[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,7,0,0],[0,4,0,4,0,7,1,7,0],[0,0,2,0,0,0,7,0,0],[0,4,0,4,0,0,0,0,0],[0,0,0,0,0,8,0,0,0],[0,0,0,0,0,0,4,0,4],[0,6,0,0,0,0,0,2,0],[0,0,0,0,0,0,4,0,4]]}]}')
W, H = 840, 284
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Une tâche ARC</title>",
     "<desc>Une vraie tâche du corpus ARC. Trois exemples, chacun formé d'une grille d'entrée et d'une grille de sortie de neuf "
     "cases sur neuf, sur fond noir. Dans les entrées, quelques cases isolées de couleur : rouge, bleu, et parfois bleu clair ou "
     "magenta. Dans les sorties, chaque case rouge est entourée de quatre cases jaunes en diagonale, chaque case bleue de quatre "
     "cases orange en croix, et les autres couleurs ne changent pas. À droite, une entrée de test, avec un point d'interrogation à "
     "la place de la sortie : il faut trouver la règle à partir des trois exemples, puis l'appliquer.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Une tâche ARC{NB}: trois exemples, puis un test</text>']
C = 8


def grille(x, y, g):
    n = len(g)
    o.append(f'<rect x="{x - 1}" y="{y - 1}" width="{n * C + 2}" height="{n * C + 2}" fill="#4b5563"/>')
    for i, r in enumerate(g):
        for j, v in enumerate(r):
            o.append(f'<rect x="{x + j * C + 0.5:.1f}" y="{y + i * C + 0.5:.1f}" width="{C - 1}" height="{C - 1}" fill="{ARC[v]}"/>')


G = 9 * C
Y0 = 92
for k, p in enumerate(TACHE["train"]):
    x = 22 + k * 203
    o.append(f'<rect x="{x - 10}" y="{Y0 - 34}" width="{2 * G + 52}" height="{G + 74}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
    o.append(f'<text x="{x + G + 16}" y="{Y0 - 14}" font-size="12" fill="{BRUN}" text-anchor="middle" font-weight="700">exemple {k + 1}</text>')
    grille(x, Y0, p["input"])
    o.append(f'<line x1="{x + G + 6}" y1="{Y0 + G / 2}" x2="{x + G + 26}" y2="{Y0 + G / 2}" stroke="{GRIS}" stroke-width="1.5" marker-end="url(#p)"/>')
    grille(x + G + 32, Y0, p["output"])
    o.append(f'<text x="{x + G / 2}" y="{Y0 + G + 22}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">entrée</text>')
    o.append(f'<text x="{x + G * 1.5 + 32}" y="{Y0 + G + 22}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">sortie</text>')
x = 22 + 3 * 203 + 2
o.append(f'<rect x="{x - 10}" y="{Y0 - 34}" width="{2 * G + 52}" height="{G + 74}" rx="10" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="2"/>')
o.append(f'<text x="{x + G + 16}" y="{Y0 - 14}" font-size="12" fill="{TEAL}" text-anchor="middle" font-weight="700">test</text>')
grille(x, Y0, TACHE["test"][0]["input"])
o.append(f'<line x1="{x + G + 6}" y1="{Y0 + G / 2}" x2="{x + G + 26}" y2="{Y0 + G / 2}" stroke="{GRIS}" stroke-width="1.5" marker-end="url(#p)"/>')
o.append(f'<rect x="{x + G + 32}" y="{Y0}" width="{G}" height="{G}" rx="4" fill="{FOND}" stroke="{TEAL}" stroke-width="1.5" stroke-dasharray="5 4"/>')
o.append(f'<text x="{x + G * 1.5 + 32}" y="{Y0 + G / 2 + 14}" font-size="40" fill="{TEAL}" text-anchor="middle" font-weight="700">?</text>')
o.append(f'<text x="{x + G / 2}" y="{Y0 + G + 22}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">entrée</text>')
o.append(f'<text x="{x + G * 1.5 + 32}" y="{Y0 + G + 22}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">à trouver</text>')
yb = Y0 + G + 76
o.append(f'<text x="{W / 2}" y="{yb}" font-size="12" fill="{ENCRE}" text-anchor="middle">Aucune règle n\'est donnée{NB}: il faut la découvrir à partir des trois exemples, puis l\'appliquer au test.</text>')
o.append(f'<text x="{W / 2}" y="{yb + 20}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">Tâche 0ca9ddb6 du jeu d\'entraînement d\'ARC (François Chollet, 2019)</text>')
o.append("</svg>")
(OUT / "arc-tache.svg").write_text("\n".join(o) + "\n")
print("arc-tache.svg écrit")
