# /// script
# requires-python = ">=3.10,<3.13"
# dependencies = ["torch", "numpy", "scikit-learn"]
# ///
"""Module 4, « Prédire le mot suivant » : une petite expérience réelle d'oubli catastrophique. Un petit réseau apprend
d'abord à reconnaître les chiffres manuscrits 0 à 4 (tâche A), puis seulement les chiffres 5 à 9 (tâche B). Sa justesse
sur la tâche A s'effondre pendant qu'il apprend la tâche B. Si l'on rejoue quelques anciens exemples parmi les nouveaux,
il n'oublie presque rien.

Les chiffres sont ceux de scikit-learn (8 × 8 pixels, livrés avec la bibliothèque).

    uv run scripts/gen_oubli_catastrophique.py
"""
from pathlib import Path
import numpy as np
import torch
from torch import nn
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
X, y = load_digits(return_X_y=True)
X = X / 16.0
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0, stratify=y)
t = lambda a, d=torch.float32: torch.tensor(a, dtype=d)
A_tr, B_tr = ytr < 5, ytr >= 5
A_te, B_te = yte < 5, yte >= 5
PAS = 300                                                      # pas d'entraînement par tâche
LOT = 32


def experience(rejouer, graine=0):
    torch.manual_seed(graine); rng = np.random.default_rng(graine)
    m = nn.Sequential(nn.Linear(64, 64), nn.ReLU(), nn.Linear(64, 10))
    opt = torch.optim.SGD(m.parameters(), lr=0.1)
    ia, ib = np.flatnonzero(A_tr), np.flatnonzero(B_tr)
    gardes = rng.choice(ia, 50, replace=False)                 # quelques anciens exemples, mis de côté pour être rejoués
    courbes = {"A": [], "B": []}

    def justesse(masque):
        with torch.no_grad():
            return float((m(t(Xte[masque])).argmax(1) == t(yte[masque], torch.long)).float().mean())

    for pas in range(2 * PAS + 1):
        if pas % 5 == 0:
            courbes["A"].append(justesse(A_te)); courbes["B"].append(justesse(B_te))
        if pas == 2 * PAS:
            break
        if pas < PAS:
            lot = rng.choice(ia, LOT)
        elif rejouer:
            lot = np.concatenate([rng.choice(ib, LOT - 8), rng.choice(gardes, 8)])
        else:
            lot = rng.choice(ib, LOT)
        perte = nn.functional.cross_entropy(m(t(Xtr[lot])), t(ytr[lot], torch.long))
        opt.zero_grad(); perte.backward(); opt.step()
    return {k: np.array(v) for k, v in courbes.items()}


sans = experience(False)
avec = experience(True)
print("sans rejouer : A", round(sans["A"][PAS // 5], 2), "→", round(sans["A"][-1], 2), "; B →", round(sans["B"][-1], 2))
print("avec rejouer : A", round(avec["A"][PAS // 5], 2), "→", round(avec["A"][-1], 2), "; B →", round(avec["B"][-1], 2))

# ── la figure ──
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
pc = lambda v: f"{v * 100:.0f}{NB}%"
W, H = 840, 430
GX, GY, GW, GH = 90, 96, 520, 250                              # le graphique
n = len(sans["A"])
px = lambda k: GX + k / (n - 1) * GW
py = lambda v: GY + (1 - v) * GH
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>L'oubli catastrophique</title>",
     "<desc>Un graphique de la justesse d'un petit réseau au fil de l'entraînement. Pendant la première moitié, il apprend à "
     "reconnaître les chiffres manuscrits 0 à 4 (tâche A), et sa justesse sur cette tâche monte à "
     f"{pc(sans['A'][PAS // 5])}. Pendant la seconde moitié, on ne lui montre plus que les chiffres 5 à 9 (tâche B). Sa justesse "
     f"sur la tâche B monte à {pc(sans['B'][-1])}, mais celle sur la tâche A s'effondre, jusqu'à {pc(sans['A'][-1])} : il a "
     "oublié. Une courbe en pointillés montre la même expérience quand on rejoue quelques anciens exemples de la tâche A parmi "
     f"les nouveaux : la justesse sur la tâche A reste à {pc(avec['A'][-1])}.</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">L\'oubli catastrophique{NB}: apprendre B fait oublier A</text>',
     f'<rect x="20" y="52" width="{W - 40}" height="{H - 72}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>']
# les deux phases
xm = px(PAS // 5)
o.append(f'<rect x="{xm}" y="{GY}" width="{GX + GW - xm}" height="{GH}" fill="#f3ecdc"/>')
o.append(f'<text x="{(GX + xm) / 2}" y="{GY - 14}" font-size="12" fill="{TEAL}" text-anchor="middle" font-weight="700">on entraîne sur A{NB}: chiffres 0 à 4</text>')
o.append(f'<text x="{(xm + GX + GW) / 2}" y="{GY - 14}" font-size="12" fill="{BLEU}" text-anchor="middle" font-weight="700">puis seulement sur B{NB}: chiffres 5 à 9</text>')
o.append(f'<line x1="{xm}" y1="{GY}" x2="{xm}" y2="{GY + GH}" stroke="{AXE}" stroke-width="1.2" stroke-dasharray="4 3"/>')
# les axes
for v in (0, 0.25, 0.5, 0.75, 1):
    o.append(f'<line x1="{GX}" y1="{py(v)}" x2="{GX + GW}" y2="{py(v)}" stroke="{BORD}" stroke-width="0.8"/>')
    o.append(f'<text x="{GX - 8}" y="{py(v) + 4}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="end">{pc(v)}</text>')
o.append(f'<line x1="{GX}" y1="{GY + GH}" x2="{GX + GW}" y2="{GY + GH}" stroke="{AXE}" stroke-width="1.2"/>')
o.append(f'<text x="{GX - 50}" y="{GY + GH / 2}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle" transform="rotate(-90 {GX - 50} {GY + GH / 2})">justesse</text>')
o.append(f'<text x="{GX + GW / 2}" y="{GY + GH + 22}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">pas d\'entraînement →</text>')


def courbe(v, c, tirets=False, l=2.4, debut=0):
    pts = " ".join(f"{px(k):.1f},{py(v[k]):.1f}" for k in range(debut, n))
    o.append(f'<polyline points="{pts}" fill="none" stroke="{c}" stroke-width="{l}" stroke-linejoin="round"'
             + (' stroke-dasharray="6 4"' if tirets else "") + "/>")


courbe(sans["B"], BLEU, debut=PAS // 5)                      # B n'est pas entraînée avant la seconde phase
courbe(avec["A"], TEAL, tirets=True, l=2, debut=PAS // 5)
courbe(sans["A"], TEAL)
# les étiquettes, au bout des courbes
xe = GX + GW + 10


def etiquette(v, c, l1, l2, dy=0):
    y = py(v) + dy
    o.append(f'<text x="{xe}" y="{y - 2}" font-size="11.5" fill="{c}" font-weight="700">{l1}</text>')
    o.append(f'<text x="{xe}" y="{y + 12}" font-size="10.5" fill="{c}">{l2}</text>')


etiquette(sans["B"][-1], BLEU, f"tâche B{NB}: {pc(sans['B'][-1])}", "apprise", dy=-14)
etiquette(avec["A"][-1], TEAL, f"tâche A{NB}: {pc(avec['A'][-1])}", "en rejouant d'anciens exemples", dy=16)
etiquette(sans["A"][-1], TEAL, f"tâche A{NB}: {pc(sans['A'][-1])}", "oubliée", dy=-4)
o[-1] = o[-1].replace(f'fill="{TEAL}">oubliée', f'fill="{ROUGE}" font-weight="700">oubliée')
o.append(f'<text x="{GX + GW / 2}" y="{H - 34}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">trait plein{NB}: on ne montre que les nouveaux exemples{NB}; '
         f'pointillés{NB}: on y mêle 8 anciens exemples sur 32</text>')
o.append("</svg>")
(OUT / "oubli-catastrophique.svg").write_text("\n".join(o) + "\n")
print("oubli-catastrophique.svg écrit")
