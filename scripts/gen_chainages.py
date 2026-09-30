"""Chaînage avant et chaînage arrière sur l'exemple de la voiture (R1, R2).

Deux figures de même géométrie : les faits à gauche, la conclusion à droite.
En chaînage avant, le raisonnement va de gauche à droite (des faits observés
vers la conclusion) ; en chaînage arrière, il part de l'hypothèse, à droite, et
remonte vers la gauche jusqu'aux questions à poser à l'utilisateur.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module1"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#3a6ea5", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "
W, H = 776, 330
BOITE_H = 54
# colonnes : (x, largeur) des boîtes ; centres des règles
FAITS_X, FAITS_W = 24, 180
R1_X = 266
DEDUIT_X, DEDUIT_W = 330, 150
R2_X = 544
CONCL_X, CONCL_W = 606, 150
Y_HAUT, Y_BAS, Y_MILIEU = 128, 206, 167


def boite(o, x, w, cy, lignes, couleur, epais=False):
    o.append(f'<rect x="{x}" y="{cy - BOITE_H / 2}" width="{w}" height="{BOITE_H}" rx="9" fill="{couleur}" '
             f'fill-opacity="0.12" stroke="{couleur}" stroke-width="{2.2 if epais else 1.5}"/>')
    y0 = cy - (len(lignes) - 1) * 8 + 4.5
    for i, t in enumerate(lignes):
        o.append(f'<text x="{x + w / 2}" y="{y0 + i * 16}" font-size="12.5" fill="{ENCRE}" text-anchor="middle">{t}</text>')


def regle(o, cx, nom):
    o.append(f'<circle cx="{cx}" cy="{Y_MILIEU}" r="21" fill="{PANNEAU}" stroke="{BRUN}" stroke-width="2"/>')
    o.append(f'<text x="{cx}" y="{Y_MILIEU + 5}" font-size="14" fill="{BRUN}" text-anchor="middle" font-weight="700">{nom}</text>')


def fleche(o, x1, y1, x2, y2, couleur, pointillee=False):
    o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{couleur}" stroke-width="2.4" '
             f'marker-end="url(#pointe-{couleur[1:]})"' + (' stroke-dasharray="6 4"' if pointillee else '') + '/>')


def legende_colonnes(o, textes):
    xs = [FAITS_X + FAITS_W / 2, R1_X, DEDUIT_X + DEDUIT_W / 2, R2_X, CONCL_X + CONCL_W / 2]
    for x, t in zip(xs, textes):
        o.append(f'<text x="{x}" y="{Y_BAS + BOITE_H / 2 + 34}" font-size="11.5" fill="{GRIS}" text-anchor="middle">{t}</text>')


def figure(nom, titre, desc, avant):
    couleur = TEAL if avant else BRUN
    o = ['<?xml version="1.0" encoding="UTF-8"?>',
         f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
         f"<title>{titre}</title>", f"<desc>{desc}</desc>",
         f'<defs><marker id="pointe-{couleur[1:]}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
         f'<path d="M0 0 L10 5 L0 10 z" fill="{couleur}"/></marker></defs>',
         f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
         f'<text x="{W / 2}" y="38" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">{titre}</text>']
    sens = "de gauche à droite : des faits vers la conclusion" if avant else "de droite à gauche : de l'hypothèse vers les faits à vérifier"
    o.append(f'<text x="{W / 2}" y="60" font-size="12.5" fill="{ENCRE_PALE}" text-anchor="middle">Le raisonnement va {sens}</text>')

    if avant:
        boite(o, FAITS_X, FAITS_W, Y_HAUT, ["le moteur ne se lance pas"], BLEU)
        boite(o, FAITS_X, FAITS_W, Y_BAS, ["les phares sont faibles"], BLEU)
        boite(o, DEDUIT_X, DEDUIT_W, Y_MILIEU, ["la batterie", "est déchargée"], BRUN)
        boite(o, CONCL_X, CONCL_W, Y_MILIEU, ["recharger ou", "remplacer la batterie"], TEAL, epais=True)
        for y in (Y_HAUT, Y_BAS):
            fleche(o, FAITS_X + FAITS_W + 4, y, R1_X - 24, Y_MILIEU + (y - Y_MILIEU) * 0.35, couleur)
        fleche(o, R1_X + 23, Y_MILIEU, DEDUIT_X - 5, Y_MILIEU, couleur)
        fleche(o, DEDUIT_X + DEDUIT_W + 4, Y_MILIEU, R2_X - 24, Y_MILIEU, couleur)
        fleche(o, R2_X + 23, Y_MILIEU, CONCL_X - 5, Y_MILIEU, couleur)
        legende_colonnes(o, ["faits observés", "R1 se déclenche", "fait déduit", "R2 se déclenche", "conclusion"])
        note = f"R3 et R4 sont aussi examinées, mais leurs conditions ne sont pas remplies{FINE}; elles ne font rien."
    else:
        boite(o, FAITS_X, FAITS_W, Y_HAUT, [f"le moteur se lance-t-il{FINE}?"], BLEU)
        boite(o, FAITS_X, FAITS_W, Y_BAS, [f"les phares sont-ils faibles{FINE}?"], BLEU)
        boite(o, DEDUIT_X, DEDUIT_W, Y_MILIEU, ["la batterie est-elle", f"déchargée{FINE}?"], BRUN)
        boite(o, CONCL_X, CONCL_W, Y_MILIEU, ["et si c'était", f"la batterie{FINE}?"], TEAL, epais=True)
        fleche(o, CONCL_X - 4, Y_MILIEU, R2_X + 24, Y_MILIEU, couleur, True)
        fleche(o, R2_X - 23, Y_MILIEU, DEDUIT_X + DEDUIT_W + 5, Y_MILIEU, couleur, True)
        fleche(o, DEDUIT_X - 4, Y_MILIEU, R1_X + 24, Y_MILIEU, couleur, True)
        for y in (Y_HAUT, Y_BAS):
            fleche(o, R1_X - 21, Y_MILIEU + (y - Y_MILIEU) * 0.35, FAITS_X + FAITS_W + 5, y, couleur, True)
        legende_colonnes(o, ["questions à l'utilisateur", "R1 l'établirait si…", "sous-but", "R2 conclurait si…", "hypothèse de départ"])
        note = f"Aucune règle ne produit les deux faits de gauche{FINE}: le système les demande. R3 et R4 ne sont pas examinées."
    regle(o, R1_X, "R1")
    regle(o, R2_X, "R2")
    o.append(f'<text x="{W / 2}" y="{H - 22}" font-size="12.5" fill="{ENCRE_PALE}" text-anchor="middle">{note}</text>')
    o.append("</svg>")
    (OUT / nom).write_text("\n".join(o) + "\n")
    print(nom, "écrit")


figure("chainage-avant.svg", "Le chaînage avant",
       f"Schéma de gauche à droite. Deux faits observés, «{FINE}le moteur ne se lance pas{FINE}» et «{FINE}les phares sont faibles{FINE}», mènent à la règle R1, qui se déclenche et produit le fait déduit «{FINE}la batterie est déchargée{FINE}». Ce fait mène à la règle R2, qui se déclenche et donne la conclusion «{FINE}recharger ou remplacer la batterie{FINE}». R3 et R4 sont examinées sans se déclencher.",
       avant=True)
figure("chainage-arriere.svg", "Le chaînage arrière",
       f"Même schéma, parcouru de droite à gauche avec des flèches en pointillé. On part de l'hypothèse «{FINE}et si c'était la batterie{FINE}?{FINE}». La règle R2 conclurait à recharger la batterie si la batterie était déchargée{NB}: c'est le sous-but. La règle R1 établirait ce sous-but si le moteur ne se lançait pas et si les phares étaient faibles. Aucune règle ne produit ces deux faits{NB}: le système pose donc deux questions à l'utilisateur. R3 et R4 ne sont pas examinées.",
       avant=False)
