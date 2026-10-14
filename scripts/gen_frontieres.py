"""Module 4, « Des outils et des agents » : qui fait quoi, et où. Le modèle tourne chez son fournisseur et ne sait que
prolonger un texte ; le harnais, un programme classique, tient la conversation, exécute les appels et applique les
permissions ; les outils sont des programmes ordinaires qui agissent sur le monde."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
W, H = 840, 500
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Le modèle, le harnais et les outils</title>",
     "<desc>Trois zones côte à côte, séparées par des frontières en pointillés. À gauche, chez le fournisseur du modèle : le "
     "modèle, des milliards de paramètres sur des processeurs graphiques ; il sait prolonger un texte, jeton après jeton, mais "
     "n'a ni réseau, ni fichiers, ni horloge, ni mémoire d'un appel à l'autre. Au milieu, chez l'entreprise qui offre "
     "l'assistant, ou sur l'ordinateur de l'utilisateur : le harnais, un programme classique, relié à l'utilisateur ; il tient "
     "la conversation, assemble le texte, lit et vérifie les appels, exécute les outils, applique les permissions et demande des "
     "confirmations. Le harnais envoie le texte au modèle et reçoit sa suite, parfois un appel. À droite, le monde : les outils, "
     "des programmes ordinaires, comme une base de données, une recherche sur le Web, une messagerie et un bac à sable pour "
     "exécuter du code. Le harnais les exécute et reçoit leurs résultats. En bas : le modèle propose, le harnais dispose.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Qui fait quoi, et où{NB}: le modèle, le harnais, les outils</text>']
ZY, ZH = 52, 372
ZONES = [(20, 220, "chez le fournisseur", "du modèle"), (300, 240, "chez l'entreprise qui offre l'assistant,", "ou sur l'ordinateur de l'utilisateur"),
         (600, 220, "le monde", "")]
HALO = f' stroke="{FOND}" stroke-width="5" paint-order="stroke"'
for x, w, t1, t2 in ZONES:
    o.append(f'<rect x="{x}" y="{ZY}" width="{w}" height="{ZH}" rx="12" fill="none" stroke="{AXE}" stroke-width="1.6" stroke-dasharray="7 5"/>')
    o.append(f'<text x="{x + w / 2}" y="{ZY + 20}" font-size="11.5" fill="{GRIS}" text-anchor="middle" font-weight="700">{t1}</text>')
    if t2:
        o.append(f'<text x="{x + w / 2}" y="{ZY + 35}" font-size="11.5" fill="{GRIS}" text-anchor="middle" font-weight="700">{t2}</text>')


def boite(x, y, w, h, titre, sous, coul, lignes, fond=PANNEAU, dy=66):
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fond}" stroke="{coul}" stroke-width="2"/>')
    o.append(f'<text x="{x + w / 2}" y="{y + 24}" font-size="14" fill="{coul}" text-anchor="middle" font-weight="700">{titre}</text>')
    o.append(f'<text x="{x + w / 2}" y="{y + 41}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">{sous}</text>')
    for k, (signe, l) in enumerate(lignes):
        c = TEAL if signe == "+" else ROUGE
        o.append(f'<text x="{x + 14}" y="{y + dy + k * 18}" font-size="11.5" fill="{c}" font-weight="700">{"✓" if signe == "+" else "✗"}</text>')
        o.append(f'<text x="{x + 30}" y="{y + dy + k * 18}" font-size="11.5" fill="{ENCRE}">{l}</text>')


# le modèle
boite(32, 150, 196, 190, "le modèle", "des milliards de paramètres,", TEAL,
      [("+", "prolonger un texte"), ("-", "aucun accès au réseau"), ("-", "aucun accès aux fichiers"), ("-", "aucune horloge"),
       ("-", "rien ne reste d'un appel")], fond=FOND, dy=84)
o.append(f'<text x="130" y="{150 + 41 + 14}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">sur des processeurs graphiques</text>')
# le harnais, et l'utilisateur au-dessus
o.append(f'<rect x="350" y="94" width="140" height="30" rx="15" fill="{BLEU}"/>')
o.append(f'<text x="420" y="113.5" font-size="12" fill="{PANNEAU}" text-anchor="middle" font-weight="700">l\'utilisateur</text>')
o.append(f'<line x1="410" y1="126" x2="410" y2="146" stroke="{GRIS}" stroke-width="1.5" marker-end="url(#p)"/>')
o.append(f'<line x1="430" y1="148" x2="430" y2="128" stroke="{GRIS}" stroke-width="1.5" marker-end="url(#p)"/>')
boite(314, 150, 212, 222, "le harnais", "un programme classique", BLEU,
      [("+", "tient la conversation"), ("+", "assemble le texte"), ("+", "lit et vérifie les appels"), ("+", "exécute les outils"),
       ("+", "applique les permissions"), ("+", "demande des confirmations"), ("+", "affiche la réponse")])
# les outils
for k, (l1, l2) in enumerate([("base de données", "le catalogue"), ("recherche Web", ""), ("messagerie", "envoyer un courriel"),
                              ("bac à sable", "exécuter du code, isolé")]):
    y = 104 + k * 70
    o.append(f'<rect x="618" y="{y}" width="184" height="52" rx="8" fill="{PANNEAU}" stroke="{BRUN}" stroke-width="1.6"/>')
    o.append(f'<text x="710" y="{y + (23 if l2 else 31)}" font-size="12.5" fill="{ENCRE}" text-anchor="middle" font-weight="700">{l1}</text>')
    if l2:
        o.append(f'<text x="710" y="{y + 40}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">{l2}</text>')
o.append(f'<text x="710" y="{104 + 4 * 70 + 10}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">des programmes ordinaires</text>')
# les échanges
o.append(f'<line x1="312" y1="214" x2="232" y2="214" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')
o.append(f'<text x="270" y="205" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle"{HALO}>texte</text>')
o.append(f'<line x1="230" y1="262" x2="310" y2="262" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')
for k, l in enumerate(["la suite,", "parfois", "un appel"]):
    o.append(f'<text x="270" y="{280 + k * 13}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle"{HALO}>{l}</text>')
o.append(f'<line x1="528" y1="214" x2="612" y2="214" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')
o.append(f'<text x="570" y="205" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle"{HALO}>exécute</text>')
o.append(f'<line x1="614" y1="262" x2="530" y2="262" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')
o.append(f'<text x="570" y="280" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle"{HALO}>résultat</text>')
# la maxime
o.append(f'<text x="{W / 2}" y="{H - 40}" font-size="14" fill="{ENCRE}" text-anchor="middle" font-weight="700">'
         f'<tspan fill="{TEAL}">le modèle propose</tspan>, <tspan fill="{BLEU}">le harnais dispose</tspan></text>')
o.append(f'<text x="{W / 2}" y="{H - 18}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">ce qu\'un assistant peut faire dans le monde dépend des outils que son harnais lui branche, et des permissions qu\'il accorde</text>')
o.append("</svg>")
(OUT / "modele-harnais-outils.svg").write_text("\n".join(o) + "\n")
print("modele-harnais-outils.svg écrit")
