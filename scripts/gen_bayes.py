"""Module 2, « Classer » : du classifieur naïf au réseau bayésien, et le réseau de l'alarme avec ses tables."""
import math
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module2"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, GRILLE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#e8dfc9", "#fbf7ee")
NB, FINE = " ", " "


def entete(w, h, titre, desc):
    return ['<?xml version="1.0" encoding="UTF-8"?>',
            f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
            f"<title>{titre}</title>", f"<desc>{desc}</desc>",
            f'<defs><marker id="pointe" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto">'
            f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
            f'<rect x="0" y="0" width="{w}" height="{h}" rx="14" fill="{FOND}" stroke="{BORD}"/>']


def noeud(o, x, y, nom, l=104, coul=TEAL):
    o.append(f'<rect x="{x - l / 2}" y="{y - 18}" width="{l}" height="36" rx="18" fill="{PANNEAU}" stroke="{coul}" stroke-width="2"/>')
    o.append(f'<text x="{x}" y="{y + 4.5}" font-size="12.5" fill="{ENCRE}" text-anchor="middle" font-weight="600">{nom}</text>')


def fleche(o, a, b, la=104, lb=104):
    """Flèche du bord de l'ovale a vers le bord de l'ovale b (approximation par une ellipse)."""
    (x1, y1), (x2, y2) = a, b
    ang = math.atan2(y2 - y1, x2 - x1)
    def bord(l, sens):
        rx, ry = l / 2, 18
        t = math.atan2(math.sin(ang) * sens, math.cos(ang) * sens)
        k = 1 / math.sqrt((math.cos(t) / rx) ** 2 + (math.sin(t) / ry) ** 2)
        return k * math.cos(t), k * math.sin(t)
    dx1, dy1 = bord(la, 1)
    dx2, dy2 = bord(lb, -1)
    o.append(f'<line x1="{x1 + dx1:.1f}" y1="{y1 + dy1:.1f}" x2="{x2 + dx2:.1f}" y2="{y2 + dy2:.1f}" stroke="{GRIS}" stroke-width="1.8" marker-end="url(#pointe)"/>')


def naif_et_reseau():
    W, H = 700, 330
    o = entete(W, H, "Du classifieur naïf au réseau bayésien",
               f"Deux panneaux. À gauche, le classifieur bayésien naïf dessiné comme un graphe{NB}: un nœud «{FINE}pourriel{FINE}?{FINE}» relié par des "
               f"flèches à trois nœuds de mots, «{FINE}gratuit{FINE}», «{FINE}carte{FINE}» et «{FINE}réunion{FINE}», sans flèche entre les mots. À droite, "
               f"un réseau bayésien plus riche{NB}: «{FINE}grippe{FINE}» pointe vers «{FINE}fièvre{FINE}» et «{FINE}toux{FINE}», «{FINE}rhume{FINE}» pointe "
               f"aussi vers «{FINE}toux{FINE}», et «{FINE}fièvre{FINE}» pointe vers «{FINE}fatigue{FINE}».")
    o.append(f'<text x="{W / 2}" y="34" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Deux réseaux bayésiens</text>')
    for ox, titre, sous in ((22, "Le classifieur naïf", "les mots ne dépendent que de la classe"), (358, "Un réseau plus riche", "chaque flèche est une influence directe")):
        o.append(f'<rect x="{ox}" y="54" width="320" height="250" rx="10" fill="{PANNEAU}" stroke="{AXE}" stroke-width="1.2"/>')
        o.append(f'<text x="{ox + 160}" y="80" font-size="13.5" fill="{ENCRE}" text-anchor="middle" font-weight="700">{titre}</text>')
        o.append(f'<text x="{ox + 160}" y="98" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle">{sous}</text>')
    c = (182, 150)
    mots = [(82, 250, "gratuit"), (182, 250, "carte"), (282, 250, "réunion")]
    for x, y, m in mots:
        fleche(o, c, (x, y), 110, 86)
    noeud(o, *c, f"pourriel{FINE}?", 110, ROUGE)
    for x, y, m in mots:
        noeud(o, x, y, m, 86, BLEU)
    n = {"grippe": (450, 145), "rhume": (600, 145), "fièvre": (430, 215), "toux": (560, 215), "fatigue": (470, 275)}
    for a, b in (("grippe", "fièvre"), ("grippe", "toux"), ("rhume", "toux"), ("fièvre", "fatigue")):
        fleche(o, n[a], n[b], 86, 86)
    for nom, (x, y) in n.items():
        noeud(o, x, y, nom, 86, ROUGE if nom in ("grippe", "rhume") else BLEU)
    o.append(f'<text x="{W / 2}" y="{H - 10}" font-size="12" fill="{GRIS}" text-anchor="middle">En rouge, les causes{FINE}; en bleu, ce qu\'on observe.</text>')
    o.append("</svg>")
    (OUT / "bayes-naif-et-reseau.svg").write_text("\n".join(o) + "\n")


def table(o, x, y, lignes, l):
    """Une petite table de probabilités : lignes = liste de (condition, probabilité)."""
    h = 16 * len(lignes) + 8
    o.append(f'<rect x="{x}" y="{y}" width="{l}" height="{h}" rx="5" fill="{FOND}" stroke="{AXE}"/>')
    for k, (cond, p) in enumerate(lignes):
        yy = y + 17 + 16 * k
        o.append(f'<text x="{x + 8}" y="{yy}" font-size="11" fill="{ENCRE_PALE}">{cond}</text>')
        o.append(f'<text x="{x + l - 8}" y="{yy}" font-size="11" fill="{ENCRE}" text-anchor="end" font-weight="700">{p}</text>')


def alarme():
    W, H = 700, 470
    o = entete(W, H, "Le réseau bayésien de l'alarme",
               f"Cinq nœuds. Cambriolage et Séisme pointent vers Alarme, qui pointe vers Jean appelle et Marie appelle. Chaque nœud porte sa table{NB}: "
               f"cambriolage 0,1{NB}%{FINE}; séisme 0,2{NB}%{FINE}; l'alarme sonne à 95{NB}% s'il y a cambriolage et séisme, 94{NB}% s'il y a seulement "
               f"cambriolage, 29{NB}% s'il y a seulement séisme, 0,1{NB}% sinon{FINE}; Jean appelle à 90{NB}% si l'alarme sonne et 5{NB}% sinon{FINE}; "
               f"Marie appelle à 70{NB}% si l'alarme sonne et 1{NB}% sinon.")
    o.append(f'<text x="{W / 2}" y="34" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Le réseau de l\'alarme et ses tables</text>')
    C, S, A, J, M = (240, 100), (460, 100), (350, 235), (240, 370), (460, 370)
    for a, b in ((C, A), (S, A), (A, J), (A, M)):
        fleche(o, a, b, 120, 120)
    noeud(o, *C, "Cambriolage", 120, ROUGE)
    noeud(o, *S, "Séisme", 120, ROUGE)
    noeud(o, *A, "Alarme", 120, TEAL)
    noeud(o, *J, "Jean appelle", 120, BLEU)
    noeud(o, *M, "Marie appelle", 120, BLEU)
    pc = f"{NB}%"
    table(o, 32, 76, [("P(cambriolage)", "0,1" + pc)], 140)
    table(o, 548, 76, [("P(séisme)", "0,2" + pc)], 120)
    table(o, 446, 184, [("cambriolage et séisme", "95" + pc), ("cambriolage seul", "94" + pc), ("séisme seul", "29" + pc), ("ni l'un ni l'autre", "0,1" + pc)], 206)
    o.append(f'<text x="549" y="176" font-size="11" fill="{TEAL}" text-anchor="middle" font-weight="700">P(alarme sonne)</text>')
    table(o, 32, 400, [("si alarme", "90" + pc), ("sinon", "5" + pc)], 124)
    o.append(f'<text x="94" y="394" font-size="11" fill="{BLEU}" text-anchor="middle" font-weight="700">P(Jean appelle)</text>')
    table(o, 544, 400, [("si alarme", "70" + pc), ("sinon", "1" + pc)], 124)
    o.append(f'<text x="606" y="394" font-size="11" fill="{BLEU}" text-anchor="middle" font-weight="700">P(Marie appelle)</text>')
    o.append("</svg>")
    (OUT / "reseau-alarme.svg").write_text("\n".join(o) + "\n")


naif_et_reseau()
alarme()
print("bayes-naif-et-reseau.svg et reseau-alarme.svg écrits")
