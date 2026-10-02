"""Module 3, « Lire une séquence : les réseaux récurrents » : le réseau déroulé, l'influence qui s'efface."""
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
            '<defs>'
            f'<marker id="pointe" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker>'
            f'<marker id="pointe-rouge" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{ROUGE}"/></marker>'
            '</defs>',
            f'<rect x="0" y="0" width="{w}" height="{h}" rx="14" fill="{FOND}" stroke="{BORD}"/>']


def ecrire(nom, o):
    o.append("</svg>")
    (OUT / nom).write_text("\n".join(o) + "\n")


def cellule(o, x, y, op=1):
    o.append(f'<rect x="{x - 26}" y="{y - 24}" width="52" height="48" rx="12" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="2.4" opacity="{op}"/>')
    o.append(f'<text x="{x}" y="{y + 4}" font-size="11" fill="{TEAL}" text-anchor="middle" font-weight="700">cellule</text>')


def entree(o, x, y, nom):
    l = 66 if len(nom) > 3 else 48
    o.append(f'<rect x="{x - l / 2}" y="{y - 14}" width="{l}" height="28" rx="6" fill="{PANNEAU}" stroke="{BLEU}" stroke-width="1.8"/>')
    o.append(f'<text x="{x}" y="{y + 5}" font-size="12" fill="{BLEU}" text-anchor="middle" font-weight="700">{nom}</text>')


def deroule():
    W, H = 700, 330
    o = entete(W, H, "Un réseau récurrent, avec sa boucle puis déroulé",
               f"Deux panneaux. À gauche, une cellule reçoit un élément de la séquence par en dessous, et son état sort par la droite pour revenir dans la cellule par une boucle. "
               f"À droite, la même cellule déroulée sur cinq étapes{NB}: chaque copie reçoit un élément de la séquence, de x1 à x5, et passe son état à la copie suivante. "
               "Les cinq copies ont les mêmes poids.")
    o.append(f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Un réseau récurrent, replié puis déroulé</text>')
    for ox, wp, titre in ((22, 180, "avec sa boucle"), (226, 452, "déroulé sur cinq étapes")):
        o.append(f'<rect x="{ox}" y="58" width="{wp}" height="240" rx="10" fill="{PANNEAU}" stroke="{AXE}" stroke-width="1.2"/>')
        o.append(f'<text x="{ox + wp / 2}" y="84" font-size="14" fill="{ENCRE}" text-anchor="middle" font-weight="700">{titre}</text>')
    yc, ye = 178, 262
    # la version repliée
    x = 112
    cellule(o, x, yc)
    entree(o, x, ye, "élément")
    o.append(f'<line x1="{x}" y1="{ye - 16}" x2="{x}" y2="{yc + 27}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#pointe)"/>')
    o.append(f'<path d="M{x + 27} {yc} C{x + 75} {yc} {x + 70} {yc - 70} {x} {yc - 70} C{x - 70} {yc - 70} {x - 75} {yc} {x - 29} {yc}" fill="none" stroke="{ROUGE}" stroke-width="2.4" marker-end="url(#pointe-rouge)"/>')
    o.append(f'<text x="{x}" y="{yc - 78}" font-size="12" fill="{ROUGE}" text-anchor="middle" font-weight="700">état</text>')
    # la version déroulée
    xs = [292 + k * 82 for k in range(5)]
    o.append(f'<text x="231" y="{yc - 16}" font-size="10.5" fill="{GRIS}" text-anchor="start">départ</text>')
    o.append(f'<line x1="246" y1="{yc}" x2="{xs[0] - 29}" y2="{yc}" stroke="{ROUGE}" stroke-width="2.4" marker-end="url(#pointe-rouge)"/>')
    for k, x in enumerate(xs):
        cellule(o, x, yc)
        entree(o, x, ye, f"x{k + 1}")
        o.append(f'<line x1="{x}" y1="{ye - 16}" x2="{x}" y2="{yc + 27}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#pointe)"/>')
        if k < 4:
            o.append(f'<line x1="{x + 27}" y1="{yc}" x2="{xs[k + 1] - 29}" y2="{yc}" stroke="{ROUGE}" stroke-width="2.4" marker-end="url(#pointe-rouge)"/>')
            o.append(f'<text x="{x + 43}" y="{yc - 10}" font-size="11" fill="{ROUGE}" text-anchor="middle">état</text>')
    o.append(f'<line x1="{xs[-1] + 27}" y1="{yc}" x2="{xs[-1] + 48}" y2="{yc}" stroke="{ROUGE}" stroke-width="2.4" marker-end="url(#pointe-rouge)"/>')
    o.append(f'<text x="{(xs[0] + xs[-1]) / 2}" y="{yc - 52}" font-size="12" fill="{TEAL}" text-anchor="middle">la même cellule, avec les mêmes poids, à chaque étape</text>')
    o.append(f'<text x="{W / 2}" y="{H - 12}" font-size="12.5" fill="{GRIS}" text-anchor="middle">L\'état transmet à chaque étape un résumé de ce qui a été lu.</text>')
    ecrire("reseau-recurrent-deroule.svg", o)


def influence():
    W, H = 700, 360
    n = 12
    o = entete(W, H, "L'influence de chaque élément d'une séquence sur l'apprentissage",
               f"Un diagramme à barres pour une séquence de douze éléments. La barre du dernier élément, à droite, est la plus haute. Les barres diminuent vers la gauche, "
               "et celles des premiers éléments de la séquence sont presque nulles.")
    o.append(f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Les premiers éléments s\'effacent</text>')
    gx, gy, gw, gh = 70, 270, 590, 190
    o.append(f'<line x1="{gx}" y1="{gy}" x2="{gx + gw}" y2="{gy}" stroke="{AXE}" stroke-width="1.5"/>')
    pas, lb = gw / n, 30
    for k in range(n):
        v = 0.62 ** (n - 1 - k)
        x = gx + k * pas + (pas - lb) / 2
        o.append(f'<rect x="{x:.1f}" y="{gy - v * gh:.1f}" width="{lb}" height="{v * gh:.1f}" rx="3" fill="{TEAL}" fill-opacity="0.85"/>')
        o.append(f'<text x="{x + lb / 2:.1f}" y="{gy + 17}" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">{k + 1}</text>')
    o.append(f'<text x="{gx + gw / 2}" y="{gy + 40}" font-size="12.5" fill="{ENCRE_PALE}" text-anchor="middle">position de l\'élément dans la séquence</text>')
    o.append(f'<text x="{gx}" y="{gy + 40}" font-size="12" fill="{GRIS}" text-anchor="start">← début</text>')
    o.append(f'<text x="{gx + gw}" y="{gy + 40}" font-size="12" fill="{GRIS}" text-anchor="end">fin →</text>')
    o.append(f'<text x="{gx - 18}" y="{gy - gh / 2}" font-size="12.5" fill="{ENCRE_PALE}" text-anchor="middle" transform="rotate(-90 {gx - 18} {gy - gh / 2})">influence sur la sortie</text>')
    ecrire("influence-sequence.svg", o)



def lstm():
    W, H = 700, 360
    o = entete(W, H, "Une cellule LSTM, simplifiée",
               f"Une ligne horizontale, la mémoire, traverse la cellule de gauche à droite. Trois portes agissent sur elle{NB}: la porte d'oubli efface une partie "
               f"de la mémoire, la porte d'entrée y écrit, la porte de sortie y lit pour produire le nouvel état. L'état précédent et l'élément courant arrivent par le bas "
               "et alimentent les trois portes.")
    o.append(f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Une cellule LSTM{NB}: une mémoire et trois portes</text>')
    o.append(f'<rect x="170" y="86" width="400" height="236" rx="14" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="2" stroke-dasharray="6 5"/>')
    o.append(f'<text x="560" y="312" font-size="12" fill="{TEAL}" text-anchor="end" font-weight="700">cellule LSTM</text>')
    ym, yg, yb = 125, 190, 282
    o.append(f'<line x1="40" y1="{ym}" x2="652" y2="{ym}" stroke="{BRUN}" stroke-width="5" marker-end="url(#pointe)"/>')
    o.append(f'<text x="40" y="{ym - 14}" font-size="12.5" fill="{BRUN}" font-weight="700">mémoire</text>')
    portes = ((250, "porte", "d'oubli", "×"), (360, "porte", "d'entrée", "+"), (470, "porte", "de sortie", ""))
    o.append(f'<line x1="200" y1="{yb}" x2="470" y2="{yb}" stroke="{BLEU}" stroke-width="2"/>')
    o.append(f'<line x1="40" y1="{yb}" x2="200" y2="{yb}" stroke="{BLEU}" stroke-width="2"/>')
    o.append(f'<text x="40" y="{yb - 26}" font-size="12" fill="{BLEU}" font-weight="700">état précédent</text>')
    o.append(f'<text x="40" y="{yb - 10}" font-size="12" fill="{BLEU}" font-weight="700">+ élément courant</text>')
    for x, l1, l2, op in portes:
        o.append(f'<line x1="{x}" y1="{yb}" x2="{x}" y2="{yg + 22}" stroke="{BLEU}" stroke-width="1.8" marker-end="url(#pointe)"/>')
        o.append(f'<rect x="{x - 44}" y="{yg - 22}" width="88" height="44" rx="10" fill="{FOND}" stroke="{TEAL}" stroke-width="2.2"/>')
        o.append(f'<text x="{x}" y="{yg - 3}" font-size="11.5" fill="{TEAL}" text-anchor="middle" font-weight="700">{l1}</text>')
        o.append(f'<text x="{x}" y="{yg + 12}" font-size="11.5" fill="{TEAL}" text-anchor="middle" font-weight="700">{l2}</text>')
        if op:
            o.append(f'<line x1="{x}" y1="{yg - 22}" x2="{x}" y2="{ym + 14}" stroke="{TEAL}" stroke-width="1.8"/>')
            o.append(f'<circle cx="{x}" cy="{ym}" r="13" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="2"/>')
            o.append(f'<text x="{x}" y="{ym + 6}" font-size="17" fill="{TEAL}" text-anchor="middle" font-weight="700">{op}</text>')
        else:
            o.append(f'<line x1="{x}" y1="{ym + 3}" x2="{x}" y2="{yg - 23}" stroke="{BRUN}" stroke-width="2" marker-end="url(#pointe)"/>')
    o.append(f'<line x1="514" y1="{yg}" x2="652" y2="{yg}" stroke="{ROUGE}" stroke-width="2.4" marker-end="url(#pointe-rouge)"/>')
    o.append(f'<text x="618" y="{yg - 10}" font-size="12" fill="{ROUGE}" text-anchor="middle" font-weight="700">nouvel état</text>')
    for x, t in ((250, "efface"), (360, "écrit"), (470, "lit")):
        o.append(f'<text x="{x + (22 if x != 470 else 12)}" y="{ym + 32 if x != 470 else ym + 30}" font-size="11.5" fill="{GRIS}" text-anchor="start">{t}</text>')
    o.append(f'<text x="{W / 2}" y="{H - 12}" font-size="12.5" fill="{GRIS}" text-anchor="middle">Chaque porte agit comme un robinet, entre 0 (fermé) et 1 (ouvert){NB}; ses poids sont appris.</text>')
    ecrire("cellule-lstm.svg", o)


def encodeur_decodeur():
    W, H = 700, 330
    o = entete(W, H, "L'architecture encodeur-décodeur pour la traduction",
               f"À gauche, l'encodeur, un réseau récurrent, lit les mots «{FINE}le{FINE}», «{FINE}chat{FINE}» et «{FINE}dort{FINE}» un à un. Son état final, au centre, "
               f"résume la phrase. À droite, le décodeur, un second réseau récurrent, part de ce résumé et écrit «{FINE}the{FINE}», «{FINE}cat{FINE}» et «{FINE}sleeps{FINE}» un à un.")
    o.append(f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Traduire avec deux réseaux récurrents</text>')
    yc = 168
    enc, dec, xr = [80, 160, 240], [460, 540, 620], 350
    for xs, mots, bas in ((enc, ("le", "chat", "dort"), True), (dec, ("the", "cat", "sleeps"), False)):
        for k, (x, m) in enumerate(zip(xs, mots)):
            cellule(o, x, yc)
            if bas:
                entree(o, x, yc + 82, m)
                o.append(f'<line x1="{x}" y1="{yc + 66}" x2="{x}" y2="{yc + 27}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#pointe)"/>')
            else:
                o.append(f'<line x1="{x}" y1="{yc - 26}" x2="{x}" y2="{yc - 64}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#pointe)"/>')
                o.append(f'<rect x="{x - 30}" y="{yc - 94}" width="60" height="28" rx="6" fill="{PANNEAU}" stroke="{ROUGE}" stroke-width="1.8"/>')
                o.append(f'<text x="{x}" y="{yc - 75}" font-size="12" fill="{ROUGE}" text-anchor="middle" font-weight="700">{m}</text>')
            if k < 2:
                o.append(f'<line x1="{x + 27}" y1="{yc}" x2="{xs[k + 1] - 29}" y2="{yc}" stroke="{ROUGE}" stroke-width="2.2" marker-end="url(#pointe-rouge)"/>')
    o.append(f'<line x1="{enc[-1] + 27}" y1="{yc}" x2="{xr - 24}" y2="{yc}" stroke="{ROUGE}" stroke-width="2.4" marker-end="url(#pointe-rouge)"/>')
    o.append(f'<line x1="{xr + 22}" y1="{yc}" x2="{dec[0] - 29}" y2="{yc}" stroke="{ROUGE}" stroke-width="2.4" marker-end="url(#pointe-rouge)"/>')
    o.append(f'<circle cx="{xr}" cy="{yc}" r="20" fill="{ROUGE}" fill-opacity="0.2" stroke="{ROUGE}" stroke-width="2.4"/>')
    o.append(f'<text x="{xr}" y="{yc + 44}" font-size="12" fill="{ROUGE}" text-anchor="middle" font-weight="700">le résumé</text>')
    o.append(f'<text x="{xr}" y="{yc + 59}" font-size="12" fill="{ROUGE}" text-anchor="middle" font-weight="700">de la phrase</text>')
    for xs, nom in ((enc, "encodeur"), (dec, "décodeur")):
        o.append(f'<text x="{xs[1]}" y="{yc - 52 if nom == "encodeur" else yc + 56}" font-size="13" fill="{TEAL}" text-anchor="middle" font-weight="700">{nom}</text>')
    o.append(f'<text x="{W / 2}" y="{H - 14}" font-size="12.5" fill="{GRIS}" text-anchor="middle">Toute la phrase d\'origine passe par un seul état, de taille fixe.</text>')
    ecrire("encodeur-decodeur.svg", o)


deroule()
influence()
lstm()
encodeur_decodeur()
print("quatre figures écrites pour « Lire une séquence »")
