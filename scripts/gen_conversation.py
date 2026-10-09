"""Module 4, « Prédire le mot suivant » : une conversation avec un modèle de langage (à chaque réplique, tout le texte depuis
le début lui est présenté de nouveau) comparée à une conversation humaine (seule la nouvelle phrase entre, et un état
intérieur évolue)."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
W, H = 840, 500
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Une conversation qui n'en est pas une</title>",
     "<desc>Deux rangées de trois répliques. En haut, une personne : à chaque réplique, seule la nouvelle question entre ; ce qui "
     "change, c'est un état intérieur, dessiné dans une tête, qui grandit et évolue d'une réplique à l'autre. En bas, un modèle de "
     "langage : à la première réplique, il reçoit les instructions de départ et la première question, et produit la première "
     "réponse ; à la deuxième, il reçoit tout cela de nouveau, plus la deuxième question ; à la troisième, encore tout, plus la "
     "troisième question. La barre de texte s'allonge à chaque réplique, alors que le modèle, au milieu, reste identique, avec des "
     "paramètres fixes.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Une conversation{NB}: la personne se souvient, le modèle relit tout</text>']
CX = [175, 435, 695]
SW, SH = 36, 22
COUL = {"inst.": GRIS, "Q": BLEU, "R": TEAL}


def segment(x, y, lab, neuf=False):
    c = ROUGE if neuf else COUL["inst." if lab == "inst." else lab[0]]
    o.append(f'<rect x="{x}" y="{y}" width="{SW - 2}" height="{SH}" rx="4" fill="{c}"/>')
    o.append(f'<text x="{x + SW / 2 - 1}" y="{y + 15}" font-size="10.5" fill="{PANNEAU}" text-anchor="middle" font-weight="700">{lab}</text>')


def fleche(x1, y1, x2, y2):
    o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')


# ── le modèle, en bas ──
o.append('<g transform="translate(0, 202)">')
o.append(f'<rect x="20" y="50" width="{W - 40}" height="214" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
o.append(f'<text x="36" y="72" font-size="13" fill="{BRUN}" font-weight="700">Un modèle de langage{NB}: à chaque réplique, tout le texte est présenté de nouveau</text>')
textes = [["inst.", "Q1"], ["inst.", "Q1", "R1", "Q2"], ["inst.", "Q1", "R1", "Q2", "R2", "Q3"]]
for k, (cx, tx) in enumerate(zip(CX, textes)):
    o.append(f'<text x="{cx}" y="98" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">réplique {k + 1}</text>')
    x0 = cx - len(tx) * SW / 2
    for j, lab in enumerate(tx):
        segment(x0 + j * SW, 108, lab)
    fleche(cx, 134, cx, 150)
    o.append(f'<rect x="{cx - 62}" y="153" width="124" height="38" rx="8" fill="{FOND}" stroke="{TEAL}" stroke-width="1.8"/>')
    o.append(f'<text x="{cx}" y="169" font-size="12" fill="{ENCRE}" text-anchor="middle" font-weight="700">modèle</text>')
    o.append(f'<text x="{cx}" y="184" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">paramètres fixes</text>')
    fleche(cx, 193, cx, 209)
    segment(cx - SW / 2, 212, f"R{k + 1}", neuf=True)
o.append(f'<text x="{W / 2}" y="254" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">le texte s\'allonge à chaque réplique{NB}; le modèle, lui, ne change pas et ne garde rien d\'une réplique à l\'autre</text>')

o.append('</g>')
# ── la personne, en haut ──
o.append('<g transform="translate(0, -226)">')
o.append(f'<rect x="20" y="276" width="{W - 40}" height="190" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
o.append(f'<text x="36" y="298" font-size="13" fill="{BRUN}" font-weight="700">Une personne{NB}: seule la nouvelle phrase entre, et un état intérieur évolue</text>')
etats = [(9, "#9fc7c2"), (14, "#6aa49d"), (19, TEAL)]
for k, (cx, (r, c)) in enumerate(zip(CX, etats)):
    segment(cx - SW / 2, 314, f"Q{k + 1}")
    fleche(cx, 340, cx, 352)
    o.append(f'<circle cx="{cx}" cy="384" r="30" fill="{FOND}" stroke="{ENCRE_PALE}" stroke-width="1.6"/>')
    o.append(f'<circle cx="{cx}" cy="384" r="{r}" fill="{c}"/>')
    fleche(cx, 416, cx, 426)
    segment(cx - SW / 2, 428, f"R{k + 1}", neuf=True)
    if k < 2:
        fleche(cx + 36, 384, CX[k + 1] - 36, 384)
        o.append(f'<text x="{(cx + CX[k + 1]) / 2}" y="376" font-size="10.5" fill="{TEAL}" text-anchor="middle">l\'état intérieur</text>')
        o.append(f'<text x="{(cx + CX[k + 1]) / 2}" y="402" font-size="10.5" fill="{TEAL}" text-anchor="middle">évolue</text>')
o.append('</g>')
o.append(f'<text x="{W / 2}" y="{H - 14}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">inst.{NB}: instructions de départ{NB}; Q{NB}: question{NB}; R{NB}: réponse (en rouge, la réponse produite à cette réplique)</text>')
o.append("</svg>")
(OUT / "conversation.svg").write_text("\n".join(o) + "\n")
print("conversation.svg écrit")
