"""Module 4, « Prédire le mot suivant » : comment un grand modèle de langage écrit, jeton après jeton."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "
W, H = 700, 560
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Comment un grand modèle de langage écrit</title>",
     "<desc>Un schéma en cinq étapes, de haut en bas. 1 : le texte « Le capitaine Nemo » est découpé en trois jetons. 2 : chaque "
     "jeton est remplacé par son plongement, une colonne de nombres. 3 : les plongements traversent les couches d'un Transformer, "
     "où chaque jeton ne peut regarder que les jetons qui le précèdent. 4 : à la sortie, le modèle donne une probabilité pour chacun "
     "des jetons du vocabulaire, par exemple 18 % pour « regarda », 11 % pour « sortit ». 5 : on tire un jeton, ici « regarda », "
     "on l'ajoute au texte, et on recommence avec le texte allongé.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker>'
     f'<marker id="pb" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{BRUN}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>']


def etape(y, num, titre):
    o.append(f'<circle cx="38" cy="{y}" r="13" fill="{TEAL}"/>')
    o.append(f'<text x="38" y="{y + 4.5}" font-size="13" fill="#fff" text-anchor="middle" font-weight="700">{num}</text>')
    for k, l in enumerate(titre.split("|")):
        o.append(f'<text x="60" y="{y + 4.5 + 17 * k}" font-size="13.5" fill="{ENCRE}" font-weight="700">{l}</text>')


def fleche(x1, y1, x2, y2):
    o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{GRIS}" stroke-width="1.8" marker-end="url(#p)"/>')


XS = [330, 430, 530]                                  # colonnes des trois jetons
# 1. jetons
etape(40, 1, "Découper en jetons")
for x, j in zip(XS, ["Le", "·capitaine", "·Nemo"]):
    o.append(f'<rect x="{x - 46}" y="24" width="92" height="32" rx="6" fill="{PANNEAU}" stroke="{BLEU}" stroke-width="1.8"/>')
    o.append(f'<text x="{x}" y="45" font-size="13" fill="{ENCRE}" text-anchor="middle" font-family="ui-monospace, Menlo, monospace">{j}</text>')
    fleche(x, 58, x, 82)
# 2. plongements
etape(106, 2, "Remplacer chaque jeton|par son plongement")
for k, x in enumerate(XS):
    for r in range(6):
        teinte = ["#c9d8ea", "#9fbad8", "#e7c9c3", "#d8e6e2", "#b9d3cd", "#efdcc8"][(r + 2 * k) % 6]
        o.append(f'<rect x="{x - 9}" y="{86 + r * 9}" width="18" height="8" fill="{teinte}" stroke="{AXE}" stroke-width="0.6"/>')
    fleche(x, 144, x, 172)
# 3. Transformer
etape(222, 3, "Traverser le Transformer")
o.append(f'<rect x="270" y="176" width="320" height="92" rx="10" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="2"/>')
for c in range(3):
    o.append(f'<line x1="282" y1="{198 + c * 22}" x2="578" y2="{198 + c * 22}" stroke="{BORD}" stroke-width="1"/>')
o.append(f'<text x="430" y="192" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">des dizaines de couches d\'attention</text>')
for (a, b) in [(0, 1), (0, 2), (1, 2)]:                 # chaque jeton regarde les précédents
    o.append(f'<path d="M{XS[a]} 236 Q{(XS[a] + XS[b]) / 2} {212 - 6 * (b - a)} {XS[b]} 236" fill="none" stroke="{BLEU}" stroke-width="1.6" marker-end="url(#p)"/>')
for x in XS:
    o.append(f'<circle cx="{x}" cy="240" r="5" fill="{BLEU}"/>')
o.append(f'<text x="430" y="261" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">chaque jeton ne regarde que ceux qui le précèdent</text>')
fleche(530, 270, 530, 298)
o.append(f'<text x="60" y="242" font-size="11.5" fill="{ENCRE_PALE}">les vecteurs sont modifiés</text>')
o.append(f'<text x="60" y="257" font-size="11.5" fill="{ENCRE_PALE}">d\'après le contexte</text>')
# 4. distribution
etape(318, 4, "Calculer la probabilité|de chaque jeton suivant")
cand = [("·regarda", 18), ("·sortit", 11), (",", 9), ("·me", 7), ("·répondit", 5)]
for k, (j, p) in enumerate(cand):
    y = 304 + k * 19
    o.append(f'<text x="420" y="{y + 11}" font-size="12" fill="{ENCRE}" text-anchor="end" font-family="ui-monospace, Menlo, monospace">{j}</text>')
    o.append(f'<rect x="428" y="{y + 2}" width="{p * 7}" height="12" fill="{BLEU}"/>')
    o.append(f'<text x="{434 + p * 7}" y="{y + 12}" font-size="11.5" fill="{ENCRE_PALE}">{p}{NB}%</text>')
o.append(f'<text x="428" y="{304 + 5 * 19 + 10}" font-size="11.5" fill="{ENCRE_PALE}">… et ainsi pour 200{NB}000 jetons</text>')
o.append(f'<text x="60" y="358" font-size="11.5" fill="{ENCRE_PALE}">(probabilités fictives,</text>')
o.append(f'<text x="60" y="373" font-size="11.5" fill="{ENCRE_PALE}">pour l\'exemple)</text>')
fleche(530, 422, 530, 446)
# 5. tirage et boucle
etape(462, 5, "Tirer un jeton,|l'ajouter")
o.append(f'<rect x="284" y="454" width="292" height="32" rx="6" fill="{PANNEAU}" stroke="{BLEU}" stroke-width="1.8"/>')
o.append(f'<text x="430" y="475" font-size="13" fill="{ENCRE}" text-anchor="middle" font-family="ui-monospace, Menlo, monospace">Le·capitaine·Nemo<tspan fill="{ROUGE}" font-weight="700">·regarda</tspan></text>')
o.append(f'<path d="M578 470 L650 470 L650 40 L582 40" fill="none" stroke="{BRUN}" stroke-width="2" stroke-dasharray="6 5" marker-end="url(#pb)"/>')
o.append(f'<text x="60" y="500" font-size="11.5" fill="{ENCRE_PALE}">selon la température</text>')
o.append(f'<text x="{W / 2}" y="{H - 30}" font-size="12.5" fill="{BRUN}" text-anchor="middle" font-weight="700">On recommence avec le texte allongé, jusqu\'à un jeton spécial qui marque la fin.</text>')
o.append("</svg>")
(OUT / "llm-jeton-apres-jeton.svg").write_text("\n".join(o) + "\n")
print("llm-jeton-apres-jeton.svg écrit")
