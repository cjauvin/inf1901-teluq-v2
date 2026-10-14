# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""Module 4, « Des outils et des agents » : la recherche approximative des plus proches voisins dans un graphe à plusieurs
étages (HNSW). Des points tirés au hasard, chacun présent à l'étage 0, certains aussi aux étages supérieurs ; à chaque étage,
chaque point est relié à ses voisins de l'étage. La recherche part du point d'entrée de l'étage le plus haut, avance de
voisin en voisin vers la question tant qu'elle s'en rapproche, puis descend d'un étage. Le trajet est réellement calculé.

    uv run scripts/gen_hnsw.py
"""
from pathlib import Path
import numpy as np

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
import os
rng = np.random.default_rng(int(os.environ.get("GRAINE", 12)))
N = 64
P = rng.uniform(0.04, 0.96, (N, 2))
niveaux = [np.arange(N)]
niveaux.append(rng.choice(N, 14, replace=False))
niveaux.append(rng.choice(niveaux[1], 4, replace=False))
Q = np.array([0.80, 0.30])                                      # la question
d = lambda i: float(np.linalg.norm(P[i] - Q))


def aretes(ids, k):
    """Chaque point relié à ses k plus proches voisins de l'étage (graphe rendu symétrique)."""
    e = set()
    for i in ids:
        autres = sorted((j for j in ids if j != i), key=lambda j: np.linalg.norm(P[i] - P[j]))[:k]
        for j in autres:
            e.add((min(i, j), max(i, j)))
    return e


E = [aretes(niveaux[0], 4), aretes(niveaux[1], 3), aretes(niveaux[2], 2)]
voisins = [{i: [b if a == i else a for a, b in e if i in (a, b)] for i in niv} for e, niv in zip(E, niveaux)]
# la recherche gloutonne, d'étage en étage
courant = max(niveaux[2], key=d)                                # le point d'entrée : le plus loin de la question, pour l'exemple
trajet = []
for n in (2, 1, 0):
    chemin = [courant]
    while True:
        meilleur = min(voisins[n][courant], key=d)
        if d(meilleur) >= d(courant):
            break
        courant = meilleur
        chemin.append(courant)
    trajet.append((n, chemin))
trouves = sorted(niveaux[0], key=d)[:3]
print("trajet", [(n, len(c)) for n, c in trajet], "arrivée", courant, "vrai plus proche", trouves[0])

# ── la figure ──
W, H = 840, 560
PX, PW, PH, SK = 180, 430, 120, 80                               # les étages, dessinés comme des plans inclinés
Y = {2: 70, 1: 225, 0: 380}
vers = lambda n, p: (PX + p[0] * PW + (1 - p[1]) * SK, Y[n] + p[1] * PH)
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>La recherche dans un graphe à étages</title>",
     "<desc>Trois plans superposés, les étages d'un graphe de vecteurs. L'étage du bas contient tous les vecteurs, reliés à leurs "
     "voisins proches ; l'étage du milieu en contient une quinzaine, reliés à des voisins plus éloignés ; l'étage du haut, "
     "seulement quatre. Une étoile rouge marque la position de la question, au même endroit à chaque étage. La recherche part "
     "d'un point d'entrée à l'étage du haut, fait un grand saut vers la question, descend à l'étage du milieu, se rapproche "
     "encore, puis descend à l'étage du bas, où quelques petits pas l'amènent au plus proche voisin de la question. Les trois "
     "plus proches voisins trouvés sont entourés.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{ROUGE}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="34" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Trouver les plus proches voisins{NB}: descendre d\'étage en étage</text>']
LEG = {2: ("étage 2", "quelques vecteurs,", "de grands sauts"), 1: ("étage 1", "une partie des vecteurs,", "des sauts moyens"),
       0: ("étage 0", "tous les vecteurs,", "de petits pas")}
for n in (2, 1, 0):
    a, b, c, dd = vers(n, (0, 0)), vers(n, (1, 0)), vers(n, (1, 1)), vers(n, (0, 1))
    o.append(f'<path d="M{a[0] - 10} {a[1] - 8} L{b[0] + 10} {b[1] - 8} L{c[0] + 10} {c[1] + 8} L{dd[0] - 10} {dd[1] + 8} Z" '
             f'fill="{PANNEAU}" stroke="{BORD}" stroke-width="1.4"/>')
    l1, l2, l3 = LEG[n]
    o.append(f'<text x="30" y="{Y[n] + 48}" font-size="13" fill="{BRUN}" font-weight="700">{l1}</text>')
    o.append(f'<text x="30" y="{Y[n] + 66}" font-size="11" fill="{ENCRE_PALE}">{l2}</text>')
    o.append(f'<text x="30" y="{Y[n] + 80}" font-size="11" fill="{ENCRE_PALE}">{l3}</text>')
    for i, j in E[n]:
        (x1, y1), (x2, y2) = vers(n, P[i]), vers(n, P[j])
        o.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{AXE}" stroke-width="1"/>')
    for i in niveaux[n]:
        x, y = vers(n, P[i])
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{4.2 if n else 3.4}" fill="{BLEU}"/>')
    qx, qy = vers(n, Q)
    o.append(f'<path d="M{qx} {qy - 8} L{qx + 2.4} {qy - 2.4} L{qx + 8} {qy - 2.4} L{qx + 3.4} {qy + 1.6} L{qx + 5} {qy + 8} '
             f'L{qx} {qy + 4} L{qx - 5} {qy + 8} L{qx - 3.4} {qy + 1.6} L{qx - 8} {qy - 2.4} L{qx - 2.4} {qy - 2.4} Z" fill="{ROUGE}"/>')
# les trois plus proches voisins trouvés
for i in trouves:
    x, y = vers(0, P[i])
    o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="8" fill="none" stroke="{TEAL}" stroke-width="2"/>')
# le trajet
for k, (n, chemin) in enumerate(trajet):
    for a, b in zip(chemin, chemin[1:]):
        (x1, y1), (x2, y2) = vers(n, P[a]), vers(n, P[b])
        o.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{ROUGE}" stroke-width="2.4" marker-end="url(#p)"/>')
    if n > 0:
        (x1, y1), (x2, y2) = vers(n, P[chemin[-1]]), vers(n - 1, P[chemin[-1]])
        o.append(f'<line x1="{x1:.1f}" y1="{y1 + 6:.1f}" x2="{x2:.1f}" y2="{y2 - 7:.1f}" stroke="{ROUGE}" stroke-width="1.6" stroke-dasharray="4 3" marker-end="url(#p)"/>')
x0, y0 = vers(2, P[trajet[0][1][0]])
o.append(f'<text x="{x0:.1f}" y="{y0 - 12:.1f}" font-size="11" fill="{ROUGE}" text-anchor="middle" font-weight="700">entrée</text>')
# la légende
LX = 690
for k, (sym, txt) in enumerate([("etoile", "la question"), ("trajet", "la recherche"), ("rond", "les voisins trouvés")]):
    y = 120 + k * 26
    if sym == "etoile":
        qx, qy = LX + 8, y - 4
        o.append(f'<path d="M{qx} {qy - 8} L{qx + 2.4} {qy - 2.4} L{qx + 8} {qy - 2.4} L{qx + 3.4} {qy + 1.6} L{qx + 5} {qy + 8} '
                 f'L{qx} {qy + 4} L{qx - 5} {qy + 8} L{qx - 3.4} {qy + 1.6} L{qx - 8} {qy - 2.4} L{qx - 2.4} {qy - 2.4} Z" fill="{ROUGE}"/>')
    elif sym == "trajet":
        o.append(f'<line x1="{LX}" y1="{y - 4}" x2="{LX + 18}" y2="{y - 4}" stroke="{ROUGE}" stroke-width="2.4"/>')
    else:
        o.append(f'<circle cx="{LX + 8}" cy="{y - 4}" r="7" fill="none" stroke="{TEAL}" stroke-width="2"/>')
    o.append(f'<text x="{LX + 26}" y="{y}" font-size="11.5" fill="{ENCRE}">{txt}</text>')
o.append(f'<text x="{W / 2}" y="{H - 16}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">Chaque point est un vecteur (un passage){NB}; '
         f'les vecteurs ont des centaines de dimensions, dessinées ici sur deux.</text>')
o.append("</svg>")
(OUT / "hnsw.svg").write_text("\n".join(o) + "\n")
print("hnsw.svg écrit")
