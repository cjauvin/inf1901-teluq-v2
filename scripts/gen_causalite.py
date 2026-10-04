"""Module 2, « Bien évaluer un modèle » : la chaleur, cause commune des ventes de crème glacée et des noyades."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module2"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "
W, H = 700, 330
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Une cause commune : la chaleur</title>",
     f"<desc>Un petit graphe. En haut, un nœud «{FINE}chaleur{FINE}» pointe par deux flèches vers deux nœuds placés en bas{NB}: «{FINE}ventes de crème "
     f"glacée{FINE}» à gauche et «{FINE}noyades{FINE}» à droite. Une ligne pointillée relie ces deux nœuds, avec la mention «{FINE}corrélation, sans cause{FINE}».</desc>",
     f'<defs><marker id="pointe" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="34" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Une cause commune{NB}: la chaleur</text>']


def noeud(x, y, l, texte, coul):
    o.append(f'<rect x="{x - l / 2}" y="{y - 22}" width="{l}" height="44" rx="22" fill="{PANNEAU}" stroke="{coul}" stroke-width="2.2"/>')
    o.append(f'<text x="{x}" y="{y + 5}" font-size="14" fill="{ENCRE}" text-anchor="middle" font-weight="600">{texte}</text>')


o.append(f'<line x1="330" y1="112" x2="212" y2="216" stroke="{GRIS}" stroke-width="2.2" marker-end="url(#pointe)"/>')
o.append(f'<line x1="370" y1="112" x2="488" y2="216" stroke="{GRIS}" stroke-width="2.2" marker-end="url(#pointe)"/>')
o.append(f'<line x1="268" y1="240" x2="467" y2="240" stroke="{BRUN}" stroke-width="2.2" stroke-dasharray="6 5"/>')
o.append(f'<text x="367" y="272" font-size="12.5" fill="{BRUN}" text-anchor="middle" font-weight="700">corrélation, sans cause</text>')
noeud(350, 90, 130, "chaleur", ROUGE)
noeud(165, 240, 200, "ventes de crème glacée", BLEU)
noeud(535, 240, 130, "noyades", BLEU)
o.append(f'<text x="{W / 2}" y="{H - 18}" font-size="12.5" fill="{GRIS}" text-anchor="middle">Les flèches indiquent une influence directe, comme dans un réseau bayésien.</text>')
o.append("</svg>")
(OUT / "cause-commune.svg").write_text("\n".join(o) + "\n")
print("cause-commune.svg écrit")
