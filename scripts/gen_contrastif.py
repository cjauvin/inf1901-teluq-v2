"""Module 4, « Relier les mots et les images » : le principe de l'apprentissage contrastif de CLIP."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "
W, H = 750, 474
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>L'apprentissage contrastif</title>",
     "<desc>Un schéma. Quatre images, à gauche, passent par un encodeur d'images ; quatre légendes, en haut, passent par un encodeur "
     "de textes. Chaque image et chaque légende devient un vecteur. Une grille de quatre sur quatre compare chaque image à chaque "
     "légende. Les quatre cases de la diagonale, qui associent chaque image à sa propre légende, sont marquées « rapprocher » ; les "
     "douze autres cases sont marquées « éloigner ».</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="30" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Rapprocher les bonnes paires, éloigner toutes les autres</text>']
LEG = ["un chat", "un vélo", "une pizza", "méduses"]
ICONES = ["chat", "vélo", "pizza", "méduses"]
c, gx, gy = 70, 300, 170                                   # taille des cases et coin de la grille
# encodeur de textes et légendes
o.append(f'<rect x="{gx}" y="50" width="{4 * c}" height="34" rx="8" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="2"/>')
o.append(f'<text x="{gx + 2 * c}" y="72" font-size="13" fill="{TEAL}" text-anchor="middle" font-weight="700">encodeur de textes</text>')
for j, t in enumerate(LEG):
    x = gx + j * c + c / 2
    o.append(f'<line x1="{x}" y1="86" x2="{x}" y2="{gy - 52}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')
    o.append(f'<text x="{x}" y="{gy - 34}" font-size="11" fill="{ENCRE}" text-anchor="middle">«{FINE}{t}{FINE}»</text>')
    o.append(f'<text x="{x}" y="{gy - 14}" font-size="11" fill="{BLEU}" text-anchor="middle" font-weight="700">T{j + 1}</text>')
# encodeur d'images et images
o.append(f'<rect x="150" y="{gy}" width="40" height="{4 * c}" rx="8" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="2"/>')
o.append(f'<text x="170" y="{gy + 2 * c}" font-size="13" fill="{TEAL}" text-anchor="middle" font-weight="700" transform="rotate(-90 170 {gy + 2 * c})">encodeur d\'images</text>')
for i, t in enumerate(ICONES):
    y = gy + i * c + c / 2
    o.append(f'<rect x="16" y="{y - 22}" width="110" height="44" rx="6" fill="{PANNEAU}" stroke="{AXE}"/>')
    o.append(f'<text x="71" y="{y + 4}" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">[photo{NB}: {t}]</text>')
    o.append(f'<line x1="126" y1="{y}" x2="146" y2="{y}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')
    o.append(f'<line x1="192" y1="{y}" x2="{gx - 26}" y2="{y}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')
    o.append(f'<text x="{gx - 12}" y="{y + 4}" font-size="11" fill="{BLEU}" text-anchor="middle" font-weight="700">I{i + 1}</text>')
# grille
for i in range(4):
    for j in range(4):
        x, y = gx + j * c, gy + i * c
        diag = i == j
        o.append(f'<rect x="{x + 2}" y="{y + 2}" width="{c - 4}" height="{c - 4}" rx="6" fill="{TEAL if diag else PANNEAU}" '
                 f'fill-opacity="{0.85 if diag else 1}" stroke="{TEAL if diag else BORD}"/>')
        o.append(f'<text x="{x + c / 2}" y="{y + c / 2 + 4}" font-size="10.5" fill="{"#fff" if diag else GRIS}" text-anchor="middle" font-weight="{700 if diag else 400}">'
                 f'{"rapprocher" if diag else "éloigner"}</text>')
o.append(f'<text x="{gx + 4 * c + 20}" y="{gy + 30}" font-size="12" fill="{ENCRE}">Chaque case compare</text>')
o.append(f'<text x="{gx + 4 * c + 20}" y="{gy + 46}" font-size="12" fill="{ENCRE}">le vecteur d\'une image</text>')
o.append(f'<text x="{gx + 4 * c + 20}" y="{gy + 62}" font-size="12" fill="{ENCRE}">à celui d\'une légende.</text>')
o.append(f'<text x="{gx + 4 * c + 20}" y="{gy + 98}" font-size="12" fill="{TEAL}" font-weight="700">Diagonale{NB}: l\'image</text>')
o.append(f'<text x="{gx + 4 * c + 20}" y="{gy + 114}" font-size="12" fill="{TEAL}" font-weight="700">et sa vraie légende.</text>')
o.append(f'<text x="{gx + 4 * c + 20}" y="{gy + 150}" font-size="12" fill="{ENCRE_PALE}">Dans CLIP, chaque lot</text>')
o.append(f'<text x="{gx + 4 * c + 20}" y="{gy + 166}" font-size="12" fill="{ENCRE_PALE}">compte des milliers</text>')
o.append(f'<text x="{gx + 4 * c + 20}" y="{gy + 182}" font-size="12" fill="{ENCRE_PALE}">de paires.</text>')
o.append("</svg>")
(OUT / "apprentissage-contrastif.svg").write_text("\n".join(o) + "\n")
print("apprentissage-contrastif.svg écrit")
