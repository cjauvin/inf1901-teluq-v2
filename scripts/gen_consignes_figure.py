"""Module 4, « Quatre façons de générer » : trois sortes de consignes pour un générateur, en trois rangées.

Images reprises : le 7 de generation-conditionnelle.svg (gen_generation_conditionnelle.py), le dessin et le tableau de
gen_consignes.py, le chat astronaute de stable-diffusion-etapes.jpg (gen_stable_diffusion_etapes.py).

    uv run --with pillow python scripts/gen_consignes_figure.py
"""
import base64, io, re
from pathlib import Path
from PIL import Image

RACINE = Path(__file__).resolve().parent
OUT = RACINE.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "


def url(im, taille):
    buf = io.BytesIO(); im.convert("RGB").resize((taille, taille), Image.LANCZOS).save(buf, "JPEG", quality=88)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


svg = (OUT / "generation-conditionnelle.svg").read_text()
sept = re.search(r'<image x="330"[^>]*xlink:href="(data:image/png;base64,[^"]+)"', svg).group(1)
sept = Image.open(io.BytesIO(base64.b64decode(sept.split(",", 1)[1])))
dessin = Image.open(OUT / "consigne-image-dessin.png")
tableau = Image.open(OUT / "consigne-image-tableau.jpg")
bande = Image.open(OUT / "stable-diffusion-etapes.jpg")
C, M, E = 300, 40, 24
x = M + 4 * (C + E)
chat = bande.crop((x, 96, x + C, 96 + C))

W, H = 780, 520
XC, XT0, XT1, XG0, XG1, XR = 30, 222, 382, 418, 568, 604     # consigne, traduction, générateur, résultat
TI = 118
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Trois sortes de consignes</title>",
     "<desc>Trois rangées, de gauche à droite : la consigne, sa traduction en nombres, le générateur qui reçoit aussi du hasard, "
     "et le résultat. Première rangée : une étiquette, « 7 », devient un code de dix cases dont une seule est allumée ; un VAE "
     "conditionnel produit un 7 manuscrit. Deuxième rangée : une image de départ, un dessin d'enfant d'une maison sous le soleil, "
     "est déjà faite de nombres ; un modèle de diffusion en fait un tableau qui reprend sa composition. Troisième rangée : une "
     "phrase, « un chat astronaute sur la lune », passe par un encodeur de textes, l'étape difficile, qui doit représenter le sens "
     "de la phrase ; un modèle de diffusion produit un chat en scaphandre sur la Lune.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Une consigne, traduite en nombres, guide le générateur</text>']
for xc, t in ((XC + 85, "la consigne"), ((XT0 + XT1) / 2, "traduite en nombres"), ((XG0 + XG1) / 2, "générateur, plus le hasard"), (XR + TI / 2, "le résultat")):
    o.append(f'<text x="{xc}" y="66" font-size="12" fill="{BRUN}" text-anchor="middle" font-weight="700">{t}</text>')


def fleche(x1, y1, x2, y2):
    o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')


def boite(x0, x1, yc, lignes, coul, fond=PANNEAU, l=1.6):
    h = 18 + 15 * len(lignes)
    o.append(f'<rect x="{x0}" y="{yc - h / 2}" width="{x1 - x0}" height="{h}" rx="7" fill="{fond}" stroke="{coul}" stroke-width="{l}"/>')
    for k, (txt, style) in enumerate(lignes):
        y = yc - h / 2 + 22 + 15 * k
        o.append(f'<text x="{(x0 + x1) / 2}" y="{y}" font-size="{11.5 if k == 0 else 10.5}" fill="{ENCRE if k == 0 else ENCRE_PALE}" text-anchor="middle"{style}>{txt}</text>')


def image(x, yc, im, taille=TI):
    o.append(f'<image x="{x}" y="{yc - taille / 2}" width="{taille}" height="{taille}" xlink:href="{url(im, taille * 2)}"/>')
    o.append(f'<rect x="{x}" y="{yc - taille / 2}" width="{taille}" height="{taille}" fill="none" stroke="{BORD}" stroke-width="1.5"/>')


def rangee(yc, nom):
    o.append(f'<text x="{XC}" y="{yc - TI / 2 + 4}" font-size="11.5" fill="{ROUGE}" font-weight="700">{nom}</text>')


ys = [146, 286, 426]
G = ' font-weight="700"'
# 1. une étiquette
yc = ys[0]
rangee(yc, "une étiquette")
o.append(f'<text x="{XC + 85}" y="{yc + 18}" font-size="40" fill="{ENCRE}" text-anchor="middle" font-weight="700">«{NB}7{NB}»</text>')
fleche(XC + 175, yc, XT0 - 4, yc)
for k in range(10):
    o.append(f'<rect x="{XT0 + 6 + k * 15}" y="{yc - 22}" width="13" height="13" fill="{TEAL if k == 7 else PANNEAU}" stroke="{TEAL}" stroke-width="1"/>')
    o.append(f'<text x="{XT0 + 12.5 + k * 15}" y="{yc + 4}" font-size="9" fill="{ENCRE_PALE}" text-anchor="middle">{k}</text>')
o.append(f'<text x="{(XT0 + XT1) / 2}" y="{yc + 24}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">dix cases, une seule allumée</text>')
fleche(XT1 + 4, yc, XG0 - 4, yc)
boite(XG0, XG1, yc, [("VAE conditionnel", G), (f"+{NB}hasard", "")], TEAL)
fleche(XG1 + 4, yc, XR - 4, yc)
image(XR, yc, sept)
# 2. une image de départ
yc = ys[1]
rangee(yc, "une image de départ")
image(XC + 26, yc + 8, dessin, 104)
fleche(XC + 175, yc, XT0 - 4, yc)
o.append(f'<text x="{(XT0 + XT1) / 2}" y="{yc - 4}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">une image est déjà</text>')
o.append(f'<text x="{(XT0 + XT1) / 2}" y="{yc + 11}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">faite de nombres (ses pixels)</text>')
fleche(XT1 + 4, yc, XG0 - 4, yc)
boite(XG0, XG1, yc, [("modèle de diffusion", G), (f"+{NB}hasard", "")], TEAL)
fleche(XG1 + 4, yc, XR - 4, yc)
image(XR, yc, tableau)
# 3. une phrase
yc = ys[2]
rangee(yc, "une phrase")
o.append(f'<text x="{XC + 85}" y="{yc + 2}" font-size="12.5" fill="{ENCRE}" text-anchor="middle" font-style="italic">«{NB}un chat astronaute</text>')
o.append(f'<text x="{XC + 85}" y="{yc + 19}" font-size="12.5" fill="{ENCRE}" text-anchor="middle" font-style="italic">sur la lune{NB}»</text>')
fleche(XC + 175, yc, XT0 - 4, yc)
boite(XT0, XT1, yc, [("encodeur de textes", G), (f"l'étape difficile{NB}:", ""), ("représenter le sens", "")], ROUGE, l=2.2)
fleche(XT1 + 4, yc, XG0 - 4, yc)
boite(XG0, XG1, yc, [("modèle de diffusion", G), (f"+{NB}hasard", "")], TEAL)
fleche(XG1 + 4, yc, XR - 4, yc)
image(XR, yc, chat)
o.append("</svg>")
(OUT / "trois-consignes.svg").write_text("\n".join(o) + "\n")
print("trois-consignes.svg écrit")
