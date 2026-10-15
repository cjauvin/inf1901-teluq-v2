# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""Module 4, « Regarder à l'intérieur » : deux figures.
1. demeler-activation.svg : un autoencodeur clairsemé récrit l'activation d'un modèle, un vecteur dense où chaque neurone
   mêle plusieurs concepts, comme une somme de quelques caractéristiques lisibles, tirées d'un très grand dictionnaire.
2. graphe-attribution.svg : un graphe d'attribution simplifié, d'après l'exemple d'Anthropic (2025) : pour « la capitale de
   l'État où se trouve Dallas », le modèle passe par une étape interne, « Texas », avant de répondre « Austin ».
Valeurs illustratives."""
from pathlib import Path
import numpy as np

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "


def entete(W, H, titre, desc):
    return ['<?xml version="1.0" encoding="UTF-8"?>',
            f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
            f"<title>{titre}</title>", f"<desc>{desc}</desc>",
            f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto">'
            f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker>'
            f'<marker id="pt" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto">'
            f'<path d="M0 0 L10 5 L0 10 z" fill="{TEAL}"/></marker>'
            f'<marker id="pr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto">'
            f'<path d="M0 0 L10 5 L0 10 z" fill="{ROUGE}"/></marker></defs>',
            f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>']


def teinte(v, coul):
    r, g, b = (int(coul[q:q + 2], 16) for q in (1, 3, 5))
    a = min(1, abs(v))
    return "#%02x%02x%02x" % tuple(round(f + (c - f) * a * 0.9) for f, c in zip((251, 247, 238), (r, g, b)))


# ── 1. démêler une activation ──
rng = np.random.default_rng(4)
W, H = 840, 380
o = entete(W, H, "Démêler une activation",
           "À gauche, l'activation du modèle sur le mot « Gate », dans la phrase « Nous avons traversé le Golden Gate à vélo » : "
           "une colonne de nombres où presque toutes les cases sont actives, chaque neurone mêlant plusieurs concepts. Au milieu, "
           "l'autoencodeur clairsemé la récrit comme un choix dans un immense dictionnaire de caractéristiques : une longue rangée "
           "de cases presque toutes éteintes, dont trois seulement s'allument, « le pont du Golden Gate », « San Francisco » et « le "
           "vélo ». À droite, ces trois caractéristiques, additionnées, reconstruisent presque l'activation de départ. En bas : en "
           "amplifiant la caractéristique « le pont du Golden Gate », on obtient le Golden Gate Claude, qui ramène toute "
           "conversation au pont.")
o.append(f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Démêler une activation{NB}: quelques caractéristiques parmi des millions</text>')
o.append(f'<text x="{W / 2}" y="54" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle" font-style="italic">«{NB}Nous avons traversé le Golden <tspan font-weight="700" fill="{ENCRE}">Gate</tspan> à vélo.{NB}»</text>')
act = rng.normal(0, 0.7, 14)
# l'activation dense
o.append(f'<text x="70" y="84" font-size="11.5" fill="{BRUN}" text-anchor="middle" font-weight="700">l\'activation</text>')
o.append(f'<text x="70" y="98" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">des milliers de neurones</text>')
for k, v in enumerate(act):
    o.append(f'<rect x="56" y="{108 + k * 15}" width="28" height="13" rx="2" fill="{teinte(v, BRUN)}" stroke="{BORD}" stroke-width="0.6"/>')
o.append(f'<text x="70" y="{108 + 14 * 15 + 16}" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">chaque neurone</text>')
o.append(f'<text x="70" y="{108 + 14 * 15 + 29}" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">mêle plusieurs concepts</text>')
o.append(f'<line x1="94" y1="212" x2="150" y2="212" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')
o.append(f'<text x="122" y="204" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">démêler</text>')
# le dictionnaire de caractéristiques
DX, DY, NC, CW = 160, 150, 40, 12.5
o.append(f'<text x="{DX + NC * CW / 2}" y="84" font-size="11.5" fill="{TEAL}" text-anchor="middle" font-weight="700">les caractéristiques</text>')
o.append(f'<text x="{DX + NC * CW / 2}" y="98" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">un dictionnaire de millions de concepts, presque tous éteints</text>')
allumees = {9: ("le pont du Golden Gate", 1.0), 22: ("San Francisco", 0.6), 33: ("le vélo", 0.45)}
for k in range(NC):
    v = allumees.get(k, (None, 0))[1]
    o.append(f'<rect x="{DX + k * CW}" y="{DY}" width="{CW - 2}" height="26" rx="2" fill="{teinte(v, TEAL) if v else "#ebe5d6"}" stroke="{TEAL if v else BORD}" stroke-width="{1.4 if v else 0.6}"/>')
o.append(f'<text x="{DX + NC * CW + 6}" y="{DY + 18}" font-size="13" fill="{GRIS}">…</text>')
for i, (k, (nom, v)) in enumerate(sorted(allumees.items())):
    x = DX + k * CW + CW / 2 - 1
    y2 = DY + 60 + i * 26
    o.append(f'<line x1="{x}" y1="{DY + 28}" x2="{x}" y2="{y2 - 12}" stroke="{TEAL}" stroke-width="1.2"/>')
    o.append(f'<text x="{x}" y="{y2}" font-size="11.5" fill="{TEAL}" text-anchor="middle" font-weight="700">{nom}</text>')
o.append(f'<line x1="{DX + NC * CW + 26}" y1="212" x2="{DX + NC * CW + 80}" y2="212" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')
o.append(f'<text x="{DX + NC * CW + 53}" y="204" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">additionner</text>')
# la reconstruction
RX = DX + NC * CW + 104
rec = act + rng.normal(0, 0.12, 14)
o.append(f'<text x="{RX + 14}" y="84" font-size="11.5" fill="{BRUN}" text-anchor="middle" font-weight="700">la reconstruction</text>')
o.append(f'<text x="{RX + 14}" y="98" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">presque identique</text>')
for k, v in enumerate(rec):
    o.append(f'<rect x="{RX}" y="{108 + k * 15}" width="28" height="13" rx="2" fill="{teinte(v, BRUN)}" stroke="{BORD}" stroke-width="0.6"/>')
# le Golden Gate Claude
o.append(f'<rect x="160" y="{H - 64}" width="{NC * CW}" height="44" rx="8" fill="{PANNEAU}" stroke="{ROUGE}" stroke-width="1.4"/>')
o.append(f'<text x="{160 + NC * CW / 2}" y="{H - 46}" font-size="11.5" fill="{ROUGE}" text-anchor="middle" font-weight="700">Amplifier «{NB}le pont du Golden Gate{NB}» dans le modèle (2024)</text>')
o.append(f'<text x="{160 + NC * CW / 2}" y="{H - 30}" font-size="11" fill="{ENCRE}" text-anchor="middle">le modèle ramène toute conversation au pont, jusqu\'à se prendre pour lui</text>')
o.append("</svg>")
(OUT / "demeler-activation.svg").write_text("\n".join(o) + "\n")

# ── 2. un graphe d'attribution ──
W, H = 840, 430
o = entete(W, H, "Suivre un raisonnement dans le modèle",
           "En bas, la question donnée au modèle : « La capitale de l'État où se trouve Dallas est… ». Au-dessus, les caractéristiques "
           "internes qui s'activent, reliées par des flèches selon leur influence. Le mot « Dallas » active une caractéristique « Texas », "
           "qui n'apparaît nulle part dans la question. Les mots « capitale » et « État » activent une caractéristique « dire une "
           "capitale ». Les deux se combinent pour produire la réponse, « Austin ». À droite, une intervention : si l'on remplace, "
           "dans le modèle, la caractéristique « Texas » par « Californie », il répond « Sacramento ».")
o.append(f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Suivre un raisonnement dans le modèle{NB}: un graphe d\'attribution</text>')
o.append(f'<rect x="20" y="50" width="540" height="{H - 70}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')


def noeud(cx, cy, l1, l2, coul, w=150, fond=FOND):
    o.append(f'<rect x="{cx - w / 2}" y="{cy - 22}" width="{w}" height="44" rx="10" fill="{fond}" stroke="{coul}" stroke-width="1.8"/>')
    o.append(f'<text x="{cx}" y="{cy - 3}" font-size="12.5" fill="{coul}" text-anchor="middle" font-weight="700">{l1}</text>')
    o.append(f'<text x="{cx}" y="{cy + 13}" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">{l2}</text>')


def lien(x1, y1, x2, y2, coul=TEAL, m="pt"):
    o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{coul}" stroke-width="2" marker-end="url(#{m})"/>')


# la question, en bas
YQ = H - 62
mots = [("La", 0), ("capitale", 1), ("de l'État", 1), ("où se trouve", 0), ("Dallas", 2), ("est…", 0)]
xs, x = {}, 44
for m, role in mots:
    w = 16 + 7.4 * len(m)
    coul = BLEU if role else GRIS
    o.append(f'<rect x="{x}" y="{YQ - 16}" width="{w}" height="28" rx="5" fill="{"#e6eef6" if role else FOND}" stroke="{coul}" stroke-width="{1.4 if role else 0.8}"/>')
    o.append(f'<text x="{x + w / 2}" y="{YQ + 3}" font-size="12" fill="{ENCRE}" text-anchor="middle" font-style="italic">{m}</text>')
    xs[m] = x + w / 2
    x += w + 6
o.append(f'<text x="290" y="{H - 24}" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">la question</text>')
# les caractéristiques
TX, TY = xs["Dallas"], 236
CX, CY = (xs["capitale"] + xs["de l'État"]) / 2, 236
noeud(TX, TY, "Texas", "une étape interne", TEAL)
noeud(CX, CY, "dire une capitale", "le genre de réponse", TEAL, w=160)
lien(xs["Dallas"], YQ - 18, TX, TY + 24)
lien(xs["capitale"], YQ - 18, CX - 30, CY + 24)
lien(xs["de l'État"], YQ - 18, CX + 20, CY + 24)
RX, RY = (TX + CX) / 2, 112
noeud(RX, RY, "Austin", "la réponse", BRUN, w=140, fond="#f3e3d3")
lien(TX, TY - 24, RX + 30, RY + 24)
lien(CX, CY - 24, RX - 30, RY + 24)
o.append(f'<text x="{TX + 84}" y="{TY + 4}" font-size="10.5" fill="{ENCRE_PALE}">absent de la</text>')
o.append(f'<text x="{TX + 84}" y="{TY + 18}" font-size="10.5" fill="{ENCRE_PALE}">question{NB}!</text>')
# l'intervention, à droite
o.append(f'<rect x="576" y="50" width="244" height="{H - 70}" rx="10" fill="{PANNEAU}" stroke="{ROUGE}" stroke-width="1.4"/>')
o.append(f'<text x="698" y="76" font-size="12.5" fill="{ROUGE}" text-anchor="middle" font-weight="700">Une intervention</text>')
for k, l in enumerate(["On remplace, à l'intérieur du", "modèle, la caractéristique"]):
    o.append(f'<text x="698" y="{102 + k * 16}" font-size="11" fill="{ENCRE}" text-anchor="middle">{l}</text>')
noeud(698, 166, "Texas  →  Californie", "modifiée à la main", ROUGE, w=200)
lien(698, 190, 698, 236, ROUGE, "pr")
noeud(698, 262, "Sacramento", "la nouvelle réponse", BRUN, w=160, fond="#f3e3d3")
for k, l in enumerate(["L'étape «" + NB + "Texas" + NB + "» n'est donc pas", "une illusion : elle est vraiment", "utilisée pour répondre."]):
    o.append(f'<text x="698" y="{318 + k * 16}" font-size="11" fill="{ENCRE}" text-anchor="middle">{l}</text>')
o.append("</svg>")
(OUT / "graphe-attribution.svg").write_text("\n".join(o) + "\n")
print("demeler-activation.svg et graphe-attribution.svg écrits")
