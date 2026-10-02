"""Module 3, « L'apprentissage profond » : large ou profond, hiérarchie de caractéristiques, sigmoïde et ReLU, concours ImageNet."""
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
            f'<rect x="0" y="0" width="{w}" height="{h}" rx="14" fill="{FOND}" stroke="{BORD}"/>']


def ecrire(nom, o):
    o.append("</svg>")
    (OUT / nom).write_text("\n".join(o) + "\n")


# ---------------------------------------------------------------- large ou profond
def reseau(o, ox, largeur, couches, haut=118, bas=318):
    """Dessine un réseau dont `couches` donne le nombre de neurones par couche, dans un panneau de `largeur` pixels."""
    n = len(couches)
    xs = [ox + 46 + k * (largeur - 92) / (n - 1) for k in range(n)]
    cy = (haut + bas) / 2

    def ys(m):
        pas = min(34, (bas - haut) / max(m - 1, 1))
        return [cy + (i - (m - 1) / 2) * pas for i in range(m)]

    pos = [[(x, y) for y in ys(m)] for x, m in zip(xs, couches)]
    for a, b in zip(pos, pos[1:]):
        for x1, y1 in a:
            for x2, y2 in b:
                o.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{AXE}" stroke-width="0.7" opacity="0.85"/>')
    for k, col in enumerate(pos):
        coul = BLEU if k == 0 else ROUGE if k == n - 1 else TEAL
        r = 9 if len(col) <= 6 else 6.5
        for x, y in col:
            o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{PANNEAU}" stroke="{coul}" stroke-width="2"/>')


def large_ou_profond():
    W, H = 700, 400
    o = entete(W, H, "Un réseau large et un réseau profond",
               f"Deux réseaux qui ont les mêmes quatre entrées et les mêmes deux sorties. À gauche, un réseau large{NB}: une seule couche cachée de douze neurones. "
               f"À droite, un réseau profond{NB}: trois couches cachées de quatre neurones chacune.")
    o.append(f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Deux façons d\'agrandir un réseau</text>')
    for ox, titre, sous, couches in ((22, "Un réseau large", "une couche cachée de 12 neurones", [4, 12, 2]),
                                     (358, "Un réseau profond", "trois couches cachées de 4 neurones", [4, 4, 4, 4, 2])):
        o.append(f'<rect x="{ox}" y="58" width="320" height="300" rx="10" fill="{PANNEAU}" stroke="{AXE}" stroke-width="1.2"/>')
        o.append(f'<text x="{ox + 160}" y="84" font-size="14" fill="{ENCRE}" text-anchor="middle" font-weight="700">{titre}</text>')
        o.append(f'<text x="{ox + 160}" y="103" font-size="12" fill="{TEAL}" text-anchor="middle">{sous}</text>')
        reseau(o, ox, 320, couches, 132, 328)
    o.append(f'<text x="{W / 2}" y="{H - 16}" font-size="12.5" fill="{GRIS}" text-anchor="middle">Dans le réseau profond, chaque couche part de ce que la précédente a construit.</text>')
    ecrire("large-ou-profond.svg", o)


# ---------------------------------------------------------------- hiérarchie de caractéristiques
def tuile(o, x, y, dessin, cote=54, coul=ENCRE):
    o.append(f'<rect x="{x - cote / 2}" y="{y - cote / 2}" width="{cote}" height="{cote}" rx="7" fill="{PANNEAU}" stroke="{AXE}" stroke-width="1.2"/>')
    o.append(f'<g transform="translate({x} {y})" fill="none" stroke="{coul}" stroke-width="4" stroke-linecap="round">{dessin}</g>')


def hierarchie():
    W, H = 700, 430
    o = entete(W, H, "Une hiérarchie de caractéristiques",
               f"Trois colonnes reliées par des traits. À gauche, la première couche détecte des traits simples{NB}: horizontal, vertical, oblique, arcs de cercle. "
               f"Au centre, la deuxième couche les combine en formes{NB}: une boucle, une barre verticale, un angle. À droite, la troisième couche combine les formes en chiffres{NB}: "
               "le 8 est fait de deux boucles, le 9 d'une boucle au-dessus d'une barre.")
    o.append(f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">De couche en couche, des caractéristiques plus complexes</text>')
    x1, x2, x3 = 120, 350, 580
    traits = [("arc haut", '<path d="M-14 8 A14 14 0 0 1 14 8"/>'), ("arc bas", '<path d="M-14 -8 A14 14 0 0 0 14 -8"/>'),
              ("vertical", '<line x1="0" y1="-16" x2="0" y2="16"/>'), ("horizontal", '<line x1="-16" y1="0" x2="16" y2="0"/>'),
              ("oblique", '<line x1="-13" y1="13" x2="13" y2="-13"/>')]
    formes = [("boucle", '<circle cx="0" cy="0" r="14"/>'), ("barre", '<line x1="0" y1="-19" x2="0" y2="19"/>'),
              ("angle", '<path d="M-13 -13 L13 -13 L-6 16"/>')]
    chiffres = [("8", '<circle cx="0" cy="-10" r="9"/><circle cx="0" cy="11" r="11"/>'),
                ("9", '<circle cx="-1" cy="-9" r="10"/><path d="M9 -9 L9 6 Q8 20 -6 20"/>')]
    yt = [112 + k * 62 for k in range(5)]
    yf = [142, 236, 330]
    yc = [180, 300]
    liens12 = [(0, 0), (1, 0), (2, 1), (3, 2), (4, 2)]
    liens23 = [(0, 0), (0, 1), (1, 1)]
    for a, b in liens12:
        o.append(f'<line x1="{x1 + 31}" y1="{yt[a]}" x2="{x2 - 39}" y2="{yf[b]}" stroke="{GRIS}" stroke-width="1.6"/>')
    for a, b in liens23:
        o.append(f'<line x1="{x2 + 39}" y1="{yf[a]}" x2="{x3 - 46}" y2="{yc[b]}" stroke="{GRIS}" stroke-width="1.6"/>')
    for y, (_, d) in zip(yt, traits):
        tuile(o, x1, y, d, 50, BLEU)
    for y, (_, d) in zip(yf, formes):
        tuile(o, x2, y, d, 66, TEAL)
    for y, (_, d) in zip(yc, chiffres):
        tuile(o, x3, y, d, 80, ROUGE)
    for x, t, s in ((x1, "première couche", "des traits"), (x2, "deuxième couche", "des formes"), (x3, "troisième couche", "des chiffres")):
        o.append(f'<text x="{x}" y="62" font-size="12.5" fill="{ENCRE_PALE}" text-anchor="middle" font-weight="700">{t}</text>')
        o.append(f'<text x="{x}" y="78" font-size="12" fill="{GRIS}" text-anchor="middle">{s}</text>')
    o.append(f'<text x="{W / 2}" y="{H - 16}" font-size="12.5" fill="{GRIS}" text-anchor="middle">Schéma simplifié{NB}: le réseau trouve lui-même ses caractéristiques pendant l\'entraînement.</text>')
    ecrire("hierarchie-chiffres.svg", o)


# ---------------------------------------------------------------- sigmoïde et ReLU
def activations():
    W, H = 700, 330
    o = entete(W, H, "Deux fonctions d'activation : la sigmoïde et la ReLU",
               f"Deux graphiques. À gauche, la sigmoïde{NB}: une courbe en S, qui plafonne à 0 pour les entrées très négatives et à 1 pour les entrées très positives. "
               f"À droite, la ReLU{NB}: elle vaut 0 pour toute entrée négative, puis monte en ligne droite pour les entrées positives, sans plafond.")
    o.append(f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Deux fonctions d\'activation</text>')
    for ox, titre, sous, f, ymax in ((22, "La sigmoïde", "plafonne des deux côtés", lambda z: 1 / (1 + math.exp(-z)), 1.0),
                                     (358, "La ReLU", "zéro, puis une droite", lambda z: max(0.0, z), 5.0)):
        o.append(f'<rect x="{ox}" y="58" width="320" height="240" rx="10" fill="{PANNEAU}" stroke="{AXE}" stroke-width="1.2"/>')
        o.append(f'<text x="{ox + 160}" y="84" font-size="14" fill="{ENCRE}" text-anchor="middle" font-weight="700">{titre}</text>')
        o.append(f'<text x="{ox + 160}" y="103" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle">{sous}</text>')
        gx, gw, gy, gh = ox + 44, 240, 252, 118
        X = lambda z: gx + (z + 6) / 12 * gw
        Y = lambda v: gy - v / ymax * gh
        o.append(f'<line x1="{gx}" y1="{gy}" x2="{gx + gw}" y2="{gy}" stroke="{AXE}" stroke-width="1.4"/>')
        o.append(f'<line x1="{X(0)}" y1="{gy + 4}" x2="{X(0)}" y2="{gy - gh - 6}" stroke="{AXE}" stroke-width="1.4"/>')
        o.append(f'<line x1="{gx}" y1="{Y(ymax)}" x2="{gx + gw}" y2="{Y(ymax)}" stroke="{GRILLE}" stroke-width="1" stroke-dasharray="4 4"/>')
        o.append(f'<text x="{X(0) - 7}" y="{Y(ymax) + 4}" font-size="11.5" fill="{GRIS}" text-anchor="end">{int(ymax)}</text>')
        o.append(f'<text x="{X(0) - 7}" y="{gy - 5}" font-size="11.5" fill="{GRIS}" text-anchor="end">0</text>')
        o.append(f'<text x="{gx}" y="{gy + 18}" font-size="11.5" fill="{GRIS}" text-anchor="middle">−6</text>')
        o.append(f'<text x="{gx + gw}" y="{gy + 18}" font-size="11.5" fill="{GRIS}" text-anchor="middle">6</text>')
        o.append(f'<text x="{gx + gw / 2}" y="{gy + 34}" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle">entrée du neurone</text>')
        pts = " ".join(f"{X(z / 10):.1f},{Y(min(f(z / 10), ymax)):.1f}" for z in range(-60, 51 if ymax > 1 else 61))
        o.append(f'<polyline points="{pts}" fill="none" stroke="{TEAL}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>')
    ecrire("sigmoide-relu.svg", o)


# ---------------------------------------------------------------- le concours ImageNet
def imagenet():
    W, H = 700, 420
    donnees = [(2010, 28.2), (2011, 25.8), (2012, 15.3), (2013, 11.7), (2014, 6.7), (2015, 3.6), (2016, 3.0), (2017, 2.3)]
    o = entete(W, H, "Le taux d'erreur du système gagnant au concours ImageNet, de 2010 à 2017",
               f"Un diagramme à barres. En 2010 et 2011, les systèmes gagnants reposent sur des caractéristiques fabriquées à la main{NB}: 28,2{NB}% puis 25,8{NB}% d'erreur. "
               f"En 2012, le réseau profond AlexNet obtient 15,3{NB}%. Les gagnants suivants sont tous des réseaux profonds{NB}: 11,7{NB}% en 2013, 6,7{NB}% en 2014, "
               f"3,6{NB}% en 2015, 3,0{NB}% en 2016 et 2,3{NB}% en 2017. Une ligne horizontale marque le niveau humain, estimé à 5{NB}%, dépassé à partir de 2015.")
    o.append(f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Concours ImageNet{NB}: taux d\'erreur du système gagnant</text>')
    gx, gy, gw, gh = 76, 330, 580, 240
    Y = lambda v: gy - v / 30 * gh
    for v in (0, 10, 20, 30):
        o.append(f'<line x1="{gx}" y1="{Y(v)}" x2="{gx + gw}" y2="{Y(v)}" stroke="{AXE if v == 0 else GRILLE}" stroke-width="{1.4 if v == 0 else 1}"/>')
        o.append(f'<text x="{gx - 10}" y="{Y(v) + 4}" font-size="11.5" fill="{GRIS}" text-anchor="end">{v}{NB}%</text>')
    pas, lb = gw / len(donnees), 44
    for k, (an, v) in enumerate(donnees):
        x = gx + k * pas + (pas - lb) / 2
        coul = BRUN if an < 2012 else TEAL
        o.append(f'<rect x="{x:.1f}" y="{Y(v):.1f}" width="{lb}" height="{gy - Y(v):.1f}" rx="3" fill="{coul}" fill-opacity="0.85"/>')
        yv = Y(v) - 8 if v > 6 else Y(5) - 9          # sous la ligne du niveau humain, la valeur passe au-dessus de la ligne
        o.append(f'<text x="{x + lb / 2:.1f}" y="{yv:.1f}" font-size="12" fill="{ENCRE}" text-anchor="middle" font-weight="700">{str(v).replace(".", ",")}</text>')
        o.append(f'<text x="{x + lb / 2:.1f}" y="{gy + 18}" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle">{an}</text>')
        if an == 2012:
            o.append(f'<text x="{x + lb / 2:.1f}" y="{Y(v) - 28:.1f}" font-size="12.5" fill="{TEAL}" text-anchor="middle" font-weight="700">AlexNet</text>')
    # le niveau humain
    xh = gx + 2 * pas + 8
    o.append(f'<line x1="{xh}" y1="{Y(5)}" x2="{gx + gw}" y2="{Y(5)}" stroke="{ROUGE}" stroke-width="1.8" stroke-dasharray="6 5"/>')
    o.append(f'<line x1="{gx + gw - 4}" y1="{Y(12.2)}" x2="{gx + gw - 4}" y2="{Y(5)}" stroke="{ROUGE}" stroke-width="1.2"/>')
    o.append(f'<text x="{gx + gw}" y="{Y(13.3)}" font-size="12" fill="{ROUGE}" text-anchor="end" font-weight="700">niveau humain, estimé à 5{NB}%</text>')
    # légende
    y = H - 26
    o.append(f'<rect x="150" y="{y - 11}" width="16" height="12" rx="2" fill="{BRUN}" fill-opacity="0.85"/><text x="173" y="{y}" font-size="12.5" fill="{ENCRE_PALE}">caractéristiques fabriquées à la main</text>')
    o.append(f'<rect x="430" y="{y - 11}" width="16" height="12" rx="2" fill="{TEAL}" fill-opacity="0.85"/><text x="453" y="{y}" font-size="12.5" fill="{ENCRE_PALE}">réseaux profonds</text>')
    ecrire("imagenet-erreur.svg", o)



# ---------------------------------------------------------------- la double descente
def lisse(pts):
    """Chemin SVG lisse (Catmull-Rom converti en courbes de Bézier) passant par les points donnés."""
    d = f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"
    for i in range(len(pts) - 1):
        p0, p1, p2, p3 = pts[max(i - 1, 0)], pts[i], pts[i + 1], pts[min(i + 2, len(pts) - 1)]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f" C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}"
    return d


def double_descente():
    W, H = 700, 400
    o = entete(W, H, "La double descente",
               f"Un graphique. À l'horizontale, la taille du modèle{FINE}; à la verticale, l'erreur sur des exemples nouveaux. La courbe descend, remonte "
               f"jusqu'à un pic, puis redescend plus bas qu'avant. La partie à gauche du pic est la courbe en U du Module 2. Le pic se trouve à la taille où le "
               "modèle peut mémoriser tous ses exemples. La partie à droite est celle des grands réseaux.")
    o.append(f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">La double descente</text>')
    gx, gy, gw, gh = 80, 318, 570, 230
    X = lambda t: gx + t * gw
    Y = lambda e: gy - e * gh
    xp = 0.48
    o.append(f'<rect x="{gx}" y="{gy - gh}" width="{X(xp) - gx:.1f}" height="{gh}" fill="{BRUN}" fill-opacity="0.06"/>')
    o.append(f'<rect x="{X(xp):.1f}" y="{gy - gh}" width="{gx + gw - X(xp):.1f}" height="{gh}" fill="{TEAL}" fill-opacity="0.07"/>')
    o.append(f'<line x1="{gx}" y1="{gy}" x2="{gx + gw}" y2="{gy}" stroke="{AXE}" stroke-width="1.5"/>')
    o.append(f'<line x1="{gx}" y1="{gy}" x2="{gx}" y2="{gy - gh}" stroke="{AXE}" stroke-width="1.5"/>')
    o.append(f'<line x1="{X(xp):.1f}" y1="{gy}" x2="{X(xp):.1f}" y2="{gy - gh}" stroke="{GRIS}" stroke-width="1.3" stroke-dasharray="5 5"/>')
    cles = [(0, .82), (0.08, .56), (0.17, .41), (0.26, .38), (0.35, .47), (0.43, .68), (0.48, .84), (0.53, .68), (0.60, .50), (0.70, .38), (0.83, .30), (1, .26)]
    o.append(f'<path d="{lisse([(X(t), Y(e)) for t, e in cles])}" fill="none" stroke="{ROUGE}" stroke-width="3" stroke-linecap="round"/>')
    o.append(f'<text x="{X(xp / 2):.1f}" y="{gy - gh + 20}" font-size="12.5" fill="{BRUN}" text-anchor="middle" font-weight="700">la courbe en U du Module 2</text>')
    o.append(f'<text x="{X((1 + xp) / 2):.1f}" y="{gy - gh + 20}" font-size="12.5" fill="{TEAL}" text-anchor="middle" font-weight="700">les grands réseaux</text>')
    o.append(f'<text x="{X(xp) + 10:.1f}" y="{gy - 26}" font-size="11.5" fill="{ENCRE_PALE}">le modèle peut mémoriser</text>')
    o.append(f'<text x="{X(xp) + 10:.1f}" y="{gy - 11}" font-size="11.5" fill="{ENCRE_PALE}">tous ses exemples</text>')
    o.append(f'<text x="{gx + gw / 2}" y="{gy + 28}" font-size="12.5" fill="{ENCRE_PALE}" text-anchor="middle">taille du modèle (nombre de paramètres) →</text>')
    o.append(f'<text x="{gx - 22}" y="{gy - gh / 2}" font-size="12.5" fill="{ENCRE_PALE}" text-anchor="middle" transform="rotate(-90 {gx - 22} {gy - gh / 2})">erreur sur des exemples nouveaux</text>')
    ecrire("double-descente.svg", o)


# ---------------------------------------------------------------- l'autoencodeur
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


def image_chiffre(o, x0, y0, t, flou):
    g = chiffre_zero()
    o.append(f'<rect x="{x0 - 3}" y="{y0 - 3}" width="{28 * t + 6:.1f}" height="{28 * t + 6:.1f}" rx="4" fill="{PANNEAU}" stroke="{AXE}"/>')
    for j, ligne in enumerate(g):
        for i, v in enumerate(ligne):
            if flou:          # l'image reconstruite : la moyenne des voisins, donc un trait un peu plus flou
                vs = [g[b][a] for a in range(max(i - 1, 0), min(i + 2, 28)) for b in range(max(j - 1, 0), min(j + 2, 28))]
                v = sum(vs) / len(vs)
            if v > 0.03:
                o.append(f'<rect x="{x0 + i * t:.1f}" y="{y0 + j * t:.1f}" width="{t + 0.3:.1f}" height="{t + 0.3:.1f}" fill="{ENCRE}" fill-opacity="{v:.2f}"/>')


def autoencodeur():
    W, H = 700, 400
    o = entete(W, H, "Un autoencodeur",
               f"De gauche à droite{NB}: l'image d'un zéro manuscrit{FINE}; un réseau en forme de sablier, dont les couches comptent de moins en moins de neurones "
               f"jusqu'à une couche centrale très étroite, puis de plus en plus{FINE}; l'image reconstruite, presque identique à l'image de départ. La première "
               f"moitié du réseau est l'encodeur, la couche centrale est la représentation latente, la seconde moitié est le décodeur.")
    o.append(f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Un autoencodeur{NB}: reproduire l\'entrée en passant par une couche étroite</text>')
    cy, t = 205, 3.6
    image_chiffre(o, 24, cy - 14 * t, t, False)
    image_chiffre(o, W - 24 - 28 * t, cy - 14 * t, t, True)
    o.append(f'<text x="{24 + 14 * t:.1f}" y="{cy + 14 * t + 24:.1f}" font-size="12" fill="{GRIS}" text-anchor="middle">image d\'entrée</text>')
    o.append(f'<text x="{W - 24 - 14 * t:.1f}" y="{cy + 14 * t + 24:.1f}" font-size="12" fill="{GRIS}" text-anchor="middle">image reconstruite</text>')
    couches, xs = [8, 5, 2, 5, 8], [190, 270, 350, 430, 510]
    pos = [[(x, cy + (i - (m - 1) / 2) * 27) for i in range(m)] for x, m in zip(xs, couches)]
    for a, b in zip(pos, pos[1:]):
        for x1, y1 in a:
            for x2, y2 in b:
                o.append(f'<line x1="{x1}" y1="{y1:.1f}" x2="{x2}" y2="{y2:.1f}" stroke="{AXE}" stroke-width="0.7" opacity="0.85"/>')
    for k, col in enumerate(pos):
        coul = ROUGE if k == 2 else TEAL
        for x, y in col:
            o.append(f'<circle cx="{x}" cy="{y:.1f}" r="{10 if k == 2 else 8}" fill="{PANNEAU}" stroke="{coul}" stroke-width="2.2"/>')
    yb = cy + 118
    for x1, x2, nom, coul in ((182, 300, "encodeur", TEAL), (400, 518, "décodeur", TEAL)):
        o.append(f'<path d="M{x1} {yb} v8 H{x2} v-8" fill="none" stroke="{coul}" stroke-width="1.6"/>')
        o.append(f'<text x="{(x1 + x2) / 2}" y="{yb + 28}" font-size="13" fill="{coul}" text-anchor="middle" font-weight="700">{nom}</text>')
    o.append(f'<text x="350" y="{cy - 46}" font-size="12.5" fill="{ROUGE}" text-anchor="middle" font-weight="700">représentation</text>')
    o.append(f'<text x="350" y="{cy - 31}" font-size="12.5" fill="{ROUGE}" text-anchor="middle" font-weight="700">latente</text>')
    ecrire("autoencodeur.svg", o)


large_ou_profond()
hierarchie()
activations()
imagenet()
double_descente()
autoencodeur()
print("six figures écrites pour « L'apprentissage profond »")
