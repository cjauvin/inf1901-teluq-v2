"""Module 5, « Une machine peut-elle penser ? » : la chambre chinoise de Searle (1980), et le même schéma appliqué à un
modèle de langage. Les caractères chinois sont dessinés comme des formes abstraites (les « squiggles » et « squoggles » de
Searle), pour ne dépendre d'aucune police."""
import random
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module5" / "chambre-chinoise.svg"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
rng = random.Random(7)


def glyphe(x, y, t=16, coul=ENCRE):
    """Un pseudo-caractère : trois ou quatre traits dans un carré de côté t."""
    traits = []
    for _ in range(rng.randint(3, 4)):
        genre = rng.random()
        if genre < 0.4:
            yy = y + rng.uniform(0.15, 0.85) * t
            traits.append(f"M{x + rng.uniform(0, .3) * t:.1f} {yy:.1f} H{x + rng.uniform(.7, 1) * t:.1f}")
        elif genre < 0.75:
            xx = x + rng.uniform(0.2, 0.8) * t
            traits.append(f"M{xx:.1f} {y + rng.uniform(0, .3) * t:.1f} V{y + rng.uniform(.7, 1) * t:.1f}")
        else:
            traits.append(f"M{x + .1 * t:.1f} {y + .9 * t:.1f} Q{x + .5 * t:.1f} {y + rng.uniform(.2, .5) * t:.1f} {x + .9 * t:.1f} {y + .8 * t:.1f}")
    return f'<path d="{" ".join(traits)}" fill="none" stroke="{coul}" stroke-width="1.6" stroke-linecap="round"/>'


def carte(x, y, n, coul):
    o.append(f'<rect x="{x}" y="{y}" width="{n * 21 + 10}" height="30" rx="4" fill="#ffffff" stroke="{coul}" stroke-width="1.4"/>')
    for k in range(n):
        o.append(glyphe(x + 7 + k * 21, y + 7))


def fleche(x1, y1, x2, y2, coul=GRIS):
    o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{coul}" stroke-width="1.8" marker-end="url(#p)"/>')


W, H = 840, 430
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>La chambre chinoise, et un modèle de langage</title>",
     "<desc>Deux panneaux. À gauche, la chambre chinoise imaginée par John Searle en 1980 : une personne enfermée dans une pièce, "
     "qui ne connaît pas le chinois, reçoit par une fente des questions écrites en caractères chinois. Elle consulte un gros livre "
     "de règles, écrit dans sa langue, qui lui dit quels caractères renvoyer selon ceux qu'elle reçoit, et glisse sa réponse par une "
     "autre fente. De l'extérieur, les réponses sont parfaites ; à l'intérieur, personne ne comprend le chinois. À droite, le même "
     "schéma pour un modèle de langage : des jetons entrent, d'autres sortent, et entre les deux il n'y a que des milliards de "
     "nombres, les poids du modèle. Personne n'a écrit ces règles : elles ont été apprises.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">La chambre chinoise, et un modèle de langage</text>']
# ── panneau gauche : la chambre ──
o.append(f'<rect x="20" y="50" width="470" height="{H - 70}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
o.append(f'<text x="255" y="76" font-size="12.5" fill="{BRUN}" text-anchor="middle" font-weight="700">La chambre chinoise (Searle, 1980)</text>')
RX, RY, RW, RH = 150, 100, 210, 210
o.append(f'<rect x="{RX}" y="{RY}" width="{RW}" height="{RH}" rx="6" fill="{FOND}" stroke="{BRUN}" stroke-width="3"/>')
# les deux fentes
o.append(f'<rect x="{RX - 2}" y="146" width="5" height="22" fill="{PANNEAU}"/>')
o.append(f'<rect x="{RX + RW - 3}" y="236" width="5" height="22" fill="{PANNEAU}"/>')
# la personne et son livre
o.append(f'<circle cx="215" cy="196" r="13" fill="{PANNEAU}" stroke="{ENCRE}" stroke-width="2"/>')
o.append(f'<path d="M193 246 Q193 214 215 214 Q237 214 237 246" fill="{PANNEAU}" stroke="{ENCRE}" stroke-width="2"/>')
o.append(f'<rect x="250" y="214" width="80" height="44" rx="3" fill="{BRUN}" fill-opacity="0.2" stroke="{BRUN}" stroke-width="1.8"/>')
o.append(f'<line x1="290" y1="214" x2="290" y2="258" stroke="{BRUN}" stroke-width="1.4"/>')
for k in range(3):
    o.append(f'<line x1="256" y1="{224 + k * 10}" x2="284" y2="{224 + k * 10}" stroke="{BRUN}" stroke-width="1"/>')
    o.append(f'<line x1="296" y1="{224 + k * 10}" x2="324" y2="{224 + k * 10}" stroke="{BRUN}" stroke-width="1"/>')
o.append(f'<text x="290" y="276" font-size="10.5" fill="{BRUN}" text-anchor="middle" font-weight="700">le livre de règles</text>')
o.append(f'<text x="290" y="290" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">écrit dans sa langue</text>')
o.append(f'<text x="215" y="126" font-size="10.5" fill="{ENCRE}" text-anchor="middle">ne connaît pas</text>')
o.append(f'<text x="215" y="140" font-size="10.5" fill="{ENCRE}" text-anchor="middle">le chinois</text>')
# entrée et sortie
carte(36, 142, 4, BLEU)
fleche(132, 157, 160, 157)
o.append(f'<text x="80" y="192" font-size="10.5" fill="{BLEU}" text-anchor="middle" font-weight="700">une question</text>')
o.append(f'<text x="80" y="206" font-size="10.5" fill="{BLEU}" text-anchor="middle">en chinois</text>')
fleche(RX + RW - 6, 247, RX + RW + 26, 247)
carte(RX + RW + 30, 232, 3, TEAL)
o.append(f'<text x="428" y="282" font-size="10.5" fill="{TEAL}" text-anchor="middle" font-weight="700">une réponse</text>')
o.append(f'<text x="428" y="296" font-size="10.5" fill="{TEAL}" text-anchor="middle">parfaite</text>')
o.append(f'<text x="255" y="{H - 52}" font-size="11.5" fill="{ENCRE}" text-anchor="middle">De l\'extérieur, la chambre semble comprendre le chinois.</text>')
o.append(f'<text x="255" y="{H - 34}" font-size="11.5" fill="{ENCRE}" text-anchor="middle">À l\'intérieur, personne ne le comprend.</text>')
# ── panneau droit : le modèle ──
o.append(f'<rect x="506" y="50" width="314" height="{H - 70}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
o.append(f'<text x="663" y="76" font-size="12.5" fill="{TEAL}" text-anchor="middle" font-weight="700">Un modèle de langage</text>')
o.append(f'<rect x="590" y="110" width="146" height="180" rx="8" fill="{FOND}" stroke="{TEAL}" stroke-width="2.4"/>')
for r in range(7):
    ligne = " ".join(f"{rng.uniform(-1, 1):+.2f}".replace(".", ",") for _ in range(3))
    o.append(f'<text x="663" y="{140 + r * 20}" font-size="10" fill="{GRIS}" text-anchor="middle" font-family="ui-monospace, Menlo, monospace">{ligne}</text>')
o.append(f'<text x="663" y="306" font-size="10.5" fill="{TEAL}" text-anchor="middle" font-weight="700">des milliards de poids</text>')
o.append(f'<text x="663" y="320" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">appris, non écrits</text>')
for k, y in enumerate((150, 175, 200)):
    o.append(f'<rect x="522" y="{y - 10}" width="44" height="18" rx="3" fill="#ffffff" stroke="{BLEU}" stroke-width="1.2"/>')
    o.append(f'<text x="544" y="{y + 3}" font-size="9.5" fill="{BLEU}" text-anchor="middle" font-family="ui-monospace, Menlo, monospace">{["17 233", "4 501", "902"][k]}</text>')
fleche(568, 175, 588, 175)
fleche(738, 200, 758, 200)
o.append(f'<rect x="762" y="191" width="44" height="18" rx="3" fill="#ffffff" stroke="{TEAL}" stroke-width="1.2"/>')
o.append(f'<text x="784" y="204" font-size="9.5" fill="{TEAL}" text-anchor="middle" font-family="ui-monospace, Menlo, monospace">88 016</text>')
o.append(f'<text x="544" y="224" font-size="10" fill="{BLEU}" text-anchor="middle">jetons</text>')
o.append(f'<text x="784" y="226" font-size="10" fill="{TEAL}" text-anchor="middle">jeton</text>')
o.append(f'<text x="663" y="{H - 52}" font-size="11.5" fill="{ENCRE}" text-anchor="middle">Le même schéma{NB}: des symboles entrent,</text>')
o.append(f'<text x="663" y="{H - 34}" font-size="11.5" fill="{ENCRE}" text-anchor="middle">d\'autres sortent, selon des règles.</text>')
o.append("</svg>")
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(o) + "\n")
print(OUT.name, "écrit")
