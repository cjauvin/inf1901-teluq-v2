"""Module 3, « L'apprentissage profond » : les trois lauréats du prix Turing 2018.

Aucune photo libre des trois ensemble n'existe sur Wikimedia Commons ; la figure réunit trois portraits
(scripts/data/turing/) : Geoffrey Hinton en 2023 (Ramsey Cardy / Collision via Sportsfile, CC BY 2.0),
Yoshua Bengio en 2019 (Maryse Boyce, CC BY 4.0), Yann Le Cun en 2018 (Jérémy Barande, CC BY-SA 2.0).

    uv run --with pillow python scripts/gen_turing.py
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

RACINE = Path(__file__).resolve().parent
FOND, BORD, ENCRE, PALE, TEAL = "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#2f6f6a"
police = lambda t, gras=False: ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", t, index=1 if gras else 0)
PORTRAITS = [("hinton.jpg", "Geoffrey Hinton", "Université de Toronto"),
             ("bengio.jpg", "Yoshua Bengio", "Université de Montréal"),
             ("lecun.jpg", "Yann Le Cun", "Université de New York")]
l, h, e, x0, y0 = 300, 360, 22, 40, 96
W = 2 * x0 + 3 * l + 2 * e
H = y0 + h + 130
im = Image.new("RGB", (W, H), FOND)
d = ImageDraw.Draw(im)
d.rounded_rectangle((1, 1, W - 2, H - 2), radius=24, outline=BORD, width=2)
d.text((W / 2, 46), "Les lauréats du prix Turing 2018", fill=ENCRE, font=police(30, True), anchor="mm")
for k, (f, nom, lieu) in enumerate(PORTRAITS):
    v = Image.open(RACINE / "data" / "turing" / f).convert("RGB")
    r = max(l / v.width, h / v.height)                 # recadrage centré, en gardant le haut du visage
    v = v.resize((round(v.width * r), round(v.height * r)), Image.LANCZOS)
    gx = (v.width - l) // 2
    gy = min((v.height - h) // 4, v.height - h)
    v = v.crop((gx, gy, gx + l, gy + h))
    x = x0 + k * (l + e)
    im.paste(v, (x, y0))
    d.rectangle((x - 1, y0 - 1, x + l, y0 + h), outline=BORD, width=2)
    d.text((x + l / 2, y0 + h + 30), nom, fill=TEAL, font=police(24, True), anchor="mm")
    d.text((x + l / 2, y0 + h + 58), lieu, fill=PALE, font=police(19), anchor="mm")
d.text((W / 2, H - 22), "Photos : Ramsey Cardy / Collision via Sportsfile (CC BY 2.0), Maryse Boyce (CC BY 4.0), "
       "Jérémy Barande (CC BY-SA 2.0), Wikimedia Commons.", fill=PALE, font=police(15), anchor="mm")
im.save(RACINE.parent / "static" / "images" / "module3" / "laureats-turing-2018.jpg", quality=88)
print("laureats-turing-2018.jpg écrit", im.size)
