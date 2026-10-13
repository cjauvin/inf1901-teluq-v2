"""Module 4, « Du modèle à l'assistant » : les trois étapes de l'entraînement d'un assistant (préentraînement, puis
post-entraînement : ajustement et renforcement), et ce qui se passe ensuite, au moment de la réponse."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "
W, H = 900, 470
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Du modèle de base à l'assistant</title>",
     "<desc>Trois colonnes reliées par des flèches. 1, le préentraînement : des milliers de milliards de jetons de textes, la tâche "
     "de prédire le jeton suivant, et pour résultat un modèle de base qui continue des textes. 2, l'ajustement par instructions : "
     "des dizaines de milliers d'exemples de requêtes et de bonnes réponses rédigées par des humains, et pour résultat un modèle "
     "qui répond aux requêtes. 3, l'apprentissage par renforcement : des humains comparent des réponses, un modèle de récompense "
     "apprend leurs préférences, et le modèle est ajusté pour obtenir la meilleure récompense ; pour les mathématiques et le code, "
     "la récompense peut venir d'une vérification automatique. Le résultat est un assistant. 4, en grisé, au moment de la réponse : "
     "aucun entraînement, les poids ne changent plus, mais le modèle peut réfléchir plus ou moins longtemps avant de répondre ; "
     "plus de calcul donne de meilleures réponses. Des accolades regroupent les étapes : la première est le préentraînement, la "
     "deuxième et la troisième forment le post-entraînement, la quatrième se passe au moment de la réponse.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Du modèle de base à l\'assistant</text>']
COLS = [
    ("1", "Préentraînement", ["des milliers de milliards", "de jetons de textes"], ["prédire le jeton suivant"],
     ["des semaines de calcul,", "l'essentiel du coût"], "un modèle de base,", "qui continue des textes", BLEU),
    ("2", "Ajustement", ["des dizaines de milliers", "de requêtes et de réponses", "rédigées par des humains"], ["imiter ces réponses"],
     ["quelques jours"], "un modèle qui répond", "aux requêtes", TEAL),
    ("3", "Renforcement", ["des humains comparent", "deux réponses ; un modèle", "de récompense apprend", "leurs préférences"],
     ["obtenir la meilleure", "récompense"], ["ou une vérification", "automatique (calcul, code)"], "un assistant", "", BRUN),
    ("4", "La réponse", ["la requête de", "l'utilisateur ; aucun", "entraînement, les poids", "ne changent plus"],
     ["réfléchir plus ou moins", "longtemps, puis répondre"], ["plus de calcul, de meilleures", "réponses (modèles de", "raisonnement)"],
     "une réponse", "", GRIS),
]
l, e, x0 = 196, 20, 22
for k, (num, titre, donnees, tache, note, res1, res2, coul) in enumerate(COLS):
    x = x0 + k * (l + e)
    cx = x + l / 2
    pointilles = ' stroke-dasharray="6 4"' if k == 3 else ""
    o.append(f'<rect x="{x}" y="52" width="{l}" height="252" rx="10" fill="{PANNEAU}" stroke="{coul}" stroke-width="2"{pointilles}/>')
    o.append(f'<circle cx="{x + 22}" cy="76" r="12" fill="{coul}"/>')
    o.append(f'<text x="{x + 22}" y="80.5" font-size="12.5" fill="#fff" text-anchor="middle" font-weight="700">{num}</text>')
    o.append(f'<text x="{x + 42}" y="81" font-size="14" fill="{coul}" font-weight="700">{titre}</text>')
    y = 110
    o.append(f'<text x="{x + 14}" y="{y}" font-size="11" fill="{GRIS}">{"ENTRÉE" if k == 3 else "DONNÉES"}</text>')
    for j, ligne in enumerate(donnees):
        o.append(f'<text x="{x + 14}" y="{y + 17 + 15 * j}" font-size="12" fill="{ENCRE}">{ligne}</text>')
    y = 110 + 17 + 15 * len(donnees) + 14
    o.append(f'<text x="{x + 14}" y="{y}" font-size="11" fill="{GRIS}">TÂCHE</text>')
    for j, ligne in enumerate(tache):
        o.append(f'<text x="{x + 14}" y="{y + 17 + 15 * j}" font-size="12" fill="{ENCRE}" font-weight="600">{ligne}</text>')
    y = y + 17 + 15 * len(tache) + 10
    for j, ligne in enumerate(note):
        o.append(f'<text x="{x + 14}" y="{y + 15 * j}" font-size="11.5" fill="{ENCRE_PALE}" font-style="italic">{ligne}</text>')
    o.append(f'<rect x="{x + 12}" y="318" width="{l - 24}" height="48" rx="8" fill="{FOND}" stroke="{coul}" stroke-width="1.6"{pointilles}/>')
    o.append(f'<text x="{cx}" y="{338 if res2 else 347}" font-size="12.5" fill="{ENCRE}" text-anchor="middle" font-weight="700">{res1}</text>')
    if res2:
        o.append(f'<text x="{cx}" y="355" font-size="12.5" fill="{ENCRE}" text-anchor="middle" font-weight="700">{res2}</text>')
    o.append(f'<line x1="{cx}" y1="304" x2="{cx}" y2="316" stroke="{coul}" stroke-width="1.6"/>')
    if k < 3:
        o.append(f'<line x1="{x + l - 12}" y1="342" x2="{x + l + e + 10}" y2="342" stroke="{GRIS}" stroke-width="2" marker-end="url(#p)"/>')
# les accolades : préentraînement, post-entraînement, au moment de la réponse


def accolade(xa, xb, y, l1, l2, coul):
    m = (xa + xb) / 2
    o.append(f'<path d="M{xa} {y} Q{xa} {y + 10} {xa + 10} {y + 10} H{m - 8} Q{m} {y + 10} {m} {y + 18} Q{m} {y + 10} {m + 8} {y + 10} '
             f'H{xb - 10} Q{xb} {y + 10} {xb} {y}" fill="none" stroke="{coul}" stroke-width="1.6"/>')
    o.append(f'<text x="{m}" y="{y + 36}" font-size="13" fill="{coul}" text-anchor="middle" font-weight="700">{l1}</text>')
    o.append(f'<text x="{m}" y="{y + 52}" font-size="11" fill="{coul}" text-anchor="middle" font-style="italic">{l2}</text>')


xs = [x0 + k * (l + e) for k in range(4)]
accolade(xs[0] + 6, xs[0] + l - 6, 378, "préentraînement", "pre-training", BLEU)
accolade(xs[1] + 6, xs[2] + l - 6, 378, "post-entraînement", "post-training", BRUN)
accolade(xs[3] + 6, xs[3] + l - 6, 378, "au moment de la réponse", "test-time", GRIS)
o.append(f'<text x="{W / 2}" y="{H - 12}" font-size="11.5" fill="{GRIS}" text-anchor="middle">Chaque étape part du modèle produit par la précédente.</text>')
o.append("</svg>")
(OUT / "du-modele-a-l-assistant.svg").write_text("\n".join(o) + "\n")
print("du-modele-a-l-assistant.svg écrit")
