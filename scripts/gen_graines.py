# /// script
# requires-python = ">=3.10,<3.13"
# dependencies = ["torch", "diffusers", "transformers", "accelerate", "pillow"]
# ///
"""Module 4, « Quatre façons de générer » : la même consigne, quatre graines, quatre images (Stable Diffusion 1.5).

    uv run scripts/gen_graines.py
"""
from pathlib import Path
import torch
from diffusers import StableDiffusionPipeline, DDIMScheduler
from PIL import Image, ImageDraw, ImageFont

RACINE = Path(__file__).resolve().parent
SORTIE = RACINE.parent / "static" / "images" / "module4" / "quatre-graines.jpg"
CONSIGNE = "a cat astronaut on the moon, digital painting"
GRAINES = [1, 4, 7, 11]
dev = "mps" if torch.backends.mps.is_available() else "cpu"

pipe = StableDiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5", safety_checker=None,
                                               requires_safety_checker=False).to(dev)
pipe.scheduler = DDIMScheduler.from_config(pipe.scheduler.config)
pipe.set_progress_bar_config(disable=True)
images = []
for gr in GRAINES:
    g = torch.Generator("cpu").manual_seed(gr)
    depart = torch.randn((1, 4, 64, 64), generator=g) * pipe.scheduler.init_noise_sigma   # comme gen_stable_diffusion_etapes.py
    images.append(pipe(CONSIGNE, num_inference_steps=50, guidance_scale=7.5, latents=depart.to(dev)).images[0])

FOND, BORD, ENCRE, PALE, BLEU = "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#3a6ea5"
police = lambda t, gras=False: ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", t, index=1 if gras else 0)
C, M, E = 320, 40, 26
W, H = 2 * M + 4 * C + 3 * E, 540
bande = Image.new("RGB", (W, H), FOND)
dr = ImageDraw.Draw(bande)
dr.rounded_rectangle((1, 1, W - 2, H - 2), radius=24, outline=BORD, width=2)
dr.text((W / 2, 48), "La même consigne, quatre graines", fill=ENCRE, font=police(36, True), anchor="mm")
dr.text((W / 2, 92), "« un chat astronaute sur la lune »", fill=PALE, font=police(26), anchor="mm")
for k, (im, gr) in enumerate(zip(images, GRAINES)):
    x = M + k * (C + E)
    bande.paste(im.resize((C, C), Image.LANCZOS), (x, 130))
    dr.rectangle((x - 1, 129, x + C, 130 + C), outline=BORD, width=2)
    dr.text((x + C / 2, 130 + C + 40), f"graine {gr}", fill=BLEU, font=police(28, True), anchor="mm")
bande.save(SORTIE, quality=88)
print(SORTIE.name, "écrit", bande.size)
