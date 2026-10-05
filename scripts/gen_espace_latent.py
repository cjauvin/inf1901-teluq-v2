# /// script
# requires-python = ">=3.10,<3.13"
# dependencies = ["torch", "torchvision", "numpy"]
# ///
"""Module 4, « Générer : imiter une distribution » : l'espace latent des chiffres manuscrits.

Entraîne un petit autoencodeur variationnel (VAE) sur MNIST, avec un espace latent à deux
dimensions, puis exporte pour l'applet `espace-latent.html` :
- les poids du décodeur (2 → 128 → 256 → 784), en float16 encodés en base64 ;
- la position latente (moyenne de l'encodeur) de 2 000 chiffres du jeu de test, avec leur étiquette et leur numéro.

MNIST est téléchargé par torchvision dans ~/.cache/inf1901/mnist au premier lancement.

    uv run scripts/gen_espace_latent.py
"""
import base64, json
from pathlib import Path
import numpy as np
import torch
from torch import nn
from torchvision import datasets, transforms

torch.manual_seed(0)
RACINE = Path(__file__).resolve().parent
CACHE = Path.home() / ".cache" / "inf1901" / "mnist"
SORTIE = RACINE.parent / "static" / "html" / "applets" / "data" / "espace-latent.json"
dev = "mps" if torch.backends.mps.is_available() else "cpu"

t = transforms.ToTensor()
train = datasets.MNIST(CACHE, train=True, download=True, transform=t)
test = datasets.MNIST(CACHE, train=False, download=True, transform=t)
X = train.data.float().div(255).view(-1, 784).to(dev)
Xt = test.data.float().div(255).view(-1, 784)


class VAE(nn.Module):
    def __init__(self):
        super().__init__()
        self.enc = nn.Sequential(nn.Linear(784, 512), nn.ReLU(), nn.Linear(512, 256), nn.ReLU())
        self.mu, self.logvar = nn.Linear(256, 2), nn.Linear(256, 2)
        self.dec = nn.Sequential(nn.Linear(2, 128), nn.ReLU(), nn.Linear(128, 256), nn.ReLU(), nn.Linear(256, 784))

    def forward(self, x):
        h = self.enc(x)
        mu, logvar = self.mu(h), self.logvar(h)
        z = mu + torch.randn_like(mu) * (0.5 * logvar).exp()
        return self.dec(z), mu, logvar


m = VAE().to(dev)
opt = torch.optim.Adam(m.parameters(), lr=1e-3)
for epoque in range(40):
    perm = torch.randperm(len(X), device=dev)
    total = 0.0
    for i in range(0, len(X), 128):
        x = X[perm[i:i + 128]]
        logits, mu, logvar = m(x)
        rec = nn.functional.binary_cross_entropy_with_logits(logits, x, reduction="sum")
        kl = -0.5 * (1 + logvar - mu ** 2 - logvar.exp()).sum()
        perte = (rec + kl) / len(x)
        opt.zero_grad(); perte.backward(); opt.step()
        total += perte.item() * len(x)
    print(f"époque {epoque + 1:2d} : perte {total / len(X):.1f}")

m = m.cpu().eval()
with torch.no_grad():
    idx = torch.randperm(len(Xt))[:2000]
    mu = m.mu(m.enc(Xt[idx])).numpy()
etiquettes = test.targets[idx].numpy()


def couche(l):
    w = l.weight.detach().numpy().T.astype(np.float16)     # (entrées, sorties)
    b = l.bias.detach().numpy().astype(np.float16)
    return {"entrees": w.shape[0], "sorties": w.shape[1],
            "w": base64.b64encode(w.tobytes()).decode(), "b": base64.b64encode(b.tobytes()).decode()}


SORTIE.parent.mkdir(parents=True, exist_ok=True)
SORTIE.write_text(json.dumps({
    "couches": [couche(m.dec[0]), couche(m.dec[2]), couche(m.dec[4])],
    "points": [[round(float(a), 2), round(float(b), 2), int(e)] for (a, b), e in zip(mu, etiquettes)],
    "indices": [int(i) for i in idx],                  # numéros des images de test, pour les figures
}, separators=(",", ":")))
print(SORTIE.name, "écrit,", SORTIE.stat().st_size // 1024, "Ko ; étendue latente",
      mu.min(0).round(2), mu.max(0).round(2))
