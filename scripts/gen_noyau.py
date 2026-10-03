"""Module 2, « Généraliser » : le XOR soulevé en trois dimensions (x₁, x₂, x₁·x₂), séparé par un plan, puis la frontière courbe correspondante."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module2"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, GRILLE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#e8dfc9", "#fbf7ee")
NB, FINE = " ", " "
CAS = [(0, 0, False), (1, 1, False), (0, 1, True), (1, 0, True)]      # (x₁, x₂, XOR vrai ?)
T = 0.3
plan_z = lambda a, b: (a + b - T) / 2                                  # le plan x₁ + x₂ − 2z = 0,3

W, H = 700, 430
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Le XOR en trois dimensions, puis sa frontière courbe</title>",
     f"<desc>Deux panneaux. À gauche, les quatre cas du XOR dans un espace à trois dimensions{NB}: les deux entrées x₁ et x₂, et une troisième, leur produit "
     f"x₁·x₂. Seul le cas (1, 1) est soulevé. Un plan incliné passe entre les deux points bleus, au-dessus, et les deux points rouges, au-dessous. À droite, "
     f"le plan de départ, où cette séparation devient une frontière courbe, en deux branches, qui entourent chacune un coin bleu ; les deux points rouges sont dans la zone entre les deux courbes.</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="34" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Un plan dans l\'espace agrandi, une courbe dans le plan de départ</text>']
for ox, titre in ((20, "avec la caractéristique x₁·x₂"), (360, "ramené dans le plan de départ")):
    o.append(f'<rect x="{ox}" y="54" width="320" height="320" rx="10" fill="{PANNEAU}" stroke="{AXE}" stroke-width="1.2"/>')
    o.append(f'<text x="{ox + 160}" y="78" font-size="13.5" fill="{ENCRE}" text-anchor="middle" font-weight="700">{titre}</text>')

# --- à gauche, une perspective cavalière
ox, oy = 70, 300
P = lambda a, b, z: (ox + a * 150 + b * 75, oy - b * 62 - z * 120)
pt = lambda q: f"{q[0]:.1f},{q[1]:.1f}"
base = [P(-0.1, -0.1, 0), P(1.1, -0.1, 0), P(1.1, 1.1, 0), P(-0.1, 1.1, 0)]
o.append(f'<polygon points="{" ".join(pt(q) for q in base)}" fill="{GRILLE}" fill-opacity="0.7" stroke="{AXE}"/>')
# les points du dessous du plan (rouges) et le cas (0, 0), puis le plan, puis le point soulevé (1, 1)
def pierre(a, b, z, vrai):
    x, y = P(a, b, z)
    if z > 0:
        xb, yb = P(a, b, 0)
        o.append(f'<line x1="{xb:.1f}" y1="{yb:.1f}" x2="{x:.1f}" y2="{y:.1f}" stroke="{GRIS}" stroke-width="1.4" stroke-dasharray="4 3"/>')
    o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="9" fill="{ROUGE if vrai else BLEU}" stroke="{PANNEAU}" stroke-width="1.8"/>')
for a, b, v in CAS:                    # les rouges sont sous le plan, les bleus au-dessus
    if v:
        pierre(a, b, a * b, v)
plan = [P(-0.1, -0.1, plan_z(-0.1, -0.1)), P(1.1, -0.1, plan_z(1.1, -0.1)), P(1.1, 1.1, plan_z(1.1, 1.1)), P(-0.1, 1.1, plan_z(-0.1, 1.1))]
o.append(f'<polygon points="{" ".join(pt(q) for q in plan)}" fill="{TEAL}" fill-opacity="0.18" stroke="{TEAL}" stroke-width="1.6"/>')
pierre(0, 0, 0, False)
pierre(1, 1, 1, False)
for (a, b, v), dx, dy in zip(CAS, (-34, 14, -40, 16), (16, -8, -4, 18)):
    x, y = P(a, b, a * b)
    o.append(f'<text x="{x + dx:.1f}" y="{y + dy:.1f}" font-size="11" fill="{ENCRE_PALE}">({a}, {b})</text>')
o.append(f'<text x="{P(0.55, -0.1, 0)[0]:.1f}" y="{P(0.55, -0.1, 0)[1] + 22:.1f}" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle">x₁</text>')
o.append(f'<text x="{P(1.1, 0.6, 0)[0] + 14:.1f}" y="{P(1.1, 0.6, 0)[1] + 4:.1f}" font-size="12" fill="{ENCRE_PALE}">x₂</text>')
o.append(f'<text x="{P(-0.1, -0.1, 0)[0] - 8:.1f}" y="{P(0, 0, 0.9)[1]:.1f}" font-size="12" fill="{ENCRE_PALE}" text-anchor="end">x₁·x₂</text>')
o.append(f'<line x1="{P(-0.1, -0.1, 0)[0]:.1f}" y1="{P(-0.1, -0.1, 0)[1]:.1f}" x2="{P(-0.1, -0.1, 1.05)[0]:.1f}" y2="{P(-0.1, -0.1, 1.05)[1]:.1f}" stroke="{AXE}" stroke-width="1.3"/>')
o.append(f'<text x="{P(1.1, -0.1, plan_z(1.1, -0.1))[0] + 8:.1f}" y="{P(1.1, -0.1, plan_z(1.1, -0.1))[1] + 4:.1f}" font-size="11.5" fill="{TEAL}" font-weight="700">le plan</text>')

# --- à droite, la frontière x₁ + x₂ − 2·x₁·x₂ = 0,5 dans le plan de départ
x0, y0, c = 420, 320, 200
X = lambda a: x0 + a * c
Y = lambda b: y0 - b * c
f = lambda a, b: a + b - 2 * a * b
pas = 8
for i in range(int(-0.25 * c), int(1.25 * c), pas):
    for j in range(int(-0.15 * c), int(1.18 * c), pas):
        a, b = (i + pas / 2) / c, (j + pas / 2) / c
        if f(a, b) > T and 92 < Y(b) - pas < 374 and 360 < X(a) < 680 - pas:
            o.append(f'<rect x="{X(a) - pas / 2:.1f}" y="{Y(b) - pas / 2:.1f}" width="{pas}" height="{pas}" fill="{ROUGE}" fill-opacity="0.10"/>')
for v in (0, 1):
    o.append(f'<line x1="{X(v)}" y1="{Y(-0.12)}" x2="{X(v)}" y2="{Y(1.12)}" stroke="{GRILLE}"/>')
    o.append(f'<line x1="{X(-0.22)}" y1="{Y(v)}" x2="{X(1.25)}" y2="{Y(v)}" stroke="{GRILLE}"/>')
for branche in ((-0.22, 0.49), (0.51, 1.25)):
    pts = []
    k = 0
    while True:
        a = branche[0] + k * 0.01
        if a > branche[1]:
            break
        b = (T - a) / (1 - 2 * a)
        if -0.12 <= b <= 1.12:
            pts.append(f"{X(a):.1f},{Y(b):.1f}")
        k += 1
    o.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{BRUN}" stroke-width="3"/>')
for a, b, v in CAS:
    o.append(f'<circle cx="{X(a)}" cy="{Y(b)}" r="9" fill="{ROUGE if v else BLEU}" stroke="{PANNEAU}" stroke-width="1.8"/>')
o.append(f'<text x="{X(0.5)}" y="{Y(-0.12) + 20}" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle">x₁</text>')
o.append(f'<text x="{X(-0.22) + 4}" y="{Y(0.5)}" font-size="12" fill="{ENCRE_PALE}">x₂</text>')
o.append(f'<text x="{W / 2}" y="{H - 30}" font-size="12.5" fill="{GRIS}" text-anchor="middle">Bleu{NB}: XOR faux. Rouge{NB}: XOR vrai. La zone rosée est celle où la frontière répond «{FINE}vrai{FINE}».</text>')
o.append("</svg>")
(OUT / "xor-noyau.svg").write_text("\n".join(o) + "\n")
print("xor-noyau.svg écrit")
