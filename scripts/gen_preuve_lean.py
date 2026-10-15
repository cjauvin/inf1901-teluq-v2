"""Module 4, « Démontrer » : une preuve vérifiée par une machine. À gauche, un petit théorème écrit en Lean 4 (la somme de
deux nombres pairs est paire), dont chaque étape est vérifiée. À droite, la boucle : un modèle de langage propose une preuve,
Lean l'accepte ou la refuse avec un message d'erreur ; l'acceptation sert de récompense à l'entraînement, et le message
d'erreur aide le modèle à corriger."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module4"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
TERM, TERM_TXT, VERT = "#1f2421", "#e5e7e0", "#8fd3a0"
MONO = "ui-monospace, Menlo, Consolas, monospace"
W, H = 840, 430
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Une preuve vérifiée par une machine</title>",
     "<desc>À gauche, un énoncé en français, « la somme de deux nombres pairs est paire », et sa traduction en Lean, un langage "
     "de preuve : pour tous entiers naturels a et b, s'il existe x tel que a égale 2 fois x, et y tel que b égale 2 fois y, alors "
     "il existe z tel que a plus b égale 2 fois z. Suivent trois étapes de preuve : extraire x, extraire y, puis proposer z égal à "
     "x plus y, le calcul étant fait par une procédure automatique. Lean répond : aucune erreur, la preuve est acceptée. À "
     "droite, une boucle : le modèle de langage propose une preuve ; Lean la vérifie ; si elle est acceptée, c'est une récompense "
     "pour l'entraînement ; si elle est refusée, le message d'erreur revient au modèle, qui corrige. En bas : le vérificateur est "
     "un petit programme écrit par des humains, auquel on peut se fier ; il n'y a rien à croire sur parole.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker>'
     f'<marker id="pt" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{TEAL}"/></marker>'
     f'<marker id="pr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{ROUGE}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Une preuve vérifiée par une machine</text>']
# ── à gauche : l'énoncé et la preuve ──
o.append(f'<rect x="20" y="50" width="452" height="320" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
o.append(f'<text x="36" y="74" font-size="12.5" fill="{BRUN}" font-weight="700">L\'énoncé</text>')
o.append(f'<text x="36" y="94" font-size="12.5" fill="{ENCRE}" font-style="italic">«{NB}La somme de deux nombres pairs est paire.{NB}»</text>')
o.append(f'<text x="36" y="122" font-size="12.5" fill="{BRUN}" font-weight="700">La même chose en Lean, avec sa preuve</text>')
CODE = [("theorem somme_pairs (a b : Nat)", TERM_TXT),
        ("    (ha : ∃ x, a = 2 * x) (hb : ∃ y, b = 2 * y) :", TERM_TXT),
        ("    ∃ z, a + b = 2 * z := by", TERM_TXT),
        ("  obtain ⟨x, hx⟩ := ha", VERT),
        ("  obtain ⟨y, hy⟩ := hb", VERT),
        ("  exact ⟨x + y, by omega⟩", VERT)]
o.append(f'<rect x="32" y="134" width="428" height="{len(CODE) * 19 + 16}" rx="6" fill="{TERM}"/>')
for k, (l, c) in enumerate(CODE):
    o.append(f'<text x="44" y="{156 + k * 19}" font-size="11.5" fill="{c}" font-family="{MONO}" xml:space="preserve">{l}</text>')
yr = 156 + len(CODE) * 19 + 26
o.append(f'<rect x="32" y="{yr - 2}" width="428" height="30" rx="6" fill="#dcebe8" stroke="{TEAL}"/>')
o.append(f'<text x="46" y="{yr + 18}" font-size="12" fill="{TEAL}" font-weight="700">Lean{NB}: aucune erreur. La preuve est acceptée.</text>')
for k, l in enumerate(["En vert, les étapes de la preuve : Lean vérifie chacune d'elles,",
                       "et refuserait la moindre étape fausse ou incomplète."]):
    o.append(f'<text x="36" y="{yr + 52 + k * 16}" font-size="11" fill="{ENCRE_PALE}">{l}</text>')
# ── à droite : la boucle ──
o.append(f'<rect x="488" y="50" width="332" height="320" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
o.append(f'<text x="654" y="74" font-size="12.5" fill="{BRUN}" text-anchor="middle" font-weight="700">La boucle</text>')


def boite(cx, cy, w, h, l1, l2, coul, fond=FOND):
    o.append(f'<rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" rx="9" fill="{fond}" stroke="{coul}" stroke-width="1.8"/>')
    o.append(f'<text x="{cx}" y="{cy - 3}" font-size="12" fill="{ENCRE}" text-anchor="middle" font-weight="700">{l1}</text>')
    o.append(f'<text x="{cx}" y="{cy + 13}" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">{l2}</text>')


boite(632, 116, 196, 44, "le modèle de langage", "propose une preuve, en Lean", TEAL)
boite(632, 206, 196, 44, "Lean", "vérifie chaque étape", BLEU)
o.append(f'<line x1="632" y1="140" x2="632" y2="180" stroke="{GRIS}" stroke-width="1.8" marker-end="url(#p)"/>')
boite(566, 298, 136, 52, "acceptée", "une récompense exacte", TEAL, "#dcebe8")
boite(712, 298, 140, 52, "refusée", "avec un message d'erreur", ROUGE, "#f6dcd6")
o.append(f'<line x1="606" y1="230" x2="586" y2="268" stroke="{TEAL}" stroke-width="1.8" marker-end="url(#pt)"/>')
o.append(f'<line x1="658" y1="230" x2="690" y2="268" stroke="{ROUGE}" stroke-width="1.8" marker-end="url(#pr)"/>')
o.append(f'<path d="M{712 + 70} 290 C 806 210 800 116 {632 + 104} 116" fill="none" stroke="{ROUGE}" stroke-width="1.6" stroke-dasharray="5 4" marker-end="url(#pr)"/>')
o.append(f'<text x="790" y="200" font-size="10.5" fill="{ROUGE}" text-anchor="end" stroke="{PANNEAU}" stroke-width="4" paint-order="stroke">le modèle</text>')
o.append(f'<text x="790" y="213" font-size="10.5" fill="{ROUGE}" text-anchor="end" stroke="{PANNEAU}" stroke-width="4" paint-order="stroke">corrige</text>')
o.append(f'<text x="566" y="342" font-size="10.5" fill="{TEAL}" text-anchor="middle">sert à l\'entraînement</text>')
o.append(f'<text x="566" y="356" font-size="10.5" fill="{TEAL}" text-anchor="middle">par renforcement</text>')
o.append(f'<text x="{W / 2}" y="{H - 34}" font-size="12" fill="{ENCRE}" text-anchor="middle">Le vérificateur est un petit programme, écrit et éprouvé par des humains{NB}:</text>')
o.append(f'<text x="{W / 2}" y="{H - 16}" font-size="12" fill="{ENCRE}" text-anchor="middle">une preuve acceptée n\'a pas à être crue sur parole, même si c\'est une machine qui l\'a trouvée.</text>')
o.append("</svg>")
(OUT / "preuve-lean.svg").write_text("\n".join(o) + "\n")
print("preuve-lean.svg écrit")
