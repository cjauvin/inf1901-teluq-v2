"""Module 4, « Passer à l'échelle » : la taille des modèles et une loi d'échelle.

Sources des chiffres : articles et fiches des modèles (GPT-1 et GPT-2, OpenAI 2018-2019 ; GPT-3, Brown et al. 2020 ;
Chinchilla, Hoffmann et al. 2022 ; Llama 3.1, Meta 2024). La taille de GPT-4 et des modèles suivants d'OpenAI,
Google ou Anthropic n'a pas été publiée. La seconde figure est un schéma, sans données.
"""
import math
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "
MODELES = [("GPT-1", "2018", 0.117e9, None), ("GPT-2", "2019", 1.5e9, None), ("GPT-3", "2020", 175e9, 300e9),
           ("Chinchilla", "2022", 70e9, 1.4e12), ("Llama 3.1", "2024", 405e9, 15e12)]


def lisible(x):                                       # en milliards plutôt qu'en billions, pour éviter la confusion avec l'anglais
    if x >= 1e12:
        return f"{x / 1e9:,.0f}".replace(",", NB) + f"{NB}milliards"
    for v, nom in [(1e9, "milliard"), (1e6, "million")]:
        if x >= v:
            q = x / v
            t = f"{q:.0f}" if q >= 10 else f"{q:.1f}".replace(".", ",").replace(",0", "")
            return f"{t}{NB}{nom}{'s' if q >= 2 else ''}"
    return str(x)


W, H = 700, 444
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>La croissance des modèles de langage</title>",
     "<desc>Deux diagrammes à barres sur une échelle logarithmique, où chaque graduation vaut dix fois la précédente. À gauche, le "
     "nombre de paramètres : 117 millions pour GPT-1 en 2018, 1,5 milliard pour GPT-2 en 2019, 175 milliards pour GPT-3 en 2020, "
     "70 milliards pour Chinchilla en 2022, 405 milliards pour Llama 3.1 en 2024. À droite, le nombre de jetons d'entraînement : "
     "300 milliards pour GPT-3, 1 400 milliards pour Chinchilla, 15 000 milliards pour Llama 3.1.</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Six ans de croissance (échelle logarithmique{NB}: chaque graduation vaut dix fois la précédente)</text>']


def panneau(x0, titre, valeurs, lo, hi, coul):
    l, h, y0 = 300, 280, 70
    o.append(f'<rect x="{x0}" y="{y0 - 22}" width="{l + 20}" height="{h + 80}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
    o.append(f'<text x="{x0 + (l + 20) / 2}" y="{y0}" font-size="13.5" fill="{TEAL}" text-anchor="middle" font-weight="700">{titre}</text>')
    base = y0 + h - 10
    echelle = lambda v: (math.log10(v) - lo) / (hi - lo) * (h - 50)
    for e in range(lo, hi + 1):
        y = base - echelle(10 ** e)
        o.append(f'<line x1="{x0 + 10}" y1="{y:.1f}" x2="{x0 + l + 10}" y2="{y:.1f}" stroke="{BORD}" stroke-width="1"/>')
    pas = l / len(valeurs)
    for k, (nom, an, v) in enumerate(valeurs):
        x = x0 + 10 + k * pas + pas * 0.18
        lb = pas * 0.64
        if v is None:
            o.append(f'<text x="{x + lb / 2:.1f}" y="{base - 6}" font-size="11" fill="{GRIS}" text-anchor="middle">—</text>')
        else:
            hb = echelle(v)
            o.append(f'<rect x="{x:.1f}" y="{base - hb:.1f}" width="{lb:.1f}" height="{hb:.1f}" fill="{coul}"/>')
            o.append(f'<text x="{x + lb / 2:.1f}" y="{base - hb - 6:.1f}" font-size="10.5" fill="{ENCRE}" text-anchor="middle">{lisible(v)}</text>')
        o.append(f'<text x="{x + lb / 2:.1f}" y="{base + 16}" font-size="11" fill="{ENCRE}" text-anchor="middle" font-weight="600">{nom}</text>')
        o.append(f'<text x="{x + lb / 2:.1f}" y="{base + 30}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">{an}</text>')
    o.append(f'<line x1="{x0 + 10}" y1="{base}" x2="{x0 + l + 10}" y2="{base}" stroke="{AXE}" stroke-width="1.4"/>')


panneau(20, "Paramètres", [(n, a, p) for n, a, p, _ in MODELES], 8, 12, BLEU)
panneau(360, "Jetons d'entraînement", [(n, a, t) for n, a, _, t in MODELES], 11, 14, TEAL)
o.append(f'<text x="{W / 2}" y="{H - 10}" font-size="11.5" fill="{GRIS}" text-anchor="middle">La taille de GPT-4 (2023) et des modèles suivants des grandes entreprises n\'a pas été publiée.</text>')
o.append("</svg>")
(OUT / "taille-des-modeles.svg").write_text("\n".join(o) + "\n")

# ── Schéma d'une loi d'échelle ────────────────────────────────────────────────
W, H = 700, 360
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Une loi d'échelle</title>",
     "<desc>Un schéma. L'axe horizontal donne la quantité de calcul utilisée pour l'entraînement, l'axe vertical l'erreur du modèle "
     "sur des textes qu'il n'a jamais vus, tous deux sur une échelle logarithmique. Des points, un par modèle entraîné, s'alignent "
     "sur une droite qui descend régulièrement. La droite est prolongée en pointillé vers la droite : on peut prédire l'erreur d'un "
     "modèle plus grand avant de l'entraîner.</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Une loi d\'échelle (schéma)</text>']
x0, y0, x1, y1 = 90, 60, 640, 290
o.append(f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="{AXE}" stroke-width="1.6"/>')
o.append(f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="{AXE}" stroke-width="1.6"/>')
for k in range(6):
    x = x0 + 30 + k * 95
    o.append(f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y1 + 6}" stroke="{AXE}" stroke-width="1.4"/>')
    o.append(f'<text x="{x}" y="{y1 + 22}" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">{"1" if k == 0 else "×" + "10" + ("" if k == 1 else "<tspan baseline-shift=\"super\" font-size=\"8\">" + str(k) + "</tspan>")}</text>')
o.append(f'<text x="{(x0 + x1) / 2}" y="{y1 + 48}" font-size="13" fill="{ENCRE}" text-anchor="middle">calcul utilisé pour l\'entraînement (échelle logarithmique)</text>')
o.append(f'<text x="34" y="{(y0 + y1) / 2}" font-size="13" fill="{ENCRE}" text-anchor="middle" transform="rotate(-90 34 {(y0 + y1) / 2})">erreur sur des textes neufs</text>')
pts = [(x0 + 30 + k * 95 * 0.7, 90 + k * 0.7 * 33 + d) for k, d in zip(range(7), [4, -5, 3, -3, 5, -2, 1])]
o.append(f'<line x1="{x0 + 20}" y1="86" x2="{x0 + 30 + 4.2 * 95}" y2="{90 + 4.2 * 33}" stroke="{BLEU}" stroke-width="2.2"/>')
o.append(f'<line x1="{x0 + 30 + 4.2 * 95}" y1="{90 + 4.2 * 33}" x2="{x0 + 30 + 5.2 * 95}" y2="{90 + 5.2 * 33}" stroke="{BLEU}" stroke-width="2.2" stroke-dasharray="7 6"/>')
for x, y in pts[:6]:
    o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{ROUGE}" stroke="{FOND}" stroke-width="1.5"/>')
o.append(f'<circle cx="{x0 + 30 + 5.2 * 95:.1f}" cy="{90 + 5.2 * 33:.1f}" r="7" fill="none" stroke="{BRUN}" stroke-width="2.5"/>')
o.append(f'<text x="{x0 + 30 + 5.2 * 95 - 18:.1f}" y="{y1 - 10}" font-size="12" fill="{BRUN}" text-anchor="end" font-weight="700">le modèle suivant, prévu avant d\'être entraîné</text>')
o.append(f'<text x="430" y="110" font-size="12" fill="{ENCRE_PALE}">chaque point est un modèle entraîné</text>')
o.append("</svg>")
(OUT / "loi-d-echelle.svg").write_text("\n".join(o) + "\n")
print("taille-des-modeles.svg et loi-d-echelle.svg écrits")
