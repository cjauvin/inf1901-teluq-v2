# /// script
# requires-python = ">=3.10"
# ///
"""Module 5, « Une machine peut-elle penser ? » : l'hypothèse de la représentation platonicienne (Huh, Cheung, Wang
et Isola, 2024). À gauche, le monde ; au centre, ses ombres, une image et une phrase ; à droite, ce qu'en tirent un
modèle de vision et un modèle de langage, entraînés séparément : deux nuages de concepts dont les voisinages se
ressemblent. Positions schématiques."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module5" / "caverne-platonicienne.svg"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "

W, H = 920, 470
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>L'hypothèse de la représentation platonicienne</title>",
     "<desc>Trois colonnes. À gauche, le monde, représenté par un chat. Au centre, ses ombres, les seules données que "
     "voient les modèles : une photo du chat et une phrase, « Un chat dort au soleil ». À droite, ce qu'en tire chaque "
     "modèle, entraîné séparément : un modèle de vision, qui n'a vu que des images, et un modèle de langage, qui n'a lu "
     "que des textes. Chacun place six concepts dans son espace de représentation : chat, chien et lion d'un côté, "
     "voiture et vélo d'un autre, pomme à part. Les deux nuages sont disposés différemment, mais les voisinages sont "
     "les mêmes. Une double flèche entre eux demande si ces voisinages sont semblables.</desc>",
     '<defs>' + "".join(
         f'<marker id="{n}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto-start-reverse">'
         f'<path d="M0 0 L10 5 L0 10 z" fill="{c}"/></marker>' for n, c in (("g", GRIS), ("t", TEAL))) + '</defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Des ombres différentes, une même structure{NB}?</text>']


def texte(x, y, t, taille=10.5, coul=ENCRE, ancre="middle", gras=False, ital=False):
    g = ' font-weight="700"' if gras else ""
    i = ' font-style="italic"' if ital else ""
    o.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{taille}" fill="{coul}" text-anchor="{ancre}"{g}{i}>{t}</text>')


def chat(cx, cy, s, coul, op=1.0):
    """Silhouette de chat assis, centrée sur (cx, cy), d'échelle s."""
    f = f'fill="{coul}" fill-opacity="{op}"'
    o.append(f'<ellipse cx="{cx:.1f}" cy="{cy + 14 * s:.1f}" rx="{20 * s:.1f}" ry="{24 * s:.1f}" {f}/>')
    o.append(f'<circle cx="{cx:.1f}" cy="{cy - 18 * s:.1f}" r="{13 * s:.1f}" {f}/>')
    for d in (-1, 1):
        o.append(f'<polygon points="{cx + d * 4 * s:.1f},{cy - 27 * s:.1f} {cx + d * 13 * s:.1f},{cy - 40 * s:.1f} '
                 f'{cx + d * 13 * s:.1f},{cy - 22 * s:.1f}" {f}/>')
    o.append(f'<path d="M{cx + 16 * s:.1f} {cy + 32 * s:.1f} Q{cx + 42 * s:.1f} {cy + 30 * s:.1f} {cx + 34 * s:.1f} '
             f'{cy + 4 * s:.1f}" fill="none" stroke="{coul}" stroke-opacity="{op}" stroke-width="{5 * s:.1f}" stroke-linecap="round"/>')


def fleche(x1, y1, x2, y2, m="g", coul=GRIS, pointille=False):
    d = ' stroke-dasharray="5 4"' if pointille else ""
    o.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{coul}" stroke-width="1.6"{d} marker-end="url(#{m})"/>')


# ── en-têtes de colonnes ──
for x, t in ((125, "Le monde"), (345, "Ses ombres : les données"), (690, "Ce qu'en tire chaque modèle")):
    texte(x, 66, t, 12, ENCRE, gras=True)

# ── le monde ──
o.append(f'<rect x="30" y="80" width="190" height="360" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
chat(118, 250, 1.6, ENCRE)
texte(125, 360, "hors de la caverne,", 10.5, ENCRE_PALE, ital=True)
texte(125, 375, "aucun modèle n'y accède", 10.5, ENCRE_PALE, ital=True)

# ── les ombres ──
o.append(f'<rect x="250" y="80" width="190" height="360" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
o.append(f'<rect x="290" y="105" width="110" height="80" rx="3" fill="{FOND}" stroke="{GRIS}" stroke-width="1.2"/>')
chat(338, 145, 0.62, GRIS, 0.75)
texte(345, 205, "une image", 10.5, BLEU, gras=True)
o.append(f'<rect x="270" y="290" width="150" height="46" rx="3" fill="{FOND}" stroke="{GRIS}" stroke-width="1.2"/>')
texte(345, 318, "« Un chat dort au soleil. »", 10.5, ENCRE, ital=True)
texte(345, 356, "un texte", 10.5, BRUN, gras=True)
fleche(196, 205, 284, 155)
fleche(198, 296, 264, 312)

# ── les deux modèles : mêmes voisinages, disposition différente ──
GROUPE = {"chat": TEAL, "chien": TEAL, "lion": TEAL, "voiture": ROUGE, "vélo": ROUGE, "pomme": BRUN}
VISION = [("lion", 240, 42, "haut"), ("chat", 278, 76, "d"), ("chien", 228, 110, "g"),
          ("voiture", 318, 124, "g"), ("vélo", 366, 98, "d"), ("pomme", 362, 42, "d")]
LANGAGE = [("lion", 228, 58, "g"), ("chat", 268, 44, "haut"), ("chien", 288, 90, "d"),
           ("voiture", 236, 128, "g"), ("vélo", 280, 136, "d"), ("pomme", 360, 108, "d")]


def nuage(x0, y0, w, h, points, coul_titre, titre, sous_titre):
    o.append(f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
    texte(x0 + 16, y0 + 24, titre, 11.5, coul_titre, "start", gras=True)
    texte(x0 + 16, y0 + 40, sous_titre, 10, ENCRE_PALE, "start", ital=True)
    pts = {nom: (x0 + dx, y0 + dy) for nom, dx, dy, _ in points}
    for a_, b_ in (("chat", "chien"), ("chat", "lion"), ("chien", "lion"), ("voiture", "vélo")):
        (x1, y1), (x2, y2) = pts[a_], pts[b_]
        o.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{AXE}" stroke-width="1.2" stroke-dasharray="3 3"/>')
    for nom, dx, dy, cote in points:
        x, y = pts[nom]
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{GROUPE[nom]}" stroke="#ffffff" stroke-width="1.2"/>')
        if cote == "haut":
            texte(x, y - 10, nom, 10, ENCRE)
        elif cote == "d":
            texte(x + 10, y + 4, nom, 10, ENCRE, "start")
        else:
            texte(x - 10, y + 4, nom, 10, ENCRE, "end")


nuage(470, 80, 420, 160, VISION, BLEU, "Modèle de vision", "n'a vu que des images")
nuage(470, 280, 420, 160, LANGAGE, BRUN, "Modèle de langage", "n'a lu que des textes")
fleche(400, 145, 466, 150)
fleche(420, 313, 466, 330)
# double flèche entre les deux nuages
o.append(f'<line x1="760" y1="246" x2="760" y2="274" stroke="{TEAL}" stroke-width="1.6" marker-start="url(#t)" marker-end="url(#t)"/>')
texte(748, 264, f"des voisinages semblables{NB}?", 10.5, TEAL, "end", gras=True)
o.append("</svg>")
OUT.write_text("\n".join(o) + "\n")
print(OUT.name, "écrit")
