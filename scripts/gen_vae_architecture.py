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
    buf = io.BytesIO(); Image.fromarray(rgb).resize((84, 84), Image.NEAREST).save(buf, "PNG")
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


W, H = 760, 614
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Autoencodeur et autoencodeur variationnel</title>",
     "<desc>Deux rangées, chacune en forme de sablier. En haut, l'autoencodeur ordinaire : un 7 manuscrit de 784 nombres entre "
     "dans l'encodeur, qui le réduit à un code de deux nombres seulement ; le décodeur reconstruit à partir de ces deux nombres une "
     "image de 784 nombres. Sous le code, une petite carte montre ces deux nombres comme un point de l'espace latent. L'erreur de "
     "reconstruction compare l'entrée et la sortie. En bas, l'autoencodeur variationnel : l'encodeur donne deux paires de nombres, "
     "le centre et la taille d'une zone floue ; deux nombres sont tirés au hasard dans cette zone, et le décodeur reconstruit le 7 à "
     "partir d'eux. Sur la petite carte, la zone est une tache en forme de cloche, avec le point tiré, et une pénalité la ramène vers "
     "le centre de la carte. Les éléments propres à l'autoencodeur variationnel sont en rouge.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker>'
     f'<marker id="pr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{ROUGE}"/></marker>'
     f'<radialGradient id="cloche"><stop offset="0" stop-color="{ROUGE}" stop-opacity="0.55"/>'
     f'<stop offset="1" stop-color="{ROUGE}" stop-opacity="0"/></radialGradient></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">De l\'autoencodeur à l\'autoencodeur variationnel</text>']
D0 = 46
XI, XE0, XE1, XP, XT, XZ, XD0, XD1, XO = D0, D0 + 100, D0 + 180, D0 + 202, D0 + 312, D0 + 344, D0 + 446, D0 + 526, D0 + 542
LX, LY = (-2.7, 0.7), (-2.9, 0.5)                            # la carte, cadrée sur la zone et le centre
TI, TM, CW, CH = 84, 76, 40, 20                               # image, carte, case d'un nombre
num = lambda v: f"{v:.2f}".replace(".", ",").replace("-", "−")


def fleche(x1, y1, x2, y2, coul=GRIS, m="p", l=1.6):
    o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{coul}" stroke-width="{l}" marker-end="url(#{m})"/>')


def trapeze(x0, x1, yc, titre, a, b):
    o.append(f'<polygon points="{x0},{yc - a} {x1},{yc - b} {x1},{yc + b} {x0},{yc + a}" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="1.8"/>')
    o.append(f'<text x="{(x0 + x1) / 2}" y="{yc + 4}" font-size="11.5" fill="{ENCRE}" text-anchor="middle" font-weight="600">{titre}</text>')


def image(x, yc, url, legende):
    o.append(f'<image x="{x}" y="{yc - TI / 2}" width="{TI}" height="{TI}" xlink:href="{url}"/>')
    o.append(f'<rect x="{x}" y="{yc - TI / 2}" width="{TI}" height="{TI}" fill="none" stroke="{BORD}" stroke-width="1.5"/>')
    o.append(f'<text x="{x + TI / 2}" y="{yc + TI / 2 + 17}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">{legende}{NB}: <tspan font-weight="700" fill="{ENCRE}">784{NB}nombres</tspan></text>')


def paire(x, y, valeurs, coul):                               # deux nombres, deux petites cases
    for j, v in enumerate(valeurs):
        o.append(f'<rect x="{x + j * CW}" y="{y}" width="{CW}" height="{CH}" fill="{PANNEAU}" stroke="{coul}" stroke-width="1.5"/>')
        o.append(f'<text x="{x + j * CW + CW / 2}" y="{y + 14}" font-size="10.5" fill="{ENCRE}" text-anchor="middle">{num(v)}</text>')


def carte(xc, y0, gauche):                                    # petit encart : le code vu comme un point de la carte
    x0 = xc - TM / 2
    o.append(f'<rect x="{x0}" y="{y0}" width="{TM}" height="{TM}" fill="{FOND}" stroke="{AXE}" stroke-width="1.2"/>')
    vers = lambda p: (x0 + (p[0] - LX[0]) / (LX[1] - LX[0]) * TM, y0 + TM - (p[1] - LY[0]) / (LY[1] - LY[0]) * TM)
    cx, cy = vers((0, 0))
    o.append(f'<path d="M{cx - 5} {cy} L{cx + 5} {cy} M{cx} {cy - 5} L{cx} {cy + 5}" stroke="{GRIS}" stroke-width="1.2"/>')
    o.append(f'<text x="{cx - 8}" y="{cy + 4}" font-size="9.5" fill="{GRIS}" text-anchor="end">centre</text>')
    for k, l in enumerate(gauche):
        o.append(f'<text x="{x0 - 10}" y="{y0 + TM / 2 - 4 + 14 * k}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="end">{l}</text>')
    return vers, (cx, cy)


def rangee(y0, h, titre):
    o.append(f'<rect x="20" y="{y0}" width="{W - 40}" height="{h}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
    o.append(f'<text x="36" y="{y0 + 22}" font-size="13" fill="{BRUN}" font-weight="700">{titre}</text>')


def erreur(y):
    a, b = XI + TI / 2, XO + TI / 2
    o.append(f'<path d="M{a} {y - 8} L{a} {y} L{b} {y} L{b} {y - 8}" fill="none" stroke="{GRIS}" stroke-width="1.2" stroke-dasharray="4 3"/>')
    o.append(f'<text x="{(a + b) / 2}" y="{y + 15}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">erreur de reconstruction{NB}: l\'entrée et la sortie doivent se ressembler</text>')


def relier(xc, y1, y2):                                       # pointillé du code vers sa carte
    o.append(f'<line x1="{xc}" y1="{y1}" x2="{xc}" y2="{y2}" stroke="{AXE}" stroke-width="1.2" stroke-dasharray="3 3"/>')


# ── autoencodeur ordinaire ──
rangee(50, 248, "Autoencodeur ordinaire")
yc = 128
image(XI, yc, png(entree), "entrée")
trapeze(XE0, XE1, yc, "encodeur", 42, 12)
fleche(XI + TI + 4, yc, XE0 - 4, yc)
fleche(XE1 + 4, yc, XZ - 4, yc)
paire(XZ, yc - CH / 2, mu, ENCRE)
o.append(f'<text x="{XZ + CW}" y="{yc - CH / 2 - 8}" font-size="11.5" fill="{ENCRE}" text-anchor="middle" font-weight="700">code{NB}: 2{NB}nombres</text>')
fleche(XZ + 2 * CW + 4, yc, XD0 - 4, yc)
trapeze(XD0, XD1, yc, "décodeur", 12, 42)
image(XO, yc, png(decoder(mu)), "sortie")
fleche(XD1 + 4, yc, XO - 4, yc)
relier(XZ + CW, yc + CH / 2, yc + 44)
vers, _ = carte(XZ + CW, yc + 44, ["le même code, vu comme", "un point de l'espace latent"])
px, py = vers(mu)
o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3.5" fill="{ENCRE}"/>')
erreur(yc + 142)

# ── autoencodeur variationnel ──
rangee(310, 288, "Autoencodeur variationnel (VAE)")
yc = 396
image(XI, yc, png(entree), "entrée")
trapeze(XE0, XE1, yc, "encodeur", 42, 30)
fleche(XI + TI + 4, yc, XE0 - 4, yc)
for dy, t, vals in ((-26, "centre", mu), (26, "taille", (SIGMA, SIGMA))):
    paire(XP, yc + dy - CH / 2, vals, ROUGE)
    ly = yc + dy - CH / 2 - 7 if dy < 0 else yc + dy + CH / 2 + 15
    o.append(f'<text x="{XP + CW}" y="{ly}" font-size="11" fill="{ROUGE}" text-anchor="middle" font-weight="600">{t}{NB}: 2{NB}nombres</text>')
    fleche(XE1 + 2, yc + dy * 0.75, XP - 3, yc + dy)
    fleche(XP + 2 * CW + 2, yc + dy, XT - 14, yc)
o.append(f'<circle cx="{XT}" cy="{yc}" r="11" fill="{PANNEAU}" stroke="{ROUGE}" stroke-width="1.6"/>')
o.append(f'<text x="{XT}" y="{yc + 5}" font-size="13" fill="{ROUGE}" text-anchor="middle" font-weight="700">?</text>')
o.append(f'<text x="{XT}" y="{yc + 28}" font-size="11" fill="{ROUGE}" text-anchor="middle" font-weight="600">tirage</text>')
fleche(XT + 12, yc, XZ - 4, yc)
paire(XZ, yc - CH / 2, z, ENCRE)
o.append(f'<text x="{XZ + CW}" y="{yc - CH / 2 - 8}" font-size="11.5" fill="{ENCRE}" text-anchor="middle" font-weight="700">code{NB}: 2{NB}nombres</text>')
fleche(XZ + 2 * CW + 4, yc, XD0 - 4, yc)
trapeze(XD0, XD1, yc, "décodeur", 12, 42)
image(XO, yc, png(decoder(z)), "sortie")
fleche(XD1 + 4, yc, XO - 4, yc)
relier(XZ + CW, yc + CH / 2, yc + 56)
vers, centre = carte(XZ + CW, yc + 56, ["zone floue, et le point", "tiré au hasard, sur la carte"])
px, py = vers(mu)
r = SIGMA / (LX[1] - LX[0]) * TM * 2.4
o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r:.1f}" fill="url(#cloche)"/>')
o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r * 0.62:.1f}" fill="none" stroke="{ROUGE}" stroke-width="1" stroke-dasharray="2 2"/>')
zx, zy = vers(z)
o.append(f'<circle cx="{zx:.1f}" cy="{zy:.1f}" r="3.5" fill="{ENCRE}"/>')
dx, dy = centre[0] - px, centre[1] - py; n = (dx * dx + dy * dy) ** 0.5
fleche(px + dx / n * (r * 0.62 + 2), py + dy / n * (r * 0.62 + 2), centre[0] - dx / n * 7, centre[1] - dy / n * 7, ROUGE, "pr", 1.6)
o.append(f'<text x="{XZ + CW + TM / 2 + 10}" y="{yc + 56 + TM / 2 + 4}" font-size="10.5" fill="{ROUGE}">+{NB}pénalité{NB}: ramener</text>')
o.append(f'<text x="{XZ + CW + TM / 2 + 10}" y="{yc + 56 + TM / 2 + 18}" font-size="10.5" fill="{ROUGE}">la zone vers le centre</text>')
erreur(yc + 162)
o.append("</svg>")
(OUT / "ae-et-vae.svg").write_text("\n".join(o) + "\n")
print("ae-et-vae.svg écrit ; centre", mu.round(2), "tirage", z.round(2))
