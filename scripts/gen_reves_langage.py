"""Module 4, « Des règles aux probabilités » : deux rêves anciens, en un panneau.

À gauche, le panneau de HAL 9000 (2001 : l'odyssée de l'espace), dessin de Tom Cowap, Wikimedia Commons, CC BY-SA 4.0
(File:Hal_9000_Panel.svg, rendu en PNG par rsvg-convert). À droite, La Tour de Babel de Pieter Bruegel l'Ancien (1563),
domaine public, Wikimedia Commons.

    rsvg-convert -h 1240 Hal_9000_Panel.svg -o hal-9000-panneau.png
    uv run --with pillow python scripts/gen_reves_langage.py hal-9000-panneau.png
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

RACINE = Path(__file__).resolve().parent
OUT = RACINE.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, PALE = "#efe7d3", "#d9cbac", "#3a3531", "#5b5249"
police = lambda t, gras=False, ital=False: ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", t, index=1 if gras else (2 if ital else 0))

hal = Image.open(sys.argv[1]).convert("RGBA")
babel = Image.open(OUT / "tour-de-babel.jpg").convert("RGB")
HI = 640                                                       # hauteur commune des deux images
hal = hal.resize((round(HI * hal.width / hal.height), HI), Image.LANCZOS)
babel = babel.resize((round(HI * babel.width / babel.height), HI), Image.LANCZOS)
M, G, Y0 = 44, 44, 104
W, H = 2 * M + hal.width + G + babel.width, Y0 + HI + 124
im = Image.new("RGB", (W, H), FOND)
dr = ImageDraw.Draw(im)
dr.rounded_rectangle((1, 1, W - 2, H - 2), radius=26, outline=BORD, width=2)
dr.text((W / 2, 52), "Deux rêves anciens : parler avec une machine, comprendre toutes les langues", fill=ENCRE, font=police(28, True), anchor="mm")
for x, img in ((M, hal), (M + hal.width + G, babel)):
    im.paste(img, (x, Y0), img if img.mode == "RGBA" else None)
    dr.rectangle((x - 1, Y0 - 1, x + img.width, Y0 + img.height), outline=BORD, width=2)
xb = M + hal.width + G
dr.text((M + hal.width / 2, Y0 + HI + 36), "HAL 9000", fill=ENCRE, font=police(26, True), anchor="mm")
dr.text((M + hal.width / 2, Y0 + HI + 68), "2001 : l'odyssée", fill=PALE, font=police(22), anchor="mm")
dr.text((M + hal.width / 2, Y0 + HI + 96), "de l'espace (1968)", fill=PALE, font=police(22), anchor="mm")
dr.text((xb + babel.width / 2, Y0 + HI + 36), "La Tour de Babel", fill=ENCRE, font=police(26, True), anchor="mm")
dr.text((xb + babel.width / 2, Y0 + HI + 68), "Pieter Bruegel l'Ancien (1563)", fill=PALE, font=police(22), anchor="mm")
im.save(OUT / "reves-langage.jpg", quality=86)
print("reves-langage.jpg écrit", im.size)
