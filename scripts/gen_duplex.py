# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""Module 4, « Des modèles qui voient, entendent et parlent » : une conversation à voix haute en duplex intégral. En haut,
six secondes d'échange où les voix se chevauchent : le modèle acquiesce pendant que la personne parle, répond après un
court silence, s'arrête quand on l'interrompt. En bas, les deux flux de jetons audio, un toutes les 80 millisecondes, que
le modèle lit et écrit en même temps. Échange illustratif ; le rythme des jetons est celui du codec de Moshi (12,5 par
seconde)."""
from pathlib import Path
import numpy as np

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
rng = np.random.default_rng(3)
W, H = 840, 470
X0, X1, T = 150, 812, 6.0
tx = lambda s: X0 + s / T * (X1 - X0)
PERS = [(0.0, 2.4, f"«{NB}Je cherche un livre pour ma mère, elle aime les romans…{NB}»"), (3.6, 4.6, f"«{NB}Ah, elle l'a déjà lu{NB}!{NB}»")]
MOD = [(1.35, 1.7, "mm-hmm"), (2.65, 3.85, f"«{NB}Je vous suggère Kamouraska, d'An…{NB}»"), (4.85, 5.95, f"«{NB}Alors, Les Fous de Bassan{NB}?{NB}»")]
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Converser à voix haute</title>",
     "<desc>Six secondes d'une conversation à voix haute, sur une ligne du temps. En haut, la voix de la personne : « Je cherche "
     "un livre pour ma mère, elle aime les romans… ». Pendant qu'elle parle, le modèle glisse un « mm-hmm », sans l'interrompre. "
     "Environ deux cents millisecondes après la fin de sa phrase, comme entre deux humains, il répond : « Je vous suggère "
     "Kamouraska, d'An… ». La personne l'interrompt, « Ah, elle l'a déjà lu ! », et le modèle s'arrête aussitôt, puis propose "
     "autre chose. En bas, deux rangées de petits carrés : les jetons audio de la personne, que le modèle écoute, et ses propres "
     "jetons, qu'il produit, un toutes les 80 millisecondes, en même temps ; les silences sont aussi des jetons.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Converser à voix haute{NB}: écouter et parler en même temps</text>']
o.append(f'<rect x="20" y="50" width="{W - 40}" height="232" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')


def piste(y, segs, coul, nom):
    o.append(f'<text x="36" y="{y + 4}" font-size="12.5" fill="{coul}" font-weight="700">{nom}</text>')
    o.append(f'<line x1="{X0}" y1="{y}" x2="{X1}" y2="{y}" stroke="{BORD}" stroke-width="1"/>')
    for a, b, txt in segs:
        n = int((tx(b) - tx(a)) / 3)
        for k in range(n):
            x = tx(a) + k * 3
            env = np.sin(np.pi * (k + 0.5) / n) ** 0.4
            h = 3 + 15 * env * rng.uniform(0.25, 1)
            o.append(f'<line x1="{x:.1f}" y1="{y - h:.1f}" x2="{x:.1f}" y2="{y + h:.1f}" stroke="{coul}" stroke-width="1.6"/>')


YP, YM = 104, 196
piste(YP, PERS, BLEU, "la personne")
piste(YM, MOD, TEAL, "le modèle")
# les paroles, au-dessus ou au-dessous des voix
o.append(f'<text x="{tx(0.0)}" y="{YP - 26}" font-size="11" fill="{BLEU}" font-style="italic">{PERS[0][2]}</text>')
o.append(f'<text x="{tx(3.55)}" y="{YP - 26}" font-size="11" fill="{BLEU}" font-style="italic">{PERS[1][2]}</text>')
o.append(f'<text x="{tx(1.2)}" y="{YM + 36}" font-size="11" fill="{TEAL}" font-style="italic">mm-hmm</text>')
o.append(f'<text x="{tx(2.55)}" y="{YM + 36}" font-size="11" fill="{TEAL}" font-style="italic">{MOD[1][2]}</text>')
o.append(f'<text x="{X1}" y="{YM - 28}" font-size="11" fill="{TEAL}" font-style="italic" text-anchor="end">{MOD[2][2]}</text>')
# les annotations
def note(x, y, l1, l2, coul=GRIS, ancre="middle"):
    o.append(f'<text x="{x}" y="{y}" font-size="10.5" fill="{coul}" text-anchor="{ancre}">{l1}</text>')
    o.append(f'<text x="{x}" y="{y + 13}" font-size="10.5" fill="{coul}" text-anchor="{ancre}">{l2}</text>')


o.append(f'<line x1="{tx(1.52)}" y1="{YM - 22}" x2="{tx(1.52)}" y2="{YP + 22}" stroke="{AXE}" stroke-width="1" stroke-dasharray="3 3"/>')
note(tx(1.52) - 8, YP + 40, "acquiescer sans", "interrompre", ancre="end")
o.append(f'<rect x="{tx(2.4)}" y="{YP + 26}" width="{tx(2.65) - tx(2.4):.1f}" height="{YM - YP - 52}" fill="{BRUN}" opacity="0.18"/>')
note(tx(2.52), YP + 40, "≈ 200 ms", "de silence", BRUN)
o.append(f'<line x1="{tx(3.85)}" y1="{YM - 22}" x2="{tx(3.85)}" y2="{YP + 22}" stroke="{ROUGE}" stroke-width="1.2" stroke-dasharray="3 3"/>')
note(tx(3.85) + 8, YP + 40, "interrompu,", "il s'arrête", ROUGE, ancre="start")
# l'axe du temps
for s in range(7):
    o.append(f'<line x1="{tx(s):.1f}" y1="250" x2="{tx(s):.1f}" y2="255" stroke="{GRIS}"/>')
    o.append(f'<text x="{tx(s):.1f}" y="268" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">{s}{NB}s</text>')
o.append(f'<line x1="{X0}" y1="250" x2="{X1}" y2="250" stroke="{GRIS}" stroke-width="1"/>')
# ── les deux flux de jetons ──
o.append(f'<rect x="20" y="296" width="{W - 40}" height="152" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
o.append(f'<text x="36" y="318" font-size="12.5" fill="{BRUN}" font-weight="700">Ce que voit le modèle{NB}: deux flux de jetons audio, un toutes les 80{NB}ms</text>')
DT = 0.08
CW = (X1 - X0) / (T / DT)


def flux(y, segs, coul, nom, sous):
    o.append(f'<text x="36" y="{y + 12}" font-size="11.5" fill="{coul}" font-weight="700">{nom}</text>')
    o.append(f'<text x="36" y="{y + 26}" font-size="10" fill="{ENCRE_PALE}">{sous}</text>')
    for k in range(int(T / DT)):
        t = (k + 0.5) * DT
        parle = any(a <= t <= b for a, b, _ in segs)
        o.append(f'<rect x="{X0 + k * CW + 0.6:.1f}" y="{y}" width="{CW - 1.2:.1f}" height="18" rx="1.5" '
                 f'fill="{coul if parle else "#ddd6c6"}" opacity="{rng.uniform(0.55, 1) if parle else 1:.2f}"/>')


flux(334, PERS, BLEU, "jetons écoutés", "la voix de la personne")
flux(374, MOD, TEAL, "jetons produits", "la voix du modèle")
o.append(f'<text x="{W / 2}" y="420" font-size="11" fill="{ENCRE}" text-anchor="middle">À chaque pas, le modèle lit le jeton de la personne et prédit le sien{NB}; '
         f'quand il doit se taire, il produit un jeton de silence (en gris).</text>')
o.append(f'<text x="{W / 2}" y="437" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">Échange illustratif{NB}; le rythme des jetons est celui du codec de Moshi (Kyutai, 2024).</text>')
o.append("</svg>")
(OUT / "duplex.svg").write_text("\n".join(o) + "\n")
print("duplex.svg écrit")
