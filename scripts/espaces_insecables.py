"""Espaces insécables de la typographie française, dans tous les .md du cours.

  * espace insécable (U+00A0) avant « : » ;
  * espace fine insécable (U+202F) avant « ; », « ! », « ? » et « » », après « « ».

Sont laissés intacts : les blocs de code (``` ou ~~~), le code en ligne (`…`),
les formules ($…$ et $$…$$), les lignes d'alignement des tableaux, et les
séquences déjà insécables. Le script est idempotent.

Usage :
    uv run scripts/espaces_insecables.py            # corrige en place
    uv run scripts/espaces_insecables.py --verifier # liste ce qui reste à corriger
"""
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent / "content"
NBSP, FINE = " ", " "

# segments à ne pas toucher : code en ligne, math affichée ou en ligne (un « $ »
# n'ouvre une formule que s'il est collé au contenu, ce qui exclut les montants
# comme « 500 000 $ »)
PROTEGE = r"(`+)[^`]*?\1|\$\$.*?\$\$|(?<!\\)\$(?=\S)[^$\n]*?(?<=\S)\$"
MOTIF = re.compile(PROTEGE + r"|(?<=\S) +(:)|(?<=\S) +([;!?»])|(«) (?=\S)")
LIGNE_ALIGNEMENT = re.compile(r"^\s*\|?\s*:?-{2,}")


def remplacer(m):
    if m.group(2):
        return NBSP + ":"
    if m.group(3):
        return FINE + m.group(3)
    if m.group(4):
        return "«" + FINE
    return m.group(0)


def corriger_ligne(ligne):
    if LIGNE_ALIGNEMENT.match(ligne):
        return ligne
    return MOTIF.sub(remplacer, ligne)


def corriger_texte(texte):
    sortie, dans_code, cloture, dans_math = [], False, None, False
    for ligne in texte.split("\n"):
        barriere = re.match(r"^\s*(```|~~~)", ligne)
        if barriere and not dans_code:
            dans_code, cloture = True, barriere.group(1)
        elif barriere and dans_code and ligne.strip().startswith(cloture):
            dans_code = False
        elif not dans_code and not dans_math:
            ligne = corriger_ligne(ligne)
        if not dans_code and ligne.count("$$") % 2 == 1:
            dans_math = not dans_math  # bloc $$ … $$ sur plusieurs lignes
        sortie.append(ligne)
    return "\n".join(sortie)


if __name__ == "__main__":
    verifier = "--verifier" in sys.argv
    touches = 0
    # fichiers donnés en argument, sinon tout content/
    fichiers = [Path(a).resolve() for a in sys.argv[1:] if not a.startswith("--")] or sorted(RACINE.rglob("*.md"))
    for f in fichiers:
        avant = f.read_text(encoding="utf-8")
        apres = corriger_texte(avant)
        if apres != avant:
            touches += 1
            n = sum(1 for a, b in zip(avant.split("\n"), apres.split("\n")) if a != b)
            print(f"{'à corriger' if verifier else 'corrigé'} : {f.relative_to(RACINE.parent) if f.is_relative_to(RACINE.parent) else f} ({n} lignes)")
            if not verifier:
                f.write_text(apres, encoding="utf-8")
    print(f"{touches} fichier(s) {'à corriger' if verifier else 'corrigé(s)'}")
