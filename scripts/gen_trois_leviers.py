# /// script
# requires-python = ">=3.10"
# ///
"""Module 4, « Passer à l'échelle », section « Jusqu'où ? » : les trois leviers de l'échelle, de 2018 à 2026.
L'épaisseur de chaque bande est schématique : elle indique la place du levier dans l'effort des laboratoires, pas
une quantité mesurée. Au-dessus, la périodisation d'Ilya Sutskever (entretien avec Dwarkesh Patel, novembre 2025).
Dates des repères : articles et annonces des laboratoires, vérifiées."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4" / "trois-leviers.svg"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "

W, H = 920, 470
X0, X1, A0, A1 = 250, 890, 2018.0, 2027.0


def px(an):
    return X0 + (an - A0) / (A1 - A0) * (X1 - X0)


o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Les trois leviers de l'échelle</title>",
     "<desc>Une frise de 2018 à 2026 avec trois bandes horizontales, dont l'épaisseur indique, de façon schématique, "
     "la place de chaque levier dans l'effort des laboratoires. Première bande, agrandir le pré-entraînement, le modèle "
     "et ses données : épaisse dès le départ, avec GPT-2 en 2019, les lois d'échelle de Kaplan et GPT-3 en 2020, "
     "Chinchilla en 2022 et GPT-4 en 2023 ; à partir de la fin de 2024, la bande est hachurée, les rendements sont "
     "discutés, avec GPT-4.5 en février 2025 et GPT-6 Astra en septembre 2026. Deuxième bande, l'apprentissage par "
     "renforcement : un mince filet à partir de 2022, celui des préférences humaines, qui s'élargit à partir de o1, en "
     "septembre 2024, avec DeepSeek R1, o3 et Grok 4 en 2025. Troisième bande, le calcul au moment de la réponse : "
     "absente jusqu'à o1, puis de plus en plus large. Au-dessus, la périodisation d'Ilya Sutskever : l'âge de la "
     "recherche jusqu'en 2020, l'âge de l'échelle de 2020 à 2025, puis un retour à la recherche, avec de gros "
     "ordinateurs.</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Trois façons de dépenser plus de calcul</text>',
     '<defs><pattern id="hachures" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
     f'<rect width="7" height="7" fill="{BRUN}" fill-opacity="0.35"/><line x1="0" y1="0" x2="0" y2="7" stroke="{BRUN}" stroke-width="3"/></pattern></defs>']


def texte(x, y, t, taille=10.5, coul=ENCRE, ancre="middle", gras=False, ital=False):
    g = ' font-weight="700"' if gras else ""
    i = ' font-style="italic"' if ital else ""
    o.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{taille}" fill="{coul}" text-anchor="{ancre}"{g}{i}>{t}</text>')


# Périodisation de Sutskever
YS = 62
for a, b, etq in ((A0, 2020.0, "l'âge de la recherche"), (2020.0, 2025.0, "l'âge de l'échelle"),
                  (2025.0, A1, "retour à la recherche")):
    o.append(f'<rect x="{px(a) + 2:.1f}" y="{YS}" width="{px(b) - px(a) - 4:.1f}" height="24" rx="5" '
             f'fill="{PANNEAU}" stroke="{BORD}"/>')
    texte((px(a) + px(b)) / 2, YS + 16, etq, 10.5, ENCRE_PALE, ital=True)
texte(X0 - 16, YS + 16, "selon Ilya Sutskever (2025)", 10.5, GRIS, "end", ital=True)

# Grille des années
YH, YB = 100, 410
o.append(f'<rect x="{X0}" y="{YH}" width="{X1 - X0}" height="{YB - YH}" fill="{PANNEAU}" stroke="{BORD}"/>')
for an in range(2018, 2027):
    if an > 2018:
        o.append(f'<line x1="{px(an):.1f}" y1="{YH}" x2="{px(an):.1f}" y2="{YB}" stroke="{BORD}" stroke-width="0.8"/>')
    texte(px(an + 0.5), YB + 18, str(an), 11, ENCRE_PALE)


def bande(yc, profil, coul, hachure_des=None):
    """profil : liste de (année, épaisseur) ; la bande est symétrique autour de yc."""
    haut = [(px(a), yc - e / 2) for a, e in profil]
    bas = [(px(a), yc + e / 2) for a, e in reversed(profil)]
    pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in haut + bas)
    o.append(f'<polygon points="{pts}" fill="{coul}" fill-opacity="0.85"/>')
    if hachure_des:
        x = px(hachure_des)
        e = max(e for a, e in profil if a >= hachure_des)
        o.append(f'<rect x="{x:.1f}" y="{yc - e / 2:.1f}" width="{px(profil[-1][0]) - x:.1f}" height="{e:.1f}" fill="{PANNEAU}"/>')
        o.append(f'<rect x="{x:.1f}" y="{yc - e / 2:.1f}" width="{px(profil[-1][0]) - x:.1f}" height="{e:.1f}" fill="url(#hachures)"/>')


def repere(an, yc, e, etq, coul, dessus=True, ancre="middle"):
    """Un repère : trait fin sur la bande, étiquette au-dessus ou au-dessous."""
    x = px(an)
    y1, y2 = (yc - e / 2 - 10, yc - e / 2) if dessus else (yc + e / 2, yc + e / 2 + 10)
    o.append(f'<line x1="{x:.1f}" y1="{y1:.1f}" x2="{x:.1f}" y2="{y2:.1f}" stroke="{coul}" stroke-width="1.2"/>')
    o.append(f'<circle cx="{x:.1f}" cy="{(y1 if dessus else y2):.1f}" r="2.2" fill="{coul}"/>')
    dx = {"middle": 0, "end": 4, "start": -4}[ancre]
    texte(x + dx, y1 - 6 if dessus else y2 + 14, etq, 10, coul, ancre, gras=True)


FIN = 2026.85
LIGNES = [
    (160, "Agrandir le pré-entraînement", "le modèle et ses données", BRUN),
    (260, "Le renforcement", "après le pré-entraînement", TEAL),
    (352, "Réfléchir plus longtemps", "le calcul au moment de la réponse", BLEU),
]
for yc, t1, t2, coul in LIGNES:
    texte(X0 - 16, yc - 2, t1, 12, coul, "end", gras=True)
    texte(X0 - 16, yc + 14, t2, 10.5, ENCRE_PALE, "end")

# 1. Pré-entraînement
bande(160, [(A0 + 0.05, 30), (FIN, 30)], BRUN, hachure_des=2024.85)
for an, etq, dessus in ((2019.12, "GPT-2", True), (2020.05, "Kaplan", False), (2020.41, "GPT-3", True),
                        (2022.24, "Chinchilla", True), (2023.2, "GPT-4", True), (2025.16, "GPT-4.5", True),
                        (2026.67, "GPT-6 Astra", True)):
    repere(an, 160, 30, etq, ENCRE if an < 2024.85 else BRUN, dessus, "end" if an > 2026 else "middle")
texte(px(2025.85), 160 + 15 + 22, "des rendements discutés", 10, BRUN, ital=True)

# 2. Renforcement
bande(260, [(2022.0, 0), (2022.08, 4), (2024.6, 4), (2024.7, 6), (2025.6, 28), (FIN, 32)], TEAL)
texte(px(2022.1), 260 + 18, "préférences humaines (RLHF)", 10, TEAL, "start", ital=True)
for an, etq, dessus in ((2024.7, "o1", True), (2025.05, "R1", False), (2025.29, "o3", True), (2025.52, "Grok 4", False)):
    e = 6 + (an - 2024.7) / 0.9 * 22
    repere(an, 260, e, etq, TEAL, dessus)

# 3. Calcul au moment de la réponse
bande(352, [(2024.62, 0), (2024.7, 4), (2025.4, 20), (FIN, 28)], BLEU)
for an, etq, dessus in ((2024.7, "o1", True), (2024.97, "o3 et ARC", False)):
    e = 4 + (an - 2024.7) / 0.7 * 16
    repere(an, 352, e, etq, BLEU, dessus)

texte(X1, YB + 42, "épaisseur des bandes schématique : la place du levier dans l'effort des laboratoires", 9.5, GRIS, "end", ital=True)
o.append("</svg>")
OUT.write_text("\n".join(o) + "\n")
print(OUT.name, "écrit")
