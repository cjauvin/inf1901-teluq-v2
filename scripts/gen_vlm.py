"""Module 4, « Des modèles qui voient, entendent et parlent » : comment un modèle de langage lit une image."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "
W, H = 700, 330
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Un modèle de langage qui lit une image</title>",
     "<desc>Un schéma. Une image est découpée en carreaux, qui passent par un encodeur d'images. Une projection transforme chaque "
     "vecteur obtenu en un jeton visuel, de même forme que les jetons de mots. Les jetons visuels et les jetons de la question « Combien "
     "de personnes traversent ? » forment une seule séquence, que lit le modèle de langage. Le modèle répond par du texte, jeton après "
     "jeton.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="30" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Des carreaux d\'image lus comme des mots</text>']


def fleche(x1, y1, x2, y2):
    o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{GRIS}" stroke-width="1.8" marker-end="url(#p)"/>')


# image en carreaux
o.append(f'<rect x="24" y="56" width="96" height="96" fill="#b9c7d6" stroke="{AXE}"/>')
for k in range(1, 4):
    o.append(f'<line x1="{24 + 24 * k}" y1="56" x2="{24 + 24 * k}" y2="152" stroke="#fff" stroke-width="1.5"/>')
    o.append(f'<line x1="24" y1="{56 + 24 * k}" x2="120" y2="{56 + 24 * k}" stroke="#fff" stroke-width="1.5"/>')
o.append(f'<text x="72" y="172" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle">une image en carreaux</text>')
fleche(124, 104, 156, 104)
o.append(f'<rect x="160" y="70" width="110" height="68" rx="10" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="2"/>')
o.append(f'<text x="215" y="98" font-size="12.5" fill="{TEAL}" text-anchor="middle" font-weight="700">encodeur</text>')
o.append(f'<text x="215" y="115" font-size="12.5" fill="{TEAL}" text-anchor="middle" font-weight="700">d\'images</text>')
fleche(272, 104, 300, 104)
o.append(f'<rect x="304" y="78" width="92" height="52" rx="10" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="2"/>')
o.append(f'<text x="350" y="109" font-size="12.5" fill="{TEAL}" text-anchor="middle" font-weight="700">projection</text>')
fleche(350, 132, 350, 190)
# séquence
xs = 60
o.append(f'<text x="650" y="184" font-size="12" fill="{ENCRE_PALE}" text-anchor="end">la séquence lue par le modèle de langage</text>')
for k in range(6):
    o.append(f'<rect x="{xs + k * 34}" y="196" width="30" height="30" rx="4" fill="#b9c7d6" stroke="{BLEU}" stroke-width="1.4"/>')
o.append(f'<text x="{xs + 6 * 34 + 2}" y="216" font-size="13" fill="{GRIS}">…</text>')
for k, mot in enumerate(["Combien", "·de", "·personnes", "·traversent", "·?"]):
    l = 18 + 7.2 * len(mot)
    x = xs + 6 * 34 + 22 + sum(18 + 7.2 * len(m) + 4 for m in ["Combien", "·de", "·personnes", "·traversent", "·?"][:k])
    o.append(f'<rect x="{x:.1f}" y="196" width="{l:.1f}" height="30" rx="4" fill="{PANNEAU}" stroke="{BRUN}" stroke-width="1.4"/>')
    o.append(f'<text x="{x + l / 2:.1f}" y="215" font-size="11.5" fill="{ENCRE}" text-anchor="middle" font-family="ui-monospace, Menlo, monospace">{mot}</text>')
o.append(f'<text x="{xs + 100}" y="244" font-size="11.5" fill="{BLEU}" text-anchor="middle">jetons visuels</text>')
o.append(f'<text x="{xs + 420}" y="244" font-size="11.5" fill="{BRUN}" text-anchor="middle">jetons de texte</text>')
fleche(350, 252, 350, 268)
o.append(f'<rect x="200" y="270" width="300" height="40" rx="10" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="2"/>')
o.append(f'<text x="350" y="295" font-size="13" fill="{TEAL}" text-anchor="middle" font-weight="700">modèle de langage → «{FINE}Sept personnes…{FINE}»</text>')
o.append("</svg>")
(OUT / "modele-qui-voit.svg").write_text("\n".join(o) + "\n")
print("modele-qui-voit.svg écrit")
