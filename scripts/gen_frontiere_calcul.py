# /// script
# requires-python = ">=3.10"
# ///
"""Module 4, « Passer à l'échelle » : les modèles de frontière. Le calcul d'entraînement des modèles notables
recensés par Epoch AI, de 2018 à 2026, sur une échelle logarithmique, avec les seuils de 10²⁵ (AI Act) et de 10²⁶
opérations (lois de la Californie et de New York). En brun, les modèles qu'Epoch classe « de frontière » (parmi
les dix plus coûteux en calcul au moment de leur sortie). Données : scripts/data/epoch-calcul.csv, extrait de
https://epoch.ai/data/notable_ai_models.csv (CC BY 4.0)."""
import csv
import math
from datetime import date
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
OUT = RACINE / "static" / "images" / "module4" / "frontiere-calcul.svg"
DONNEES = RACINE / "scripts" / "data" / "epoch-calcul.csv"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "

W, H = 920, 540
X0, X1, Y0, Y1 = 92, 880, 74, 452          # zone du graphique
A0, A1, E0, E1 = 2018.0, 2027.0, 19, 28    # années et exposants de 10


def px(an):
    return X0 + (an - A0) / (A1 - A0) * (X1 - X0)


def py(flop):
    return Y1 - (math.log10(flop) - E0) / (E1 - E0) * (Y1 - Y0)


def annee(s):
    d = date.fromisoformat(s)
    return d.year + (d.timetuple().tm_yday - 1) / 365.25


EXP = "⁰¹²³⁴⁵⁶⁷⁸⁹"


def puissance(e):
    return "10" + "".join(EXP[int(c)] for c in str(e))


modeles = []
with DONNEES.open() as f:
    for r in csv.DictReader(f):
        if float(r["calcul_flop"]) >= 10 ** E0:
            modeles.append((r["modele"], annee(r["date"]), float(r["calcul_flop"]), r["frontiere"] == "1"))
par_nom = {m[0]: m for m in modeles}

o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Le calcul d'entraînement des modèles de frontière</title>",
     "<desc>Un nuage de points. L'axe horizontal donne la date de sortie, de 2018 à 2026, l'axe vertical le calcul "
     "utilisé pour l'entraînement, sur une échelle logarithmique, de 10 puissance 19 à 10 puissance 28 opérations. "
     "Chaque point est un modèle notable recensé par Epoch AI ; les modèles de frontière, en brun, montent d'environ "
     "un facteur dix tous les un an et demi. On lit GPT-1 en 2018, GPT-3 en 2020, GPT-4 en 2023, Llama 3.1 405B en "
     "2024, Grok 3, premier modèle au-delà de 10 puissance 26, en février 2025, et GPT-6 Astra en septembre 2026, "
     "proche de 10 puissance 27. Deux droites horizontales marquent les seuils : 10 puissance 25 opérations, celui "
     "de l'AI Act européen, et 10 puissance 26, celui des lois de la Californie et de New York. DeepSeek V3, "
     "en décembre 2024, proche des meilleurs modèles, reste sous le seuil européen.</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Le calcul d\'entraînement des modèles, de 2018 à 2026</text>',
     f'<rect x="{X0}" y="{Y0}" width="{X1 - X0}" height="{Y1 - Y0}" fill="{PANNEAU}" stroke="{BORD}"/>']


def texte(x, y, t, taille=10.5, coul=ENCRE, ancre="middle", gras=False, ital=False, halo=False):
    g = ' font-weight="700"' if gras else ""
    i = ' font-style="italic"' if ital else ""
    h = f' stroke="{PANNEAU}" stroke-width="4" stroke-linejoin="round" paint-order="stroke"' if halo else ""
    o.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{taille}" fill="{coul}" text-anchor="{ancre}"{g}{i}{h}>{t}</text>')


# Grille et axes
for e in range(E0, E1 + 1):
    y = py(10 ** e)
    if E0 < e < E1:
        o.append(f'<line x1="{X0}" y1="{y:.1f}" x2="{X1}" y2="{y:.1f}" stroke="{BORD}" stroke-width="0.8"/>')
    texte(X0 - 10, y + 4, puissance(e), 11, ENCRE_PALE, "end")
for an in range(2018, 2027):
    x = px(an + 0.5)
    texte(x, Y1 + 18, str(an), 11, ENCRE_PALE)
    if an > 2018:
        o.append(f'<line x1="{px(an):.1f}" y1="{Y1}" x2="{px(an):.1f}" y2="{Y1 + 5}" stroke="{AXE}"/>')
o.append(f'<text transform="translate(26 {(Y0 + Y1) / 2}) rotate(-90)" font-size="11" fill="{ENCRE_PALE}" '
         f'text-anchor="middle">calcul d\'entraînement (opérations)</text>')

# Seuils
for e, coul, etq in ((25, ROUGE, "AI Act (Union européenne)"), (26, ROUGE, "Californie, New York")):
    y = py(10 ** e)
    o.append(f'<line x1="{X0}" y1="{y:.1f}" x2="{X1}" y2="{y:.1f}" stroke="{coul}" stroke-width="1.6" stroke-dasharray="7 5"/>')
    texte(X0 + 12, y - 7, f"{etq} : {puissance(e)}", 10.5, coul, "start", gras=True)

# Points : d'abord les autres, puis ceux de frontière par-dessus
for nom, an, c, front in modeles:
    if not front and nom != "DeepSeek-V3":
        o.append(f'<circle cx="{px(an):.1f}" cy="{py(c):.1f}" r="2.6" fill="{GRIS}" fill-opacity="0.35"/>')
for nom, an, c, front in modeles:
    if front:
        o.append(f'<circle cx="{px(an):.1f}" cy="{py(c):.1f}" r="4" fill="{BRUN}" fill-opacity="0.9" stroke="{PANNEAU}" stroke-width="0.8"/>')

# Modèles nommés : (nom dans les données, étiquette, position de l'étiquette (année, calcul) ou décalage, ancre, couleur)
NOMMES = [("GPT-1", "GPT-1", (8, 4), "start", ENCRE),
          ("GPT-3 175B (davinci)", "GPT-3", (-9, -6), "end", ENCRE),
          ("GPT-4 (Mar 2023)", "GPT-4", (-9, -6), "end", ENCRE),
          ("Llama 3.1-405B", "Llama 3.1 405B (ouvert)", (2023.95, 2.6e26), "end", TEAL),
          ("DeepSeek-V3", "DeepSeek V3 (ouvert)", (2025.05, 6e22), "start", TEAL),
          ("Grok 3", "Grok 3", (-9, -8), "end", ENCRE),
          ("GPT-6 Astra", "GPT-6 Astra", (-9, -8), "end", ENCRE)]
for cle, etq, pos, ancre, coul in NOMMES:
    nom, an, c, front = par_nom[cle]
    x, y = px(an), py(c)
    if coul == TEAL:
        lx, ly = px(pos[0]), py(pos[1])
        o.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{lx + (4 if ancre == "end" else -4):.1f}" y2="{ly - 4:.1f}" '
                 f'stroke="{TEAL}" stroke-width="1"/>')
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.6" fill="{TEAL}" stroke="{PANNEAU}" stroke-width="0.8"/>')
        texte(lx, ly, etq, 10.5, coul, ancre, gras=True, halo=True)
    else:
        if not front:
            o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.4" fill="{GRIS}"/>')
        texte(x + pos[0], y + pos[1], etq, 10.5, coul, ancre, gras=True, halo=True)

# Légende
ly = Y1 + 50
o.append(f'<circle cx="{X0 + 6}" cy="{ly - 4}" r="4" fill="{BRUN}"/>')
texte(X0 + 16, ly, "modèle de frontière : parmi les dix plus coûteux en calcul à sa sortie", 10.5, ENCRE_PALE, "start")
o.append(f'<circle cx="{X0 + 6}" cy="{ly + 14}" r="2.6" fill="{GRIS}" fill-opacity="0.5"/>')
texte(X0 + 16, ly + 18, "autre modèle notable", 10.5, ENCRE_PALE, "start")
texte(X1, ly + 18, "données : Epoch AI, octobre 2026 ; calcul estimé", 9.5, GRIS, "end", ital=True)
o.append("</svg>")
OUT.write_text("\n".join(o) + "\n")
print(OUT.name, "écrit")
