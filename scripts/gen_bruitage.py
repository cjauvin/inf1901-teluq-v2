"""Module 4, « Quatre façons de générer » : un visage de plus en plus bruité, comme dans un modèle de diffusion.

Le visage est l'un des visages StyleGAN de la page précédente (scripts/data/visages/visage-1.jpg, domaine
public). Le bruit suit le calendrier du modèle de diffusion de Ho, Jain et Abbeel (2020) : 1 000 étapes,
x_t = √ᾱ_t · x_0 + √(1 − ᾱ_t) · ε, avec β croissant de 0,0001 à 0,02.
"""
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont

RACINE = Path(__file__).resolve().parent
FOND, BORD, ENCRE, PALE, TEAL, BRUN = "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#2f6f6a", "#9a5b33"
police = lambda t, gras=False: ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", t, index=1 if gras else 0)
abar = np.cumprod(1 - np.linspace(1e-4, 0.02, 1000))
ETAPES = [0, 60, 180, 400, 1000]
c, e, x0, y0 = 220, 28, 40, 156
v = Image.open(RACINE / "data" / "visages" / "visage-1.jpg").convert("RGB")
s = min(v.size)
v = v.crop(((v.width - s) // 2, (v.height - s) // 2, (v.width + s) // 2, (v.height + s) // 2)).resize((c, c), Image.LANCZOS)
x = np.asarray(v).astype(float) / 127.5 - 1
rng = np.random.default_rng(1)
eps = rng.standard_normal(x.shape)
W = 2 * x0 + 5 * c + 4 * e
H = y0 + c + 150
im = Image.new("RGB", (W, H), FOND)
d = ImageDraw.Draw(im)
d.rounded_rectangle((1, 1, W - 2, H - 2), radius=24, outline=BORD, width=2)
d.text((W / 2, 44), "Brouiller une image, puis apprendre à la débrouiller", fill=ENCRE, font=police(30, True), anchor="mm")
for k, t in enumerate(ETAPES):
    a = abar[t - 1] if t else 1.0
    xt = np.sqrt(a) * x + np.sqrt(1 - a) * eps
    p = Image.fromarray(((xt.clip(-1, 1) + 1) * 127.5).astype(np.uint8))
    xx = x0 + k * (c + e)
    im.paste(p, (xx, y0))
    d.rectangle((xx - 1, y0 - 1, xx + c, y0 + c), outline=BORD, width=2)
    d.text((xx + c / 2, y0 + c + 26), f"étape {t:,}".replace(",", "\u202f"), fill=PALE, font=police(21, True), anchor="mm")


def fleche(y, de, a, coul, texte):
    d.line((de, y, a, y), fill=coul, width=4)
    sens = 1 if a > de else -1
    d.polygon([(a, y), (a - sens * 18, y - 10), (a - sens * 18, y + 10)], fill=coul)
    d.text(((de + a) / 2, y - 22 if y < y0 else y + 24), texte, fill=coul, font=police(22, True), anchor="mm")


fleche(y0 - 22, x0 + 20, W - x0 - 20, BRUN, "ajouter du bruit, étape par étape (sans apprentissage)")
fleche(H - 52, W - x0 - 20, x0 + 20, TEAL, "retirer du bruit, étape par étape : c'est ce que le réseau apprend")
im.save(RACINE.parent / "static" / "images" / "module4" / "diffusion-visage.jpg", quality=88)
print("diffusion-visage.jpg écrit", im.size)
