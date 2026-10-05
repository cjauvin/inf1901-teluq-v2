# /// script
# requires-python = ">=3.10,<3.13"
# dependencies = ["torch", "torchvision", "numpy", "pillow"]
# ///
"""Module 4, « Quatre façons de générer » : tirer au hasard dans l'espace latent d'un autoencodeur
ordinaire, puis dans celui d'un autoencodeur variationnel (VAE).

L'autoencodeur ordinaire (même architecture que le VAE, sans hasard ni pénalité) est entraîné ici sur
MNIST (cache de gen_espace_latent.py). Le VAE est celui de l'applet `espace-latent.html` : ses points
et son décodeur sont relus dans static/html/applets/data/espace-latent.json. Dans chaque carte, cinq
points sont tirés selon la même règle, celle du VAE (une cloche centrée sur l'origine, d'écart-type 1),
puis décodés. Le cercle pointillé contient 95 % de ces tirages.

    uv run scripts/gen_ae_vae.py
"""
import base64, json
from pathlib import Path
import numpy as np
import torch
from torch import nn
from torchvision import datasets
from PIL import Image, ImageDraw, ImageFont

torch.manual_seed(0)
RACINE = Path(__file__).resolve().parent
CACHE = Path.home() / ".cache" / "inf1901" / "mnist"
FOND, BORD, ENCRE, PALE, TEAL, PANNEAU = "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#2f6f6a", "#fbf7ee"
COUL = ['#c4564a', '#3a6ea5', '#2f6f6a', '#9a5b33', '#7b5ea7', '#d18f2f', '#4f8f3a', '#b5487f', '#5b7d8a', '#8a7a2e']
police = lambda t, gras=False: ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", t, index=1 if gras else 0)

train = datasets.MNIST(CACHE, train=True, download=True)
test = datasets.MNIST(CACHE, train=False, download=True)
dev = "mps" if torch.backends.mps.is_available() else "cpu"
X = train.data.float().div(255).view(-1, 784).to(dev)
enc = nn.Sequential(nn.Linear(784, 512), nn.ReLU(), nn.Linear(512, 256), nn.ReLU(), nn.Linear(256, 2)).to(dev)
dec = nn.Sequential(nn.Linear(2, 128), nn.ReLU(), nn.Linear(128, 256), nn.ReLU(), nn.Linear(256, 784)).to(dev)
opt = torch.optim.Adam(list(enc.parameters()) + list(dec.parameters()), lr=1e-3)
for epoque in range(30):
    perm = torch.randperm(len(X), device=dev)
    for i in range(0, len(X), 128):
        x = X[perm[i:i + 128]]
        perte = nn.functional.binary_cross_entropy_with_logits(dec(enc(x)), x, reduction="sum") / len(x)
        opt.zero_grad(); perte.backward(); opt.step()
    print(f"époque {epoque + 1:2d} : perte {perte.item():.1f}")
enc, dec = enc.cpu().eval(), dec.cpu().eval()
idx = torch.randperm(len(test.data))[:2000]
with torch.no_grad():
    z_ae = enc(test.data[idx].float().div(255).view(-1, 784)).numpy()
lab_ae = test.targets[idx].numpy()


def dec_ae(z):
    with torch.no_grad():
        return torch.sigmoid(dec(torch.tensor(z, dtype=torch.float32))).numpy()


d = json.loads((RACINE.parent / "static" / "html" / "applets" / "data" / "espace-latent.json").read_text())
couches = [(np.frombuffer(base64.b64decode(c["w"]), np.float16).astype(np.float32).reshape(c["entrees"], c["sorties"]),
            np.frombuffer(base64.b64decode(c["b"]), np.float16).astype(np.float32)) for c in d["couches"]]


def dec_vae(z):
    h = np.asarray(z, np.float32)
    for k, (w, b) in enumerate(couches):
        h = h @ w + b
        if k < 2:
            h = np.maximum(h, 0)
    return 1 / (1 + np.exp(-np.clip(h, -30, 30)))


pts_vae = np.array(d["points"])
z_vae, lab_vae = pts_vae[:, :2], pts_vae[:, 2].astype(int)

c, marge, n_tir = 440, 40, 10
W = 2 * marge + 2 * c + 60
H = 110 + c + 150
im = Image.new("RGB", (W, H), FOND)
dr = ImageDraw.Draw(im)
dr.rounded_rectangle((1, 1, W - 2, H - 2), radius=24, outline=BORD, width=2)
dr.text((W / 2, 42), "La même règle de tirage, dans deux espaces latents", fill=ENCRE, font=police(30, True), anchor="mm")
rng = np.random.default_rng(0)
for k, (titre, z, lab, decode) in enumerate([("autoencodeur ordinaire", z_ae, lab_ae, dec_ae),
                                              ("autoencodeur variationnel (VAE)", z_vae, lab_vae, dec_vae)]):
    x0 = marge + k * (c + 60)
    y0 = 110
    dr.text((x0 + c / 2, 84), titre, fill=TEAL, font=police(23, True), anchor="mm")
    dr.rectangle((x0, y0, x0 + c, y0 + c), fill=PANNEAU, outline=BORD, width=2)
    lo, hi = np.percentile(z, 2, axis=0), np.percentile(z, 98, axis=0)
    centre, demi = (lo + hi) / 2, (hi - lo).max() / 2 * 1.08
    vers = lambda p: (x0 + c / 2 + (p[0] - centre[0]) / demi * c / 2, y0 + c / 2 - (p[1] - centre[1]) / demi * c / 2)
    for p, e in zip(z, lab):
        X_, Y_ = vers(p)
        if x0 + 3 < X_ < x0 + c - 3 and y0 + 3 < Y_ < y0 + c - 3:
            dr.ellipse((X_ - 3, Y_ - 3, X_ + 3, Y_ + 3), fill=COUL[e])
    tirs = rng.standard_normal((n_tir, 2))
    imgs = decode(tirs)
    (cx_, cy_), r = vers((0, 0)), 2.0 / demi * c / 2
    dr.ellipse((cx_ - r, cy_ - r, cx_ + r, cy_ + r), outline=ENCRE, width=3)
    for j, p in enumerate(tirs):
        X_, Y_ = vers(p)
        dr.ellipse((X_ - 5, Y_ - 5, X_ + 5, Y_ + 5), fill=ENCRE, outline=PANNEAU, width=2)
        v = Image.fromarray((255 - imgs[j].reshape(28, 28) * 255).astype(np.uint8)).resize((40, 40), Image.NEAREST)
        vx = x0 + j * (c - 40) / (n_tir - 1)
        im.paste(v.convert("RGB"), (int(vx), y0 + c + 30))
        dr.rectangle((int(vx) - 1, y0 + c + 29, int(vx) + 40, y0 + c + 70), outline=BORD, width=2)
dr.text((W / 2, H - 34), "Points colorés : 2 000 vrais chiffres, rangés par l'encodeur. Points noirs : dix tirages, qui tombent presque tous dans le cercle.",
        fill=PALE, font=police(16), anchor="mm")
im.save(RACINE.parent / "static" / "images" / "module4" / "ae-vae.png")
print("ae-vae.png écrit", im.size)
