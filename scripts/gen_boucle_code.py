"""Module 4, « Programmer avec des agents » : la boucle d'un agent de programmation. Explorer, modifier, vérifier, lire le
résultat, jusqu'à ce que les tests passent ; chaque étape passe par des commandes classiques d'Unix, et tout est du texte."""
from pathlib import Path
import math

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
TERM, TERM_TXT = "#1f2421", "#e5e7e0"
W, H = 840, 478
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>La boucle d'un agent de programmation</title>",
     "<desc>Une boucle en quatre étapes autour d'une tâche : explorer le projet, avec ls, find, grep et cat ; modifier le code, "
     "en remplaçant des lignes précises dans un fichier ; vérifier, en lançant les tests ou la compilation, avec python -m "
     "pytest ou make ; lire le résultat, c'est-à-dire les messages d'erreur et le code de sortie, puis revenir à l'exploration. "
     "Quand les tests passent, l'agent sort de la boucle : il consulte git diff, résume ce qu'il a fait et, si on le lui permet, "
     "enregistre une version avec git commit. Une note rappelle que tout passe par du texte : commandes, résultats et "
     "erreurs.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{TEAL}"/></marker>'
     f'<marker id="pg" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">La boucle d\'un agent de programmation{NB}: tout passe par du texte</text>']
CX, CY, R = 300, 270, 150
ETAPES = [("1. explorer", "où est le problème ?", ["ls", "find . -name '*.py'", 'grep -rn "moyenne" .', "cat notes.py"], -90),
          ("2. modifier", "changer quelques lignes", ["notes.py, ligne 3 :", "+ if not notes:", "+     return None"], 0),
          ("3. vérifier", "le verdict des tests", ["python -m pytest", "make"], 90),
          ("4. lire le résultat", "erreurs, code de sortie", ["FAILED test_notes.py…", "code de sortie : 1"], 180)]
# le cercle de la boucle, en quatre arcs
for k in range(4):
    a1, a2 = math.radians(-90 + k * 90 + 22), math.radians(-90 + (k + 1) * 90 - 22)
    x1, y1, x2, y2 = CX + R * math.cos(a1), CY + R * math.sin(a1), CX + R * math.cos(a2), CY + R * math.sin(a2)
    o.append(f'<path d="M{x1:.1f} {y1:.1f} A{R} {R} 0 0 1 {x2:.1f} {y2:.1f}" fill="none" stroke="{TEAL}" stroke-width="2.4" marker-end="url(#p)"/>')
o.append(f'<circle cx="{CX}" cy="{CY}" r="54" fill="{PANNEAU}" stroke="{BORD}" stroke-width="1.4"/>')
o.append(f'<text x="{CX}" y="{CY - 6}" font-size="12.5" fill="{ENCRE}" text-anchor="middle" font-weight="700">la tâche</text>')
o.append(f'<text x="{CX}" y="{CY + 11}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle" font-style="italic">«{NB}les tests</text>')
o.append(f'<text x="{CX}" y="{CY + 25}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle" font-style="italic">échouent{NB}»</text>')
for nom, sous, cmds, ang in ETAPES:
    a = math.radians(ang)
    x, y = CX + R * math.cos(a), CY + R * math.sin(a)
    bw = 168
    bh = 46 + 16 * len(cmds)
    bx = x - bw / 2
    by = y - bh / 2
    o.append(f'<rect x="{bx:.1f}" y="{by:.1f}" width="{bw}" height="{bh}" rx="9" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="1.8"/>')
    o.append(f'<text x="{x:.1f}" y="{by + 18:.1f}" font-size="12.5" fill="{TEAL}" text-anchor="middle" font-weight="700">{nom}</text>')
    o.append(f'<text x="{x:.1f}" y="{by + 33:.1f}" font-size="10" fill="{ENCRE_PALE}" text-anchor="middle">{sous}</text>')
    o.append(f'<rect x="{bx + 8:.1f}" y="{by + 39:.1f}" width="{bw - 16}" height="{16 * len(cmds) + 2}" rx="4" fill="{TERM}"/>')
    for j, c in enumerate(cmds):
        mono = ang in (-90, 90)
        txt = (("$ " if mono else "") + c.replace("<", "&lt;")).replace("  ", "\u00a0\u00a0")
        coul = TERM_TXT if mono else "#c9cdc4"
        o.append(f'<text x="{bx + 14:.1f}" y="{by + 52 + 16 * j:.1f}" font-size="10" fill="{coul}" font-family="ui-monospace, Menlo, monospace">{txt}</text>')
# la sortie de la boucle
EX, EY = 560, 360
o.append(f'<path d="M{CX + 90} {CY + 128} C {CX + 180} {CY + 150} {EX - 60} {EY + 40} {EX - 6} {EY + 40}" fill="none" stroke="{GRIS}" stroke-width="1.8" stroke-dasharray="6 4" marker-end="url(#pg)"/>')
o.append(f'<text x="{(CX + 90 + EX) / 2}" y="{EY + 72}" font-size="11" fill="{GRIS}" text-anchor="middle" font-weight="700">quand les tests passent</text>')
o.append(f'<rect x="{EX}" y="{EY}" width="250" height="96" rx="9" fill="{PANNEAU}" stroke="{BLEU}" stroke-width="1.8"/>')
o.append(f'<text x="{EX + 125}" y="{EY + 20}" font-size="12.5" fill="{BLEU}" text-anchor="middle" font-weight="700">sortir de la boucle</text>')
o.append(f'<rect x="{EX + 10}" y="{EY + 28}" width="230" height="38" rx="4" fill="{TERM}"/>')
for j, c in enumerate(["$ git diff", "$ git commit   (si on le lui permet)"]):
    o.append(f'<text x="{EX + 16}" y="{EY + 42 + 16 * j}" font-size="10" fill="{TERM_TXT}" font-family="ui-monospace, Menlo, monospace">{c}</text>')
o.append(f'<text x="{EX + 125}" y="{EY + 84}" font-size="11" fill="{ENCRE}" text-anchor="middle">puis résumer ce qui a été fait</text>')
# la note sur le texte
NX, NY = 560, 96
o.append(f'<rect x="{NX}" y="{NY}" width="250" height="150" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
for j, (l, gras) in enumerate([("Tout est du texte", True), ("les commandes, écrites par le modèle,", False), ("et leurs résultats, lus par le modèle.", False),
                               ("Chaque outil Unix fait une chose,", False), ("lit du texte et en produit.", False), ("Un seul outil, « exécuter une", False),
                               ("commande », en donne des milliers.", False)]):
    o.append(f'<text x="{NX + 14}" y="{NY + 24 + j * 18}" font-size="{12.5 if gras else 11.5}" fill="{BRUN if gras else ENCRE}"'
             + (' font-weight="700"' if gras else "") + f'>{l}</text>')
o.append("</svg>")
(OUT / "boucle-agent-code.svg").write_text("\n".join(o) + "\n")
print("boucle-agent-code.svg écrit")
