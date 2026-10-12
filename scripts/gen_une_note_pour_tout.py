"""Module 4, « Du modèle à l'assistant » : imiter ou être noté. Pendant le préentraînement, chaque jeton reçoit sa propre
correction ; pendant le renforcement, le modèle tire plusieurs réponses complètes, et chacune reçoit une seule note, qui pousse
tous ses jetons dans le même sens, y compris une bonne étape dans une réponse fausse. Sur un grand nombre d'essais, ce qui est
commun s'annule et ce qui distingue les bonnes réponses se dégage. Réponses et bilan illustratifs."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
VERT_PALE, ROUGE_PALE = "#dcebe8", "#f6dcd6"
W, H = 840, 624
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Imiter ou être noté</title>",
     "<desc>Trois parties. En haut, imiter : dans un texte écrit par d'autres, « Il en reste 23 − 20 = 3 », le bon jeton est "
     "connu à chaque position, et chaque jeton reçoit sa propre correction. Au milieu, le renforcement : à la question de la "
     "cafétéria, qui avait 23 pommes, en utilise 20 et en achète 6, le modèle tire quatre réponses complètes. Deux mènent à 9 et "
     "reçoivent la note 1 : tous leurs jetons sont rendus plus probables. Deux mènent à une réponse fausse, 49 et 18, et reçoivent "
     "la note 0 : tous leurs jetons sont rendus moins probables. La dernière contient pourtant une bonne étape, 23 − 20 = 3, "
     "pénalisée quand même, parce que la note ne dit pas quelle étape était fautive. En bas, sur un grand nombre d'essais : "
     "« Elle avait 23 pommes », présent dans toutes les réponses, est poussé dans les deux sens et l'effet s'annule ; "
     "« 23 − 20 = 3 », plus fréquent dans les bonnes réponses, est renforcé ; « 3 × 6 = 18 », présent seulement dans les "
     "mauvaises, est affaibli.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker>'
     f'<marker id="pr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{ROUGE}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Imiter, ou recevoir une seule note pour toute la réponse</text>']


def panneau(y, h, titre, sous):
    o.append(f'<rect x="20" y="{y}" width="{W - 40}" height="{h}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
    o.append(f'<text x="36" y="{y + 24}" font-size="13" fill="{BRUN}" font-weight="700">{titre}</text>')
    o.append(f'<text x="36" y="{y + 42}" font-size="11" fill="{ENCRE_PALE}">{sous}</text>')


def case(x, y, texte, w, fond=PANNEAU, bord=BORD, coul=ENCRE, h=26, taille=12):
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fond}" stroke="{bord}" stroke-width="1.2"/>')
    o.append(f'<text x="{x + w / 2}" y="{y + h / 2 + 4.5}" font-size="{taille}" fill="{coul}" text-anchor="middle">{texte}</text>')


# ── 1. imiter ──
panneau(52, 118, "1. Imiter (préentraînement, ajustement par instructions)",
        f"le texte est écrit par d'autres{NB}: à chaque position, on connaît le bon jeton")
x = 60
for j in ["Il", "en", "reste", "23", "−", "20", "=", "3"]:
    w = 18 + 8 * len(j)
    case(x, 104, j, w, fond="#e6eef6", bord=BLEU)
    o.append(f'<line x1="{x + w / 2}" y1="{148}" x2="{x + w / 2}" y2="{134}" stroke="{BLEU}" stroke-width="1.3" marker-end="url(#p)"/>')
    x += w + 8
o.append(f'<text x="{x + 16}" y="{122}" font-size="12" fill="{BLEU}" font-weight="700">une correction</text>')
o.append(f'<text x="{x + 16}" y="{139}" font-size="12" fill="{BLEU}" font-weight="700">par jeton</text>')
o.append(f'<text x="60" y="{162}" font-size="10.5" fill="{ENCRE_PALE}">l\'erreur est mesurée sur chaque jeton, et chacun est corrigé pour lui-même</text>')

# ── 2. le renforcement ──
PY = 184
panneau(PY, 252, "2. Renforcement{0}: une seule note pour toute la réponse".format(NB),
        f"Q{NB}: La cafétéria avait 23 pommes. Elle en utilise 20 et en achète 6. Combien en a-t-elle{NB}?{NB}{NB}— le modèle tire quatre réponses")
reponses = [(["Elle avait 23 pommes.", "23 − 20 = 3", "3 + 6 = 9", "réponse : 9"], 1),
            (["Elle avait 23 pommes.", "23 + 6 = 29", "29 − 20 = 9", "réponse : 9"], 1),
            (["Elle avait 23 pommes.", "23 + 20 = 43", "43 + 6 = 49", "réponse : 49"], 0),
            (["Elle avait 23 pommes.", "23 − 20 = 3", "3 × 6 = 18", "réponse : 18"], 0)]
LW = [150, 104, 104, 96]
RY0, RP = PY + 58, 44
for i, (etapes, note) in enumerate(reponses):
    y = RY0 + i * RP
    bonne = note == 1
    c = TEAL if bonne else ROUGE
    o.append(f'<rect x="32" y="{y - 6}" width="{W - 64}" height="{RP - 6}" rx="6" fill="{VERT_PALE if bonne else ROUGE_PALE}"/>')
    o.append(f'<text x="44" y="{y + 16}" font-size="11" fill="{ENCRE_PALE}">{i + 1}</text>')
    x = 60
    for e, w in zip(etapes, LW):
        case(x, y, e.replace(" : ", f"{NB}: "), w, bord=c, coul=ENCRE)
        x += w + 8
    o.append(f'<line x1="{x}" y1="{y + 13}" x2="{x + 28}" y2="{y + 13}" stroke="{GRIS}" stroke-width="1.4" marker-end="url(#p)"/>')
    o.append(f'<rect x="{x + 34}" y="{y}" width="64" height="26" rx="13" fill="{c}"/>')
    o.append(f'<text x="{x + 66}" y="{y + 17.5}" font-size="12" fill="{PANNEAU}" text-anchor="middle" font-weight="700">note {note}</text>')
    o.append(f'<text x="{x + 110}" y="{y + 12}" font-size="11.5" fill="{c}" font-weight="700">{"↑ tous ses jetons" if bonne else "↓ tous ses jetons"}</text>')
    o.append(f'<text x="{x + 110}" y="{y + 26}" font-size="10.5" fill="{c}">{"plus probables" if bonne else "moins probables"}</text>')
# la bonne étape, pénalisée quand même
yb = RY0 + 3 * RP
xb = 60 + LW[0] + 8
o.append(f'<rect x="{xb - 3}" y="{yb - 3}" width="{LW[1] + 6}" height="32" rx="7" fill="none" stroke="{ROUGE}" stroke-width="2" stroke-dasharray="4 3"/>')
o.append(f'<line x1="{xb + LW[1] / 2}" y1="{yb + 54}" x2="{xb + LW[1] / 2}" y2="{yb + 32}" stroke="{ROUGE}" stroke-width="1.4" marker-end="url(#pr)"/>')
o.append(f'<text x="{xb + LW[1] / 2 + 10}" y="{yb + 52}" font-size="11.5" fill="{ROUGE}" font-weight="700">une bonne étape, pénalisée quand même{NB}: la note ne dit pas quelle étape était fautive</text>')

# ── 3. sur un grand nombre d'essais ──
BY = PY + 252 + 14
panneau(BY, 140, "3. Sur un grand nombre d'essais", "chaque étape est poussée vers le haut ou vers le bas selon les réponses où elle apparaît")
bilan = [("Elle avait 23 pommes.", 150, "dans toutes les réponses, bonnes ou mauvaises", "les poussées s'annulent", GRIS, "＝"),
         ("23 − 20 = 3", 104, "plus souvent dans les bonnes réponses", "renforcée", TEAL, "↑"),
         ("3 × 6 = 18", 104, "seulement dans des réponses fausses", "affaiblie", ROUGE, "↓")]
for k, (e, w, ou, effet, c, fl) in enumerate(bilan):
    y = BY + 54 + k * 28
    case(60, y, e, w, bord=c, h=22, taille=11.5)
    o.append(f'<text x="230" y="{y + 15}" font-size="11.5" fill="{ENCRE}">{ou}</text>')
    o.append(f'<text x="560" y="{y + 15}" font-size="12" fill="{c}" font-weight="700">{fl}{NB}{NB}{effet}</text>')
o.append(f'<text x="{W / 2}" y="{H - 12}" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">chaque case regroupe quelques jetons{NB}; réponses illustratives</text>')
o.append("</svg>")
(OUT / "une-note-pour-tout.svg").write_text("\n".join(o) + "\n")
print("une-note-pour-tout.svg écrit")
