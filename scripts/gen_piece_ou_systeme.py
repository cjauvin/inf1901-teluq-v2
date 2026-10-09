"""Module 4, « Des règles aux probabilités » : le modèle de langage, longtemps une pièce d'arbitrage dans un système plus
vaste (ici la reconnaissance de la parole), devenu le système lui-même avec les grands modèles de langage."""
import math
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "
W, H = 800, 470
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Le modèle de langage, de la pièce au système</title>",
     "<desc>Deux panneaux. À gauche, « Avant : une pièce du système » : dans un système de reconnaissance de la parole, un signal "
     "sonore passe par un composant qui analyse les sons et propose trois transcriptions, « un verre d'eau », « un vert d'eau » et "
     "« un ver d'eau ». Un petit modèle de langage, en arbitre, leur donne des probabilités, 0,92, 0,07 et 0,01, et retient « un "
     "verre d'eau ». À droite, « Depuis 2022 : le système » : un grand modèle de langage, au centre, reçoit trois demandes, une "
     "question sur la capitale de l'Australie, une phrase anglaise à traduire et une demande de programme, et produit lui-même "
     "les trois réponses.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Le modèle de langage{NB}: d\'une pièce du système au système lui-même</text>']


def fleche(x1, y1, x2, y2):
    o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')


def boite(x, y, w, h, lignes, coul, fond=PANNEAU, l=1.6, taille=12):
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fond}" stroke="{coul}" stroke-width="{l}"/>')
    y0 = y + h / 2 - (len(lignes) - 1) * 8 + 4
    for k, (txt, g) in enumerate(lignes):
        o.append(f'<text x="{x + w / 2}" y="{y0 + 16 * k}" font-size="{taille}" fill="{ENCRE}" text-anchor="middle"{" font-weight=" + chr(34) + "700" + chr(34) if g else ""}>{txt}</text>')


# ── panneau de gauche : la reconnaissance de la parole ──
PX, PW = 20, 370
o.append(f'<rect x="{PX}" y="52" width="{PW}" height="{H - 72}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
o.append(f'<text x="{PX + PW / 2}" y="78" font-size="13" fill="{BRUN}" text-anchor="middle" font-weight="700">Avant{NB}: une pièce du système</text>')
o.append(f'<text x="{PX + PW / 2}" y="96" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">un système de reconnaissance de la parole</text>')
# le signal sonore
pts = " ".join(f"{PX + 40 + i * 1.5:.1f},{128 + 14 * math.sin(i * 0.55) * math.exp(-((i - 60) / 38) ** 2):.1f}" for i in range(120))
o.append(f'<polyline points="{pts}" fill="none" stroke="{BLEU}" stroke-width="1.6"/>')
o.append(f'<text x="{PX + 232}" y="132" font-size="11" fill="{ENCRE_PALE}">les sons</text>')
fleche(PX + 130, 146, PX + 130, 160)
boite(PX + 50, 162, 160, 36, [("analyse des sons", True)], BLEU)
fleche(PX + 130, 200, PX + 130, 214)
cands = [("un verre d'eau", "0,92", True), ("un vert d'eau", "0,07", False), ("un ver d'eau", "0,01", False)]
for k, (c, p, ok) in enumerate(cands):
    y = 218 + k * 30
    o.append(f'<rect x="{PX + 40}" y="{y}" width="180" height="24" rx="5" fill="{FOND}" stroke="{ROUGE if ok else BORD}" stroke-width="{1.8 if ok else 1}"/>')
    o.append(f'<text x="{PX + 130}" y="{y + 16}" font-size="12" fill="{ENCRE}" text-anchor="middle" font-style="italic">{c}</text>')
    o.append(f'<text x="{PX + 236}" y="{y + 16}" font-size="12" fill="{ROUGE if ok else ENCRE_PALE}" font-weight="{700 if ok else 400}">{p}</text>')
o.append(f'<text x="{PX + 130}" y="{212}" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle"> </text>')
# le petit modèle de langage, en arbitre, sur le côté
boite(PX + 278, 238, 80, 46, [("modèle", True), ("de langage", True)], TEAL, taille=10.5)
o.append(f'<text x="{PX + 318}" y="300" font-size="10" fill="{TEAL}" text-anchor="middle">l\'arbitre</text>')
o.append(f'<line x1="{PX + 276}" y1="261" x2="{PX + 268}" y2="261" stroke="{TEAL}" stroke-width="1.6"/>')
o.append(f'<path d="M{PX + 268} 230 L{PX + 268} 292" fill="none" stroke="{TEAL}" stroke-width="1.6"/>')
fleche(PX + 130, 308, PX + 130, 326)
o.append(f'<rect x="{PX + 40}" y="330" width="180" height="30" rx="6" fill="{PANNEAU}" stroke="{ROUGE}" stroke-width="2"/>')
o.append(f'<text x="{PX + 130}" y="350" font-size="13" fill="{ENCRE}" text-anchor="middle" font-weight="700" font-style="italic">un verre d\'eau</text>')
o.append(f'<text x="{PX + PW / 2}" y="{H - 54}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">le modèle de langage choisit parmi</text>')
o.append(f'<text x="{PX + PW / 2}" y="{H - 38}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">des propositions faites par d\'autres</text>')

# ── panneau de droite : le grand modèle de langage ──
QX, QW = 410, 370
o.append(f'<rect x="{QX}" y="52" width="{QW}" height="{H - 72}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
o.append(f'<text x="{QX + QW / 2}" y="78" font-size="13" fill="{BRUN}" text-anchor="middle" font-weight="700">Depuis 2022{NB}: le système</text>')
o.append(f'<text x="{QX + QW / 2}" y="96" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">un assistant comme ChatGPT</text>')
demandes = ["«" + NB + "Capitale de l'Australie" + FINE + "?" + NB + "»", "«" + NB + "Traduis : the house is small" + NB + "»", "«" + NB + "Écris un programme qui…" + NB + "»"]
reponses = ["Canberra.", "La maison est petite.", "def trier(liste): …"]
xs = [QX + 66, QX + QW / 2, QX + QW - 66]
for k, (x, d) in enumerate(zip(xs, demandes)):
    y = 116 + k * 30
    o.append(f'<text x="{QX + QW / 2}" y="{y + 12}" font-size="11.5" fill="{BLEU}" text-anchor="middle" font-style="italic">{d}</text>')
fleche(QX + QW / 2, 200, QX + QW / 2, 222)
o.append(f'<rect x="{QX + 40}" y="226" width="{QW - 80}" height="84" rx="10" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="2.4"/>')
o.append(f'<text x="{QX + QW / 2}" y="256" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="700">grand modèle de langage</text>')
o.append(f'<text x="{QX + QW / 2}" y="284" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">prédit le mot suivant, encore et encore</text>')
fleche(QX + QW / 2, 314, QX + QW / 2, 334)
for k, r in enumerate(reponses):
    y = 340 + k * 22
    o.append(f'<text x="{QX + QW / 2}" y="{y + 12}" font-size="12" fill="{ENCRE}" text-anchor="middle">{r}</text>')
o.append(f'<text x="{QX + QW / 2}" y="{H - 38}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">le modèle de langage fait lui-même tout le travail</text>')
o.append("</svg>")
(OUT / "piece-ou-systeme.svg").write_text("\n".join(o) + "\n")
print("piece-ou-systeme.svg écrit")
