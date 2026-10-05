"""Module 4, « Des images, des voix, des vidéos » : les images de l'applet `vraie-ou-generee.html`.

Cinq vraies photos (Unsplash, CC0, via Wikimedia Commons), recadrées sur le visage, et cinq visages
générés, d'époques différentes et absents de la page « Générer » (Wikimedia Commons) :
- StyleGAN2 : GAN Mensch StyleGAN2.png (domaine public) et This person doesn't exist … StyleGAN2
  (Dec 2019).jpg (Datasciencearabic1, CC BY-SA 4.0) ;
- Stable Diffusion : deux portraits recadrés (900 × 900, colonnes 5 et 6 de la grille) dans X-Y plot of
  algorithmically-generated photorealistic portraits by nationality.png (Benlisquare, CC BY-SA 4.0),
  conservés sous src-sd-1.jpg et src-sd-2.jpg ;
- ChatGPT Images : User-Kerberiel.jpg (domaine public).
Sources dans scripts/data/vraie-ou-generee/. Les images sont mélangées et renommées img-01 … img-10 ; les réponses
et les indices sont écrits dans data/vraie-ou-generee.json.
"""
import json
import random
from pathlib import Path
from PIL import Image

RACINE = Path(__file__).resolve().parent
SOURCE = RACINE / "data" / "vraie-ou-generee"
SORTIE = RACINE.parent / "static" / "html" / "applets" / "data" / "vraie-ou-generee"
SORTIE.mkdir(parents=True, exist_ok=True)
CADRAGE = "Le cadrage aussi : comme tous les visages StyleGAN, il est centré, les yeux exactement au même endroit."
LISSE = ("La peau est parfaitement lisse et les traits très réguliers. Ce visage vient d'une grille où le même modèle a "
         "produit douze femmes presque identiques, avec la même coiffure et le même chemisier.")


IMAGES = [
    ("vraie-1.jpg", "1280", (498, 177, 882, 561), True, "Photo de Foto Sushi (Unsplash, CC0)."),
    ("vraie-2.jpg", "1280", (512, 104, 812, 404), True, "Photo de Christopher Campbell (Unsplash, CC0)."),
    ("vraie-3.jpg", "1280", (244, 135, 804, 695), True, "Photo de Kahar Saidyhalam (Unsplash, CC0)."),
    ("vraie-4.jpg", "1280", (411, 203, 671, 463), True, "Photo de REASONS ART (Unsplash, CC0)."),
    ("vraie-5.jpg", "1280", (353, 168, 913, 728), True, "Photo de Seth Doyle (Unsplash, CC0)."),
    ("generee-5.jpg", None, None, False, "StyleGAN2, 2020. Dans le fond, à droite, un objet flou qui ne ressemble à rien de connu. "
     + CADRAGE + " (Wikimedia Commons, domaine public.)"),
    ("src-tpdne-2019.jpg", None, None, False, "StyleGAN2, 2019. Le fond, à droite, contient des formes qui ne correspondent à aucun objet. "
     + CADRAGE + " (Datasciencearabic1, Wikimedia Commons, CC BY-SA 4.0.)"),
    ("src-sd-1.jpg", None, None, False, "Stable Diffusion, 2022. " + LISSE + " (Benlisquare, Wikimedia Commons, CC BY-SA 4.0.)"),
    ("src-sd-2.jpg", None, None, False, "Stable Diffusion, 2022. " + LISSE + " (Benlisquare, Wikimedia Commons, CC BY-SA 4.0.)"),
    ("src-chatgpt-2025.jpg", "px", (352, 16, 1152, 816), False,
     "ChatGPT Images, 2026. Presque aucun indice : seulement une lumière de studio très flatteuse et des mèches qui se "
     "fondent dans le fond. Les générateurs récents ont fait disparaître la plupart des défauts visibles. (Wikimedia Commons, domaine public.)"),
]
rnd = random.Random(2)
ordre = list(range(len(IMAGES)))
rnd.shuffle(ordre)
reponses = []
for n, k in enumerate(ordre, 1):
    f, repere, boite, vraie, note = IMAGES[k]
    im = Image.open(SOURCE / f).convert("RGB")
    if boite:
        e = im.width / 1280 if repere == "1280" else 1   # « 1280 » : boîte donnée pour une image de 1 280 pixels de large
        im = im.crop(tuple(round(e * v) for v in boite))
    im.resize((400, 400), Image.LANCZOS).save(SORTIE / f"img-{n:02d}.jpg", quality=88)
    note = note.replace(" : ", "\u00a0: ").replace(" ; ", "\u202f; ")
    reponses.append({"image": f"img-{n:02d}.jpg", "vraie": vraie, "note": note})
(SORTIE.parent / "vraie-ou-generee.json").write_text(json.dumps(reponses, ensure_ascii=False, indent=1))
print([r["vraie"] for r in reponses])
