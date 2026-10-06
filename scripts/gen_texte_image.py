"""Module 4, « Mots et images » : le fonctionnement de Stable Diffusion, en un schéma.

L'image finale est celle de gen_stable_diffusion_etapes.py (dernier panneau de stable-diffusion-etapes.jpg). Les deux
petites grilles de l'espace latent sont des illustrations : du bruit, puis une version très réduite de l'image finale.

    uv run --with numpy --with pillow python scripts/gen_texte_image.py
"""
import base64, io
from pathlib import Path
import numpy as np
from PIL import Image

RACINE = Path(__file__).resolve().parent
OUT = RACINE.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "

bande = Image.open(OUT / "stable-diffusion-etapes.jpg")
C, M, E = 300, 40, 24                                         # mise en page de la bande (voir gen_stable_diffusion_etapes.py)
x = M + 4 * (C + E)
finale = bande.crop((x, 96, x + C, 96 + C))


def url(im, taille, fmt="JPEG"):
    buf = io.BytesIO(); im.resize((taille, taille), Image.LANCZOS if taille > im.width else Image.BOX).save(buf, fmt, quality=88)
    return f"data:image/{fmt.lower()};base64," + base64.b64encode(buf.getvalue()).decode()


rng = np.random.default_rng(1)
bruit = Image.fromarray((rng.random((16, 16, 3)) * 255).astype(np.uint8)).resize((70, 70), Image.NEAREST)
grille = finale.resize((16, 16), Image.BOX).resize((70, 70), Image.NEAREST)

W, H = 820, 392
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Comment Stable Diffusion produit une image</title>",
     "<desc>Un schéma. En haut, la consigne « un chat astronaute sur la lune » entre dans l'encodeur de textes de CLIP, qui en fait "
     "six vecteurs, un par mot. En bas, de gauche à droite : une petite grille de bruit dans l'espace latent, de 16 384 nombres ; le "
     "débruiteur, appliqué cinquante fois, qui consulte les vecteurs des mots par attention croisée ; la grille débruitée, toujours "
     "dans l'espace latent ; le décodeur de l'autoencodeur ; et l'image finale de 512 sur 512 pixels, soit 786 432 nombres, qui "
     "montre un chat en combinaison spatiale sur la Lune.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker>'
     f'<marker id="pr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{ROUGE}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Comment Stable Diffusion produit une image</text>']


def fleche(x1, y1, x2, y2, coul=GRIS, m="p", l=1.6, op=1):
    o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{coul}" stroke-width="{l}" stroke-opacity="{op}" marker-end="url(#{m})"/>')


def legende(xc, y, lignes, coul=ENCRE_PALE, gras=None):
    for k, l in enumerate(lignes):
        g = ' font-weight="700"' if gras == k else ""
        o.append(f'<text x="{xc}" y="{y + 14 * k}" font-size="11" fill="{coul}" text-anchor="middle"{g}>{l}</text>')


# ── la consigne et l'encodeur de textes, au-dessus du débruiteur ──
XB0, XB1 = 150, 380                                           # le débruiteur
xc = (XB0 + XB1) / 2
o.append(f'<text x="{xc}" y="66" font-size="13" fill="{ENCRE}" text-anchor="middle" font-style="italic">«{NB}un chat astronaute sur la lune{NB}»</text>')
fleche(xc, 74, xc, 88)
o.append(f'<rect x="{xc - 95}" y="90" width="190" height="30" rx="7" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="1.8"/>')
o.append(f'<text x="{xc}" y="110" font-size="11.5" fill="{ENCRE}" text-anchor="middle" font-weight="600">encodeur de textes (CLIP)</text>')
mots = ["un", "chat", "astronaute", "sur", "la", "lune"]
xs = [xc + (k - 2.5) * 48 for k in range(len(mots))]
for k, (m, xm) in enumerate(zip(mots, xs)):
    fleche(xc + (k - 2.5) * 20, 121, xm, 129, AXE, "p", 1)
    for j in range(5):
        v = rng.random()
        o.append(f'<rect x="{xm - 5}" y="{132 + j * 6}" width="10" height="5.5" fill="{TEAL}" fill-opacity="{0.25 + 0.7 * v:.2f}"/>')
    o.append(f'<text x="{xm}" y="176" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">{m}</text>')
o.append(f'<text x="{xs[-1] + 26}" y="152" font-size="10.5" fill="{ENCRE_PALE}">un vecteur</text>')
o.append(f'<text x="{xs[-1] + 26}" y="165" font-size="10.5" fill="{ENCRE_PALE}">par mot</text>')
# attention croisée : des mots vers le débruiteur
for k, xm in enumerate(xs):
    fort = mots[k] in ("astronaute", "chat", "lune")
    fleche(xm, 182, xc + (xm - xc) * 0.55, 220, ROUGE, "pr", 2 if fort else 1.1, 1 if fort else 0.55)
o.append(f'<text x="{XB0 - 8}" y="204" font-size="11" fill="{ROUGE}" text-anchor="end" font-weight="600">attention croisée</text>')

# ── la chaîne du bas ──
yc = 262
def carre(x, im, haut, bas):
    o.append(f'<image x="{x}" y="{yc - 35}" width="70" height="70" xlink:href="{url(im, 70, "PNG")}"/>')
    o.append(f'<rect x="{x}" y="{yc - 35}" width="70" height="70" fill="none" stroke="{AXE}" stroke-width="1.2"/>')
    legende(x + 35, yc + 52, [haut, bas], gras=1)


carre(40, bruit, "bruit de départ", f"16{FINE}384{NB}nombres")
fleche(114, yc, XB0 - 4, yc)
o.append(f'<rect x="{XB0}" y="{yc - 34}" width="{XB1 - XB0}" height="68" rx="8" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="1.8"/>')
o.append(f'<text x="{xc}" y="{yc - 6}" font-size="13" fill="{ENCRE}" text-anchor="middle" font-weight="700">débruiteur</text>')
o.append(f'<text x="{xc}" y="{yc + 13}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">retire un peu de bruit, 50{NB}fois de suite</text>')
o.append(f'<path d="M{XB1 - 30} {yc + 34} q 0 22 -{(XB1 - XB0) / 2 - 30} 22 q -{(XB1 - XB0) / 2 - 30} 0 -{(XB1 - XB0) / 2 - 30} -20" fill="none" stroke="{GRIS}" stroke-width="1.4" marker-end="url(#p)"/>')
o.append(f'<text x="{xc}" y="{yc + 72}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">×{NB}50</text>')
fleche(XB1 + 4, yc, 408, yc)
carre(412, grille, "grille débruitée", f"16{FINE}384{NB}nombres")
fleche(486, yc, 500, yc)
o.append(f'<polygon points="504,{yc - 16} 584,{yc - 70} 584,{yc + 70} 504,{yc + 16}" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="1.8"/>')
o.append(f'<text x="546" y="{yc + 4}" font-size="11.5" fill="{ENCRE}" text-anchor="middle" font-weight="600">décodeur</text>')
fleche(588, yc, 602, yc)
o.append(f'<image x="606" y="{yc - 85}" width="170" height="170" xlink:href="{url(finale, 340)}"/>')
o.append(f'<rect x="606" y="{yc - 85}" width="170" height="170" fill="none" stroke="{BORD}" stroke-width="1.5"/>')
legende(691, yc + 102, [f"image de 512{NB}×{NB}512{NB}pixels", f"786{FINE}432{NB}nombres"], gras=1)
# l'espace latent, en arrière-plan de la chaîne
o.append(f'<text x="261" y="{yc + 98}" font-size="10.5" fill="{GRIS}" text-anchor="middle">tout se passe dans l\'espace latent, 48{NB}fois plus petit que l\'image</text>')
o.append("</svg>")
(OUT / "texte-image.svg").write_text("\n".join(o) + "\n")
print("texte-image.svg écrit")
