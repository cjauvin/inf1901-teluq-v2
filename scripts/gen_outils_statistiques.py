"""Module 4, « Les outils statistiques » : deux figures.

1. hmm.svg : un modèle de Markov caché ; des étiquettes cachées, reliées par des transitions, émettent les mots visibles.
2. canal-bruite.svg : la traduction statistique comme canal bruité, avec l'alignement des mots d'une phrase.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "


def entete(W, H, titre, desc, sous_titre):
    return ['<?xml version="1.0" encoding="UTF-8"?>',
            f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
            f"<title>{titre}</title>", f"<desc>{desc}</desc>",
            f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
            f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker>'
            f'<marker id="pt" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
            f'<path d="M0 0 L10 5 L0 10 z" fill="{TEAL}"/></marker>'
            f'<marker id="pb" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
            f'<path d="M0 0 L10 5 L0 10 z" fill="{BRUN}"/></marker></defs>',
            f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
            f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">{sous_titre}</text>']


# ── 1. le modèle de Markov caché ──
W, H = 760, 330
etats = ["déterminant", "nom", "verbe", "déterminant", "nom"]
mots = ["la", "petite", "brise", "la", "glace"]
trans = ["0,70", "0,30", "0,35", "0,70"]
emis = ["0,25", "0,005", "0,005", "0,25", "0,02"]
o = entete(W, H, "Un modèle de Markov caché",
           "Deux rangées. En haut, dans une bande marquée « caché », une suite d'étiquettes grammaticales : déterminant, nom, verbe, "
           "déterminant, nom, reliées par des flèches de transition, avec leur probabilité, par exemple 0,70 de passer d'un déterminant à "
           "un nom. En bas, dans une bande marquée « visible », les mots de la phrase « la petite brise la glace ». Chaque étiquette "
           "émet le mot placé sous elle, avec une probabilité d'émission, par exemple 0,005 pour qu'un nom soit le mot « petite ».",
           "Un modèle de Markov caché{NB}: des étiquettes cachées émettent des mots visibles".replace("{NB}", NB))
xs = [110 + k * 135 for k in range(5)]
o.append(f'<rect x="20" y="58" width="{W - 40}" height="96" rx="10" fill="{PANNEAU}" stroke="{TEAL}" stroke-dasharray="6 4"/>')
o.append(f'<text x="34" y="78" font-size="12" fill="{TEAL}" font-weight="700">caché</text>')
o.append(f'<rect x="20" y="226" width="{W - 40}" height="64" rx="10" fill="{PANNEAU}" stroke="{BRUN}" stroke-dasharray="6 4"/>')
o.append(f'<text x="34" y="246" font-size="12" fill="{BRUN}" font-weight="700">visible</text>')
for k, (x, et, m) in enumerate(zip(xs, etats, mots)):
    o.append(f'<rect x="{x - 52}" y="94" width="104" height="36" rx="18" fill="{FOND}" stroke="{TEAL}" stroke-width="1.8"/>')
    o.append(f'<text x="{x}" y="117" font-size="12.5" fill="{ENCRE}" text-anchor="middle" font-weight="600">{et}</text>')
    o.append(f'<line x1="{x}" y1="132" x2="{x}" y2="250" stroke="{BRUN}" stroke-width="1.6" marker-end="url(#pb)"/>')
    o.append(f'<text x="{x + 6}" y="194" font-size="11" fill="{BRUN}">{emis[k]}</text>')
    o.append(f'<text x="{x}" y="272" font-size="16" fill="{ENCRE}" text-anchor="middle" font-style="italic" font-weight="600">{m}</text>')
    if k < 4:
        o.append(f'<line x1="{x + 54}" y1="112" x2="{xs[k + 1] - 56}" y2="112" stroke="{TEAL}" stroke-width="1.8" marker-end="url(#pt)"/>')
        o.append(f'<text x="{(x + xs[k + 1]) / 2}" y="106" font-size="11" fill="{TEAL}" text-anchor="middle">{trans[k]}</text>')
xe = (xs[1] + xs[2]) / 2                                       # entre deux flèches, pour ne rien toucher
o.append(f'<text x="{xe}" y="166" font-size="11" fill="{BRUN}" text-anchor="middle">émissions{NB}:</text>')
o.append(f'<text x="{xe}" y="180" font-size="11" fill="{BRUN}" text-anchor="middle">P(mot{NB}|{NB}étiquette)</text>')
o.append(f'<text x="{W / 2}" y="84" font-size="11" fill="{TEAL}" text-anchor="middle">transitions{NB}: P(étiquette{NB}|{NB}étiquette précédente)</text>')
o.append(f'<text x="{W / 2}" y="{H - 16}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">On ne voit que les mots{NB}; l\'algorithme de Viterbi retrouve la suite d\'étiquettes la plus probable.</text>')
o.append("</svg>")
(OUT / "hmm.svg").write_text("\n".join(o) + "\n")

# ── 2. le canal bruité ──
W, H = 760, 400
o = entete(W, H, "La traduction comme canal bruité",
           "En haut, le canal bruité : une phrase anglaise, « the house is small », traverse un canal qui la brouille et en sort en "
           "français, « la maison est petite ». Seule la phrase française est observée. Au milieu, les mots des deux phrases sont "
           "reliés par l'alignement que le modèle apprend sur le Hansard : la et the, maison et house, est et is, petite et small. En "
           "bas, la traduction consiste à retrouver la phrase anglaise e qui rend le produit P(e) × P(f | e) le plus grand : P(e), un "
           "modèle de langage de l'anglais, juge si la phrase est de l'anglais naturel ; P(f | e), le modèle de traduction, juge si la "
           "phrase française en est une traduction plausible.",
           "La traduction statistique{NB}: retrouver la phrase d'origine «{NB}brouillée{NB}»".replace("{NB}", NB))
# le canal
o.append(f'<rect x="40" y="64" width="190" height="44" rx="8" fill="{PANNEAU}" stroke="{BLEU}" stroke-width="1.6"/>')
o.append(f'<text x="135" y="84" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">phrase anglaise (cachée)</text>')
o.append(f'<text x="135" y="100" font-size="13" fill="{BLEU}" text-anchor="middle" font-style="italic" font-weight="600">the house is small</text>')
o.append(f'<line x1="234" y1="86" x2="282" y2="86" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')
o.append(f'<rect x="286" y="64" width="188" height="44" rx="22" fill="{FOND}" stroke="{GRIS}" stroke-width="1.6" stroke-dasharray="5 3"/>')
o.append(f'<text x="380" y="91" font-size="12.5" fill="{ENCRE}" text-anchor="middle" font-weight="600">canal bruité</text>')
o.append(f'<line x1="478" y1="86" x2="526" y2="86" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')
o.append(f'<rect x="530" y="64" width="190" height="44" rx="8" fill="{PANNEAU}" stroke="{ROUGE}" stroke-width="1.6"/>')
o.append(f'<text x="625" y="84" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">phrase française (observée)</text>')
o.append(f'<text x="625" y="100" font-size="13" fill="{ROUGE}" text-anchor="middle" font-style="italic" font-weight="600">la maison est petite</text>')
# l'alignement
fr_mots, en_mots = ["la", "maison", "est", "petite"], ["the", "house", "is", "small"]
xs = [220 + k * 110 for k in range(4)]
o.append(f'<text x="40" y="166" font-size="11.5" fill="{BLEU}" font-weight="700">anglais</text>')
o.append(f'<text x="40" y="234" font-size="11.5" fill="{ROUGE}" font-weight="700">français</text>')
for x, a, b in zip(xs, en_mots, fr_mots):
    o.append(f'<text x="{x}" y="166" font-size="14" fill="{BLEU}" text-anchor="middle" font-style="italic">{a}</text>')
    o.append(f'<text x="{x}" y="234" font-size="14" fill="{ROUGE}" text-anchor="middle" font-style="italic">{b}</text>')
    o.append(f'<line x1="{x}" y1="174" x2="{x}" y2="218" stroke="{AXE}" stroke-width="1.6"/>')
o.append(f'<text x="680" y="204" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">l\'alignement,</text>')
o.append(f'<text x="680" y="218" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">appris sur le Hansard</text>')
# la formule
o.append(f'<text x="{W / 2}" y="282" font-size="13" fill="{ENCRE}" text-anchor="middle">traduire{NB}= trouver l\'anglais <tspan font-style="italic">e</tspan> qui rend le plus grand</text>')
o.append(f'<text x="{W / 2}" y="312" font-size="17" fill="{ENCRE}" text-anchor="middle" font-weight="700"><tspan fill="{BLEU}">P(<tspan font-style="italic">e</tspan>)</tspan>{NB}×{NB}<tspan fill="{TEAL}">P(<tspan font-style="italic">f</tspan>{NB}|{NB}<tspan font-style="italic">e</tspan>)</tspan></text>')
o.append(f'<text x="250" y="348" font-size="11.5" fill="{BLEU}" text-anchor="middle" font-weight="700">modèle de langage</text>')
o.append(f'<text x="250" y="364" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">est-ce de l\'anglais naturel{FINE}?</text>')
o.append(f'<text x="510" y="348" font-size="11.5" fill="{TEAL}" text-anchor="middle" font-weight="700">modèle de traduction</text>')
o.append(f'<text x="510" y="364" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">le français en est-il une traduction plausible{FINE}?</text>')
o.append(f'<line x1="355" y1="318" x2="270" y2="336" stroke="{BLEU}" stroke-width="1.2"/>')
o.append(f'<line x1="420" y1="318" x2="495" y2="336" stroke="{TEAL}" stroke-width="1.2"/>')
o.append("</svg>")
(OUT / "canal-bruite.svg").write_text("\n".join(o) + "\n")
print("hmm.svg et canal-bruite.svg écrits")
