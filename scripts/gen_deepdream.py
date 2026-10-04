"""Module 3, « L'apprentissage profond » : une photo de méduses transformée par DeepDream.

Images de Martin Thoma sur Wikimedia Commons, domaine public (CC0) : Aurelia-aurita-3.jpg (la photo d'origine) et
Aurelia-aurita-3-0009, -0049, -0099 (après 10, 50 et 100 itérations de DeepDream), conservées dans scripts/data/deepdream/.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

RACINE = Path(__file__).resolve().parent
SOURCE = RACINE / "data" / "deepdream"
FOND, BORD, ENCRE, PALE, TEAL = "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#2f6f6a"
police = lambda t, gras=False: ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", t, index=1 if gras else 0)
images = [("meduse-origine.jpg", "la photo d'origine"), ("meduse-0009.jpg", "après 10 itérations"),
          ("meduse-0049.jpg", "après 50 itérations"), ("meduse-0099.jpg", "après 100 itérations")]
l, h, e, x0, y0 = 300, 225, 16, 40, 96
W = 2 * x0 + 4 * l + 3 * e
H = y0 + h + 110
im = Image.new("RGB", (W, H), FOND)
d = ImageDraw.Draw(im)
d.rounded_rectangle((1, 1, W - 2, H - 2), radius=24, outline=BORD, width=2)
d.text((W / 2, 46), "DeepDream : le réseau renforce ce qu'il croit voir", fill=ENCRE, font=police(30, True), anchor="mm")
for k, (f, legende) in enumerate(images):
    v = Image.open(SOURCE / f).convert("RGB")
    r = max(l / v.width, h / v.height)                 # recadrage centré au format l × h
    v = v.resize((round(v.width * r), round(v.height * r)), Image.LANCZOS)
    gx, gy = (v.width - l) // 2, (v.height - h) // 2
    v = v.crop((gx, gy, gx + l, gy + h))
    x = x0 + k * (l + e)
    im.paste(v, (x, y0))
    d.rectangle((x - 1, y0 - 1, x + l, y0 + h), outline=BORD, width=2)
    d.text((x + l / 2, y0 + h + 30), legende, fill=TEAL if k else PALE, font=police(23, True), anchor="mm")
d.text((W / 2, H - 28), "Images de Martin Thoma, Wikimedia Commons, domaine public (CC0).", fill=PALE, font=police(20), anchor="mm")
im.save(RACINE.parent / "static" / "images" / "module3" / "deepdream-meduses.jpg", quality=86)
print("deepdream-meduses.jpg écrit", im.size)
