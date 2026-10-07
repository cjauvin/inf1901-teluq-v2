"""Module 4, « Des règles aux probabilités » : une frise du traitement de la langue, de Markov à ChatGPT, en trois ères."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
ERES = [("les règles", 1950, 1992, BRUN), ("les statistiques", 1975, 2014, TEAL), ("les réseaux de neurones", 2003, 2025, ROUGE)]
EVENEMENTS = [                                                # année, texte, ère (couleur)
    (1913, "Markov compte les lettres d'Eugène Onéguine", TEAL),
    (1948, "Shannon : un modèle de langage", TEAL),
    (1954, "expérience Georgetown-IBM", BRUN),
    (1957, "grammaires de Chomsky", BRUN),
    (1966, "rapport ALPAC ; ELIZA", BRUN),
    (1970, "SHRDLU", BRUN),
    (1972, "TF-IDF", TEAL),
    (1977, "TAUM-MÉTÉO", BRUN),
    (1980, "HMM en reconnaissance vocale", TEAL),
    (1990, "traduction statistique d'IBM ; LSA", TEAL),
    (1993, "Penn Treebank", TEAL),
    (1995, "lissage de Kneser-Ney", TEAL),
    (2001, "CRF", TEAL),
    (2003, "modèle de langage neuronal", ROUGE),
    (2006, "Google Traduction (statistique)", TEAL),
    (2013, "word2vec", ROUGE),
    (2014, "séquence à séquence", ROUGE),
    (2016, "Google Traduction (neuronal)", ROUGE),
    (2017, "Transformer", ROUGE),
    (2018, "BERT, GPT", ROUGE),
    (2020, "GPT-3", ROUGE),
    (2022, "ChatGPT", ROUGE),
]
RH, Y0 = 19, 72                                              # hauteur d'une ligne, première ligne
W, H = 660, Y0 + len(EVENEMENTS) * RH + 40
XB = [58, 78, 98]                                             # les trois bandes verticales
XT = 130
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Une histoire du traitement de la langue</title>",
     "<desc>Une frise chronologique verticale, de 1913 à 2022, avec trois ères qui se chevauchent, marquées par des bandes de "
     "couleur : les règles, d'environ 1950 à 1990 ; les statistiques, d'environ 1975 à 2014 ; les réseaux de neurones, depuis "
     "2003. Les jalons : " + " ; ".join(f"{a}, {t}" for a, t, _ in EVENEMENTS) + ".</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Le traitement de la langue{NB}: trois ères qui se chevauchent</text>']
# légende des ères, en colonne à droite
for k, (nom, a, b, coul) in enumerate(ERES):
    y = Y0 + 70 + k * 24
    o.append(f'<rect x="470" y="{y - 11}" width="12" height="12" rx="3" fill="{coul}"/>')
    o.append(f'<text x="490" y="{y}" font-size="12" fill="{coul}" font-weight="700">{nom}</text>')
ligne = lambda k: Y0 + k * RH
# les bandes : de la première à la dernière ligne comprise dans l'ère
for (nom, a, b, coul), xb in zip(ERES, XB):
    ks = [k for k, (an, _, _) in enumerate(EVENEMENTS) if a <= an <= b]
    o.append(f'<rect x="{xb - 5}" y="{ligne(ks[0]) - 13}" width="10" height="{ligne(ks[-1]) - ligne(ks[0]) + 17}" rx="5" fill="{coul}" fill-opacity="0.8"/>')
for k, (a, t, coul) in enumerate(EVENEMENTS):
    y = ligne(k)
    xb = XB[[BRUN, TEAL, ROUGE].index(coul)]
    o.append(f'<line x1="{xb + 7}" y1="{y - 4}" x2="{XT - 8}" y2="{y - 4}" stroke="{coul}" stroke-width="1" stroke-opacity="0.5" stroke-dasharray="2 2"/>')
    o.append(f'<circle cx="{xb}" cy="{y - 4}" r="3" fill="{FOND}"/>')
    o.append(f'<text x="{XT}" y="{y}" font-size="12" fill="{ENCRE}"><tspan font-weight="700" fill="{coul}">{a}</tspan>{NB}{NB} {t}</text>')
o.append(f'<text x="{W / 2}" y="{H - 16}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">Une ère n\'efface pas la précédente{NB}: le modèle de langage de Shannon traverse toute l\'histoire.</text>')
o.append("</svg>")
(OUT / "frise-langage.svg").write_text("\n".join(o) + "\n")
print("frise-langage.svg écrit")
