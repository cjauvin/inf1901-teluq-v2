"""Module 4, « Quatre façons de générer » : le principe d'un réseau antagoniste génératif (GAN)."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "
W, H = 700, 400
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Un réseau antagoniste génératif</title>",
     "<desc>Un schéma en deux parties. En bas à gauche, des nombres tirés au hasard entrent dans le générateur, qui produit "
     "une image fausse. En haut, des vraies images. Les vraies images et l'image fausse entrent toutes deux dans le "
     "discriminateur, qui répond « vraie » ou « fausse ». Deux flèches pointillées repartent de ce verdict : l'une vers "
     "le discriminateur, qui apprend à mieux distinguer, l'autre vers le générateur, qui apprend à mieux tromper.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker>'
     f'<marker id="pb" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{BRUN}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="34" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Deux réseaux qui s\'entraînent l\'un contre l\'autre</text>']


def noeud(x, y, l, titre, sous, coul):
    o.append(f'<rect x="{x - l / 2}" y="{y - 30}" width="{l}" height="60" rx="14" fill="{PANNEAU}" stroke="{coul}" stroke-width="2.4"/>')
    o.append(f'<text x="{x}" y="{y - 4}" font-size="14.5" fill="{ENCRE}" text-anchor="middle" font-weight="700">{titre}</text>')
    o.append(f'<text x="{x}" y="{y + 16}" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle">{sous}</text>')


def vignette(x, y, c, coul, marque):
    o.append(f'<rect x="{x}" y="{y}" width="{c}" height="{c}" rx="4" fill="{PANNEAU}" stroke="{coul}" stroke-width="2"/>')
    # un visage stylisé
    o.append(f'<circle cx="{x + c / 2}" cy="{y + c * 0.45}" r="{c * 0.22}" fill="none" stroke="{coul}" stroke-width="1.8"/>')
    o.append(f'<path d="M{x + c * 0.22} {y + c * 0.92} Q{x + c / 2} {y + c * 0.62} {x + c * 0.78} {y + c * 0.92}" fill="none" stroke="{coul}" stroke-width="1.8"/>')
    if marque:
        o.append(f'<text x="{x + c / 2}" y="{y + c * 0.52}" font-size="{c * 0.28}" fill="{coul}" text-anchor="middle" font-weight="700">?</text>')


def fleche(x1, y1, x2, y2, coul=GRIS, pointe="p", tirets=""):
    o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{coul}" stroke-width="2.2" marker-end="url(#{pointe})"{tirets}/>')


# hasard → générateur → image fausse
o.append(f'<g font-family="ui-monospace, Menlo, monospace" font-size="13" fill="{ENCRE}">'
         f'<text x="70" y="250" text-anchor="middle">0,82</text><text x="70" y="270" text-anchor="middle">−1,37</text>'
         f'<text x="70" y="290" text-anchor="middle">0,05</text><text x="70" y="310" text-anchor="middle">…</text></g>')
o.append(f'<text x="70" y="226" font-size="12.5" fill="{ENCRE_PALE}" text-anchor="middle">hasard</text>')
fleche(104, 275, 150, 275)
noeud(225, 275, 140, "générateur", "le faussaire", TEAL)
fleche(297, 275, 342, 275)
vignette(350, 245, 60, TEAL, True)
o.append(f'<text x="380" y="327" font-size="12.5" fill="{TEAL}" text-anchor="middle" font-weight="700">image fausse</text>')
# vraies images
for k in range(3):
    vignette(338 + 12 * k, 70 + 6 * k, 60, BLEU, False)
o.append(f'<text x="380" y="168" font-size="12.5" fill="{BLEU}" text-anchor="middle" font-weight="700">vraies images</text>')
# → discriminateur → verdict
fleche(420, 120, 492, 178)
fleche(420, 268, 492, 214)
noeud(570, 196, 150, "discriminateur", "l'expert", BLEU)
fleche(570, 228, 570, 268)
o.append(f'<rect x="490" y="272" width="160" height="40" rx="20" fill="{FOND}" stroke="{ENCRE}" stroke-width="1.6"/>')
o.append(f'<text x="570" y="297" font-size="13.5" fill="{ENCRE}" text-anchor="middle" font-weight="700">«{FINE}vraie{FINE}» ou «{FINE}fausse{FINE}»{FINE}?</text>')
# rétroactions
o.append(f'<path d="M650 292 L682 292 L682 120 L612 120 L612 162" fill="none" stroke="{BRUN}" stroke-width="2" stroke-dasharray="6 5" marker-end="url(#pb)"/>')
o.append(f'<path d="M570 314 L570 352 L225 352 L225 310" fill="none" stroke="{BRUN}" stroke-width="2" stroke-dasharray="6 5" marker-end="url(#pb)"/>')
o.append(f'<text x="398" y="374" font-size="12.5" fill="{BRUN}" text-anchor="middle" font-weight="700">le générateur apprend à mieux tromper</text>')
o.append(f'<text x="590" y="88" font-size="12.5" fill="{BRUN}" text-anchor="middle" font-weight="700">le discriminateur apprend</text>')
o.append(f'<text x="590" y="104" font-size="12.5" fill="{BRUN}" text-anchor="middle" font-weight="700">à mieux distinguer</text>')
o.append("</svg>")
(OUT / "gan.svg").write_text("\n".join(o) + "\n")
print("gan.svg écrit")
