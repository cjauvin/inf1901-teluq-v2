"""Module 4, « Programmer avec des agents » : un tube Unix. Cinq petits programmes, reliés par le symbole |, répondent à la
question « qui a fait le plus de modifications dans ce projet ? » ; on voit le texte passer de l'un à l'autre."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
TERM, TERM_TXT = "#1f2421", "#e5e7e0"
W, H = 840, 390
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Un tube Unix</title>",
     "<desc>La question : qui a fait le plus de modifications dans ce projet ? En bas, la ligne de commande qui y répond : git log "
     "--format=%an, puis sort, puis uniq -c, puis sort -rn, puis head -2, reliés par le symbole |, le tube. Au-dessus, cinq "
     "boîtes, une par programme, avec le texte qui sort de chacune. git log donne le nom de l'auteur de chaque modification : "
     "Grace, Ada, Grace, Linus, Grace, Ada. sort les trie : Ada, Ada, Grace, Grace, Grace, Linus. uniq -c compte les lignes "
     "identiques qui se suivent : 2 Ada, 3 Grace, 1 Linus. sort -rn trie par nombre, du plus grand au plus petit : 3 Grace, 2 "
     "Ada, 1 Linus. head -2 garde les deux premières lignes : 3 Grace, 2 Ada. Chaque programme fait une seule chose, lit du "
     "texte et en produit.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Un tube Unix{NB}: de petits programmes, reliés par du texte</text>',
     f'<text x="{W / 2}" y="56" font-size="12.5" fill="{ENCRE_PALE}" text-anchor="middle" font-style="italic">«{NB}Qui a fait le plus de modifications dans ce projet{NB}?{NB}»</text>']
ETAPES = [("git log --format=%an", "l'auteur de chaque", "modification", ["Grace", "Ada", "Grace", "Linus", "Grace", "Ada"]),
          ("sort", "trie les lignes", "", ["Ada", "Ada", "Grace", "Grace", "Grace", "Linus"]),
          ("uniq -c", "compte les lignes", "identiques voisines", ["2 Ada", "3 Grace", "1 Linus"]),
          ("sort -rn", "trie par nombre,", "du plus grand", ["3 Grace", "2 Ada", "1 Linus"]),
          ("head -2", "garde les deux", "premières lignes", ["3 Grace", "2 Ada"])]
BW, GAP, X0 = 140, 26, 26
for k, (cmd, l1, l2, sortie) in enumerate(ETAPES):
    x = X0 + k * (BW + GAP)
    o.append(f'<rect x="{x}" y="76" width="{BW}" height="66" rx="9" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="1.8"/>')
    o.append(f'<text x="{x + BW / 2}" y="98" font-size="{10 if len(cmd) > 12 else 11.5}" fill="{TEAL}" text-anchor="middle" font-weight="700" font-family="ui-monospace, Menlo, monospace">{cmd}</text>')
    o.append(f'<text x="{x + BW / 2}" y="117" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">{l1}</text>')
    if l2:
        o.append(f'<text x="{x + BW / 2}" y="131" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">{l2}</text>')
    o.append(f'<line x1="{x + BW / 2}" y1="144" x2="{x + BW / 2}" y2="160" stroke="{GRIS}" stroke-width="1.4" marker-end="url(#p)"/>')
    o.append(f'<rect x="{x + 10}" y="164" width="{BW - 20}" height="{16 * 6 + 12}" rx="5" fill="{TERM}"/>')
    for j, l in enumerate(sortie):
        o.append(f'<text x="{x + 22}" y="{182 + 16 * j}" font-size="11" fill="{TERM_TXT}" font-family="ui-monospace, Menlo, monospace">{l}</text>')
    if k < len(ETAPES) - 1:
        xa = x + BW - 10
        o.append(f'<path d="M{xa} {218} C {xa + 22} {218} {x + BW + GAP - 6} {109} {x + BW + GAP + 2} {109}" fill="none" stroke="{GRIS}" stroke-width="1.4" marker-end="url(#p)"/>')
        o.append(f'<text x="{x + BW + GAP / 2 + 2}" y="{176}" font-size="15" fill="{BRUN}" text-anchor="middle" font-weight="700" font-family="ui-monospace, Menlo, monospace" stroke="{FOND}" stroke-width="4" paint-order="stroke">|</text>')
# la ligne de commande complète
o.append(f'<rect x="26" y="298" width="{W - 52}" height="34" rx="6" fill="{TERM}"/>')
o.append(f'<text x="40" y="320" font-size="12.5" fill="{TERM_TXT}" font-family="ui-monospace, Menlo, monospace">'
         f'<tspan fill="#8fd3c9">$</tspan>\u00a0git log --format=%an <tspan fill="#e0a36b">|</tspan> sort <tspan fill="#e0a36b">|</tspan> uniq -c '
         f'<tspan fill="#e0a36b">|</tspan> sort -rn <tspan fill="#e0a36b">|</tspan> head -2</text>')
o.append(f'<text x="{W / 2}" y="358" font-size="11.5" fill="{ENCRE}" text-anchor="middle">Le symbole <tspan font-family="ui-monospace, Menlo, monospace" fill="{BRUN}" font-weight="700">|</tspan>, le tube, envoie le texte produit par un programme au suivant.</text>')
o.append(f'<text x="{W / 2}" y="376" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">Aucun de ces programmes ne sait répondre à la question{NB}; ensemble, en une ligne, ils y répondent.</text>')
o.append("</svg>")
(OUT / "tube-unix.svg").write_text("\n".join(o) + "\n")
print("tube-unix.svg écrit")
