"""Module 3, « Une couche cachée » : le petit réseau qui résout le XOR, et ce que fait sa couche cachée."""
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


reseau()
avant_apres()
print("reseau-xor.svg et xor-couche-cachee.svg écrits")
