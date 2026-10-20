# /// script
# requires-python = ">=3.10"
# ///
"""Module 5, « Penser, est-ce calculer ? » : l'argument de Lucas (1961) tiré du théorème de Gödel. À gauche, ses trois
étapes : une machine équivaut à un système formel F, F a sa phrase de Gödel G, qu'il ne peut pas démontrer, et un
humain voit que G est vraie. À droite, la régression : ajouter G à la machine donne un nouveau système, qui a sa propre
phrase de Gödel, et ainsi de suite. En bas, l'hypothèse cachée que visent les objections : la cohérence."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module5" / "argument-de-lucas.svg"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB = " "
PRIME, SECONDE = "′", "″"

W, H = 860, 420
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>L'argument de Lucas</title>",
     "<desc>Deux panneaux. À gauche, l'argument de John Lucas (1961) en trois étapes : une machine qui fait des "
     "mathématiques équivaut à un système formel F ; ce système a sa phrase de Gödel G, « Je ne suis pas démontrable "
     "dans F », qu'il ne peut pas démontrer ; un humain, lui, voit que G est vraie. À droite, la régression : si l'on "
     "ajoute G à la machine, on obtient un nouveau système, F + G, qui a sa propre phrase de Gödel G′, puis F + G + G′, "
     "qui a la sienne, G″, et ainsi de suite ; pour Lucas, l'humain garde toujours une longueur d'avance. En bas, "
     "l'hypothèse cachée : pour voir que G est vraie, il faut savoir que F est cohérent.</desc>",
     f'<defs><marker id="p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{GRIS}"/></marker>'
     f'<marker id="t" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{TEAL}"/></marker>'
     f'<marker id="r" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto">'
     f'<path d="M0 0 L10 5 L0 10 z" fill="{ROUGE}"/></marker></defs>',
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="32" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">L\'argument de Lucas (1961)</text>']


def engrenage(cx, cy, r, coul):
    pts = []
    import math
    for k in range(16):
        a = k * math.pi / 8
        rr = r if k % 2 == 0 else r * 0.78
        for da in (-0.13, 0.13):
            pts.append(f"{cx + rr * math.cos(a + da):.1f},{cy + rr * math.sin(a + da):.1f}")
    o.append(f'<polygon points="{" ".join(pts)}" fill="{PANNEAU}" stroke="{coul}" stroke-width="1.6" stroke-linejoin="round"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r * 0.3:.1f}" fill="{FOND}" stroke="{coul}" stroke-width="1.4"/>')


def carte(x, y, w, l1, l2=None, coul=BRUN, taille=11.5):
    h = 46 if l2 else 30
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="#ffffff" stroke="{coul}" stroke-width="1.5"/>')
    if l2:
        o.append(f'<text x="{x + w / 2}" y="{y + 19}" font-size="{taille}" fill="{ENCRE}" text-anchor="middle" font-style="italic">{l1}</text>')
        o.append(f'<text x="{x + w / 2}" y="{y + 35}" font-size="{taille}" fill="{ENCRE}" text-anchor="middle" font-style="italic">{l2}</text>')
    else:
        o.append(f'<text x="{x + w / 2}" y="{y + 20}" font-size="{taille}" fill="{ENCRE}" text-anchor="middle" font-weight="700">{l1}</text>')


def pastille(x, y, n, coul):
    o.append(f'<circle cx="{x}" cy="{y}" r="10" fill="{coul}"/>')
    o.append(f'<text x="{x}" y="{y + 4}" font-size="11" fill="#ffffff" text-anchor="middle" font-weight="700">{n}</text>')


# ── panneau gauche : les trois étapes ──
o.append(f'<rect x="20" y="50" width="420" height="292" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
o.append(f'<text x="230" y="76" font-size="12.5" fill="{BRUN}" text-anchor="middle" font-weight="700">Trois étapes</text>')
# 1. la machine
o.append(f'<rect x="44" y="100" width="140" height="104" rx="8" fill="{FOND}" stroke="{BLEU}" stroke-width="2"/>')
engrenage(114, 140, 22, BLEU)
o.append(f'<text x="114" y="182" font-size="11.5" fill="{ENCRE}" text-anchor="middle" font-weight="700">une machine</text>')
o.append(f'<text x="114" y="196" font-size="10.5" fill="{ENCRE_PALE}" text-anchor="middle">= un système formel F</text>')
pastille(44, 100, 1, BLEU)
# 2. la phrase de Gödel
carte(262, 114, 156, "« Je ne suis pas", f"démontrable dans F{NB}»")
o.append(f'<text x="340" y="99" font-size="10.5" fill="{BRUN}" text-anchor="middle" font-weight="700">sa phrase de Gödel G</text>')
pastille(262, 114, 2, BRUN)
o.append(f'<line x1="190" y1="137" x2="254" y2="137" stroke="{ROUGE}" stroke-width="1.8" stroke-dasharray="5 4" marker-end="url(#r)"/>')
o.append(f'<text x="222" y="158" font-size="16" fill="{ROUGE}" text-anchor="middle" font-weight="700">✗</text>')
o.append(f'<text x="222" y="174" font-size="10" fill="{ROUGE}" text-anchor="middle">ne peut pas</text>')
o.append(f'<text x="222" y="186" font-size="10" fill="{ROUGE}" text-anchor="middle">la démontrer</text>')
# 3. l'humain
HX, HY = 340, 262
o.append(f'<circle cx="{HX}" cy="{HY}" r="11" fill="{PANNEAU}" stroke="{ENCRE}" stroke-width="2"/>')
o.append(f'<path d="M{HX - 18} {HY + 40} Q{HX - 18} {HY + 14} {HX} {HY + 14} Q{HX + 18} {HY + 14} {HX + 18} {HY + 40}" fill="{PANNEAU}" stroke="{ENCRE}" stroke-width="2"/>')
pastille(HX - 34, HY - 4, 3, TEAL)
o.append(f'<line x1="{HX}" y1="{HY - 18}" x2="{HX}" y2="168" stroke="{TEAL}" stroke-width="2" marker-end="url(#t)"/>')
o.append(f'<text x="{HX + 12}" y="210" font-size="10.5" fill="{TEAL}" font-weight="700">un humain voit</text>')
o.append(f'<text x="{HX + 12}" y="224" font-size="10.5" fill="{TEAL}" font-weight="700">que G est vraie</text>')
o.append(f'<text x="114" y="262" font-size="11" fill="{ENCRE}" text-anchor="middle">Donc l\'esprit humain</text>')
o.append(f'<text x="114" y="277" font-size="11" fill="{ENCRE}" text-anchor="middle">ferait toujours une chose</text>')
o.append(f'<text x="114" y="292" font-size="11" fill="{ENCRE}" text-anchor="middle">qu\'aucune machine</text>')
o.append(f'<text x="114" y="307" font-size="11" fill="{ENCRE}" text-anchor="middle">donnée ne peut faire.</text>')

# ── panneau droit : la régression ──
o.append(f'<rect x="456" y="50" width="384" height="292" rx="10" fill="{PANNEAU}" stroke="{BORD}"/>')
o.append(f'<text x="648" y="76" font-size="12.5" fill="{BLEU}" text-anchor="middle" font-weight="700">Ajouter G à la machine{NB}?</text>')
ETAPES = [("F", "G"), ("F + G", f"G{PRIME}"), (f"F + G + G{PRIME}", f"G{SECONDE}")]
LW = [64, 84, 104]
x = 472
centres = []
for k, ((sys_, g), w) in enumerate(zip(ETAPES, LW)):
    y = 110 + k * 62
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="5" fill="{FOND}" stroke="{BLEU}" stroke-width="1.6"/>')
    o.append(f'<text x="{x + w / 2}" y="{y + 20}" font-size="11.5" fill="{ENCRE}" text-anchor="middle" font-weight="700">{sys_}</text>')
    gx = x + w + 46
    o.append(f'<line x1="{x + w + 6}" y1="{y + 15}" x2="{gx - 6}" y2="{y + 15}" stroke="{ROUGE}" stroke-width="1.6" stroke-dasharray="4 3" marker-end="url(#r)"/>')
    o.append(f'<rect x="{gx}" y="{y}" width="40" height="30" rx="4" fill="#ffffff" stroke="{BRUN}" stroke-width="1.5"/>')
    o.append(f'<text x="{gx + 20}" y="{y + 20}" font-size="12" fill="{ENCRE}" text-anchor="middle" font-weight="700" font-style="italic">{g}</text>')
    o.append(f'<text x="{gx + 52}" y="{y + 19}" font-size="10" fill="{ROUGE}">indémontrable dans {sys_}</text>')
    if k < 2:
        o.append(f'<path d="M{gx + 20} {y + 34} Q{gx + 20} {y + 46} {x + w / 2 + 10} {y + 46} L{x + w / 2 + 10} {y + 56}" fill="none" stroke="{GRIS}" stroke-width="1.4" marker-end="url(#p)"/>')
        o.append(f'<text x="{x + w / 2 + 16}" y="{y + 56}" font-size="9.5" fill="{GRIS}">on l\'ajoute</text>')
o.append(f'<text x="520" y="{110 + 3 * 62 - 6}" font-size="18" fill="{GRIS}" text-anchor="middle">…</text>')
o.append(f'<text x="648" y="314" font-size="11" fill="{ENCRE}" text-anchor="middle">Chaque nouveau système a sa propre phrase de Gödel.</text>')
o.append(f'<text x="648" y="330" font-size="11" fill="{ENCRE}" text-anchor="middle">Pour Lucas, l\'humain garde toujours une longueur d\'avance.</text>')

# ── l'hypothèse cachée ──
o.append(f'<text x="{W / 2}" y="374" font-size="12" fill="{ROUGE}" text-anchor="middle" font-weight="700">L\'hypothèse cachée{NB}: pour voir que G est vraie, il faut savoir que F est cohérent.</text>')
o.append(f'<text x="{W / 2}" y="396" font-size="11.5" fill="{ENCRE}" text-anchor="middle">Savons-nous que notre propre raisonnement l\'est{NB}?</text>')
o.append("</svg>")
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(o) + "\n")
print(OUT.name, "écrit")
