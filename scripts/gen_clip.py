# /// script
# requires-python = ">=3.10,<3.13"
# dependencies = ["torch", "transformers", "pillow", "numpy"]
# ///
"""Module 4, « Relier les mots et les images » : les ressemblances de l'applet `clip.html`.

Le modèle CLIP d'OpenAI (openai/clip-vit-base-patch32, téléchargé depuis Hugging Face au premier lancement)
place douze images et une vingtaine de légendes dans un même espace, et on calcule la ressemblance (cosinus)
de chaque image avec chaque légende. CLIP a été entraîné sur des légendes en anglais : les légendes lui sont
données en anglais, et l'applet affiche leur traduction.

Images (scripts/data/clip/) : photos Unsplash sous CC0 et Joconde (domaine public) de Wikimedia Commons, plus des
images déjà utilisées dans le module (rue de Vancouver, méduses, Théâtre D'opéra Spatial, un chiffre de MNIST).

    uv run scripts/gen_clip.py
"""
import base64, io, json
from pathlib import Path
import numpy as np
import torch
from PIL import Image
from transformers import CLIPModel, CLIPProcessor

RACINE = Path(__file__).resolve().parent
SORTIE = RACINE.parent / "static" / "html" / "applets" / "data" / "clip.json"
IMAGES = ["chat", "chiens", "velo", "guitare", "pizza", "erable", "joconde", "theatre", "rue", "meduses", "chiffre", "neige"]
LEGENDES = [
    ("a photo of a cat", "une photo d'un chat"),
    ("a photo of dogs", "une photo de chiens"),
    ("a red bicycle", "un vélo rouge"),
    ("a woman playing the guitar", "une femme qui joue de la guitare"),
    ("a pizza", "une pizza"),
    ("a red maple leaf", "une feuille d'érable rouge"),
    ("the Mona Lisa", "la Joconde"),
    ("a science fiction painting", "une peinture de science-fiction"),
    ("a busy city street", "une rue animée en ville"),
    ("jellyfish", "des méduses"),
    ("a handwritten digit seven", "un sept écrit à la main"),
    ("a person walking a dog in the snow", "une personne qui promène un chien dans la neige"),
    ("the flag of Canada", "le drapeau du Canada"),
    ("an Italian dish", "un plat italien"),
    ("a musical instrument", "un instrument de musique"),
    ("a portrait of a woman", "le portrait d'une femme"),
    ("an animal", "un animal"),
    ("a stop sign", "un panneau d'arrêt"),
    ("a winter landscape", "un paysage d'hiver"),
    ("a creature living in the ocean", "une créature qui vit dans l'océan"),
]
m = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").eval()
p = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
ims = [Image.open(RACINE / "data" / "clip" / f"{n}.jpg").convert("RGB") for n in IMAGES]
with torch.no_grad():
    ei = m.visual_projection(m.vision_model(**p(images=ims, return_tensors="pt")).pooler_output)
    et = m.text_projection(m.text_model(**p(text=[e for e, _ in LEGENDES], return_tensors="pt", padding=True)).pooler_output)
ei = ei / ei.norm(dim=-1, keepdim=True)
et = et / et.norm(dim=-1, keepdim=True)
S = (ei @ et.T).numpy()


def vignette(im):
    c = min(im.size)
    im = im.crop(((im.width - c) // 2, (im.height - c) // 2, (im.width + c) // 2, (im.height + c) // 2)).resize((160, 160), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, "JPEG", quality=82)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()


SORTIE.write_text(json.dumps({
    "echelle": float(m.logit_scale.exp()),
    "images": [{"nom": n, "src": vignette(im)} for n, im in zip(IMAGES, ims)],
    "legendes": [{"en": e, "fr": f} for e, f in LEGENDES],
    "sim": [[round(float(x), 4) for x in ligne] for ligne in S],
}, ensure_ascii=False, separators=(",", ":")))
print(SORTIE.name, SORTIE.stat().st_size // 1024, "Ko")
for i, n in enumerate(IMAGES):
    o = np.argsort(-S[i])[:3]
    print(f"{n:9s}", " | ".join(f"{LEGENDES[j][1]} {S[i, j]:.3f}" for j in o))
