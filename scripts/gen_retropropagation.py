"""Module 3, « Entraîner un réseau » : la propagation avant et la rétropropagation, sur le réseau du XOR."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module3"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, GRILLE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#e8dfc9", "#fbf7ee")
NB, FINE = " ", " "
POLICE = 'font-family="system-ui, -apple-system, sans-serif"'


def fleche(o, x1, y1, x2, y2, coul, ep):
    """Une flèche de (x1, y1) à (x2, y2), dont la pointe grandit avec l'épaisseur."""
    import math
    a, L = math.atan2(y2 - y1, x2 - x1), 9 + ep * 1.6
    bx, by = x2 - L * math.cos(a), y2 - L * math.sin(a)
    l = 3.5 + ep
    o.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="{coul}" stroke-width="{ep}" stroke-linecap="round"/>')
    o.append(f'<polygon points="{x2:.1f},{y2:.1f} {bx + l * math.sin(a):.1f},{by - l * math.cos(a):.1f} {bx - l * math.sin(a):.1f},{by + l * math.cos(a):.1f}" fill="{coul}"/>')


def panneau(o, ox, titre, sous_titre, retour):
    Wp = 320
    o.append(f'<rect x="{ox}" y="58" width="{Wp}" height="330" rx="10" fill="{PANNEAU}" stroke="{AXE}" stroke-width="1.2"/>')
    o.append(f'<text x="{ox + Wp / 2}" y="84" font-size="14" fill="{ENCRE}" text-anchor="middle" font-weight="700">{titre}</text>')
    o.append(f'<text x="{ox + Wp / 2}" y="103" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle">{sous_titre}</text>')
    xe, xc, xs = ox + 52, ox + 160, ox + 268
    ye, yc, ys = (170, 270), (170, 270), 220
    coul = ROUGE if retour else TEAL
    # connexions entre l'entrée et la couche cachée
    for y1 in ye:
        for k, y2 in enumerate(yc):
            dy = (y2 - y1) * 0.12
            if retour:
                fleche(o, xc - 30, y2 - dy, xe + 26, y1 + dy, coul, 2.6 if k == 0 else 1.2)
            else:
                fleche(o, xe + 26, y1 + dy, xc - 30, y2 - dy, coul, 1.8)
    # connexions entre la couche cachée et la sortie
    for k, y1 in enumerate(yc):
        dy = (ys - y1) * 0.2
        if retour:
            fleche(o, xs - 30, ys - dy, xc + 30, y1 + dy, coul, 4.2 if k == 0 else 1.4)
        else:
            fleche(o, xc + 30, y1 + dy, xs - 30, ys - dy, coul, 1.8)
    for y, nom, val in zip(ye, "AB", ("0", "1")):
        o.append(f'<circle cx="{xe}" cy="{y}" r="22" fill="{FOND}" stroke="{BLEU}" stroke-width="2"/>')
        o.append(f'<text x="{xe}" y="{y + 5}" font-size="13" fill="{BLEU}" text-anchor="middle" font-weight="700">{nom} = {val}</text>')
    for y, nom in zip(yc, ("neurone 1", "neurone 2")):
        o.append(f'<circle cx="{xc}" cy="{y}" r="26" fill="{FOND}" stroke="{TEAL}" stroke-width="2.2"/>')
        o.append(f'<text x="{xc}" y="{y - 2}" font-size="10.5" fill="{TEAL}" text-anchor="middle" font-weight="700">neurone</text>')
        o.append(f'<text x="{xc}" y="{y + 12}" font-size="12" fill="{TEAL}" text-anchor="middle" font-weight="700">{nom[-1]}</text>')
    o.append(f'<circle cx="{xs}" cy="{ys}" r="26" fill="{FOND}" stroke="{BRUN}" stroke-width="2.2"/>')
    o.append(f'<text x="{xs}" y="{ys + 4}" font-size="11.5" fill="{BRUN}" text-anchor="middle" font-weight="700">sortie</text>')
    return xe, xc, xs, yc, ys


def figure():
    W, H = 700, 430
    lignes = ['<?xml version="1.0" encoding="UTF-8"?>',
              f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" {POLICE}>',
              "<title>La propagation avant et la rétropropagation</title>",
              f"<desc>Deux panneaux qui montrent le réseau du XOR{NB}: deux entrées, deux neurones cachés, un neurone de sortie. À gauche, la propagation avant{NB}: "
              f"les flèches vont de l'entrée vers la sortie{FINE}; le réseau répond 0,62 alors que la bonne réponse est 1, soit une erreur de 0,38. À droite, la "
              f"rétropropagation{NB}: les flèches vont de la sortie vers l'entrée{FINE}; le neurone 1, relié à la sortie par un poids élevé, reçoit une grande part "
              "de l'erreur, et le neurone 2, relié par un poids faible, une petite part.</desc>",
              f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>']
    o = lignes
    o.append(f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Pour chaque exemple{NB}: un aller, puis un retour</text>')
    # --- l'aller
    xe, xc, xs, yc, ys = panneau(o, 22, "1. La propagation avant", "le réseau calcule sa réponse", False)
    o.append(f'<text x="{xs}" y="{ys - 40}" font-size="12.5" fill="{BRUN}" text-anchor="middle" font-weight="700">0,62</text>')
    y = 338
    for k, (t, v, c) in enumerate((("réponse du réseau", "0,62", BRUN), ("bonne réponse", "1", ENCRE), ("erreur", "0,38", ROUGE))):
        x = 22 + 58 + k * 102
        o.append(f'<text x="{x}" y="{y}" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">{t}</text>')
        o.append(f'<text x="{x}" y="{y + 22}" font-size="17" fill="{c}" text-anchor="middle" font-weight="700">{v}</text>')
    # --- le retour
    xe, xc, xs, yc, ys = panneau(o, 358, "2. La rétropropagation", "l'erreur remonte vers l'entrée", True)
    o.append(f'<text x="{xs}" y="{ys - 40}" font-size="12.5" fill="{ROUGE}" text-anchor="middle" font-weight="700">erreur</text>')
    o.append(f'<text x="{xc}" y="{yc[0] - 36}" font-size="12" fill="{ROUGE}" text-anchor="middle" font-weight="700">grande part</text>')
    o.append(f'<text x="{xc}" y="{yc[1] + 46}" font-size="12" fill="{ROUGE}" text-anchor="middle" font-weight="700">petite part</text>')
    o.append(f'<text x="{358 + 160}" y="352" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">Une flèche épaisse correspond à un poids élevé.</text>')
    o.append(f'<text x="{358 + 160}" y="370" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">Chaque poids reçoit sa part de l\'erreur.</text>')
    o.append(f'<text x="{W / 2}" y="{H - 16}" font-size="12.5" fill="{GRIS}" text-anchor="middle">Après le retour, tous les poids sont modifiés un peu, puis on passe à l\'exemple suivant.</text>')
    o.append("</svg>")
    (OUT / "retropropagation.svg").write_text("\n".join(o) + "\n")


figure()
print("retropropagation.svg écrit")
