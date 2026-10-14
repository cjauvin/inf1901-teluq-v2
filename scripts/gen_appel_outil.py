"""Module 4, « Des outils et des agents » : un appel d'outil, pas à pas, en diagramme de séquence. Le modèle ne fait que
prédire des jetons ; le harnais lit l'appel, exécute l'outil, ajoute le résultat au texte et rappelle le modèle."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
W, H = 840, 640
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Un appel d'outil, pas à pas</title>",
     "<desc>Un diagramme en trois colonnes : le modèle, le harnais et l'outil, avec le temps qui s'écoule vers le bas. 1, "
     "le harnais envoie au modèle le texte assemblé : la requête système avec la description des outils, la question « Combien "
     "coûte Kamouraska ? », et l'ouverture de la réplique de l'assistant. 2, le modèle prédit des jetons qui forment un appel : "
     "chercher_catalogue, avec le titre Kamouraska, puis s'arrête à la marque de fin. 3, le harnais vérifie l'appel. 4, il "
     "interroge le catalogue. 5, l'outil répond : format poche, 14,95 $, trois en stock. 6, le harnais ajoute ce résultat au "
     "texte et rouvre une réplique de l'assistant. 7, il rappelle le modèle avec tout le texte. 8, le modèle écrit la réponse : "
     "« Oui, nous l'avons en format poche, à 14,95 $. » 9, le harnais l'affiche à l'utilisateur. À côté des étapes 1 et 7, le "
     "texte envoyé au modèle est dessiné comme une barre de segments, plus longue la seconde fois.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Un appel d\'outil, pas à pas</text>']
XM, XA, XO = 130, 430, 730
for x, nom, sous, c in ((XM, "le modèle", "ne fait que prédire des jetons", TEAL), (XA, "le harnais", "un programme classique", BLEU),
                        (XO, "l'outil", "ici, le catalogue", BRUN)):
    o.append(f'<rect x="{x - 90}" y="50" width="180" height="46" rx="8" fill="{PANNEAU}" stroke="{c}" stroke-width="2"/>')
    o.append(f'<text x="{x}" y="70" font-size="13" fill="{c}" text-anchor="middle" font-weight="700">{nom}</text>')
    o.append(f'<text x="{x}" y="87" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">{sous}</text>')
    o.append(f'<line x1="{x}" y1="98" x2="{x}" y2="{H - 24}" stroke="{AXE}" stroke-width="1.4" stroke-dasharray="5 4"/>')


def num(x, y, n):
    o.append(f'<circle cx="{x}" cy="{y}" r="9" fill="{ENCRE_PALE}"/>')
    o.append(f'<text x="{x}" y="{y + 4}" font-size="10.5" fill="{PANNEAU}" text-anchor="middle" font-weight="700">{n}</text>')


def message(y, x1, x2, n, l1, l2="", coul=ENCRE, mono=False):
    o.append(f'<line x1="{x1}" y1="{y}" x2="{x2 + (8 if x2 < x1 else -8)}" y2="{y}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')
    m = (x1 + x2) / 2
    num(22, y - 4, n)
    fam = ' font-family="ui-monospace, Menlo, monospace"' if mono else ""
    o.append(f'<text x="{m + 8}" y="{y - 8}" font-size="11.5" fill="{coul}" text-anchor="middle"{fam}>{l1}</text>')
    if l2:
        o.append(f'<text x="{m + 8}" y="{y + 16}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">{l2}</text>')


def note(x, y, n, l1, l2=""):
    w = 196
    o.append(f'<rect x="{x - w / 2}" y="{y - 16}" width="{w}" height="{36 if l2 else 26}" rx="6" fill="{PANNEAU}" stroke="{BLEU}" stroke-width="1.2"/>')
    num(22, y + 2, n)
    o.append(f'<text x="{x}" y="{y + 1}" font-size="11" fill="{ENCRE}" text-anchor="middle">{l1}</text>')
    if l2:
        o.append(f'<text x="{x}" y="{y + 15}" font-size="11" fill="{ENCRE}" text-anchor="middle">{l2}</text>')


def texte(x, y, segments):
    """Le texte envoyé au modèle, comme une barre de segments colorés."""
    for lab, c, w in segments:
        o.append(f'<rect x="{x}" y="{y}" width="{w}" height="16" rx="3" fill="{c}"/>')
        o.append(f'<text x="{x + w / 2}" y="{y + 11.5}" font-size="9" fill="{PANNEAU}" text-anchor="middle" font-weight="700">{lab}</text>')
        x += w + 2


y = 142
message(y, XA, XM, 1, "le texte assemblé", "")
texte(XM + 40, y + 6, [("système + outils", BRUN, 92), ("question", BLEU, 52), ("assistant", TEAL, 50)])
y += 64
o.append(f'<rect x="{XM - 8}" y="{y - 40}" width="16" height="50" rx="3" fill="{TEAL}" opacity="0.85"/>')
message(y, XM, XA, 2, 'appel{0}: chercher_catalogue("Kamouraska")'.format(NB), "puis la marque de fin : la génération s'arrête", ROUGE, mono=True)
y += 58
note(XA, y, 3, "vérifie l'appel{0}: outil connu,".format(NB), "arguments valides, action permise")
y += 54
message(y, XA, XO, 4, "requête au catalogue")
y += 50
message(y, XO, XA, 5, "poche, 14,95 $, 3 en stock", "", BRUN)
y += 50
note(XA, y, 6, "ajoute le résultat au texte,", "rouvre une réplique de l'assistant")
y += 58
message(y, XA, XM, 7, "tout le texte, résultat compris")
texte(XM + 40, y + 6, [("système + outils", BRUN, 92), ("question", BLEU, 52), ("appel", ROUGE, 34), ("résultat", BRUN, 46), ("assistant", TEAL, 50)])
y += 64
o.append(f'<rect x="{XM - 8}" y="{y - 40}" width="16" height="50" rx="3" fill="{TEAL}" opacity="0.85"/>')
message(y, XM, XA, 8, f"«{NB}Oui, nous l'avons en format poche, à 14,95{NB}${NB}»", "", TEAL)
y += 48
o.append(f'<line x1="{XA}" y1="{y}" x2="{XA + 80}" y2="{y}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')
num(22, y, 9)
o.append(f'<text x="{XA + 88}" y="{y + 4}" font-size="11.5" fill="{ENCRE}">réponse affichée à l\'utilisateur</text>')
o.append(f'<text x="{XM}" y="{H - 8}" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">rectangles pleins{NB}: le modèle prédit des jetons</text>')
o.append("</svg>")
(OUT / "appel-outil.svg").write_text("\n".join(o) + "\n")
print("appel-outil.svg écrit")
