"""Module 4, « Du modèle à l'assistant » : les trois niveaux d'un acte de parole selon John Austin (locutoire, illocutoire,
perlocutoire), sur un seul énoncé, « Sais-tu quelle heure il est ? », et deux réponses : à la lettre, ou à l'acte."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
W, H = 840, 490
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Trois niveaux dans un même énoncé</title>",
     "<desc>À gauche, une bulle : « Sais-tu quelle heure il est ? ». Trois flèches en partent vers trois niveaux. L'acte "
     "locutoire, ce qui est dit : une question sur ce que sait l'autre. L'acte illocutoire, ce qu'on fait en le disant : une "
     "demande, « dis-moi l'heure ». L'acte perlocutoire, l'effet produit : l'autre regarde sa montre et donne l'heure. En bas, "
     "deux réponses possibles. « Oui. » répond à la lettre, au niveau locutoire : c'est exact, mais personne ne l'attend. "
     "« Il est 15 h 20. » répond à l'acte, au niveau illocutoire.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Trois niveaux dans un même énoncé</text>']
# la bulle
BX, BY, BW, BH = 30, 132, 210, 70
o.append(f'<path d="M{BX + 10} {BY} H{BX + BW - 10} Q{BX + BW} {BY} {BX + BW} {BY + 10} V{BY + BH - 10} Q{BX + BW} {BY + BH} {BX + BW - 10} {BY + BH} '
         f'H{BX + 60} L{BX + 34} {BY + BH + 20} L{BX + 40} {BY + BH} H{BX + 10} Q{BX} {BY + BH} {BX} {BY + BH - 10} V{BY + 10} Q{BX} {BY} {BX + 10} {BY} Z" '
         f'fill="{PANNEAU}" stroke="{ENCRE_PALE}" stroke-width="1.6"/>')
o.append(f'<text x="{BX + BW / 2}" y="{BY + 41}" font-size="14" fill="{ENCRE}" text-anchor="middle" font-style="italic" font-weight="600">Sais-tu quelle heure il est{NB}?</text>')
# les trois niveaux
NX, NW, NH = 300, 510, 66
niveaux = [("acte locutoire", "ce qui est dit", "une question sur ce que sait l'autre", BRUN),
           ("acte illocutoire", "ce qu'on fait en le disant", f"une demande{NB}: «{NB}dis-moi l'heure{NB}»", TEAL),
           ("acte perlocutoire", "l'effet produit", "l'autre regarde sa montre et donne l'heure", BLEU)]
for k, (nom, sens, contenu, c) in enumerate(niveaux):
    y = 58 + k * (NH + 14)
    o.append(f'<rect x="{NX}" y="{y}" width="{NW}" height="{NH}" rx="10" fill="{PANNEAU}" stroke="{c}" stroke-width="1.8"/>')
    o.append(f'<text x="{NX + 16}" y="{y + 27}" font-size="13" fill="{c}" font-weight="700">{nom}</text>')
    o.append(f'<text x="{NX + 16}" y="{y + 46}" font-size="11" fill="{ENCRE_PALE}">{sens}</text>')
    o.append(f'<text x="{NX + 190}" y="{y + 38}" font-size="12.5" fill="{ENCRE}">{contenu}</text>')
    o.append(f'<path d="M{BX + BW + 4} {BY + BH / 2} C {BX + BW + 30} {BY + BH / 2} {NX - 34} {y + NH / 2} {NX - 6} {y + NH / 2}" '
             f'fill="none" stroke="{GRIS}" stroke-width="1.5" marker-end="url(#p)"/>')
# les deux réponses
RY = 336
o.append(f'<text x="{W / 2}" y="{RY - 14}" font-size="12.5" fill="{ENCRE_PALE}" text-anchor="middle" font-weight="700">deux réponses possibles</text>')
for x, rep, l1, l2, c in ((30, "Oui.", "répond à la lettre (niveau locutoire)", "exact, mais personne ne l'attend", BRUN),
                          (W / 2 + 10, f"Il est 15{NB}h{NB}20.", "répond à l'acte (niveau illocutoire)", "ce qu'on attendait", TEAL)):
    w = W / 2 - 40
    o.append(f'<rect x="{x}" y="{RY}" width="{w}" height="120" rx="10" fill="{PANNEAU}" stroke="{c}" stroke-width="1.8"/>')
    o.append(f'<text x="{x + w / 2}" y="{RY + 46}" font-size="18" fill="{ENCRE}" text-anchor="middle" font-style="italic" font-weight="600">{rep}</text>')
    o.append(f'<text x="{x + w / 2}" y="{RY + 80}" font-size="12.5" fill="{c}" text-anchor="middle" font-weight="700">{l1}</text>')
    o.append(f'<text x="{x + w / 2}" y="{RY + 100}" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">{l2}</text>')
o.append("</svg>")
(OUT / "actes-de-parole.svg").write_text("\n".join(o) + "\n")
print("actes-de-parole.svg écrit")
