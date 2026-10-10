# /// script
# requires-python = ">=3.10,<3.13"
# dependencies = ["torch", "numpy"]
# ///
"""Module 4, « Prédire le mot suivant » : une petite expérience réelle. Un modèle de langage neuronal minuscule, du même type
que celui de 2003 (table de plongements, couche cachée, sortie sur le vocabulaire), est entraîné sur un corpus jouet, avec
des plongements à deux dimensions pour pouvoir les dessiner. Le corpus contient « le chat dort », mais jamais « le chien
dort » ; « le camion démarre », mais jamais « le tracteur démarre ».

La figure montre, à gauche, la trajectoire des plongements pendant l'entraînement, et à droite la probabilité de « dort »
après « le chat », « le chien » et « le tracteur ».

    uv run scripts/gen_plongements_rapprochent.py
"""
from pathlib import Path
import numpy as np
import torch
from torch import nn

torch.manual_seed(8)                                            # un tirage où les deux paires partent éloignées
OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
ANIMAL = ["mange", "court", "joue", "saute", "boit", "grandit"]           # six verbes communs au chat et au chien
VEHICULE = ["roule", "freine", "accélère", "tourne", "recule", "klaxonne"]  # six verbes communs au camion et au tracteur
phrases = [f"le {a} {v}" for a in ("chat", "chien") for v in ANIMAL] + ["le chat dort"] + \
          [f"le {a} {v}" for a in ("camion", "tracteur") for v in VEHICULE] + ["le camion démarre"]
vocab = sorted({m for p in phrases for m in p.split()} | {"<fin>"})
ix = {m: i for i, m in enumerate(vocab)}
X, Y = [], []
for p in phrases:
    m = p.split() + ["<fin>"]
    for k in range(1, len(m)):
        ctx = ([ix["<fin>"]] + [ix[w] for w in m[:k]])[-2:]       # contexte de deux mots
        X.append(ctx); Y.append(ix[m[k]])
X, Y = torch.tensor(X), torch.tensor(Y)


class Modele(nn.Module):
    def __init__(self, v, d=2, h=4):
        super().__init__()
        self.plong = nn.Embedding(v, d)                            # la table des plongements : des paramètres comme les autres
        self.cache = nn.Linear(2 * d, h)
        self.sortie = nn.Linear(h, v)

    def forward(self, x):
        e = self.plong(x).view(len(x), -1)
        return self.sortie(torch.tanh(self.cache(e)))


m = Modele(len(vocab))
with torch.no_grad():
    m.plong.weight.mul_(1.2)
opt = torch.optim.AdamW(m.parameters(), lr=0.02, weight_decay=0.2)   # régularisation, comme au Module 2
suivis = ["chat", "chien", "camion", "tracteur"]
traj = {w: [] for w in suivis}
for pas in range(801):
    if pas % 20 == 0:
        for w in suivis:
            traj[w].append(m.plong.weight[ix[w]].detach().numpy().copy())
    perte = nn.functional.cross_entropy(m(X), Y)
    opt.zero_grad(); perte.backward(); opt.step()


def proba(ctx, mot):
    with torch.no_grad():
        p = torch.softmax(m(torch.tensor([[ix[c] for c in ctx]])), -1)[0]
    return float(p[ix[mot]])


P = {"dort | le chat": proba(["le", "chat"], "dort"), "dort | le chien": proba(["le", "chien"], "dort"),
     "dort | le tracteur": proba(["le", "tracteur"], "dort")}
print("perte finale", round(float(perte), 3), {k: round(v, 2) for k, v in P.items()})

# ── la figure ──
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
num = lambda v: f"{v * 100:.0f}{NB}%"
COUL = {"chat": TEAL, "chien": TEAL, "camion": BLEU, "tracteur": BLEU}
W, H = 840, 430
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Les plongements se rapprochent</title>",
     "<desc>À gauche, une carte des plongements à deux dimensions d'un petit modèle de langage, pendant son entraînement. Chat, "
     "chien, camion et tracteur partent de positions tirées au hasard, marquées par des cercles vides, et suivent une trajectoire "
     "en pointillés jusqu'à leur position finale, marquée par un point plein. À la fin, chat et chien sont voisins, de même que "
     "camion et tracteur. À droite, des barres : la probabilité de « dort » après « le chat », une suite présente dans le corpus, "
     f"vaut {num(P['dort | le chat'])} ; après « le chien », une suite jamais vue, {num(P['dort | le chien'])} ; après « le "
     f"tracteur », {num(P['dort | le tracteur'])}. Un modèle à n-grammes donnerait 0 % à « le chien dort ».</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Pendant l\'entraînement, les mots qui partagent leurs contextes se rapprochent</text>']
# la carte
cx0, cy0, cl = 30, 54, 420
o.append(f'<rect x="{cx0}" y="{cy0}" width="{cl}" height="{H - cy0 - 20}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
o.append(f'<text x="{cx0 + cl / 2}" y="{cy0 + 22}" font-size="12.5" fill="{BRUN}" text-anchor="middle" font-weight="700">Les plongements, du début à la fin de l\'entraînement</text>')
tout = np.array([p for w in suivis for p in traj[w]])
lo, hi = tout.min(0), tout.max(0)
marge = 0.12 * (hi - lo)
lo, hi = lo - marge, hi + marge
ch = H - cy0 - 20 - 80
vers = lambda z: (cx0 + 20 + (z[0] - lo[0]) / (hi[0] - lo[0]) * (cl - 40), cy0 + 40 + (hi[1] - z[1]) / (hi[1] - lo[1]) * ch)
for w in suivis:
    pts = [vers(z) for z in traj[w]]
    c = COUL[w]
    o.append(f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="none" stroke="{c}" stroke-width="1.4" stroke-dasharray="3 3" stroke-opacity="0.8"/>')
    (x0, y0), (x1, y1) = pts[0], pts[-1]
    o.append(f'<circle cx="{x0:.1f}" cy="{y0:.1f}" r="5" fill="{PANNEAU}" stroke="{c}" stroke-width="1.6"/>')
    o.append(f'<circle cx="{x1:.1f}" cy="{y1:.1f}" r="6" fill="{c}"/>')
fins = {w: vers(traj[w][-1]) for w in suivis}
debuts = {w: vers(traj[w][0]) for w in suivis}
for w in suivis:                                                 # étiquettes : au départ (pâle) et à l'arrivée (en couleur)
    (x0, y0), (x1, y1) = debuts[w], fins[w]
    o.append(f'<text x="{x0 + 8:.1f}" y="{y0 - 6:.1f}" font-size="10.5" fill="{ENCRE_PALE}" font-style="italic" stroke="{PANNEAU}" stroke-width="4" paint-order="stroke">{w}</text>')
voisin = {"chat": "chien", "chien": "chat", "camion": "tracteur", "tracteur": "camion"}
for w in suivis:
    x1, y1 = fins[w]
    xv, yv = fins[voisin[w]]
    dy = -10 if y1 <= yv else 18
    o.append(f'<text x="{x1:.1f}" y="{y1 + dy:.1f}" font-size="12.5" fill="{COUL[w]}" font-weight="700" text-anchor="middle" stroke="{PANNEAU}" stroke-width="4" paint-order="stroke">{w}</text>')
yl = H - 46
o.append(f'<circle cx="{cx0 + 40}" cy="{yl}" r="5" fill="{PANNEAU}" stroke="{GRIS}" stroke-width="1.6"/>')
o.append(f'<text x="{cx0 + 52}" y="{yl + 4}" font-size="10.5" fill="{ENCRE_PALE}">au départ, au hasard</text>')
o.append(f'<circle cx="{cx0 + 210}" cy="{yl}" r="6" fill="{GRIS}"/>')
o.append(f'<text x="{cx0 + 222}" y="{yl + 4}" font-size="10.5" fill="{ENCRE_PALE}">à la fin de l\'entraînement</text>')
# les probabilités
bx0 = 470
o.append(f'<rect x="{bx0}" y="{cy0}" width="{W - bx0 - 30}" height="{H - cy0 - 20}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
o.append(f'<text x="{bx0 + (W - bx0 - 30) / 2}" y="{cy0 + 22}" font-size="12.5" fill="{BRUN}" text-anchor="middle" font-weight="700">Ce qu\'il apprend sur l\'un profite à l\'autre</text>')


barres = [("le chat", "vu dans le corpus", P["dort | le chat"], TEAL), ("le chien", "jamais vu", P["dort | le chien"], TEAL),
          ("le tracteur", "jamais vu", P["dort | le tracteur"], BLEU)]
yg = cy0 + 70
o.append(f'<text x="{bx0 + 20}" y="{yg}" font-size="12.5" fill="{ENCRE}" font-weight="700">Probabilité de «{NB}dort{NB}» après…</text>')
for k, (lab, note, v, c) in enumerate(barres):
    yy = yg + 26 + k * 46
    o.append(f'<text x="{bx0 + 20}" y="{yy + 13}" font-size="12" fill="{ENCRE}" font-style="italic" font-weight="700">{lab}</text>')
    o.append(f'<text x="{bx0 + 20}" y="{yy + 28}" font-size="10.5" fill="{ROUGE if note == "jamais vu" else ENCRE_PALE}">{note}</text>')
    o.append(f'<rect x="{bx0 + 110}" y="{yy + 2}" width="{max(2, v * 1400):.1f}" height="16" rx="3" fill="{c}"/>')
    o.append(f'<text x="{bx0 + 116 + max(2, v * 1400):.1f}" y="{yy + 15}" font-size="12" fill="{ENCRE}">{num(v)}</text>')
o.append(f'<text x="{bx0 + 20}" y="{yg + 180}" font-size="11" fill="{ENCRE}">Un modèle à n-grammes, qui ne fait que compter,</text>')
o.append(f'<text x="{bx0 + 20}" y="{yg + 196}" font-size="11" fill="{ENCRE}">donnerait <tspan font-weight="700">0{NB}%</tspan> à «{NB}le chien dort{NB}».</text>')
o.append(f'<text x="{bx0 + (W - bx0 - 30) / 2}" y="{H - 40}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">«{NB}chien{NB}», voisin de «{NB}chat{NB}», hérite de</text>')
o.append(f'<text x="{bx0 + (W - bx0 - 30) / 2}" y="{H - 26}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">ce que le modèle a appris sur «{NB}chat{NB}»</text>')
o.append("</svg>")
(OUT / "plongements-rapprochent.svg").write_text("\n".join(o) + "\n")
print("plongements-rapprochent.svg écrit")
