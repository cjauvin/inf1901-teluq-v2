"""Module 3, « Tromper un réseau » : la carte de saillance d'un 7, calculée sur le classifieur de l'applet adverse.html.

Les valeurs (scripts/data/saillance-7.json) ont été exportées depuis l'applet : pour chaque pixel, son intensité
multipliée par l'écart entre le poids de la sortie « 7 » et celui de la sortie « 2 », la deuxième réponse du
classifieur. Une valeur positive pousse vers « 7 », une valeur négative vers « 2 ».
"""
import json
from pathlib import Path

RACINE = Path(__file__).resolve().parent
OUT = RACINE.parent / "static" / "images" / "module3"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, ROUGE, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#c4564a", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "
d = json.loads((RACINE / "data" / "saillance-7.json").read_text())
x = [float(v) for v in d["x"].split(",")]
s = [float(v) for v in d["s"].split(",")]
smax = max(abs(v) for v in s)

W, H, t = 700, 400, 9
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Un chiffre 7 et sa carte de saillance</title>",
     f"<desc>Deux grilles de 28 pixels sur 28. À gauche, l'image d'un 7. À droite, sa carte de saillance{NB}: en vert, les pixels qui ont poussé le "
     f"classifieur vers la réponse «{FINE}7{FINE}», surtout les extrémités de la barre horizontale et le haut du trait vertical{FINE}; en rouge, ceux "
     f"qui l'ont poussé vers «{FINE}2{FINE}», sa deuxième réponse, surtout le bas du trait.</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Quels pixels ont pesé sur la réponse{NB}?</text>']
for k, (x0, titre) in enumerate(((80, "l'image"), (368, "la carte de saillance"))):
    y0 = 70
    o.append(f'<text x="{x0 + 14 * t}" y="{y0 - 8}" font-size="13" fill="{ENCRE_PALE}" text-anchor="middle" font-weight="700">{titre}</text>')
    o.append(f'<rect x="{x0 - 2}" y="{y0 - 2 + 6}" width="{28 * t + 4}" height="{28 * t + 4}" fill="{PANNEAU}" stroke="{AXE}"/>')
    for i in range(784):
        cx, cy = x0 + (i % 28) * t, y0 + 6 + (i // 28) * t
        if k == 0:
            if x[i] > 0.02:
                o.append(f'<rect x="{cx}" y="{cy}" width="{t + 0.2}" height="{t + 0.2}" fill="{ENCRE}" fill-opacity="{x[i]:.2f}"/>')
        elif abs(s[i]) > 0.02:
            v = s[i] / smax
            o.append(f'<rect x="{cx}" y="{cy}" width="{t + 0.2}" height="{t + 0.2}" fill="{TEAL if v > 0 else ROUGE}" fill-opacity="{min(1, abs(v) ** 0.6):.2f}"/>')
y = H - 46
o.append(f'<rect x="200" y="{y - 11}" width="14" height="14" fill="{TEAL}"/><text x="220" y="{y}" font-size="12.5" fill="{ENCRE_PALE}">pousse vers «{FINE}7{FINE}»</text>')
o.append(f'<rect x="370" y="{y - 11}" width="14" height="14" fill="{ROUGE}"/><text x="390" y="{y}" font-size="12.5" fill="{ENCRE_PALE}">pousse vers «{FINE}2{FINE}», la deuxième réponse</text>')
o.append(f'<text x="{W / 2}" y="{H - 18}" font-size="12" fill="{GRIS}" text-anchor="middle">Calculée sur le classifieur de l\'applet de ce chapitre.</text>')
o.append("</svg>")
(OUT / "saillance-7.svg").write_text("\n".join(o) + "\n")
print("saillance-7.svg écrit")
