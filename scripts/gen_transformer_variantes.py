"""Module 4, « Prédire le mot suivant » : les trois façons d'assembler le Transformer
(encodeur et décodeur, encodeur seul, décodeur seul), en silhouettes simplifiées du schéma de 2017."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
W, H = 780, 352
lp, e, x0, y0 = 244, 10, 14, 52
BL, BH = 92, 36
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Trois façons d'assembler le Transformer</title>",
     "<desc>Trois silhouettes simplifiées du Transformer de 2017. Première : encodeur et décodeur, les deux colonnes, reliées par "
     "l'attention croisée ; c'est le Transformer de 2017 et T5, pour traduire et résumer. Deuxième : encodeur seul, le décodeur est "
     "grisé ; l'encodeur donne un vecteur par mot ; c'est BERT, pour comprendre et classer. Troisième : décodeur seul, l'encodeur et "
     "l'attention croisée sont grisés ; le décodeur donne le mot suivant ; c'est GPT et les grands modèles de langue, pour générer "
     "du texte.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker>'
     f'<marker id="pb" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{BLEU}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Trois façons d\'assembler le Transformer</text>']


def etiquette(cx, y, texte, attrs):
    lignes = texte.split(" ") if " " in texte else [texte]           # « attention masquée » sur deux lignes
    for k, l in enumerate(lignes):
        o.append(f'<text x="{cx}" y="{y + 20 + (k - (len(lignes) - 1) / 2) * 12}" font-size="10.5" text-anchor="middle" {attrs}>{l}</text>')


def boite(cx, y, texte, coul, actif):
    if actif:
        o.append(f'<rect x="{cx - BL / 2}" y="{y}" width="{BL}" height="{BH}" rx="6" fill="{PANNEAU}" stroke="{coul}" stroke-width="1.6"/>')
        etiquette(cx, y, texte, f'fill="{ENCRE}" font-weight="600"')
    else:
        o.append(f'<rect x="{cx - BL / 2}" y="{y}" width="{BL}" height="{BH}" rx="6" fill="none" stroke="{AXE}" stroke-width="1.2" stroke-dasharray="3 3"/>')
        etiquette(cx, y, texte, f'fill="{AXE}"')


def cadre(cx, haut, bas, titre, actif):
    coul = TEAL if actif else AXE
    o.append(f'<rect x="{cx - BL / 2 - 6}" y="{haut}" width="{BL + 12}" height="{bas - haut}" rx="9" fill="none" stroke="{coul}" '
             f'stroke-width="{1.8 if actif else 1.2}" stroke-dasharray="5 4"/>')
    o.append(f'<text x="{cx}" y="{bas + 18}" font-size="11.5" fill="{coul}" text-anchor="middle" font-weight="700">{titre}</text>')


def sortie(cx, haut, texte):
    o.append(f'<line x1="{cx}" y1="{haut}" x2="{cx}" y2="{haut - 22}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')
    o.append(f'<text x="{cx}" y="{haut - 30}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle" font-style="italic">{texte}</text>')


def panneau(px, titre, exemples, usage, enc, dec):
    o.append(f'<rect x="{px}" y="{y0}" width="{lp}" height="{H - y0 - 16}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
    ce, cd = px + 12 + BL / 2, px + lp - 12 - BL / 2
    yb = [210, 164, 118]                                    # trois rangées de boîtes, du bas vers le haut
    # encodeur : auto-attention, puis réseau
    cadre(ce, yb[1] - 8, yb[0] + BH + 8, "encodeur", enc)
    boite(ce, yb[0], "auto-attention", ROUGE, enc)
    boite(ce, yb[1], "réseau", TEAL, enc)
    # décodeur : attention masquée, attention croisée, réseau
    cadre(cd, yb[2] - 8, yb[0] + BH + 8, "décodeur", dec)
    boite(cd, yb[0], "attention masquée", ROUGE, dec)
    boite(cd, yb[1], "attention croisée", ROUGE, enc and dec)
    boite(cd, yb[2], "réseau", TEAL, dec)
    # l'encodeur nourrit l'attention croisée
    croise = enc and dec
    o.append(f'<line x1="{ce + BL / 2 + 1}" y1="{yb[1] + BH / 2}" x2="{cd - BL / 2 - 2}" y2="{yb[1] + BH / 2}" '
             f'stroke="{BLEU if croise else AXE}" stroke-width="{2 if croise else 1.2}"'
             f'{" marker-end=" + chr(34) + "url(#pb)" + chr(34) if croise else " stroke-dasharray=" + chr(34) + "3 3" + chr(34)}/>')
    if dec:
        sortie(cd, yb[2] - 8, "le mot suivant")
    elif enc:
        sortie(ce, yb[1] - 8, "un vecteur par mot")
    yt = 296
    o.append(f'<text x="{px + lp / 2}" y="{yt}" font-size="13" fill="{BRUN}" text-anchor="middle" font-weight="700">{titre}</text>')
    o.append(f'<text x="{px + lp / 2}" y="{yt + 18}" font-size="11" fill="{ENCRE}" text-anchor="middle">{exemples}</text>')
    o.append(f'<text x="{px + lp / 2}" y="{yt + 34}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle" font-style="italic">{usage}</text>')


panneau(x0, "Encodeur et décodeur", "Transformer de 2017, T5", "traduire, résumer", True, True)
panneau(x0 + lp + e, "Encodeur seul", "BERT", "comprendre, classer", True, False)
panneau(x0 + 2 * (lp + e), "Décodeur seul", "GPT, grands modèles de langue", "générer du texte", False, True)
o.append("</svg>")
(OUT / "transformer-variantes.svg").write_text("\n".join(o) + "\n")
print("transformer-variantes.svg écrit")
