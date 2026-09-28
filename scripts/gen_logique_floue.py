"""« Fièvre élevée » : seuil de la logique classique contre degré de la logique floue."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module1"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, AXE, GRILLE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#b8a888", "#e8dfc9", "#fbf7ee")
NB, FINE = " ", " "
T0, T1 = 36.5, 40.5          # axe des températures
SEUIL = 38.5                 # seuil classique
BAS, HAUT = 37.5, 39.0       # rampe floue : 0 sous BAS, 1 au-dessus de HAUT
TEST = 38.4                  # la température qu'on examine


def classique(t):
    return 1.0 if t >= SEUIL else 0.0


def flou(t):
    return min(1.0, max(0.0, (t - BAS) / (HAUT - BAS)))


def virgule(x, n=1):
    return f"{x:.{n}f}".replace(".", ",")


def panneau(ox, titre, sous_titre, f, marches, o):
    W, H = 300, 270
    o.append(f'<rect x="{ox}" y="58" width="{W}" height="{H}" rx="10" fill="{PANNEAU}" stroke="{AXE}" stroke-width="1.2"/>')
    o.append(f'<text x="{ox + W / 2:.0f}" y="84" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="700">{titre}</text>')
    o.append(f'<text x="{ox + W / 2:.0f}" y="103" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle">{sous_titre}</text>')
    gx0, gx1, gy0, gy1 = ox + 58, ox + W - 22, 272, 130      # zone du graphique (gy0 = bas)
    X = lambda t: gx0 + (t - T0) / (T1 - T0) * (gx1 - gx0)
    Y = lambda v: gy0 - v * (gy0 - gy1)
    for v in (0, 0.5, 1):
        o.append(f'<line x1="{gx0}" y1="{Y(v):.1f}" x2="{gx1}" y2="{Y(v):.1f}" stroke="{GRILLE}" stroke-width="1"/>')
        o.append(f'<text x="{gx0 - 10}" y="{Y(v) + 4:.1f}" font-size="11.5" fill="{GRIS}" text-anchor="end">{virgule(v, 1) if v == 0.5 else int(v)}</text>')
    for t in (37, 38, 39, 40):
        o.append(f'<text x="{X(t):.1f}" y="{gy0 + 20}" font-size="11.5" fill="{GRIS}" text-anchor="middle">{t}{NB}°C</text>')
    o.append(f'<line x1="{gx0}" y1="{gy0}" x2="{gx1}" y2="{gy0}" stroke="{AXE}" stroke-width="1.5"/>')
    o.append(f'<line x1="{gx0}" y1="{gy0}" x2="{gx0}" y2="{gy1 - 6}" stroke="{AXE}" stroke-width="1.5"/>')
    # la courbe
    pts = " ".join(f"{X(t):.1f},{Y(f(t)):.1f}" for t in marches)
    o.append(f'<polyline points="{pts}" fill="none" stroke="{BRUN}" stroke-width="3" stroke-linejoin="round"/>')
    # la température examinée
    v = f(TEST)
    o.append(f'<line x1="{X(TEST):.1f}" y1="{gy0}" x2="{X(TEST):.1f}" y2="{Y(v):.1f}" stroke="{TEAL}" stroke-width="1.5" stroke-dasharray="4 3"/>')
    o.append(f'<circle cx="{X(TEST):.1f}" cy="{Y(v):.1f}" r="6" fill="{TEAL}" stroke="{PANNEAU}" stroke-width="2"/>')
    etiquette = f"{virgule(TEST)}{NB}°C → {virgule(v, 1) if 0 < v < 1 else int(v)}"
    o.append(f'<text x="{X(TEST) - 10:.1f}" y="{Y(v) - 12:.1f}" font-size="12" fill="{TEAL}" text-anchor="end" font-weight="700">{etiquette}</text>')


o = ['<?xml version="1.0" encoding="UTF-8"?>',
     '<svg viewBox="0 0 660 380" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Fièvre élevée : un seuil ou un degré</title>",
     f"<desc>Deux graphiques du degré auquel une température est une «{FINE}fièvre élevée{FINE}», de 0 à 1, en fonction de la température, de 36,5 à 40,5{NB}°C. À gauche, la logique classique{NB}: une marche d'escalier, 0 sous 38,5{NB}°C et 1 à partir de 38,5{NB}°C{FINE}; une fièvre de 38,4{NB}°C vaut 0. À droite, la logique floue{NB}: une rampe qui monte de 0 à 37,5{NB}°C jusqu'à 1 à 39{NB}°C{FINE}; une fièvre de 38,4{NB}°C vaut 0,6.</desc>",
     f'<rect x="0" y="0" width="660" height="380" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="330" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">À quel point la fièvre est-elle «{FINE}élevée{FINE}»{FINE}?</text>']
panneau(24, "Logique classique", f"vrai ou faux, avec un seuil à 38,5{NB}°C", classique,
        [T0, SEUIL - 1e-9, SEUIL, T1], o)
panneau(336, "Logique floue", "vrai à un certain degré, entre 0 et 1", flou,
        [T0, BAS, HAUT, T1], o)
o.append(f'<text x="330" y="360" font-size="13" fill="{ENCRE_PALE}" text-anchor="middle">Un dixième de degré sépare 38,4 de 38,5{NB}°C{FINE}: la logique floue n\'en fait pas un saut de 0 à 1.</text>')
o.append('</svg>')
(OUT / "logique-floue.svg").write_text("\n".join(o) + "\n")
print("logique-floue.svg écrit")
