"""Vérifie qu'une réécriture de style n'a touché à rien de structurel.

Compare chaque fichier donné à sa version dans git (HEAD par défaut) :
front matter, titres, liens (cibles), shortcodes, images, blocs de code,
formules et commentaires HTML doivent être identiques.

    uv run scripts/verifier_invariants.py content/docs/module2/60-classer.md [...]
"""
import re
import subprocess
import sys


def extraire(s):
    fm, corps = re.match(r"(---.*?---)(.*)", s, re.S).groups()
    code = re.findall(r"```.*?```", corps, re.S)
    sans_code = re.sub(r"```.*?```", "", corps, flags=re.S)
    return {
        "front matter": [fm],
        "titres": re.findall(r"^#{1,6} .*$", sans_code, re.M),
        "cibles de liens": sorted(re.findall(r"\]\(([^)\s]+)", sans_code)),
        "href html": sorted(re.findall(r'href="([^"]+)"', sans_code)),
        "shortcodes": [re.sub(r'"[^"]*"$', "", x) if x.startswith("{{% details") else x
                       for x in re.findall(r"\{\{[<%]\s*/?\s*(?:image|applet|youtube|hint|details|youtube-playlist)\b[^}]*[>%]\}\}", sans_code)],
        "blocs de code": code,
        "formules": re.findall(r"\$\$.*?\$\$|\\\\\[.*?\\\\\]|\\\\\(.*?\\\\\)", sans_code, re.S),
        "commentaires html": re.findall(r"<!--.*?-->", sans_code, re.S),
    }


def normaliser_details(liste):
    # le titre d'un details et le texte (alt, title) d'une image peuvent être neutralisés
    liste = [re.sub(r'\{\{% details ".*?"', '{{% details "…"', x) for x in liste]
    return [re.sub(r'\s(alt|title)="[^"]*"', "", x) for x in liste]


ok = True
ref = "HEAD"
for chemin in sys.argv[1:]:
    avant = subprocess.run(["git", "show", f"{ref}:{chemin}"], capture_output=True, text=True).stdout
    apres = open(chemin, encoding="utf-8").read()
    a, b = extraire(avant), extraire(apres)
    a["shortcodes"], b["shortcodes"] = normaliser_details(a["shortcodes"]), normaliser_details(b["shortcodes"])
    for cle in a:
        if a[cle] != b[cle]:
            ok = False
            print(f"✗ {chemin} : {cle} différents")
            for x in a[cle]:
                if x not in b[cle]:
                    print("   - avant seulement :", x[:160])
            for x in b[cle]:
                if x not in a[cle]:
                    print("   + après seulement :", x[:160])
    if ok:
        print(f"✓ {chemin}")
sys.exit(0 if ok else 1)
