"""Module 3, « Un neurone » : le schéma d'un neurone, et un chiffre manuscrit en entrée."""
import math
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module3"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "
POLICE = 'font-family="system-ui, -apple-system, sans-serif"'


def entete(w, h, titre, desc):
    return ['<?xml version="1.0" encoding="UTF-8"?>',
            f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" {POLICE}>',
            f"<title>{titre}</title>", f"<desc>{desc}</desc>",
            f'<defs><marker id="pointe" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
            f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
            f'<rect x="0" y="0" width="{w}" height="{h}" rx="14" fill="{FOND}" stroke="{BORD}"/>']


def fleche(o, x1, y1, x2, y2, epaisseur=2.0):
    o.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{GRIS}" stroke-width="{epaisseur}" marker-end="url(#pointe)"/>')


# ---------------------------------------------------------------- le schéma d'un neurone
def schema():
    W, H = 700, 330
    o = entete(W, H, "Le schéma d'un neurone artificiel",
               f"De gauche à droite{NB}: deux entrées, x1 et x2, reliées chacune par une flèche qui porte un poids, w1 et w2, à un neurone. "
               f"Le neurone fait deux opérations{NB}: la somme pondérée des entrées, à laquelle s'ajoute le biais b, puis la fonction d'activation sigmoïde. "
               "Une flèche sort du neurone vers la sortie, un nombre entre 0 et 1.")
    o.append(f'<text x="{W / 2}" y="38" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Un neurone artificiel</text>')
    # entrées
    for y, nom, poids in ((120, "x₁", "w₁"), (230, "x₂", "w₂")):
        o.append(f'<circle cx="90" cy="{y}" r="26" fill="{PANNEAU}" stroke="{BLEU}" stroke-width="2"/>')
        o.append(f'<text x="90" y="{y + 6}" font-size="18" fill="{BLEU}" text-anchor="middle" font-weight="700">{nom}</text>')
        fleche(o, 118, y, 268, 175 + (y - 175) * 0.32)
        o.append(f'<text x="186" y="{y + (-14 if y < 175 else 34) + (175 - y) * 0.25:.0f}" font-size="16" fill="{BRUN}" text-anchor="middle" font-weight="700">{poids}</text>')
    o.append(f'<text x="90" y="290" font-size="12.5" fill="{GRIS}" text-anchor="middle">entrées</text>')
    o.append(f'<text x="186" y="290" font-size="12.5" fill="{BRUN}" text-anchor="middle">poids</text>')
    # le neurone : deux étapes dans un même cadre
    o.append(f'<rect x="272" y="105" width="256" height="140" rx="70" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="2.5"/>')
    o.append(f'<line x1="400" y1="118" x2="400" y2="232" stroke="{AXE}" stroke-width="1.5" stroke-dasharray="4 4"/>')
    o.append(f'<text x="340" y="170" font-size="30" fill="{TEAL}" text-anchor="middle" font-weight="700">Σ</text>')
    o.append(f'<text x="340" y="198" font-size="12.5" fill="{ENCRE_PALE}" text-anchor="middle">somme + biais</text>')
    o.append(f'<text x="340" y="214" font-size="12" fill="{BRUN}" text-anchor="middle" font-weight="700">w₁x₁ + w₂x₂ + b</text>')
    # petite sigmoïde
    pts = " ".join(f"{432 + i * 2:.1f},{172 - 34 / (1 + math.exp(-(i - 16) / 3.2)):.1f}" for i in range(33))
    o.append(f'<polyline points="{pts}" fill="none" stroke="{TEAL}" stroke-width="3" stroke-linecap="round"/>')
    o.append(f'<text x="464" y="198" font-size="12.5" fill="{ENCRE_PALE}" text-anchor="middle">activation</text>')
    o.append(f'<text x="464" y="214" font-size="12" fill="{TEAL}" text-anchor="middle" font-weight="700">sigmoïde σ</text>')
    o.append(f'<text x="400" y="272" font-size="12.5" fill="{TEAL}" text-anchor="middle">le neurone</text>')
    # sortie
    fleche(o, 532, 175, 596, 175)
    o.append(f'<circle cx="628" cy="175" r="26" fill="{PANNEAU}" stroke="{ROUGE}" stroke-width="2"/>')
    o.append(f'<text x="628" y="180" font-size="13" fill="{ROUGE}" text-anchor="middle" font-weight="700">0 à 1</text>')
    o.append(f'<text x="628" y="290" font-size="12.5" fill="{GRIS}" text-anchor="middle">sortie</text>')
    o.append("</svg>")
    (OUT / "neurone-schema.svg").write_text("\n".join(o) + "\n")


# ---------------------------------------------------------------- un chiffre en entrée
def chiffre_zero(n=28):
    """Un zéro manuscrit stylisé, sur une grille n × n : un anneau ovale légèrement penché."""
    grille = []
    for j in range(n):
        ligne = []
        for i in range(n):
            x, y = (i + 0.5) / n - 0.5, (j + 0.5) / n - 0.5
            xr, yr = x * math.cos(0.18) - y * math.sin(0.18), x * math.sin(0.18) + y * math.cos(0.18)
            d = abs(math.hypot(xr / 0.24, yr / 0.34) - 1.0)          # distance au trait de l'ovale
            ligne.append(max(0.0, min(1.0, 1.25 - d / 0.14)))
        grille.append(ligne)
    return grille


def chiffre():
    W, H = 700, 340
    o = entete(W, H, "Une image de chiffre en entrée d'un neurone",
               f"À gauche, une image de 28 pixels sur 28 qui montre un zéro manuscrit{NB}; chaque pixel est un nombre. "
               f"Des flèches relient les 784 pixels à un neurone, chacune avec son poids. À droite, la sortie du neurone{NB}: 0,97, "
               f"lue comme la réponse à la question «{FINE}cette image est-elle un zéro{FINE}?{FINE}».")
    o.append(f'<text x="{W / 2}" y="38" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Une image de 28 × 28 pixels{NB}: 784 entrées pour un neurone</text>')
    g, t, x0, y0 = chiffre_zero(), 7.2, 46, 72
    o.append(f'<rect x="{x0 - 3}" y="{y0 - 3}" width="{28 * t + 6}" height="{28 * t + 6}" rx="4" fill="{PANNEAU}" stroke="{AXE}"/>')
    for j, ligne in enumerate(g):
        for i, v in enumerate(ligne):
            if v > 0.02:
                o.append(f'<rect x="{x0 + i * t:.1f}" y="{y0 + j * t:.1f}" width="{t + 0.3:.1f}" height="{t + 0.3:.1f}" fill="{ENCRE}" fill-opacity="{v:.2f}"/>')
    # la grille des 28 × 28 pixels, par-dessus le chiffre
    for k in range(29):
        o.append(f'<line x1="{x0 + k * t:.1f}" y1="{y0}" x2="{x0 + k * t:.1f}" y2="{y0 + 28 * t:.1f}" stroke="{AXE}" stroke-width="0.6" opacity="0.75"/>')
        o.append(f'<line x1="{x0}" y1="{y0 + k * t:.1f}" x2="{x0 + 28 * t:.1f}" y2="{y0 + k * t:.1f}" stroke="{AXE}" stroke-width="0.6" opacity="0.75"/>')
    o.append(f'<text x="{x0 + 14 * t}" y="{y0 + 28 * t + 26}" font-size="12.5" fill="{GRIS}" text-anchor="middle">784 pixels, donc 784 nombres</text>')
    # éventail de flèches vers le neurone
    cx, cy = 480, 172
    xd = x0 + 28 * t + 12
    for k in range(9):
        y = y0 + 10 + k * (28 * t - 20) / 8
        o.append(f'<line x1="{xd}" y1="{y:.1f}" x2="{cx - 46}" y2="{cy + (y - cy) * 0.22:.1f}" stroke="{AXE}" stroke-width="1.3"/>')
    o.append(f'<text x="{(xd + cx - 46) / 2}" y="{y0 + 2}" font-size="12.5" fill="{BRUN}" text-anchor="middle" font-weight="700">784 poids</text>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="44" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="2.5"/>')
    o.append(f'<text x="{cx}" y="{cy - 2}" font-size="24" fill="{TEAL}" text-anchor="middle" font-weight="700">Σ  σ</text>')
    o.append(f'<text x="{cx}" y="{cy + 20}" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">un neurone</text>')
    fleche(o, cx + 48, cy, cx + 98, cy)
    o.append(f'<rect x="{cx + 104}" y="{cy - 30}" width="92" height="60" rx="9" fill="{PANNEAU}" stroke="{ROUGE}" stroke-width="2"/>')
    o.append(f'<text x="{cx + 150}" y="{cy + 8}" font-size="22" fill="{ROUGE}" text-anchor="middle" font-weight="700">0,97</text>')
    o.append(f'<text x="{cx + 150}" y="{cy + 54}" font-size="12.5" fill="{GRIS}" text-anchor="middle">«{FINE}est-ce un zéro{FINE}?{FINE}»</text>')
    o.append(f'<text x="{cx + 150}" y="{cy + 72}" font-size="12.5" fill="{GRIS}" text-anchor="middle">très probablement</text>')
    o.append("</svg>")
    (OUT / "chiffre-vers-neurone.svg").write_text("\n".join(o) + "\n")


schema()
chiffre()
print("neurone-schema.svg et chiffre-vers-neurone.svg écrits")


# ---------------------------------------------------------------- neurone biologique et neurone artificiel
def comparaison():
    W, H = 700, 450
    o = entete(W, H, "Un neurone biologique et un neurone artificiel",
               f"En haut, un neurone biologique{NB}: des dendrites ramifiées à gauche, un corps cellulaire au centre, un long axone vers la droite, terminé par des ramifications. "
               f"En bas, un neurone artificiel{NB}: des entrées et leurs poids à gauche, la somme et la fonction d'activation au centre, la sortie à droite. "
               f"Les mêmes couleurs relient les éléments qui se correspondent{NB}: dendrites et entrées, synapses et poids, corps cellulaire et calcul, axone et sortie.")
    o.append(f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Du neurone biologique au neurone artificiel</text>')
    # --- neurone biologique
    yb = 150
    for nom, coul in (("brun", BRUN), ("rouge", ROUGE)):
        o.append(f'<defs><marker id="p-{nom}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="13" markerHeight="13" '
                 f'markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{coul}"/></marker></defs>')
    o.append(f'<text x="{W - 30}" y="76" font-size="13" fill="{ENCRE_PALE}" font-weight="700" text-anchor="end">Neurone biologique</text>')
    cx = 250
    for dy, dx, branche in ((-52, -150, 16), (-18, -165, 12), (20, -160, -14), (52, -145, -16)):
        x1, y1 = cx - 34, yb + dy * 0.45
        x2, y2 = cx + dx, yb + dy
        o.append(f'<path d="M{x1} {y1:.0f} Q{(x1 + x2) / 2} {(y1 + y2) / 2 + branche / 2:.0f} {x2} {y2:.0f}" fill="none" stroke="{BLEU}" stroke-width="3.2" stroke-linecap="round"/>')
        for s in (-1, 1):
            o.append(f'<path d="M{x2} {y2:.0f} l-20 {s * 8}" fill="none" stroke="{BLEU}" stroke-width="2.2" stroke-linecap="round"/>')
            o.append(f'<circle cx="{x2 - 23}" cy="{y2 + s * 9:.0f}" r="3.6" fill="{BRUN}"/>')
    o.append(f'<ellipse cx="{cx}" cy="{yb}" rx="44" ry="36" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="3"/>')
    o.append(f'<circle cx="{cx - 4}" cy="{yb + 2}" r="11" fill="{TEAL}" fill-opacity="0.35"/>')
    o.append(f'<path d="M{cx + 44} {yb} C{cx + 130} {yb - 16} {cx + 210} {yb + 16} {cx + 300} {yb}" fill="none" stroke="{ROUGE}" stroke-width="4.5" stroke-linecap="round"/>')
    for dy in (-22, 0, 22):
        o.append(f'<path d="M{cx + 300} {yb} l42 {dy}" fill="none" stroke="{ROUGE}" stroke-width="2.6" stroke-linecap="round"/>')
        o.append(f'<circle cx="{cx + 346}" cy="{yb + dy}" r="4" fill="{ROUGE}"/>')
    o.append(f'<text x="92" y="{yb + 84}" font-size="12.5" fill="{BLEU}" text-anchor="middle" font-weight="700">dendrites</text>')
    o.append(f'<text x="80" y="{yb - 76}" font-size="12.5" fill="{BRUN}" text-anchor="middle" font-weight="700">synapses</text>')
    o.append(f'<text x="{cx}" y="{yb + 62}" font-size="12.5" fill="{TEAL}" text-anchor="middle" font-weight="700">corps cellulaire</text>')
    o.append(f'<text x="{cx + 190}" y="{yb + 34}" font-size="12.5" fill="{ROUGE}" text-anchor="middle" font-weight="700">axone</text>')
    o.append(f'<line x1="30" y1="{yb + 100}" x2="{W - 30}" y2="{yb + 100}" stroke="{AXE}" stroke-width="1" stroke-dasharray="5 5"/>')
    # --- neurone artificiel
    ya = 340
    o.append(f'<text x="{W - 30}" y="{ya - 62}" font-size="13" fill="{ENCRE_PALE}" font-weight="700" text-anchor="end">Neurone artificiel</text>')
    for dy in (-46, 0, 46):
        o.append(f'<circle cx="92" cy="{ya + dy * 0.9:.0f}" r="13" fill="{PANNEAU}" stroke="{BLEU}" stroke-width="2"/>')
        o.append(f'<line x1="106" y1="{ya + dy * 0.9:.0f}" x2="{cx - 48}" y2="{ya + dy * 0.25:.0f}" stroke="{BRUN}" stroke-width="2.4" marker-end="url(#p-brun)"/>')
    o.append(f'<ellipse cx="{cx}" cy="{ya}" rx="44" ry="36" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="3"/>')
    o.append(f'<text x="{cx}" y="{ya + 8}" font-size="22" fill="{TEAL}" text-anchor="middle" font-weight="700">Σ  σ</text>')
    o.append(f'<line x1="{cx + 46}" y1="{ya}" x2="{cx + 296}" y2="{ya}" stroke="{ROUGE}" stroke-width="3.2" marker-end="url(#p-rouge)"/>')
    o.append(f'<text x="92" y="{ya + 74}" font-size="12.5" fill="{BLEU}" text-anchor="middle" font-weight="700">entrées</text>')
    o.append(f'<text x="158" y="{ya - 40}" font-size="12.5" fill="{BRUN}" text-anchor="middle" font-weight="700">poids</text>')
    o.append(f'<text x="{cx}" y="{ya + 62}" font-size="12.5" fill="{TEAL}" text-anchor="middle" font-weight="700">somme et activation</text>')
    o.append(f'<text x="{cx + 190}" y="{ya + 26}" font-size="12.5" fill="{ROUGE}" text-anchor="middle" font-weight="700">sortie</text>')
    o.append("</svg>")
    (OUT / "neurone-biologique-artificiel.svg").write_text("\n".join(o) + "\n")


comparaison()
print("neurone-biologique-artificiel.svg écrit")
