# /// script
# requires-python = ">=3.10"
# dependencies = ["fonttools"]
# ///
"""Module 5, « Une machine peut-elle penser ? » : le problème de l'ancrage des symboles (Harnad, 1990), en trois
panneaux construits sur le même petit réseau de mots. Le dictionnaire unilingue chinois, où les définitions tournent en
rond ; l'humain, dont quelques mots s'ancrent dans la perception ; le modèle de langage, dont les vecteurs ne rejoignent
le monde que par le détour des textes. Les caractères chinois sont convertis en tracés (police Hiragino Sans GB de
macOS), comme dans la figure de la chambre chinoise."""
from pathlib import Path
from fontTools.ttLib import TTCollection
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module5" / "ancrage-des-symboles.svg"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB, FIN = " ", " "

POLICE = TTCollection("/System/Library/Fonts/Hiragino Sans GB.ttc").fonts[0]
CMAP, GLYPHES, UPM = POLICE.getBestCmap(), POLICE.getGlyphSet(), POLICE["head"].unitsPerEm


def largeur_zh(texte, taille):
    return sum(GLYPHES[CMAP[ord(c)]].width for c in texte) * taille / UPM


def chinois(texte, x, y, taille, coul=ENCRE):
    k, dx, chemins = taille / UPM, 0, []
    for c in texte:
        nom = CMAP[ord(c)]
        pen = SVGPathPen(GLYPHES)
        GLYPHES[nom].draw(TransformPen(pen, (k, 0, 0, -k, x + dx, y)))
        chemins.append(pen.getCommands())
        dx += GLYPHES[nom].width * k
    o.append(f'<path d="{" ".join(chemins)}" fill="{coul}"/>')


W, H, LP, PY, PH = 900, 482, 280, 50, 412
CY = 166                                    # centre du réseau
BANDE = 330                                 # haut de la bande « le monde »
# le réseau : position relative, mot français, mot chinois, vecteur
NOEUDS = [((0, 58), "chat", "猫", "0,21 −1,30 …"),
          ((-84, 0), "animal", "动物", "0,57 0,08 …"),
          ((84, 0), "miauler", "叫", "−0,92 0,44 …"),
          ((-58, -58), "poil", "毛", "1,13 −0,36 …"),
          ((58, -58), "compagnie", "宠物", "−0,15 0,71 …")]
ARETES = [(0, 1), (0, 2), (1, 3), (2, 4), (3, 4), (4, 0), (1, 2)]


def boite(mode, k):
    """Demi-largeur et demi-hauteur de la boîte du nœud k."""
    (_, _), fr, zh, _ = NOEUDS[k]
    if mode == "zh":
        return (largeur_zh(zh, 16) + 16) / 2, 15
    if mode == "fr":
        return (len(fr) * 6.6 + 18) / 2, 14
    return 40, 18


def bord(cx, cy, hw, hh, tx, ty, marge=4):
    """Point où le segment du centre (cx, cy) vers (tx, ty) sort de la boîte, plus une marge."""
    dx, dy = tx - cx, ty - cy
    t = min(hw / abs(dx) if dx else 1e9, hh / abs(dy) if dy else 1e9)
    n = (dx * dx + dy * dy) ** 0.5
    return cx + dx * t + dx / n * marge, cy + dy * t + dy / n * marge


def reseau(x0, mode):
    cx = x0 + LP / 2
    pos = [(cx + dx, CY + dy) for (dx, dy), *_ in NOEUDS]
    for a, b in ARETES:
        (xa, ya), (xb, yb) = pos[a], pos[b]
        ha, hb = boite(mode, a), boite(mode, b)
        x1, y1 = bord(xa, ya, *ha, xb, yb)
        x2, y2 = bord(xb, yb, *hb, xa, ya, marge=6)
        o.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{GRIS}" stroke-width="1.4" marker-end="url(#p)"/>')
    for k, ((x, y), (_, fr, zh, vec)) in enumerate(zip(pos, NOEUDS)):
        hw, hh = boite(mode, k)
        coul = {"zh": BRUN, "fr": TEAL, "vec": BLEU}[mode]
        o.append(f'<rect x="{x - hw:.1f}" y="{y - hh:.1f}" width="{2 * hw:.1f}" height="{2 * hh:.1f}" rx="4" fill="#ffffff" stroke="{coul}" stroke-width="1.5"/>')
        if mode == "zh":
            chinois(zh, x - largeur_zh(zh, 16) / 2, y + 6.5, 16)
        elif mode == "fr":
            o.append(f'<text x="{x:.1f}" y="{y + 4.5:.1f}" font-size="12" fill="{ENCRE}" text-anchor="middle">{fr}</text>')
        else:
            o.append(f'<text x="{x:.1f}" y="{y - 3:.1f}" font-size="10.5" fill="{ENCRE}" text-anchor="middle" font-weight="600">{fr}</text>')
            o.append(f'<text x="{x:.1f}" y="{y + 11:.1f}" font-size="9" fill="{GRIS}" text-anchor="middle" font-family="ui-monospace, Menlo, monospace">{vec}</text>')
    return pos


def monde(x0, pale=False):
    """La bande « le monde », avec un chat ; renvoie le centre du chat."""
    cx, cy = x0 + LP / 2, BANDE + 26
    op = ' opacity="0.45"' if pale else ""
    o.append(f'<g{op}>')
    o.append(f'<rect x="{x0 + 14}" y="{BANDE}" width="{LP - 28}" height="52" rx="8" fill="{FOND}" stroke="{AXE}" stroke-width="1.2"/>')
    o.append(f'<text x="{x0 + 26}" y="{BANDE + 30}" font-size="11" fill="{ENCRE_PALE}" font-style="italic">le monde</text>')
    # un chat, de face
    o.append(f'<path d="M{cx - 13} {cy - 4} L{cx - 11} {cy - 19} L{cx - 3} {cy - 11} Z M{cx + 13} {cy - 4} L{cx + 11} {cy - 19} L{cx + 3} {cy - 11} Z" fill="{PANNEAU}" stroke="{ENCRE}" stroke-width="1.6" stroke-linejoin="round"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="13" fill="{PANNEAU}" stroke="{ENCRE}" stroke-width="1.6"/>')
    o.append(f'<circle cx="{cx - 5}" cy="{cy - 2}" r="1.7" fill="{ENCRE}"/><circle cx="{cx + 5}" cy="{cy - 2}" r="1.7" fill="{ENCRE}"/>')
    o.append(f'<path d="M{cx - 2} {cy + 3} L{cx + 2} {cy + 3} L{cx} {cy + 5.5} Z" fill="{ROUGE}"/>')
    for s in (-1, 1):
        for d in (-2, 2):
            o.append(f'<line x1="{cx + s * 5}" y1="{cy + 5}" x2="{cx + s * 21}" y2="{cy + 5 + d * 1.6}" stroke="{ENCRE}" stroke-width="0.9"/>')
    o.append('</g>')
    return cx, cy


def panneau(x0, titre, coul, l1, l2):
    o.append(f'<rect x="{x0}" y="{PY}" width="{LP}" height="{PH}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
    o.append(f'<text x="{x0 + LP / 2}" y="{PY + 24}" font-size="12.5" fill="{coul}" text-anchor="middle" font-weight="700">{titre}</text>')
    o.append(f'<text x="{x0 + LP / 2}" y="{PY + PH - 34}" font-size="11.5" fill="{ENCRE}" text-anchor="middle">{l1}</text>')
    o.append(f'<text x="{x0 + LP / 2}" y="{PY + PH - 16}" font-size="11.5" fill="{ENCRE}" text-anchor="middle">{l2}</text>')


o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Le problème de l'ancrage des symboles</title>",
     "<desc>Trois panneaux, construits sur le même petit réseau de cinq mots : chat, animal, miauler, poil, compagnie, "
     "reliés par des flèches qui vont de chaque mot aux mots qui le définissent. À gauche, le dictionnaire unilingue "
     "imaginé par Stevan Harnad : les mots sont en chinois (猫, 动物, 叫, 毛, 宠物), les flèches tournent en rond, et "
     "aucune ne rejoint le monde, représenté en bas, pâli, par un chat. Au centre, un humain : le même réseau en "
     "français, mais les mots « chat » et « miauler » sont reliés directement au chat du monde, par la vue et par "
     "l'ouïe ; les autres mots se définissent à partir d'eux. À droite, un modèle de langage : chaque mot est un vecteur "
     "de nombres, défini par d'autres vecteurs ; aucun lien direct ne descend vers le monde, mais un chemin en "
     "pointillé y mène par un détour, en passant par des textes écrits par des humains, marqué d'un point "
     "d'interrogation : est-ce encore un ancrage ?</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker>'
     f'<marker id="b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{BRUN}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Le problème de l\'ancrage des symboles</text>']

X = [15, 15 + LP + 15, 15 + 2 * (LP + 15)]

# ── 1. le dictionnaire unilingue ──
panneau(X[0], "Le dictionnaire unilingue", BRUN,
        f"Chaque mot renvoie à d'autres mots{NB}:", "on tourne en rond, sans atteindre le sens.")
reseau(X[0], "zh")
monde(X[0], pale=True)
o.append(f'<text x="{X[0] + LP / 2}" y="{BANDE - 22}" font-size="11" fill="{ROUGE}" text-anchor="middle" font-weight="700">aucune flèche n\'en sort</text>')

# ── 2. l'humain ──
panneau(X[1], "Un humain", TEAL,
        f"Quelques mots s'ancrent dans la perception{NB};", "les autres se définissent à partir d'eux.")
pos = reseau(X[1], "fr")
mx, my = monde(X[1])
(xc, yc), (xm, ym) = pos[0], pos[2]
o.append(f'<line x1="{xc}" y1="{yc + 18}" x2="{mx}" y2="{my - 24}" stroke="{TEAL}" stroke-width="2.2"/>')
o.append(f'<text x="{xc - 8}" y="{(yc + my) / 2 - 2}" font-size="10.5" fill="{TEAL}" text-anchor="end" font-weight="700">voir</text>')
o.append(f'<line x1="{xm}" y1="{ym + 18}" x2="{mx + 20}" y2="{my - 14}" stroke="{TEAL}" stroke-width="2.2"/>')
o.append(f'<text x="{(xm + mx + 20) / 2 + 12}" y="{(ym + 18 + my - 14) / 2 + 4}" font-size="10.5" fill="{TEAL}" font-weight="700">entendre</text>')

# ── 3. le modèle de langage ──
panneau(X[2], "Un modèle de langage", BLEU,
        f"Des vecteurs définis par d'autres vecteurs{NB};", "le monde n'est atteint que par les textes.")
pos = reseau(X[2], "vec")
mx, my = monde(X[2])
xc, yc = pos[0]
TY = 264
o.append(f'<rect x="{xc - 58}" y="{TY}" width="116" height="36" rx="4" fill="{FOND}" stroke="{BRUN}" stroke-width="1.4" stroke-dasharray="4 3"/>')
o.append(f'<text x="{xc}" y="{TY + 15}" font-size="10.5" fill="{BRUN}" text-anchor="middle">des textes écrits</text>')
o.append(f'<text x="{xc}" y="{TY + 29}" font-size="10.5" fill="{BRUN}" text-anchor="middle">par des humains</text>')
o.append(f'<line x1="{xc}" y1="{yc + 22}" x2="{xc}" y2="{TY - 4}" stroke="{BRUN}" stroke-width="1.8" stroke-dasharray="5 4"/>')
o.append(f'<line x1="{xc}" y1="{TY + 40}" x2="{xc}" y2="{my - 24}" stroke="{BRUN}" stroke-width="1.8" stroke-dasharray="5 4"/>')
o.append(f'<text x="{xc + 72}" y="{TY + 24}" font-size="20" fill="{ROUGE}" text-anchor="middle" font-weight="700">?</text>')
o.append(f'<text x="{xc + 72}" y="{TY + 44}" font-size="10" fill="{ROUGE}" text-anchor="middle">ancrage</text>')
o.append(f'<text x="{xc + 72}" y="{TY + 57}" font-size="10" fill="{ROUGE}" text-anchor="middle">emprunté</text>')

o.append("</svg>")
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(o) + "\n")
print(OUT.name, "écrit")
