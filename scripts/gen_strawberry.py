"""Module 4, « Ce que les LLM comprennent, et ce qu'ils ratent » : combien de r dans strawberry ? Le mot vu par un humain
(dix lettres), vu par GPT-4o dans la question (un seul jeton), puis épelé dans une chaîne de pensée (une lettre par jeton).
Les découpages sont ceux du jeton o200k_base de GPT-4o, obtenus avec la bibliothèque tiktoken :
    « Combien de r dans strawberry ? » → Comb|ien| de| r| dans| strawberry| ?   (strawberry = 101830)
    « s-t-r-a-w-b-e-r-r-y »            → s|-t|-r|-a|-w|-b|-e|-r|-r|-y"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
MONO = "ui-monospace, Menlo, Consolas, monospace"
W, H = 840, 470
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Combien de r dans strawberry ?</title>",
     "<desc>Trois rangées. En haut, ce que voit un humain : les dix lettres s, t, r, a, w, b, e, r, r, y, dont trois r, "
     "surlignés. Au milieu, ce que reçoit GPT-4o quand on lui pose la question « Combien de r dans strawberry ? » : sept jetons, "
     "Comb, ien, de, r, dans, strawberry et le point d'interrogation ; strawberry est un seul jeton, le numéro 101 830, où aucune "
     "lettre n'est visible. En bas, le mot épelé dans une chaîne de pensée, s-t-r-a-w-b-e-r-r-y : chaque lettre devient un jeton, "
     "et les trois jetons qui contiennent un r peuvent être comptés, un, deux, trois.</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Combien de <tspan font-style="italic">r</tspan> dans <tspan font-style="italic">strawberry</tspan>{NB}?</text>']


def rangee(y, h, titre, sous, coul):
    o.append(f'<rect x="20" y="{y}" width="{W - 40}" height="{h}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
    o.append(f'<text x="36" y="{y + 24}" font-size="13" fill="{coul}" font-weight="700">{titre}</text>')
    o.append(f'<text x="36" y="{y + 42}" font-size="11" fill="{ENCRE_PALE}">{sous}</text>')


def jeton(x, y, texte, coul, fond, w=None, taille=14):
    w = w or 14 + 9 * len(texte)
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="5" fill="{fond}" stroke="{coul}" stroke-width="1.4"/>')
    o.append(f'<text x="{x + w / 2}" y="{y + 20}" font-size="{taille}" fill="{ENCRE}" text-anchor="middle" font-family="{MONO}" xml:space="preserve">{texte}</text>')
    return x + w + 6


# 1. ce que voit un humain
rangee(50, 100, "Ce que vous voyez", "dix lettres, dont trois r", BLEU)
x = 260
for c in "strawberry":
    r = c == "r"
    o.append(f'<rect x="{x}" y="88" width="30" height="40" rx="5" fill="{"#f6dcd6" if r else FOND}" stroke="{ROUGE if r else AXE}" stroke-width="{1.8 if r else 1}"/>')
    o.append(f'<text x="{x + 15}" y="115" font-size="20" fill="{ROUGE if r else ENCRE}" text-anchor="middle" font-family="{MONO}" font-weight="{700 if r else 400}">{c}</text>')
    x += 34
# 2. ce que voit le modèle
rangee(162, 132, "Ce que reçoit GPT-4o", "la question, découpée en sept jetons", BRUN)
x = 200
for t in ["Comb", "ien", " de", " r", " dans"]:
    x = jeton(x, 216, t.replace(" ", "·"), AXE, FOND)
xs = x
x = jeton(x, 216, "·strawberry", BRUN, "#f3e3d3", taille=14)
jeton(x, 216, "·?", AXE, FOND)
o.append(f'<text x="{(xs + x - 6) / 2}" y="266" font-size="11.5" fill="{BRUN}" text-anchor="middle" font-weight="700">un seul jeton, le numéro 101{NB}830</text>')
o.append(f'<text x="{(xs + x - 6) / 2}" y="282" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">aucune lettre n\'y est visible</text>')
# 3. épelé dans une chaîne de pensée
rangee(306, 136, "Épelé dans une chaîne de pensée", "chaque lettre devient un jeton, qu'on peut compter", TEAL)
x = 250
n = 0
for t in ["s", "-t", "-r", "-a", "-w", "-b", "-e", "-r", "-r", "-y"]:
    r = "r" in t
    w = 36
    x0 = x
    x = jeton(x, 360, t, ROUGE if r else AXE, "#f6dcd6" if r else FOND, w=w)
    if r:
        n += 1
        o.append(f'<circle cx="{x0 + w / 2}" cy="408" r="9" fill="{ROUGE}"/>')
        o.append(f'<text x="{x0 + w / 2}" y="412" font-size="11" fill="{PANNEAU}" text-anchor="middle" font-weight="700">{n}</text>')
o.append(f'<text x="{x + 10}" y="380" font-size="12" fill="{TEAL}" font-weight="700">trois{NB}r</text>')
o.append(f'<text x="{W / 2}" y="{H - 8}" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">Découpages réels de GPT-4o, obtenus avec la bibliothèque tiktoken{NB}; le point · marque une espace.</text>')
o.append("</svg>")
(OUT / "strawberry.svg").write_text("\n".join(o) + "\n")
print("strawberry.svg écrit")
