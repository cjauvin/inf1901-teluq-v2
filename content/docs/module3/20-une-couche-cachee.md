---
title: "Une couche cachée"
weight: 20
slug: une-couche-cachee
---

# Une couche cachée

Le chapitre « [Un neurone](docs/module3/10-un-neurone/#ce-quun-neurone-seul-ne-peut-pas-faire) »
s'est terminé sur une limite : un neurone seul ne trace qu'une frontière droite, et
il ne peut donc pas apprendre le XOR. Ce chapitre montre comment quelques neurones
reliés entre eux dépassent cette limite.

## Relier des neurones

La sortie d'un neurone est un nombre. Rien n'empêche de donner ce nombre en entrée
à un autre neurone. On obtient alors un **réseau de neurones**, organisé en
**couches** :

- la **couche d'entrée** contient les données, par exemple les deux entrées du XOR
  ou les 784 pixels d'une image ;
- la **couche de sortie** donne la réponse du réseau ;
- entre les deux, une ou plusieurs **couches cachées** font des calculs
  intermédiaires. On les appelle « cachées » parce que, de l'extérieur, on ne voit
  que les entrées et la réponse.

Chaque neurone d'une couche reçoit les sorties de tous les neurones de la couche
précédente, chacune avec son propre poids.

{{< image src="/images/module3/reseau-xor.svg" alt="Trois colonnes. À gauche, la couche d'entrée : A et B. Au centre, la couche cachée : le neurone 1, qui répond à la question « au moins une ? », et le neurone 2, qui répond à « les deux ? ». À droite, la couche de sortie : un neurone qui donne A XOR B. Chaque entrée est reliée aux deux neurones cachés, et chaque neurone caché au neurone de sortie." title="Le plus petit réseau qui résout le XOR : deux entrées, deux neurones cachés, un neurone de sortie." loading="lazy" >}}

## Le XOR résolu avec trois neurones

Reprenons le XOR, avec ses deux entrées A et B. Le réseau ci-dessus le résout si
chaque neurone répond à une question simple, qu'un neurone seul sait traiter :

- le premier neurone caché répond à la question « **au moins une** des deux
  entrées est-elle vraie ? » ;
- le second neurone caché répond à la question « les **deux** entrées sont-elles
  vraies ? » ;
- le neurone de sortie combine ces deux réponses. Il répond « vrai » quand le
  premier neurone dit oui et que le second dit non, c'est-à-dire quand au moins une
  entrée est vraie, mais pas les deux.

La table suivante reprend les quatre cas :

| A | B | Neurone 1 : au moins une ? | Neurone 2 : les deux ? | Sortie : A XOR B |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 | 0 |

La dernière colonne est bien celle de la
[table de vérité du XOR](docs/module1/60-hivers/#le-premier-hiver-la-mort-du-perceptron-1969).
Aucun des trois neurones ne fait quelque chose de difficile. C'est leur combinaison
qui résout un problème qu'aucun d'eux ne peut résoudre seul.

{{% details "Pour aller plus loin : les poids de ce réseau" %}}
Voici des poids et des biais qui donnent exactement ce comportement. Chaque
neurone calcule une somme pondérée, puis la passe dans la sigmoïde, comme dans le
chapitre « [Un neurone](docs/module3/10-un-neurone/#un-neurone-est-une-régression-logistique) ».

| Neurone | Poids | Biais | Somme calculée |
|---|:---:|:---:|:---:|
| Neurone 1 (au moins une ?) | 10 et 10 | −5 | 10·A + 10·B − 5 |
| Neurone 2 (les deux ?) | 10 et 10 | −15 | 10·A + 10·B − 15 |
| Sortie | 10 et −20 | −5 | 10·(neurone 1) − 20·(neurone 2) − 5 |

Prenons le cas A = 0 et B = 1 :

- le neurone 1 calcule 10·0 + 10·1 − 5 = 5, et la sigmoïde donne environ 0,99 ;
- le neurone 2 calcule 10·0 + 10·1 − 15 = −5, et la sigmoïde donne environ 0,01 ;
- la sortie calcule 10·0,99 − 20·0,01 − 5 = 4,7, et la sigmoïde donne environ 0,99.

Le réseau répond donc « vrai », comme prévu. Les trois autres cas se vérifient de
la même façon. Les poids sont grands (10, 20) pour que la sigmoïde donne des
réponses nettes, très proches de 0 ou de 1.
{{% /details %}}

## Ce que fait la couche cachée : changer de point de vue

On peut comprendre ce résultat de deux façons.

**Première lecture : deux droites au lieu d'une.** Chaque neurone caché trace sa
propre droite dans le plan des entrées. Avec deux droites, on délimite une bande.
Les deux cas « vrai » du XOR sont dans la bande, et les deux cas « faux » sont à
l'extérieur, un de chaque côté. Une seule droite ne pouvait pas faire ce découpage.

**Seconde lecture : un nouvel espace.** La couche cachée remplace les deux
entrées, A et B, par deux nouvelles valeurs, les réponses des neurones 1 et 2. Dans
ce nouvel espace, les quatre cas ne sont plus aux coins d'un carré. Les deux cas
« vrai » arrivent au même endroit, et une seule droite suffit maintenant à les
séparer des deux autres. Le neurone de sortie trace cette droite.

{{< image src="/images/module3/xor-couche-cachee.svg" alt="Deux panneaux. À gauche, le plan des entrées A et B : les deux cas « faux », en bleu, sont aux coins (0, 0) et (1, 1) ; les deux cas « vrai », en rouge, aux coins (0, 1) et (1, 0). Deux droites parallèles, une par neurone caché, délimitent une bande qui contient les deux points rouges. À droite, l'espace de la couche cachée : les deux cas rouges sont au même point, les cas bleus aux deux autres, et une seule droite sépare le rouge du bleu." title="Le XOR avant et après la couche cachée : deux droites dans le plan des entrées, une seule droite dans le nouvel espace." loading="lazy" >}}

Cette seconde lecture rejoint une idée du Module 2. Dans
« [Généraliser](docs/module2/70-generaliser/#linéaire-ou-non-linéaire-ce-quun-modèle-peut-dessiner) »,
on rendait le XOR séparable en ajoutant à la main une caractéristique, le produit
des deux entrées. Ce produit vaut 1 seulement quand les deux entrées valent 1. C'est
exactement la question à laquelle répond le neurone 2. La différence est que
personne n'a besoin de trouver cette caractéristique : avec les bons poids, le
réseau la construit lui-même. Une couche cachée est donc une **fabrique de
caractéristiques**.
