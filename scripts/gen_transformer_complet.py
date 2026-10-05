"""Module 3, « L'attention et le Transformer » : le Transformer de 2017, d'après la figure de l'article
« Attention Is All You Need » (Vaswani et al.), redessiné et traduit."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module3"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "
W, H = 760, 600
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Le Transformer de 2017</title>",
     "<desc>Le schéma du Transformer de l'article de 2017, en deux colonnes. À gauche, l'encodeur : la phrase d'origine est transformée "
     "en plongements, auxquels on ajoute un encodage de la position ; puis un bloc, répété N fois, formé d'une attention multi-têtes et "
     "d'un réseau à propagation avant, chacun suivi d'une étape « ajouter et normaliser » qui reçoit aussi, par un raccourci, l'entrée de "
     "l'étape. À droite, le décodeur : la traduction déjà écrite passe par les mêmes plongements et le même encodage de position ; son "
     "bloc, répété N fois, contient une attention multi-têtes masquée, une attention croisée qui reçoit la sortie de l'encodeur, et un "
     "réseau à propagation avant, chacun suivi d'« ajouter et normaliser ». En haut du décodeur, une couche linéaire et un softmax donnent "
     "la probabilité de chaque mot suivant.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Le Transformer de 2017, pour la traduction</text>']
BL, BH = 210, 38                                            # largeur et hauteur des boîtes


def boite(cx, y, titre, anglais, coul, fond=PANNEAU):
    o.append(f'<rect x="{cx - BL / 2}" y="{y}" width="{BL}" height="{BH}" rx="7" fill="{fond}" stroke="{coul}" stroke-width="1.8"/>')
    o.append(f'<text x="{cx}" y="{y + 16}" font-size="12.5" fill="{ENCRE}" text-anchor="middle" font-weight="700">{titre}</text>')
    o.append(f'<text x="{cx}" y="{y + 30}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle" font-style="italic">{anglais}</text>')


def norme(cx, y):
    o.append(f'<rect x="{cx - BL / 2}" y="{y}" width="{BL}" height="24" rx="6" fill="#efe3c2" stroke="{BRUN}" stroke-width="1.4"/>')
    o.append(f'<text x="{cx}" y="{y + 16}" font-size="11.5" fill="{ENCRE}" text-anchor="middle">ajouter et normaliser <tspan font-style="italic" fill="{ENCRE_PALE}">(add &amp; norm)</tspan></text>')


def fleche(x1, y1, x2, y2):
    o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')


def raccourci(cx, y_bas, y_haut):                            # le raccourci contourne la sous-couche, à gauche
    x = cx - BL / 2 - 14
    o.append(f'<path d="M{cx} {y_bas} L{cx} {y_bas - 6} L{x} {y_bas - 6} L{x} {y_haut + 12} L{cx - BL / 2 - 2} {y_haut + 12}" fill="none" '
             f'stroke="{BRUN}" stroke-width="1.4" marker-end="url(#p)"/>')


def entree(cx, y, texte):
    o.append(f'<text x="{cx}" y="{y}" font-size="12" fill="{ENCRE}" text-anchor="middle" font-weight="600">{texte}</text>')
    fleche(cx, y - 14, cx, y - 30)
    boite(cx, y - 70, "plongements", "embeddings", BLEU)
    o.append(f'<circle cx="{cx}" cy="{y - 96}" r="10" fill="{PANNEAU}" stroke="{GRIS}" stroke-width="1.4"/>')
    o.append(f'<text x="{cx}" y="{y - 91.5}" font-size="14" fill="{ENCRE}" text-anchor="middle">+</text>')
    o.append(f'<line x1="{cx}" y1="{y - 72}" x2="{cx}" y2="{y - 86}" stroke="{GRIS}" stroke-width="1.6"/>')
    o.append(f'<text x="{cx + 18}" y="{y - 99}" font-size="11" fill="{ENCRE_PALE}">encodage de la position</text>')
    o.append(f'<text x="{cx + 18}" y="{y - 86}" font-size="10.5" fill="{ENCRE_PALE}" font-style="italic">(positional encoding)</text>')
    return y - 106


# ── encodeur ──
cxe, cxd = 210, 540
y = entree(cxe, H - 30, "phrase d'origine")
top_enc = y - 2 * BH - 152
o.append(f'<rect x="{cxe - BL / 2 - 30}" y="{top_enc}" width="{BL + 60}" height="{y - 12 - top_enc}" rx="12" fill="none" stroke="{TEAL}" stroke-width="2" stroke-dasharray="6 4"/>')
o.append(f'<text x="{cxe - BL / 2 - 40}" y="{(y + top_enc) / 2}" font-size="14" fill="{TEAL}" text-anchor="end" font-weight="700">× N</text>')
o.append(f'<text x="{cxe - BL / 2 - 30}" y="{top_enc - 10}" font-size="14" fill="{TEAL}" font-weight="700">ENCODEUR</text>')
fleche(cxe, y, cxe, y - 30)
ya = y - 30 - BH
boite(cxe, ya, "attention multi-têtes", "multi-head attention", ROUGE)
norme(cxe, ya - 40); raccourci(cxe, y - 18, ya - 40); fleche(cxe, ya, cxe, ya - 14)
yf = ya - 40 - 22 - BH
fleche(cxe, ya - 40, cxe, yf + BH + 2)
boite(cxe, yf, "réseau à propagation avant", "feed-forward", TEAL)
norme(cxe, yf - 40); raccourci(cxe, ya - 46, yf - 40); fleche(cxe, yf, cxe, yf - 14)
sortie_enc_y = yf - 40
# ── décodeur ──
y = entree(cxd, H - 30, "traduction déjà écrite")
top_dec = None
y_dec = y
fleche(cxd, y, cxd, y - 30)
ym = y - 30 - BH
boite(cxd, ym, "attention multi-têtes masquée", "masked multi-head attention", ROUGE)
norme(cxd, ym - 40); raccourci(cxd, y - 18, ym - 40); fleche(cxd, ym, cxd, ym - 14)
yc = ym - 40 - 22 - BH
fleche(cxd, ym - 40, cxd, yc + BH + 2)
boite(cxd, yc, "attention croisée", "cross-attention", ROUGE)
norme(cxd, yc - 40); raccourci(cxd, ym - 46, yc - 40); fleche(cxd, yc, cxd, yc - 14)
yf2 = yc - 40 - 22 - BH
fleche(cxd, yc - 40, cxd, yf2 + BH + 2)
boite(cxd, yf2, "réseau à propagation avant", "feed-forward", TEAL)
norme(cxd, yf2 - 40); raccourci(cxd, yc - 46, yf2 - 40); fleche(cxd, yf2, cxd, yf2 - 14)
# cadre du décodeur
top_dec = yf2 - 40 - 20
o.append(f'<rect x="{cxd - BL / 2 - 30}" y="{top_dec}" width="{BL + 60}" height="{y_dec - 12 - top_dec}" rx="12" fill="none" stroke="{TEAL}" stroke-width="2" stroke-dasharray="6 4"/>')
o.append(f'<text x="{cxd + BL / 2 + 40}" y="{(y_dec + top_dec) / 2}" font-size="14" fill="{TEAL}" font-weight="700">× N</text>')
o.append(f'<text x="{cxd - BL / 2 - 30}" y="{top_dec - 10}" font-size="14" fill="{TEAL}" font-weight="700">DÉCODEUR</text>')
# sortie de l'encodeur vers l'attention croisée, par le haut, comme dans la figure de 2017
xm = (cxe + BL / 2 + 30 + cxd - BL / 2 - 30) / 2
yh = top_enc - 16
o.append(f'<path d="M{cxe} {sortie_enc_y} L{cxe} {yh} L{xm} {yh} L{xm} {yc + BH / 2} '
         f'L{cxd - BL / 2 - 2} {yc + BH / 2}" fill="none" stroke="{BLEU}" stroke-width="2" marker-end="url(#p)"/>')
o.append(f'<text x="{cxe + 12}" y="{yh - 8}" font-size="11.5" fill="{BLEU}">la phrase d\'origine, encodée</text>')
# sortie : linéaire et softmax
yl = top_dec - 66
fleche(cxd, yf2 - 40, cxd, yl + 34)
o.append(f'<rect x="{cxd - BL / 2}" y="{yl}" width="{BL}" height="32" rx="7" fill="{PANNEAU}" stroke="{ENCRE}" stroke-width="1.6"/>')
o.append(f'<text x="{cxd}" y="{yl + 20}" font-size="12" fill="{ENCRE}" text-anchor="middle" font-weight="700">linéaire, puis softmax</text>')
o.append(f'<text x="{cxd - BL / 2 - 12}" y="{yl + 13}" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="end">probabilité de</text>')
o.append(f'<text x="{cxd - BL / 2 - 12}" y="{yl + 28}" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="end">chaque mot suivant</text>')
o.append("</svg>")
(OUT / "transformer-complet.svg").write_text("\n".join(o) + "\n")
print("transformer-complet.svg écrit")
