# /// script
# requires-python = ">=3.10"
# ///
"""Module 5, « Qu'est-ce que l'intelligence ? » : modèle génératif contre JEPA (Joint Embedding Predictive
Architecture, Le Cun). À gauche, un modèle génératif prédit l'image suivante pixel par pixel, y compris les détails
imprévisibles, et produit une image floue. À droite, un JEPA encode les deux images et ne prédit que la représentation
de l'image suivante : la comparaison se fait dans l'espace des représentations."""
import random
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module5" / "generatif-contre-jepa.svg"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
VERT, CIEL = "#5d8a45", "#dfe9ef"
NB = " "

W, H = 900, 430
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Modèle génératif contre JEPA</title>",
     "<desc>Deux panneaux. À gauche, un modèle génératif reçoit une image, une balle près d'un arbre, et doit prédire "
     "l'image suivante pixel par pixel. Comme il ne peut pas savoir où iront la balle et chaque feuille, il produit une "
     "image floue, comparée pixel par pixel à la vraie image suivante. À droite, un JEPA : un encodeur transforme "
     "chaque image en une représentation abstraite, une courte rangée de nombres ; un prédicteur prédit la "
     "représentation de l'image suivante à partir de celle de l'image actuelle, et la comparaison se fait entre "
     "représentations. Le modèle n'a pas à prédire les détails imprévisibles.</desc>",
     '<defs>'
     f'<marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker>'
     f'<marker id="r" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="{ROUGE}"/></marker>'
     f'<marker id="t" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="{TEAL}"/></marker>'
     '<filter id="flou" x="-5%" y="-5%" width="110%" height="110%"><feGaussianBlur stdDeviation="3.2"/></filter>'
     '</defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Prédire les pixels, ou prédire une représentation</text>']


def texte(x, y, t, taille=11, coul=ENCRE, ancre="middle", gras=False, ital=False):
    g = ' font-weight="700"' if gras else ""
    i = ' font-style="italic"' if ital else ""
    o.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{taille}" fill="{coul}" text-anchor="{ancre}"{g}{i}>{t}</text>')


FW, FH = 96, 72


def image(x, y, balle, graine, flou=False, balles=None):
    """Une petite scène : ciel, sol, arbre et ses feuilles, balle."""
    rng = random.Random(graine)
    g = ' filter="url(#flou)"' if flou else ""
    o.append(f'<rect x="{x}" y="{y}" width="{FW}" height="{FH}" rx="3" fill="{CIEL}" stroke="{ENCRE_PALE}" stroke-width="1.4"/>')
    o.append(f'<g{g}>')
    o.append(f'<rect x="{x + 1}" y="{y + FH - 18}" width="{FW - 2}" height="17" fill="#cfc29a"/>')
    o.append(f'<rect x="{x + 68}" y="{y + 30}" width="6" height="26" fill="{BRUN}"/>')
    o.append(f'<circle cx="{x + 71}" cy="{y + 26}" r="16" fill="{VERT}"/>')
    for _ in range(14):
        o.append(f'<circle cx="{x + 71 + rng.uniform(-17, 17):.1f}" cy="{y + 26 + rng.uniform(-16, 14):.1f}" r="{rng.uniform(1.6, 3):.1f}" fill="#3f6b2c"/>')
    for bx, op in (balles or [(balle, 1)]):
        o.append(f'<circle cx="{x + bx}" cy="{y + FH - 26}" r="8" fill="{ROUGE}" fill-opacity="{op}"/>')
    o.append('</g>')


def boite(x, y, w, h, l1, coul, l2=None):
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#ffffff" stroke="{coul}" stroke-width="1.7"/>')
    if l2:
        texte(x + w / 2, y + h / 2 - 2, l1, 11, ENCRE, gras=True)
        texte(x + w / 2, y + h / 2 + 12, l2, 10, ENCRE_PALE)
    else:
        texte(x + w / 2, y + h / 2 + 4, l1, 11, ENCRE, gras=True)


def vecteur(x, y, valeurs, coul):
    for k, v in enumerate(valeurs):
        o.append(f'<rect x="{x}" y="{y + k * 11}" width="16" height="10" fill="{coul}" fill-opacity="{0.25 + 0.7 * v:.2f}" stroke="{coul}" stroke-width="0.8"/>')


def fleche(x1, y1, x2, y2, coul=GRIS, mk="p"):
    o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{coul}" stroke-width="1.7" marker-end="url(#{mk})"/>')


# ── panneau gauche : génératif ──
o.append(f'<rect x="20" y="50" width="420" height="360" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
texte(230, 76, "Un modèle génératif", 12.5, ROUGE, gras=True)
image(40, 112, 22, 1)
texte(88, 104, "l'image actuelle", 10.5, ENCRE_PALE)
fleche(140, 148, 170, 148)
boite(174, 128, 92, 40, "prédicteur", ROUGE)
fleche(270, 148, 300, 148)
image(304, 112, 44, 2, flou=True, balles=[(36, 0.45), (48, 0.45), (60, 0.35)])
texte(352, 104, "l'image prédite", 10.5, ENCRE_PALE)
image(304, 262, 52, 3)
texte(352, 350, "la vraie image suivante", 10.5, ENCRE_PALE)
o.append(f'<line x1="352" y1="190" x2="352" y2="256" stroke="{ROUGE}" stroke-width="1.8" marker-start="url(#r)" marker-end="url(#r)"/>')
texte(344, 220, "comparer", 10.5, ROUGE, "end", gras=True)
texte(344, 234, "pixel par pixel", 10.5, ROUGE, "end", gras=True)
texte(150, 270, "La balle et chaque feuille", 10.5, ENCRE, ital=True)
texte(150, 284, "peuvent aller n'importe où :", 10.5, ENCRE, ital=True)
texte(150, 298, "la prédiction devient floue.", 10.5, ENCRE, ital=True)
texte(230, 380, "Prédire chaque détail, même imprévisible.", 11.5)

# ── panneau droit : JEPA ──
o.append(f'<rect x="460" y="50" width="420" height="360" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
texte(670, 76, "Un JEPA (Le Cun)", 12.5, TEAL, gras=True)
image(476, 112, 22, 1)
texte(524, 104, "l'image actuelle", 10.5, ENCRE_PALE)
fleche(576, 148, 592, 148)
boite(596, 128, 70, 40, "encodeur", TEAL)
fleche(670, 148, 684, 148)
vecteur(688, 126, [0.2, 0.8, 0.5, 0.9], TEAL)
fleche(708, 148, 722, 148)
boite(726, 128, 82, 40, "prédicteur", TEAL)
fleche(812, 148, 826, 148)
vecteur(830, 126, [0.3, 0.7, 0.6, 0.8], TEAL)
texte(838, 116, "prédite", 9.5, TEAL, gras=True)
image(476, 262, 52, 3)
texte(524, 350, "la vraie image suivante", 10.5, ENCRE_PALE)
fleche(576, 298, 592, 298)
boite(596, 278, 70, 40, "encodeur", TEAL)
o.append(f'<line x1="670" y1="298" x2="826" y2="298" stroke="{GRIS}" stroke-width="1.7" marker-end="url(#p)"/>')
vecteur(830, 276, [0.3, 0.75, 0.55, 0.85], TEAL)
texte(838, 334, "réelle", 9.5, TEAL, gras=True)
o.append(f'<line x1="838" y1="176" x2="838" y2="268" stroke="{TEAL}" stroke-width="1.8" marker-start="url(#t)" marker-end="url(#t)"/>')
texte(830, 216, "comparer les", 10.5, TEAL, "end", gras=True)
texte(830, 230, "représentations", 10.5, TEAL, "end", gras=True)
texte(670, 380, "Prédire seulement l'essentiel, sous forme abstraite.", 11.5)
o.append("</svg>")
OUT.write_text("\n".join(o) + "\n")
print(OUT.name, "écrit")
