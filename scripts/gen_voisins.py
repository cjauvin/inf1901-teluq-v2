"""Module 4, « Des mots aux nombres » : représenter un mot par le sac de ses mots voisins, puis réduire ces immenses listes
à quelques nombres. Comptes et vecteurs illustratifs ; les ressemblances (cosinus) sont calculées sur ces vecteurs."""
from pathlib import Path
import numpy as np

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
num = lambda v: f"{v:.2f}".replace(".", ",").replace("-", "−")
MOTS = ["chat", "chien", "démocratie"]
COUL = [TEAL, TEAL, BLEU]
VOISINS = ["le", "croquettes", "dort", "caresse", "vétérinaire", "miaule", "aboie", "vote", "élection", "liberté"]
C = np.array([[900, 85, 140, 60, 30, 70, 2, 0, 0, 3],
              [950, 90, 120, 55, 40, 1, 75, 0, 0, 4],
              [800, 0, 1, 0, 0, 0, 0, 110, 95, 130]])
V = np.array([[0.80, 0.50, -0.10], [0.70, 0.60, -0.20], [0.10, -0.15, 0.95]])
cos = lambda a, b: a @ b / np.linalg.norm(a) / np.linalg.norm(b)
W, H = 840, 360
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Le sac des mots voisins</title>",
     "<desc>À gauche, un tableau : trois mots en rangées, chat, chien et démocratie, et en colonnes dix mots voisins, avec le "
     "nombre de fois où chacun est apparu près du mot. Chat et chien ont des rangées semblables : croquettes, dort, caresse et "
     "vétérinaire reviennent souvent, et miaule pour l'un, aboie pour l'autre. Démocratie a une rangée différente : vote, élection "
     "et liberté. La colonne du mot « le » est grisée : il est voisin de tout, avec des comptes très élevés pour les trois mots. "
     "Une mention indique 99 990 autres colonnes, presque toutes à zéro. Une flèche « réduire » mène, à droite, à trois vecteurs de "
     "trois nombres seulement. Ceux de chat et de chien se ressemblent, avec une ressemblance de 0,98 ; ceux de chat et de "
     "démocratie, presque pas, avec une ressemblance de −0,1.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Représenter un mot par le sac de ses voisins, puis réduire</text>']
X0, CW, Y0, RH = 120, 46, 150, 40
o.append(f'<text x="{X0 + 5 * CW}" y="64" font-size="12.5" fill="{BRUN}" text-anchor="middle" font-weight="700">combien de fois chaque mot est apparu près de…</text>')
for j, v in enumerate(VOISINS):
    x = X0 + j * CW + CW / 2
    coul = GRIS if v == "le" else ENCRE_PALE
    o.append(f'<text x="{x}" y="{Y0 - 12}" font-size="11.5" fill="{coul}" font-style="italic" transform="rotate(-40 {x} {Y0 - 12})">{v}</text>')
for i, (m, c) in enumerate(zip(MOTS, COUL)):
    y = Y0 + i * RH
    o.append(f'<text x="{X0 - 10}" y="{y + 24}" font-size="13.5" fill="{c}" text-anchor="end" font-weight="700">{m}</text>')
    for j, v in enumerate(VOISINS):
        n = C[i, j]
        if v == "le":
            fond, coulT = "#e4dccb", GRIS
        else:
            a = min(1, n / 140)
            r, g, b = (int(c[k:k + 2], 16) for k in (1, 3, 5))
            fond = "#%02x%02x%02x" % tuple(round(f + (cc - f) * a * 0.8) for f, cc in zip((251, 247, 238), (r, g, b)))
            coulT = "#fbf7ee" if a > 0.6 else ENCRE
        o.append(f'<rect x="{X0 + j * CW + 2}" y="{y + 2}" width="{CW - 4}" height="{RH - 4}" rx="4" fill="{fond}" stroke="{BORD}"/>')
        o.append(f'<text x="{X0 + j * CW + CW / 2}" y="{y + 25}" font-size="12" fill="{coulT}" text-anchor="middle">{n}</text>')
xe = X0 + len(VOISINS) * CW
for i in range(3):
    o.append(f'<text x="{xe + 14}" y="{Y0 + i * RH + 25}" font-size="14" fill="{GRIS}" text-anchor="middle">…</text>')
yb = Y0 + 3 * RH
o.append(f'<text x="{X0 + 5 * CW}" y="{yb + 22}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">…{NB}et 99{NB}990 autres colonnes, une par mot du vocabulaire, presque toutes à 0</text>')
o.append(f'<text x="{X0 + CW / 2}" y="{yb + 44}" font-size="10.5" fill="{GRIS}" text-anchor="middle">«{NB}le{NB}», voisin de tout,</text>')
o.append(f'<text x="{X0 + CW / 2}" y="{yb + 58}" font-size="10.5" fill="{GRIS}" text-anchor="middle">ne dit rien</text>')
# réduire
xa = xe + 34
o.append(f'<line x1="{xa}" y1="{Y0 + 60}" x2="{xa + 50}" y2="{Y0 + 60}" stroke="{GRIS}" stroke-width="1.8" marker-end="url(#p)"/>')
o.append(f'<text x="{xa + 25}" y="{Y0 + 46}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">réduire</text>')
xv, vw = xa + 62, 44
o.append(f'<text x="{xv + 1.5 * vw}" y="64" font-size="12.5" fill="{BRUN}" text-anchor="middle" font-weight="700">quelques nombres</text>')
for i, (m, c) in enumerate(zip(MOTS, COUL)):
    y = Y0 + i * RH
    for k in range(3):
        v = V[i, k]
        r, g, b = (int(c[q:q + 2], 16) for q in (1, 3, 5))
        a = min(1, abs(v))
        fond = "#%02x%02x%02x" % tuple(round(f + (cc - f) * a * 0.7) for f, cc in zip((251, 247, 238), (r, g, b)))
        o.append(f'<rect x="{xv + k * vw + 2}" y="{y + 2}" width="{vw - 4}" height="{RH - 4}" rx="4" fill="{fond}" stroke="{c}" stroke-width="1.2"/>')
        o.append(f'<text x="{xv + k * vw + vw / 2}" y="{y + 25}" font-size="11.5" fill="{"#fbf7ee" if a > 0.7 else ENCRE}" text-anchor="middle">{num(v)}</text>')
yr = yb + 30
o.append(f'<text x="{xv + 1.5 * vw}" y="{yr}" font-size="11" fill="{ENCRE}" text-anchor="middle">ressemblance</text>')
o.append(f'<text x="{xv + 1.5 * vw}" y="{yr + 17}" font-size="11" fill="{TEAL}" text-anchor="middle">chat–chien{NB}: <tspan font-weight="700">{num(cos(V[0], V[1]))}</tspan></text>')
o.append(f'<text x="{xv + 1.5 * vw}" y="{yr + 34}" font-size="11" fill="{BLEU}" text-anchor="middle">chat–démocratie{NB}: <tspan font-weight="700">{num(cos(V[0], V[2]))}</tspan></text>')
o.append("</svg>")
(OUT / "sac-des-voisins.svg").write_text("\n".join(o) + "\n")
print("sac-des-voisins.svg écrit", round(cos(V[0], V[1]), 2), round(cos(V[0], V[2]), 2))
