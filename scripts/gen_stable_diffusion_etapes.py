# /// script
# requires-python = ">=3.10,<3.13"
# dependencies = ["torch", "diffusers", "transformers", "accelerate", "pillow", "numpy"]
# ///
"""Module 4, « Mots et images » : les vraies étapes du débruitage de Stable Diffusion 1.5.

Le modèle (environ 4 Go) est téléchargé depuis Hugging Face au premier lancement. La grille latente est décodée en
image au départ (bruit pur) et après quelques passages du débruiteur, puis les images sont assemblées en une bande.

    uv run scripts/gen_stable_diffusion_etapes.py
"""
from pathlib import Path
import numpy as np
import torch
from diffusers import StableDiffusionPipeline, DDIMScheduler
from PIL import Image, ImageDraw, ImageFont

RACINE = Path(__file__).resolve().parent
SORTIE = RACINE.parent / "static" / "images" / "module4" / "stable-diffusion-etapes.jpg"
CONSIGNE = "a cat astronaut on the moon, digital painting"
PAS, GARDER, GRAINE = 50, [0, 20, 30, 40, 50], 11
dev = "mps" if torch.backends.mps.is_available() else "cpu"

pipe = StableDiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5", torch_dtype=torch.float32,
                                               safety_checker=None, requires_safety_checker=False).to(dev)
pipe.scheduler = DDIMScheduler.from_config(pipe.scheduler.config)
latents = {}


def garder(p, i, t, kw):                                      # i : passage qui vient de se terminer (0 = le premier)
    if i + 1 in GARDER:
        latents[i + 1] = kw["latents"].detach().clone()
    return kw


g = torch.Generator("cpu").manual_seed(GRAINE)
depart = torch.randn((1, 4, 64, 64), generator=g) * pipe.scheduler.init_noise_sigma
latents[0] = depart.clone().to(dev)
pipe(CONSIGNE, num_inference_steps=PAS, guidance_scale=7.5, latents=depart.to(dev),
     callback_on_step_end=garder, callback_on_step_end_tensor_inputs=["latents"])


@torch.no_grad()
def decoder(z):
    x = pipe.vae.decode(z / pipe.vae.config.scaling_factor).sample
    x = ((x.clamp(-1, 1) + 1) / 2 * 255).round().byte()[0].permute(1, 2, 0).cpu().numpy()
    return Image.fromarray(x)


images = [decoder(latents[k]) for k in GARDER]
FOND, BORD, ENCRE, PALE = "#efe7d3", "#d9cbac", "#3a3531", "#5b5249"
police = lambda t, gras=False: ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", t, index=1 if gras else 0)
C, M, E = 300, 40, 24
W, H = 2 * M + len(images) * C + (len(images) - 1) * E, 470
bande = Image.new("RGB", (W, H), FOND)
dr = ImageDraw.Draw(bande)
dr.rounded_rectangle((1, 1, W - 2, H - 2), radius=24, outline=BORD, width=2)
dr.text((W / 2, 46), "Stable Diffusion retire le bruit, passage après passage", fill=ENCRE, font=police(34, True), anchor="mm")
titres = ["bruit de départ"] + [f"après {k} passages" for k in GARDER[1:]]
for k, (im, titre) in enumerate(zip(images, titres)):
    x = M + k * (C + E)
    bande.paste(im.resize((C, C), Image.LANCZOS), (x, 96))
    dr.rectangle((x - 1, 95, x + C, 96 + C), outline=BORD, width=2)
    dr.text((x + C / 2, 96 + C + 34), titre, fill=PALE, font=police(24), anchor="mm")
bande.save(SORTIE, quality=88)
print(SORTIE.name, "écrit", bande.size)
