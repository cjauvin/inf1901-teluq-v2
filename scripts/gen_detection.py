# /// script
# requires-python = ">=3.10,<3.13"
# dependencies = ["torch", "torchvision", "pillow", "numpy"]
# ///
"""Module 3, « Voir : les réseaux convolutifs » : classer, détecter, segmenter.

Une même photo de rue (Gabriel Santiago, Unsplash, via Wikimedia Commons, CC0 ;
scripts/data/detection/rue-pietons.jpg) est traitée par deux vrais réseaux préentraînés
de torchvision : un classifieur ImageNet (MobileNet V3) donne une seule étiquette pour
l'image entière, et Mask R-CNN (entraîné sur COCO) donne les rectangles et les contours.
Rien n'est dessiné à la main : les étiquettes, rectangles et silhouettes sont ceux que
produisent les réseaux. Les poids sont téléchargés par torchvision au premier lancement.

    uv run scripts/gen_detection.py
"""
from pathlib import Path
import numpy as np
import torch
from torchvision.models import MobileNet_V3_Large_Weights, mobilenet_v3_large
from torchvision.models.detection import MaskRCNN_ResNet50_FPN_V2_Weights, maskrcnn_resnet50_fpn_v2
from torchvision.transforms.functional import to_tensor
from PIL import Image, ImageDraw, ImageFilter, ImageFont

RACINE = Path(__file__).resolve().parent
FOND, BORD, ENCRE, PALE, TEAL = "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#2f6f6a"
police = lambda t, gras=False: ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", t, index=1 if gras else 0)
SEUIL = 0.7
FR = {"person": "personne", "car": "voiture", "bus": "autobus", "truck": "camion",
      "traffic light": "feu", "handbag": "sac", "backpack": "sac à dos", "bicycle": "vélo",
      "motorcycle": "moto", "umbrella": "parapluie", "dog": "chien"}
COULEURS = {"personne": (196, 86, 74), "voiture": (58, 110, 165), "autobus": (47, 111, 106),
            "camion": (154, 91, 51), "feu": (214, 170, 40)}

photo = Image.open(RACINE / "data" / "detection" / "rue-pietons.jpg").convert("RGB")
W0, H0 = photo.size                                   # recadrage 4:3 sur le passage piéton
photo = photo.crop((round(0.26 * W0), round(0.45 * H0), round(0.26 * W0) + round(0.55 * H0 * 4 / 3), H0))
x = to_tensor(photo)

with torch.no_grad():
    pc = MobileNet_V3_Large_Weights.IMAGENET1K_V2
    clf = mobilenet_v3_large(weights=pc).eval()
    proba = clf(pc.transforms()(photo).unsqueeze(0)).softmax(1)[0]
    top = proba.topk(5)
    for p, i in zip(top.values, top.indices):
        print(f"classification : {pc.meta['categories'][i]} ({p:.0%})")
    pd = MaskRCNN_ResNet50_FPN_V2_Weights.COCO_V1
    det = maskrcnn_resnet50_fpn_v2(weights=pd).eval()
    sortie = det([x])[0]

garde = sortie["scores"] >= SEUIL
objets = [(pd.meta["categories"][int(c)], float(s), b.tolist(), m[0].numpy() > 0.5)
          for c, s, b, m in zip(sortie["labels"][garde], sortie["scores"][garde],
                                sortie["boxes"][garde], sortie["masks"][garde])]
for nom, s, _, _ in objets:
    print(f"objet : {nom} ({s:.0%})")

ETIQUETTE = "taxi"           # traduction de la meilleure classe ImageNet, vérifiée à l'exécution ci-dessus


def couleur(nom):
    return COULEURS.get(FR.get(nom, nom), (120, 110, 100))


def detecter(im, echelle):
    d = ImageDraw.Draw(im)
    for nom, _, (x0, y0, x1, y1), _ in objets:
        c = couleur(nom)
        x0, y0, x1, y1 = (v * echelle for v in (x0, y0, x1, y1))
        d.rectangle((x0, y0, x1, y1), outline=c, width=3)
    poses = []                                   # étiquettes des plus grands objets, sans chevauchement
    for nom, _, (x0, y0, x1, y1), _ in sorted(objets, key=lambda o: -(o[2][2] - o[2][0]) * (o[2][3] - o[2][1])):
        if (x1 - x0) * echelle < 40:
            continue
        c, t = couleur(nom), FR.get(nom, nom)
        f = police(14, True)
        lx = d.textlength(t, font=f)
        x0, y0 = x0 * echelle, y0 * echelle
        ty = max(y0 - 20, 0)
        r = (x0, ty, x0 + lx + 10, ty + 20)
        if any(r[0] < q[2] and q[0] < r[2] and r[1] < q[3] and q[1] < r[3] for q in poses):
            continue
        poses.append(r)
        d.rectangle(r, fill=c)
        d.text((x0 + 5, ty + 10), t, fill="white", font=f, anchor="lm")
    return im


def segmenter(im, echelle):
    base = np.asarray(im).astype(float) * 0.55 + 255 * 0.45 * np.array([0.94, 0.91, 0.83])
    for k, (nom, _, _, m) in enumerate(sorted(objets, key=lambda o: -o[3].sum())):   # les grands d'abord
        masque = Image.fromarray(m).resize(im.size, Image.NEAREST)
        mm = np.asarray(masque)
        teinte = np.array(couleur(nom)) * (0.82, 1.0, 1.15)[k % 3]   # chaque objet a sa nuance
        base[mm] = base[mm] * 0.25 + teinte.clip(0, 255) * 0.75
        bord = mm & ~np.asarray(masque.filter(ImageFilter.MinFilter(3)))   # contour d'un pixel
        base[bord] = 255
    return Image.fromarray(base.clip(0, 255).astype(np.uint8))


l, h, e, x0, y0 = 440, 330, 18, 40, 96
W = 2 * x0 + 3 * l + 2 * e
H = y0 + h + 150
fig = Image.new("RGB", (W, H), FOND)
d = ImageDraw.Draw(fig)
d.rounded_rectangle((1, 1, W - 2, H - 2), radius=24, outline=BORD, width=2)
d.text((W / 2, 46), "Une même photo, trois tâches", fill=ENCRE, font=police(30, True), anchor="mm")
r = max(l / photo.width, h / photo.height)
petite = photo.resize((round(photo.width * r), round(photo.height * r)), Image.LANCZOS)
gx, gy = (petite.width - l) // 2, (petite.height - h) // 2
panneaux = []
for k in range(3):
    v = petite.copy()
    if k == 1:
        v = detecter(v, r)
    elif k == 2:
        v = segmenter(v, r)
    panneaux.append(v.crop((gx, gy, gx + l, gy + h)))
d0 = ImageDraw.Draw(panneaux[0])
f = police(20, True)
t = f"« {ETIQUETTE} »"
lx = d0.textlength(t, font=f)
d0.rounded_rectangle((l / 2 - lx / 2 - 14, 14, l / 2 + lx / 2 + 14, 52), radius=8, fill=TEAL)
d0.text((l / 2, 33), t, fill="white", font=f, anchor="mm")
titres = [("Classer", "une étiquette pour toute l'image"),
          ("Détecter", "un rectangle et une étiquette par objet"),
          ("Segmenter", "la forme exacte de chaque objet")]
for k, (v, (t1, t2)) in enumerate(zip(panneaux, titres)):
    x = x0 + k * (l + e)
    fig.paste(v, (x, y0))
    d.rectangle((x - 1, y0 - 1, x + l, y0 + h), outline=BORD, width=2)
    d.text((x + l / 2, y0 + h + 30), t1, fill=TEAL, font=police(24, True), anchor="mm")
    d.text((x + l / 2, y0 + h + 60), t2, fill=PALE, font=police(19), anchor="mm")
d.text((W / 2, H - 30), "Une rue de Vancouver, photo de Gabriel Santiago (Unsplash, CC0). Étiquettes, rectangles et formes produits par "
       "deux réseaux : MobileNet V3 et Mask R-CNN.", fill=PALE, font=police(17), anchor="mm")
sortie_fig = RACINE.parent / "static" / "images" / "module3" / "classer-detecter-segmenter.jpg"
fig.save(sortie_fig, quality=88)
print(sortie_fig.name, "écrit", fig.size)
