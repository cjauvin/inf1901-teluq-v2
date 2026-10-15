"""Module 5, « Les camps du débat » : la carte des camps du débat sur l'IA, sur deux axes. En abscisse, l'ampleur attendue
de l'IA (une technologie normale, voire surestimée, ou une rupture) ; en ordonnée, ce qu'il faut faire (accélérer, encadrer
les usages, freiner, voire arrêter). Les positions sont les mêmes que dans l'applet camps-du-debat.html ; elles résument
des positions publiques, de façon nécessairement simplifiée."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module5" / "camps-du-debat.svg"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, AXE, PANNEAU = "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#b8a888", "#fbf7ee"
NB = " "
CAMPS = [  # nom (lignes), x, y, couleur, voix
    (["Sceptiques"], -0.72, 0.1, "#7a6f63", ["Gary Marcus", "Yann Le Cun"]),
    (["Technologie", "normale"], -0.4, -0.2, "#2f6f6a", ["Arvind Narayanan", "Sayash Kapoor"]),
    (["Éthique", "de l'IA"], -0.4, 0.52, "#3a6ea5", ["Timnit Gebru", "Emily Bender"]),
    (["Populistes"], 0.2, 0.72, "#7b5ea7", ["Steve Bannon", "Bernie Sanders"]),
    (["Sécurité"], 0.72, 0.6, "#c4564a", ["Geoffrey Hinton, Yoshua Bengio", "Eliezer Yudkowsky"]),
    (["Accélération-", "nistes"], 0.62, -0.7, "#9a5b33", ["Marc Andreessen", "David Sacks"]),
]
W, H = 840, 620
X0, X1, Y0, Y1 = 90, 810, 56, 530
CX, CY, RX, RY = (X0 + X1) / 2, (Y0 + Y1) / 2, (X1 - X0) / 2, (Y1 - Y0) / 2
px = lambda x: CX + x * RX
py = lambda y: CY - y * RY
R = 46

o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Les camps du débat sur l'IA</title>",
     "<desc>Une carte à deux axes. Horizontalement, l'ampleur attendue de l'IA, d'une technologie normale, à gauche, à une "
     "rupture, à droite. Verticalement, ce qu'il faut faire : accélérer, en bas ; encadrer les usages, au milieu ; freiner, "
     "voire arrêter, en haut. À gauche, au milieu, les sceptiques (Gary Marcus, Yann Le Cun). "
     "Un peu plus à droite et un peu plus bas, la technologie normale (Arvind Narayanan, Sayash Kapoor). Au-dessus, l'éthique "
     "de l'IA (Timnit Gebru, Emily Bender). En haut, au centre, les populistes (Steve Bannon, Bernie Sanders). En haut à droite, "
     "la sécurité (Geoffrey Hinton, Yoshua Bengio, Eliezer Yudkowsky). En bas à droite, les accélérationnistes (Marc Andreessen, "
     "David Sacks). Accélérationnistes et sécurité s'accordent sur l'ampleur de l'IA et s'opposent sur ce qu'il faut faire.</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<rect x="{X0}" y="{Y0}" width="{X1 - X0}" height="{Y1 - Y0}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>',
     f'<line x1="{X0}" y1="{CY}" x2="{X1}" y2="{CY}" stroke="{AXE}" stroke-dasharray="5 5"/>',
     f'<line x1="{CX}" y1="{Y0}" x2="{CX}" y2="{Y1}" stroke="{AXE}" stroke-dasharray="5 5"/>',
     f'<text x="{CX}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Les camps du débat sur l\'IA</text>',
     # axe vertical
     f'<text x="0" y="0" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle" font-weight="700" transform="translate(34 {CY}) rotate(-90)">Que faire{NB}?</text>',
     f'<text x="0" y="0" font-size="10.5" fill="{GRIS}" text-anchor="end" transform="translate(58 {Y0 + 6}) rotate(-90)">freiner, voire arrêter →</text>',
     f'<text x="0" y="0" font-size="10.5" fill="{GRIS}" text-anchor="start" transform="translate(58 {Y1 - 6}) rotate(-90)">← accélérer</text>',
     f'<text x="{X1 - 10}" y="{CY - 8}" font-size="10.5" fill="{GRIS}" text-anchor="end">encadrer les usages</text>',
     # axe horizontal
     f'<text x="{CX}" y="{Y1 + 30}" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle" font-weight="700">L\'ampleur attendue de l\'IA</text>',
     f'<text x="{X0}" y="{Y1 + 30}" font-size="10.5" fill="{GRIS}">← une technologie normale</text>',
     f'<text x="{X1}" y="{Y1 + 30}" font-size="10.5" fill="{GRIS}" text-anchor="end">une rupture →</text>',
     f'<text x="{CX}" y="{H - 16}" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle" font-style="italic">Positions simplifiées{NB}: la plupart des gens empruntent à plusieurs camps.</text>']
for lignes, x, y, coul, voix in CAMPS:
    cx, cy = px(x), py(y)
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="{coul}" fill-opacity="0.14" stroke="{coul}" stroke-width="1.6"/>')
    for i, l in enumerate(lignes):
        o.append(f'<text x="{cx}" y="{cy + 5 + (i - (len(lignes) - 1) / 2) * 14}" font-size="12" fill="{coul}" text-anchor="middle" font-weight="700">{l}</text>')
    for i, v in enumerate(voix):
        o.append(f'<text x="{cx}" y="{cy + R + 16 + i * 14}" font-size="10.5" fill="{ENCRE}" text-anchor="middle">{v}</text>')
o.append("</svg>")
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(o) + "\n")
print(OUT.name, "écrit")
