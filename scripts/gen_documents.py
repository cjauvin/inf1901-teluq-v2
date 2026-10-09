"""Module 4, « Les outils statistiques » : deux figures sur la représentation des documents.

1. tfidf.svg : le sac de mots (les comptes) et les poids TF-IDF de trois petits documents.
2. lsa.svg : l'analyse sémantique latente sur huit petits documents ; le tableau mots × documents, réduit à deux
   dimensions par décomposition en valeurs singulières, place « médecin » près d'« hôpital », bien qu'ils
   n'apparaissent jamais dans le même document.

    uv run --with numpy python scripts/gen_documents.py
"""
import math
from pathlib import Path
import numpy as np

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "
num = lambda v, d=1: f"{v:.{d}f}".replace(".", ",")


def entete(W, H, titre, desc, sous_titre):
    return ['<?xml version="1.0" encoding="UTF-8"?>',
            f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
            f"<title>{titre}</title>", f"<desc>{desc}</desc>",
            f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
            f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
            f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
            f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">{sous_titre}</text>']


def teinte(v, vmax, coul):                                    # case d'autant plus foncée que la valeur est grande
    r, g, b = (int(coul[i:i + 2], 16) for i in (1, 3, 5))
    a = 0 if vmax == 0 else min(1, v / vmax)
    f = (251, 247, 238)
    return "#%02x%02x%02x" % tuple(round(f[k] + (c - f[k]) * a * 0.85) for k, c in enumerate((r, g, b)))


# ── 1. TF-IDF ──
docs = ["botanique", "biologie", "sport"]
mots = ["le", "photosynthèse", "chlorophylle", "match", "but"]
C = np.array([[12, 10, 15], [3, 1, 0], [2, 0, 0], [0, 0, 4], [0, 0, 3]], float)
df = (C > 0).sum(1)
idf = np.log(len(docs) / df)
T = C * idf[:, None]
W, H = 800, 400
o = entete(W, H, "TF-IDF",
           "Deux tableaux, des mots en rangées et trois documents en colonnes : botanique, biologie et sport. À gauche, le sac de "
           "mots, avec le nombre d'occurrences : le mot « le » apparaît 12, 10 et 15 fois, photosynthèse 3, 1 et 0 fois, chlorophylle "
           "2, 0 et 0 fois, match 0, 0 et 4 fois, but 0, 0 et 3 fois. À droite, les poids TF-IDF : « le », présent dans les trois "
           "documents, reçoit un poids nul partout ; chlorophylle, match et but, propres à un seul document, reçoivent les poids les "
           "plus élevés. En bas, la formule : le poids d'un mot dans un document est son nombre d'occurrences multiplié par le "
           "logarithme du nombre de documents divisé par le nombre de documents qui contiennent le mot.",
           f"Du sac de mots à TF-IDF{NB}: les mots fréquents partout perdent leur poids")


def tableau(x0, titre, sous, M, fmt, coul):
    cw, rh, xm = 76, 34, x0 + 112
    o.append(f'<text x="{x0 + 112 + 1.5 * cw}" y="66" font-size="13" fill="{BRUN}" text-anchor="middle" font-weight="700">{titre}</text>')
    o.append(f'<text x="{x0 + 112 + 1.5 * cw}" y="82" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">{sous}</text>')
    for j, d in enumerate(docs):
        o.append(f'<text x="{xm + j * cw + cw / 2}" y="106" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle" font-style="italic">{d}</text>')
    vmax = M.max()
    for i, m in enumerate(mots):
        y = 116 + i * rh
        o.append(f'<text x="{xm - 10}" y="{y + 21}" font-size="12" fill="{ENCRE}" text-anchor="end">{m}</text>')
        for j in range(len(docs)):
            v = M[i, j]
            o.append(f'<rect x="{xm + j * cw + 2}" y="{y}" width="{cw - 4}" height="{rh - 4}" rx="4" fill="{teinte(v, vmax, coul)}" stroke="{BORD}"/>')
            o.append(f'<text x="{xm + j * cw + cw / 2}" y="{y + 20}" font-size="12" fill="{ENCRE}" text-anchor="middle">{fmt(v)}</text>')


tableau(20, "Sac de mots", "nombre d'occurrences", C, lambda v: str(int(v)), BLEU)
tableau(420, "TF-IDF", "occurrences × rareté", T, lambda v: "0" if v == 0 else num(v), TEAL)
o.append(f'<line x1="392" y1="200" x2="420" y2="200" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')
o.append(f'<text x="{W / 2}" y="{H - 44}" font-size="13" fill="{ENCRE}" text-anchor="middle">poids{NB}={NB}occurrences{NB}×{NB}log'
         f'<tspan font-size="10" dy="3">{NB}</tspan><tspan dy="-3">(</tspan>nombre de documents{NB}/{NB}documents qui contiennent le mot)</text>')
o.append(f'<text x="{W / 2}" y="{H - 22}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">«{NB}le{NB}» est dans les trois documents{NB}: log(3{NB}/{NB}3){NB}={NB}0, son poids s\'annule partout</text>')
o.append("</svg>")
(OUT / "tfidf.svg").write_text("\n".join(o) + "\n")

# ── 2. LSA ──
corpus = [["médecin", "patient", "soigne", "maladie"], ["médecin", "patient", "maladie"],
          ["hôpital", "patient", "soigne", "urgence"], ["hôpital", "urgence", "maladie", "blessure"],
          ["match", "équipe", "but", "joueur", "blessure"], ["équipe", "joueur", "match"],
          ["match", "but", "arbitre", "équipe"], ["arbitre", "joueur", "but"]]
vocab = ["médecin", "hôpital", "patient", "soigne", "maladie", "urgence", "blessure",
         "match", "équipe", "but", "joueur", "arbitre"]
SANTE, SPORT, PARTAGE = range(0, 6), range(7, 12), 6
M = np.array([[d.count(w) for d in corpus] for w in vocab], float)
U, S, Vt = np.linalg.svd(M, full_matrices=False)
Z = U[:, :2] * S[:2]                                           # chaque mot devient un point à deux coordonnées
Z = Z @ np.array([[1, -1], [1, 1]]) / np.sqrt(2)                # rotation de 45°, pour une carte plus lisible
assert not any(M[0, j] and M[1, j] for j in range(len(corpus)))   # médecin et hôpital : jamais dans le même document
W, H = 800, 440
o = entete(W, H, "L'analyse sémantique latente",
           "À gauche, un tableau de 12 mots sur 8 petits documents, avec une case colorée quand le mot apparaît dans le document. "
           "Les quatre premiers documents parlent de santé, les quatre derniers de sport. « Médecin » n'apparaît que dans les "
           "documents 1 et 2, « hôpital » que dans les documents 3 et 4 : jamais ensemble. Une flèche indique la réduction à deux "
           "dimensions. À droite, la carte obtenue : chaque mot est un point. Les mots de la santé se regroupent d'un côté, ceux du "
           "sport de l'autre, « blessure », présent dans les deux thèmes, entre les deux, et « médecin » et « hôpital » sont voisins.",
           f"L'analyse sémantique latente{NB}: des mots aux vecteurs")
cw, rh, x0, y0 = 22, 22, 112, 84
o.append(f'<text x="{x0 + 4 * cw}" y="66" font-size="12.5" fill="{BRUN}" text-anchor="middle" font-weight="700">mots × documents</text>')
for j in range(len(corpus)):
    o.append(f'<text x="{x0 + j * cw + cw / 2}" y="{y0 - 4}" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">{j + 1}</text>')
for i, w in enumerate(vocab):
    y = y0 + i * rh
    coul = ROUGE if i < 2 else ENCRE
    o.append(f'<text x="{x0 - 8}" y="{y + 15}" font-size="11" fill="{coul}" text-anchor="end" font-weight="{700 if i < 2 else 400}">{w}</text>')
    for j in range(len(corpus)):
        on = M[i, j] > 0
        c = (ROUGE if i < 2 else (TEAL if j < 4 else BLEU)) if on else PANNEAU
        o.append(f'<rect x="{x0 + j * cw + 1}" y="{y + 1}" width="{cw - 2}" height="{rh - 2}" rx="2" fill="{c}" stroke="{BORD}" stroke-width="0.8"/>')
o.append(f'<text x="{x0 + 2 * cw}" y="{y0 + len(vocab) * rh + 18}" font-size="10.5" fill="{TEAL}" text-anchor="middle">santé</text>')
o.append(f'<text x="{x0 + 6 * cw}" y="{y0 + len(vocab) * rh + 18}" font-size="10.5" fill="{BLEU}" text-anchor="middle">sport</text>')
xa = x0 + 8 * cw + 14
o.append(f'<line x1="{xa}" y1="216" x2="{xa + 62}" y2="216" stroke="{GRIS}" stroke-width="1.8" marker-end="url(#p)"/>')
o.append(f'<text x="{xa + 31}" y="202" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">réduire à</text>')
o.append(f'<text x="{xa + 31}" y="236" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">2 dimensions</text>')
# la carte : les mots en points, les deux thèmes nommés
cx0, cy0, cl, ch = 400, 60, 370, 360
o.append(f'<rect x="{cx0}" y="{cy0}" width="{cl}" height="{ch}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
lo, hi = Z.min(0), Z.max(0)
marge = 0.2 * (hi - lo)
lo, hi = lo - marge, hi + marge
vers = lambda z: (cx0 + 20 + (z[0] - lo[0]) / (hi[0] - lo[0]) * (cl - 40), cy0 + 30 + (hi[1] - z[1]) / (hi[1] - lo[1]) * (ch - 100))
for groupe, coul, nom in ((SANTE, TEAL, "santé"), (SPORT, BLEU, "sport")):
    P = np.array([vers(Z[i]) for i in groupe])
    gx, gy = P.mean(0)
    o.append(f'<text x="{gx:.1f}" y="{P[:, 1].min() - 18:.1f}" font-size="13" fill="{coul}" text-anchor="middle" font-weight="700">{nom}</text>')
NOMMES = {"médecin": (10, 4, "start"), "hôpital": (0, 22, "middle"), "blessure": (0, 20, "middle")}
for i, w in enumerate(vocab):
    X, Y = vers(Z[i])
    coul = ROUGE if i < 2 else (GRIS if i == PARTAGE else (TEAL if i in SANTE else BLEU))
    o.append(f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="{5.5 if i < 2 else 4}" fill="{coul}" stroke="{PANNEAU}" stroke-width="1"/>')
    if w in NOMMES:
        ddx, ddy, ancre = NOMMES[w]
        o.append(f'<text x="{X + ddx:.1f}" y="{Y + ddy:.1f}" font-size="{12.5 if i < 2 else 11}" fill="{coul}" text-anchor="{ancre}" font-weight="{700 if i < 2 else 400}">{w}</text>')
o.append(f'<text x="{cx0 + cl / 2}" y="{cy0 + ch - 34}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">«{NB}médecin{NB}» et «{NB}hôpital{NB}» ne sont jamais dans le même document,</text>')
o.append(f'<text x="{cx0 + cl / 2}" y="{cy0 + ch - 18}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">mais ils fréquentent les mêmes mots{NB}: ils deviennent voisins</text>')
o.append("</svg>")
(OUT / "lsa.svg").write_text("\n".join(o) + "\n")
print("tfidf.svg et lsa.svg écrits")
print({w: Z[i].round(2).tolist() for i, w in enumerate(vocab)})
