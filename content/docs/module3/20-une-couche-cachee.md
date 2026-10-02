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

## Deux droites à déplacer

Dans l'applet ci-dessous, chaque droite représente un neurone caché. Vous pouvez la
déplacer et la faire pivoter, comme dans l'applet de la
[régression logistique](docs/module2/60-classer/#tracer-une-frontière-la-régression-logistique).
La zone délimitée par les deux droites est colorée : c'est là que le réseau répond
« vrai ». Un point mal classé est entouré d'un cercle orange.

{{< applet src="/html/applets/xor-deux-droites.html" height="667" >}}

1. Placez les deux droites pour que la zone colorée contienne les deux points
   rouges, et aucun point bleu.
2. Cherchez une autre solution, avec des droites orientées autrement. Il en existe
   plusieurs.
3. Choisissez ensuite le second jeu de points, « un groupe entouré », où un groupe
   rouge est entouré de points bleus. Constatez que deux droites ne suffisent plus.
4. Ajoutez une troisième droite, avec le bouton « 3 », et entourez le groupe rouge.

## Plus de neurones, plus de formes

Deux neurones cachés donnent deux droites. Trois neurones en donnent trois, ce qui
permet de délimiter un triangle, comme dans la dernière manipulation. Avec un grand
nombre de neurones, on peut entourer une zone de forme quelconque, à la précision
voulue.

Ce résultat a été démontré en 1989, sous le nom de **théorème d'approximation
universelle** : un réseau à une seule couche cachée, avec assez de neurones, peut
approcher presque n'importe quelle fonction. Le répertoire de formes d'un réseau de
neurones n'a donc pas la limite de celui d'un
[modèle linéaire](docs/module2/70-generaliser/#linéaire-ou-non-linéaire-ce-quun-modèle-peut-dessiner).

Un réseau peut aussi avoir plusieurs sorties. Pour reconnaître les chiffres
manuscrits, on utilise un réseau à **dix sorties**, une par chiffre. Chaque sortie
donne un nombre entre 0 et 1, et le réseau répond par le chiffre dont la sortie est
la plus élevée.

{{< image src="/images/module3/reseau-chiffres.svg" alt="De gauche à droite : une image de 28 pixels sur 28 qui montre un zéro ; une couche d'entrée de 784 valeurs, une par pixel ; une couche cachée de 30 neurones ; une couche de sortie de dix neurones, numérotés de 0 à 9. Chaque sortie donne un nombre entre 0 et 1. La sortie du chiffre 0 est la plus élevée, 0,96 : c'est la réponse du réseau." title="Un réseau pour les chiffres manuscrits : 784 entrées, une couche cachée de 30 neurones, dix sorties." loading="lazy" >}}

## Qui règle tous ces poids ?

Pour le XOR, nous avons choisi les poids à la main, parce que le réseau n'en compte
que neuf. Le réseau des chiffres en compte des milliers. Avec une couche cachée de
30 neurones, il y a 784 × 30 poids entre l'entrée et la couche cachée, puis 30 × 10
entre la couche cachée et la sortie, soit près de 24 000 paramètres en comptant les
biais. Personne ne peut les régler à la main.

Le théorème d'approximation universelle dit qu'il existe de bons poids. Il ne dit
pas comment les trouver. Ce problème a bloqué les réseaux de neurones pendant près
de vingt ans. On savait depuis les années 1960 qu'une couche cachée dépasserait la
[limite du perceptron](docs/module1/60-hivers/#le-premier-hiver-la-mort-du-perceptron-1969),
mais on ne savait pas comment entraîner un tel réseau. La solution, la
**rétropropagation du gradient**, s'est imposée en 1986. C'est le sujet du chapitre
suivant, « Entraîner un réseau ».
