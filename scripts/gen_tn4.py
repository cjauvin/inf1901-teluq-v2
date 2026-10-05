"""Module 4, travail noté 4 : tirer le mot suivant d'un modèle à bigrammes.

Les probabilités sont celles du corpus du travail noté (après « le » : chat 0,5, chien 0,4, fromage 0,1). La bande
des probabilités cumulées correspond exactement à la formule de génération du tableur, qui compare un nombre tiré au
hasard entre 0 et 1 aux probabilités cumulées.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "
W, H = 700, 400
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Tirer le mot suivant</title>",
     "<desc>En haut, une bande horizontale de 0 à 1 découpée en trois segments, un par mot qui peut suivre « le » : chat de 0 à 0,5, "
     "chien de 0,5 à 0,9, fromage de 0,9 à 1. Une flèche marque un nombre tiré au hasard, 0,63, qui tombe dans le segment de chien. "
     "En bas, une chaîne de mots générés, le, chien, court, le, chat, chaque mot étant tiré d'après le mot qui le précède.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker>'
     f'<marker id="pr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{ROUGE}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Après «{FINE}le{FINE}», tirer le mot suivant</text>']
x0, l, y0 = 70, 560, 96
segs = [("chat", 0.0, 0.5, BLEU), ("chien", 0.5, 0.9, TEAL), ("fromage", 0.9, 1.0, BRUN)]
for nom, a, b, c in segs:
    o.append(f'<rect x="{x0 + a * l}" y="{y0}" width="{(b - a) * l}" height="46" fill="{c}" fill-opacity="0.85" stroke="{FOND}" stroke-width="2"/>')
    o.append(f'<text x="{x0 + (a + b) / 2 * l}" y="{y0 + 28}" font-size="{13.5 if b - a > 0.2 else 10.5}" fill="#fff" text-anchor="middle" font-weight="700">{nom}</text>')
    o.append(f'<text x="{x0 + (a + b) / 2 * l}" y="{y0 + 66}" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle">{f"{b - a:.1f}".replace(".", ",")}</text>')
for v in [0, 0.5, 0.9, 1.0]:
    o.append(f'<line x1="{x0 + v * l}" y1="{y0 - 6}" x2="{x0 + v * l}" y2="{y0}" stroke="{AXE}" stroke-width="1.4"/>')
    o.append(f'<text x="{x0 + v * l}" y="{y0 - 10}" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">{str(v).replace(".", ",").replace(",0", "")}</text>')
o.append(f'<text x="{x0 - 10}" y="{y0 + 66}" font-size="11.5" fill="{GRIS}" text-anchor="end">probabilité</text>')
xr = x0 + 0.63 * l
o.append(f'<line x1="{xr}" y1="{y0 + 112}" x2="{xr}" y2="{y0 + 50}" stroke="{ROUGE}" stroke-width="2.4" marker-end="url(#pr)"/>')
o.append(f'<text x="{xr}" y="{y0 + 130}" font-size="12.5" fill="{ROUGE}" text-anchor="middle" font-weight="700">nombre tiré au hasard{NB}: 0,63 → «{FINE}chien{FINE}»</text>')
# chaîne
mots = ["le", "chien", "court", "le", "chat", "…"]
yc, pas = 320, 104
for k, m in enumerate(mots):
    x = 90 + k * pas
    if m != "…":
        o.append(f'<rect x="{x - 36}" y="{yc - 18}" width="72" height="36" rx="8" fill="{PANNEAU}" stroke="{BLEU if k else ENCRE}" stroke-width="1.8"/>')
    o.append(f'<text x="{x}" y="{yc + 5}" font-size="14" fill="{ENCRE}" text-anchor="middle" font-family="ui-monospace, Menlo, monospace">{m}</text>')
    if k < len(mots) - 1:
        o.append(f'<path d="M{x + 30} {yc - 20} Q{x + pas / 2} {yc - 52} {x + pas - 30} {yc - 20}" fill="none" stroke="{GRIS}" stroke-width="1.6" stroke-dasharray="5 4" marker-end="url(#p)"/>')
o.append(f'<text x="{W / 2}" y="{yc - 58}" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle">chaque mot est tiré d\'après le mot qui le précède</text>')
o.append(f'<text x="90" y="{yc + 38}" font-size="11.5" fill="{GRIS}" text-anchor="middle">mot de départ</text>')
o.append("</svg>")
(OUT / "tn4-tirer-le-mot-suivant.svg").write_text("\n".join(o) + "\n")
print("tn4-tirer-le-mot-suivant.svg écrit")
