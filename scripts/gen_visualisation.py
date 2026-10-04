"""Module 3, « L'apprentissage profond » : ce que cherchent des neurones de couches de plus en plus profondes.

Vignettes tirées de la planche d'en-tête de « Feature Visualization » (Olah, Mordvintsev et Schubert, Distill, 2017,
licence CC BY 4.0), conservée dans scripts/data/distill-feature-visualization-sprite.jpg : cinq colonnes (traits,
textures, motifs, parties, objets) de six vignettes de 200 pixels.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

RACINE = Path(__file__).resolve().parent
planche = Image.open(RACINE / "data" / "distill-feature-visualization-sprite.jpg").convert("RGB")
FOND, BORD, ENCRE, PALE, TEAL = "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#2f6f6a"
police = lambda t, gras=False: ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", t, index=1 if gras else 0)

colonnes = [("Traits", "première couche"), ("Textures", ""), ("Motifs", ""), ("Parties d'objets", ""), ("Objets", "dernières couches")]
lignes = (0, 1, 3)                                 # trois des six vignettes de chaque colonne
c, e, x0, y0 = 230, 18, 60, 150
W = x0 * 2 + 5 * c + 4 * e
H = y0 + 3 * c + 2 * e + 110
im = Image.new("RGB", (W, H), FOND)
d = ImageDraw.Draw(im)
d.rounded_rectangle((1, 1, W - 2, H - 2), radius=28, outline=BORD, width=2)
d.text((W / 2, 50), "Ce que cherchent des neurones, de la première couche à la dernière", fill=ENCRE, font=police(34, True), anchor="mm")
for k, (nom, sous) in enumerate(colonnes):
    x = x0 + k * (c + e)
    d.text((x + c / 2, 104), nom, fill=TEAL, font=police(28, True), anchor="mm")
    if sous:
        d.text((x + c / 2, 134), sous, fill=PALE, font=police(22), anchor="mm")
    for r, j in enumerate(lignes):
        v = planche.crop((k * 200, j * 200, k * 200 + 200, j * 200 + 200)).resize((c, c), Image.LANCZOS)
        y = y0 + r * (c + e)
        im.paste(v, (x, y))
        d.rectangle((x - 1, y - 1, x + c, y + c), outline=BORD, width=2)
fl = y0 + 3 * c + 2 * e + 40
d.line((x0, fl, W - x0 - 20, fl), fill=PALE, width=3)
d.polygon([(W - x0, fl), (W - x0 - 22, fl - 10), (W - x0 - 22, fl + 10)], fill=PALE)
d.text((W / 2, fl + 36), "D'après Olah, Mordvintsev et Schubert, « Feature Visualization », Distill (2017), CC BY 4.0.", fill=PALE, font=police(22), anchor="mm")
im.save(RACINE.parent / "static" / "images" / "module3" / "visualisation-neurones.jpg", quality=85)
print("visualisation-neurones.jpg écrit", im.size)
