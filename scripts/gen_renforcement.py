"""Module 3, « Apprendre à jouer » : la table remplacée par un réseau, et l'architecture d'AlphaGo."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module3"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, GRILLE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#e8dfc9", "#fbf7ee")
NB, FINE = " ", " "
POLICE = 'font-family="system-ui, -apple-system, sans-serif"'
BOIS = "#e6c98f"


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


def fr(v):
    return f"{v:.1f}".replace(".", ",").replace("-", "−")


def table_reseau():
    W, H = 700, 380
    o = entete(W, H, "La table du Module 2 remplacée par un réseau",
               f"Deux panneaux. À gauche, une grille de quatre cases sur cinq, avec une valeur écrite dans chaque case, comme la table du Module 2. "
               f"À droite, un écran de jeu, avec un mur de briques, une balle et une raquette, est donné à un réseau de neurones{NB}; le réseau produit une valeur "
               f"pour chacune des trois actions possibles{NB}: aller à gauche, rester, aller à droite.")
    o.append(f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">D\'une table de valeurs à un réseau</text>')
    for ox, wp, titre, sous in ((22, 250, "une table", "une valeur par situation"), (290, 388, "un réseau", "une valeur par action, pour toute situation")):
        o.append(f'<rect x="{ox}" y="56" width="{wp}" height="290" rx="10" fill="{PANNEAU}" stroke="{AXE}" stroke-width="1.2"/>')
        o.append(f'<text x="{ox + wp / 2}" y="82" font-size="14" fill="{ENCRE}" text-anchor="middle" font-weight="700">{titre}</text>')
        o.append(f'<text x="{ox + wp / 2}" y="100" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle">{sous}</text>')
    vals = [[0.3, 0.5, 0.7, 1.0], [0.2, None, 0.5, -1.0], [0.1, 0.2, 0.3, 0.1], [0.0, 0.1, 0.2, 0.1], [0.0, 0.0, 0.1, 0.0]]
    c, x0, y0 = 40, 67, 118
    for j, ligne in enumerate(vals):
        for i, v in enumerate(ligne):
            x, y = x0 + i * c, y0 + j * c
            if v is None:
                o.append(f'<rect x="{x}" y="{y}" width="{c}" height="{c}" fill="{GRIS}" fill-opacity="0.5" stroke="{PANNEAU}" stroke-width="2"/>')
                continue
            coul = TEAL if v > 0 else ROUGE if v < 0 else GRIS
            o.append(f'<rect x="{x}" y="{y}" width="{c}" height="{c}" fill="{coul}" fill-opacity="{0.08 + 0.35 * abs(v):.2f}" stroke="{PANNEAU}" stroke-width="2"/>')
            o.append(f'<text x="{x + c / 2}" y="{y + c / 2 + 4}" font-size="11.5" fill="{ENCRE}" text-anchor="middle">{fr(v)}</text>')
    # l'écran de jeu
    ex, ey, el, eh = 312, 140, 112, 150
    o.append(f'<rect x="{ex}" y="{ey}" width="{el}" height="{eh}" rx="4" fill="{ENCRE}"/>')
    couleurs = [ROUGE, BRUN, "#e2b33c", TEAL]
    for r, coul in enumerate(couleurs):
        for k in range(7):
            if (r, k) in ((3, 0), (3, 1), (2, 0)):
                continue
            o.append(f'<rect x="{ex + 4 + k * 15.4:.1f}" y="{ey + 10 + r * 9}" width="13.4" height="7" fill="{coul}"/>')
    o.append(f'<circle cx="{ex + 40}" cy="{ey + 92}" r="3.5" fill="{PANNEAU}"/>')
    o.append(f'<rect x="{ex + 46}" y="{ey + eh - 12}" width="24" height="5" fill="{PANNEAU}"/>')
    o.append(f'<text x="{ex + el / 2}" y="{ey + eh + 20}" font-size="11.5" fill="{GRIS}" text-anchor="middle">l\'écran (les pixels)</text>')
    # le réseau
    xs = [470, 520]
    ys1 = [150 + k * 26 for k in range(6)]
    ys2 = [176 + k * 30 for k in range(3)]
    o.append(f'<line x1="{ex + el + 6}" y1="{ey + eh / 2}" x2="{xs[0] - 14}" y2="{ey + eh / 2}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#pointe)"/>')
    for y1 in ys1:
        for y2 in ys2:
            o.append(f'<line x1="{xs[0]}" y1="{y1}" x2="{xs[1]}" y2="{y2}" stroke="{AXE}" stroke-width="0.7"/>')
    for y in ys1:
        o.append(f'<circle cx="{xs[0]}" cy="{y}" r="7" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="1.8"/>')
    for y, (nom, v) in zip(ys2, (("gauche", 0.2), ("rester", 0.4), ("droite", 0.7))):
        o.append(f'<circle cx="{xs[1]}" cy="{y}" r="8" fill="{PANNEAU}" stroke="{ROUGE}" stroke-width="2"/>')
        o.append(f'<text x="{xs[1] + 16}" y="{y + 4}" font-size="12" fill="{ENCRE}">{nom}</text>')
        o.append(f'<rect x="{xs[1] + 64}" y="{y - 6}" width="{80 * v:.0f}" height="12" rx="2" fill="{ROUGE}" fill-opacity="{0.9 if v > 0.5 else 0.5}"/>')
        o.append(f'<text x="{xs[1] + 70 + 80 * v:.0f}" y="{y + 4}" font-size="11.5" fill="{ENCRE_PALE}">{fr(v)}</text>')
    o.append(f'<text x="{W / 2}" y="{H - 14}" font-size="12.5" fill="{GRIS}" text-anchor="middle">Le réseau estime aussi la valeur des situations qu\'il n\'a jamais rencontrées.</text>')
    ecrire("table-vers-reseau.svg", o)


def alphago():
    W, H = 700, 420
    o = entete(W, H, "Le fonctionnement d'AlphaGo",
               f"Un arbre de coups qui part de la position actuelle, en haut. Le réseau de politique désigne trois coups prometteurs, dont les branches sont "
               f"explorées{FINE}; les autres coups possibles, en pointillé, sont laissés de côté. Au bout des branches explorées, le réseau de valeur estime la "
               "probabilité de gagner de chaque position. AlphaGo joue le coup dont les positions sont les mieux évaluées.")
    o.append(f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">AlphaGo{NB}: une recherche guidée par deux réseaux</text>')

    def goban(x, y, t, accent=False):
        o.append(f'<rect x="{x - t / 2}" y="{y - t / 2}" width="{t}" height="{t}" rx="3" fill="{BOIS}" stroke="{ROUGE if accent else BRUN}" stroke-width="{2.2 if accent else 1}"/>')
        for k in range(1, 4):
            o.append(f'<line x1="{x - t / 2 + k * t / 4}" y1="{y - t / 2 + 2}" x2="{x - t / 2 + k * t / 4}" y2="{y + t / 2 - 2}" stroke="{ENCRE_PALE}" stroke-width="0.5"/>')
            o.append(f'<line x1="{x - t / 2 + 2}" y1="{y - t / 2 + k * t / 4}" x2="{x + t / 2 - 2}" y2="{y - t / 2 + k * t / 4}" stroke="{ENCRE_PALE}" stroke-width="0.5"/>')

    rx, ry = 350, 92
    goban(rx, ry, 40, True)
    o.append(f'<text x="{rx + 32}" y="{ry + 4}" font-size="12" fill="{ENCRE_PALE}">position actuelle</text>')
    # tous les coups possibles, la plupart laissés de côté
    enfants = [(90 + k * 47.5, 196) for k in range(12)]
    choisis = {3, 6, 9}
    for k, (x, y) in enumerate(enfants):
        if k in choisis:
            o.append(f'<line x1="{rx}" y1="{ry + 21}" x2="{x}" y2="{y - 16}" stroke="{TEAL}" stroke-width="2.6"/>')
        else:
            o.append(f'<line x1="{rx}" y1="{ry + 21}" x2="{x}" y2="{y - 16}" stroke="{AXE}" stroke-width="1" stroke-dasharray="3 4"/>')
            o.append(f'<circle cx="{x}" cy="{y - 10}" r="3" fill="{AXE}"/>')
    vals = {3: (58, 64, 51), 6: (71, 66, 74), 9: (40, 47, 38)}
    for k in sorted(choisis):
        x, y = enfants[k]
        goban(x, y, 30)
        for m, v in enumerate(vals[k]):
            fx, fy = x + (m - 1) * 40, 300
            o.append(f'<line x1="{x}" y1="{y + 16}" x2="{fx}" y2="{fy - 13}" stroke="{TEAL}" stroke-width="1.6"/>')
            goban(fx, fy, 24)
            o.append(f'<text x="{fx}" y="{fy + 30}" font-size="11.5" fill="{BRUN}" text-anchor="middle" font-weight="700">{v}{NB}%</text>')
    o.append(f'<text x="{enfants[6][0] + 22}" y="{enfants[6][1] + 4}" font-size="11.5" fill="{ROUGE}" text-anchor="start" font-weight="700">coup choisi</text>')
    goban(enfants[6][0], enfants[6][1], 30, True)
    # étiquettes des deux réseaux
    o.append(f'<text x="40" y="140" font-size="12.5" fill="{TEAL}" font-weight="700">réseau de politique</text>')
    o.append(f'<text x="40" y="156" font-size="11.5" fill="{ENCRE_PALE}">quels coups explorer{NB}?</text>')
    o.append(f'<text x="40" y="358" font-size="12.5" fill="{BRUN}" font-weight="700">réseau de valeur</text>')
    o.append(f'<text x="40" y="374" font-size="11.5" fill="{ENCRE_PALE}">qui va gagner{NB}?</text>')
    o.append(f'<text x="{W / 2}" y="{H - 14}" font-size="12.5" fill="{GRIS}" text-anchor="middle">Les coups en pointillé ne sont pas explorés{NB}; les pourcentages sont des probabilités de gagner.</text>')
    ecrire("alphago-recherche.svg", o)


table_reseau()
alphago()
print("table-vers-reseau.svg et alphago-recherche.svg écrits")
