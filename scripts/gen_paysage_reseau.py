"""Module 3, « Entraîner un réseau » : une tranche du paysage d'erreur d'un réseau, avec plusieurs creux.

Schéma : la surface est une fonction choisie pour l'illustration (une cuvette large et trois creux gaussiens), vue en
perspective. Les deux trajets sont de vraies descentes de gradient sur cette surface, à partir de deux points de départ.

    uv run --with numpy python scripts/gen_paysage_reseau.py
"""
import math
from pathlib import Path
import numpy as np

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module3"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "
CREUX = [(-1.1, -0.8, 1.0, 0.65), (1.2, 1.0, 0.55, 0.55), (1.3, -1.4, 0.4, 0.45)]   # x, y, profondeur, largeur


def f(x, y):
    z = 0.05 * (x ** 2 + y ** 2)
    for cx, cy, p, l in CREUX:
        z -= p * np.exp(-((x - cx) ** 2 + (y - cy) ** 2) / (2 * l ** 2))
    return z


def grad(x, y, h=1e-4):
    return (f(x + h, y) - f(x - h, y)) / (2 * h), (f(x, y + h) - f(x, y - h)) / (2 * h)


def descente(x, y, pas=0.18, n=60):
    t = [(x, y)]
    for _ in range(n):
        gx, gy = grad(x, y)
        x, y = x - pas * gx, y - pas * gy
        t.append((x, y))
    return t


L, N = 2.6, 34
W, H = 720, 520
az, el = math.radians(30), math.radians(40)


def proj(x, y, z):
    xr = x * math.cos(az) - y * math.sin(az)
    yr = x * math.sin(az) + y * math.cos(az)
    return 380 + 80 * xr, 318 - 80 * (yr * math.sin(el)) - 85 * z * math.cos(el), yr   # yr : profondeur


xs = np.linspace(-L, L, N)
Z = f(*np.meshgrid(xs, xs, indexing="ij"))
zmin, zmax = Z.min(), Z.max()
quads = []
for i in range(N - 1):
    for j in range(N - 1):
        pts = [(xs[i], xs[j]), (xs[i + 1], xs[j]), (xs[i + 1], xs[j + 1]), (xs[i], xs[j + 1])]
        P = [proj(a, b, f(a, b)) for a, b in pts]
        prof = sum(p[2] for p in P) / 4
        zc = sum(f(a, b) for a, b in pts) / 4
        quads.append((prof, P, zc))
quads.sort(key=lambda q: -q[0])                        # du fond vers l'avant

o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Le paysage d'erreur d'un réseau</title>",
     "<desc>Une surface en trois dimensions, vue en perspective, au-dessus du plan de deux poids du réseau. La hauteur de la surface "
     "est l'erreur. Contrairement à une cuvette, la surface est accidentée : elle a plusieurs creux de profondeurs différentes. Deux "
     "billes partent de deux points de départ différents et descendent la pente, pas à pas. La première arrive au fond du creux le plus "
     "profond, la seconde s'arrête dans un creux moins profond, d'où elle ne peut plus sortir en descendant.</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Une tranche du paysage d\'erreur d\'un réseau{NB}: plusieurs creux</text>']
for _, P, zc in quads:
    t = (zc - zmin) / (zmax - zmin)                    # bas : teal foncé, haut : parchemin clair
    r = int(47 + t * (240 - 47)); g = int(111 + t * (231 - 111)); b = int(106 + t * (211 - 106))
    o.append(f'<polygon points="{" ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in P)}" fill="rgb({r},{g},{b})" stroke="#ffffff" stroke-opacity="0.35" stroke-width="0.6"/>')


def trajet(depart, coul, num):
    t = descente(*depart)
    P = [proj(x, y, f(x, y) + 0.02) for x, y in t]
    o.append(f'<polyline points="{" ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in P)}" fill="none" stroke="{coul}" stroke-width="3" stroke-linejoin="round"/>')
    for p in P[1:-1:3]:
        o.append(f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="2.6" fill="{coul}"/>')
    x0, y0 = P[0][:2]
    o.append(f'<circle cx="{x0:.1f}" cy="{y0:.1f}" r="8" fill="{FOND}" stroke="{coul}" stroke-width="3"/>')
    o.append(f'<text x="{x0:.1f}" y="{y0 + 4:.1f}" font-size="10.5" fill="{coul}" text-anchor="middle" font-weight="700">{num}</text>')
    x1, y1 = P[-1][:2]
    o.append(f'<circle cx="{x1:.1f}" cy="{y1:.1f}" r="7" fill="{coul}" stroke="#fff" stroke-width="2"/>')
    return P


P1 = trajet((-2.2, 0.9), ROUGE, 1)
P2 = trajet((2.4, -0.6), BRUN, 2)
o.append(f'<text x="40" y="70" font-size="12.5" fill="{ROUGE}" font-weight="700">Départ 1{NB}: la bille arrive au creux le plus profond.</text>')
o.append(f'<text x="40" y="90" font-size="12.5" fill="{BRUN}" font-weight="700">Départ 2{NB}: elle s\'arrête dans un creux moins profond,</text>')
o.append(f'<text x="40" y="108" font-size="12.5" fill="{BRUN}" font-weight="700">d\'où elle ne peut plus sortir en descendant.</text>')
o.append(f'<text x="{W / 2}" y="{H - 34}" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle">Deux axes{NB}: deux poids du réseau, parmi des milliers. Hauteur{NB}: l\'erreur.</text>')
o.append(f'<text x="{W / 2}" y="{H - 16}" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle">(schéma{NB}: la forme du paysage est inventée, mais les trajets sont de vraies descentes de gradient)</text>')
o.append("</svg>")
(OUT / "paysage-reseau.svg").write_text("\n".join(o) + "\n")
print("paysage-reseau.svg écrit", "fin 1 :", [round(float(v), 2) for v in descente(-2.2, 0.9)[-1]], "fin 2 :", [round(float(v), 2) for v in descente(2.4, -0.6)[-1]], "z :", round(float(zmin), 2), round(float(zmax), 2))
