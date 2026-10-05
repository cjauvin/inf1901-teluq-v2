"""Module 3, « L'attention et le Transformer » : recherche exacte et recherche floue (requête, clés, valeurs)."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module3"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
ENTREES = [("chameau", "« animal à bosses… »", BRUN), ("chat", "« petit félin… »", ROUGE),
           ("château", "« grande demeure… »", BLEU), ("chien", "« animal qui aboie… »", TEAL)]
W, H = 760, 542
RH, RG = 28, 9                                              # hauteur et écart des rangées
XQ, XK, XP, XV, XR = 40, 186, 300, 410, 596                 # requête, clés, poids, valeurs, résultat
LQ, LK, LP, LV, LR = 96, 92, 84, 152, 136
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Recherche exacte et recherche floue</title>",
     "<desc>Deux panneaux, avec les mêmes colonnes : requête, clés, poids, valeurs, résultat. Les clés sont quatre entrées d'un "
     "dictionnaire, chameau, chat, château et chien, et les valeurs leurs définitions. En haut, une recherche exacte : la requête "
     "« chat » correspond exactement à la clé « chat », qui reçoit tout le poids ; le résultat est sa définition, « petit félin ». "
     "En bas, une recherche floue, comme l'attention : la requête « chaton » n'est pas dans le dictionnaire ; elle est comparée à "
     "toutes les clés, qui reçoivent des poids de 12 % pour chameau, 60 % pour chat, 8 % pour château et 20 % pour chien ; le "
     "résultat est un mélange des quatre définitions dans ces proportions, surtout celle de chat.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Chercher dans un dictionnaire{NB}: exactement, ou de façon floue</text>']


def panneau(y0, titre, requete, poids, legende):
    o.append(f'<rect x="20" y="{y0}" width="{W - 40}" height="230" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
    o.append(f'<text x="36" y="{y0 + 24}" font-size="13" fill="{BRUN}" font-weight="700">{titre}</text>')
    yh = y0 + 50
    for x, l, t in [(XQ, LQ, "requête"), (XK, LK, "clés"), (XP, LP, "poids"), (XV, LV, "valeurs"), (XR, LR, "résultat")]:
        o.append(f'<text x="{x + l / 2}" y="{yh}" font-size="11.5" fill="{TEAL}" text-anchor="middle" font-weight="700">{t}</text>')
    ys = [yh + 14 + k * (RH + RG) for k in range(4)]
    ymid = (ys[0] + ys[-1] + RH) / 2
    # la requête et ses liens vers les clés, d'épaisseur proportionnelle au poids
    for y, p in zip(ys, poids):
        if p:
            o.append(f'<line x1="{XQ + LQ}" y1="{ymid}" x2="{XK - 2}" y2="{y + RH / 2}" stroke="{GRIS}" stroke-width="{0.8 + 4 * p:.1f}" stroke-linecap="round"/>')
        else:
            o.append(f'<line x1="{XQ + LQ}" y1="{ymid}" x2="{XK - 2}" y2="{y + RH / 2}" stroke="{AXE}" stroke-width="1" stroke-dasharray="3 3"/>')
    o.append(f'<rect x="{XQ}" y="{ymid - 17}" width="{LQ}" height="34" rx="7" fill="#efe3c2" stroke="{BRUN}" stroke-width="1.8"/>')
    o.append(f'<text x="{XQ + LQ / 2}" y="{ymid + 5}" font-size="13.5" fill="{ENCRE}" text-anchor="middle" font-weight="700">{requete}</text>')
    xr_entree = XR - 4
    for (cle, val, coul), y, p in zip(ENTREES, ys, poids):
        actif = p > 0
        op = "" if actif else ' opacity="0.45"'
        # clé
        o.append(f'<rect x="{XK}" y="{y}" width="{LK}" height="{RH}" rx="6" fill="{FOND}" stroke="{ENCRE if p == 1 else AXE}" stroke-width="{2 if p == 1 else 1.2}"{op}/>')
        o.append(f'<text x="{XK + LK / 2}" y="{y + 18.5}" font-size="12" fill="{ENCRE}" text-anchor="middle"{op}>{cle}</text>')
        # poids : une barre et un pourcentage
        o.append(f'<rect x="{XP}" y="{y + 8}" width="{LP - 44}" height="{RH - 16}" rx="3" fill="{FOND}" stroke="{BORD}"/>')
        if actif:
            o.append(f'<rect x="{XP}" y="{y + 8}" width="{(LP - 44) * p:.1f}" height="{RH - 16}" rx="3" fill="{coul}"/>')
        o.append(f'<text x="{XP + LP}" y="{y + 18.5}" font-size="11.5" fill="{ENCRE if actif else AXE}" text-anchor="end">{round(p * 100)}{NB}%</text>')
        # valeur : une carte à bande de couleur
        o.append(f'<g{op}><rect x="{XV}" y="{y}" width="{LV}" height="{RH}" rx="6" fill="{PANNEAU}" stroke="{coul}" stroke-width="1.4"/>'
                 f'<rect x="{XV}" y="{y}" width="9" height="{RH}" rx="3" fill="{coul}"/>'
                 f'<text x="{XV + 16}" y="{y + 18.5}" font-size="11" fill="{ENCRE}" font-style="italic">{val}</text></g>')
        # vers le résultat
        if actif:
            o.append(f'<line x1="{XV + LV + 2}" y1="{y + RH / 2}" x2="{xr_entree}" y2="{ymid}" stroke="{coul}" '
                     f'stroke-width="{0.8 + 4 * p:.1f}" stroke-linecap="round" marker-end="url(#p)"/>')
    # résultat
    yr = ymid - 17
    if poids.count(0) == 3:                                   # une seule entrée retenue : sa définition
        k = poids.index(1)
        cle, val, coul = ENTREES[k]
        o.append(f'<rect x="{XR}" y="{yr}" width="{LR}" height="34" rx="6" fill="{PANNEAU}" stroke="{coul}" stroke-width="2"/>'
                 f'<rect x="{XR}" y="{yr}" width="9" height="34" rx="3" fill="{coul}"/>'
                 f'<text x="{XR + 16}" y="{yr + 21.5}" font-size="11.5" fill="{ENCRE}" font-style="italic">{val}</text>')
    else:                                                      # un mélange, chaque couleur selon son poids
        x = XR
        o.append(f'<clipPath id="c{y0}"><rect x="{XR}" y="{yr}" width="{LR}" height="34" rx="6"/></clipPath><g clip-path="url(#c{y0})">')
        for (_, _, coul), p in zip(ENTREES, poids):
            o.append(f'<rect x="{x:.1f}" y="{yr}" width="{LR * p + 0.5:.1f}" height="34" fill="{coul}"/>')
            x += LR * p
        o.append("</g>")
        o.append(f'<rect x="{XR}" y="{yr}" width="{LR}" height="34" rx="6" fill="none" stroke="{ENCRE}" stroke-width="1.4"/>')
    for k, l in enumerate(legende):
        o.append(f'<text x="{XR + LR / 2}" y="{yr + 56 + 15 * k}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">{l}</text>')


panneau(52, "1. Recherche exacte : le dictionnaire", "chat", [0, 1, 0, 0], ["la définition de", "l'entrée trouvée"])
panneau(296, "2. Recherche floue : l'attention", "chaton", [0.12, 0.60, 0.08, 0.20], ["surtout « chat »,", "un peu de chacune"])
o.append("</svg>")
(OUT / "recherche-floue.svg").write_text("\n".join(o) + "\n")
print("recherche-floue.svg écrit")
