"""Module 2, « Classer » : trois droites qui séparent les mêmes points, puis celle de plus grande marge et ses vecteurs de support."""
import math
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module2"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, GRILLE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#e8dfc9", "#fbf7ee")
NB, FINE = " ", " "

# Points dans un repère de 0 à 100 sur chaque axe (y vers le bas).
ROUGES = [(12, 16), (28, 30), (8, 42), (25, 55), (40, 14), (44, 38), (16, 68), (34, 75)]
BLEUS = [(66, 50), (82, 40), (73, 66), (92, 62), (58, 80), (86, 84), (70, 94), (95, 80)]

# La droite de plus grande marge, par balayage des directions.
meilleur = None
for k in range(7200):
    t = k / 7200 * 2 * math.pi
    u = (math.cos(t), math.sin(t))
    pr = [x * u[0] + y * u[1] for x, y in ROUGES]
    pb = [x * u[0] + y * u[1] for x, y in BLEUS]
    ecart = min(pb) - max(pr)
    if meilleur is None or ecart > meilleur[0]:
        meilleur = (ecart, u, (min(pb) + max(pr)) / 2)
MARGE, (NX, NY), CENTRE = meilleur
ANGLE = math.atan2(NX, -NY)                    # direction de la frontière, perpendiculaire à la normale
SUPPORTS = [p for p in ROUGES + BLEUS if abs((p[0] * NX + p[1] * NY) - CENTRE) - MARGE / 2 < 0.05]


def panneau(o, ox, titre, lignes, bande):
    L, oy, e = 300, 70, 2.8                    # côté du cadre, haut du cadre, échelle (unités → pixels)
    X = lambda v: ox + 10 + v * e
    Y = lambda v: oy + 10 + v * e
    o.append(f'<text x="{ox + L / 2 + 10}" y="{oy - 12}" font-size="13.5" fill="{ENCRE}" text-anchor="middle" font-weight="700">{titre}</text>')
    o.append(f'<clipPath id="c{ox}"><rect x="{ox}" y="{oy}" width="{L + 20}" height="{L}" rx="8"/></clipPath>')
    o.append(f'<rect x="{ox}" y="{oy}" width="{L + 20}" height="{L}" rx="8" fill="{PANNEAU}" stroke="{AXE}"/>')
    o.append(f'<g clip-path="url(#c{ox})">')

    def droite(decalage, angle, coul, ep, tirets=""):
        cx, cy = (CENTRE + decalage) * NX, (CENTRE + decalage) * NY
        dx, dy = math.cos(angle), math.sin(angle)
        return (f'<line x1="{X(cx - 200 * dx):.1f}" y1="{Y(cy - 200 * dy):.1f}" x2="{X(cx + 200 * dx):.1f}" y2="{Y(cy + 200 * dy):.1f}" '
                f'stroke="{coul}" stroke-width="{ep}" {tirets}/>')

    if bande:
        d = MARGE / 2
        coins = []
        for s, t in ((1, -1), (1, 1), (-1, 1), (-1, -1)):
            cx, cy = (CENTRE + s * d) * NX, (CENTRE + s * d) * NY
            coins.append((X(cx + t * 200 * math.cos(ANGLE)), Y(cy + t * 200 * math.sin(ANGLE))))
        o.append(f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in coins)}" fill="{TEAL}" fill-opacity="0.14"/>')
        for s in (1, -1):
            o.append(droite(s * d, ANGLE, TEAL, 1.8, 'stroke-dasharray="6 5"'))
    for decalage, angle, coul, ep in lignes:
        o.append(droite(decalage, angle, coul, ep))
    for pts, coul in ((ROUGES, ROUGE), (BLEUS, BLEU)):
        for x, y in pts:
            o.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="7.5" fill="{coul}" stroke="{PANNEAU}" stroke-width="1.5"/>')
            if bande and (x, y) in SUPPORTS:
                o.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="12" fill="none" stroke="{ENCRE}" stroke-width="2"/>')
    o.append("</g>")
    return X, Y


W, H = 700, 450
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Trois droites sans erreur, et la droite de plus grande marge</title>",
     f"<desc>Deux panneaux avec les mêmes points, rouges en haut à gauche et bleus en bas à droite. À gauche, trois droites les séparent toutes sans "
     f"erreur{NB}: A frôle les points rouges, B frôle les points bleus, C passe au milieu. À droite, la droite C seule, entourée de la plus large bande vide "
     f"possible, la marge{FINE}; les trois points qui touchent les bords de la bande, les vecteurs de support, sont entourés.</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Parmi toutes les droites sans erreur, la plus grande marge</text>']
d = MARGE / 2
lignes = [(-d + 5, ANGLE + 0.035, GRIS, 2.2), (d - 5, ANGLE - 0.035, GRIS, 2.2), (0, ANGLE, BRUN, 3)]
X, Y = panneau(o, 20, "Trois droites sans erreur", lignes, False)
# étiquettes A, B, C près du bas de chaque droite, en dehors du nuage
for nom, (dec, a, coul, _) in zip("ABC", lignes):
    cx, cy = (CENTRE + dec) * NX, (CENTRE + dec) * NY
    t = (100 - cy) / math.sin(a)
    o.append(f'<text x="{X(cx + t * math.cos(a)) + 9:.1f}" y="{Y(100) + 2:.1f}" font-size="13" fill="{coul}" font-weight="700">{nom}</text>')
panneau(o, 360, "La droite C et sa marge", [(0, ANGLE, BRUN, 3)], True)
o.append(f'<text x="{W / 2}" y="{H - 34}" font-size="12.5" fill="{GRIS}" text-anchor="middle">C passe le plus loin des deux groupes{NB}: sa marge, en vert, est la plus large possible.</text>')
o.append(f'<text x="{W / 2}" y="{H - 16}" font-size="12.5" fill="{GRIS}" text-anchor="middle">Les points entourés, les vecteurs de support, suffisent à la déterminer.</text>')
o.append("</svg>")
(OUT / "trois-droites-marge.svg").write_text("\n".join(o) + "\n")
print("trois-droites-marge.svg écrit ; vecteurs de support :", SUPPORTS)
