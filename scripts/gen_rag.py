"""Module 4, « Des outils et des agents » : le principe de la génération augmentée par la recherche (RAG)."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "
W, H = 700, 344
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>La génération augmentée par la recherche</title>",
     "<desc>Un schéma de gauche à droite. La question de l'utilisateur est transformée en plongement. On cherche, dans une base de "
     "documents déjà transformés en plongements, les passages dont le vecteur est le plus proche. Les trois passages trouvés sont "
     "ajoutés au contexte du modèle de langage, avec la question. Le modèle rédige une réponse appuyée sur ces passages, en les "
     "citant.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Chercher d\'abord, répondre ensuite</text>']


def boite(x, y, l, h, titre, lignes, coul):
    o.append(f'<rect x="{x}" y="{y}" width="{l}" height="{h}" rx="10" fill="{PANNEAU}" stroke="{coul}" stroke-width="2"/>')
    o.append(f'<text x="{x + l / 2}" y="{y + 22}" font-size="13" fill="{coul}" text-anchor="middle" font-weight="700">{titre}</text>')
    for k, t in enumerate(lignes):
        o.append(f'<text x="{x + l / 2}" y="{y + 42 + 16 * k}" font-size="11.5" fill="{ENCRE}" text-anchor="middle">{t}</text>')


def fleche(x1, y1, x2, y2):
    o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{GRIS}" stroke-width="2" marker-end="url(#p)"/>')


boite(20, 60, 140, 92, "Question", ["«" + FINE + "Quelle est la durée", "du TN4 dans le", "cours INF1901" + FINE + "?" + FINE + "»"], BLEU)
fleche(160, 106, 196, 106)
boite(200, 60, 140, 92, "Plongement", ["la question devient", "un vecteur"], BLEU)
for r in range(5):
    o.append(f'<rect x="{247 + r * 9}" y="128" width="8" height="16" fill="{["#c9d8ea", "#9fbad8", "#e7c9c3", "#d8e6e2", "#efdcc8"][r]}" stroke="{AXE}" stroke-width="0.6"/>')
fleche(270, 152, 270, 186)
boite(170, 190, 200, 120, "Base de documents", ["des milliers de passages,", "chacun avec son plongement", "", "on garde les trois plus", "proches de la question"], TEAL)
fleche(370, 250, 412, 190)
boite(416, 60, 264, 160, "Contexte du modèle", ["la question", "+ passage 1 (guide du cours)", "+ passage 2 (travail noté 4)", "+ passage 3 (feuille de route)", "+ «" + FINE + "Réponds à partir de ces", "passages, et cite-les." + FINE + "»"], BRUN)
fleche(548, 220, 548, 246)
boite(416, 250, 264, 74, "Réponse", ["appuyée sur les passages,", "avec leurs références"], BRUN)
o.append("</svg>")
(OUT / "rag.svg").write_text("\n".join(o) + "\n")
print("rag.svg écrit")
