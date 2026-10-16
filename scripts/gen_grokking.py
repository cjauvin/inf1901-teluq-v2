"""Module 4, « Regarder à l'intérieur », le grokking expliqué (Nanda et coll., 2023). Deux figures.
1. grokking-horloge.svg : l'addition modulaire sur une horloge (9 + 5 = 2 sur 12 heures), puis ce que fait le réseau pour
   l'addition modulo 113 : chaque nombre devient un angle sur quelques cercles qui tournent à des vitesses différentes
   (fréquences 14, 35 et 41, parmi les cinq qu'utilise le réseau étudié), et la somme est une rotation.
2. grokking-trois-temps.svg : les trois temps de l'entraînement (mémorisation, formation du circuit, nettoyage), d'après
   les époques rapportées par l'article (1 400, 9 400, 14 000). Allure des courbes simplifiée."""
from math import pi, sin, cos, exp
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "


def entete(W, H, titre, desc):
    return ['<?xml version="1.0" encoding="UTF-8"?>',
            f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
            f"<title>{titre}</title>", f"<desc>{desc}</desc>",
            '<defs>' + "".join(
                f'<marker id="m{n}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
                f'<path d="M0 0 L10 5 L0 10 z" fill="{c}"/></marker>' for n, c in [("b", BLEU), ("t", TEAL), ("r", ROUGE)]) + '</defs>',
            f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>']


def pt(cx, cy, r, t):                       # t en tours, 0 en haut, sens horaire
    return cx + r * sin(2 * pi * t), cy - r * cos(2 * pi * t)


def arc(cx, cy, r, t0, dt):
    x0, y0 = pt(cx, cy, r, t0)
    x1, y1 = pt(cx, cy, r, t0 + dt)
    return f'M{x0:.1f} {y0:.1f} A{r} {r} 0 {1 if dt > 0.5 else 0} 1 {x1:.1f} {y1:.1f}'


# ── 1. l'horloge ──
W, H = 840, 440
o = entete(W, H, "Additionner sur des horloges",
           "À gauche, une horloge de 12 heures. Une aiguille bleue pointe sur 9 ; un arc vert avance de 5 heures et arrive sur 2, "
           "marqué en rouge : 9 + 5 = 14, soit 2 sur l'horloge. Additionner, c'est faire tourner l'aiguille. À droite, ce que fait le "
           "réseau pour l'addition modulo 113 : trois petits cercles, qui tournent à des vitesses différentes (fréquences 14, 35 et 41). "
           "Sur chacun, le nombre 9 est un point bleu, et l'ajout de 5 le fait tourner jusqu'au point rouge, la position de 14. Le "
           "réseau combine les angles des deux nombres par une identité trigonométrique, puis lit la réponse là où tous les cercles "
           "s'accordent.")
o.append(f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Additionner en tournant{NB}: l\'arithmétique de l\'horloge</text>')
o.append(f'<rect x="20" y="50" width="380" height="{H - 70}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
o.append(f'<rect x="420" y="50" width="400" height="{H - 70}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
o.append(f'<text x="210" y="76" font-size="12.5" fill="{ENCRE}" text-anchor="middle" font-weight="700">Sur une horloge de 12 heures</text>')
CX, CY, R = 210, 236, 102
o.append(f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="{FOND}" stroke="{AXE}" stroke-width="2"/>')
for h in range(12):
    x, y = pt(CX, CY, R - 18, h / 12)
    coul, gras = (BLEU, 700) if h == 9 else (ROUGE, 700) if h == 2 else (ENCRE_PALE, 400)
    o.append(f'<text x="{x:.1f}" y="{y + 4.5:.1f}" font-size="13" fill="{coul}" text-anchor="middle" font-weight="{gras}">{h if h else 12}</text>')
    x0, y0 = pt(CX, CY, R, h / 12); x1, y1 = pt(CX, CY, R - 6, h / 12)
    o.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{AXE}" stroke-width="1.5"/>')
x, y = pt(CX, CY, R - 36, 9 / 12)
o.append(f'<line x1="{CX}" y1="{CY}" x2="{x:.1f}" y2="{y:.1f}" stroke="{BLEU}" stroke-width="3" marker-end="url(#mb)"/>')
o.append(f'<path d="{arc(CX, CY, R + 14, 9 / 12, 5 / 12)}" fill="none" stroke="{TEAL}" stroke-width="3" marker-end="url(#mt)"/>')
x, y = pt(CX, CY, R + 30, 10.2 / 12)
o.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="12" fill="{TEAL}" text-anchor="middle" font-weight="700">+5</text>')
o.append(f'<circle cx="{CX}" cy="{CY}" r="4" fill="{ENCRE}"/>')
o.append(f'<text x="210" y="{H - 52}" font-size="12" fill="{ENCRE}" text-anchor="middle">9 + 5 = 14, soit <tspan fill="{ROUGE}" font-weight="700">2</tspan> sur l\'horloge.</text>')
o.append(f'<text x="210" y="{H - 34}" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">Additionner, c\'est faire tourner l\'aiguille.</text>')
# le réseau
o.append(f'<text x="620" y="76" font-size="12.5" fill="{ENCRE}" text-anchor="middle" font-weight="700">Dans le réseau, modulo 113</text>')
o.append(f'<text x="620" y="96" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">9 + 5, sur trois des cercles qu\'il utilise</text>')
P, A, B = 113, 9, 5
for i, k in enumerate([14, 35, 41]):
    cx, cy, r = 492 + i * 128, 196, 48
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{FOND}" stroke="{AXE}" stroke-width="1.6"/>')
    t0, dt = (k * A / P) % 1, (k * B / P) % 1
    o.append(f'<path d="{arc(cx, cy, r, t0, dt)}" fill="none" stroke="{TEAL}" stroke-width="2.4" marker-end="url(#mt)"/>')
    for t, coul in [(t0, BLEU), (t0 + dt, ROUGE)]:
        x, y = pt(cx, cy, r, t)
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5.5" fill="{coul}" stroke="{PANNEAU}" stroke-width="1.5"/>')
    o.append(f'<text x="{cx}" y="{cy + r + 22}" font-size="11" fill="{ENCRE}" text-anchor="middle">fréquence {k}</text>')
    o.append(f'<text x="{cx}" y="{cy + r + 37}" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">{k} tours pour 113</text>')
y = 312
for x, coul, t in [(470, BLEU, "le nombre 9"), (590, ROUGE, "9 + 5 = 14")]:
    o.append(f'<circle cx="{x}" cy="{y - 4}" r="5.5" fill="{coul}"/>')
    o.append(f'<text x="{x + 12}" y="{y}" font-size="11" fill="{ENCRE}">{t}</text>')
o.append(f'<line x1="700" y1="{y - 4}" x2="730" y2="{y - 4}" stroke="{TEAL}" stroke-width="2.4" marker-end="url(#mt)"/>')
o.append(f'<text x="738" y="{y}" font-size="11" fill="{ENCRE}">ajouter 5</text>')
for j, l in enumerate(["Chaque nombre devient un angle sur quelques cercles,",
                       "chacun tournant à sa vitesse. Le réseau combine les angles",
                       "par une identité trigonométrique, puis lit la réponse",
                       "là où tous les cercles s'accordent."]):
    o.append(f'<text x="620" y="{340 + j * 16}" font-size="11.5" fill="{ENCRE}" text-anchor="middle">{l}</text>')
o.append("</svg>")
(OUT / "grokking-horloge.svg").write_text("\n".join(o) + "\n")

# ── 2. les trois temps ──
W, H = 840, 400
o = entete(W, H, "Les trois temps du grokking",
           "Un graphique de l'entraînement, en époques, de 0 à 16 000. La précision sur les exemples d'entraînement monte à 100 % avant "
           "1 400 époques : c'est la mémorisation. La précision sur les exemples nouveaux reste presque nulle jusqu'à environ 9 400 "
           "époques, puis monte d'un coup jusqu'à 100 % avant 14 000 époques. Entre les deux, une courbe pointillée montre la part du "
           "calcul confiée au circuit des horloges : elle grandit régulièrement pendant la formation du circuit, bien avant le saut. "
           "Trois bandes marquent les trois temps : mémorisation, formation du circuit, nettoyage.")
o.append(f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Les trois temps du grokking</text>')
X0, X1, Y0, Y1, EMAX = 90, 800, 80, 320, 16000
px = lambda e: X0 + (X1 - X0) * e / EMAX
py = lambda v: Y1 - (Y1 - Y0) * v
for e0, e1, coul, nom in [(0, 1400, BRUN, "mémorisation"), (1400, 9400, TEAL, "formation du circuit"), (9400, 14000, ROUGE, "nettoyage")]:
    o.append(f'<rect x="{px(e0):.1f}" y="{Y0}" width="{px(e1) - px(e0):.1f}" height="{Y1 - Y0}" fill="{coul}" fill-opacity="0.09"/>')
    o.append(f'<text x="{(px(e0) + px(e1)) / 2:.1f}" y="{Y0 - 10}" font-size="11.5" fill="{coul}" text-anchor="middle" font-weight="700">{nom}</text>')
o.append(f'<line x1="{X0}" y1="{Y1}" x2="{X1}" y2="{Y1}" stroke="{AXE}" stroke-width="1.4"/>')
o.append(f'<line x1="{X0}" y1="{Y0}" x2="{X0}" y2="{Y1}" stroke="{AXE}" stroke-width="1.4"/>')
for v in (0, 0.5, 1):
    o.append(f'<text x="{X0 - 8}" y="{py(v) + 4:.1f}" font-size="10.5" fill="{GRIS}" text-anchor="end">{int(v * 100)}{NB}%</text>')
for e in (0, 4000, 8000, 12000, 16000):
    o.append(f'<text x="{px(e):.1f}" y="{Y1 + 18}" font-size="10.5" fill="{GRIS}" text-anchor="middle">{e:,}'.replace(",", NB) + '</text>')
o.append(f'<text x="{(X0 + X1) / 2}" y="{Y1 + 38}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">époques d\'entraînement</text>')
o.append(f'<text x="0" y="0" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle" transform="translate(36 {(Y0 + Y1) / 2}) rotate(-90)">précision</text>')


def courbe(f, coul, ep, pointille=False):
    pts = " ".join(f"{px(e):.1f},{py(f(e)):.1f}" for e in range(0, EMAX + 1, 100))
    o.append(f'<polyline points="{pts}" fill="none" stroke="{coul}" stroke-width="{ep}"' + (' stroke-dasharray="6 4"' if pointille else '') + '/>')


courbe(lambda e: 1 - exp(-e / 280), BRUN, 2.6)
courbe(lambda e: 0.01 + 0.99 / (1 + exp(-(e - 11000) / 450)), BLEU, 2.6)
courbe(lambda e: 0 if e < 1400 else min(1, ((e - 1400) / 9000) ** 1.3), TEAL, 2, True)
o.append(f'<text x="{px(2100):.1f}" y="{py(1) + 18:.1f}" font-size="11" fill="{BRUN}" font-weight="700">exemples d\'entraînement</text>')
o.append(f'<text x="{px(12300):.1f}" y="{py(0.62):.1f}" font-size="11" fill="{BLEU}" font-weight="700">exemples nouveaux</text>')
o.append(f'<text x="{px(3600):.1f}" y="{py(0.62):.1f}" font-size="11" fill="{TEAL}" font-weight="700" text-anchor="middle">le circuit des horloges</text>')
o.append(f'<text x="{px(3600):.1f}" y="{py(0.62) + 14:.1f}" font-size="10.5" fill="{TEAL}" text-anchor="middle">(sa part dans le calcul)</text>')
o.append(f'<text x="{px(3600):.1f}" y="{py(0.62) + 28:.1f}" font-size="10.5" fill="{TEAL}" text-anchor="middle">se forme sans que rien n\'y paraisse</text>')
o.append(f'<text x="{W / 2}" y="{H - 12}" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle" font-style="italic">D\'après Nanda et coll. (2023), addition modulo 113{NB}; allure des courbes simplifiée.</text>')
o.append("</svg>")
(OUT / "grokking-trois-temps.svg").write_text("\n".join(o) + "\n")
print("grokking-horloge.svg et grokking-trois-temps.svg écrits")
