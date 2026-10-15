"""Module 5, « Sur quoi porte le débat ? » : démonter un désaccord. Deux personnes s'opposent sur une conclusion (« il faut
freiner l'IA » / « surtout pas ») ; sous la conclusion, six plans de désaccord, avec la position de chacune. Elles sont
d'accord sur les faits et sur les concepts : leur désaccord porte sur les valeurs, le pouvoir et la façon de décider dans
l'incertitude, et la stratégie en découle. Exemple construit pour l'illustration."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module5" / "demonter-un-desaccord.svg"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#fbf7ee")
NB = " "
PLANS = [  # plan, Camille, Sacha, même avis ?
    ("Faits et prévisions", "Des IA plus capables que nous d'ici 20 ans", "Des IA plus capables que nous d'ici 20 ans", True),
    ("Concepts", "Ces IA auront des buts propres", "Ces IA auront des buts propres", True),
    ("Valeurs", "Éviter une catastrophe, avant tout", "Guérir des maladies, avant tout", False),
    ("Pouvoir", "Des lois et des accords entre pays", "La concurrence entre entreprises", False),
    ("Décider dans l'incertitude", "Dans le doute, ralentir", "Dans le doute, avancer et corriger", False),
    ("Stratégie", "Une pause, puis un traité", "Aller vite, pour ne pas perdre la course", False),
]
W, H = 840, 560
XA, XP, XB = 165, 420, 675          # centres : Camille, plan, Sacha
LW = 250
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Démonter un désaccord</title>",
     "<desc>Deux personnes s'opposent. Camille conclut : « Il faut freiner l'IA. » Sacha conclut : « Surtout pas. » Sous ces "
     "conclusions, six plans, avec la position de chacune. Faits et prévisions : toutes deux attendent des IA plus capables que "
     "nous d'ici vingt ans, même avis. Concepts : toutes deux pensent que ces IA auront des buts propres, même avis. "
     "Valeurs : pour Camille, éviter une catastrophe, avant tout ; pour Sacha, guérir des maladies, avant tout. Pouvoir : des lois et "
     "des accords entre pays, contre la concurrence entre entreprises. Décider dans l'incertitude : dans le doute, ralentir, "
     "contre dans le doute, avancer et corriger. Stratégie : une pause puis un traité, contre aller vite pour ne pas perdre la "
     "course. Le désaccord ne porte pas sur les faits, mais sur les valeurs, le pouvoir et la façon de décider dans "
     "l'incertitude ; la stratégie en découle.</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="34" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Démonter un désaccord</text>']
# les deux conclusions
for x, nom, concl, coul in [(XA, "Camille", "«" + NB + "Il faut freiner l'IA." + NB + "»", ROUGE), (XB, "Sacha", "«" + NB + "Surtout pas." + NB + "»", BRUN)]:
    o.append(f'<rect x="{x - LW / 2}" y="54" width="{LW}" height="58" rx="10" fill="{PANNEAU}" stroke="{coul}" stroke-width="1.8"/>')
    o.append(f'<text x="{x}" y="77" font-size="12" fill="{coul}" text-anchor="middle" font-weight="700">{nom}</text>')
    o.append(f'<text x="{x}" y="99" font-size="13" fill="{ENCRE}" text-anchor="middle" font-style="italic">{concl}</text>')
o.append(f'<text x="{XP}" y="82" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">la conclusion</text>')
o.append(f'<text x="{XP}" y="98" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">visible</text>')
o.append(f'<text x="{XP}" y="140" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle" font-style="italic">ce qui la soutient, plan par plan</text>')
Y0, DY = 158, 56
for i, (plan, a, b, meme) in enumerate(PLANS):
    y = Y0 + i * DY
    coul = TEAL if meme else ROUGE
    fond = "#e3eeec" if meme else "#f6e1dd"
    if i == 5:
        o.append(f'<line x1="40" y1="{y - 6}" x2="{W - 40}" y2="{y - 6}" stroke="{BORD}" stroke-dasharray="5 4"/>')
    for x, t in [(XA, a), (XB, b)]:
        o.append(f'<rect x="{x - LW / 2}" y="{y}" width="{LW}" height="42" rx="7" fill="{fond}" stroke="{coul}" stroke-width="1.2"/>')
        o.append(f'<text x="{x}" y="{y + 25}" font-size="11.5" fill="{ENCRE}" text-anchor="middle">{t}</text>')
    o.append(f'<text x="{XP}" y="{y + 18}" font-size="12" fill="{ENCRE}" text-anchor="middle" font-weight="700">{plan}</text>')
    o.append(f'<text x="{XP}" y="{y + 34}" font-size="11" fill="{coul}" text-anchor="middle" font-weight="700">{"même avis" if meme else "désaccord"}</text>')
o.append(f'<text x="{W / 2}" y="{H - 14}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">Les faits ne les séparent pas{NB}: '
         f'les valeurs, le pouvoir et le rapport au risque, oui. La stratégie en découle.</text>')
o.append("</svg>")
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(o) + "\n")
print(OUT.name, "écrit")
