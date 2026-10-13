"""Module 4, « Le défi ARC » : extrait des dépôts officiels les tâches retenues pour l'applet arc.html, de la plus facile à la
plus difficile. Les tâches sont sous licence Apache 2.0 (ARC-AGI : François Chollet ; ARC-AGI-2 : ARC Prize Foundation).

    git clone https://github.com/fchollet/ARC-AGI.git /tmp/ARC-AGI
    git clone https://github.com/arcprize/ARC-AGI-2.git /tmp/ARC-AGI-2
    uv run scripts/gen_arc_taches.py /tmp/ARC-AGI /tmp/ARC-AGI-2
"""
import json
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "html" / "applets" / "data" / "arc-taches.json"
ARC1 = ["25ff71a9", "3c9b0459", "6f8cd79b", "a416b8f3", "4258a5f9", "d037b0a7",
        "3aa6fb7a", "a699fb00", "007bbfb7", "05f2a901", "39a8645d", "00d62c1b"]
ARC2 = ["dbff022c"]

arc1, arc2 = Path(sys.argv[1]), Path(sys.argv[2])
taches = []
for version, dossier, ids in (("ARC-AGI-1", arc1 / "data" / "training", ARC1), ("ARC-AGI-2", arc2 / "data" / "evaluation", ARC2)):
    for i in ids:
        t = json.loads((dossier / f"{i}.json").read_text())
        taches.append({"id": i, "version": version, "train": t["train"], "test": t["test"]})
OUT.write_text(json.dumps(taches, separators=(",", ":")) + "\n")
print(OUT.name, "écrit :", len(taches), "tâches,", OUT.stat().st_size // 1024, "Ko")
