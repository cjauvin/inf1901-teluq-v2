"""Module 3, accueil : quatre architectures (perceptron multicouche, convolutif, récurrent, Transformer), dessinées
avec les mêmes pièces. Les données montent du bas vers le haut dans les quatre panneaux."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module3"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
OR = "#d18f2f"
W, H = 760, 340
lp, e, x0, y0 = 172.5, 10, 20, 52
YH, YM, YB = 96, 158, 220                                   # rangées du haut, du milieu, du bas
R = 6.5
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Quatre architectures, les mêmes pièces</title>",
     "<desc>Quatre petits réseaux, dessinés avec les mêmes neurones, les données montant du bas vers le haut. "
     "Perceptron multicouche : trois couches, chaque neurone relié à tous ceux de la couche précédente. "
     "Réseau convolutif : chaque neurone n'est relié qu'à trois voisins de la couche précédente, avec les trois mêmes poids, "
     "marqués de trois couleurs qui se répètent partout : un même filtre, réutilisé partout. "
     "Réseau récurrent : la même couche, déroulée sur les mots « le », « chat », « dort », chaque étape transmettant sa mémoire "
     "à la suivante par les mêmes poids. "
     "Transformer : pour les mêmes trois mots, chaque mot consulte tous les autres, avec des poids d'attention plus ou moins forts, "
     "puis un petit réseau est appliqué à chaque mot.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{BRUN}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Quatre architectures, les mêmes pièces</text>']
liens, neurones = [], []


def rang(px, n, y, ecart=None):
    cx = px + lp / 2
    ecart = ecart or (lp - 40) / max(n - 1, 1)
    return [(cx + (k - (n - 1) / 2) * ecart, y) for k in range(n)]


def lien(a, b, coul=AXE, l=1, op=1, fleche=False):
    m = ' marker-end="url(#p)"' if fleche else ""
    if fleche:                                               # la flèche s'arrête au bord du neurone
        dx, dy = b[0] - a[0], b[1] - a[1]; d = (dx * dx + dy * dy) ** 0.5
        a, b = (a[0] + dx / d * R, a[1] + dy / d * R), (b[0] - dx / d * (R + 2), b[1] - dy / d * (R + 2))
    liens.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{coul}" stroke-width="{l}" '
                 f'stroke-opacity="{op}" stroke-linecap="round"{m}/>')


def neurone(p, coul):
    neurones.append(f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{R}" fill="{coul}" stroke="{PANNEAU}" stroke-width="1.5"/>')


def panneau(px, titre, legende):
    o.append(f'<rect x="{px}" y="{y0}" width="{lp}" height="{H - y0 - 16}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
    o.extend(liens); o.extend(neurones); liens.clear(); neurones.clear()
    o.append(f'<text x="{px + lp / 2}" y="{H - 64}" font-size="12.5" fill="{BRUN}" text-anchor="middle" font-weight="700">{titre}</text>')
    for k, l in enumerate(legende):
        o.append(f'<text x="{px + lp / 2}" y="{H - 45 + 14 * k}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">{l}</text>')


def mots(couche):
    for (x, y), m in zip(couche, ["le", "chat", "dort"]):
        neurones.append(f'<text x="{x:.1f}" y="{y + 22}" font-size="11" fill="{ENCRE}" text-anchor="middle" font-style="italic">{m}</text>')


px = [x0 + k * (lp + e) for k in range(4)]
# 1. perceptron multicouche : tout est relié à tout
b, m, h = rang(px[0], 5, YB), rang(px[0], 4, YM, 30), rang(px[0], 2, YH, 34)
for c1, c2 in [(b, m), (m, h)]:
    for a in c1:
        for z in c2:
            lien(a, z)
for p in b: neurone(p, BLEU)
for p in m: neurone(p, TEAL)
for p in h: neurone(p, BLEU)
panneau(px[0], "Perceptron multicouche", ["chaque neurone relié à tous", "ceux de la couche précédente"])
# 2. réseau convolutif : trois poids, les mêmes partout
FILTRE = [BRUN, ROUGE, BLEU]
b, m, h = rang(px[1], 7, YB), rang(px[1], 5, YM, (lp - 40) / 6), rang(px[1], 3, YH, (lp - 40) / 6)
for c1, c2 in [(b, m), (m, h)]:
    for k, z in enumerate(c2):
        for j in range(3):
            lien(c1[k + j], z, FILTRE[j], 1.8)
for p in b: neurone(p, BLEU)
for p in m: neurone(p, TEAL)
for p in h: neurone(p, TEAL)
panneau(px[1], "Réseau convolutif", ["un même filtre (trois poids),", "réutilisé partout"])
# 3. réseau récurrent : la même couche à chaque mot, la mémoire passe de l'une à l'autre
ec = (lp - 52) / 2
b, m, h = rang(px[2], 3, YB, ec), rang(px[2], 3, YM, ec), rang(px[2], 3, YH, ec)
for k in range(3):
    lien(b[k], m[k], TEAL, 1.8); lien(m[k], h[k], AXE, 1.4)
    if k < 2:
        lien(m[k], m[k + 1], BRUN, 2.2, fleche=True)
for p in b: neurone(p, BLEU)
for p in m: neurone(p, TEAL)
for p in h: neurone(p, BLEU)
mots(b)
panneau(px[2], "Réseau récurrent", ["la même couche,", "réutilisée à chaque mot"])
# 4. Transformer : chaque mot consulte tous les autres, puis un petit réseau par mot
b, m, h = rang(px[3], 3, YB, ec), rang(px[3], 3, YM, ec), rang(px[3], 3, YH, ec)
ATT = [[0.6, 0.25, 0.15], [0.2, 0.55, 0.25], [0.1, 0.65, 0.25]]  # « dort » regarde surtout « chat »
for i, z in enumerate(m):
    for j, a in enumerate(b):
        lien(a, z, ROUGE, 0.6 + 4 * ATT[i][j], 0.35 + 0.65 * ATT[i][j])
for k in range(3):
    lien(m[k], h[k], TEAL, 1.8)
for p in b: neurone(p, BLEU)
for p in m: neurone(p, TEAL)
for p in h: neurone(p, TEAL)
mots(b)
panneau(px[3], "Transformer", ["chaque mot consulte", "tous les autres"])
o.append("</svg>")
(OUT / "quatre-architectures.svg").write_text("\n".join(o) + "\n")
print("quatre-architectures.svg écrit")
