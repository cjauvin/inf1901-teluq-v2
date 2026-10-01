"""« Déplacer les poteaux du but » : à chaque succès de l'IA, le but recule."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module1"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "
W, H = 780, 402
SOL = 226                       # ligne du terrain
ETAPES = [
    ("1997", ["battre le champion", "du monde d'échecs"], f"«{FINE}ce n'est que", f"du calcul{FINE}»"),
    ("2012", ["reconnaître", "des images"], f"«{FINE}ce n'est que", f"de la statistique{FINE}»"),
    ("2016", ["battre le champion", "du monde de go"], f"«{FINE}ce n'est", f"qu'un jeu{FINE}»"),
    ("2022", ["converser en", "langage courant"], f"«{FINE}ce n'est que de la", f"prédiction de mots{FINE}»"),
]
XS = [96, 252, 408, 564]
X_FUTUR = 706


def but(o, x, couleur, opacite=1.0, pointille=False):
    """Des poteaux de but (football, rugby) : un pied, une barre transversale, deux montants."""
    demi, pied, montant = 27, 26, 50
    y_barre, y_haut = SOL - pied, SOL - pied - montant
    trait = ' stroke-dasharray="5 4"' if pointille else ""
    style = f'fill="none" stroke="{couleur}" stroke-linecap="round" stroke-linejoin="round" opacity="{opacite}"{trait}'
    o.append(f'<line x1="{x}" y1="{SOL}" x2="{x}" y2="{y_barre}" stroke-width="6" {style}/>')
    o.append(f'<path d="M{x - demi} {y_haut} L{x - demi} {y_barre} L{x + demi} {y_barre} L{x + demi} {y_haut}" stroke-width="4.5" {style}/>')
    o.append(f'<ellipse cx="{x}" cy="{SOL + 1}" rx="12" ry="3" fill="{couleur}" opacity="{0.35 * opacite}"/>')   # le pied au sol


o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Déplacer les poteaux du but</title>",
     f"<desc>Une ligne du temps avec quatre paires de poteaux de but, en forme de fourche. 1997{NB}: battre le champion du monde d'échecs, suivi de la réaction «{FINE}ce n'est que du calcul{FINE}». 2012{NB}: reconnaître des images, «{FINE}ce n'est que de la statistique{FINE}». 2016{NB}: battre le champion du monde de go, «{FINE}ce n'est qu'un jeu{FINE}». 2022{NB}: converser en langage courant, «{FINE}ce n'est que de la prédiction de mots{FINE}». Après chaque succès, une flèche en pointillé déplace le but vers la droite{FINE}; un cinquième but, en pointillé, porte un point d'interrogation.</desc>",
     f'<defs><marker id="pointe" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{BRUN}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="38" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Déplacer les poteaux du but (<tspan font-style="italic">moving the goalposts</tspan>)</text>',
     f'<text x="{W / 2}" y="60" font-size="12.5" fill="{ENCRE_PALE}" text-anchor="middle">À chaque succès, la tâche réussie cesse de compter comme de l\'intelligence, et le but recule.</text>']

# le terrain
o.append(f'<line x1="30" y1="{SOL}" x2="{W - 30}" y2="{SOL}" stroke="{AXE}" stroke-width="2"/>')

# les déplacements du but : arcs en pointillé au-dessus des buts
tous = XS + [X_FUTUR]
for a, b in zip(tous, tous[1:]):
    m = (a + b) / 2
    o.append(f'<path d="M{a + 8} {SOL - 88} Q{m} {SOL - 132} {b - 10} {SOL - 90}" fill="none" stroke="{BRUN}" stroke-width="2" '
             f'stroke-dasharray="6 4" marker-end="url(#pointe)"/>')

for x, (annee, succes, r1, r2) in zip(XS, ETAPES):
    but(o, x, TEAL)
    o.append(f'<text x="{x}" y="{SOL + 24}" font-size="14" fill="{ENCRE}" text-anchor="middle" font-weight="700">{annee}</text>')
    for i, t in enumerate(succes):
        o.append(f'<text x="{x}" y="{SOL + 46 + i * 16}" font-size="12.5" fill="{ENCRE}" text-anchor="middle">{t}</text>')
    o.append(f'<circle cx="{x}" cy="{SOL - 52}" r="10" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="2"/>')       # le ballon, dans le but
    o.append(f'<path d="M{x - 4.5} {SOL - 52} l3.3 3.8 l6.5 -7.5" fill="none" stroke="{TEAL}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')
    for i, t in enumerate((r1, r2)):
        o.append(f'<text x="{x}" y="{SOL + 100 + i * 16}" font-size="12" fill="{ROUGE}" text-anchor="middle" font-style="italic">{t}</text>')

but(o, X_FUTUR, GRIS, opacite=0.8, pointille=True)
o.append(f'<text x="{X_FUTUR}" y="{SOL - 44}" font-size="22" fill="{GRIS}" text-anchor="middle" font-weight="700">?</text>')
o.append(f'<text x="{X_FUTUR}" y="{SOL + 24}" font-size="12.5" fill="{GRIS}" text-anchor="middle">le prochain but</text>')

o.append(f'<text x="{W / 2}" y="{H - 20}" font-size="12.5" fill="{ENCRE_PALE}" text-anchor="middle">En rouge{NB}: la réaction typique après chaque succès (des formules courantes, pas des citations).</text>')
o.append("</svg>")
(OUT / "poteaux-du-but.svg").write_text("\n".join(o) + "\n")
print("poteaux-du-but.svg écrit")
