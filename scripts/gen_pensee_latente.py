# /// script
# requires-python = ">=3.10"
# ///
"""Module 4, « Du modèle à l'assistant » : raisonner en mots ou raisonner dans l'espace des vecteurs. À gauche, une
chaîne de pensée : à chaque étape, l'état interne du modèle est réduit à un seul jeton, qui est réinjecté en entrée.
À droite, une pensée continue (Coconut, 2024) : l'état interne est réinjecté tel quel, sans passer par un mot."""
import random
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4" / "pensee-latente.svg"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
rng = random.Random(4)

W, H = 880, 400
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Penser en mots, ou penser en vecteurs</title>",
     "<desc>Deux panneaux. À gauche, une chaîne de pensée : le modèle produit un état interne, un vecteur de milliers "
     "de nombres ; cet état est réduit à un seul jeton, ici le mot « donc », qui est réinjecté en entrée pour l'étape "
     "suivante. Tout ce que le vecteur contenait d'autre est perdu, mais le raisonnement reste lisible. À droite, une "
     "pensée continue : l'état interne est réinjecté tel quel en entrée, sans passer par un mot. Rien ne se perd, mais "
     "le raisonnement n'est plus lisible pour un humain.</desc>",
     '<defs>' + "".join(
         f'<marker id="{n}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
         f'<path d="M0 0 L10 5 L0 10 z" fill="{c}"/></marker>' for n, c in (("p", GRIS), ("b", BRUN), ("t", TEAL))) + '</defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Penser en mots, ou penser en vecteurs</text>']


def texte(x, y, t, taille=11, coul=ENCRE, ancre="middle", gras=False, ital=False):
    g = ' font-weight="700"' if gras else ""
    i = ' font-style="italic"' if ital else ""
    o.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{taille}" fill="{coul}" text-anchor="{ancre}"{g}{i}>{t}</text>')


def modele(x, y):
    o.append(f'<rect x="{x}" y="{y}" width="110" height="92" rx="8" fill="#ffffff" stroke="{BLEU}" stroke-width="1.8"/>')
    for k in range(4):
        o.append(f'<rect x="{x + 14}" y="{y + 14 + k * 17}" width="82" height="11" rx="2" fill="{BLEU}" fill-opacity="{0.15 + 0.12 * k:.2f}"/>')
    texte(x + 55, y + 108, "le modèle", 10.5, BLEU, gras=True)


def vecteur(x, y, n=8, coul=TEAL, w=16):
    for k in range(n):
        o.append(f'<rect x="{x}" y="{y + k * 10}" width="{w}" height="9" fill="{coul}" fill-opacity="{rng.uniform(0.2, 0.95):.2f}" stroke="{coul}" stroke-width="0.7"/>')


def fleche(x1, y1, x2, y2, mk="p", coul=GRIS):
    o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{coul}" stroke-width="1.8" marker-end="url(#{mk})"/>')


# ── panneau gauche : chaîne de pensée ──
o.append(f'<rect x="20" y="50" width="410" height="330" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
texte(225, 76, "Une chaîne de pensée", 12.5, BRUN, gras=True)
modele(44, 104)
fleche(158, 150, 182, 150)
vecteur(186, 110)
texte(194, 204, "l'état interne", 10, TEAL, gras=True)
texte(194, 217, "(des milliers de nombres)", 9.5, ENCRE_PALE)
# l'entonnoir
o.append(f'<path d="M212 112 L262 136 L262 164 L212 188 Z" fill="{BRUN}" fill-opacity="0.15" stroke="{BRUN}" stroke-width="1.4"/>')
fleche(266, 150, 292, 150, "b", BRUN)
o.append(f'<rect x="296" y="134" width="60" height="32" rx="4" fill="#ffffff" stroke="{BRUN}" stroke-width="1.6"/>')
texte(326, 155, "« donc »", 12, ENCRE, gras=True)
texte(326, 124, "un seul jeton", 10, BRUN, gras=True)
# retour en entrée
o.append(f'<path d="M326 170 L326 262 L30 262 L30 150 L40 150" fill="none" stroke="{BRUN}" stroke-width="1.8" stroke-dasharray="5 4" marker-end="url(#b)"/>')
texte(178, 280, "réinjecté en entrée pour l'étape suivante", 10.5, BRUN, ital=True)
texte(225, 330, "À chaque étape, l'état interne est réduit à un mot.", 11.5)
texte(225, 348, "Le raisonnement est lisible, mais l'essentiel se perd.", 11.5)

# ── panneau droit : pensée continue ──
o.append(f'<rect x="450" y="50" width="410" height="330" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
texte(655, 76, "Une pensée continue", 12.5, TEAL, gras=True)
modele(500, 104)
fleche(614, 150, 650, 150)
vecteur(654, 110)
texte(662, 204, "l'état interne", 10, TEAL, gras=True)
texte(662, 217, "(des milliers de nombres)", 9.5, ENCRE_PALE)
o.append(f'<path d="M674 150 L740 150 L740 262 L470 262 L470 150 L496 150" fill="none" stroke="{TEAL}" stroke-width="2.2" marker-end="url(#t)"/>')
texte(605, 280, "réinjecté tel quel, sans passer par un mot", 10.5, TEAL, ital=True)
texte(800, 150, "?", 30, ROUGE, gras=True)
texte(800, 172, "illisible", 10, ROUGE, gras=True)
texte(800, 185, "pour un humain", 10, ROUGE)
texte(655, 330, "Rien ne se perd entre deux étapes,", 11.5)
texte(655, 348, "mais on ne peut plus lire le raisonnement.", 11.5)
o.append("</svg>")
OUT.write_text("\n".join(o) + "\n")
print(OUT.name, "écrit")
