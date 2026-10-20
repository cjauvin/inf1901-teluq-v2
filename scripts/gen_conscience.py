# /// script
# requires-python = ">=3.10"
# ///
"""Module 5, « Une machine peut-elle être consciente ? », section « Ce que l'on appelle conscience » : trois figures.
- nagel-chauve-souris.svg : l'écholocation, que l'on peut décrire, et ce que cela fait de la vivre, qui échappe ;
- qualia-rouge.svg : la chaîne physique de la vision du rouge, et l'expérience vécue du rouge, séparées par le fossé ;
- mary-chambre.svg : Mary dans sa pièce en noir et blanc, puis devant une tomate mûre (Jackson, 1982)."""
import math
from pathlib import Path

DOSSIER = Path(__file__).resolve().parent.parent / "static" / "images" / "module5"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
VERT = "#4f7d3a"
NB = " "


def entete(o, W, H, titre, desc, extra_defs=""):
    o += ['<?xml version="1.0" encoding="UTF-8"?>',
          f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
          f"<title>{titre}</title>", f"<desc>{desc}</desc>",
          f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
          f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker>{extra_defs}</defs>',
          f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
          f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">{titre}</text>']


def texte(o, x, y, t, taille=11.5, coul=ENCRE, ancre="middle", gras=False, ital=False):
    g = ' font-weight="700"' if gras else ""
    i = ' font-style="italic"' if ital else ""
    o.append(f'<text x="{x}" y="{y}" font-size="{taille}" fill="{coul}" text-anchor="{ancre}"{g}{i}>{t}</text>')


def panneau(o, x, y, w, h, fond=PANNEAU, bord=BORD):
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fond}" stroke="{bord}"/>')


def personne(o, x, y, coul=ENCRE, fond=PANNEAU):
    """Une silhouette en buste ; (x, y) est le bas des épaules."""
    o.append(f'<circle cx="{x}" cy="{y - 44}" r="12" fill="{fond}" stroke="{coul}" stroke-width="2"/>')
    o.append(f'<path d="M{x - 20} {y} Q{x - 20} {y - 28} {x} {y - 28} Q{x + 20} {y - 28} {x + 20} {y}" fill="{fond}" stroke="{coul}" stroke-width="2"/>')


def ecrire(nom, o):
    o.append("</svg>")
    (DOSSIER / nom).write_text("\n".join(o) + "\n")
    print(nom, "écrit")


# ───────────────────────── 1. la chauve-souris de Nagel ─────────────────────────
def chauve_souris(o, cx, cy, s=1.0, coul=ENCRE):
    def aile(sg):
        p = [(6, -6), (30, -30), (70, -22), (60, -2), (52, 6), (42, -2), (34, 10), (24, 2), (8, 10)]
        q = [(cx + sg * dx * s, cy + dy * s) for dx, dy in p]
        return (f"M{q[0][0]:.1f} {q[0][1]:.1f} Q{q[1][0]:.1f} {q[1][1]:.1f} {q[2][0]:.1f} {q[2][1]:.1f} "
                f"Q{q[3][0]:.1f} {q[3][1]:.1f} {q[4][0]:.1f} {q[4][1]:.1f} Q{q[5][0]:.1f} {q[5][1]:.1f} {q[6][0]:.1f} {q[6][1]:.1f} "
                f"Q{q[7][0]:.1f} {q[7][1]:.1f} {q[8][0]:.1f} {q[8][1]:.1f} Z")
    o.append(f'<path d="{aile(1)} {aile(-1)}" fill="{coul}"/>')
    o.append(f'<ellipse cx="{cx}" cy="{cy + 2 * s:.1f}" rx="{9 * s:.1f}" ry="{14 * s:.1f}" fill="{coul}"/>')
    o.append(f'<circle cx="{cx}" cy="{cy - 12 * s:.1f}" r="{7.5 * s:.1f}" fill="{coul}"/>')
    for sg in (-1, 1):
        o.append(f'<path d="M{cx + sg * 3 * s:.1f} {cy - 17 * s:.1f} L{cx + sg * 8 * s:.1f} {cy - 27 * s:.1f} L{cx + sg * 7.5 * s:.1f} {cy - 13 * s:.1f} Z" fill="{coul}"/>')
        o.append(f'<circle cx="{cx + sg * 3 * s:.1f}" cy="{cy - 13 * s:.1f}" r="{1.3 * s:.1f}" fill="{PANNEAU}"/>')


def papillon(o, cx, cy):
    for sg in (-1, 1):
        o.append(f'<ellipse cx="{cx + sg * 8}" cy="{cy - 6}" rx="9" ry="7" fill="{BRUN}" fill-opacity="0.75" transform="rotate({sg * -25} {cx + sg * 8} {cy - 6})"/>')
        o.append(f'<ellipse cx="{cx + sg * 7}" cy="{cy + 6}" rx="6" ry="5" fill="{BRUN}" fill-opacity="0.6" transform="rotate({sg * 25} {cx + sg * 7} {cy + 6})"/>')
    o.append(f'<ellipse cx="{cx}" cy="{cy}" rx="2.2" ry="10" fill="{ENCRE}"/>')


def arc(o, cx, cy, r, a1, a2, coul, tirets=False):
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
    x2, y2 = cx + r * math.cos(math.radians(a2)), cy + r * math.sin(math.radians(a2))
    d = ' stroke-dasharray="5 4"' if tirets else ""
    o.append(f'<path d="M{x1:.1f} {y1:.1f} A{r} {r} 0 0 1 {x2:.1f} {y2:.1f}" fill="none" stroke="{coul}" stroke-width="2" stroke-linecap="round"{d}/>')


W, H = 840, 330
o = []
entete(o, W, H, "Quel effet cela fait-il d'être une chauve-souris ?",
       "Deux panneaux. À gauche, ce que l'on peut décrire : une chauve-souris émet des cris très aigus, représentés par des "
       "arcs, qui rebondissent sur un papillon de nuit ; elle écoute leurs échos, représentés par des arcs en pointillé qui "
       "reviennent vers elle, et en déduit la position de sa proie. À droite, ce qui échappe à la description : une personne "
       "imagine, dans une bulle de pensée, ce que vit la chauve-souris, mais la bulle ne contient qu'un point "
       "d'interrogation.")
panneau(o, 20, 50, 520, 260)
texte(o, 280, 76, "Ce que l'on peut décrire : l'écholocation".replace(" :", NB + ":"), 12.5, BLEU, gras=True)
BX, BY = 110, 175
chauve_souris(o, BX, BY)
for r in (95, 120, 145, 170):
    arc(o, BX + 10, BY - 8, r, -22, 22, BLEU)
MX, MY = 450, 160
papillon(o, MX, MY)
for r in (34, 60, 86):
    arc(o, MX - 6, MY + 2, r, 158, 202, TEAL, tirets=True)
texte(o, 262, 106, "des cris très aigus", 11, BLEU, gras=True)
texte(o, 395, 228, "leurs échos", 11, TEAL, gras=True)
texte(o, MX, 128, "une proie", 10.5, BRUN)
texte(o, 280, 270, "On peut décrire ce mécanisme en détail,", 11.5)
texte(o, 280, 288, "mesurer chaque cri et chaque écho.", 11.5)
panneau(o, 556, 50, 264, 260)
texte(o, 688, 76, "Ce qui échappe à la description", 12.5, ROUGE, gras=True)
personne(o, 616, 236)
for cx, cy, r in ((634, 174, 4), (646, 160, 6)):
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#ffffff" stroke="{GRIS}" stroke-width="1.4"/>')
o.append(f'<ellipse cx="{722}" cy="{122}" rx="80" ry="40" fill="#ffffff" stroke="{GRIS}" stroke-width="1.4"/>')
chauve_souris(o, 696, 126, 0.42, GRIS)
texte(o, 752, 136, "?", 30, ROUGE, gras=True)
texte(o, 688, 270, "Ce que cela fait de la vivre,", 11.5)
texte(o, 688, 288, "de l'intérieur, reste hors de portée.", 11.5)
ecrire("nagel-chauve-souris.svg", o)

# ───────────────────────── 2. les qualia du rouge ─────────────────────────
W, H = 840, 330
o = []
grad = (f'<radialGradient id="rouge" cx="0.42" cy="0.4" r="0.65"><stop offset="0" stop-color="#ea7a6c"/>'
        f'<stop offset="0.6" stop-color="{ROUGE}"/><stop offset="1" stop-color="#a5392f"/></radialGradient>')
entete(o, W, H, "Les qualia : ce que cela fait de voir du rouge".replace(" :", NB + ":"),
       "Deux panneaux séparés par un point d'interrogation. À gauche, ce que la science décrit quand on voit du rouge : "
       "une onde lumineuse de 700 nanomètres entre dans l'œil, active certains cônes de la rétine, qui envoient des influx "
       "nerveux jusqu'au cortex visuel. Tout cela se mesure de l'extérieur. À droite, ce que l'on vit : une tache rouge, "
       "le rouge tel qu'on le voit, accessible seulement de l'intérieur. Entre les deux, le fossé explicatif : rien, dans "
       "la chaîne physique, ne dit pourquoi elle s'accompagne de cette expérience.", grad)
panneau(o, 20, 50, 470, 260)
texte(o, 255, 76, "Ce que la science décrit", 12.5, BLEU, gras=True)
Y = 160
pts = " ".join(f"{40 + i:.1f},{Y + 14 * math.sin(i / 90 * 3 * 2 * math.pi):.1f}" for i in range(0, 91, 2))
o.append(f'<polyline points="{pts}" fill="none" stroke="{ROUGE}" stroke-width="2.2"/>')
texte(o, 85, 205, "la lumière", 11, ENCRE, gras=True)
texte(o, 85, 220, "700 nm", 10.5, ENCRE_PALE)
o.append(f'<line x1="138" y1="{Y}" x2="160" y2="{Y}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')
EX = 192
o.append(f'<path d="M{EX - 26} {Y} Q{EX} {Y - 24} {EX + 26} {Y} Q{EX} {Y + 24} {EX - 26} {Y} Z" fill="#ffffff" stroke="{ENCRE}" stroke-width="1.8"/>')
o.append(f'<circle cx="{EX}" cy="{Y}" r="9" fill="{BLEU}"/><circle cx="{EX}" cy="{Y}" r="4" fill="{ENCRE}"/>')
texte(o, EX, 205, "l'œil", 11, ENCRE, gras=True)
texte(o, EX, 220, "des cônes s'activent", 10.5, ENCRE_PALE)
o.append(f'<line x1="224" y1="{Y}" x2="246" y2="{Y}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')
train = [(252, Y)]
for x in (266, 284, 296, 318, 332):
    train += [(x - 3, Y), (x, Y - 24), (x + 3, Y + 8), (x + 6, Y)]
train.append((350, Y))
o.append(f'<polyline points="{" ".join(f"{a},{b}" for a, b in train)}" fill="none" stroke="{TEAL}" stroke-width="1.8" stroke-linejoin="round"/>')
texte(o, 301, 205, "des influx", 11, ENCRE, gras=True)
texte(o, 301, 220, "nerveux", 10.5, ENCRE_PALE)
o.append(f'<line x1="356" y1="{Y}" x2="378" y2="{Y}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')
CX = 425
o.append(f'<path d="M{CX - 36} {Y + 8} Q{CX - 40} {Y - 26} {CX - 8} {Y - 28} Q{CX + 6} {Y - 38} {CX + 26} {Y - 24} '
         f'Q{CX + 42} {Y - 14} {CX + 36} {Y + 6} Q{CX + 34} {Y + 22} {CX + 12} {Y + 20} Q{CX - 4} {Y + 28} {CX - 18} {Y + 20} '
         f'Q{CX - 34} {Y + 22} {CX - 36} {Y + 8} Z" fill="{PANNEAU}" stroke="{ENCRE}" stroke-width="1.8"/>')
o.append(f'<path d="M{CX - 22} {Y - 6} Q{CX - 10} {Y - 18} {CX} {Y - 6} Q{CX + 10} {Y + 6} {CX + 22} {Y - 8} M{CX - 16} {Y + 10} Q{CX} {Y + 2} {CX + 14} {Y + 10}" fill="none" stroke="{ENCRE_PALE}" stroke-width="1.3"/>')
texte(o, CX, 205, "le cerveau", 11, ENCRE, gras=True)
texte(o, CX, 220, "cortex visuel", 10.5, ENCRE_PALE)
texte(o, 255, 270, "Tout cela se mesure,", 11.5)
texte(o, 255, 288, "de l'extérieur.", 11.5)
o.append(f'<line x1="496" y1="{Y - 30}" x2="560" y2="{Y - 30}" stroke="{GRIS}" stroke-width="1.6" stroke-dasharray="5 4" marker-end="url(#p)"/>')
texte(o, 528, Y + 8, "?", 34, ROUGE, gras=True)
texte(o, 528, Y + 36, "le fossé", 10.5, ROUGE, gras=True)
texte(o, 528, Y + 50, "explicatif", 10.5, ROUGE, gras=True)
panneau(o, 566, 50, 254, 260)
texte(o, 693, 76, "Ce que l'on vit", 12.5, ROUGE, gras=True)
o.append(f'<circle cx="693" cy="{Y - 4}" r="54" fill="url(#rouge)"/>')
texte(o, 693, 236, "le rouge, tel qu'on le voit", 11, ENCRE, gras=True, ital=True)
texte(o, 693, 270, "Une expérience vécue,", 11.5)
texte(o, 693, 288, "accessible de l'intérieur seulement.", 11.5)
ecrire("qualia-rouge.svg", o)

# ───────────────────────── 3. Mary ─────────────────────────
W, H = 840, 330
o = []
entete(o, W, H, "La chambre de Mary (Jackson, 1982)",
       "Deux panneaux. À gauche, tout en gris : Mary, une scientifique, dans une pièce en noir et blanc, devant un écran "
       "qui affiche le spectre de la lumière, avec la longueur d'onde du rouge, 700 nanomètres, et une pile de livres "
       "d'optique, de neurologie et de physique : elle sait tout ce que la science dit de la vision des couleurs. Une "
       "flèche indique qu'elle sort. À droite, en couleurs : Mary voit pour la première fois une tomate mûre, d'un rouge "
       "vif. La question posée : apprend-elle quelque chose de nouveau ?")
G1, G2, G3, G4 = "#e4e4e2", "#bdbdbb", "#8c8c8a", "#4a4a48"
panneau(o, 20, 50, 365, 260, G1, G2)
texte(o, 202, 76, "Dans sa pièce en noir et blanc", 12.5, G4, gras=True)
o.append(f'<rect x="44" y="98" width="150" height="96" rx="5" fill="#ffffff" stroke="{G4}" stroke-width="1.6"/>')
pts = " ".join(f"{54 + i},{180 - 62 * math.exp(-((i - 70) / 32) ** 2):.1f}" for i in range(0, 131, 3))
o.append(f'<polyline points="{pts}" fill="none" stroke="{G4}" stroke-width="1.8"/>')
o.append(f'<line x1="54" y1="181" x2="186" y2="181" stroke="{G3}" stroke-width="1"/>')
o.append(f'<line x1="166" y1="112" x2="166" y2="181" stroke="{G3}" stroke-width="1" stroke-dasharray="3 3"/>')
texte(o, 162, 110, "700 nm", 9.5, G4, ancre="end")
o.append(f'<rect x="112" y="194" width="14" height="14" fill="{G3}"/><rect x="96" y="208" width="46" height="5" rx="2" fill="{G3}"/>')
for k, (t, w) in enumerate((("physique", 98), ("neurologie", 108), ("optique", 92))):
    y = 186 - k * 20
    o.append(f'<rect x="{204 + (108 - w) / 2}" y="{y}" width="{w}" height="18" rx="2" fill="{[G2, "#d2d2d0", G2][k]}" stroke="{G4}" stroke-width="1.2"/>')
    texte(o, 258, y + 13, t, 10, G4)
personne(o, 352, 214, G4, "#f2f2f0")
texte(o, 202, 270, "Mary sait tout ce que la science", 11.5, G4)
texte(o, 202, 288, "dit de la vision des couleurs.", 11.5, G4)
o.append(f'<line x1="392" y1="180" x2="448" y2="180" stroke="{GRIS}" stroke-width="1.8" marker-end="url(#p)"/>')
texte(o, 420, 168, "elle sort", 10.5, ENCRE_PALE, ital=True)
panneau(o, 455, 50, 365, 260)
texte(o, 637, 76, "Elle voit une tomate mûre", 12.5, ROUGE, gras=True)
TX, TY = 585, 168
o.append(f'<ellipse cx="{TX}" cy="{TY}" rx="52" ry="46" fill="{ROUGE}"/>')
o.append(f'<ellipse cx="{TX - 18}" cy="{TY - 18}" rx="12" ry="7" fill="#ffffff" fill-opacity="0.35" transform="rotate(-30 {TX - 18} {TY - 18})"/>')
etoile = []
for k in range(10):
    a = -math.pi / 2 + k * math.pi / 5
    r = 20 if k % 2 == 0 else 6
    etoile.append(f"{TX + r * math.cos(a):.1f},{TY - 44 + r * math.sin(a) * 0.55:.1f}")
o.append(f'<polygon points="{" ".join(etoile)}" fill="{VERT}"/>')
o.append(f'<path d="M{TX} {TY - 48} Q{TX + 2} {TY - 60} {TX + 8} {TY - 64}" fill="none" stroke="{VERT}" stroke-width="3" stroke-linecap="round"/>')
personne(o, 728, 214)
texte(o, 754, 152, "!", 26, ROUGE, gras=True)
texte(o, 637, 270, "Apprend-elle quelque chose de nouveau" + NB + "?", 11.5, ROUGE, gras=True)
texte(o, 637, 288, "Si oui, le savoir physique ne dit pas tout.", 11.5)
ecrire("mary-chambre.svg", o)
