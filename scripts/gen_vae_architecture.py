"""Module 4, « Quatre façons de générer » : l'autoencodeur ordinaire et l'autoencodeur variationnel, côte à côte.

Le chiffre d'entrée est un vrai 7 de MNIST, choisi au cœur de la région des 7 ; sa position dans l'espace latent et les images de sortie viennent du
décodeur de l'applet (static/html/applets/data/espace-latent.json). La taille de la zone floue est illustrative :
l'applet ne garde que le décodeur.

    uv run --with numpy --with pillow python scripts/gen_vae_architecture.py
"""
import base64, io, json
from pathlib import Path
import numpy as np
from PIL import Image

RACINE = Path(__file__).resolve().parent
OUT = RACINE.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "

d = json.loads((RACINE.parent / "static" / "html" / "applets" / "data" / "espace-latent.json").read_text())
couches = [(np.frombuffer(base64.b64decode(c["w"]), np.float16).astype(np.float32).reshape(c["entrees"], c["sorties"]),
            np.frombuffer(base64.b64decode(c["b"]), np.float16).astype(np.float32)) for c in d["couches"]]


def decoder(z):
    h = np.asarray(z, np.float32)
    for k, (w, b) in enumerate(couches):
        h = h @ w + b
        if k < len(couches) - 1:
            h = np.maximum(h, 0)
    return (1 / (1 + np.exp(-np.clip(h, -30, 30)))).reshape(28, 28)


pts = np.array([p[:2] for p in d["points"]]); lab = np.array([p[2] for p in d["points"]])
k = 57                                                        # un 7 au cœur de sa région : les points voisins sont tous des 7
mu = pts[k]
SIGMA = 0.40                                                  # zone illustrative
EPS = mu / np.linalg.norm(mu)                                 # un tirage du côté opposé au centre
z = mu + SIGMA * EPS
cache = Path.home() / ".cache" / "inf1901" / "mnist" / "MNIST" / "raw"
entree = np.frombuffer((cache / "t10k-images-idx3-ubyte").read_bytes(), np.uint8, offset=16).reshape(-1, 28, 28)[d["indices"][k]] / 255


def png(x):                                                  # encre sombre sur fond de panneau
    f, e = np.array([251, 247, 238]), np.array([58, 53, 49])
    rgb = (f * (1 - x[..., None]) + e * x[..., None]).astype(np.uint8)
    buf = io.BytesIO(); Image.fromarray(rgb).resize((140, 140), Image.NEAREST).save(buf, "PNG")
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


W, H = 800, 550
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Autoencodeur et autoencodeur variationnel</title>",
     "<desc>Deux rangées. En haut, l'autoencodeur ordinaire : un 7 manuscrit entre dans l'encodeur, qui le réduit à un point sur "
     "une petite carte de l'espace latent ; le décodeur reconstruit le 7 à partir de ce point. L'erreur de reconstruction compare "
     "l'entrée et la sortie. En bas, l'autoencodeur variationnel : l'encodeur donne deux sorties, le centre et la taille d'une zone "
     "floue, dessinée sur la carte comme une tache en forme de cloche ; un point est tiré au hasard dans cette zone, et le décodeur "
     "reconstruit le 7 à partir de ce point. Une pénalité ramène la zone vers le centre de la carte. Les éléments propres à "
     "l'autoencodeur variationnel sont en rouge.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker>'
     f'<marker id="pr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{ROUGE}"/></marker>'
     f'<radialGradient id="cloche"><stop offset="0" stop-color="{ROUGE}" stop-opacity="0.55"/>'
     f'<stop offset="1" stop-color="{ROUGE}" stop-opacity="0"/></radialGradient></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">De l\'autoencodeur à l\'autoencodeur variationnel</text>']
XI, XE0, XE1, XC0, XC1, XM, XD0, XD1, XO = 40, 196, 280, 302, 368, 392, 482, 566, 586
TI, TM = 140, 66                                              # côté des images et de la carte : l'espace latent est petit
LX, LY = (-2.7, 0.7), (-2.9, 0.5)                            # la carte, agrandie autour de la zone et du centre


def fleche(x1, y1, x2, y2, coul=GRIS, m="p", l=1.6):
    o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{coul}" stroke-width="{l}" marker-end="url(#{m})"/>')


def trapeze(x0, x1, yc, titre, retrecit):
    a, b = (70, 16) if retrecit else (16, 70)
    o.append(f'<polygon points="{x0},{yc - a} {x1},{yc - b} {x1},{yc + b} {x0},{yc + a}" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="1.8"/>')
    o.append(f'<text x="{(x0 + x1) / 2}" y="{yc + 4}" font-size="11.5" fill="{ENCRE}" text-anchor="middle" font-weight="600">{titre}</text>')


def image(x, yc, url, legende):
    o.append(f'<image x="{x}" y="{yc - TI / 2}" width="{TI}" height="{TI}" xlink:href="{url}"/>')
    o.append(f'<rect x="{x}" y="{yc - TI / 2}" width="{TI}" height="{TI}" fill="none" stroke="{BORD}" stroke-width="1.5"/>')
    o.append(f'<text x="{x + TI / 2}" y="{yc + TI / 2 + 16}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">{legende}</text>')


def carte(yc):
    y0 = yc - TM / 2
    o.append(f'<rect x="{XM}" y="{y0}" width="{TM}" height="{TM}" fill="{FOND}" stroke="{AXE}" stroke-width="1.2"/>')
    vers = lambda p: (XM + (p[0] - LX[0]) / (LX[1] - LX[0]) * TM, y0 + TM - (p[1] - LY[0]) / (LY[1] - LY[0]) * TM)
    o.append(f'<text x="{XM + TM / 2}" y="{y0 + TM + 16}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">espace latent</text>')
    cx, cy = vers((0, 0))                                     # le centre de la carte
    o.append(f'<path d="M{cx - 5} {cy} L{cx + 5} {cy} M{cx} {cy - 5} L{cx} {cy + 5}" stroke="{GRIS}" stroke-width="1.2"/>')
    o.append(f'<text x="{cx - 9}" y="{cy + 4}" font-size="10" fill="{GRIS}" text-anchor="end">centre</text>')
    return vers, (cx, cy)


def rangee(y0, h, titre):
    o.append(f'<rect x="20" y="{y0}" width="{W - 40}" height="{h}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
    o.append(f'<text x="36" y="{y0 + 22}" font-size="13" fill="{BRUN}" font-weight="700">{titre}</text>')


def erreur(y):
    a, b = XI + TI / 2, XO + TI / 2
    o.append(f'<path d="M{a} {y - 8} L{a} {y} L{b} {y} L{b} {y - 8}" fill="none" stroke="{GRIS}" stroke-width="1.2" stroke-dasharray="4 3"/>')
    o.append(f'<text x="{(a + b) / 2}" y="{y + 15}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">erreur de reconstruction{NB}: l\'entrée et la sortie doivent se ressembler</text>')


# ── autoencodeur ordinaire ──
rangee(50, 236, "Autoencodeur ordinaire")
yc = 156
image(XI, yc, png(entree), "entrée")
trapeze(XE0, XE1, yc, "encodeur", True)
fleche(XI + TI + 4, yc, XE0 - 4, yc)
vers, _ = carte(yc)
fleche(XE1 + 4, yc, XM - 4, yc)
o.append(f'<text x="{(XE1 + XM) / 2}" y="{yc - 8}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">un point</text>')
px, py = vers(mu)
o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4" fill="{ENCRE}"/>')
fleche(XM + TM + 4, yc, XD0 - 4, yc)
trapeze(XD0, XD1, yc, "décodeur", False)
image(XO, yc, png(decoder(mu)), "sortie")
fleche(XD1 + 4, yc, XO - 4, yc)
erreur(yc + 104)

# ── autoencodeur variationnel ──
rangee(298, 236, "Autoencodeur variationnel (VAE)")
yc = 404
image(XI, yc, png(entree), "entrée")
trapeze(XE0, XE1, yc, "encodeur", True)
fleche(XI + TI + 4, yc, XE0 - 4, yc)
for dy, t in ((-22, "centre"), (22, "taille")):
    o.append(f'<rect x="{XC0}" y="{yc + dy - 13}" width="{XC1 - XC0}" height="26" rx="6" fill="{PANNEAU}" stroke="{ROUGE}" stroke-width="1.6"/>')
    o.append(f'<text x="{(XC0 + XC1) / 2}" y="{yc + dy + 4}" font-size="11.5" fill="{ENCRE}" text-anchor="middle" font-weight="600">{t}</text>')
    fleche(XE1 + 2, yc, XC0 - 3, yc + dy)
    fleche(XC1 + 2, yc + dy, XM - 3, yc)
vers, centre = carte(yc)
px, py = vers(mu)
r = SIGMA / (LX[1] - LX[0]) * TM * 2.4
o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r:.1f}" fill="url(#cloche)"/>')
o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r * 0.62:.1f}" fill="none" stroke="{ROUGE}" stroke-width="1" stroke-dasharray="2 2"/>')
zx, zy = vers(z)
o.append(f'<circle cx="{zx:.1f}" cy="{zy:.1f}" r="4" fill="{ENCRE}"/>')
# la pénalité tire la zone vers le centre
dx, dy = centre[0] - px, centre[1] - py; n = (dx * dx + dy * dy) ** 0.5
fleche(px + dx / n * (r * 0.62 + 2), py + dy / n * (r * 0.62 + 2), centre[0] - dx / n * 7, centre[1] - dy / n * 7, ROUGE, "pr", 1.6)
fleche(XM + TM + 4, yc, XD0 - 4, yc)
o.append(f'<text x="{XM + TM / 2}" y="{yc - TM / 2 - 24}" font-size="11" fill="{ROUGE}" text-anchor="middle">zone floue, et un</text>')
o.append(f'<text x="{XM + TM / 2}" y="{yc - TM / 2 - 10}" font-size="11" fill="{ROUGE}" text-anchor="middle">point tiré au hasard</text>')
trapeze(XD0, XD1, yc, "décodeur", False)
image(XO, yc, png(decoder(z)), "sortie")
fleche(XD1 + 4, yc, XO - 4, yc)
erreur(yc + 104)
o.append(f'<text x="{XM + TM / 2}" y="{yc + TI / 2 + 16}" font-size="11" fill="{ROUGE}" text-anchor="middle">+{NB}pénalité{NB}: ramener la zone vers le centre de la carte</text>')
o.append("</svg>")
(OUT / "ae-et-vae.svg").write_text("\n".join(o) + "\n")
print("ae-et-vae.svg écrit ; centre", mu.round(2), "tirage", z.round(2))
