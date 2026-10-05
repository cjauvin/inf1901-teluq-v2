"""Module 3, « Tromper un réseau » : entraîne hors ligne le classifieur de chiffres de l'applet `adverse.html`.

Le classifieur est une régression logistique à dix sorties (10 × 784 poids), entraînée sur 6 000 chiffres dessinés avec
sept polices, en reprenant les tirages de l'applet (taille, décalage, rotation, gras). L'entraîner dans la page prenait
près de cinq secondes et gelait le chargement. Les poids sont exportés en float16, encodés en base64, dans
static/html/applets/data/adverse.json.

    uv run --with numpy --with pillow python scripts/gen_adverse.py
"""
import base64, json, math
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont

RACINE = Path(__file__).resolve().parent
SORTIE = RACINE.parent / "static" / "html" / "applets" / "data" / "adverse.json"
SUP = "/System/Library/Fonts/Supplemental/"
POLICES = [(SUP + f"{n}.ttf", SUP + f"{n} Bold.ttf") for n in ["Arial", "Georgia", "Courier New", "Verdana", "Times New Roman", "Trebuchet MS"]]
POLICES.append(("/System/Library/Fonts/Helvetica.ttc", "/System/Library/Fonts/Helvetica.ttc"))
N, D = 28, 784
NOMS = ['Arial', 'Georgia', 'Courier New', 'Verdana', 'Times New Roman', 'Trebuchet MS', 'Helvetica']
# PIL ne dessine pas exactement comme le canvas de Chrome : décalage (x, y) et facteur d'encre par police, mesurés en
# comparant les centres de masse et l'encre totale des chiffres 0 à 9, à 22 px, dans les deux rendus.
CORR = {
    "Arial": (-0.04, -1.9, 1.09),
    "Arial B": (-0.04, -1.96, 1.16),
    "Georgia": (0.03, -1.92, 1.16),
    "Georgia B": (0.08, -1.97, 1.11),
    "Courier New": (0.47, 0.12, 1.24),
    "Courier New B": (0.5, -0.12, 1.17),
    "Verdana": (-0.01, -3.11, 1.11),
    "Verdana B": (0.23, -3.11, 1.08),
    "Times New Roman": (0.48, -1.87, 1.14),
    "Times New Roman B": (0.49, -1.94, 1.09),
    "Trebuchet MS": (0.23, -2.04, 1.12),
    "Trebuchet MS B": (0.46, -2.03, 1.14),
    "Helvetica": (-0.02, 0.82, 1.13),
    "Helvetica B": (0.02, 1.15, 1.07),
}
rng = np.random.default_rng(12345)


def dessiner(c, police, taille, dx, dy, angle, gras):
    cx, cy, encre = CORR[NOMS[POLICES.index(police)] + (" B" if gras else "")]
    dx, dy = dx + cx, dy + cy
    f = ImageFont.truetype(police[1] if gras else police[0], round(taille), index=1 if gras and police[0].endswith(".ttc") else 0)
    im = Image.new("L", (N, N), 0)
    ImageDraw.Draw(im).text((N / 2, N / 2 + 1), str(c), fill=255, font=f, anchor="mm")
    im = im.rotate(-math.degrees(angle), resample=Image.BILINEAR, center=(N / 2, N / 2))
    im = im.transform((N, N), Image.AFFINE, (1, 0, -dx, 0, 1, -dy), resample=Image.BILINEAR)
    return np.minimum(1, np.asarray(im, np.float32).reshape(D) / 255 * encre)


def exemples(n):
    X, Y = np.zeros((n, D), np.float32), np.arange(n) % 10
    for k in range(n):
        r = rng.random(6)
        X[k] = dessiner(Y[k], POLICES[int(r[0] * len(POLICES))], 19 + r[1] * 5, (r[2] - 0.5) * 3, (r[3] - 0.5) * 2, (r[4] - 0.5) * 0.2, r[5] < 0.4)
    return X, Y


def probas(X, W, B):
    z = X @ W.T + B
    e = np.exp(z - z.max(1, keepdims=True))
    return e / e.sum(1, keepdims=True)


X, Y = exemples(6000)
W, B = np.zeros((10, D), np.float32), np.zeros(10, np.float32)
for ep in range(15):                                    # descente de gradient stochastique, comme dans l'ancienne applet
    taux = 0.5 / (1 + ep)
    for n in rng.permutation(len(X)):
        g = probas(X[n:n + 1], W, B)[0]
        g[Y[n]] -= 1
        W -= taux * (np.outer(g, X[n]) + 1e-4 * W)
        B -= taux * g
Xt, Yt = exemples(1000)
print(f"justesse sur 1 000 chiffres de test : {(probas(Xt, W, B).argmax(1) == Yt).mean():.1%}")
SORTIE.write_text(json.dumps({"w": base64.b64encode(W.astype(np.float16).tobytes()).decode(),
                              "b": base64.b64encode(B.astype(np.float16).tobytes()).decode()}, separators=(",", ":")))
print(SORTIE.name, "écrit,", SORTIE.stat().st_size // 1024, "Ko")
