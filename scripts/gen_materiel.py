"""Module 3, « Le matériel et les outils » : CPU et GPU, frise du matériel et du logiciel."""
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


def cpu_gpu():
    W, H = 700, 380
    o = entete(W, H, "Un processeur ordinaire et un processeur graphique",
               f"Deux panneaux. À gauche, un processeur ordinaire (CPU){NB}: huit gros cœurs, de couleurs différentes, qui traitent chacun une tâche différente. "
               f"À droite, un processeur graphique (GPU){NB}: une grille de plusieurs centaines de petits cœurs identiques, qui font tous le même calcul en même temps.")
    o.append(f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Deux façons de calculer</text>')
    for ox, titre, sous in ((22, "Un processeur ordinaire (CPU)", "quelques cœurs puissants, des tâches variées"),
                            (358, "Un processeur graphique (GPU)", "des milliers de cœurs simples, le même calcul")):
        o.append(f'<rect x="{ox}" y="58" width="320" height="290" rx="10" fill="{PANNEAU}" stroke="{AXE}" stroke-width="1.2"/>')
        o.append(f'<text x="{ox + 160}" y="84" font-size="14" fill="{ENCRE}" text-anchor="middle" font-weight="700">{titre}</text>')
        o.append(f'<text x="{ox + 160}" y="103" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle">{sous}</text>')
    # le CPU : 4 × 2 gros cœurs
    cx0, cy0, c, e = 22 + 37, 126, 54, 10
    couleurs = [BRUN, BLEU, TEAL, ROUGE, BLEU, ROUGE, BRUN, TEAL]
    for k in range(8):
        x, y = cx0 + (k % 4) * (c + e), cy0 + (k // 4) * (c + e) + 36
        o.append(f'<rect x="{x}" y="{y}" width="{c}" height="{c}" rx="6" fill="{couleurs[k]}" fill-opacity="0.8"/>')
    o.append(f'<text x="{22 + 160}" y="328" font-size="12" fill="{GRIS}" text-anchor="middle">chaque cœur fait autre chose</text>')
    # le GPU : une grille serrée de petits cœurs
    n, m, t, g = 30, 21, 7, 2
    gx0, gy0 = 358 + (320 - (n * (t + g) - g)) / 2, 122
    for j in range(m):
        for i in range(n):
            o.append(f'<rect x="{gx0 + i * (t + g):.1f}" y="{gy0 + j * (t + g)}" width="{t}" height="{t}" rx="1.5" fill="{TEAL}" fill-opacity="0.8"/>')
    o.append(f'<text x="{358 + 160}" y="328" font-size="12" fill="{GRIS}" text-anchor="middle">tous les cœurs font le même calcul, en même temps</text>')
    o.append("</svg>")
    (OUT / "cpu-gpu.svg").write_text("\n".join(o) + "\n")


def frise():
    W, H = 700, 420
    o = entete(W, H, "Le matériel et le logiciel de l'apprentissage profond, de 1970 à 2016",
               f"Une frise chronologique à deux rangées. En haut, le matériel{NB}: fondation de Nvidia en 1993, GeForce 256 en 1999, CUDA en 2007, un réseau entraîné "
               f"70 fois plus vite sur GPU en 2009, premières machines conçues pour l'apprentissage profond en 2016. En bas, le logiciel{NB}: la méthode de Linnainmaa "
               f"en 1970, Torch en 2002, Theano en 2007, Caffe en 2013, TensorFlow et Keras en 2015, PyTorch en 2016. Au centre, en 2012, AlexNet, où les deux histoires se rejoignent.")
    o.append(f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Deux histoires qui se rejoignent en 2012</text>')
    ya = 218
    X = lambda an: 118 + (an - 1990) * 16.6
    # l'axe, avec une coupure entre 1970 et 1990
    o.append(f'<line x1="40" y1="{ya}" x2="88" y2="{ya}" stroke="{AXE}" stroke-width="2.5"/>')
    o.append(f'<path d="M88 {ya - 7} l8 14 M98 {ya - 7} l8 14" stroke="{GRIS}" stroke-width="1.5" fill="none"/>')
    o.append(f'<line x1="106" y1="{ya}" x2="{W - 30}" y2="{ya}" stroke="{AXE}" stroke-width="2.5"/>')
    for an in (1990, 2000, 2010, 2020):
        o.append(f'<line x1="{X(an):.1f}" y1="{ya - 5}" x2="{X(an):.1f}" y2="{ya + 5}" stroke="{GRIS}" stroke-width="1.5"/>')

    def evenement(x, an, nom, haut, niveau, ancre, coul):
        s = -1 if haut else 1
        bout = ya + s * (16 + niveau * 40)
        o.append(f'<line x1="{x:.1f}" y1="{ya}" x2="{x:.1f}" y2="{bout}" stroke="{coul}" stroke-width="1.4"/>')
        o.append(f'<circle cx="{x:.1f}" cy="{ya}" r="5" fill="{coul}" stroke="{FOND}" stroke-width="1.5"/>')
        tx = x + {"middle": 0, "end": -6, "start": 6}[ancre]
        y_an, y_nom = (bout - 22, bout - 7) if haut else (bout + 14, bout + 29)
        if ancre != "middle":           # le texte est à côté du trait : on le remonte pour qu'il longe son extrémité
            y_an, y_nom = (bout + 4, bout + 19) if haut else (bout - 12, bout + 3)
        o.append(f'<text x="{tx:.1f}" y="{y_an}" font-size="12.5" fill="{coul}" text-anchor="{ancre}" font-weight="700">{an}</text>')
        o.append(f'<text x="{tx:.1f}" y="{y_nom}" font-size="11.5" fill="{ENCRE}" text-anchor="{ancre}">{nom}</text>')

    evenement(X(1993), 1993, "Nvidia", True, 1, "middle", BRUN)
    evenement(X(1999), 1999, "GeForce 256", True, 1, "middle", BRUN)
    evenement(X(2007), 2007, "CUDA", True, 1, "end", BRUN)
    evenement(X(2009), 2009, "70 fois plus vite", True, 2, "end", BRUN)
    evenement(X(2016), 2016, "machines dédiées", True, 1, "start", BRUN)
    evenement(64, 1970, "Linnainmaa", False, 1, "middle", TEAL)
    evenement(X(2002), 2002, "Torch", False, 1, "middle", TEAL)
    evenement(X(2007), 2007, "Theano", False, 1, "middle", TEAL)
    evenement(X(2013), 2013, "Caffe", False, 1, "end", TEAL)
    evenement(X(2015), 2015, "TensorFlow, Keras", False, 2, "end", TEAL)
    evenement(X(2016), 2016, "PyTorch", False, 1, "start", TEAL)
    # 2012 : AlexNet, des deux côtés de l'axe
    x = X(2012)
    o.append(f'<line x1="{x:.1f}" y1="{ya - 132}" x2="{x:.1f}" y2="{ya}" stroke="{ROUGE}" stroke-width="1.8" stroke-dasharray="5 4"/>')
    o.append(f'<circle cx="{x:.1f}" cy="{ya}" r="8" fill="{ROUGE}" stroke="{FOND}" stroke-width="2"/>')
    o.append(f'<text x="{x:.1f}" y="{ya - 154}" font-size="13" fill="{ROUGE}" text-anchor="middle" font-weight="700">2012</text>')
    o.append(f'<text x="{x:.1f}" y="{ya - 139}" font-size="12" fill="{ENCRE}" text-anchor="middle">AlexNet</text>')
    o.append(f'<text x="40" y="{ya - 120}" font-size="13" fill="{BRUN}" font-weight="700">Le matériel</text>')
    o.append(f'<text x="40" y="{ya + 128}" font-size="13" fill="{TEAL}" font-weight="700">Le logiciel</text>')
    o.append(f'<text x="{W / 2}" y="{H - 18}" font-size="12.5" fill="{GRIS}" text-anchor="middle">L\'axe est coupé entre 1970 et 1990.</text>')
    o.append("</svg>")
    (OUT / "frise-materiel-logiciel.svg").write_text("\n".join(o) + "\n")


cpu_gpu()
frise()
print("cpu-gpu.svg et frise-materiel-logiciel.svg écrits")
