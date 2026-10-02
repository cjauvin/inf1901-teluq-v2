"""Module 3, « Voir : les réseaux convolutifs » : le chiffre déplacé, et l'architecture d'un réseau convolutif."""
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
            f'<defs><marker id="pointe" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" '
            f'markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
            f'<rect x="0" y="0" width="{w}" height="{h}" rx="14" fill="{FOND}" stroke="{BORD}"/>']


def ecrire(nom, o):
    o.append("</svg>")
    (OUT / nom).write_text("\n".join(o) + "\n")


# ---------------------------------------------------------------- le chiffre déplacé
def un(col):
    """Les cases d'un « 1 » simplifié sur une grille de 10 × 10 : une barre verticale et un petit crochet."""
    return {(col, j) for j in range(2, 8)} | {(col - 1, 3)}


def decalage():
    W, H = 700, 420
    o = entete(W, H, "Un chiffre et le même chiffre décalé, vus comme des listes de pixels",
               f"En haut, deux grilles de 10 pixels sur 10. La première montre un «{FINE}1{FINE}» à gauche, la seconde le même «{FINE}1{FINE}» décalé de trois "
               f"pixels vers la droite. En bas, chaque grille est mise à plat en une liste de 100 pixels, rangée après rangée. Les pixels allumés n'occupent pas "
               "les mêmes places dans les deux listes.")
    o.append(f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Le même chiffre, à deux positions</text>')
    c = 14
    for k, (x0, col, titre) in enumerate(((160, 3, "un chiffre"), (400, 6, "le même chiffre, décalé"))):
        actifs = un(col)
        o.append(f'<text x="{x0 + 5 * c}" y="68" font-size="12.5" fill="{ENCRE_PALE}" text-anchor="middle" font-weight="700">{titre}</text>')
        for j in range(10):
            for i in range(10):
                o.append(f'<rect x="{x0 + i * c}" y="{80 + j * c}" width="{c}" height="{c}" fill="{ENCRE if (i, j) in actifs else PANNEAU}" '
                         f'stroke="{AXE}" stroke-width="0.6"/>')
        # la liste à plat
        yl, cl, xl = 290 + k * 50, 5.5, 75
        o.append(f'<text x="{xl - 8}" y="{yl + 11}" font-size="12" fill="{ENCRE_PALE}" text-anchor="end">{k + 1}</text>')
        for n in range(100):
            i, j = n % 10, n // 10
            o.append(f'<rect x="{xl + n * cl:.1f}" y="{yl}" width="{cl:.1f}" height="16" fill="{ENCRE if (i, j) in actifs else PANNEAU}" stroke="{AXE}" stroke-width="0.4"/>')
    o.append(f'<text x="{W / 2}" y="274" font-size="12.5" fill="{ENCRE_PALE}" text-anchor="middle" font-weight="700">les mêmes images, vues comme des listes de 100 pixels</text>')
    o.append(f'<text x="{W / 2}" y="{H - 22}" font-size="12.5" fill="{GRIS}" text-anchor="middle">Pour un réseau ordinaire, les deux listes n\'ont presque rien en commun.</text>')
    ecrire("chiffre-decale.svg", o)


# ---------------------------------------------------------------- l'architecture convolutive
def chiffre_zero(n=28):
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


def pile(o, x, cy, cote, n, coul):
    """Une pile de n images carrées, légèrement décalées ; renvoie les bornes horizontales de la pile."""
    pas = 5
    for k in range(n):
        dx, dy = k * pas, -k * pas
        x0, y0 = x + dx, cy - cote / 2 + dy + (n - 1) * pas / 2
        o.append(f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{cote}" height="{cote}" rx="2" fill="{PANNEAU}" stroke="{coul}" stroke-width="1.6"/>')
    return x, x + cote + (n - 1) * pas


def architecture():
    W, H = 700, 360
    o = entete(W, H, "L'architecture d'un réseau convolutif",
               f"De gauche à droite{NB}: l'image d'un chiffre{FINE}; une couche convolutive, représentée par une pile d'images de même taille{FINE}; une réduction, "
               f"qui donne une pile d'images plus petites{FINE}; une seconde couche convolutive et une seconde réduction{FINE}; puis un réseau ordinaire et les dix sorties.")
    o.append(f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Un réseau convolutif, de l\'image à la réponse</text>')
    cy = 180
    # l'image
    g, t, x0 = chiffre_zero(), 2.6, 22
    y0 = cy - 14 * t
    o.append(f'<rect x="{x0 - 2}" y="{y0 - 2}" width="{28 * t + 4:.1f}" height="{28 * t + 4:.1f}" rx="3" fill="{PANNEAU}" stroke="{AXE}"/>')
    for j, ligne in enumerate(g):
        for i, v in enumerate(ligne):
            if v > 0.03:
                o.append(f'<rect x="{x0 + i * t:.1f}" y="{y0 + j * t:.1f}" width="{t + 0.2:.1f}" height="{t + 0.2:.1f}" fill="{ENCRE}" fill-opacity="{v:.2f}"/>')
    blocs = [(x0, x0 + 28 * t, "image", "")]
    x = x0 + 28 * t + 30
    for cote, n, coul, nom, sous in ((66, 6, TEAL, "convolution", "6 filtres"), (36, 6, BRUN, "réduction", ""),
                                     (32, 10, TEAL, "convolution", "10 filtres"), (18, 10, BRUN, "réduction", "")):
        a, b = pile(o, x, cy, cote, n, coul)
        blocs.append((a, b, nom, sous))
        x = b + 30
    # le réseau ordinaire
    xd = x + 10
    ys = [cy + (k - 3.5) * 22 for k in range(8)]
    xs = xd + 70
    yo = [cy + (k - 4.5) * 21 for k in range(10)]
    for y1 in ys:
        for y2 in yo:
            o.append(f'<line x1="{xd}" y1="{y1:.1f}" x2="{xs}" y2="{y2:.1f}" stroke="{AXE}" stroke-width="0.6" opacity="0.8"/>')
    for y in ys:
        o.append(f'<circle cx="{xd}" cy="{y:.1f}" r="6" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="1.8"/>')
    for k, y in enumerate(yo):
        o.append(f'<circle cx="{xs}" cy="{y:.1f}" r="8" fill="{ROUGE if k == 0 else PANNEAU}" stroke="{ROUGE}" stroke-width="1.8"/>')
        o.append(f'<text x="{xs}" y="{y + 3.5:.1f}" font-size="9.5" fill="{PANNEAU if k == 0 else ROUGE}" text-anchor="middle" font-weight="700">{k}</text>')
    blocs.append((xd - 6, xd + 6, "réseau", "ordinaire"))
    blocs.append((xs - 8, xs + 8, "sorties", ""))
    # flèches entre les blocs
    for (a1, b1, *_), (a2, b2, *_) in zip(blocs, blocs[1:-1]):
        o.append(f'<line x1="{b1 + 5:.1f}" y1="{cy}" x2="{a2 - 6:.1f}" y2="{cy}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#pointe)"/>')
    for a, b, nom, sous in blocs:
        xm = (a + b) / 2
        o.append(f'<text x="{xm:.1f}" y="{cy + 118}" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle" font-weight="700">{nom}</text>')
        if sous:
            o.append(f'<text x="{xm:.1f}" y="{cy + 134}" font-size="11.5" fill="{GRIS}" text-anchor="middle">{sous}</text>')
    o.append(f'<text x="{W / 2}" y="{H - 16}" font-size="12.5" fill="{GRIS}" text-anchor="middle">Chaque convolution produit une image par filtre{FINE}; chaque réduction divise la taille des images par deux.</text>')
    ecrire("architecture-convolutive.svg", o)


decalage()
architecture()
print("chiffre-decale.svg et architecture-convolutive.svg écrits")
