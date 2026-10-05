"""Module 4, « Prédire le mot suivant » : le corpus de l'applet `ngrammes.html`.

Deux romans de Jules Verne, domaine public, Projet Gutenberg (scripts/data/ngrammes/) :
Le Tour du monde en quatre-vingts jours (ebook 46541) et Vingt mille lieues sous les mers (ebook 5097).
On garde le texte des chapitres, on le découpe en mots et en signes de ponctuation, et on l'écrit sous forme
de numéros (deux octets chacun, base64) avec la liste du vocabulaire. L'applet compte elle-même les n-grammes.

    uv run scripts/gen_ngrammes.py
"""
import base64, json, re
from collections import Counter
from pathlib import Path
import numpy as np

RACINE = Path(__file__).resolve().parent
SORTIE = RACINE.parent / "static" / "html" / "applets" / "data" / "ngrammes.json"
LIVRES = [("verne-46541.txt", "Le Tour du monde en quatre-vingts jours", "En l'année 1872", "\nFIN\n"),
          ("verne-5097.txt", "Vingt mille lieues sous les mers", "L'année 1866 fut", "FIN DE LA SECONDE PARTIE")]
MOT = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿŒœ]+(?:-[A-Za-zÀ-ÖØ-öø-ÿŒœ]+)*'?|[0-9]+|[.,;:!?]")

jetons = []
for f, _, debut, fin in LIVRES:                        # du premier mot du roman jusqu'à « FIN »
    t = (RACINE / "data" / "ngrammes" / f).read_text(encoding="utf-8")
    t = t[t.index(debut):t.index(fin)]
    garde = []
    for ligne in t.splitlines():
        l = ligne.strip()
        if not l or "[Illustration" in l or re.fullmatch(r"[IVXLC]+\.?", l) or (l.upper() == l and re.search(r"[A-Z]", l)):
            continue                                   # lignes vides, illustrations, numéros et titres en capitales
        garde.append(l)
    t = " ".join(garde).replace("’", "'").replace("_", "")
    jetons += MOT.findall(t)
compte = Counter(jetons)
vocab = [m for m, _ in compte.most_common()]
assert len(vocab) < 65536
num = {m: i for i, m in enumerate(vocab)}
ids = np.array([num[m] for m in jetons], np.uint16)
SORTIE.write_text(json.dumps({"livres": [t for _, t, _, _ in LIVRES], "vocab": vocab,
                              "texte": base64.b64encode(ids.tobytes()).decode()}, ensure_ascii=False, separators=(",", ":")))
print(len(jetons), "jetons,", len(vocab), "mots différents ;", SORTIE.name, SORTIE.stat().st_size // 1024, "Ko")
print(" ".join(jetons[:60]))
