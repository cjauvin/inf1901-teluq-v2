"""Module 4, « Des règles aux probabilités » : l'arbre syntaxique de « Colorless green ideas sleep furiously », produit par
quatre règles de grammaire, et la même phrase à l'envers, qu'aucune règle ne permet d'analyser."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
W, H = 780, 470
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Un arbre syntaxique</title>",
     "<desc>À gauche, quatre règles de grammaire : une phrase est un groupe nominal suivi d'un groupe verbal ; un groupe nominal est "
     "un adjectif suivi d'un groupe nominal, ou un nom seul ; un groupe verbal est un verbe suivi d'un adverbe. Au centre, l'arbre "
     "que ces règles construisent pour « Colorless green ideas sleep furiously » : la phrase se divise en un groupe nominal, "
     "« colorless green ideas », fait de deux adjectifs et d'un nom emboîtés, et un groupe verbal, « sleep furiously », fait d'un "
     "verbe et d'un adverbe. En bas, la même phrase à l'envers, « Furiously sleep ideas green colorless », marquée d'une croix : "
     "aucune combinaison des règles ne permet de la construire.</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Une grammaire générative{NB}: des règles qui construisent les phrases</text>']
# les règles
o.append(f'<rect x="20" y="56" width="214" height="196" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
o.append(f'<text x="36" y="80" font-size="12.5" fill="{BRUN}" font-weight="700">Quatre règles</text>')
regles = [("Phrase", "GN GV"), ("GN", "Adj GN"), ("GN", "Nom"), ("GV", "Verbe Adv")]
for k, (g, d) in enumerate(regles):
    y = 112 + k * 30
    o.append(f'<text x="36" y="{y}" font-size="13" fill="{ENCRE}"><tspan font-weight="700" fill="{TEAL}">{g}</tspan>{NB}→{NB}{d}</text>')
o.append(f'<text x="36" y="{112 + 4 * 30 - 2}" font-size="10.5" fill="{ENCRE_PALE}">GN{NB}: groupe nominal</text>')
o.append(f'<text x="36" y="{112 + 4 * 30 + 13}" font-size="10.5" fill="{ENCRE_PALE}">GV{NB}: groupe verbal</text>')
# l'arbre
mots = ["colorless", "green", "ideas", "sleep", "furiously"]
trad = ["incolores", "vertes", "idées", "dorment", "furieusement"]
xs = [300 + k * 104 for k in range(5)]
Y = {0: 70, 1: 124, 2: 172, 3: 220, 4: 274, 5: 330}
noeuds = {                                                     # nom : (étiquette, x, niveau, enfants)
    "P": ("Phrase", None, 0, ["GN1", "GV"]),
    "GN1": ("GN", None, 1, ["A1", "GN2"]), "GV": ("GV", None, 1, ["V", "ADV"]),
    "GN2": ("GN", None, 2, ["A2", "GN3"]), "GN3": ("GN", xs[2], 3, ["N"]),
    "A1": ("Adj", xs[0], 4, ["m0"]), "A2": ("Adj", xs[1], 4, ["m1"]), "N": ("Nom", xs[2], 4, ["m2"]),
    "V": ("Verbe", xs[3], 4, ["m3"]), "ADV": ("Adv", xs[4], 4, ["m4"]),
}
pos = {f"m{k}": (x, Y[5]) for k, x in enumerate(xs)}


def place(n):
    if n in pos:
        return pos[n]
    et, x, niv, enf = noeuds[n]
    ps = [place(e) for e in enf]
    pos[n] = (x if x is not None else sum(p[0] for p in ps) / len(ps), Y[niv])
    return pos[n]


place("P")
for n, (et, x, niv, enf) in noeuds.items():
    for e in enf:
        (x1, y1), (x2, y2) = pos[n], pos[e]
        o.append(f'<line x1="{x1:.1f}" y1="{y1 + 9}" x2="{x2:.1f}" y2="{y2 - (16 if e.startswith("m") else 14)}" stroke="{AXE}" stroke-width="1.6"/>')
for n, (et, x, niv, enf) in noeuds.items():
    X, Yn = pos[n]
    l = 9 * len(et) + 18
    coul = TEAL if niv <= 3 else BRUN
    o.append(f'<rect x="{X - l / 2:.1f}" y="{Yn - 14}" width="{l}" height="24" rx="12" fill="{PANNEAU}" stroke="{coul}" stroke-width="1.6"/>')
    o.append(f'<text x="{X:.1f}" y="{Yn + 3}" font-size="12.5" fill="{coul}" text-anchor="middle" font-weight="700">{et}</text>')
for k, (x, m, t) in enumerate(zip(xs, mots, trad)):
    o.append(f'<text x="{x}" y="{Y[5]}" font-size="15" fill="{ENCRE}" text-anchor="middle" font-style="italic" font-weight="600">{m}</text>')
    o.append(f'<text x="{x}" y="{Y[5] + 17}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">{t}</text>')
# la phrase à l'envers
yb = 410
o.append(f'<rect x="20" y="{yb - 30}" width="{W - 40}" height="56" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
o.append(f'<circle cx="52" cy="{yb - 2}" r="13" fill="{ROUGE}"/>')
o.append(f'<path d="M46 {yb - 8} L58 {yb + 4} M58 {yb - 8} L46 {yb + 4}" stroke="{PANNEAU}" stroke-width="2.6" stroke-linecap="round"/>')
o.append(f'<text x="78" y="{yb + 3}" font-size="15" fill="{ENCRE}" font-style="italic" font-weight="600">Furiously sleep ideas green colorless</text>')
o.append(f'<text x="{W - 36}" y="{yb + 3}" font-size="11.5" fill="{ROUGE}" text-anchor="end">aucune combinaison des règles ne produit cette phrase</text>')
o.append("</svg>")
(OUT / "arbre-chomsky.svg").write_text("\n".join(o) + "\n")
print("arbre-chomsky.svg écrit")
