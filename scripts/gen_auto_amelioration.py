# /// script
# requires-python = ">=3.10"
# ///
"""Module 5, « Peut-on perdre le contrôle ? » : l'auto-amélioration récursive. À gauche, la boucle : un modèle fait de la
recherche en IA, ce qui produit un modèle plus capable, qui recommence. À droite, trois façons dont la boucle pourrait
tourner : l'explosion, la croissance progressive, le plafond. Les courbes sont qualitatives."""
import math
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module5" / "auto-amelioration.svg"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "

W, H = 860, 404
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>L'auto-amélioration récursive</title>",
     "<desc>Deux panneaux. À gauche, une boucle à trois étapes : un modèle d'IA fait de la recherche en IA ; il en sort un "
     "modèle plus capable ; ce nouveau modèle recommence, et ainsi de suite. À droite, un graphique qualitatif des "
     "capacités en fonction du temps, avec une ligne pointillée pour le niveau humain et trois courbes possibles : "
     "l'explosion, qui monte presque à la verticale (Good, Yudkowsky) ; une croissance progressive, qui accélère sans "
     "rupture (Christiano) ; un plafond, où la courbe s'aplatit (Chollet). Personne ne sait laquelle décrira "
     "l'avenir.</desc>",
     f'<defs>' + "".join(
         f'<marker id="{n}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
         f'<path d="M0 0 L10 5 L0 10 z" fill="{c}"/></marker>' for n, c in (("p", GRIS), ("t", TEAL))) + '</defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">L\'auto-amélioration récursive</text>']


def texte(x, y, t, taille=11.5, coul=ENCRE, ancre="middle", gras=False, ital=False):
    g = ' font-weight="700"' if gras else ""
    i = ' font-style="italic"' if ital else ""
    o.append(f'<text x="{x}" y="{y}" font-size="{taille}" fill="{coul}" text-anchor="{ancre}"{g}{i}>{t}</text>')


# ── panneau gauche : la boucle ──
o.append(f'<rect x="20" y="50" width="360" height="336" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
texte(200, 76, "La boucle", 12.5, TEAL, gras=True)
CX, CY, R = 200, 212, 92
NOEUDS = [(-90, ["un modèle"]), (30, ["il fait de la", "recherche en IA"]), (150, ["un modèle", "plus capable"])]
DEMI = {-90: (52, 15), 30: (62, 22), 150: (52, 22)}
for a, lignes in NOEUDS:
    x, y = CX + R * math.cos(math.radians(a)), CY + R * math.sin(math.radians(a))
    hw, hh = DEMI[a]
    o.append(f'<rect x="{x - hw:.1f}" y="{y - hh:.1f}" width="{2 * hw}" height="{2 * hh}" rx="6" fill="#ffffff" stroke="{TEAL}" stroke-width="1.6"/>')
    for k, l in enumerate(lignes):
        texte(f"{x:.1f}", f"{y + 4 + (k - (len(lignes) - 1) / 2) * 15:.1f}", l, 11.5, ENCRE, gras=(k == 0 and len(lignes) == 1))
for a1, a2 in ((-90, 30), (30, 150), (150, 270)):
    d1, d2 = a1 + 32, a2 - 32
    x1, y1 = CX + R * math.cos(math.radians(d1)), CY + R * math.sin(math.radians(d1))
    x2, y2 = CX + R * math.cos(math.radians(d2)), CY + R * math.sin(math.radians(d2))
    o.append(f'<path d="M{x1:.1f} {y1:.1f} A{R} {R} 0 0 1 {x2:.1f} {y2:.1f}" fill="none" stroke="{TEAL}" stroke-width="2" marker-end="url(#t)"/>')
texte(CX, CY - 2, "et ainsi", 11, ENCRE_PALE, ital=True)
texte(CX, CY + 13, "de suite", 11, ENCRE_PALE, ital=True)
texte(200, 350, "À chaque tour, le chercheur", 11.5)
texte(200, 368, "est un peu plus capable.", 11.5)

# ── panneau droit : trois trajectoires ──
o.append(f'<rect x="396" y="50" width="444" height="336" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
texte(618, 76, f"À quelle vitesse tourne-t-elle{NB}?", 12.5, BLEU, gras=True)
X0, Y0, LX, LY = 444, 322, 330, 222
o.append(f'<line x1="{X0}" y1="{Y0}" x2="{X0}" y2="{Y0 - LY - 8}" stroke="{AXE}" stroke-width="1.4" marker-end="url(#p)"/>')
o.append(f'<line x1="{X0}" y1="{Y0}" x2="{X0 + LX + 14}" y2="{Y0}" stroke="{AXE}" stroke-width="1.4" marker-end="url(#p)"/>')
texte(X0 + LX + 6, Y0 + 18, "temps", 10.5, ENCRE_PALE, ancre="end")
o.append(f'<text x="{X0 - 14}" y="{Y0 - LY / 2}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle" transform="rotate(-90 {X0 - 14} {Y0 - LY / 2})">capacités</text>')
NH = 128
o.append(f'<line x1="{X0}" y1="{Y0 - NH}" x2="{X0 + LX}" y2="{Y0 - NH}" stroke="{GRIS}" stroke-width="1.2" stroke-dasharray="4 4"/>')
texte(X0 + 6, Y0 - NH - 6, "niveau humain", 10, GRIS, ancre="start")


def courbe(f, coul):
    pts = []
    for i in range(0, 401):
        t = i / 400
        v = f(t)
        if v > LY:
            break
        pts.append(f"{X0 + t * LX:.1f},{Y0 - v:.1f}")
    o.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{coul}" stroke-width="2.4" stroke-linejoin="round"/>')


courbe(lambda t: 14 + 7 / (0.97 - t) - 7 / 0.97, ROUGE)
courbe(lambda t: 14 + 196 * t ** 2.3, BLEU)
courbe(lambda t: 14 + 148 / (1 + math.exp(-9 * (t - 0.42))) - 148 / (1 + math.exp(9 * 0.42)), TEAL)
LEG = [(ROUGE, "l'explosion", "(Good, Yudkowsky)"), (BLEU, "la croissance progressive", "(Christiano)"),
       (TEAL, "le plafond", "(Chollet)")]
for k, (c, nom, qui) in enumerate(LEG):
    y = 100 + k * 18
    o.append(f'<line x1="{X0 + 12}" y1="{y - 4}" x2="{X0 + 34}" y2="{y - 4}" stroke="{c}" stroke-width="2.4"/>')
    o.append(f'<text x="{X0 + 42}" y="{y}" font-size="10.5" fill="{c}" font-weight="700">{nom} <tspan font-weight="400" fill="{ENCRE_PALE}">{qui}</tspan></text>')
texte(618, 350, "Trois trajectoires possibles, qualitatives{NB}:".replace("{NB}", NB), 11.5)
texte(618, 368, "personne ne sait laquelle décrira l'avenir.", 11.5)
o.append("</svg>")
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(o) + "\n")
print(OUT.name, "écrit")
