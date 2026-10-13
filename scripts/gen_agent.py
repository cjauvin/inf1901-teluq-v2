"""Module 4, « Des outils et des agents » : le principe d'un agent. Un grand modèle de langage, au centre, tourne dans une
boucle (raisonner, agir, observer) ; ses actions passent par des outils ; chaque résultat s'ajoute à son contexte, jusqu'à
ce qu'il juge la tâche terminée et donne sa réponse."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
W, H = 840, 470
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Le principe d'un agent</title>",
     "<desc>À gauche, une tâche donnée par l'utilisateur : trouver trois articles récents sur un sujet et les résumer. Elle entre "
     "dans l'agent, dessiné comme un grand cadre. Au centre de l'agent, un grand modèle de langage. Autour de lui, une boucle en "
     "trois temps : raisonner, agir, observer. Pour agir, le modèle appelle un outil, à droite : recherche Web, exécution de code, "
     "documents et fichiers, courriel et agenda, mémoire. Le résultat de l'outil revient, et le modèle l'observe avant de raisonner "
     "de nouveau. En bas de l'agent, le contexte s'allonge à chaque tour : la tâche, un raisonnement, une action, un résultat, un "
     "autre raisonnement, et ainsi de suite. Quand le modèle juge la tâche terminée, il sort de la boucle et donne sa réponse "
     "finale, à gauche.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker>'
     f'<marker id="pt" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{TEAL}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Un agent{NB}: un modèle de langage qui agit en boucle, avec des outils</text>']


def boite(x, y, w, h, l1, l2="", coul=ENCRE_PALE, fond=PANNEAU, taille=12, gras=True):
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fond}" stroke="{coul}" stroke-width="1.6"/>')
    if l2:
        o.append(f'<text x="{x + w / 2}" y="{y + h / 2 - 3}" font-size="{taille}" fill="{ENCRE}" text-anchor="middle"{" font-weight=\"700\"" if gras else ""}>{l1}</text>')
        o.append(f'<text x="{x + w / 2}" y="{y + h / 2 + 13}" font-size="{taille - 1}" fill="{ENCRE_PALE}" text-anchor="middle">{l2}</text>')
    else:
        o.append(f'<text x="{x + w / 2}" y="{y + h / 2 + 4}" font-size="{taille}" fill="{ENCRE}" text-anchor="middle"{" font-weight=\"700\"" if gras else ""}>{l1}</text>')


def pastille(cx, cy, texte, w=92):
    o.append(f'<rect x="{cx - w / 2}" y="{cy - 15}" width="{w}" height="30" rx="15" fill="{TEAL}"/>')
    o.append(f'<text x="{cx}" y="{cy + 4.5}" font-size="12.5" fill="{PANNEAU}" text-anchor="middle" font-weight="700">{texte}</text>')


# la tâche et la réponse, à gauche
o.append(f'<text x="95" y="132" font-size="11" fill="{GRIS}" text-anchor="middle" font-weight="700">LA TÂCHE</text>')
boite(20, 140, 150, 78, "", coul=BLEU)
for k, l in enumerate(["«{0}Trouve trois".format(NB), "articles récents", "sur ARC et", f"résume-les{NB}»"]):
    o.append(f'<text x="95" y="{160 + k * 15}" font-size="11.5" fill="{ENCRE}" text-anchor="middle" font-style="italic">{l}</text>')
o.append(f'<text x="95" y="292" font-size="11" fill="{GRIS}" text-anchor="middle" font-weight="700">LA RÉPONSE</text>')
boite(20, 300, 150, 50, "les trois résumés", "quand la tâche est finie", coul=BLEU, taille=12)
# l'agent
AX, AY, AW, AH = 196, 58, 404, 384
o.append(f'<rect x="{AX}" y="{AY}" width="{AW}" height="{AH}" rx="14" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="2.2" stroke-dasharray="7 4"/>')
o.append(f'<rect x="{AX + 16}" y="{AY - 11}" width="72" height="22" rx="6" fill="{FOND}"/>')
o.append(f'<text x="{AX + 52}" y="{AY + 5}" font-size="13" fill="{TEAL}" text-anchor="middle" font-weight="700">l\'agent</text>')
o.append(f'<path d="M170 179 C 205 179 222 180 232 193" fill="none" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')
# le modèle au centre, et la boucle
MX, MY = 378, 210
boite(MX - 72, MY - 30, 144, 60, "grand modèle", "de langage", coul=TEAL, fond=FOND, taille=13)
R, A, O = (262, 210), (480, 128), (480, 292)
pastille(*R, "raisonner")
pastille(*A, "agir", 70)
pastille(*O, "observer", 86)
o.append(f'<path d="M{R[0]} {R[1] - 17} C {R[0]} {A[1] - 10} {A[0] - 80} {A[1]} {A[0] - 39} {A[1]}" fill="none" stroke="{TEAL}" stroke-width="1.8" marker-end="url(#pt)"/>')
o.append(f'<path d="M{O[0] - 45} {O[1]} C {O[0] - 100} {O[1]} {R[0]} {O[1] + 10} {R[0]} {R[1] + 19}" fill="none" stroke="{TEAL}" stroke-width="1.8" marker-end="url(#pt)"/>')
o.append(f'<text x="{MX}" y="{MY + 50}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">c\'est lui qui raisonne</text>')
o.append(f'<text x="{MX}" y="{MY + 64}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">et choisit l\'action</text>')
# la sortie de la boucle vers la réponse
o.append(f'<path d="M{R[0] - 46} {R[1] + 6} C {R[0] - 80} {R[1] + 40} {200} {325} {174} {325}" fill="none" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')
# le contexte, qui s'allonge
CY = 372
o.append(f'<text x="{AX + 18}" y="{CY - 8}" font-size="11" fill="{GRIS}" font-weight="700">LE CONTEXTE, QUI S\'ALLONGE À CHAQUE TOUR</text>')
x = AX + 18
for lab, c in [("tâche", BLEU), ("raisonnement", TEAL), ("action", TEAL), ("résultat", BRUN), ("raisonnement", TEAL), ("…", GRIS)]:
    w = 12 + 6.1 * len(lab)
    o.append(f'<rect x="{x}" y="{CY}" width="{w}" height="22" rx="5" fill="{c}"/>')
    o.append(f'<text x="{x + w / 2}" y="{CY + 15}" font-size="10.5" fill="{PANNEAU}" text-anchor="middle" font-weight="700">{lab}</text>')
    x += w + 5
o.append(f'<text x="{AX + 18}" y="{CY + 44}" font-size="10.5" fill="{ENCRE_PALE}">le modèle relit tout ce contexte avant chaque nouvelle étape</text>')
# les outils, à droite
TX, TW = 628, 192
o.append(f'<text x="{TX + TW / 2}" y="76" font-size="11" fill="{GRIS}" text-anchor="middle" font-weight="700">LES OUTILS</text>')
outils = [("recherche Web", ""), ("exécution de code", ""), ("documents et fichiers", ""), ("courriel, agenda…", ""), ("mémoire", "des notes d'une session à l'autre")]
for k, (l1, l2) in enumerate(outils):
    boite(TX, 88 + k * 50, TW, 40, l1, l2, coul=BRUN, taille=12 if not l2 else 12, gras=False)
# agir → outil, résultat → observer
o.append(f'<line x1="{A[0] + 36}" y1="{A[1]}" x2="{TX - 6}" y2="{A[1]}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')
o.append(f'<text x="{(A[0] + 36 + AX + AW) / 2}" y="{A[1] - 8}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">appel</text>')
o.append(f'<line x1="{TX - 6}" y1="{O[1]}" x2="{O[0] + 44}" y2="{O[1]}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')
o.append(f'<text x="{(O[0] + 44 + AX + AW) / 2}" y="{O[1] - 8}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">résultat</text>')
o.append(f'<line x1="{TX + TW / 2}" y1="{O[1] - 52}" x2="{TX + TW / 2}" y2="{O[1] - 52}" stroke="none"/>')
o.append("</svg>")
(OUT / "agent.svg").write_text("\n".join(o) + "\n")
print("agent.svg écrit")
