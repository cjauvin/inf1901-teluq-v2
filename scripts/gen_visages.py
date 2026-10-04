"""Module 4, « Générer : imiter une distribution » : quatre visages de personnes qui n'existent pas.

Images produites par StyleGAN et StyleGAN2 (réseaux antagonistes génératifs), Wikimedia Commons,
domaine public : Woman 1.jpg, Man 2.jpg, Boy 1.jpg (Owlsmcgee) et This Person Does Not Exist
example.jpg ; conservées dans scripts/data/visages/.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

RACINE = Path(__file__).resolve().parent
FOND, BORD, ENCRE, PALE = "#efe7d3", "#d9cbac", "#3a3531", "#5b5249"
police = lambda t, gras=False: ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", t, index=1 if gras else 0)
c, e, x0, y0 = 300, 16, 40, 96
W = 2 * x0 + 4 * c + 3 * e
H = y0 + c + 76
im = Image.new("RGB", (W, H), FOND)
d = ImageDraw.Draw(im)
d.rounded_rectangle((1, 1, W - 2, H - 2), radius=24, outline=BORD, width=2)
d.text((W / 2, 46), "Aucune de ces personnes n'existe", fill=ENCRE, font=police(30, True), anchor="mm")
for k in range(4):
    v = Image.open(RACINE / "data" / "visages" / f"visage-{k + 1}.jpg").convert("RGB")
    s = min(v.size)
    v = v.crop(((v.width - s) // 2, (v.height - s) // 2, (v.width + s) // 2, (v.height + s) // 2)).resize((c, c), Image.LANCZOS)
    x = x0 + k * (c + e)
    im.paste(v, (x, y0))
    d.rectangle((x - 1, y0 - 1, x + c, y0 + c), outline=BORD, width=2)
d.text((W / 2, H - 34), "Visages produits par StyleGAN (2019) et StyleGAN2 (2020). Wikimedia Commons, domaine public.",
       fill=PALE, font=police(20), anchor="mm")
im.save(RACINE.parent / "static" / "images" / "module4" / "visages-stylegan.jpg", quality=86)
print("visages-stylegan.jpg écrit", im.size)
