"""Module 4, « Des modèles qui voient, entendent et parlent » : deux façons de lire le texte d'une image. En haut, l'OCR
classique, une chaîne de pièces (repérer les lignes, isoler les caractères, reconnaître chacun, corriger avec un modèle de
langage), dont l'erreur typique est une lettre fausse. En bas, un modèle multimodal, qui lit d'un coup et comprend, mais
dont l'erreur typique est un texte plausible inventé."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
MONO = "Courier New, Courier, monospace"
W, H = 840, 500
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Deux façons de lire une image</title>",
     "<desc>Deux rangées. En haut, l'OCR classique, une chaîne de quatre pièces : repérer les lignes de texte sur la page ; isoler "
     "les caractères du mot verre, chacun dans une petite boîte ; reconnaître chaque caractère, ce qui donne v, c, r, r, e, avec "
     "une erreur, un c à la place du e ; puis corriger avec un modèle de langage, qui remplace vcrre par verre, beaucoup plus "
     "probable. Erreur typique : une lettre fausse. En bas, un modèle multimodal : l'image de la page devient des jetons visuels, "
     "que le modèle de langage lit d'un coup ; il écrit le texte, « Un verre d'eau, s'il vous plaît », et comprend en même temps "
     "la mise en page et le sens. Erreur typique : un mot ou une ligne plausible, inventé, qui ne figure pas dans l'image.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Deux façons de lire le texte d\'une image</text>']


def rangee(y, h, titre, coul):
    o.append(f'<rect x="20" y="{y}" width="{W - 40}" height="{h}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
    o.append(f'<text x="36" y="{y + 22}" font-size="13" fill="{coul}" font-weight="700">{titre}</text>')


def etape(x, y, w, h, num, titre):
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{FOND}" stroke="{AXE}" stroke-width="1.2"/>')
    o.append(f'<text x="{x + w / 2}" y="{y + 17}" font-size="11" fill="{ENCRE}" text-anchor="middle" font-weight="700">{num}. {titre}</text>')


def fleche(x1, x2, y):
    o.append(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')


# ── en haut : l'OCR classique ──
Y1 = 50
rangee(Y1, 200, "L'OCR classique : une chaîne de pièces", BRUN)
EW, EH, EY = 176, 132, Y1 + 34
xs = [36 + k * (EW + 22) for k in range(4)]
# 1. repérer les lignes
etape(xs[0], EY, EW, EH, 1, "repérer les lignes")
o.append(f'<rect x="{xs[0] + 30}" y="{EY + 28}" width="116" height="92" fill="#fffdf6" stroke="{BORD}"/>')
for k, w in enumerate([92, 100, 70, 96, 84]):
    yy = EY + 40 + k * 16
    o.append(f'<rect x="{xs[0] + 38}" y="{yy}" width="{w}" height="6" rx="1" fill="#9c958a"/>')
    o.append(f'<rect x="{xs[0] + 35}" y="{yy - 4}" width="{w + 6}" height="14" fill="none" stroke="{BLEU}" stroke-width="1.2"/>')
# 2. isoler les caractères
etape(xs[1], EY, EW, EH, 2, "isoler les caractères")
cx0, cy = xs[1] + 30, EY + 74
for k, c in enumerate("verre"):
    x = cx0 + k * 24
    o.append(f'<rect x="{x}" y="{cy - 22}" width="20" height="30" fill="none" stroke="{BLEU}" stroke-width="1.3"/>')
    o.append(f'<text x="{x + 10}" y="{cy}" font-size="24" fill="#4a453f" text-anchor="middle" font-family="{MONO}">{c}</text>')
o.append(f'<circle cx="{cx0 + 10 + 24}" cy="{cy - 10}" r="3" fill="#8a847a" opacity="0.8"/>')   # une tache sur le premier e
o.append(f'<text x="{xs[1] + EW / 2}" y="{EY + 116}" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">une tache sur le premier «{NB}e{NB}»</text>')
# 3. reconnaître chacun
etape(xs[2], EY, EW, EH, 3, "reconnaître chacun")
for k, c in enumerate("vcrre"):
    x = xs[2] + 30 + k * 24
    err = c == "c"
    o.append(f'<rect x="{x}" y="{cy - 22}" width="20" height="30" rx="3" fill="{ROUGE if err else "#e6eef6"}" stroke="{ROUGE if err else BLEU}" stroke-width="1.2"/>')
    o.append(f'<text x="{x + 10}" y="{cy - 1}" font-size="18" fill="{PANNEAU if err else ENCRE}" text-anchor="middle" font-family="{MONO}" font-weight="700">{c}</text>')
o.append(f'<text x="{xs[2] + EW / 2}" y="{EY + 116}" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">un «{NB}c{NB}» lu à la place du «{NB}e{NB}»</text>')
# 4. corriger avec un modèle de langage
etape(xs[3], EY, EW, EH, 4, "corriger")
o.append(f'<text x="{xs[3] + EW / 2}" y="{EY + 34}" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">avec un modèle de langage</text>')
o.append(f'<text x="{xs[3] + 28}" y="{EY + 64}" font-size="15" fill="{ENCRE}" font-family="{MONO}">vcrre</text>')
o.append(f'<text x="{xs[3] + EW - 16}" y="{EY + 64}" font-size="10.5" fill="{ROUGE}" text-anchor="end">✗ improbable</text>')
o.append(f'<text x="{xs[3] + 28}" y="{EY + 92}" font-size="15" fill="{ENCRE}" font-family="{MONO}" font-weight="700">verre</text>')
o.append(f'<text x="{xs[3] + EW - 16}" y="{EY + 92}" font-size="10.5" fill="{TEAL}" text-anchor="end">✓ probable</text>')
o.append(f'<text x="{xs[3] + EW / 2}" y="{EY + 116}" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">le modèle de langage arbitre</text>')
for k in range(3):
    fleche(xs[k] + EW + 2, xs[k + 1] - 2, EY + EH / 2)
o.append(f'<text x="36" y="{Y1 + 190}" font-size="11.5" fill="{BRUN}"><tspan font-weight="700">erreur typique{NB}:</tspan> une lettre fausse, que l\'on repère facilement</text>')

# ── en bas : un modèle multimodal ──
Y2 = 268
rangee(Y2, 212, "Un modèle multimodal : tout d'un coup", TEAL)
BY = Y2 + 36
# la page
o.append(f'<rect x="40" y="{BY}" width="150" height="120" fill="#fffdf6" stroke="{BORD}"/>')
o.append(f'<text x="52" y="{BY + 26}" font-size="10.5" fill="#4a453f" font-family="{MONO}">Au serveur :</text>')
o.append(f'<text x="52" y="{BY + 48}" font-size="10.5" fill="#4a453f" font-family="{MONO}">Un verre d\'eau,</text>')
o.append(f'<text x="52" y="{BY + 64}" font-size="10.5" fill="#4a453f" font-family="{MONO}">s\'il vous plaît.</text>')
o.append(f'<rect x="52" y="{BY + 80}" width="110" height="5" fill="#bdb6aa"/><rect x="52" y="{BY + 92}" width="84" height="5" fill="#bdb6aa"/>')
o.append(f'<text x="115" y="{BY + 138}" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">la page, en image</text>')
fleche(194, 232, BY + 60)
# les jetons visuels
o.append(f'<text x="290" y="{BY + 8}" font-size="11" fill="{ENCRE}" text-anchor="middle" font-weight="700">jetons visuels</text>')
for i in range(4):
    for j in range(6):
        o.append(f'<rect x="{240 + j * 17}" y="{BY + 18 + i * 17}" width="14" height="14" rx="2" fill="{TEAL}" opacity="{0.35 + 0.1 * ((i * 6 + j) % 6)}"/>')
o.append(f'<text x="290" y="{BY + 104}" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">des morceaux d\'image,</text>')
o.append(f'<text x="290" y="{BY + 117}" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">comme des mots</text>')
fleche(346, 384, BY + 60)
# le modèle de langage
o.append(f'<rect x="388" y="{BY + 30}" width="136" height="60" rx="10" fill="{FOND}" stroke="{TEAL}" stroke-width="2"/>')
o.append(f'<text x="456" y="{BY + 56}" font-size="12" fill="{ENCRE}" text-anchor="middle" font-weight="700">modèle</text>')
o.append(f'<text x="456" y="{BY + 72}" font-size="12" fill="{ENCRE}" text-anchor="middle" font-weight="700">de langage</text>')
fleche(528, 566, BY + 60)
# la sortie
o.append(f'<rect x="570" y="{BY + 6}" width="240" height="108" rx="8" fill="{FOND}" stroke="{AXE}"/>')
o.append(f'<text x="582" y="{BY + 28}" font-size="11.5" fill="{ENCRE}" font-family="{MONO}">«{NB}Au serveur : Un verre</text>')
o.append(f'<text x="582" y="{BY + 44}" font-size="11.5" fill="{ENCRE}" font-family="{MONO}">d\'eau, s\'il vous plaît.{NB}»</text>')
o.append(f'<text x="582" y="{BY + 70}" font-size="11" fill="{ENCRE_PALE}">et, en même temps, il comprend</text>')
o.append(f'<text x="582" y="{BY + 85}" font-size="11" fill="{ENCRE_PALE}">la mise en page et le sens{NB}: c\'est</text>')
o.append(f'<text x="582" y="{BY + 100}" font-size="11" fill="{ENCRE_PALE}">une demande polie</text>')
o.append(f'<text x="36" y="{Y2 + 196}" font-size="11.5" fill="{TEAL}"><tspan font-weight="700">erreur typique{NB}:</tspan> un mot ou une ligne plausible, inventé, qui ne figure pas dans l\'image, plus difficile à repérer</text>')
o.append("</svg>")
(OUT / "deux-facons-de-lire.svg").write_text("\n".join(o) + "\n")
print("deux-facons-de-lire.svg écrit")
