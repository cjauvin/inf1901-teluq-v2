# INF1901 v2 — consignes pour tout travail sur le contenu

- Lire et appliquer **GUIDE-STYLE.md** avant d'écrire ou de retoucher la moindre
  prose : registre neutre, et **tout renvoi à une autre partie du cours porte un
  lien** (section « Renvois : toujours un lien »).
- Après toute écriture de prose : `uv run scripts/espaces_insecables.py <fichiers>`.
- Après tout ajout ou changement de lien : `uv run scripts/verifier_liens.py`
  (serveur local :1313 en marche) doit donner 0 lien cassé.
- Pour une réécriture de style : `uv run scripts/verifier_invariants.py <fichiers>`
  (titres, liens, shortcodes, code, formules inchangés).
