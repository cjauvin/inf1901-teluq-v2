"""Module 4, « Des outils et des agents » : comment la requête système est combinée aux messages de l'utilisateur. L'application
assemble un seul texte selon un gabarit de conversation, délimité par des jetons spéciaux ; le texte s'arrête à l'ouverture de
la réplique de l'assistant, et le modèle le continue jusqu'à la marque de fin. Marques schématiques."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
W, H = 840, 530
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Le gabarit de conversation</title>",
     "<desc>En haut, trois sources : la requête système, rédigée par l'entreprise, que l'utilisateur ne voit pas, avec la "
     "description des outils ; les échanges précédents ; le nouveau message de l'utilisateur. L'application les assemble en un "
     "seul texte, selon un gabarit de conversation. Ce texte est dessiné au milieu : chaque partie commence par une marque "
     "spéciale, début système, début utilisateur, début assistant, et se termine par une marque de fin. Le texte s'arrête après "
     "la marque qui ouvre la réplique de l'assistant. Le modèle, à droite, le continue jeton après jeton, « Oui, nous l'avons en "
     "format poche », jusqu'à produire la marque de fin, qui rend la main à l'utilisateur. En bas, la priorité apprise pendant le "
     "post-entraînement : la requête système d'abord, puis l'utilisateur, puis le contenu des documents et des outils.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Un seul texte{NB}: la requête système, puis la conversation</text>']

# les trois sources
SOURCES = [(30, "requête système", ["rédigée par l'entreprise,", "invisible pour l'utilisateur ;", "rôle, ton, refus, outils"], BRUN),
           (300, "échanges précédents", ["les questions et les réponses", "depuis le début", "de la conversation"], GRIS),
           (570, "nouveau message", [f"«{NB}Avez-vous Kamouraska,", f"d'Anne Hébert{NB}?{NB}»", ""], BLEU)]
for x, titre, lignes, c in SOURCES:
    o.append(f'<rect x="{x}" y="52" width="240" height="86" rx="8" fill="{PANNEAU}" stroke="{c}" stroke-width="1.8"/>')
    o.append(f'<text x="{x + 120}" y="73" font-size="12.5" fill="{c}" text-anchor="middle" font-weight="700">{titre}</text>')
    for k, l in enumerate(lignes):
        o.append(f'<text x="{x + 120}" y="{92 + k * 15}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle"'
                 + (' font-style="italic"' if x == 570 else "") + f'>{l}</text>')
    o.append(f'<line x1="{x + 120}" y1="140" x2="{x + 120}" y2="156" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')
o.append(f'<text x="{W / 2}" y="176" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle" stroke="{FOND}" stroke-width="5" paint-order="stroke">l\'application assemble un seul texte, selon un gabarit de conversation</text>')

# le texte assemblé
TX, TY, TW, TH = 30, 188, 560, 262
o.append(f'<rect x="{TX}" y="{TY}" width="{TW}" height="{TH}" rx="10" fill="{PANNEAU}" stroke="{BORD}" stroke-width="1.4"/>')


def marque(x, y, texte, c):
    w = 9 + 6.4 * len(texte)
    o.append(f'<rect x="{x}" y="{y - 13}" width="{w}" height="18" rx="4" fill="{c}"/>')
    o.append(f'<text x="{x + w / 2}" y="{y}" font-size="10.5" fill="{PANNEAU}" text-anchor="middle" font-family="ui-monospace, Menlo, monospace" font-weight="700">{texte}</text>')
    return x + w + 6


def ligne(x, y, texte, c=ENCRE, italique=False):
    o.append(f'<text x="{x}" y="{y}" font-size="11.5" fill="{c}" font-family="ui-monospace, Menlo, monospace"'
             + (' font-style="italic"' if italique else "") + f'>{texte}</text>')


x0, y = TX + 14, TY + 24
marque(x0, y, "début système", BRUN)
ligne(x0 + 10, y + 19, "Tu es l'assistant de la librairie Le Signet.")
ligne(x0 + 10, y + 35, "Ne donne jamais d'avis médical.")
ligne(x0 + 10, y + 51, "Outil : chercher_catalogue(titre)")
marque(x0, y + 70, "fin", BRUN)
y += 96
o.append(f'<text x="{x0}" y="{y}" font-size="11" fill="{GRIS}" font-style="italic">…{NB}les échanges précédents, avec les mêmes marques{NB}…</text>')
y += 28
marque(x0, y, "début utilisateur", BLEU)
ligne(x0 + 10, y + 19, f"Avez-vous Kamouraska, d'Anne Hébert{NB}?")
marque(x0, y + 38, "fin", BLEU)
y += 66
xa = marque(x0, y, "début assistant", TEAL)
o.append(f'<text x="{xa + 2}" y="{y}" font-size="11.5" fill="{ROUGE}" font-family="ui-monospace, Menlo, monospace" font-weight="700">Oui, nous l\'avons en format poche.</text>')
marque(xa + 268, y, "fin", ROUGE)
o.append(f'<text x="{x0}" y="{y + 26}" font-size="10.5" fill="{ENCRE_PALE}">le texte reçu s\'arrête après «{NB}début assistant{NB}»{NB}; en rouge, ce que le modèle écrit</text>')

# le modèle
MX, MY = 630, 290
o.append(f'<rect x="{MX}" y="{MY}" width="180" height="66" rx="10" fill="{FOND}" stroke="{TEAL}" stroke-width="2"/>')
o.append(f'<text x="{MX + 90}" y="{MY + 28}" font-size="13" fill="{ENCRE}" text-anchor="middle" font-weight="700">le modèle</text>')
o.append(f'<text x="{MX + 90}" y="{MY + 46}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">prédit la suite, jeton</text>')
o.append(f'<text x="{MX + 90}" y="{MY + 60}" font-size="11" fill="{ENCRE_PALE}" text-anchor="middle">après jeton</text>')
o.append(f'<line x1="{TX + TW + 4}" y1="{MY + 20}" x2="{MX - 6}" y2="{MY + 20}" stroke="{GRIS}" stroke-width="1.6" marker-end="url(#p)"/>')
o.append(f'<path d="M{MX + 40} {MY + 68} C {MX + 40} {MY + 130} {TX + TW + 60} {TY + TH - 52} {TX + TW - 6} {TY + TH - 52}" fill="none" stroke="{ROUGE}" stroke-width="1.6" marker-end="url(#p)"/>')
o.append(f'<text x="{W - 24}" y="{MY + 106}" font-size="11" fill="{ROUGE}" text-anchor="end">jusqu\'à la marque de fin,</text>')
o.append(f'<text x="{W - 24}" y="{MY + 120}" font-size="11" fill="{ROUGE}" text-anchor="end">qui rend la main</text>')
o.append(f'<text x="{W - 24}" y="{MY + 134}" font-size="11" fill="{ROUGE}" text-anchor="end">à l\'utilisateur</text>')

# la priorité apprise
PY = TY + TH + 30
o.append(f'<text x="{W / 2}" y="{PY}" font-size="12" fill="{ENCRE}" text-anchor="middle">priorité apprise au post-entraînement{NB}: '
         f'<tspan fill="{BRUN}" font-weight="700">système</tspan>  ›  <tspan fill="{BLEU}" font-weight="700">utilisateur</tspan>  ›  '
         f'<tspan fill="{GRIS}" font-weight="700">documents et outils</tspan></text>')
o.append(f'<text x="{W / 2}" y="{PY + 22}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">les marques sont des jetons spéciaux, que l\'utilisateur ne peut pas taper{NB}; leur forme exacte varie d\'un modèle à l\'autre</text>')
o.append("</svg>")
(OUT / "gabarit-conversation.svg").write_text("\n".join(o) + "\n")
print("gabarit-conversation.svg écrit")
