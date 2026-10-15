"""Module 4, « Passer à l'échelle », encadré sur le test du pélican de Simon Willison : quatre réponses à la même
demande, « Generate an SVG of a pelican riding a bicycle », de 2024 à 2026. Les images, tirées du blogue de Simon
Willison (simonwillison.net), sont réduites dans static/images/module4/pelicans/ et intégrées à la figure."""
import base64
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
SRC = RACINE / "static" / "images" / "module4" / "pelicans"
OUT = RACINE / "static" / "images" / "module4" / "pelicans-willison.svg"
FOND, BORD, ENCRE, ENCRE_PALE, TEAL = "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#2f6f6a"
NB = " "
PANNEAUX = [("gpt-4o-mini.jpg", "GPT-4o mini", f"octobre{NB}2024"),
            ("gpt-5.jpg", "GPT-5", f"août{NB}2025"),
            ("gemini-3.jpg", "Gemini 3 Pro", f"novembre{NB}2025"),
            ("fable-5.1.jpg", "Claude Fable 5.1", f"septembre{NB}2026")]
W, H = 840, 732
LW, LH = 380, 285
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Un pélican à vélo, de 2024 à 2026</title>",
     "<desc>Quatre dessins produits par des modèles de langage à partir de la même demande, « dessiner en SVG un pélican "
     "qui fait du vélo ». GPT-4o mini, octobre 2024 : deux disques noirs pour les roues, deux traits pour le cadre, un "
     "oiseau gris posé dessus, sans bec de pélican. GPT-5, août 2025 : un vrai vélo, avec rayons, pédalier et garde-boue, "
     "et un oiseau au long bec orange assis sur la selle, les pattes vers les pédales. Gemini 3 Pro, novembre 2025 : un "
     "pélican blanc à la poche orange, assis sur un vélo rouge, une aile tendue vers le guidon, sur fond de ciel et "
     "d'herbe. Claude Fable 5.1, septembre 2026 : une illustration soignée, un pélican casqué qui pédale sur une plage, "
     "un poisson dans le panier du vélo, avec la mer, un voilier, des nuages et le soleil.</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="34" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">«{NB}Generate an SVG of a pelican riding a bicycle{NB}»</text>',
     f'<text x="{W / 2}" y="56" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">La même demande, faite à des modèles successifs</text>']
for k, (f, nom, date) in enumerate(PANNEAUX):
    x = 30 + (k % 2) * (LW + 20)
    y = 76 + (k // 2) * (LH + 50)
    b64 = base64.b64encode((SRC / f).read_bytes()).decode()
    o.append(f'<rect x="{x - 1}" y="{y - 1}" width="{LW + 2}" height="{LH + 2}" rx="6" fill="#ffffff" stroke="{BORD}"/>')
    o.append(f'<image x="{x}" y="{y}" width="{LW}" height="{LH}" preserveAspectRatio="xMidYMid meet" href="data:image/jpeg;base64,{b64}"/>')
    o.append(f'<text x="{x + LW / 2}" y="{y + LH + 22}" font-size="12.5" fill="{TEAL}" text-anchor="middle"><tspan font-weight="700">{nom}</tspan>'
             f'<tspan fill="{ENCRE_PALE}">, {date}</tspan></text>')
o.append("</svg>")
OUT.write_text("\n".join(o) + "\n")
print(OUT.name, "écrit")
