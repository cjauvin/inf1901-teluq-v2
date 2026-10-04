"""Module 3, « Une couche cachée » : le petit réseau qui résout le XOR, et ce que fait sa couche cachée."""
import math
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module3"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, GRILLE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#e8dfc9", "#fbf7ee")
NB, FINE = " ", " "
POLICE = 'font-family="system-ui, -apple-system, sans-serif"'


def entete(w, h, titre, desc):
    return ['<?xml version="1.0" encoding="UTF-8"?>',
            f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" {POLICE}>',
            f"<title>{titre}</title>", f"<desc>{desc}</desc>",
            f'<defs><marker id="pointe" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="11" markerHeight="11" '
            f'markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
            f'<rect x="0" y="0" width="{w}" height="{h}" rx="14" fill="{FOND}" stroke="{BORD}"/>']


# ---------------------------------------------------------------- le réseau 2-2-1
def reseau():
    W, H = 700, 350
    o = entete(W, H, "Un réseau de trois neurones qui résout le XOR",
               f"Trois colonnes. À gauche, la couche d'entrée{NB}: A et B. Au centre, la couche cachée{NB}: le neurone 1, qui répond à la question "
               f"«{FINE}au moins une{FINE}?{FINE}», et le neurone 2, qui répond à «{FINE}les deux{FINE}?{FINE}». À droite, la couche de sortie{NB}: "
               "un neurone qui donne A XOR B. Chaque entrée est reliée aux deux neurones cachés, et chaque neurone caché au neurone de sortie.")
    o.append(f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Le plus petit réseau qui résout le XOR</text>')
    xe, xc, xs = 110, 350, 590
    ye, yc, ys = (120, 230), (120, 230), 175
    # connexions
    for y1 in ye:
        for y2 in yc:
            o.append(f'<line x1="{xe + 30}" y1="{y1}" x2="{xc - 58}" y2="{y2}" stroke="{GRIS}" stroke-width="1.8" marker-end="url(#pointe)"/>')
    for y1 in yc:
        o.append(f'<line x1="{xc + 58}" y1="{y1}" x2="{xs - 50}" y2="{ys + (y1 - ys) * 0.15:.0f}" stroke="{GRIS}" stroke-width="1.8" marker-end="url(#pointe)"/>')
    # entrées
    for y, nom in zip(ye, "AB"):
        o.append(f'<circle cx="{xe}" cy="{y}" r="28" fill="{PANNEAU}" stroke="{BLEU}" stroke-width="2"/>')
        o.append(f'<text x="{xe}" y="{y + 7}" font-size="20" fill="{BLEU}" text-anchor="middle" font-weight="700">{nom}</text>')
    # neurones cachés
    for y, nom, question in zip(yc, ("neurone 1", "neurone 2"), (f"au moins une{FINE}?", f"les deux{FINE}?")):
        o.append(f'<rect x="{xc - 56}" y="{y - 32}" width="112" height="64" rx="32" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="2.5"/>')
        o.append(f'<text x="{xc}" y="{y - 4}" font-size="12.5" fill="{TEAL}" text-anchor="middle" font-weight="700">{nom}</text>')
        o.append(f'<text x="{xc}" y="{y + 14}" font-size="12.5" fill="{ENCRE}" text-anchor="middle">{question}</text>')
    # sortie
    o.append(f'<rect x="{xs - 48}" y="{ys - 32}" width="96" height="64" rx="32" fill="{PANNEAU}" stroke="{ROUGE}" stroke-width="2.5"/>')
    o.append(f'<text x="{xs}" y="{ys - 4}" font-size="12.5" fill="{ROUGE}" text-anchor="middle" font-weight="700">sortie</text>')
    o.append(f'<text x="{xs}" y="{ys + 14}" font-size="12.5" fill="{ENCRE}" text-anchor="middle">A XOR B</text>')
    # noms des couches
    for x, t in ((xe, "couche d'entrée"), (xc, "couche cachée"), (xs, "couche de sortie")):
        o.append(f'<text x="{x}" y="72" font-size="12.5" fill="{ENCRE_PALE}" text-anchor="middle" font-weight="700">{t}</text>')
    o.append(f'<text x="{W / 2}" y="{H - 30}" font-size="12.5" fill="{GRIS}" text-anchor="middle">Chaque flèche porte un poids. Chaque neurone a aussi son biais.</text>')
    o.append("</svg>")
    (OUT / "reseau-xor.svg").write_text("\n".join(o) + "\n")


# ---------------------------------------------------------------- avant / après la couche cachée
def panneau(o, ox, titre, sous_titre, axe_x, axe_y):
    Wp, Hp = 300, 312
    o.append(f'<rect x="{ox}" y="58" width="{Wp}" height="{Hp}" rx="10" fill="{PANNEAU}" stroke="{AXE}" stroke-width="1.2"/>')
    o.append(f'<text x="{ox + Wp / 2}" y="82" font-size="14" fill="{ENCRE}" text-anchor="middle" font-weight="700">{titre}</text>')
    o.append(f'<text x="{ox + Wp / 2}" y="100" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle">{sous_titre}</text>')
    gx0, gy0, cote = ox + 78, 292, 150            # (0,0) du repère, et longueur d'une unité
    X = lambda v: gx0 + v * cote
    Y = lambda v: gy0 - v * cote
    for v in (0, 1):
        o.append(f'<line x1="{X(v)}" y1="{Y(-0.2)}" x2="{X(v)}" y2="{Y(1.2)}" stroke="{GRILLE}" stroke-width="1"/>')
        o.append(f'<line x1="{X(-0.2)}" y1="{Y(v)}" x2="{X(1.2)}" y2="{Y(v)}" stroke="{GRILLE}" stroke-width="1"/>')
        o.append(f'<text x="{X(v)}" y="{Y(-0.2) + 16}" font-size="11.5" fill="{GRIS}" text-anchor="middle">{v}</text>')
        o.append(f'<text x="{X(-0.2) - 8}" y="{Y(v) + 4}" font-size="11.5" fill="{GRIS}" text-anchor="end">{v}</text>')
    o.append(f'<text x="{X(0.5)}" y="{Y(-0.2) + 32}" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle">{axe_x}</text>')
    o.append(f'<text x="{ox + 22}" y="{Y(0.5)}" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle" transform="rotate(-90 {ox + 22} {Y(0.5)})">{axe_y}</text>')
    return X, Y


def point(o, x, y, vrai, r=9):
    o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{ROUGE if vrai else BLEU}" stroke="{PANNEAU}" stroke-width="2"/>')


def avant_apres():
    W, H = 700, 430
    o = entete(W, H, "Le XOR avant et après la couche cachée",
               f"Deux panneaux. À gauche, le plan des entrées A et B{NB}: les deux cas «{FINE}faux{FINE}», en bleu, sont aux coins (0, 0) et (1, 1){FINE}; "
               f"les deux cas «{FINE}vrai{FINE}», en rouge, aux coins (0, 1) et (1, 0). Deux droites parallèles, une par neurone caché, délimitent une bande "
               f"qui contient les deux points rouges. À droite, l'espace de la couche cachée, avec la réponse du neurone 1 à l'horizontale et celle du neurone 2 "
               f"à la verticale{NB}: les deux cas rouges sont au même point (1, 0), les cas bleus en (0, 0) et (1, 1), et une seule droite sépare le rouge du bleu.")
    o.append(f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">La couche cachée change le point de vue</text>')
    # --- gauche : le plan des entrées
    X, Y = panneau(o, 30, "Dans le plan des entrées", "deux droites délimitent une bande", "entrée A", "entrée B")
    bande = f"{X(-0.2)},{Y(0.7)} {X(0.7)},{Y(-0.2)} {X(1.2)},{Y(-0.2)} {X(1.2)},{Y(0.3)} {X(0.3)},{Y(1.2)} {X(-0.2)},{Y(1.2)}"
    o.append(f'<polygon points="{bande}" fill="{ROUGE}" fill-opacity="0.10"/>')
    for c, nom, dx in ((0.5, "neurone 1", -6), (1.5, "neurone 2", 6)):
        o.append(f'<line x1="{X(c + 0.2 if c < 1 else 1.2)}" y1="{Y(-0.2 if c < 1 else c - 1.2)}" x2="{X(-0.2 if c < 1 else c - 1.2)}" y2="{Y(c + 0.2 if c < 1 else 1.2)}" stroke="{TEAL}" stroke-width="2.6"/>')
    o.append(f'<text x="{X(0.02)}" y="{Y(0.20)}" font-size="11.5" fill="{TEAL}" font-weight="700" text-anchor="start" transform="rotate(45 {X(0.02)} {Y(0.20)})">neurone 1</text>')
    o.append(f'<text x="{X(0.70)}" y="{Y(1.02)}" font-size="11.5" fill="{TEAL}" font-weight="700" text-anchor="start" transform="rotate(45 {X(0.70)} {Y(1.02)})">neurone 2</text>')
    for a, b in ((0, 0), (1, 1), (0, 1), (1, 0)):
        point(o, X(a), Y(b), a != b)
    # --- droite : l'espace de la couche cachée
    X, Y = panneau(o, 370, "Dans l'espace de la couche cachée", "une seule droite suffit", f"neurone 1{NB}: au moins une{FINE}?", f"neurone 2{NB}: les deux{FINE}?")
    o.append(f'<polygon points="{X(0.5)},{Y(0)} {X(1.2)},{Y(0.7)} {X(1.2)},{Y(-0.2)} {X(0.3)},{Y(-0.2)}" fill="{ROUGE}" fill-opacity="0.10"/>')
    o.append(f'<line x1="{X(0.3)}" y1="{Y(-0.2)}" x2="{X(1.2)}" y2="{Y(0.7)}" stroke="{BRUN}" stroke-width="2.6"/>')
    o.append(f'<text x="{X(0.52)}" y="{Y(0.16)}" font-size="11.5" fill="{BRUN}" font-weight="700" text-anchor="start" transform="rotate(-45 {X(0.52)} {Y(0.16)})">neurone de sortie</text>')
    point(o, X(0), Y(0), False)
    point(o, X(1), Y(1), False)
    point(o, X(1) - 7, Y(0) - 5, True)
    point(o, X(1) + 7, Y(0) + 5, True)
    o.append(f'<text x="{X(0.97)}" y="{Y(0) + 27}" font-size="11.5" fill="{ROUGE}" font-weight="700" text-anchor="middle">les deux cas «{FINE}vrai{FINE}»</text>')
    # légende
    y = H - 28
    o.append(f'<circle cx="230" cy="{y - 4}" r="7" fill="{ROUGE}"/><text x="244" y="{y}" font-size="12.5" fill="{ENCRE_PALE}">XOR vrai (1)</text>')
    o.append(f'<circle cx="380" cy="{y - 4}" r="7" fill="{BLEU}"/><text x="394" y="{y}" font-size="12.5" fill="{ENCRE_PALE}">XOR faux (0)</text>')
    o.append("</svg>")
    (OUT / "xor-couche-cachee.svg").write_text("\n".join(o) + "\n")


# ---------------------------------------------------------------- le réseau des chiffres
def chiffre_zero(n=28):
    """Un zéro manuscrit stylisé, sur une grille n × n (le même que dans gen_neurone.py)."""
    grille = []
    for j in range(n):
        ligne = []
        for i in range(n):
            x, y = (i + 0.5) / n - 0.5, (j + 0.5) / n - 0.5
            xr, yr = x * math.cos(0.18) - y * math.sin(0.18), x * math.sin(0.18) + y * math.cos(0.18)
            d = abs(math.hypot(xr / 0.24, yr / 0.34) - 1.0)
            ligne.append(max(0.0, min(1.0, 1.25 - d / 0.14)))
        grille.append(ligne)
    return grille


def reseau_chiffres():
    W, H = 700, 440
    o = entete(W, H, "Un réseau qui reconnaît les chiffres manuscrits",
               f"De gauche à droite{NB}: une image de 28 pixels sur 28 qui montre un zéro{FINE}; une couche d'entrée de 784 valeurs, une par pixel{FINE}; "
               f"une couche cachée de 30 neurones{FINE}; une couche de sortie de dix neurones, numérotés de 0 à 9. Chaque sortie donne un nombre entre 0 et 1. "
               f"La sortie du chiffre 0 est la plus élevée, 0,96{NB}: c'est la réponse du réseau.")
    o.append(f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Le réseau des chiffres{NB}: 784 entrées, une couche cachée, dix sorties</text>')
    haut, bas = 100, 370
    cy = (haut + bas) / 2
    # l'image
    g, t, x0 = chiffre_zero(), 4.0, 26
    y0 = cy - 14 * t
    o.append(f'<rect x="{x0 - 3}" y="{y0 - 3}" width="{28 * t + 6}" height="{28 * t + 6}" rx="4" fill="{PANNEAU}" stroke="{AXE}"/>')
    for j, ligne in enumerate(g):
        for i, v in enumerate(ligne):
            if v > 0.02:
                o.append(f'<rect x="{x0 + i * t:.1f}" y="{y0 + j * t:.1f}" width="{t + 0.3:.1f}" height="{t + 0.3:.1f}" fill="{ENCRE}" fill-opacity="{v:.2f}"/>')
    o.append(f'<text x="{x0 + 14 * t}" y="{y0 + 28 * t + 24}" font-size="12" fill="{GRIS}" text-anchor="middle">image de 28 × 28</text>')
    xe, xc, xs = 215, 380, 545

    def colonne(n, trou):
        """Ordonnées de n ronds répartis de haut en bas ; `trou` est l'indice remplacé par des points de suspension."""
        return [(haut + k * (bas - haut) / (n - 1), k == trou) for k in range(n)]

    entrees, caches = colonne(11, 5), colonne(9, 4)
    sorties = [haut + k * (bas - haut) / 9 for k in range(10)]
    # connexions (dessinées d'abord, pour passer sous les ronds)
    for y1, t1 in entrees:
        for y2, t2 in caches:
            if not t1 and not t2:
                o.append(f'<line x1="{xe + 7}" y1="{y1:.1f}" x2="{xc - 11}" y2="{y2:.1f}" stroke="{AXE}" stroke-width="0.7" opacity="0.8"/>')
    for y1, t1 in caches:
        for y2 in sorties:
            if not t1:
                o.append(f'<line x1="{xc + 11}" y1="{y1:.1f}" x2="{xs - 11}" y2="{y2:.1f}" stroke="{AXE}" stroke-width="0.7" opacity="0.8"/>')
    o.append(f'<line x1="{x0 + 28 * t + 10}" y1="{cy}" x2="{xe - 22}" y2="{cy}" stroke="{GRIS}" stroke-width="1.8" marker-end="url(#pointe)"/>')
    for y, trou in entrees:
        if trou:
            o.append(f'<text x="{xe}" y="{y + 5:.1f}" font-size="16" fill="{BLEU}" text-anchor="middle" font-weight="700">⋮</text>')
        else:
            o.append(f'<circle cx="{xe}" cy="{y:.1f}" r="6" fill="{PANNEAU}" stroke="{BLEU}" stroke-width="1.8"/>')
    for y, trou in caches:
        if trou:
            o.append(f'<text x="{xc}" y="{y + 6:.1f}" font-size="18" fill="{TEAL}" text-anchor="middle" font-weight="700">⋮</text>')
        else:
            o.append(f'<circle cx="{xc}" cy="{y:.1f}" r="10" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="2.2"/>')
    valeurs = [0.96, 0.00, 0.01, 0.00, 0.00, 0.01, 0.01, 0.00, 0.01, 0.00]     # elles totalisent 1
    for k, (y, v) in enumerate(zip(sorties, valeurs)):
        gagne = k == 0
        o.append(f'<circle cx="{xs}" cy="{y:.1f}" r="10" fill="{ROUGE if gagne else PANNEAU}" fill-opacity="{0.85 if gagne else 1}" stroke="{ROUGE}" stroke-width="2.2"/>')
        o.append(f'<text x="{xs}" y="{y + 4:.1f}" font-size="11.5" fill="{PANNEAU if gagne else ROUGE}" text-anchor="middle" font-weight="700">{k}</text>')
        o.append(f'<rect x="{xs + 22}" y="{y - 5:.1f}" width="60" height="10" rx="2" fill="{PANNEAU}" stroke="{AXE}" stroke-width="0.8"/>')
        o.append(f'<rect x="{xs + 22}" y="{y - 5:.1f}" width="{60 * v:.1f}" height="10" rx="2" fill="{ROUGE}" fill-opacity="{0.9 if gagne else 0.45}"/>')
        o.append(f'<text x="{xs + 90}" y="{y + 4:.1f}" font-size="11.5" fill="{ENCRE if gagne else GRIS}" font-weight="{700 if gagne else 400}">{f"{v:.2f}".replace(".", ",")}</text>')
    for x, titre, sous, coul in ((xe, "couche d'entrée", "784 valeurs", BLEU), (xc, "couche cachée", "30 neurones", TEAL), (xs + 30, "couche de sortie", "10 neurones", ROUGE)):
        o.append(f'<text x="{x}" y="66" font-size="12.5" fill="{ENCRE_PALE}" text-anchor="middle" font-weight="700">{titre}</text>')
        o.append(f'<text x="{x}" y="82" font-size="12" fill="{coul}" text-anchor="middle">{sous}</text>')
    o.append(f'<text x="{W / 2}" y="{H - 26}" font-size="12.5" fill="{GRIS}" text-anchor="middle">La sortie la plus élevée donne la réponse du réseau{NB}: ici, le chiffre 0.</text>')
    o.append("</svg>")
    (OUT / "reseau-chiffres.svg").write_text("\n".join(o) + "\n")


reseau()
avant_apres()
reseau_chiffres()
print("reseau-xor.svg, xor-couche-cachee.svg et reseau-chiffres.svg écrits")
