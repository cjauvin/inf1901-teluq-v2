"""Module 3, « L'attention et le Transformer » : grille d'attention, bloc et pile du Transformer, Vision Transformer."""
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


def grille_traduction():
    W, H = 700, 410
    anglais = ["the", "European", "Economic", "Area"]
    francais = ["la", "zone", "économique", "européenne"]
    poids = [[0.85, 0.05, 0.04, 0.06],
             [0.05, 0.05, 0.10, 0.80],
             [0.02, 0.18, 0.75, 0.05],
             [0.02, 0.78, 0.15, 0.05]]
    o = entete(W, H, "La grille d'attention d'une traduction",
               f"Une grille de quatre colonnes et quatre lignes. Les colonnes portent les mots anglais «{FINE}the European Economic Area{FINE}», les lignes les mots "
               f"français «{FINE}la zone économique européenne{FINE}». Chaque case est d'autant plus foncée que le décodeur regarde ce mot anglais en écrivant ce mot "
               f"français. «{FINE}la{FINE}» regarde «{FINE}the{FINE}», «{FINE}zone{FINE}» regarde «{FINE}Area{FINE}», «{FINE}économique{FINE}» regarde "
               f"«{FINE}Economic{FINE}» et «{FINE}européenne{FINE}» regarde «{FINE}European{FINE}»{NB}: les deux dernières cases foncées se croisent.")
    o.append(f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Où regarde le décodeur, pour chaque mot qu\'il écrit{NB}?</text>')
    c, x0, y0 = 62, 300, 116
    for j, mot in enumerate(anglais):
        o.append(f'<text x="{x0 + j * c + c / 2}" y="{y0 - 12}" font-size="13" fill="{BLEU}" text-anchor="middle" font-weight="700">{mot}</text>')
    o.append(f'<text x="{x0 + 2 * c}" y="{y0 - 38}" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle">phrase d\'origine (anglais)</text>')
    for i, mot in enumerate(francais):
        o.append(f'<text x="{x0 - 14}" y="{y0 + i * c + c / 2 + 5}" font-size="13" fill="{ROUGE}" text-anchor="end" font-weight="700">{mot}</text>')
        for j in range(4):
            v = poids[i][j]
            o.append(f'<rect x="{x0 + j * c}" y="{y0 + i * c}" width="{c}" height="{c}" fill="{ENCRE}" fill-opacity="{0.05 + 0.85 * v:.2f}" stroke="{PANNEAU}" stroke-width="2"/>')
            o.append(f'<text x="{x0 + j * c + c / 2}" y="{y0 + i * c + c / 2 + 4}" font-size="11.5" fill="{PANNEAU if v > 0.4 else ENCRE_PALE}" text-anchor="middle">{f"{v:.2f}".replace(".", ",")}</text>')
    o.append(f'<text x="{x0 - 14}" y="{y0 - 12}" font-size="12" fill="{ENCRE_PALE}" text-anchor="end">traduction (français)</text>')
    o.append(f'<text x="{W / 2}" y="{H - 16}" font-size="12.5" fill="{GRIS}" text-anchor="middle">Chaque ligne donne les poids de l\'attention pour un mot écrit{NB}; ils totalisent 1.</text>')
    ecrire("attention-traduction.svg", o)



def bloc(o, x, y, l, h, petit=False):
    """Un bloc de Transformer : l'auto-attention en bas, le petit réseau en haut."""
    o.append(f'<rect x="{x}" y="{y}" width="{l}" height="{h}" rx="10" fill="{PANNEAU}" stroke="{ENCRE_PALE}" stroke-width="1.8"/>')
    if petit:
        return
    m = 12
    hh = (h - 3 * m) / 2
    o.append(f'<rect x="{x + m}" y="{y + m}" width="{l - 2 * m}" height="{hh}" rx="8" fill="{TEAL}" fill-opacity="0.12" stroke="{TEAL}" stroke-width="1.8"/>')
    o.append(f'<text x="{x + l / 2}" y="{y + m + hh / 2 - 2}" font-size="12.5" fill="{TEAL}" text-anchor="middle" font-weight="700">petit réseau</text>')
    o.append(f'<text x="{x + l / 2}" y="{y + m + hh / 2 + 14}" font-size="11.5" fill="{TEAL}" text-anchor="middle">appliqué à chaque mot</text>')
    y2 = y + 2 * m + hh
    o.append(f'<rect x="{x + m}" y="{y2}" width="{l - 2 * m}" height="{hh}" rx="8" fill="{ROUGE}" fill-opacity="0.10" stroke="{ROUGE}" stroke-width="1.8"/>')
    o.append(f'<text x="{x + l / 2}" y="{y2 + hh / 2 - 2}" font-size="12.5" fill="{ROUGE}" text-anchor="middle" font-weight="700">auto-attention</text>')
    o.append(f'<text x="{x + l / 2}" y="{y2 + hh / 2 + 14}" font-size="11.5" fill="{ROUGE}" text-anchor="middle">chaque mot regarde les autres</text>')


def mots(o, x0, pas, y, liste, coul):
    for k, m in enumerate(liste):
        x = x0 + k * pas
        o.append(f'<rect x="{x - 26}" y="{y - 13}" width="52" height="26" rx="6" fill="{PANNEAU}" stroke="{coul}" stroke-width="1.6"/>')
        o.append(f'<text x="{x}" y="{y + 4}" font-size="11.5" fill="{coul}" text-anchor="middle" font-weight="700">{m}</text>')


def transformer():
    W, H = 700, 420
    o = entete(W, H, "Un bloc de Transformer, et une pile de blocs",
               f"Deux panneaux. À gauche, un bloc{NB}: les mots entrent par le bas, passent par une couche d'auto-attention, où chaque mot regarde les autres, "
               f"puis par un petit réseau appliqué à chaque mot, et ressortent enrichis par le haut. À droite, une pile de six blocs identiques{NB}: les mots "
               "entrent en bas et ressortent en haut, enrichis de leur contexte.")
    o.append(f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Le Transformer{NB}: des blocs identiques, empilés</text>')
    for ox, wp, titre in ((22, 330, "un bloc"), (370, 308, "une pile de blocs")):
        o.append(f'<rect x="{ox}" y="56" width="{wp}" height="330" rx="10" fill="{FOND}" stroke="{AXE}" stroke-width="1.2"/>')
        o.append(f'<text x="{ox + wp / 2}" y="80" font-size="14" fill="{ENCRE}" text-anchor="middle" font-weight="700">{titre}</text>')
    liste = ["le", "chien", "dort"]
    # le bloc
    mots(o, 107, 80, 356, liste, BLEU)
    for k in range(3):
        o.append(f'<line x1="{107 + k * 80}" y1="341" x2="{107 + k * 80}" y2="{316}" stroke="{GRIS}" stroke-width="1.5" marker-end="url(#pointe)"/>')
    bloc(o, 52, 150, 270, 162)
    for k in range(3):
        o.append(f'<line x1="{107 + k * 80}" y1="148" x2="{107 + k * 80}" y2="{124}" stroke="{GRIS}" stroke-width="1.5" marker-end="url(#pointe)"/>')
    mots(o, 107, 80, 108, liste, ROUGE)
    # la pile
    xp, lp = 396, 180
    mots(o, xp + 20, 70, 356, liste, BLEU)
    hb, e = 26, 8
    for k in range(6):
        y = 326 - (k + 1) * hb - k * e
        bloc(o, xp, y, lp, hb, petit=True)
        o.append(f'<text x="{xp + lp / 2}" y="{y + 17}" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">bloc {k + 1}</text>')
        if k < 5:
            o.append(f'<line x1="{xp + lp / 2}" y1="{y - 1}" x2="{xp + lp / 2}" y2="{y - e + 1}" stroke="{GRIS}" stroke-width="1.4"/>')
    o.append(f'<line x1="{xp + lp / 2}" y1="341" x2="{xp + lp / 2}" y2="{328}" stroke="{GRIS}" stroke-width="1.5" marker-end="url(#pointe)"/>')
    ytop = 326 - 6 * hb - 5 * e
    o.append(f'<line x1="{xp + lp / 2}" y1="{ytop - 1}" x2="{xp + lp / 2}" y2="{ytop - 14}" stroke="{GRIS}" stroke-width="1.5" marker-end="url(#pointe)"/>')
    mots(o, xp + 20, 70, ytop - 30, liste, ROUGE)
    o.append(f'<text x="{xp + lp + 10}" y="{ytop + 40}" font-size="11.5" fill="{GRIS}">6 en 2017</text>')
    o.append(f'<text x="{xp + lp + 10}" y="{ytop + 56}" font-size="11.5" fill="{GRIS}">≈ 100</text>')
    o.append(f'<text x="{xp + lp + 10}" y="{ytop + 72}" font-size="11.5" fill="{GRIS}">aujourd\'hui</text>')
    o.append(f'<text x="{W / 2}" y="{H - 14}" font-size="12.5" fill="{GRIS}" text-anchor="middle">En bas, les mots seuls{NB}; en haut, les mots enrichis de leur contexte.</text>')
    ecrire("transformer-blocs.svg", o)


def paysage(x, y):
    """Une petite image de synthèse : ciel, soleil, collines. Coordonnées entre 0 et 1."""
    if math.hypot(x - 0.72, y - 0.28) < 0.13:
        return "#e2b33c"
    colline = 0.62 + 0.10 * math.sin(6 * x) - 0.08 * math.cos(11 * x + 1)
    if y > colline:
        return "#5f8f4e" if y < colline + 0.12 else "#4a7a3d"
    return "#9cc3de" if y < 0.45 else "#b9d5e6"


def image_pixels(o, x0, y0, taille, n, x_a=0, y_a=0, x_b=1, y_b=1):
    t = taille / n
    for j in range(n):
        for i in range(n):
            u, v = x_a + (i + 0.5) / n * (x_b - x_a), y_a + (j + 0.5) / n * (y_b - y_a)
            o.append(f'<rect x="{x0 + i * t:.2f}" y="{y0 + j * t:.2f}" width="{t + 0.15:.2f}" height="{t + 0.15:.2f}" fill="{paysage(u, v)}"/>')


def vision():
    W, H = 700, 400
    o = entete(W, H, "Une image découpée en carrés pour un Transformer",
               f"En haut, une petite image de paysage, avec un ciel, un soleil et des collines, découpée par une grille en seize carrés. En bas, ces seize carrés "
               "sont alignés l'un après l'autre, numérotés de 1 à 16, comme les mots d'une phrase, et entrent dans un Transformer.")
    o.append(f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Une image traitée comme une phrase</text>')
    n, taille, x0, y0 = 4, 176, 262, 58
    image_pixels(o, x0, y0, taille, 48)
    for k in range(n + 1):
        o.append(f'<line x1="{x0 + k * taille / n}" y1="{y0}" x2="{x0 + k * taille / n}" y2="{y0 + taille}" stroke="{PANNEAU}" stroke-width="2.5"/>')
        o.append(f'<line x1="{x0}" y1="{y0 + k * taille / n}" x2="{x0 + taille}" y2="{y0 + k * taille / n}" stroke="{PANNEAU}" stroke-width="2.5"/>')
    o.append(f'<text x="{x0 + taille + 18}" y="{y0 + taille / 2}" font-size="12.5" fill="{ENCRE_PALE}">une image, découpée</text>')
    o.append(f'<text x="{x0 + taille + 18}" y="{y0 + taille / 2 + 16}" font-size="12.5" fill="{ENCRE_PALE}">en 16 carrés</text>')
    o.append(f'<line x1="{x0 + taille / 2}" y1="{y0 + taille + 8}" x2="{x0 + taille / 2}" y2="{y0 + taille + 40}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#pointe)"/>')
    # la séquence de carrés
    c, e, xs, ys = 27, 5, 40, 290
    for k in range(16):
        i, j = k % n, k // n
        x = xs + k * (c + e)
        image_pixels(o, x, ys, c, 12, i / n, j / n, (i + 1) / n, (j + 1) / n)
        o.append(f'<rect x="{x}" y="{ys}" width="{c}" height="{c}" fill="none" stroke="{ENCRE_PALE}" stroke-width="0.8"/>')
        o.append(f'<text x="{x + c / 2}" y="{ys + c + 15}" font-size="10.5" fill="{GRIS}" text-anchor="middle">{k + 1}</text>')
    o.append(f'<text x="{xs}" y="{ys - 12}" font-size="12.5" fill="{ENCRE_PALE}">les carrés, alignés comme les mots d\'une phrase</text>')
    xf = xs + 16 * (c + e)
    o.append(f'<line x1="{xf + 2}" y1="{ys + c / 2}" x2="{xf + 30}" y2="{ys + c / 2}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#pointe)"/>')
    o.append(f'<rect x="{xf + 34}" y="{ys - 12}" width="98" height="{c + 24}" rx="10" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="2.2"/>')
    o.append(f'<text x="{xf + 83}" y="{ys + c / 2 + 5}" font-size="13" fill="{TEAL}" text-anchor="middle" font-weight="700">Transformer</text>')
    o.append(f'<text x="{W / 2}" y="{H - 16}" font-size="12.5" fill="{GRIS}" text-anchor="middle">Chaque carré peut regarder tous les autres, même éloignés dans l\'image.</text>')
    ecrire("vision-transformer.svg", o)


grille_traduction()
transformer()
vision()
print("attention-traduction.svg, transformer-blocs.svg et vision-transformer.svg écrits")
