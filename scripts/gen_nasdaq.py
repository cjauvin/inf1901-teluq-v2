# /// script
# requires-python = ">=3.10"
# ///
"""Module 5, « La richesse et le pouvoir » : l'indice Nasdaq de 1995 à 2016, la bulle Internet, son éclatement et le
retour au sommet quinze ans plus tard. Valeurs approximatives (clôtures arrondies aux dates repères)."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module5" / "nasdaq-bulle-internet.svg"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "

SERIE = [(1995.0, 750), (1996.0, 1050), (1997.0, 1290), (1998.0, 1570), (1998.75, 1500), (1999.0, 2190),
         (1999.5, 2700), (1999.83, 2970), (2000.0, 4070), (2000.19, 5048), (2000.33, 3700), (2000.5, 3960),
         (2000.67, 3670), (2001.0, 2470), (2001.27, 1840), (2001.5, 2160), (2001.72, 1420), (2002.0, 1950),
         (2002.5, 1460), (2002.77, 1114), (2003.0, 1340), (2004.0, 2000), (2005.0, 2175), (2006.0, 2205),
         (2007.0, 2415), (2007.83, 2860), (2008.5, 2290), (2009.17, 1270), (2010.0, 2270), (2011.0, 2650),
         (2012.0, 2605), (2013.0, 3020), (2014.0, 4180), (2015.0, 4740), (2015.31, 5056), (2016.0, 5010)]

W, H = 860, 380
X0, X1, Y0, Y1 = 90, 820, 320, 70
T0, T1, VMAX = 1995, 2016, 5500


def px(t):
    return X0 + (t - T0) / (T1 - T0) * (X1 - X0)


def py(v):
    return Y0 - v / VMAX * (Y0 - Y1)


o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>La bulle Internet : l'indice Nasdaq de 1995 à 2016</title>",
     "<desc>Courbe de l'indice boursier Nasdaq de 1995 à 2016. L'indice passe d'environ 750 points en 1995 à un sommet "
     "de 5 048 points le 10 mars 2000, puis s'effondre jusqu'à 1 114 points le 9 octobre 2002, une baisse de 78 %. Il "
     "remonte lentement, rechute pendant la crise financière de 2008, et ne retrouve son sommet de 2000 qu'en avril "
     "2015, quinze ans plus tard.</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">La bulle Internet : l\'indice Nasdaq de 1995 à 2016</text>'.replace(" :", NB + ":")]
o.append(f'<rect x="20" y="48" width="{W - 40}" height="{H - 68}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
# l'éclatement
o.append(f'<rect x="{px(2000.19):.1f}" y="{Y1}" width="{px(2002.77) - px(2000.19):.1f}" height="{Y0 - Y1}" fill="{ROUGE}" fill-opacity="0.08"/>')
# grille et axes
for v in range(0, 5001, 1000):
    o.append(f'<line x1="{X0}" y1="{py(v):.1f}" x2="{X1}" y2="{py(v):.1f}" stroke="{AXE}" stroke-width="{1.2 if v == 0 else 0.6}"/>')
    o.append(f'<text x="{X0 - 8}" y="{py(v) + 4:.1f}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="end">{f"{v:,}".replace(",", NB)}</text>')
for an in range(1995, 2017, 3):
    o.append(f'<text x="{px(an):.1f}" y="{Y0 + 18}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">{an}</text>')
    o.append(f'<line x1="{px(an):.1f}" y1="{Y0}" x2="{px(an):.1f}" y2="{Y0 + 5}" stroke="{AXE}"/>')
o.append(f'<text x="{X0 - 58}" y="{(Y0 + Y1) / 2}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle" transform="rotate(-90 {X0 - 58} {(Y0 + Y1) / 2})">points</text>')
# le sommet de 2000, en pointillé
o.append(f'<line x1="{px(2000.19):.1f}" y1="{py(5048):.1f}" x2="{px(2015.31):.1f}" y2="{py(5048):.1f}" stroke="{GRIS}" stroke-width="1.2" stroke-dasharray="5 4"/>')
o.append(f'<polyline points="{" ".join(f"{px(t):.1f},{py(v):.1f}" for t, v in SERIE)}" fill="none" stroke="{BLEU}" stroke-width="2.4" stroke-linejoin="round"/>')
# repères
for t, v, coul in ((2000.19, 5048, ROUGE), (2002.77, 1114, ROUGE), (2015.31, 5056, TEAL)):
    o.append(f'<circle cx="{px(t):.1f}" cy="{py(v):.1f}" r="5" fill="{coul}" stroke="#ffffff" stroke-width="1.5"/>')
o.append(f'<text x="{px(2000.19) - 10:.1f}" y="{py(5048) - 2:.1f}" font-size="11" fill="{ROUGE}" text-anchor="end" font-weight="700">10 mars 2000</text>')
o.append(f'<text x="{px(2000.19) - 10:.1f}" y="{py(5048) + 12:.1f}" font-size="10.5" fill="{ROUGE}" text-anchor="end">5{NB}048 points</text>')
o.append(f'<text x="{px(2002.77) + 10:.1f}" y="{py(1114) + 4:.1f}" font-size="11" fill="{ROUGE}" font-weight="700">9 octobre 2002{NB}: 1{NB}114 points (−78{NB}%)</text>')
o.append(f'<text x="{px(2015.31) - 8:.1f}" y="{py(5056) - 12:.1f}" font-size="11" fill="{TEAL}" text-anchor="end" font-weight="700">avril 2015{NB}: le sommet est retrouvé</text>')
o.append(f'<text x="{(px(2000.19) + px(2002.77)) / 2:.1f}" y="{Y0 - 10}" font-size="10.5" fill="{ROUGE}" text-anchor="middle" font-style="italic">l\'éclatement</text>')
o.append(f'<text x="{px(2008.6):.1f}" y="{py(1270) + 26:.1f}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle" font-style="italic">la crise de 2008</text>')
o.append(f'<text x="{X1}" y="{H - 28}" font-size="9.5" fill="{GRIS}" text-anchor="end" font-style="italic">valeurs approximatives</text>')
o.append("</svg>")
OUT.write_text("\n".join(o) + "\n")
print(OUT.name, "écrit")
