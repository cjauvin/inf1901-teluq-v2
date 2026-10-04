"""Module 4, « Générer : imiter une distribution » : la température.

La fréquence approximative des lettres en français (accents confondus), transformée à trois
températures (p^(1/T), renormalisé), et vingt-quatre lettres tirées au hasard à chaque température.
"""
import random
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
FREQ = {"e": 14.7, "s": 7.9, "a": 7.6, "i": 7.5, "t": 7.2, "n": 7.1, "r": 6.7, "u": 6.3, "o": 5.8, "l": 5.5,
        "d": 3.7, "c": 3.3, "p": 3.0, "m": 3.0, "v": 1.6, "q": 1.4, "f": 1.1, "b": 0.9, "g": 0.9, "h": 0.7,
        "j": 0.6, "x": 0.4, "y": 0.3, "z": 0.1, "w": 0.1, "k": 0.05}
LETTRES = list(FREQ)
RANGEES = [(0.3, "Température basse (0,3)", "presque toujours la lettre la plus probable"),
           (1.0, "Température 1", "les fréquences du français, telles quelles"),
           (3.0, "Température haute (3)", "la distribution s'aplatit, les lettres rares sortent")]


def transformer(t):
    p = {l: f ** (1 / t) for l, f in FREQ.items()}
    s = sum(p.values())
    return {l: v / s for l, v in p.items()}


W, h_r, y0 = 700, 168, 58
H = y0 + 3 * h_r + 14
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>La température</title>",
     "<desc>Trois diagrammes à barres superposés donnent la probabilité de tirer chaque lettre, de e à k, classées de la plus "
     "fréquente à la plus rare. À température basse, la barre du e domine toutes les autres, et le tirage ne donne presque que "
     "des e. À température 1, les barres suivent les fréquences du français, et le tirage mêle des lettres courantes. À "
     "température haute, les barres sont presque toutes de la même hauteur, et le tirage contient des lettres rares comme "
     "w, k ou z.</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="34" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Tirer des lettres au hasard, à trois températures</text>']
rnd = random.Random(4)
x_b, l_b, pas = 40, 14, 18
for k, (t, titre, glose) in enumerate(RANGEES):
    y = y0 + k * h_r
    o.append(f'<rect x="20" y="{y}" width="{W - 40}" height="{h_r - 12}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
    o.append(f'<text x="40" y="{y + 26}" font-size="14" fill="{TEAL}" font-weight="700">{titre}</text>')
    o.append(f'<text x="{W - 40}" y="{y + 26}" font-size="12.5" fill="{ENCRE_PALE}" text-anchor="end">{glose}</text>')
    p = transformer(t)
    base, hmax = y + 112, 70
    o.append(f'<line x1="{x_b - 6}" y1="{base}" x2="{x_b + 26 * pas - 2}" y2="{base}" stroke="{AXE}" stroke-width="1"/>')
    for i, l in enumerate(LETTRES):
        hb = hmax * p[l] / max(p.values())          # chaque rangée à sa propre échelle : on compare des formes
        x = x_b + i * pas
        o.append(f'<rect x="{x:.1f}" y="{base - hb:.1f}" width="{l_b}" height="{max(hb, 0.6):.1f}" fill="{BLEU}" opacity="0.85"/>')
        o.append(f'<text x="{x + l_b / 2:.1f}" y="{base + 15}" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">{l}</text>')
    tirage = "".join(rnd.choices(LETTRES, weights=[p[l] for l in LETTRES], k=24))
    xs = x_b + 26 * pas + 22
    o.append(f'<text x="{xs}" y="{y + 66}" font-size="12.5" fill="{ENCRE_PALE}">tirage{NB}:</text>')
    o.append(f'<text x="{xs}" y="{y + 90}" font-size="15" fill="{ROUGE}" font-family="ui-monospace, Menlo, monospace" font-weight="700">{tirage[:12]}</text>')
    o.append(f'<text x="{xs}" y="{y + 110}" font-size="15" fill="{ROUGE}" font-family="ui-monospace, Menlo, monospace" font-weight="700">{tirage[12:]}</text>')
o.append("</svg>")
(OUT / "temperature-lettres.svg").write_text("\n".join(o) + "\n")
print("temperature-lettres.svg écrit")
