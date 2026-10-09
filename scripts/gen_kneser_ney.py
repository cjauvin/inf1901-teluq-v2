"""Module 4, « Des règles aux probabilités » : l'idée du lissage de Kneser-Ney. Un mot fréquent qui ne suit qu'un seul mot
(« Francisco », après « San ») doit peser moins, dans un contexte inconnu, qu'un mot moins fréquent qui suit toutes sortes
de mots (« lunettes »). Nombres illustratifs."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "
W, H = 800, 500
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Le lissage de Kneser-Ney</title>",
     "<desc>En haut, deux panneaux. À gauche, le mot « Francisco », vu 1 000 fois dans le corpus, mais toujours après le même mot, "
     "« San » : une seule flèche épaisse y mène. À droite, le mot « lunettes », vu 300 fois seulement, mais après 120 mots "
     "différents, comme mes, des, ses, les, nouvelles ou vos : une gerbe de flèches fines y mène. En bas, un contexte jamais vu, "
     "« Je ne vois rien sans mes », et deux façons d'estimer le mot suivant. Selon la fréquence, « Francisco » l'emporte sur "
     "« lunettes », ce qui est absurde. Selon la variété des contextes, l'idée de Kneser-Ney, « lunettes » l'emporte nettement.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Kneser-Ney{NB}: compter les contextes, pas seulement les occurrences</text>']


def panneau(x0, mot, vu, apres, precedents, epais):
    w = 360
    o.append(f'<rect x="{x0}" y="54" width="{w}" height="196" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
    xm, ym = x0 + 262, 142
    n = len(precedents)
    for k, pr in enumerate(precedents):
        y = ym if n == 1 else 76 + k * (132 / (n - 1))
        o.append(f'<text x="{x0 + 70}" y="{y + 4:.1f}" font-size="12" fill="{ENCRE_PALE if pr == "…" else ENCRE}" text-anchor="end" font-style="italic">{pr}</text>')
        if pr != "…":
            o.append(f'<line x1="{x0 + 78}" y1="{y:.1f}" x2="{xm - 52}" y2="{ym:.1f}" stroke="{GRIS}" stroke-width="{epais}" stroke-opacity="0.8" marker-end="url(#p)"/>')
    o.append(f'<rect x="{xm - 50}" y="{ym - 17}" width="100" height="34" rx="17" fill="{FOND}" stroke="{TEAL}" stroke-width="1.8"/>')
    o.append(f'<text x="{xm}" y="{ym + 5}" font-size="14" fill="{ENCRE}" text-anchor="middle" font-weight="700" font-style="italic">{mot}</text>')
    o.append(f'<text x="{xm}" y="{ym + 38}" font-size="11" fill="{ENCRE}" text-anchor="middle">vu <tspan font-weight="700">{vu}</tspan> fois</text>')
    o.append(f'<text x="{xm}" y="{ym + 54}" font-size="11" fill="{ENCRE}" text-anchor="middle">après <tspan font-weight="700" fill="{TEAL}">{apres}</tspan></text>')


panneau(30, "Francisco", f"1{FINE}000", f"1{NB}seul mot", ["San"], 5)
panneau(410, "lunettes", "300", f"120{NB}mots différents", ["mes", "des", "ses", "les", "nouvelles", "vos", "…"], 1.2)
# en bas : un contexte jamais vu
y0 = 272
o.append(f'<rect x="30" y="{y0}" width="{W - 60}" height="{H - y0 - 22}" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
o.append(f'<text x="{W / 2}" y="{y0 + 28}" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle">un contexte jamais vu{NB}:'
         f'<tspan dx="8" font-size="14" fill="{ENCRE}" font-style="italic" font-weight="600">Je ne vois rien sans mes…</tspan></text>')


def groupe(x0, titre, sous, valeurs, bon):
    o.append(f'<text x="{x0}" y="{y0 + 66}" font-size="12.5" fill="{BRUN}" font-weight="700">{titre}</text>')
    o.append(f'<text x="{x0}" y="{y0 + 82}" font-size="10.5" fill="{ENCRE_PALE}">{sous}</text>')
    for k, (mot, v) in enumerate(valeurs):
        y = y0 + 100 + k * 34
        ok = mot == bon
        coul = TEAL if mot == "lunettes" else ROUGE
        o.append(f'<text x="{x0}" y="{y + 15}" font-size="12.5" fill="{ENCRE}" font-style="italic">{mot}</text>')
        o.append(f'<rect x="{x0 + 82}" y="{y + 3}" width="{max(2, 200 * v):.1f}" height="16" rx="3" fill="{coul}" fill-opacity="{1 if ok else 0.55}"/>')
    o.append(f'<text x="{x0 + 82}" y="{y0 + 180}" font-size="11.5" fill="{TEAL if bon == "lunettes" else ROUGE}" font-weight="700">'
             f'{"«" + NB + "lunettes" + NB + "»" + NB + "l'emporte" if bon == "lunettes" else "«" + NB + "Francisco" + NB + "»" + NB + "l'emporte, absurde"}</text>')


groupe(60, "Selon la fréquence", "combien de fois le mot a été vu", [("Francisco", 1.0), ("lunettes", 0.3)], "Francisco")
groupe(430, "Selon la variété des contextes", "après combien de mots différents (Kneser-Ney)", [("Francisco", 1 / 120), ("lunettes", 1.0)], "lunettes")
o.append("</svg>")
(OUT / "kneser-ney.svg").write_text("\n".join(o) + "\n")
print("kneser-ney.svg écrit")
