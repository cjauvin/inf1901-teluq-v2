# /// script
# requires-python = ">=3.10"
# ///
"""Module 4, « Prédire le mot suivant » : l'expérience des arbres généalogiques (Rumelhart, Hinton et Williams,
Nature, 1986). À gauche, les deux familles de l'article, anglaise et italienne, de même structure. À droite, le
vecteur appris pour quelques personnes : parmi ses six nombres, l'un code la nationalité, un autre la génération,
un autre la branche de la famille, sans que personne les ait programmés. Les valeurs sont schématiques."""
import random
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4" / "arbres-genealogiques.svg"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
rng = random.Random(11)

W, H = 920, 480
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Les arbres généalogiques de 1986</title>",
     "<desc>Deux panneaux. À gauche, deux arbres généalogiques de même structure, sur trois générations : une famille "
     "anglaise (Christopher et Penelope, Andrew et Christine ; Margaret et Arthur, Victoria et James, Jennifer et "
     "Charles ; Colin et Charlotte) et une famille italienne (Roberto et Maria, Pierro et Francesca ; Gina et Emilio, "
     "Lucia et Marco, Angela et Tomaso ; Alfonso et Sophia). Le réseau apprend des faits comme « le père de Victoria est "
     "Christopher ». À droite, le vecteur de six nombres appris pour quelques personnes : un des nombres distingue les "
     "Anglais des Italiens, un autre la génération, un autre la branche de la famille. Personne n'a donné ces "
     "caractéristiques au réseau.</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Des caractéristiques que personne n\'a programmées (1986)</text>']


def texte(x, y, t, taille=10.5, coul=ENCRE, ancre="middle", gras=False, ital=False):
    g = ' font-weight="700"' if gras else ""
    i = ' font-style="italic"' if ital else ""
    o.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{taille}" fill="{coul}" text-anchor="{ancre}"{g}{i}>{t}</text>')


CW = 5.6   # largeur moyenne d'un caractère à 10,5 px


def couple(cx, y, a, b, coul):
    """Écrit « a = b » centré sur cx ; renvoie les centres des deux prénoms."""
    texte(cx - 8, y, a, 10.5, coul, "end")
    texte(cx, y, "=", 10.5, GRIS)
    texte(cx + 8, y, b, 10.5, coul, "start")
    return cx - 8 - len(a) * CW / 2, cx + 8 + len(b) * CW / 2


def descente(x_parents, y_parents, enfants, y_enfants):
    ym = (y_parents + y_enfants) / 2 - 4
    o.append(f'<line x1="{x_parents:.1f}" y1="{y_parents + 4}" x2="{x_parents:.1f}" y2="{ym:.1f}" stroke="{AXE}" stroke-width="1.3"/>')
    xs = [x for x in enfants]
    o.append(f'<line x1="{min(xs + [x_parents]):.1f}" y1="{ym:.1f}" x2="{max(xs + [x_parents]):.1f}" y2="{ym:.1f}" stroke="{AXE}" stroke-width="1.3"/>')
    for x in xs:
        o.append(f'<line x1="{x:.1f}" y1="{ym:.1f}" x2="{x:.1f}" y2="{y_enfants - 12}" stroke="{AXE}" stroke-width="1.3"/>')


def arbre(y0, noms, coul, titre):
    texte(36, y0 - 18, titre, 11.5, coul, "start", gras=True)
    g1, g2, g3 = y0 + 12, y0 + 66, y0 + 120
    (c1a, c1b), (c2a, c2b) = couple(130, g1, *noms[0:2], coul), couple(350, g1, *noms[2:4], coul)
    m1, m2, m3 = couple(86, g2, *noms[4:6], coul), couple(250, g2, *noms[6:8], coul), couple(410, g2, *noms[8:10], coul)
    descente(130, g1, [m1[1], m2[0]], g2)          # Arthur et Victoria, enfants du premier couple
    descente(350, g1, [m2[1], m3[0]], g2)          # James et Jennifer, enfants du second
    x3a, x3b = 222, 284
    descente(250, g2, [x3a, x3b], g3)
    texte(x3a, g3, noms[10], 10.5, coul)
    texte(x3b, g3, noms[11], 10.5, coul)


o.append(f'<rect x="20" y="50" width="490" height="410" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
arbre(92, ["Christopher", "Penelope", "Andrew", "Christine", "Margaret", "Arthur", "Victoria", "James",
           "Jennifer", "Charles", "Colin", "Charlotte"], BLEU, "Une famille anglaise")
arbre(290, ["Roberto", "Maria", "Pierro", "Francesca", "Gina", "Emilio", "Lucia", "Marco",
            "Angela", "Tomaso", "Alfonso", "Sophia"], ROUGE, "Une famille italienne")
texte(265, 444, "Le réseau apprend 100 faits comme « le père de Victoria est Christopher ».", 10.5, ENCRE_PALE, ital=True)

# ── à droite : les vecteurs appris ──
X0 = 528
o.append(f'<rect x="{X0}" y="50" width="372" height="410" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
texte(X0 + 186, 76, "Le vecteur appris pour chaque personne", 12, TEAL, gras=True)
PERS = [("Christopher", 0, 0, 0), ("Andrew", 0, 0, 1), ("Victoria", 0, 1, 0), ("Colin", 0, 2, None),
        ("Roberto", 1, 0, 0), ("Pierro", 1, 0, 1), ("Lucia", 1, 1, 0)]
CX, CY0, CS, DY = X0 + 128, 140, 24, 32
cols = {0: "nationalité", 1: "génération", 5: "branche"}
for j, lab in cols.items():
    x, y = CX + j * CS + CS / 2 - 2, CY0 - 8
    o.append(f'<text x="{x:.1f}" y="{y}" font-size="9.5" fill="{ENCRE}" font-weight="700" transform="rotate(-38 {x:.1f} {y})">{lab}</text>')
for k, (nom, nat, gen, branche) in enumerate(PERS):
    y = CY0 + k * DY
    texte(CX - 12, y + 16, nom, 10.5, BLEU if nat == 0 else ROUGE, "end", gras=True)
    for j in range(6):
        if j == 0:
            c, op = (BLEU, 0.85) if nat == 0 else (ROUGE, 0.85)
        elif j == 1:
            c, op = GRIS, [0.2, 0.55, 0.9][gen]
        elif j == 5:
            c, op = (TEAL, 0.85) if branche == 0 else ((BRUN, 0.85) if branche == 1 else (AXE, 0.25))
        else:
            c, op = AXE, rng.uniform(0.15, 0.6)
        o.append(f'<rect x="{CX + j * CS:.1f}" y="{y}" width="{CS - 3}" height="{CS - 3}" rx="2" fill="{c}" fill-opacity="{op:.2f}" stroke="{c}" stroke-width="0.8"/>')
# légende
LY = CY0 + len(PERS) * DY + 14
o.append(f'<rect x="{X0 + 24}" y="{LY}" width="12" height="12" fill="{BLEU}" fill-opacity="0.85"/>')
texte(X0 + 42, LY + 10, "anglais", 10, ENCRE_PALE, "start")
o.append(f'<rect x="{X0 + 92}" y="{LY}" width="12" height="12" fill="{ROUGE}" fill-opacity="0.85"/>')
texte(X0 + 110, LY + 10, "italien", 10, ENCRE_PALE, "start")
for k, op in enumerate([0.2, 0.55, 0.9]):
    o.append(f'<rect x="{X0 + 160 + k * 14}" y="{LY}" width="12" height="12" fill="{GRIS}" fill-opacity="{op}"/>')
texte(X0 + 206, LY + 10, "1ʳᵉ à 3ᵉ génération", 10, ENCRE_PALE, "start")
o.append(f'<rect x="{X0 + 24}" y="{LY + 20}" width="12" height="12" fill="{TEAL}" fill-opacity="0.85"/>')
o.append(f'<rect x="{X0 + 38}" y="{LY + 20}" width="12" height="12" fill="{BRUN}" fill-opacity="0.85"/>')
texte(X0 + 56, LY + 30, "l'une ou l'autre branche de la famille", 10, ENCRE_PALE, "start")
texte(X0 + 186, 444, "Valeurs schématiques, d'après l'article.", 9.5, GRIS, ital=True)
o.append("</svg>")
OUT.write_text("\n".join(o) + "\n")
print(OUT.name, "écrit")
