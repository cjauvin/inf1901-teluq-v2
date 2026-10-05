"""Module 4, « Du modèle à l'assistant » : le temps qu'ont mis quelques services en ligne à atteindre 100 millions
d'utilisateurs.

Sources : UBS d'après Similarweb, rapporté par Reuters le 1er février 2023 (ChatGPT, TikTok, Instagram) ; pour les
autres, l'écart entre le lancement et l'annonce des 100 millions par l'entreprise : Facebook (février 2004 → août 2008),
Twitter (juillet 2006 → septembre 2011, utilisateurs actifs), Spotify (octobre 2008 → juin 2016, utilisateurs actifs
mensuels), Netflix (lancement de la diffusion en ligne, janvier 2007 → avril 2017, abonnés), Threads (5 juillet 2023 →
10 juillet 2023, inscriptions).
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "
SERVICES = [                                                # nom, année de lancement, mois, étiquette
    ("Threads*", 2023, 5 / 30, f"5{NB}jours"),
    ("ChatGPT", 2022, 2, f"2{NB}mois"),
    ("TikTok", 2017, 9, f"9{NB}mois"),
    ("Instagram", 2010, 30, f"2{NB}ans et demi"),
    ("Facebook", 2004, 54, f"4{NB}ans et demi"),
    ("Twitter", 2006, 62, f"5{NB}ans"),
    ("Spotify", 2008, 92, f"7{NB}ans et demi"),
    ("Netflix", 2007, 123, f"10{NB}ans"),
]
W, H = 760, 496
XL, X0, X1 = 40, 200, 640                                   # noms, début et fin des barres
MMAX = 132
RH, RG, Y0 = 30, 12, 92
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Le temps pour atteindre 100 millions d'utilisateurs</title>",
     "<desc>Un graphique à barres horizontales : le temps qu'a mis chaque service, après son lancement, à atteindre 100 millions "
     "d'utilisateurs. Threads, 2023 : 5 jours, en inscriptions. ChatGPT, 2022 : 2 mois. TikTok, 2017 : 9 mois. Instagram, 2010 : "
     "2 ans et demi. Facebook, 2004 : 4 ans et demi. Twitter, 2006 : 5 ans. Spotify, 2008 : 7 ans et demi. Netflix, 2007, pour sa "
     "diffusion en ligne : 10 ans.</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Combien de temps pour atteindre 100{NB}millions d\'utilisateurs{FINE}?</text>',
     f'<text x="{X0 - 8}" y="{Y0 - 14}" font-size="10.5" fill="{GRIS}" text-anchor="end">lancement</text>']
x = lambda mois: X0 + (X1 - X0) * mois / MMAX
yb = Y0 + len(SERVICES) * (RH + RG) - RG + 8
for an in range(0, 12, 2):                                  # graduations, en années
    xa = x(12 * an)
    o.append(f'<line x1="{xa:.1f}" y1="{Y0 - 6}" x2="{xa:.1f}" y2="{yb}" stroke="{AXE}" stroke-width="1" stroke-dasharray="{"none" if an == 0 else "3 4"}"/>')
    o.append(f'<text x="{xa:.1f}" y="{yb + 16}" font-size="10.5" fill="{GRIS}" text-anchor="middle">{an if an else 0}{(NB + "ans") if an else ""}</text>')
for k, (nom, an, mois, lab) in enumerate(SERVICES):
    y = Y0 + k * (RH + RG)
    vedette = nom == "ChatGPT"
    coul = ROUGE if vedette else (AXE if nom.startswith("Threads") else BRUN)
    o.append(f'<text x="{XL}" y="{y + 20}" font-size="13" fill="{ENCRE}" font-weight="{700 if vedette else 400}">{nom}</text>')
    o.append(f'<text x="{X0 - 8}" y="{y + 20}" font-size="11" fill="{GRIS}" text-anchor="end">{an}</text>')
    o.append(f'<rect x="{X0}" y="{y}" width="{max(2.5, x(mois) - X0):.1f}" height="{RH}" rx="3" fill="{coul}"/>')
    o.append(f'<text x="{max(2.5, x(mois) - X0) + X0 + 8:.1f}" y="{y + 20}" font-size="12.5" fill="{ENCRE}" font-weight="{700 if vedette else 400}" stroke="{FOND}" stroke-width="5" paint-order="stroke">{lab}</text>')
o.append(f'<text x="{XL}" y="{H - 34}" font-size="10.5" fill="{ENCRE_PALE}">* Threads{NB}: inscriptions, grâce aux comptes Instagram existants. Netflix{NB}: depuis le lancement de sa diffusion en ligne.</text>')
o.append(f'<text x="{XL}" y="{H - 18}" font-size="10.5" fill="{ENCRE_PALE}">Sources{NB}: UBS et Similarweb (ChatGPT, TikTok, Instagram){FINE}; annonces des entreprises (les autres).</text>')
o.append("</svg>")
(OUT / "cent-millions-utilisateurs.svg").write_text("\n".join(o) + "\n")
print("cent-millions-utilisateurs.svg écrit")
