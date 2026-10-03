"""Module 3, « Tromper un réseau » : recompose la figure du panda (Goodfellow et collègues, 2014) dans le style du cours.

Les trois vignettes viennent de l'ancienne image static/images/module3/panda-vs-gibbon2.png (v1) ; seules les
étiquettes changent : la perturbation n'est pas un bruit aléatoire, elle est calculée.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

RACINE = Path(__file__).resolve().parent.parent / "static" / "images" / "module3"
src = Image.open(RACINE / "panda-vs-gibbon2.png").convert("RGB")
vignettes = [src.crop((60, 105, 310, 355)), src.crop((367, 104, 617, 354)), src.crop((669, 105, 919, 355))]

W, H, e = 1400, 560, 2
FOND, BORD, ENCRE, PALE, ROUGE, TEAL = "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#c4564a", "#2f6f6a"
im = Image.new("RGB", (W, H), FOND)
d = ImageDraw.Draw(im)
d.rounded_rectangle((1, 1, W - 2, H - 2), radius=28, outline=BORD, width=2)
police = lambda t, gras=False: ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", t, index=1 if gras else 0)
d.text((W / 2, 52), "Un panda, une perturbation calculée, un « gibbon »", fill=ENCRE, font=police(34, True), anchor="mm")
xs, y0, c = [90, 575, 1060], 110, 250
for x, v in zip(xs, vignettes):
    im.paste(v.resize((c, c)), (x, y0))
    d.rectangle((x - 1, y0 - 1, x + c, y0 + c), outline=BORD, width=2)
d.text(((xs[0] + c + xs[1]) / 2, y0 + c / 2), "+", fill=PALE, font=police(64, True), anchor="mm")
d.text(((xs[1] + c + xs[2]) / 2, y0 + c / 2), "=", fill=PALE, font=police(64, True), anchor="mm")
etiquettes = [("réponse : panda", "confiance : 57,7 %", TEAL), ("perturbation calculée", "très faible, amplifiée ici", PALE),
              ("réponse : gibbon", "confiance : 99,3 %", ROUGE)]
for x, (l1, l2, coul) in zip(xs, etiquettes):
    d.text((x + c / 2, y0 + c + 52), l1, fill=coul, font=police(30, True), anchor="mm")
    d.text((x + c / 2, y0 + c + 92), l2, fill=PALE, font=police(26), anchor="mm")
d.text((W / 2, H - 40), "D'après Goodfellow, Shlens et Szegedy (2014).", fill=PALE, font=police(24), anchor="mm")
im.save(RACINE / "panda-gibbon.png", optimize=True)
print("panda-gibbon.png écrit")
