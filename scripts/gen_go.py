"""Module 3, « Apprendre à jouer » : les positions du coup 37 (partie 2) et du coup 78 (partie 4) d'AlphaGo contre Lee Sedol.

Positions relevées sur les diagrammes de Wikimedia Commons (« Lee Sedol (W) vs AlphaGo (B) - Game 2 », et
« Lee-sedol-alphago-divine-move.jpg », par Axd), eux-mêmes tirés des fichiers SGF des parties.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module3"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, GRILLE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#e8dfc9", "#fbf7ee")
NB, FINE = " ", " "
POLICE = 'font-family="system-ui, -apple-system, sans-serif"'
COLS = "ABCDEFGHJKLMNOPQRST"
BOIS = "#e6c98f"

# Partie 2 : AlphaGo a les noirs. Les 37 premiers coups, dans l'ordre.
PARTIE2 = ("Q16 D4 C16 R4 P4 P3 O3 Q3 C6 F3 N4 R6 J17 D10 Q5 R5 C4 C3 B3 C5 B4 B5 D5 B6 D3 E4 D2 C7 K4 C13 E16 "
           "R14 R15 Q14 O16 Q11 P10").split()
# Partie 4 : Lee Sedol a les blancs. La position après son coup 78, en L11.
NOIRS78 = ("C16 C9 C6 D17 D9 E16 E10 E4 F17 F12 F11 F9 G14 G13 H17 H16 H15 H10 J3 K11 L9 M14 M12 M11 N16 N15 N13 N12 N4 "
           "O18 O17 O16 O11 O10 O3 P10 P4 Q16 Q10").split()
BLANCS78 = ("B10 B4 C13 C10 D10 D4 E17 E12 E11 E5 F16 F14 F13 F4 F3 G15 G12 J16 J9 K13 L11 M17 N17 N14 N11 N10 N9 O15 O14 "
            "O13 O12 P11 P3 Q11 Q5 Q3 R11 R10 R4").split()


def goban(nom, titre, desc, noirs, blancs, dernier, etiquette, legende):
    W, H, c, x0, y0 = 560, 636, 26, 46, 84
    X = lambda col: x0 + COLS.index(col) * c
    Y = lambda lig: y0 + (19 - lig) * c
    o = ['<?xml version="1.0" encoding="UTF-8"?>',
         f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" {POLICE}>',
         f"<title>{titre}</title>", f"<desc>{desc}</desc>",
         f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
         f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">{titre}</text>',
         f'<rect x="{x0 - 18}" y="{y0 - 18}" width="{18 * c + 36}" height="{18 * c + 36}" rx="6" fill="{BOIS}" stroke="{BRUN}" stroke-width="1.2"/>']
    for k in range(19):
        o.append(f'<line x1="{x0}" y1="{y0 + k * c}" x2="{x0 + 18 * c}" y2="{y0 + k * c}" stroke="{ENCRE_PALE}" stroke-width="0.8"/>')
        o.append(f'<line x1="{x0 + k * c}" y1="{y0}" x2="{x0 + k * c}" y2="{y0 + 18 * c}" stroke="{ENCRE_PALE}" stroke-width="0.8"/>')
        o.append(f'<text x="{x0 + k * c}" y="{y0 + 18 * c + 32}" font-size="10.5" fill="{GRIS}" text-anchor="middle">{COLS[k]}</text>')
        o.append(f'<text x="{x0 - 26}" y="{y0 + k * c + 4}" font-size="10.5" fill="{GRIS}" text-anchor="middle">{19 - k}</text>')
    for i in (3, 9, 15):
        for j in (3, 9, 15):
            o.append(f'<circle cx="{x0 + i * c}" cy="{y0 + j * c}" r="2.6" fill="{ENCRE_PALE}"/>')
    for coul, liste in (("noir", noirs), ("blanc", blancs)):
        for p in liste:
            x, y = X(p[0]), Y(int(p[1:]))
            if coul == "noir":
                o.append(f'<circle cx="{x}" cy="{y}" r="{c / 2 - 1}" fill="{ENCRE}"/>')
            else:
                o.append(f'<circle cx="{x}" cy="{y}" r="{c / 2 - 1.4}" fill="#fdfbf6" stroke="{ENCRE_PALE}" stroke-width="1"/>')
    x, y = X(dernier[0]), Y(int(dernier[1:]))
    blanc = dernier in blancs
    o.append(f'<circle cx="{x}" cy="{y}" r="{c / 2 + 3}" fill="none" stroke="{ROUGE}" stroke-width="3"/>')
    o.append(f'<text x="{x}" y="{y + 4}" font-size="10.5" fill="{ENCRE if blanc else "#fdfbf6"}" text-anchor="middle" font-weight="700">{etiquette}</text>')
    o.append(f'<text x="{W / 2}" y="{H - 18}" font-size="12.5" fill="{GRIS}" text-anchor="middle">{legende}</text>')
    o.append("</svg>")
    (OUT / nom).write_text("\n".join(o) + "\n")


noirs37, blancs37 = PARTIE2[0::2], PARTIE2[1::2]
goban("go-coup-37.svg", "Partie 2, coup 37 d'AlphaGo",
      f"Un goban de 19 lignes sur 19, avec la position de la deuxième partie après 37 coups. AlphaGo a les noirs. Le coup 37, une pierre noire en P10, "
      f"est entouré en rouge{NB}: elle est posée sur la cinquième ligne à partir du bord droit, loin des autres pierres de la zone.",
      noirs37, blancs37, "P10", "37", f"AlphaGo (noirs) vient de jouer en P10, sur la cinquième ligne à partir du bord.")
goban("go-coup-78.svg", "Partie 4, coup 78 de Lee Sedol",
      f"Un goban de 19 lignes sur 19, avec la position de la quatrième partie après 78 coups. Lee Sedol a les blancs. Le coup 78, une pierre blanche en L11, "
      "est entourée en rouge, au milieu d'un groupe de pierres noires au centre du goban.",
      NOIRS78, BLANCS78, "L11", "78", f"Lee Sedol (blancs) vient de jouer en L11, au cœur de la zone noire du centre.")
print("go-coup-37.svg et go-coup-78.svg écrits")
