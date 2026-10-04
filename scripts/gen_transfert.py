"""Module 3, « Voir : les réseaux convolutifs » : l'apprentissage par transfert."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module3"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "
W, H = 700, 420
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>L'apprentissage par transfert</title>",
     f"<desc>Deux rangées. En haut, un réseau pré-entraîné sur ImageNet{NB}: quatre couches en bleu, puis une dernière couche en gris qui répond "
     f"«{FINE}chien, voiture, chat…{FINE}». En bas, le même réseau ajusté pour une nouvelle tâche{NB}: les quatre couches bleues sont conservées, et la dernière "
     f"couche est remplacée par une nouvelle, en rouge, qui répond «{FINE}lésion bénigne ou mélanome{FINE}».</desc>",
     f'<defs><marker id="pointe" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="34" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Réutiliser un réseau déjà entraîné</text>']


def rangee(y, titre, entree, derniere, coul_derniere, sortie):
    o.append(f'<text x="40" y="{y - 52}" font-size="13" fill="{ENCRE}" font-weight="700">{titre}</text>')
    o.append(f'<rect x="40" y="{y - 32}" width="70" height="64" rx="6" fill="{PANNEAU}" stroke="{AXE}"/>')
    o.append(f'<text x="75" y="{y + 4}" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">{entree}</text>')
    x = 130
    for k in range(4):
        o.append(f'<line x1="{x - 18}" y1="{y}" x2="{x - 2}" y2="{y}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#pointe)"/>')
        o.append(f'<rect x="{x}" y="{y - 40}" width="44" height="80" rx="6" fill="{BLEU}" fill-opacity="0.18" stroke="{BLEU}" stroke-width="2"/>')
        x += 64
    o.append(f'<line x1="{x - 18}" y1="{y}" x2="{x - 2}" y2="{y}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#pointe)"/>')
    o.append(f'<rect x="{x}" y="{y - 40}" width="44" height="80" rx="6" fill="{coul_derniere}" fill-opacity="0.2" stroke="{coul_derniere}" stroke-width="2.4"/>')
    if derniere:
        o.append(f'<text x="{x + 22}" y="{y + 58}" font-size="11" fill="{coul_derniere}" text-anchor="middle" font-weight="700">{derniere}</text>')
    o.append(f'<line x1="{x + 46}" y1="{y}" x2="{x + 72}" y2="{y}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#pointe)"/>')
    for k, ligne in enumerate(sortie):
        o.append(f'<text x="{x + 80}" y="{y - 6 + k * 16}" font-size="12" fill="{ENCRE}">{ligne}</text>')


rangee(130, "1. Pré-entraîné sur ImageNet (des millions d'images)", "photo", "", GRIS, ["chien, voiture,", "chat… (1 000 classes)"])
rangee(335, "2. Ajusté pour une nouvelle tâche (quelques milliers d'images)", "lésion", "nouvelle couche", ROUGE, ["lésion bénigne", "ou mélanome"])
# accolade « conservées »
o.append(f'<path d="M130 178 v10 h236 v-10" fill="none" stroke="{TEAL}" stroke-width="1.8"/>')
o.append(f'<text x="248" y="208" font-size="12.5" fill="{TEAL}" text-anchor="middle" font-weight="700">couches conservées{NB}: traits, textures, formes</text>')
o.append(f'<text x="{W / 2}" y="{H - 16}" font-size="12.5" fill="{GRIS}" text-anchor="middle">Seule la fin du réseau est remplacée{NB}; le début, qui sait déjà «{FINE}voir{FINE}», est réutilisé.</text>')
o.append("</svg>")
(OUT / "apprentissage-transfert.svg").write_text("\n".join(o) + "\n")
print("apprentissage-transfert.svg écrit")
