"""Vérifie les liens internes du cours : fichier cible existant et ancre présente.

Les ancres sont lues dans les pages servies par le serveur local (port 1313),
qui doit tourner. Sans argument, vérifie tous les .md des modules 1 et 2.

    uv run scripts/verifier_liens.py [fichiers…]
"""
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
BASE = "http://localhost:1313/inf1901-teluq/"
cache = {}


def url_de(cible: Path) -> str:
    """URL servie d'un fichier de contenu (slug du front matter, sinon nom de fichier)."""
    rel = cible.relative_to(RACINE / "content")
    if cible.name == "_index.md":
        return BASE + "/".join(rel.parts[:-1]) + "/"
    fm = cible.read_text(encoding="utf-8").split("---")[1]
    m = re.search(r"^slug:\s*(.+)$", fm, re.M)
    nom = m.group(1).strip().strip('"') if m else cible.stem
    return BASE + "/".join(rel.parts[:-1]) + "/" + urllib.parse.quote(nom) + "/"


def ids(url: str) -> set:
    if url not in cache:
        try:
            html = urllib.request.urlopen(url).read().decode("utf-8")
        except Exception:
            html = ""
        cache[url] = {urllib.parse.unquote(i) for i in re.findall(r'\sid="([^"]+)"', html)}
    return cache[url]


def resoudre(chemin: str):
    p = RACINE / "content" / chemin.strip("/")
    for c in (p.with_suffix(".md"), p / "_index.md"):
        if c.exists():
            return c
    # lien par slug plutôt que par nom de fichier
    for f in (RACINE / "content" / chemin.strip("/")).parent.glob("*.md"):
        if re.search(rf"^slug:\s*{re.escape(p.name)}\s*$", f.read_text(encoding="utf-8"), re.M):
            return f
    return None


fichiers = [Path(a) for a in sys.argv[1:]] or sorted((RACINE / "content/docs").glob("module[12]/*.md"))
erreurs = 0
for f in fichiers:
    source = Path(f).resolve()
    texte = source.read_text(encoding="utf-8")
    for cible in re.findall(r"\]\((docs/[^)\s]+|#[^)\s]+)\)", texte):
        chemin, _, ancre = cible.partition("#")
        fichier = resoudre(chemin.rstrip("/")) if chemin else source
        if fichier is None:
            print(f"✗ {source.relative_to(RACINE)} : page introuvable → {cible}")
            erreurs += 1
            continue
        if ancre and urllib.parse.unquote(ancre) not in ids(url_de(fichier)):
            print(f"✗ {source.relative_to(RACINE)} : ancre absente → {cible}")
            erreurs += 1
print(f"{erreurs} lien(s) cassé(s)")
sys.exit(1 if erreurs else 0)
