"""Module 4, « Des images, des voix, des vidéos » : la même phrase, de 2015 à 2025.

« A stop sign is flying in blue skies », la consigne d'alignDRAW (Mansimov et al., Université de Toronto,
2015), rendue par quatre générateurs. Images de Wikimedia Commons, conservées dans scripts/data/chronologie/ :
AlignDRAW - Flying stop sign.png (domaine public) ; Image generator-A stop sign is flying in blue skies-Dall-e2-01
et -Dall-e3-01 (Yug, CC BY-SA 4.0) ; A stop sign is flying in blue skies (GPT Image 1) (domaine public).
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

RACINE = Path(__file__).resolve().parent
SOURCE = RACINE / "data" / "chronologie"
FOND, BORD, ENCRE, PALE, TEAL = "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#2f6f6a"
police = lambda t, gras=False: ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", t, index=1 if gras else 0)
c, e, x0, y0 = 300, 18, 40, 100
W = 2 * x0 + 4 * c + 3 * e
H = y0 + c + 130
im = Image.new("RGB", (W, H), FOND)
d = ImageDraw.Draw(im)
d.rounded_rectangle((1, 1, W - 2, H - 2), radius=24, outline=BORD, width=2)
d.text((W / 2, 46), "« A stop sign is flying in blue skies », de 2015 à 2025", fill=ENCRE, font=police(30, True), anchor="mm")


def carre(v):
    s = min(v.size)
    return v.crop(((v.width - s) // 2, (v.height - s) // 2, (v.width + s) // 2, (v.height + s) // 2))


# alignDRAW : huit vignettes d'environ 32 pixels, rangées 4 × 2 ; on en garde quatre, agrandies sans lissage
a = Image.open(SOURCE / "stop-2015-aligndraw.png").convert("RGB")
grille = Image.new("RGB", (c, c), FOND)            # 134 × 66 : vignettes de 32 pixels, séparées par 2 pixels
for k in range(4):
    v = a.crop((k * 34, 0, k * 34 + 32, 32))
    grille.paste(v.resize((c // 2 - 4, c // 2 - 4), Image.NEAREST), ((k % 2) * (c // 2) + 2, (k // 2) * (c // 2) + 2))
panneaux = [(grille, "alignDRAW (2015)"),
            (carre(Image.open(SOURCE / "stop-2022-dalle2.jpg").convert("RGB")).resize((c, c), Image.LANCZOS), "DALL·E 2 (2022)"),
            (carre(Image.open(SOURCE / "stop-2023-dalle3.jpg").convert("RGB")).resize((c, c), Image.LANCZOS), "DALL·E 3 (2023)"),
            (carre(Image.open(SOURCE / "stop-2025-gptimage1.jpg").convert("RGB")).resize((c, c), Image.LANCZOS), "GPT Image 1 (2025)")]
for k, (v, legende) in enumerate(panneaux):
    x = x0 + k * (c + e)
    im.paste(v, (x, y0))
    d.rectangle((x - 1, y0 - 1, x + c, y0 + c), outline=BORD, width=2)
    d.text((x + c / 2, y0 + c + 30), legende, fill=TEAL, font=police(23, True), anchor="mm")
d.text((W / 2, H - 50), "alignDRAW et GPT Image 1 : Wikimedia Commons, domaine public. DALL·E 2 et DALL·E 3 : Yug, Wikimedia Commons, CC BY-SA 4.0.",
       fill=PALE, font=police(18), anchor="mm")
d.text((W / 2, H - 26), "Cette figure est diffusée sous la même licence CC BY-SA 4.0.", fill=PALE, font=police(18), anchor="mm")
im.save(RACINE.parent / "static" / "images" / "module4" / "panneau-stop.jpg", quality=88)
print("panneau-stop.jpg écrit", im.size)
