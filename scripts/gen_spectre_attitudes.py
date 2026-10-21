# /// script
# requires-python = ">=3.10"
# ///
"""Module 5, « Les attitudes devant l'IA » : le spectre des attitudes sur deux axes. Horizontalement, ce qu'il
faudrait faire du développement de l'IA, de l'accélérer à l'arrêter ; verticalement, les risques qui comptent le plus,
des torts présents aux risques futurs et extrêmes. Positions schématiques."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module5" / "spectre-attitudes.svg"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "

W, H = 900, 560
X0, X1, Y0, Y1 = 110, 860, 470, 80

# (nom, exemples, x de 0 = accélérer à 1 = arrêter, y de 0 = torts présents à 1 = risques futurs, côté de l'étiquette)
ATTITUDES = [
    ("le successionnisme", "Sutton, Faggella", 0.03, 0.95, "d"),
    ("le transhumanisme", "Kurzweil", 0.07, 0.77, "d"),
    ("l'accélérationnisme", "Andreessen, Verdon", 0.06, 0.52, "d"),
    ("la souveraineté", "droite technologique, Europe, Québec", 0.21, 0.32, "d"),
    ("le d/acc", "Buterin", 0.30, 0.64, "d"),
    ("la normalisation", "Narayanan, Kapoor", 0.33, 0.13, "d"),
    ("l'usage pragmatique", "la plupart des gens", 0.45, 0.44, "d"),
    ("la construction prudente", "Anthropic", 0.48, 0.86, "d"),
    ("le souci des IA", "bien-être des modèles", 0.52, 0.66, "d"),
    ("le scepticisme", "Marcus", 0.53, 0.05, "d"),
    ("les voix spirituelles", "Léon XIV", 0.64, 0.38, "d"),
    ("la critique des torts présents", "Gebru, Bender", 0.66, 0.12, "d"),
    ("l'alarme réformiste", "Hinton, Bengio", 0.78, 0.78, "g"),
    ("la protection et le refus", "syndicats, néo-luddites", 0.90, 0.30, "g"),
    ("l'abolition", "Yudkowsky, PauseAI", 0.97, 0.96, "g"),
]


def px(x):
    return X0 + x * (X1 - X0)


def py(y):
    return Y0 - y * (Y0 - Y1)


def couleur(x):
    return TEAL if x < 0.36 else (BLEU if x < 0.62 else ROUGE)


o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Le spectre des attitudes devant l'IA</title>",
     "<desc>Un plan à deux axes. Horizontalement, ce qu'il faudrait faire du développement de l'IA, de « accélérer » à "
     "gauche à « arrêter » à droite. Verticalement, les risques qui comptent le plus, des torts présents en bas aux "
     "risques futurs et extrêmes en haut. À gauche, de haut en bas : le successionnisme, le transhumanisme, "
     "l'accélérationnisme, la souveraineté, le d/acc, la normalisation. Au centre : l'usage pragmatique, la construction "
     "prudente, le souci des IA, le scepticisme, les voix spirituelles. À droite : la critique des torts présents, "
     "l'alarme réformiste, la protection et le refus, et, tout en haut à droite, l'abolition. Positions "
     "schématiques.</desc>",
     '<defs>' + "".join(
         f'<marker id="{n}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto-start-reverse">'
         f'<path d="M0 0 L10 5 L0 10 z" fill="{c}"/></marker>' for n, c in (("p", GRIS),)) + '</defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Le spectre des attitudes devant l\'IA</text>',
     f'<rect x="20" y="48" width="{W - 40}" height="{H - 68}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>']
# zones de fond
for x0, x1, c in ((0, 0.36, TEAL), (0.36, 0.62, BLEU), (0.62, 1, ROUGE)):
    o.append(f'<rect x="{px(x0):.1f}" y="{Y1}" width="{px(x1) - px(x0):.1f}" height="{Y0 - Y1}" fill="{c}" fill-opacity="0.05"/>')
# axes
o.append(f'<line x1="{X0}" y1="{Y0 + 14}" x2="{X1}" y2="{Y0 + 14}" stroke="{GRIS}" stroke-width="1.6" marker-start="url(#p)" marker-end="url(#p)"/>')
o.append(f'<text x="{X0}" y="{Y0 + 34}" font-size="11.5" fill="{TEAL}" font-weight="700">accélérer</text>')
o.append(f'<text x="{(X0 + X1) / 2}" y="{Y0 + 34}" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">Que faire du développement de l\'IA{NB}?</text>')
o.append(f'<text x="{X1}" y="{Y0 + 34}" font-size="11.5" fill="{ROUGE}" font-weight="700" text-anchor="end">arrêter</text>')
o.append(f'<line x1="{X0 - 30}" y1="{Y0}" x2="{X0 - 30}" y2="{Y1}" stroke="{GRIS}" stroke-width="1.6" marker-start="url(#p)" marker-end="url(#p)"/>')
for y, t in ((Y1 + 4, "risques"), (Y1 + 18, "futurs")):
    o.append(f'<text x="{X0 - 44}" y="{y}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="end">{t}</text>')
for y, t in ((Y0 - 14, "torts"), (Y0, "présents")):
    o.append(f'<text x="{X0 - 44}" y="{y}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="end">{t}</text>')
o.append(f'<text x="{X0 - 52}" y="{(Y0 + Y1) / 2}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle" transform="rotate(-90 {X0 - 52} {(Y0 + Y1) / 2})">Quels risques comptent le plus{NB}?</text>')
for nom, ex, x, y, cote in ATTITUDES:
    cx, cy, c = px(x), py(y), couleur(x)
    o.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="6" fill="{c}" stroke="#ffffff" stroke-width="1.5"/>')
    a, dx = ("start", 10) if cote == "d" else ("end", -10)
    o.append(f'<text x="{cx + dx:.1f}" y="{cy - 1:.1f}" font-size="11.5" fill="{c}" text-anchor="{a}" font-weight="700">{nom}</text>')
    o.append(f'<text x="{cx + dx:.1f}" y="{cy + 12:.1f}" font-size="10" fill="{ENCRE_PALE}" text-anchor="{a}">{ex}</text>')
o.append(f'<text x="{X1}" y="{H - 28}" font-size="9.5" fill="{GRIS}" text-anchor="end" font-style="italic">positions schématiques</text>')
o.append("</svg>")
OUT.write_text("\n".join(o) + "\n")
print(OUT.name, "écrit")
