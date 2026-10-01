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


def but(o, x, couleur, opacite=1.0, pointille=False, texte="BUT"):
    """Un poteau de signalisation : un poteau planté au sol et un panneau octogonal, comme un stop."""
    import math
    r, cy = 27, SOL - 62
    pts = " ".join(f"{x + r * math.cos(math.radians(22.5 + 45 * k)):.1f},{cy + r * math.sin(math.radians(22.5 + 45 * k)):.1f}" for k in range(8))
    o.append(f'<line x1="{x}" y1="{SOL}" x2="{x}" y2="{cy + r - 2}" stroke="{GRIS}" stroke-width="5" stroke-linecap="round" opacity="{opacite}"/>')
    o.append(f'<ellipse cx="{x}" cy="{SOL + 1}" rx="11" ry="3" fill="{GRIS}" opacity="{0.4 * opacite}"/>')
    if pointille:
        o.append(f'<polygon points="{pts}" fill="{PANNEAU}" stroke="{couleur}" stroke-width="3" stroke-dasharray="5 4" stroke-linejoin="round" opacity="{opacite}"/>')
        o.append(f'<text x="{x}" y="{cy + 8}" font-size="23" fill="{couleur}" text-anchor="middle" font-weight="700">{texte}</text>')
    else:
        o.append(f'<polygon points="{pts}" fill="{couleur}" stroke="{PANNEAU}" stroke-width="2.5" stroke-linejoin="round"/>')
        o.append(f'<polygon points="{pts}" fill="none" stroke="{couleur}" stroke-width="1" stroke-linejoin="round" transform="translate({x} {cy}) scale(1.09) translate({-x} {-cy})"/>')
        o.append(f'<text x="{x}" y="{cy + 5.5}" font-size="15" fill="{PANNEAU}" text-anchor="middle" font-weight="700" letter-spacing="1">{texte}</text>')


o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Déplacer les poteaux du but</title>",
     f"<desc>Une ligne du temps avec quatre poteaux de signalisation, dont le panneau octogonal porte le mot «{FINE}BUT{FINE}». 1997{NB}: battre le champion du monde d'échecs, suivi de la réaction «{FINE}ce n'est que du calcul{FINE}». 2012{NB}: reconnaître des images, «{FINE}ce n'est que de la statistique{FINE}». 2016{NB}: battre le champion du monde de go, «{FINE}ce n'est qu'un jeu{FINE}». 2022{NB}: converser en langage courant, «{FINE}ce n'est que de la prédiction de mots{FINE}». Après chaque succès, une flèche en pointillé déplace le but vers la droite{FINE}; le panneau d'un cinquième poteau, en pointillé, porte un point d'interrogation.</desc>",
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
    o.append(f'<path d="M{a + 12} {SOL - 100} Q{m} {SOL - 142} {b - 14} {SOL - 102}" fill="none" stroke="{BRUN}" stroke-width="2" '
             f'stroke-dasharray="6 4" marker-end="url(#pointe)"/>')

for x, (annee, succes, r1, r2) in zip(XS, ETAPES):
    but(o, x, TEAL)
    o.append(f'<text x="{x}" y="{SOL + 24}" font-size="14" fill="{ENCRE}" text-anchor="middle" font-weight="700">{annee}</text>')
    for i, t in enumerate(succes):
        o.append(f'<text x="{x}" y="{SOL + 46 + i * 16}" font-size="12.5" fill="{ENCRE}" text-anchor="middle">{t}</text>')
    o.append(f'<circle cx="{x + 22}" cy="{SOL - 84}" r="9" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="2"/>')       # pastille : but atteint
    o.append(f'<path d="M{x + 18} {SOL - 84} l3 3.4 l5.6 -6.6" fill="none" stroke="{TEAL}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')
    for i, t in enumerate((r1, r2)):
        o.append(f'<text x="{x}" y="{SOL + 100 + i * 16}" font-size="12" fill="{ROUGE}" text-anchor="middle" font-style="italic">{t}</text>')

but(o, X_FUTUR, GRIS, opacite=0.9, pointille=True, texte="?")
o.append(f'<text x="{X_FUTUR}" y="{SOL + 24}" font-size="12.5" fill="{GRIS}" text-anchor="middle">le prochain but</text>')

o.append(f'<text x="{W / 2}" y="{H - 20}" font-size="12.5" fill="{ENCRE_PALE}" text-anchor="middle">En rouge{NB}: la réaction typique après chaque succès (des formules courantes, pas des citations).</text>')
o.append("</svg>")
(OUT / "poteaux-du-but.svg").write_text("\n".join(o) + "\n")
print("poteaux-du-but.svg écrit")
