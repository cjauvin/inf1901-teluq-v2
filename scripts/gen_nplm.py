"""Module 4, « Prédire le mot suivant » : le modèle de langage neuronal de 2003 (Bengio, Ducharme, Vincent, Jauvin). La table
des plongements fait partie du modèle : la rétropropagation l'ajuste avec les poids des neurones. Valeurs illustratives."""
from pathlib import Path
import numpy as np

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
rng = np.random.default_rng(5)
VOCAB = ["aboie", "canapé", "chat", "chien", "dort", "le", "sur", "…"]
CONTEXTE = ["chat", "dort", "sur"]
D = 6
E = {w: rng.normal(0, 1, D) for w in VOCAB}
W, H = 840, 520
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Le modèle de langage neuronal de 2003</title>",
     "<desc>Le contexte « chat dort sur » entre dans le modèle, dessiné comme un grand cadre. Dans le cadre, à gauche, la table des "
     "plongements : une rangée de nombres pour chaque mot du vocabulaire, aboie, canapé, chat, chien, dort, le, sur. Les rangées de "
     "chat, dort et sur sont surlignées. Leurs plongements sont mis bout à bout, puis passent dans une couche cachée de neurones, qui "
     "donne la probabilité de chaque mot suivant : le en tête, puis un, son et mon. Une flèche rouge, en bas, revient en "
     "sens inverse, de l'erreur jusqu'à la table : la rétropropagation ajuste les poids des neurones et aussi les plongements. Une "
     "étiquette sur le cadre indique que les paramètres du modèle sont la table des plongements et les poids des neurones, appris "
     "ensemble.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker>'
     f'<marker id="pr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{ROUGE}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Le modèle de 2003{NB}: les plongements font partie du modèle</text>']


def fleche(x1, y1, x2, y2, coul=GRIS, m="p", l=1.5):
    o.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{coul}" stroke-width="{l}" marker-end="url(#{m})"/>')


def cases(x, y, v, coul, cw=16, ch=16):
    for k, a in enumerate(v):
        r, g, b = (int(coul[q:q + 2], 16) for q in (1, 3, 5))
        t = min(1, abs(a) / 1.8)
        fond = "#%02x%02x%02x" % tuple(round(f + (c - f) * t * 0.85) for f, c in zip((251, 247, 238), (r, g, b)))
        o.append(f'<rect x="{x + k * cw}" y="{y}" width="{cw - 2}" height="{ch}" rx="2" fill="{fond}" stroke="{BORD}" stroke-width="0.7"/>')


# le contexte, au-dessus du modèle
o.append(f'<text x="40" y="70" font-size="12" fill="{ENCRE_PALE}">le contexte{NB}:</text>')
o.append(f'<text x="130" y="70" font-size="14.5" fill="{BLEU}" font-style="italic" font-weight="700">chat dort sur <tspan fill="{ENCRE_PALE}" font-weight="400">…{NB}?</tspan></text>')
o.append(f'<text x="330" y="70" font-size="11" fill="{ENCRE_PALE}">on va chercher les rangées de ces trois mots dans la table</text>')
# le cadre du modèle
FX, FY, FW, FH = 24, 92, W - 48, 330
o.append(f'<rect x="{FX}" y="{FY}" width="{FW}" height="{FH}" rx="14" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="2.2" stroke-dasharray="7 4"/>')
o.append(f'<rect x="{FX + FW - 112}" y="{FY - 11}" width="96" height="22" rx="6" fill="{FOND}"/>')
o.append(f'<text x="{FX + FW - 64}" y="{FY + 5}" font-size="12.5" fill="{TEAL}" text-anchor="middle" font-weight="700">le modèle</text>')
# la table des plongements
TX, TY, RH = 110, 140, 30
TW = 72 + D * 16 + 14
o.append(f'<rect x="{TX - 72}" y="{TY - 30}" width="{TW}" height="{len(VOCAB) * RH + 40}" rx="10" fill="{FOND}" stroke="{ROUGE}" stroke-width="2"/>')
o.append(f'<text x="{TX - 72 + TW / 2}" y="{TY - 12}" font-size="12" fill="{ROUGE}" text-anchor="middle" font-weight="700">table des plongements</text>')
ligne = {}
for i, w in enumerate(VOCAB):
    y = TY + i * RH
    ligne[w] = y
    sel = w in CONTEXTE
    if sel:
        o.append(f'<rect x="{TX - 66}" y="{y - 3}" width="{66 + D * 16 + 4}" height="22" rx="4" fill="#cfe0f0"/>')
    o.append(f'<text x="{TX - 8}" y="{y + 12}" font-size="12" fill="{BLEU if sel else (ENCRE if w != "…" else ENCRE_PALE)}" text-anchor="end" font-style="italic" font-weight="{700 if sel else 400}">{w}</text>')
    if w != "…":
        cases(TX, y, E[w], TEAL)
# les plongements mis bout à bout
CX, CY = 300, 228
o.append(f'<text x="{CX + 1.5 * D * 12}" y="{CY - 14}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">plongements mis bout à bout</text>')
for k, w in enumerate(CONTEXTE):
    cases(CX + k * D * 12, CY, E[w], TEAL, cw=12, ch=26)
    fleche(TX + D * 16 + 8, ligne[w] + 8, CX + k * D * 12 + D * 6, CY + (-3 if ligne[w] + 8 < CY else 29), BLEU, "p", 1.1)
# la couche cachée
HX, HY = 560, 199
o.append(f'<rect x="{HX}" y="{HY}" width="90" height="84" rx="10" fill="{FOND}" stroke="{TEAL}" stroke-width="1.8"/>')
for k in range(5):
    o.append(f'<circle cx="{HX + 45}" cy="{HY + 14 + k * 14}" r="5" fill="{TEAL}"/>')
o.append(f'<text x="{HX + 45}" y="{HY + 102}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">neurones</text>')
fleche(CX + 3 * D * 12 + 6, CY + 13, HX - 4, HY + 42)
# la sortie
OX, OY = 690, 170
o.append(f'<text x="{OX + 50}" y="{OY - 10}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">mot suivant</text>')
sortie = [("le", 0.45), ("un", 0.20), ("son", 0.10), ("mon", 0.06), ("…", 0.0)]
for k, (w, pv) in enumerate(sortie):
    y = OY + k * 24
    o.append(f'<text x="{OX}" y="{y + 12}" font-size="11.5" fill="{ENCRE if w != "…" else ENCRE_PALE}" font-style="italic" font-weight="{700 if k == 0 else 400}">{w}</text>')
    if pv:
        o.append(f'<rect x="{OX + 40}" y="{y + 2}" width="{pv * 160:.0f}" height="12" rx="2" fill="{ROUGE if k == 0 else TEAL}"/>')
fleche(HX + 94, HY + 42, OX - 6, OY + 50)
# la rétropropagation, en sens inverse, jusqu'au flanc de la table
yb = TY + 7 * RH + 2
xt = TX - 72 + TW
o.append(f'<path d="M{OX + 30} {OY + 128} L{OX + 30} {yb} L{xt + 4} {yb}" fill="none" stroke="{ROUGE}" stroke-width="2.2" stroke-dasharray="7 4" marker-end="url(#pr)"/>')
o.append(f'<text x="{OX + 38}" y="{OY + 146}" font-size="11" fill="{ROUGE}">erreur</text>')
o.append(f'<text x="{(xt + OX + 30) / 2}" y="{yb + 22}" font-size="12" fill="{ROUGE}" text-anchor="middle" font-weight="700">la rétropropagation ajuste les poids des neurones…</text>')
o.append(f'<text x="{(xt + OX + 30) / 2}" y="{yb + 40}" font-size="12" fill="{ROUGE}" text-anchor="middle" font-weight="700">… et la table des plongements</text>')
# l'étiquette des paramètres
o.append(f'<text x="{W / 2}" y="{FY + FH + 30}" font-size="12.5" fill="{TEAL}" text-anchor="middle" font-weight="700">les paramètres du modèle{NB}: la table des plongements et les poids des neurones, appris ensemble</text>')
o.append(f'<text x="{W / 2}" y="{FY + FH + 50}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">au départ, toutes ces valeurs sont tirées au hasard{NB}; aucune n\'est calculée d\'avance</text>')
o.append("</svg>")
(OUT / "modele-neuronal-2003.svg").write_text("\n".join(o) + "\n")
print("modele-neuronal-2003.svg écrit")
