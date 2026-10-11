"""Module 4, « Du modèle à l'assistant » : la même consigne donnée à GPT-3 et à InstructGPT, d'après l'exemple publié par
OpenAI en janvier 2022 (« Aligning language models to follow instructions »), traduit. Le modèle de base continue une liste
de consignes ; InstructGPT y répond."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
W, H = 840, 420
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Même consigne, deux modèles</title>",
     "<desc>En haut, une consigne : « Explique l'alunissage à un enfant de six ans, en quelques phrases. » Elle est donnée à "
     "deux modèles. À gauche, GPT-3, un modèle de base, la continue par d'autres consignes du même genre : explique la théorie "
     "de la gravité à un enfant de six ans, explique la théorie de la relativité, explique le big bang, explique l'évolution. Il "
     "continue une liste de consignes. À droite, InstructGPT y répond : des gens sont allés sur la Lune, ils ont pris des photos "
     "de ce qu'ils voyaient et les ont envoyées sur la Terre, pour que tout le monde puisse les voir.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Même consigne, deux modèles</text>']
# la consigne
o.append(f'<rect x="{W / 2 - 250}" y="52" width="500" height="44" rx="10" fill="{PANNEAU}" stroke="{ENCRE_PALE}" stroke-width="1.4"/>')
o.append(f'<text x="{W / 2}" y="79" font-size="13" fill="{ENCRE}" text-anchor="middle" font-style="italic">Explique l\'alunissage à un enfant de six ans, en quelques phrases.</text>')
X1, X2, PW, PY, PH = 24, W / 2 + 12, W / 2 - 36, 140, 230
for xc in (X1 + PW / 2, X2 + PW / 2):
    o.append(f'<path d="M{W / 2} 98 Q {W / 2} 118 {xc} 118 L {xc} {PY - 4}" fill="none" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')


def panneau(x, titre, sous, coul):
    o.append(f'<rect x="{x}" y="{PY}" width="{PW}" height="{PH}" rx="10" fill="{PANNEAU}" stroke="{coul}" stroke-width="1.8"/>')
    o.append(f'<text x="{x + 18}" y="{PY + 26}" font-size="13.5" fill="{coul}" font-weight="700">{titre}</text>')
    o.append(f'<text x="{x + 18}" y="{PY + 44}" font-size="11" fill="{ENCRE_PALE}">{sous}</text>')


def lignes(x, y, ls, coul=ENCRE, pas=19, taille=12.5):
    for k, l in enumerate(ls):
        o.append(f'<text x="{x}" y="{y + k * pas}" font-size="{taille}" fill="{coul}" font-style="italic">{l}</text>')


panneau(X1, "GPT-3", "un modèle de base", BRUN)
lignes(X1 + 18, PY + 78, ["Explique la théorie de la gravité à un enfant",
                         "de six ans.",
                         "Explique la théorie de la relativité à un enfant",
                         "de six ans, en quelques phrases.",
                         "Explique le big bang à un enfant de six ans.",
                         "Explique l'évolution à un enfant de six ans."], ENCRE_PALE)
o.append(f'<text x="{X1 + 18}" y="{PY + PH - 18}" font-size="12" fill="{BRUN}" font-weight="700">il continue une liste de consignes</text>')
panneau(X2, "InstructGPT", "le même modèle, entraîné à suivre des consignes", TEAL)
lignes(X2 + 18, PY + 78, ["Des gens sont allés sur la Lune. Ils ont pris",
                         "des photos de ce qu'ils voyaient et les ont",
                         "envoyées sur la Terre, pour que tout le monde",
                         "puisse les voir."])
o.append(f'<text x="{X2 + 18}" y="{PY + PH - 18}" font-size="12" fill="{TEAL}" font-weight="700">il répond à la consigne</text>')
o.append(f'<text x="{W / 2}" y="{H - 18}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">D\'après l\'exemple publié par OpenAI en 2022, traduit de l\'anglais</text>')
o.append("</svg>")
(OUT / "instructgpt.svg").write_text("\n".join(o) + "\n")
print("instructgpt.svg écrit")
