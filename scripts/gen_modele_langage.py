"""Module 4, « Des règles aux probabilités » : ce que donne un modèle de langage, une distribution sur le mot suivant, dans
laquelle on tire un mot. Probabilités illustratives."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
MOTS = [("canapé", 0.28), ("lit", 0.22), ("tapis", 0.14), ("coussin", 0.09), ("sol", 0.07), ("fauteuil", 0.06),
        ("(autres mots)", 0.135), ("toit", 0.005), ("démocratie", 0.0000001)]
TIRE = "lit"
W, H = 810, 430
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Un modèle de langage</title>",
     "<desc>À gauche, le début de phrase « Le chat dort sur le » entre dans un modèle de langage. À droite, le modèle donne une "
     "probabilité à chaque mot qui pourrait suivre, sous forme de barres : canapé 28 %, lit 22 %, tapis 14 %, coussin 9 %, sol 7 %, "
     "fauteuil 6 %, d'autres mots 13,5 % au total, toit 0,5 %, et démocratie presque 0. En bas, on tire un mot selon ces "
     "probabilités, ici « lit », et la phrase devient « Le chat dort sur le lit ».</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Un modèle de langage{NB}: la probabilité de chaque mot suivant</text>']
# le début de texte et le modèle
yc = 190
o.append(f'<rect x="24" y="{yc - 26}" width="168" height="52" rx="8" fill="{PANNEAU}" stroke="{BLEU}" stroke-width="1.6"/>')
o.append(f'<text x="108" y="{yc - 6}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">début de texte</text>')
o.append(f'<text x="108" y="{yc + 13}" font-size="14" fill="{ENCRE}" text-anchor="middle" font-style="italic" font-weight="600">Le chat dort sur le…</text>')
o.append(f'<line x1="196" y1="{yc}" x2="220" y2="{yc}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')
o.append(f'<rect x="224" y="{yc - 30}" width="112" height="60" rx="8" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="1.8"/>')
o.append(f'<text x="280" y="{yc - 4}" font-size="12.5" fill="{ENCRE}" text-anchor="middle" font-weight="700">modèle</text>')
o.append(f'<text x="280" y="{yc + 13}" font-size="12.5" fill="{ENCRE}" text-anchor="middle" font-weight="700">de langage</text>')
o.append(f'<line x1="340" y1="{yc}" x2="364" y2="{yc}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')
# les barres
X0, XL, LMAX, Y0, RH = 470, 368, 220, 66, 28
o.append(f'<text x="{XL}" y="{Y0 - 10}" font-size="11" fill="{ENCRE_PALE}">mot suivant</text>')
o.append(f'<text x="{X0}" y="{Y0 - 10}" font-size="11" fill="{ENCRE_PALE}">probabilité</text>')
for k, (m, p) in enumerate(MOTS):
    y = Y0 + k * RH
    tire = m == TIRE
    autre = m.startswith("(")
    coul = ROUGE if tire else (AXE if autre else TEAL)
    o.append(f'<text x="{XL}" y="{y + 15}" font-size="13" fill="{ENCRE_PALE if autre else ENCRE}" font-weight="{700 if tire else 400}"'
             f'{" font-style=" + chr(34) + "italic" + chr(34) if autre else ""}>{m}</text>')
    l = max(1.5, LMAX * p / 0.28)
    o.append(f'<rect x="{X0}" y="{y + 3}" width="{l:.1f}" height="16" rx="3" fill="{coul}"/>')
    if p >= 0.01:
        txt = f"{p * 100:.1f}".replace(".0", "").replace(".", ",") + f"{NB}%"
    elif p >= 0.001:
        txt = f"{p * 100:.1f}".replace(".", ",") + f"{NB}%"
    else:
        txt = "presque 0"
    o.append(f'<text x="{X0 + l + 8:.1f}" y="{y + 15}" font-size="12" fill="{ENCRE}" font-weight="{700 if tire else 400}">{txt}</text>')
ytire = Y0 + 1 * RH + 11
o.append(f'<text x="{X0 + LMAX * 0.22 / 0.28 + 60:.0f}" y="{ytire + 4}" font-size="11.5" fill="{ROUGE}" font-weight="700">← le mot tiré</text>')
o.append(f'<text x="{XL}" y="{Y0 + len(MOTS) * RH + 8}" font-size="10.5" fill="{ENCRE_PALE}">total{NB}: 100{NB}%</text>')
# la phrase complétée
yb = H - 44
o.append(f'<rect x="24" y="{yb - 22}" width="{W - 48}" height="40" rx="8" fill="{PANNEAU}" stroke="{BORD}"/>')
o.append(f'<text x="44" y="{yb + 3}" font-size="11.5" fill="{ENCRE_PALE}">on tire un mot selon ces probabilités{NB}:</text>')
o.append(f'<text x="290" y="{yb + 4}" font-size="15" fill="{ENCRE}" font-style="italic" font-weight="600">Le chat dort sur le <tspan fill="{ROUGE}" font-weight="700">lit</tspan></text>')
o.append(f'<text x="{W - 44}" y="{yb + 3}" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="end">puis on recommence, mot après mot</text>')
o.append("</svg>")
(OUT / "modele-de-langage.svg").write_text("\n".join(o) + "\n")
print("modele-de-langage.svg écrit")
