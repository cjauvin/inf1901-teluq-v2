"""Module 3, « L'apprentissage profond » : l'espace latent d'un autoencodeur, en trois panneaux.

Le réseau est l'autoencodeur variationnel de l'applet `espace-latent.html` du Module 4 (gen_espace_latent.py), dont
l'espace latent n'a que deux dimensions. Données : static/html/applets/data/espace-latent.json (décodeur, positions
latentes de 2 000 chiffres de test et leurs numéros) et MNIST (cache ~/.cache/inf1901/mnist).
1. un vrai chiffre et ses deux coordonnées ; 2. la carte des 2 000 chiffres ; 3. le décodeur appliqué à une grille.

    uv run --with numpy --with pillow python scripts/gen_espace_latent_figure.py
"""
import base64, json
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont

RACINE = Path(__file__).resolve().parent
FOND, BORD, ENCRE, PALE, TEAL, PANNEAU = "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#2f6f6a", "#fbf7ee"
COUL = ['#c4564a', '#3a6ea5', '#2f6f6a', '#9a5b33', '#7b5ea7', '#d18f2f', '#4f8f3a', '#b5487f', '#5b7d8a', '#8a7a2e']
police = lambda t, gras=False: ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", t, index=1 if gras else 0)

d = json.loads((RACINE.parent / "static" / "html" / "applets" / "data" / "espace-latent.json").read_text())
couches = [(np.frombuffer(base64.b64decode(c["w"]), np.float16).astype(np.float32).reshape(c["entrees"], c["sorties"]),
            np.frombuffer(base64.b64decode(c["b"]), np.float16).astype(np.float32)) for c in d["couches"]]


def decoder(z):
    h = np.asarray(z, np.float32)
    for k, (w, b) in enumerate(couches):
        h = h @ w + b
        if k < len(couches) - 1:
            h = np.maximum(h, 0)
    return 1 / (1 + np.exp(-np.clip(h, -30, 30)))


pts = np.array([p[:2] for p in d["points"]]); lab = np.array([p[2] for p in d["points"]])
cache = Path.home() / ".cache" / "inf1901" / "mnist" / "MNIST" / "raw"
imgs = np.frombuffer((cache / "t10k-images-idx3-ubyte").read_bytes(), np.uint8, offset=16).reshape(-1, 28, 28)
k = int(np.argmax(lab == 3))                            # le premier 3 de la carte
ex_img, ex_z = imgs[d["indices"][k]], pts[k]

c = 460
W, H = 40 + 300 + 30 + c + 30 + c + 40, 680
im = Image.new("RGB", (W, H), FOND)
dr = ImageDraw.Draw(im)
dr.rounded_rectangle((1, 1, W - 2, H - 2), radius=24, outline=BORD, width=2)
dr.text((W / 2, 42), "L'espace latent d'un autoencodeur", fill=ENCRE, font=police(30, True), anchor="mm")
y0 = 96
# 1. compresser
x1 = 40
dr.text((x1 + 150, y0), "1. Compresser", fill=TEAL, font=police(23, True), anchor="mm")
v = Image.fromarray(255 - ex_img).resize((168, 168), Image.NEAREST).convert("RGB")
im.paste(v, (x1 + 66, y0 + 40)); dr.rectangle((x1 + 65, y0 + 39, x1 + 234, y0 + 208), outline=BORD, width=2)
dr.text((x1 + 150, y0 + 232), "784 pixels", fill=PALE, font=police(19), anchor="mm")
dr.line((x1 + 150, y0 + 254, x1 + 150, y0 + 318), fill="#7a6f63", width=3)
dr.polygon([(x1 + 150, y0 + 330), (x1 + 141, y0 + 314), (x1 + 159, y0 + 314)], fill="#7a6f63")
dr.text((x1 + 162, y0 + 286), "encodeur", fill=PALE, font=police(18), anchor="lm")
coord = f"({ex_z[0]:.2f} ; {ex_z[1]:.2f})".replace(".", ",").replace("-", "−")
dr.rounded_rectangle((x1 + 40, y0 + 340, x1 + 260, y0 + 392), radius=10, fill=PANNEAU, outline=COUL[3], width=3)
dr.text((x1 + 150, y0 + 366), coord, fill=ENCRE, font=police(22, True), anchor="mm")
dr.text((x1 + 150, y0 + 416), "2 nombres", fill=PALE, font=police(19), anchor="mm")
# 2. la carte
x2 = x1 + 300 + 30
dr.text((x2 + c / 2, y0), "2. La carte", fill=TEAL, font=police(23, True), anchor="mm")
lo, hi = -3.3, 3.6
vers = lambda z: (x2 + (z[0] - lo) / (hi - lo) * c, y0 + 30 + c - (z[1] - lo) / (hi - lo) * c)
dr.rectangle((x2, y0 + 30, x2 + c, y0 + 30 + c), fill=PANNEAU, outline=BORD, width=2)
for z, e in zip(pts, lab):
    X, Y = vers(z)
    if x2 + 3 < X < x2 + c - 3 and y0 + 33 < Y < y0 + 27 + c:
        dr.ellipse((X - 2.6, Y - 2.6, X + 2.6, Y + 2.6), fill=COUL[e])
for e in range(10):
    X, Y = vers(np.median(pts[lab == e], axis=0))
    dr.text((X, Y), str(e), fill=COUL[e], font=police(34, True), anchor="mm", stroke_width=4, stroke_fill=PANNEAU)
X, Y = vers(ex_z)
dr.ellipse((X - 10, Y - 10, X + 10, Y + 10), outline=ENCRE, width=4)
# 3. l'atlas
x3 = x2 + c + 30
dr.text((x3 + c / 2, y0), "3. L'atlas", fill=TEAL, font=police(23, True), anchor="mm")
n = 16
atlas = np.ones((n * 28, n * 28))
for i, y in enumerate(np.linspace(hi - 0.2, lo + 0.2, n)):
    for j, x in enumerate(np.linspace(lo + 0.2, hi - 0.2, n)):
        atlas[i * 28:(i + 1) * 28, j * 28:(j + 1) * 28] = 1 - decoder([x, y]).reshape(28, 28)
a = Image.fromarray((atlas * 255).astype(np.uint8)).resize((c, c), Image.LANCZOS).convert("RGB")
im.paste(a, (x3, y0 + 30)); dr.rectangle((x3 - 1, y0 + 29, x3 + c, y0 + 30 + c), outline=BORD, width=2)
# légendes
yl = y0 + 30 + c + 30
dr.text((x1 + 150, yl), "un vrai chiffre devient", fill=PALE, font=police(18), anchor="mm")
dr.text((x1 + 150, yl + 24), "un point de la carte", fill=PALE, font=police(18), anchor="mm")
dr.text((x2 + c / 2, yl), "2 000 vrais chiffres, placés par l'encodeur :", fill=PALE, font=police(18), anchor="mm")
dr.text((x2 + c / 2, yl + 24), "les chiffres semblables se regroupent", fill=PALE, font=police(18), anchor="mm")
dr.text((x3 + c / 2, yl), "ce que le décodeur dessine en chaque point :", fill=PALE, font=police(18), anchor="mm")
dr.text((x3 + c / 2, yl + 24), "on passe d'un chiffre à l'autre par petites étapes", fill=PALE, font=police(18), anchor="mm")
im.save(RACINE.parent / "static" / "images" / "module3" / "espace-latent.jpg", quality=90)
print("espace-latent.jpg écrit", im.size, coord)
