# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""Module 4, « Des mots aux nombres » : les plongements de l'applet `plongements.html`.

Source : les vecteurs fastText français entraînés sur Common Crawl (cc.fr.300.vec, Facebook/Meta,
licence CC BY-SA 3.0 ; https://fasttext.cc/docs/en/crawl-vectors.html). Les mots y sont rangés du
plus fréquent au plus rare ; seuls les 60 000 premiers sont lus, dans
~/.cache/inf1901/fasttext/cc.fr.300.60k.vec, obtenu ainsi :

    curl -sL https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.fr.300.vec.gz | gunzip -c | head -n 60001

On garde les 20 000 premiers mots alphabétiques, moins les variantes en majuscule d'un mot plus fréquent en
minuscules (« Chat », mais pas « Paris »), puis on réduit les vecteurs à 200 dimensions par analyse en
composantes principales et on les code sur un octet chacun.

    uv run scripts/gen_plongements.py
"""
import base64, json, os, re
from pathlib import Path
import numpy as np

SOURCE = Path.home() / ".cache" / "inf1901" / "fasttext" / "cc.fr.300.60k.vec"
SORTIE = Path(__file__).resolve().parent.parent / "static" / "html" / "applets" / "data" / "plongements.json"

DIMS = int(os.environ.get("DIMS", 200))                 # 200 : presque aussi fidèle que 300, en un tiers de moins
NMOTS = int(os.environ.get("NMOTS", 20000))
MOT = re.compile(r"[a-zàâäçéèêëîïôöùûüÿœæ][a-zàâäçéèêëîïôöùûüÿœæ\-]*|[A-ZÀÉÈÎ][a-zàâäçéèêëîïôöùûüÿœæ\-]+")

mots, vecs, rang = [], [], {}
with open(SOURCE, encoding="utf-8") as f:
    next(f)
    for l in f:
        p = l.rstrip().split(" ")
        if MOT.fullmatch(p[0]) and len(p[0]) >= 2:
            rang[p[0]] = len(mots)
            mots.append(p[0]); vecs.append(np.array(p[1:], np.float32))
        if len(mots) >= NMOTS:
            break
garde = [i for i, m in enumerate(mots) if not (m[0].isupper() and rang.get(m.lower(), 10 ** 9) < i)]
mots = [mots[i] for i in garde]
X = np.stack([vecs[i] for i in garde])
X -= X.mean(0)
_, _, Wt = np.linalg.svd(X, full_matrices=False)
Y = X @ Wt[:DIMS].T
Y /= np.linalg.norm(Y, axis=1, keepdims=True)
echelle = float(np.abs(Y).max()) / 127
Q = np.round(Y / echelle).astype(np.int8)
SORTIE.write_text(json.dumps({"dims": DIMS, "echelle": echelle, "mots": mots,
                              "v": base64.b64encode(Q.tobytes()).decode()}, ensure_ascii=False, separators=(",", ":")))
print(len(mots), "mots ;", SORTIE.name, SORTIE.stat().st_size // 1024, "Ko")

# contrôle, avec les vecteurs tels que l'applet les lira
V = Q.astype(np.float32); V /= np.linalg.norm(V, axis=1, keepdims=True)
idx = {m: i for i, m in enumerate(mots)}
for a, b, c in [("homme", "roi", "femme"), ("France", "Paris", "Italie"), ("homme", "médecin", "femme")]:
    v = V[idx[b]] - V[idx[a]] + V[idx[c]]
    s = V @ (v / np.linalg.norm(v))
    print(f"{a} : {b} :: {c} : ?", [mots[i] for i in np.argsort(-s) if mots[i] not in (a, b, c)][:5])
