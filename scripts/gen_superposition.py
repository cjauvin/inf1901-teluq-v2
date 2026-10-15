# /// script
# requires-python = ">=3.10,<3.13"
# dependencies = ["torch", "numpy"]
# ///
"""Module 4, « Regarder à l'intérieur » : le modèle jouet de la superposition (Elhage et coll., Anthropic, 2022), entraîné
d'avance pour l'applet superposition.html. Cinq caractéristiques (des « concepts ») doivent passer par un espace de deux
dimensions seulement : h = W x, puis x' = ReLU(Wᵀ h + b). Chaque caractéristique est absente avec une probabilité S (la
rareté), sinon tirée uniformément entre 0 et 1 ; leur importance décroît de 1 à 0,9⁴, comme dans l'article. Quand les caractéristiques sont fréquentes, le réseau n'en garde que deux,
à angle droit ; quand elles deviennent rares, il les range toutes les cinq, en pentagone, au prix d'un peu d'interférence.

    uv run scripts/gen_superposition.py
"""
import json
from pathlib import Path
import numpy as np
import torch

OUT = Path(__file__).resolve().parent.parent / "static" / "html" / "applets" / "data" / "superposition.json"
N, M = 5, 2
IMPORTANCE = torch.tensor([0.9 ** i for i in range(N)])          # comme dans l'article : des concepts d'importance décroissante
RARETES = [0.0, 0.5, 0.7, 0.8, 0.9, 0.95, 0.98, 0.99]


def entrainer(S, graine=0):
    torch.manual_seed(graine)
    W = torch.nn.Parameter(torch.randn(M, N) * 0.3)
    b = torch.nn.Parameter(torch.zeros(N))
    opt = torch.optim.Adam([W, b], lr=3e-3)
    for pas in range(30000):
        x = torch.rand(2048, N) * (torch.rand(2048, N) > S).float()
        xr = torch.relu(x @ W.T @ W + b)
        perte = (IMPORTANCE * (x - xr) ** 2).mean()
        opt.zero_grad(); perte.backward(); opt.step()
    return W.detach().numpy(), b.detach().numpy(), float(perte)


resultats = []
for S in RARETES:
    meilleur = min((entrainer(S, g) for g in range(8)), key=lambda r: r[2])   # quelques départs, on garde le meilleur
    W, b, perte = meilleur
    normes = np.linalg.norm(W, axis=0)
    angles = sorted(round(float(np.degrees(np.arctan2(W[1, i], W[0, i]))) % 360) for i in range(N) if normes[i] > 0.5)
    print(f"rareté {S:.2f} : perte {perte:.4f}, normes {np.round(normes, 2)}, angles {angles}")
    resultats.append({"rarete": S, "W": np.round(W, 4).tolist(), "b": np.round(b, 4).tolist(), "perte": round(perte, 5)})
OUT.write_text(json.dumps(resultats, separators=(",", ":")) + "\n")
print(OUT.name, "écrit")
