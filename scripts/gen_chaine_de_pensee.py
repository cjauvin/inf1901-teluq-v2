"""Module 4, « Du modèle à l'assistant » : la chaîne de pensée, d'après la figure 1 de Wei et coll. (2022), traduite. La même
question reçoit une réponse fausse quand l'exemple de la requête donne la réponse directement, et une réponse juste quand
l'exemple détaille les étapes : le modèle écrit alors les siennes, et chaque résultat intermédiaire sert au suivant."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
W, H = 840, 482
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>La chaîne de pensée</title>",
     "<desc>Deux colonnes. Dans chacune, une requête contient un exemple résolu, puis une nouvelle question. L'exemple : Roger a "
     "5 balles de tennis ; il achète 2 boîtes de 3 balles ; combien de balles a-t-il maintenant ? La nouvelle question : la "
     "cafétéria avait 23 pommes ; elle en utilise 20 pour le dîner et en achète 6 ; combien en a-t-elle ? À gauche, l'exemple "
     "donne la réponse directement, « La réponse est 11 », et le modèle répond à son tour directement : « La réponse est 27 », "
     "ce qui est faux. À droite, l'exemple détaille les étapes, et le modèle fait de même : la cafétéria avait 23 pommes, elle en "
     "a utilisé 20, 23 − 20 = 3 ; elle en a acheté 6, 3 + 6 = 9 ; la réponse est 9, ce qui est juste. Le résultat intermédiaire, 3, "
     "est réutilisé dans le calcul suivant.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker>'
     f'<marker id="pt" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{TEAL}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">La même question, avec et sans les étapes</text>']
PW = (W - 60) / 2
COLS = [20, 40 + PW]


def lignes(x, y, ls, coul=ENCRE, pas=17, taille=11.5, gras=False):
    for k, l in enumerate(ls):
        o.append(f'<text x="{x}" y="{y + k * pas}" font-size="{taille}" fill="{coul}"{" font-weight=\"700\"" if gras else ""}>{l}</text>')


Q1 = [f"Q{NB}: Roger a 5 balles de tennis. Il achète 2 boîtes", f"de 3 balles. Combien de balles a-t-il maintenant{NB}?"]
Q2 = [f"Q{NB}: La cafétéria avait 23 pommes. Elle en utilise 20", f"pour le dîner et en achète 6. Combien en a-t-elle{NB}?"]
R1 = {0: [f"R{NB}: La réponse est 11."],
      1: [f"R{NB}: Roger avait 5 balles. 2 boîtes de 3 balles,", f"c'est 6 balles. 5 + 6 = 11. La réponse est 11."]}
titres = [("l'exemple donne la réponse", BRUN), ("l'exemple détaille les étapes", TEAL)]
RY, RH = 58, 190
for k, x in enumerate(COLS):
    t, c = titres[k]
    o.append(f'<text x="{x + PW / 2}" y="{RY + 14}" font-size="13" fill="{c}" text-anchor="middle" font-weight="700">{t}</text>')
    o.append(f'<rect x="{x}" y="{RY + 26}" width="{PW}" height="{RH}" rx="10" fill="{PANNEAU}" stroke="{BORD}" stroke-width="1.4"/>')
    o.append(f'<text x="{x + 14}" y="{RY + 46}" font-size="10.5" fill="{ENCRE_PALE}" font-weight="700">LA REQUÊTE</text>')
    # l'exemple résolu, sur fond teinté
    hy = RY + 56
    hh = 18 + 17 * (len(Q1) + len(R1[k]))
    o.append(f'<rect x="{x + 8}" y="{hy}" width="{PW - 16}" height="{hh}" rx="6" fill="{"#f6e9dc" if k == 0 else "#dcebe8"}"/>')
    lignes(x + 16, hy + 18, Q1, ENCRE_PALE)
    lignes(x + 16, hy + 18 + 17 * len(Q1), R1[k], c, gras=True)
    qy = hy + hh + 22
    lignes(x + 16, qy, Q2)
    o.append(f'<text x="{x + 16}" y="{qy + 17 * len(Q2)}" font-size="11.5" fill="{ENCRE}">R{NB}:</text>')
    # le modèle continue
    ay = RY + 26 + RH
    o.append(f'<line x1="{x + PW / 2}" y1="{ay + 4}" x2="{x + PW / 2}" y2="{ay + 30}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')
    o.append(f'<text x="{x + PW / 2 + 10}" y="{ay + 22}" font-size="11" fill="{ENCRE_PALE}">le modèle continue</text>')
MY, MH = RY + 26 + RH + 36, 126
for k, x in enumerate(COLS):
    c = ROUGE if k == 0 else TEAL
    o.append(f'<rect x="{x}" y="{MY}" width="{PW}" height="{MH}" rx="10" fill="{PANNEAU}" stroke="{c}" stroke-width="1.8"/>')
x0, x1 = COLS
o.append(f'<text x="{x0 + 16}" y="{MY + 30}" font-size="13" fill="{ENCRE}" font-style="italic">La réponse est 27.</text>')
o.append(f'<text x="{x0 + 16}" y="{MY + MH - 18}" font-size="12.5" fill="{ROUGE}" font-weight="700">faux{NB}: le résultat est deviné d\'un coup</text>')
lignes(x1 + 16, MY + 30, ["La cafétéria avait 23 pommes. Elle en a utilisé 20."], ENCRE, taille=12)
o.append(f'<text x="{x1 + 16}" y="{MY + 49}" font-size="12" fill="{ENCRE}">Il en reste 23 − 20 = <tspan font-weight="700" fill="{TEAL}">3</tspan>. '
         f'Elle en a acheté 6.</text>')
o.append(f'<text x="{x1 + 16}" y="{MY + 68}" font-size="12" fill="{ENCRE}">Elle en a donc <tspan font-weight="700" fill="{TEAL}">3</tspan> + 6 = 9. '
         f'La réponse est 9.</text>')
o.append(f'<text x="{x1 + 16}" y="{MY + MH - 36}" font-size="11" fill="{ENCRE_PALE}">le résultat écrit, 3, devient le contexte du calcul suivant</text>')
o.append(f'<text x="{x1 + 16}" y="{MY + MH - 18}" font-size="12.5" fill="{TEAL}" font-weight="700">juste{NB}: le calcul est fait pas à pas</text>')
o.append(f'<text x="{W / 2}" y="{H - 14}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">D\'après la figure 1 de Wei et coll. (2022), traduite de l\'anglais</text>')
o.append("</svg>")
(OUT / "chaine-de-pensee.svg").write_text("\n".join(o) + "\n")
print("chaine-de-pensee.svg écrit")
