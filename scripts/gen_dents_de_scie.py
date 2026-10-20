# /// script
# requires-python = ">=3.10"
# ///
"""Module 5, « Qu'est-ce que l'intelligence ? » : l'intelligence en dents de scie. À gauche, la frontière en dents de
scie (Dell'Acqua et al., 2023, popularisée par Ethan Mollick) : six tâches de difficulté comparable pour un humain,
placées sur un même cercle ; la frontière des capacités du modèle passe tantôt au-delà, tantôt en deçà. À droite, un
profil de capacités schématique : régulier pour un humain, hérissé pour un modèle (Karpathy)."""
import math
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module5" / "dents-de-scie.svg"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "

W, H = 880, 440
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Une intelligence en dents de scie</title>",
     "<desc>Deux panneaux. À gauche, la frontière en dents de scie : six tâches de difficulté comparable pour un humain "
     "sont placées sur un même cercle pointillé. La frontière des capacités d'un modèle de langage, une forme hérissée, "
     "passe au-delà de certaines tâches, que le modèle réussit (résumer un article, écrire un programme, traduire un "
     "texte), et en deçà d'autres, qu'il rate (compter les r de « strawberry », comparer 9,11 et 9,9, la tâche piège de "
     "l'étude BCG). À droite, un profil de capacités schématique sur huit tâches : le profil d'un humain est régulier, "
     "celui d'un modèle est hérissé, très haut en culture générale, en mathématiques d'olympiade ou en programmation, "
     "très bas pour compter les lettres d'un mot ou apprendre d'une seule expérience.</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Une intelligence en dents de scie</text>']


def texte(x, y, t, taille=11, coul=ENCRE, ancre="middle", gras=False, ital=False):
    g = ' font-weight="700"' if gras else ""
    i = ' font-style="italic"' if ital else ""
    o.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{taille}" fill="{coul}" text-anchor="{ancre}"{g}{i}>{t}</text>')


# ── panneau gauche : la frontière ──
o.append(f'<rect x="20" y="50" width="440" height="370" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
texte(240, 76, "La frontière en dents de scie", 12.5, BLEU, gras=True)
CX, CY, R = 240, 236, 74
TACHES = [(-60, True, ["résumer", "un article"]), (0, False, ["compter les r", "de « strawberry »"]),
          (60, True, ["écrire", "un programme"]), (120, False, ["comparer", "9,11 et 9,9"]),
          (180, True, ["traduire", "un texte"]), (240, False, ["la tâche piège", "de l'étude BCG"])]
# la frontière du modèle : pointes au-delà des tâches réussies, creux en deçà des tâches ratées
pts = []
for k in range(72):
    a = -90 + k * 5
    t, ok, _ = min(TACHES, key=lambda T: abs(((a - T[0]) + 180) % 360 - 180))
    ecart = abs(((a - t) + 180) % 360 - 180)
    pic = 116 if ok else 42
    r = pic + (80 - pic) * min(ecart / 30, 1) ** 0.7
    r += 5 * math.sin(k * 1.7)        # un peu d'irrégularité
    pts.append(f"{CX + r * math.cos(math.radians(a)):.1f},{CY + r * math.sin(math.radians(a)):.1f}")
o.append(f'<polygon points="{" ".join(pts)}" fill="{BLEU}" fill-opacity="0.13" stroke="{BLEU}" stroke-width="2" stroke-linejoin="round"/>')
o.append(f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="none" stroke="{TEAL}" stroke-width="1.6" stroke-dasharray="5 4"/>')
for a, ok, lignes in TACHES:
    c, sn = math.cos(math.radians(a)), math.sin(math.radians(a))
    x, y = CX + R * c, CY + R * sn
    coul = BLEU if ok else ROUGE
    o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{coul}" stroke="#ffffff" stroke-width="1.5"/>')
    ancre = "start" if c > 0 else "end"
    if abs(c) > 0.9:
        lx, ly = CX + (126 if c > 0 else -126), CY
    else:
        lx, ly = CX + (70 if c > 0 else -70), CY + 140 * sn
    for j, l in enumerate(lignes):
        texte(lx, ly - 3 + j * 13, l, 10.5, coul, ancre, gras=(j == 0))
texte(CX, CY - 3, "même difficulté", 10, TEAL, ital=True)
texte(CX, CY + 10, "pour un humain", 10, TEAL, ital=True)
o.append(f'<rect x="40" y="396" width="14" height="10" fill="{BLEU}" fill-opacity="0.13" stroke="{BLEU}" stroke-width="1.5"/>')
texte(60, 405, "ce que le modèle réussit", 10.5, BLEU, "start")
o.append(f'<line x1="250" y1="401" x2="272" y2="401" stroke="{TEAL}" stroke-width="1.6" stroke-dasharray="5 4"/>')
texte(278, 405, "tâches comparables", 10.5, TEAL, "start")

# ── panneau droit : le profil ──
o.append(f'<rect x="476" y="50" width="384" height="370" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
texte(668, 76, "Deux profils de capacités", 12.5, BLEU, gras=True)
PROFIL = [("culture générale", 0.95, 0.55), ("mathématiques d'olympiade", 0.9, 0.3), ("programmation", 0.85, 0.45),
          ("rédaction", 0.85, 0.6), ("compter les lettres d'un mot", 0.15, 0.95), ("comparer 9,11 et 9,9", 0.35, 0.95),
          ("sens commun physique", 0.4, 0.9), ("apprendre d'une seule expérience", 0.1, 0.85)]
X0, X1, Y0, DY = 664, 840, 104, 34
o.append(f'<line x1="{X0}" y1="{Y0 - 14}" x2="{X0}" y2="{Y0 + DY * len(PROFIL) - 18}" stroke="{AXE}" stroke-width="1.2"/>')
humain = []
for k, (nom, ia, h) in enumerate(PROFIL):
    y = Y0 + k * DY
    texte(X0 - 8, y + 4, nom, 10.5, ENCRE, "end")
    o.append(f'<rect x="{X0}" y="{y - 7}" width="{(X1 - X0) * ia:.1f}" height="14" rx="2" fill="{BLEU}" fill-opacity="0.75"/>')
    humain.append((X0 + (X1 - X0) * h, y))
o.append(f'<polyline points="{" ".join(f"{x:.1f},{y}" for x, y in humain)}" fill="none" stroke="{TEAL}" stroke-width="2"/>')
for x, y in humain:
    o.append(f'<circle cx="{x:.1f}" cy="{y}" r="4" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="2"/>')
o.append(f'<rect x="500" y="388" width="18" height="10" rx="2" fill="{BLEU}" fill-opacity="0.75"/>')
texte(524, 397, "un modèle de langage", 10.5, BLEU, "start")
o.append(f'<line x1="668" y1="393" x2="690" y2="393" stroke="{TEAL}" stroke-width="2"/><circle cx="679" cy="393" r="4" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="2"/>')
texte(696, 397, "un humain cultivé", 10.5, TEAL, "start")
texte(668, 413, "valeurs schématiques", 9.5, GRIS, ital=True)
o.append("</svg>")
OUT.write_text("\n".join(o) + "\n")
print(OUT.name, "écrit")
