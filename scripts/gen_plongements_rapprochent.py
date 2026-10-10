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

torch.manual_seed(197)                                          # un tirage où les deux paires partent éloignées
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

# ── la figure : le corpus, les plongements qui se rapprochent, la conséquence ──
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
num = lambda v: f"{v * 100:.0f}{NB}%"
nd = lambda v: f"{v:.1f}".replace(".", ",")
COUL = {"chat": TEAL, "chien": TEAL, "camion": BLEU, "tracteur": BLEU}
dist = lambda a, b, k: float(np.linalg.norm(traj[a][k] - traj[b][k]))
D0 = {"animaux": dist("chat", "chien", 0), "vehicules": dist("camion", "tracteur", 0)}
D1 = {"animaux": dist("chat", "chien", -1), "vehicules": dist("camion", "tracteur", -1)}
W, H = 900, 450
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Les plongements se rapprochent</title>",
     "<desc>Trois panneaux reliés par des flèches. 1, le corpus : le chat et le chien mangent, courent, jouent, sautent, boivent "
     "et grandissent ; seul le chat dort ; « le chien dort » n'a jamais été vu. Le camion et le tracteur roulent, freinent, "
     "accélèrent, tournent, reculent et klaxonnent. 2, les plongements à deux dimensions, au départ et à la fin de "
     f"l'entraînement : chat et chien partent à une distance de {nd(D0['animaux'])} et finissent à {nd(D1['animaux'])} ; camion et "
     f"tracteur partent à {nd(D0['vehicules'])} et finissent à {nd(D1['vehicules'])} ; les deux paires restent éloignées l'une de "
     "l'autre. 3, la conséquence : chien étant placé près de chat, le modèle donne à « dort » la même probabilité après « le "
     f"chien » qu'après « le chat », {num(P['dort | le chien'])}, contre {num(P['dort | le tracteur'])} après « le tracteur ». Un "
     "modèle à n-grammes donnerait 0 % à « le chien dort ».</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker>'
     + "".join(f'<marker id="p{n}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
               f'<path d="M0 0 L10 5 L0 10 z" fill="{c}"/></marker>' for n, c in (("t", TEAL), ("b", BLEU))) + '</defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Les mots qui partagent leurs contextes se rapprochent, et l\'un profite de l\'autre</text>']


def panneau(x, w, titre):
    o.append(f'<rect x="{x}" y="54" width="{w}" height="{H - 74}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
    o.append(f'<text x="{x + w / 2}" y="78" font-size="12.5" fill="{BRUN}" text-anchor="middle" font-weight="700">{titre}</text>')


def fleche_entre(x1, x2, y, l1, l2):
    o.append(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{GRIS}" stroke-width="1.8" marker-end="url(#p)"/>')
    o.append(f'<text x="{(x1 + x2) / 2}" y="{y - 26}" font-size="9.5" fill="{ENCRE_PALE}" text-anchor="middle">{l1}</text>')
    o.append(f'<text x="{(x1 + x2) / 2}" y="{y - 14}" font-size="9.5" fill="{ENCRE_PALE}" text-anchor="middle">{l2}</text>')


# 1. le corpus
P1, W1 = 20, 232
panneau(P1, W1, "1. Le corpus")
lignes = [("le chat", "mange, court, joue,", TEAL), ("", "saute, boit, grandit", TEAL),
          ("le chien", "mange, court, joue,", TEAL), ("", "saute, boit, grandit", TEAL),
          ("le chat", "dort", TEAL)]
y = 108
for sujet, verbes, c in lignes:
    if sujet:
        o.append(f'<text x="{P1 + 16}" y="{y}" font-size="12" fill="{c}" font-weight="700">{sujet}</text>')
    o.append(f'<text x="{P1 + 82}" y="{y}" font-size="12" fill="{ENCRE}" font-style="italic">{verbes}</text>')
    y += 20 if not sujet else 18
    if sujet == "" or sujet == "le chat" and verbes == "dort":
        y += 8
o.append(f'<rect x="{P1 + 10}" y="{y - 8}" width="{W1 - 20}" height="28" rx="6" fill="#f6dcd6"/>')
o.append(f'<text x="{P1 + 16}" y="{y + 10}" font-size="12" fill="{ROUGE}" font-weight="700">le chien <tspan font-style="italic" font-weight="400">dort</tspan>{NB}: jamais vu</text>')
y += 46
o.append(f'<text x="{P1 + 16}" y="{y}" font-size="12" fill="{BLEU}" font-weight="700">le camion</text>')
o.append(f'<text x="{P1 + 16}" y="{y + 18}" font-size="12" fill="{BLEU}" font-weight="700">le tracteur</text>')
o.append(f'<text x="{P1 + 104}" y="{y}" font-size="12" fill="{ENCRE}" font-style="italic">roule, freine,</text>')
o.append(f'<text x="{P1 + 104}" y="{y + 18}" font-size="12" fill="{ENCRE}" font-style="italic">accélère, tourne…</text>')
# 2. la carte : départ et arrivée de chaque mot
P2, W2 = 316, 300
panneau(P2, W2, "2. Les plongements se rapprochent")
fleche_entre(P1 + W1 + 6, P2 - 6, 230, "on", "entraîne")
pts = np.array([z for w in suivis for z in (traj[w][0], traj[w][-1])])
lo, hi = pts.min(0), pts.max(0)
marge = 0.15 * (hi - lo)
lo, hi = lo - marge, hi + marge
zx0, zy0, zw, zh = P2 + 20, 96, W2 - 40, H - 74 - 110
vers = lambda z: (zx0 + (z[0] - lo[0]) / (hi[0] - lo[0]) * zw, zy0 + (hi[1] - z[1]) / (hi[1] - lo[1]) * zh)
for w in suivis:
    (x0, y0), (x1, y1) = vers(traj[w][0]), vers(traj[w][-1])
    c = COUL[w]
    dx, dy = x1 - x0, y1 - y0; n = (dx * dx + dy * dy) ** 0.5
    o.append(f'<line x1="{x0 + dx / n * 7:.1f}" y1="{y0 + dy / n * 7:.1f}" x2="{x1 - dx / n * 9:.1f}" y2="{y1 - dy / n * 9:.1f}" stroke="{c}" stroke-width="1.4" stroke-dasharray="4 3" marker-end="url(#p{"t" if c == TEAL else "b"})"/>')
    o.append(f'<circle cx="{x0:.1f}" cy="{y0:.1f}" r="5" fill="{PANNEAU}" stroke="{c}" stroke-width="1.6"/>')
    lx, ly = x0 - dx / n * 12, y0 - dy / n * 12 + 4              # l'étiquette de départ, à l'opposé du déplacement
    ancre = "end" if dx > 0 else "start"
    o.append(f'<text x="{lx:.1f}" y="{ly:.1f}" font-size="10.5" fill="{ENCRE_PALE}" font-style="italic" text-anchor="{ancre}" stroke="{PANNEAU}" stroke-width="4" paint-order="stroke">{w}</text>')
segs = [(np.array(vers(traj[w][0])), np.array(vers(traj[w][-1]))) for w in suivis]


def eloignement(c, w):
    """Distance entre le centre d'une étiquette et le plus proche des traits ou des points (autres que le sien)."""
    d = []
    for a, b in segs:
        u = np.clip((c - a) @ (b - a) / ((b - a) @ (b - a)), 0, 1)
        d.append(np.linalg.norm(c - (a + u * (b - a))))
    d += [np.linalg.norm(c - np.array(vers(traj[v][k]))) for v in suivis for k in (0, -1) if v != w]
    return min(d)


for w in suivis:
    x1, y1 = vers(traj[w][-1])
    o.append(f'<circle cx="{x1:.1f}" cy="{y1:.1f}" r="6" fill="{COUL[w]}"/>')
    larg = 7.5 * len(w)                                           # l'étiquette va du côté le plus dégagé
    cands = [(x1, y1 - 12, "middle", (0, -16)), (x1, y1 + 21, "middle", (0, 16)),
             (x1 + 11, y1 + 4, "start", (11 + larg / 2, 0)), (x1 - 11, y1 + 4, "end", (-11 - larg / 2, 0))]
    lx, ly, ancre, _ = max(cands, key=lambda c: min(eloignement(np.array([x1 + c[3][0] + f * larg / 2, y1 + c[3][1] + g]), w)
                                                    for f in (-1, -0.5, 0, 0.5, 1) for g in (-5, 5)))
    o.append(f'<text x="{lx:.1f}" y="{ly:.1f}" font-size="12.5" fill="{COUL[w]}" font-weight="700" text-anchor="{ancre}" stroke="{PANNEAU}" stroke-width="4" paint-order="stroke">{w}</text>')
yd = H - 74 + 54 - 48
o.append(f'<text x="{P2 + W2 / 2}" y="{yd}" font-size="11" fill="{TEAL}" text-anchor="middle">distance chat–chien{NB}: {nd(D0["animaux"])} → <tspan font-weight="700">{nd(D1["animaux"])}</tspan></text>')
o.append(f'<text x="{P2 + W2 / 2}" y="{yd + 16}" font-size="11" fill="{BLEU}" text-anchor="middle">distance camion–tracteur{NB}: {nd(D0["vehicules"])} → <tspan font-weight="700">{nd(D1["vehicules"])}</tspan></text>')
o.append(f'<text x="{P2 + W2 / 2}" y="{yd + 32}" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">○ au départ, au hasard{NB}{NB}{NB}● à la fin</text>')
# 3. la conséquence
P3, W3 = 670, 210
panneau(P3, W3, "3. Le chien hérite du chat")
fleche_entre(P2 + W2 + 6, P3 - 6, 230, "chien", "près de chat")
o.append(f'<text x="{P3 + 14}" y="{110}" font-size="11.5" fill="{ENCRE}" font-weight="700">probabilité de «{NB}dort{NB}» après…</text>')
barres = [("le chat", "vu", P["dort | le chat"], TEAL), ("le chien", "jamais vu", P["dort | le chien"], TEAL),
          ("le tracteur", "jamais vu", P["dort | le tracteur"], BLEU)]
for k, (lab, note, v, c) in enumerate(barres):
    yy = 128 + k * 50
    o.append(f'<text x="{P3 + 14}" y="{yy + 13}" font-size="12" fill="{ENCRE}" font-style="italic" font-weight="700">{lab}</text>')
    o.append(f'<text x="{P3 + 14}" y="{yy + 28}" font-size="10" fill="{ROUGE if note == "jamais vu" else ENCRE_PALE}">{note}</text>')
    o.append(f'<rect x="{P3 + 92}" y="{yy + 2}" width="{max(2, v * 1000):.1f}" height="16" rx="3" fill="{c}"/>')
    o.append(f'<text x="{P3 + 98 + max(2, v * 1000):.1f}" y="{yy + 15}" font-size="12" fill="{ENCRE}">{num(v)}</text>')
o.append(f'<text x="{P3 + 14}" y="{300}" font-size="10.5" fill="{ENCRE}">Un modèle à n-grammes, qui</text>')
o.append(f'<text x="{P3 + 14}" y="{315}" font-size="10.5" fill="{ENCRE}">ne fait que compter, donnerait</text>')
o.append(f'<text x="{P3 + 14}" y="{330}" font-size="10.5" fill="{ENCRE}"><tspan font-weight="700">0{NB}%</tspan> à «{NB}le chien dort{NB}».</text>')
o.append("</svg>")
(OUT / "plongements-rapprochent.svg").write_text("\n".join(o) + "\n")
print("plongements-rapprochent.svg écrit", {k: round(v, 2) for k, v in D0.items()}, {k: round(v, 2) for k, v in D1.items()})
