"""Module 3, « L'attention et le Transformer » : la grille d'attention d'une traduction."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module3"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, GRILLE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#e8dfc9", "#fbf7ee")
NB, FINE = " ", " "
POLICE = 'font-family="system-ui, -apple-system, sans-serif"'


def entete(w, h, titre, desc):
    return ['<?xml version="1.0" encoding="UTF-8"?>',
            f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" {POLICE}>',
            f"<title>{titre}</title>", f"<desc>{desc}</desc>",
            f'<rect x="0" y="0" width="{w}" height="{h}" rx="14" fill="{FOND}" stroke="{BORD}"/>']


def ecrire(nom, o):
    o.append("</svg>")
    (OUT / nom).write_text("\n".join(o) + "\n")


def grille_traduction():
    W, H = 700, 410
    anglais = ["the", "European", "Economic", "Area"]
    francais = ["la", "zone", "économique", "européenne"]
    poids = [[0.85, 0.05, 0.04, 0.06],
             [0.05, 0.05, 0.10, 0.80],
             [0.02, 0.18, 0.75, 0.05],
             [0.02, 0.78, 0.15, 0.05]]
    o = entete(W, H, "La grille d'attention d'une traduction",
               f"Une grille de quatre colonnes et quatre lignes. Les colonnes portent les mots anglais «{FINE}the European Economic Area{FINE}», les lignes les mots "
               f"français «{FINE}la zone économique européenne{FINE}». Chaque case est d'autant plus foncée que le décodeur regarde ce mot anglais en écrivant ce mot "
               f"français. «{FINE}la{FINE}» regarde «{FINE}the{FINE}», «{FINE}zone{FINE}» regarde «{FINE}Area{FINE}», «{FINE}économique{FINE}» regarde "
               f"«{FINE}Economic{FINE}» et «{FINE}européenne{FINE}» regarde «{FINE}European{FINE}»{NB}: les deux dernières cases foncées se croisent.")
    o.append(f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Où regarde le décodeur, pour chaque mot qu\'il écrit{NB}?</text>')
    c, x0, y0 = 62, 300, 116
    for j, mot in enumerate(anglais):
        o.append(f'<text x="{x0 + j * c + c / 2}" y="{y0 - 12}" font-size="13" fill="{BLEU}" text-anchor="middle" font-weight="700">{mot}</text>')
    o.append(f'<text x="{x0 + 2 * c}" y="{y0 - 38}" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle">phrase d\'origine (anglais)</text>')
    for i, mot in enumerate(francais):
        o.append(f'<text x="{x0 - 14}" y="{y0 + i * c + c / 2 + 5}" font-size="13" fill="{ROUGE}" text-anchor="end" font-weight="700">{mot}</text>')
        for j in range(4):
            v = poids[i][j]
            o.append(f'<rect x="{x0 + j * c}" y="{y0 + i * c}" width="{c}" height="{c}" fill="{ENCRE}" fill-opacity="{0.05 + 0.85 * v:.2f}" stroke="{PANNEAU}" stroke-width="2"/>')
            o.append(f'<text x="{x0 + j * c + c / 2}" y="{y0 + i * c + c / 2 + 4}" font-size="11.5" fill="{PANNEAU if v > 0.4 else ENCRE_PALE}" text-anchor="middle">{f"{v:.2f}".replace(".", ",")}</text>')
    o.append(f'<text x="{x0 - 14}" y="{y0 - 12}" font-size="12" fill="{ENCRE_PALE}" text-anchor="end">traduction (français)</text>')
    o.append(f'<text x="{W / 2}" y="{H - 16}" font-size="12.5" fill="{GRIS}" text-anchor="middle">Chaque ligne donne les poids de l\'attention pour un mot écrit{NB}; ils totalisent 1.</text>')
    ecrire("attention-traduction.svg", o)


grille_traduction()
print("attention-traduction.svg écrit")
