"""Module 4, « Des mots aux nombres » : deux figures tirées des plongements de l'applet.

Les positions des mots sont calculées à partir des vrais vecteurs fastText de l'applet
(static/html/applets/data/plongements.json, produit par gen_plongements.py), projetés sur leurs deux
premières composantes principales. Seules les positions des deux « avocat » contextuels, dans la seconde
figure, sont schématiques.
"""
import base64, json
from pathlib import Path
import numpy as np

RACINE = Path(__file__).resolve().parent.parent
OUT = RACINE / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "
d = json.loads((RACINE / "static" / "html" / "applets" / "data" / "plongements.json").read_text())
V = np.frombuffer(base64.b64decode(d["v"]), np.int8).reshape(-1, d["dims"]).astype(np.float32)
V /= np.linalg.norm(V, axis=1, keepdims=True)
IDX = {m: i for i, m in enumerate(d["mots"])}


def projeter(mots):
    X = np.stack([V[IDX[m]] for m in mots])
    X -= X.mean(0)
    _, _, Wt = np.linalg.svd(X, full_matrices=False)
    return dict(zip(mots, X @ Wt[:2].T))


def entete(W, H, titre, desc):
    return ['<?xml version="1.0" encoding="UTF-8"?>',
            f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
            f"<title>{titre}</title>", f"<desc>{desc}</desc>",
            f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto">'
            f'<path d="M0 0 L10 5 L0 10 z" fill="{BRUN}"/></marker></defs>',
            f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>']


# ── Figure 1 : un parmi n, ou un plongement ───────────────────────────────────
W, H = 700, 380
o = entete(W, H, "Un numéro par mot, ou un plongement",
           "Deux panneaux. À gauche, trois mots, chat, chien et démocratie, codés chacun par une rangée de cases où une seule "
           "case est pleine, à une position différente : les trois paires de mots sont à la même distance. À droite, une carte "
           "calculée à partir de vrais plongements : chat, chien, lapin et cheval forment un groupe, rouge, bleu et vert un "
           "autre, démocratie, république et liberté un troisième, loin des deux premiers.")
o.append(f'<rect x="20" y="20" width="300" height="{H - 40}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
o.append(f'<rect x="340" y="20" width="340" height="{H - 40}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
o.append(f'<text x="170" y="50" font-size="14.5" fill="{TEAL}" text-anchor="middle" font-weight="700">Un numéro par mot</text>')
o.append(f'<text x="170" y="69" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle">(un parmi n, une case par mot du vocabulaire)</text>')
for r, (mot, k) in enumerate([("chat", 1), ("chien", 4), ("démocratie", 6)]):
    y = 110 + r * 62
    o.append(f'<text x="112" y="{y + 15}" font-size="13.5" fill="{ENCRE}" text-anchor="end" font-weight="600">{mot}</text>')
    for j in range(8):
        o.append(f'<rect x="{122 + j * 20}" y="{y}" width="18" height="22" fill="{BLEU if j == k else FOND}" stroke="{AXE}"/>')
        o.append(f'<text x="{131 + j * 20}" y="{y + 15.5}" font-size="11" fill="{"#fff" if j == k else GRIS}" text-anchor="middle">{1 if j == k else 0}</text>')
    o.append(f'<text x="{122 + 8 * 20 + 8}" y="{y + 15}" font-size="13" fill="{GRIS}">…</text>')
o.append(f'<text x="170" y="{H - 82}" font-size="12.5" fill="{ENCRE}" text-anchor="middle">«{FINE}chat{FINE}» est aussi loin de «{FINE}chien{FINE}»</text>')
o.append(f'<text x="170" y="{H - 64}" font-size="12.5" fill="{ENCRE}" text-anchor="middle">que de «{FINE}démocratie{FINE}» :</text>')
o.append(f'<text x="170" y="{H - 46}" font-size="12.5" fill="{ENCRE}" text-anchor="middle">le code ne dit rien du sens.</text>')
o.append(f'<text x="510" y="50" font-size="14.5" fill="{TEAL}" text-anchor="middle" font-weight="700">Un plongement appris</text>')
o.append(f'<text x="510" y="69" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle">(vrais vecteurs fastText, projetés sur un plan)</text>')
mots = ["chat", "chien", "lapin", "cheval", "démocratie", "république", "liberté", "rouge", "bleu", "vert"]
P = projeter(mots)
xs, ys = np.array([p[0] for p in P.values()]), np.array([p[1] for p in P.values()])
px = lambda x: 380 + (x - xs.min()) / (xs.max() - xs.min()) * 200
py = lambda y: 320 - (y - ys.min()) / (ys.max() - ys.min()) * 220
coul = {**dict.fromkeys(mots[:4], BLEU), **dict.fromkeys(mots[4:7], ROUGE), **dict.fromkeys(mots[7:], TEAL)}
decale = {}                                          # les trois couleurs sont presque confondues : on écarte leurs étiquettes
for k, m in enumerate(sorted(mots[7:], key=lambda m: -P[m][1])):
    decale[m] = (k - 1) * 17
for m, (x, y) in P.items():
    o.append(f'<circle cx="{px(x):.1f}" cy="{py(y):.1f}" r="5" fill="{coul[m]}"/>')
    o.append(f'<text x="{px(x) + 12:.1f}" y="{py(y) + 4.5 + decale.get(m, 0):.1f}" font-size="12.5" fill="{ENCRE}">{m}</text>')
o.append("</svg>")
(OUT / "un-parmi-n-ou-plongement.svg").write_text("\n".join(o) + "\n")

# ── Figure 2 : « avocat », un seul vecteur pour deux sens ─────────────────────
W, H = 700, 400
mots = ["avocat", "tribunal", "juge", "procureur", "fruit", "banane", "tomate"]
JUSTICE, FRUITS = ["tribunal", "juge", "procureur"], ["fruit", "banane", "tomate"]
u = np.mean([V[IDX[m]] for m in FRUITS], 0) - np.mean([V[IDX[m]] for m in JUSTICE], 0)
u /= np.linalg.norm(u)                               # axe horizontal : de la justice vers les fruits
X = np.stack([V[IDX[m]] for m in mots]); X -= X.mean(0)
R = X - np.outer(X @ u, u)                           # axe vertical : la direction principale de ce qui reste
_, _, Wt = np.linalg.svd(R, full_matrices=False)
P = dict(zip(mots, np.stack([X @ u, R @ Wt[0]], 1)))
SIM = {m: float(V[IDX["avocat"]] @ V[IDX[m]]) for m in mots}
xs, ys = np.array([p[0] for p in P.values()]), np.array([p[1] for p in P.values()])
px = lambda x: 120 + (x - xs.min()) / (xs.max() - xs.min()) * 440
py = lambda y: 300 - (y - ys.min()) / (ys.max() - ys.min()) * 200
o = entete(W, H, "Avocat : un seul vecteur pour deux sens",
           "Une carte calculée à partir de vrais plongements. À gauche, tribunal, juge et procureur ; à droite, fruit, banane et "
           "tomate. Le point du mot avocat, un vecteur unique, se trouve du côté de la justice, loin des fruits. Deux flèches "
           "pointillées partent de ce point vers deux points vides, qui figurent les vecteurs contextuels du mot dans deux "
           "phrases : l'un rejoint le groupe de la justice, l'autre le groupe des fruits.")
o.append(f'<text x="{W / 2}" y="34" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">«{FINE}avocat{FINE}»{NB}: un seul vecteur pour deux sens</text>')
for m, (x, y) in P.items():
    if m == "avocat":
        continue
    c = BLEU if m in ("tribunal", "juge", "procureur") else TEAL
    o.append(f'<circle cx="{px(x):.1f}" cy="{py(y):.1f}" r="5.5" fill="{c}"/>')
    o.append(f'<text x="{px(x) + 10:.1f}" y="{py(y) + 4.5:.1f}" font-size="13" fill="{ENCRE}">{m}</text>')
ax, ay = px(P["avocat"][0]), py(P["avocat"][1])
jx = np.mean([px(P[m][0]) for m in JUSTICE]) + 30
jy = np.mean([py(P[m][1]) for m in JUSTICE]) + 70
fx = np.mean([px(P[m][0]) for m in FRUITS]) - 40
fy = np.mean([py(P[m][1]) for m in FRUITS]) + 70
for (cx, cy) in [(jx, jy), (fx, fy)]:
    dx, dy = cx - ax, cy - ay
    n = (dx * dx + dy * dy) ** 0.5
    o.append(f'<line x1="{ax + dx / n * 10:.1f}" y1="{ay + dy / n * 10:.1f}" x2="{cx - dx / n * 10:.1f}" y2="{cy - dy / n * 10:.1f}" '
             f'stroke="{BRUN}" stroke-width="2" stroke-dasharray="6 5" marker-end="url(#p)"/>')
    o.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="7" fill="{FOND}" stroke="{BRUN}" stroke-width="2.5"/>')
o.append(f'<circle cx="{ax:.1f}" cy="{ay:.1f}" r="7.5" fill="{ROUGE}"/>')
o.append(f'<text x="{ax + 12:.1f}" y="{ay - 8:.1f}" font-size="13.5" fill="{ROUGE}" font-weight="700">avocat (vecteur unique)</text>')
o.append(f'<text x="{jx:.1f}" y="{jy + 28:.1f}" font-size="12" fill="{BRUN}" text-anchor="middle">«{FINE}L\'avocat plaide devant le juge.{FINE}»</text>')
o.append(f'<text x="{fx:.1f}" y="{fy + 28:.1f}" font-size="12" fill="{BRUN}" text-anchor="middle">«{FINE}Cet avocat est bien mûr.{FINE}»</text>')
virgule = lambda x: f"{x:.2f}".replace(".", ",")
o.append(f'<text x="{W / 2}" y="{H - 34}" font-size="12" fill="{GRIS}" text-anchor="middle">Axe horizontal{NB}: de la justice vers les fruits. '
         f'Ressemblance avec «{FINE}procureur{FINE}»{NB}: {virgule(SIM["procureur"])}{FINE}; avec «{FINE}banane{FINE}»{NB}: {virgule(SIM["banane"])}.</text>')
o.append(f'<text x="{W / 2}" y="{H - 16}" font-size="12" fill="{GRIS}" text-anchor="middle">Points pleins{NB}: vrais vecteurs fastText. Points vides{NB}: vecteurs contextuels, position schématique.</text>')
o.append("</svg>")
(OUT / "avocat-deux-sens.svg").write_text("\n".join(o) + "\n")
print("un-parmi-n-ou-plongement.svg et avocat-deux-sens.svg écrits")
