---
title: "Un modèle qui s'entraîne"
weight: 50
slug: entrainer-un-modele
---

# Un modèle qui s'entraîne

Le chapitre « [Prédire par ressemblance](docs/module2/40-predire-par-ressemblance/#langle-mort-de-knn) » s'est terminé sur un objectif : obtenir un modèle qui ne se
contente pas de mémoriser les exemples, mais qui en extrait une tendance générale,
résumée en quelques paramètres, qu'on pourra ensuite appliquer sans conserver
toutes les données.

Nous allons construire ce modèle. Comme nous cherchons le plus simple, nous allons
faire l'opération la plus élémentaire qu'on puisse faire sur un nuage de points :
**y faire passer une droite.**

## Un modèle qui tient en deux nombres

Reprenons notre nuage de maisons (la superficie à l'horizontale, le prix à la
verticale). Faire passer une droite à travers ce nuage revient à supposer qu'il
existe une relation simple et régulière entre la taille d'une maison et son prix, du
type « chaque mètre carré supplémentaire ajoute environ tant de dollars ». Cette
droite est notre modèle. C'est aussi le plus ancien modèle de ce module. Legendre et
Gauss ajustaient déjà des droites par la méthode des moindres carrés (*least
squares*) vers 1805 pour prédire la trajectoire des comètes, et c'est Francis Galton
qui, en 1886, lui a donné le nom de *régression*, en étudiant la taille des enfants
par rapport à celle de leurs parents.

{{< image src="/images/module2/maisons-droite.svg" alt="Le nuage de maisons traversé par une droite inclinée qui suit sa tendance : le modèle de régression linéaire." title="La droite qui suit la tendance du nuage : c'est notre modèle." loading="lazy" >}}

En mathématiques, une droite se résume à deux nombres :

$$\text{prix} = m \times \text{superficie} + b$$

- **m**, la *pente* (*slope*) : de combien le prix monte quand la superficie augmente
  d'une unité ;
- **b**, l'*ordonnée à l'origine* (*intercept*) : le point de départ, là où la droite
  croise l'axe vertical.

Ces deux nombres, m et b, sont les **paramètres** du modèle, et ils ont ici une
signification. [Le modèle le plus bête](docs/module2/20-modele-le-plus-bete)
résumait tout en un seul nombre (la moyenne), et kNN n'avait aucun paramètre.
Notre droite en a deux, ce qui suffit pour représenter une *tendance*, avec une
direction et une hauteur. Si on change m et b, on obtient une autre droite, donc
un autre modèle. Le problème consiste à trouver le couple (m, b) qui donne la
droite la mieux ajustée au nuage.

Essayez vous-même. Dans l'applet ci-dessous, déplacez la droite (vous ajustez
ainsi m et b à la main) et cherchez la position qui colle le mieux aux points.

{{< applet src="/html/applets/linear-regression.html" height="635" >}}

## Mesurer l'erreur

En déplaçant la droite, vous avez cherché à la placer « bien ». Il faut cependant
préciser ce que « bien » veut dire. Il nous faut une mesure, que nous avons déjà
rencontrée avec le modèle le plus bête sans encore la définir précisément :
l'**erreur**.

Pour une droite donnée, l'erreur sur une maison est l'écart entre le prix que la
droite *prédit* (le point de la droite à la verticale de cette maison) et son prix
*réel*. Comme pour le modèle le plus bête, cet écart est un segment vertical. La
différence est qu'ici la droite est inclinée, et qu'elle peut donc passer beaucoup
plus près des points qu'une droite horizontale.

{{< image src="/images/module2/maisons-erreurs-droite.svg" alt="Le nuage de maisons et la droite de régression inclinée, avec un court segment rouge reliant chaque maison à la droite : l'erreur, bien plus courte qu'avec la droite plate du modèle le plus bête." title="Les mêmes erreurs qu'avec le modèle le plus bête, mais par rapport à une droite inclinée : elles sont beaucoup plus courtes." loading="lazy" >}}

L'erreur totale du modèle combine tous ces écarts. On les met au carré, pour que les
écarts au-dessus et en dessous de la droite ne s'annulent pas et pour pénaliser
davantage les grands écarts, puis on en fait la moyenne. Ce nombre, la moyenne des
carrés des écarts, porte un nom technique, l'*erreur quadratique moyenne* (*mean
squared error*), mais l'idée est simple : **plus il est petit, mieux la droite
s'ajuste au nuage.** (Considérez le cas limite. Si la droite passait exactement par
tous les points, chaque écart serait nul, chaque carré aussi, et l'erreur vaudrait
zéro. C'est la valeur minimale possible. Avec un nuage comme le nôtre, aucune droite
ne l'atteint, et l'objectif est de s'en approcher le plus possible.)

On peut se représenter cette erreur de la façon suivante. Imaginez que chaque
point est relié à la droite par un petit ressort vertical. Un point éloigné tire
fort, un point proche tire à peine. La meilleure droite est celle où les forces de
tous ces ressorts s'équilibrent, c'est-à-dire la position de moindre tension.
Cette position correspond à la droite de plus petite erreur. Vous pouvez
l'observer dans l'applet suivante :

{{< applet src="/html/applets/linear-regression-with-springs.html" height="635" >}}

Trouver cette droite à la main, comme dans l'applet, reste possible en deux
dimensions. Il reste à voir comment une machine peut la trouver seule, y compris
quand le modèle n'a plus deux paramètres, mais des milliers. C'est l'objet de la
[section suivante](#apprendre-cest-descendre-la-pente).

## Apprendre, c'est descendre la pente

L'idée présentée dans cette section est au cœur de tout l'apprentissage
automatique moderne, sous une forme ou une autre, y compris dans les plus grands
modèles actuels.

Repartons de l'erreur. Pour chaque choix de paramètres (m, b), le modèle commet
une certaine erreur totale. L'erreur est donc elle-même une *fonction* des
paramètres. On peut la représenter comme un **paysage**. Les deux paramètres sont
les coordonnées sur une carte (est-ouest pour m, nord-sud pour b), et l'erreur est
l'**altitude** en chaque point. Le paysage a donc **trois dimensions** : deux pour
les paramètres, *m* et *b*, et une troisième, verticale, pour l'erreur. Les
sommets correspondent aux mauvais modèles (grande erreur), et les vallées aux bons.
Trouver le meilleur modèle revient à trouver le **point le plus bas** de ce
paysage.

{{< image src="/images/module2/descente-gradient.svg" alt="Une cuvette en trois dimensions (paraboloïde) représentant l'erreur du modèle au-dessus du plan des réglages (m, b). Une bille placée au hasard sur le bord descend la pente jusqu'au creux, où l'erreur est minimale : le meilleur modèle." title="La descente de gradient : l'erreur forme une cuvette au-dessus des réglages (m, b) ; la bille descend jusqu'au creux, qui correspond au meilleur modèle." loading="lazy" >}}

La machine ne connaît pas la forme complète de ce paysage. Elle procède comme un
randonneur dans le brouillard : elle mesure la **pente** à l'endroit où elle se
trouve et fait un pas dans la direction qui descend le plus. Puis elle recommence.
Pas après pas, elle descend vers le creux, comme une bille posée sur le flanc d'une
vallée roule vers le fond. Quand la pente devient nulle, le fond est atteint, et les
meilleurs paramètres sont trouvés. Cette méthode s'appelle la **descente de
gradient** (*gradient descent* ; le « gradient » désigne la direction de plus forte
pente). C'est le mécanisme central de l'apprentissage.

La taille des pas a de l'importance. Si les pas sont trop grands, on risque de
dépasser le creux et d'osciller autour sans l'atteindre. S'ils sont trop petits, la
descente est très longue. Ce réglage, le *taux d'apprentissage* (*learning rate*),
n'est pas un paramètre du modèle, mais un réglage de la *procédure*. On l'appelle un
**hyper-paramètre** (*hyperparameter*).

Cette idée rejoint la fin du [Module 1](docs/module1/60-hivers/#la-bascule), où
nous annoncions qu'*« apprendre, c'est encore chercher, mais dans un autre
espace »*. Il ne s'agit plus d'explorer les coups d'une partie d'échecs, mais
l'ensemble très vaste des réglages possibles d'un modèle. La descente de gradient
est cette recherche. Le GOFAI cherchait la solution elle-même, alors que
l'apprentissage cherche les paramètres qui permettent de la produire. De plus, la
méthode reste la même quelle que soit l'échelle : que le paysage ait deux
dimensions (m et b) ou plusieurs milliards (les poids d'un grand réseau de
neurones), il s'agit toujours de descendre la pente.

{{% details "Les mathématiques de la régression linéaire (optionnel)" %}}

L'erreur quadratique moyenne, pour $n$ maisons, s'écrit :

$$J(m, b) = \frac{1}{n} \sum_{i=1}^{n} \big(y_i - (m x_i + b)\big)^2$$

où $x_i$ est la superficie de la maison $i$, $y_i$ son vrai prix, et $m x_i + b$
le prix prédit. Cette fonction correspond à la « carte d'altitude » du paysage :
à chaque couple $(m, b)$, elle associe une hauteur d'erreur.

La descente de gradient mesure, en un point, la pente de cette surface dans
chaque direction (les *dérivées partielles*) :

$$\frac{\partial J}{\partial m} = -\frac{2}{n} \sum_{i=1}^{n} x_i\big(y_i - (m x_i + b)\big), \qquad \frac{\partial J}{\partial b} = -\frac{2}{n} \sum_{i=1}^{n} \big(y_i - (m x_i + b)\big)$$

puis fait un pas dans le sens inverse de la pente, d'une taille réglée par le taux
d'apprentissage $\alpha$ :

$$m \leftarrow m - \alpha\,\frac{\partial J}{\partial m}, \qquad b \leftarrow b - \alpha\,\frac{\partial J}{\partial b}$$

On répète ces étapes jusqu'à ce que l'erreur ne diminue plus. Pour la régression
linéaire, il existe même une formule directe (les moindres carrés de Gauss) qui
donne la solution en une seule étape. La descente de gradient a cependant
l'avantage de fonctionner pour des modèles beaucoup plus complexes, jusqu'aux
réseaux de neurones.

{{% /details %}}

## Et pour prédire une catégorie ?

Nous avons maintenant un modèle qui apprend : une droite, deux paramètres, une
erreur à minimiser et une descente vers le creux. Ce modèle prédit un **nombre**,
ici un prix.

Beaucoup de questions demandent cependant comme réponse une **catégorie** plutôt
qu'un nombre. Par exemple, ce courriel est-il un pourriel ou non ? Cette photo
montre-t-elle un chat ou un chien ? Nous avons rencontré ce type de tâche au
[chapitre sur kNN](docs/module2/40-predire-par-ressemblance/#les-k-plus-proches-voisins) : la **classification**. Cependant, kNN n'apprenait rien. Nous
voulons maintenant un modèle qui s'entraîne comme notre droite, mais dont la
sortie est une catégorie plutôt qu'une valeur.

Presque tous les éléments que nous venons de construire vont servir de nouveau. Un
modèle réglé par des paramètres, une fonction d'erreur et une
descente de gradient pour la minimiser forment un ensemble assez général pour
s'appliquer à la classification comme à la régression. Il suffira de modifier la
*forme* du modèle (une droite qui *sépare* les points, plutôt qu'une droite qui
*suit* leur tendance) et la *façon de calculer l'erreur*. C'est l'objet du prochain
chapitre, « [Classer](docs/module2/60-classer) ».
