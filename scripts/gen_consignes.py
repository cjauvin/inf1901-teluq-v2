# /// script
# requires-python = ">=3.10,<3.13"
# dependencies = ["torch", "diffusers", "transformers", "accelerate", "pillow", "numpy"]
# ///
"""Module 4, « Quatre façons de générer » : le dessin d'enfant et sa transformation par Stable Diffusion, pour la figure
des trois sortes de consignes (gen_consignes_figure.py).

- le 7 vient du VAE conditionnel de gen_generation_conditionnelle.py (repris dans generation-conditionnelle.svg) ;
- le dessin d'enfant est tracé ici, puis transformé par Stable Diffusion 1.5 en mode « image vers image » ;
- le chat astronaute est la dernière image de stable-diffusion-etapes.jpg (gen_stable_diffusion_etapes.py).

    uv run scripts/gen_consignes.py
"""
import base64, io, re
from pathlib import Path
import torch
from diffusers import StableDiffusionImg2ImgPipeline, DDIMScheduler
from PIL import Image, ImageDraw

RACINE = Path(__file__).resolve().parent
OUT = RACINE.parent / "static" / "images" / "module4"
dev = "mps" if torch.backends.mps.is_available() else "cpu"

# ── le dessin d'enfant ──
dessin = Image.new("RGB", (512, 512), "white")
d = ImageDraw.Draw(dessin)
d.line([(0, 392), (512, 384)], fill=(70, 160, 60), width=10)                       # le sol
d.rectangle((150, 240, 330, 390), outline=(200, 70, 50), width=9)                  # la maison
d.line([(135, 245), (240, 140), (345, 245)], fill=(120, 60, 40), width=9, joint="curve")  # le toit
d.rectangle((215, 310, 265, 390), outline=(90, 60, 40), width=7)                   # la porte
d.rectangle((168, 270, 205, 300), outline=(60, 110, 200), width=6)                 # la fenêtre
d.ellipse((380, 50, 460, 130), outline=(240, 180, 30), width=9)                    # le soleil
for a in range(0, 360, 45):
    import math
    c, s = math.cos(math.radians(a)), math.sin(math.radians(a))
    d.line([(420 + 52 * c, 90 + 52 * s), (420 + 72 * c, 90 + 72 * s)], fill=(240, 180, 30), width=7)
d.line([(70, 390), (70, 300)], fill=(110, 70, 40), width=10)                       # l'arbre
d.ellipse((30, 220, 110, 310), outline=(60, 150, 60), width=9)

pipe = StableDiffusionImg2ImgPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5",
                                                      safety_checker=None, requires_safety_checker=False).to(dev)
pipe.scheduler = DDIMScheduler.from_config(pipe.scheduler.config)
pipe.set_progress_bar_config(disable=True)
g = torch.Generator("cpu").manual_seed(2)
tableau = pipe("a cozy cottage with a red door in a green meadow, a tree, blue sky, bright sun, detailed oil painting",
               image=dessin, strength=0.8, guidance_scale=8, num_inference_steps=50, generator=g).images[0]
tableau.save(RACINE.parent / "static" / "images" / "module4" / "consigne-image-tableau.jpg", quality=90)
dessin.save(RACINE.parent / "static" / "images" / "module4" / "consigne-image-dessin.png")
print("dessin et tableau écrits")
