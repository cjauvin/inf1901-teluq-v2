# /// script
# requires-python = ">=3.10"
# ///
"""Module 5, « Une machine peut-elle être consciente ? » : l'expérience de pensée du remplacement graduel des neurones
(Chalmers, 1995). Quatre étapes, d'un cerveau fait de neurones à un cerveau fait de puces ; le comportement ne change
pas, et la question est de savoir ce que devient la conscience."""
import math
import random
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module5" / "remplacement-neurones.svg"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
rng = random.Random(3)

W, H = 840, 400
RX, RY, PAS = 74, 58, 21
# les nœuds : une grille légèrement décalée, à l'intérieur d'une ellipse
NOEUDS = []
for j in range(-3, 4):
    for i in range(-4, 5):
        x, y = i * PAS + (PAS / 2 if j % 2 else 0), j * PAS * 0.87
        if (x / (RX - 12)) ** 2 + (y / (RY - 10)) ** 2 <= 1:
            NOEUDS.append((x + rng.uniform(-2.5, 2.5), y + rng.uniform(-2.5, 2.5)))
ORDRE = list(range(len(NOEUDS)))
rng.shuffle(ORDRE)
ARETES = [(a, b) for a in range(len(NOEUDS)) for b in range(a + 1, len(NOEUDS))
          if math.dist(NOEUDS[a], NOEUDS[b]) < PAS * 1.25]

o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Le remplacement graduel des neurones</title>",
     "<desc>Quatre cerveaux schématiques, de gauche à droite. Le premier est fait uniquement de neurones ; dans le deuxième, "
     "un tiers des neurones ont été remplacés par des puces de silicium qui font exactement le même travail ; dans le "
     "troisième, deux tiers ; le dernier n'est plus fait que de puces. À chaque étape, la personne répond de la même façon : "
     "« Je vois une tomate rouge. » La question posée en bas : la conscience reste-t-elle, s'estompe-t-elle peu à peu, "
     "ou s'éteint-elle d'un coup ?</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Le remplacement graduel des neurones</text>']

ETIQ = [("tous les neurones", "d'origine"), (f"un tiers remplacé", "par des puces"),
        ("deux tiers", "remplacés"), ("uniquement", "des puces")]
LP = 186
for k in range(4):
    x0 = 20 + k * (LP + 15)
    cx, cy = x0 + LP / 2, 140
    o.append(f'<rect x="{x0}" y="50" width="{LP}" height="232" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
    o.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{RX}" ry="{RY}" fill="{FOND}" stroke="{ENCRE_PALE}" stroke-width="1.6"/>')
    puces = set(ORDRE[:round(len(NOEUDS) * k / 3)])
    for a, b in ARETES:
        (xa, ya), (xb, yb) = NOEUDS[a], NOEUDS[b]
        o.append(f'<line x1="{cx + xa:.1f}" y1="{cy + ya:.1f}" x2="{cx + xb:.1f}" y2="{cy + yb:.1f}" stroke="{AXE}" stroke-width="1"/>')
    for n, (x, y) in enumerate(NOEUDS):
        x, y = cx + x, cy + y
        if n in puces:
            for d in (-3, 0, 3):
                o.append(f'<line x1="{x + d:.1f}" y1="{y - 8:.1f}" x2="{x + d:.1f}" y2="{y + 8:.1f}" stroke="{BLEU}" stroke-width="1"/>')
                o.append(f'<line x1="{x - 8:.1f}" y1="{y + d:.1f}" x2="{x + 8:.1f}" y2="{y + d:.1f}" stroke="{BLEU}" stroke-width="1"/>')
            o.append(f'<rect x="{x - 5.5:.1f}" y="{y - 5.5:.1f}" width="11" height="11" rx="1.5" fill="#ffffff" stroke="{BLEU}" stroke-width="1.6"/>')
        else:
            o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="#ffffff" stroke="{BRUN}" stroke-width="1.6"/>')
            o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.2" fill="{BRUN}"/>')
    l1, l2 = ETIQ[k]
    o.append(f'<text x="{cx}" y="{cy + RY + 26}" font-size="11.5" fill="{ENCRE}" text-anchor="middle" font-weight="700">{l1}</text>')
    o.append(f'<text x="{cx}" y="{cy + RY + 41}" font-size="11.5" fill="{ENCRE}" text-anchor="middle">{l2}</text>')
    o.append(f'<text x="{cx}" y="268" font-size="11" fill="{TEAL}" text-anchor="middle" font-style="italic">« Je vois une tomate rouge. »</text>')
    if k < 3:
        o.append(f'<line x1="{x0 + LP - 6}" y1="{cy}" x2="{x0 + LP + 21}" y2="{cy}" stroke="{GRIS}" stroke-width="1.8" marker-end="url(#p)"/>')

# légende
o.append(f'<circle cx="{W / 2 - 150}" cy="306" r="6" fill="#ffffff" stroke="{BRUN}" stroke-width="1.6"/>')
o.append(f'<circle cx="{W / 2 - 150}" cy="306" r="2.2" fill="{BRUN}"/>')
o.append(f'<text x="{W / 2 - 136}" y="310" font-size="11" fill="{BRUN}">un neurone</text>')
o.append(f'<rect x="{W / 2 + 4.5}" y="300.5" width="11" height="11" rx="1.5" fill="#ffffff" stroke="{BLEU}" stroke-width="1.6"/>')
o.append(f'<text x="{W / 2 + 24}" y="310" font-size="11" fill="{BLEU}">une puce qui fait exactement le même travail</text>')
o.append(f'<text x="{W / 2}" y="342" font-size="12" fill="{ENCRE}" text-anchor="middle">Le comportement ne change à aucune étape. Et la conscience{NB}?</text>')
o.append(f'<text x="{W / 2}" y="366" font-size="12" fill="{ROUGE}" text-anchor="middle" font-weight="700">Reste-t-elle, s\'estompe-t-elle peu à peu, ou s\'éteint-elle d\'un coup{NB}?</text>')
o.append("</svg>")
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(o) + "\n")
print(OUT.name, "écrit,", len(NOEUDS), "nœuds")
