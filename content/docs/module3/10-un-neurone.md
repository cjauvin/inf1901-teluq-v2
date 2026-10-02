---
title: "Un neurone"
weight: 10
slug: un-neurone
---

# Un neurone

Le chapitre « [Deux paris rivaux](docs/module1/20-deux-paris/#le-second-pari-lesprit-comme-cerveau) »
a présenté le **perceptron** de Frank Rosenblatt (1958), une machine qui apprend à
partir d'exemples au lieu de suivre des règles écrites à la main. Le chapitre
« [Les hivers et la bascule](docs/module1/60-hivers/#le-premier-hiver-la-mort-du-perceptron-1969) »
a montré comment cette approche a été mise de côté après 1969, quand Minsky et
Papert ont démontré qu'un perceptron ne peut pas apprendre certaines fonctions
simples, comme le XOR.

Les **réseaux de neurones** actuels sont les descendants directs du perceptron. Ce
module explique comment ils fonctionnent, comment ils ont dépassé la limite de
1969, et pourquoi ils dominent l'intelligence artificielle depuis le début des
années 2010. Il commence par l'élément de base, le **neurone artificiel**.

## Un neurone est une régression logistique

Vous connaissez déjà le neurone artificiel, sous un autre nom. C'est la
[régression logistique](docs/module2/60-classer/#tracer-une-frontière-la-régression-logistique)
du Module 2.

Un neurone reçoit des nombres en **entrée**, et il produit un seul nombre en
**sortie**. Il effectue pour cela deux opérations :

1. Il multiplie chaque entrée par un **poids**, il additionne les résultats, et il
   ajoute un dernier nombre, le **biais**. On obtient une somme pondérée.
2. Il passe cette somme dans une **fonction d'activation**. La plus classique est
   la sigmoïde, qui ramène n'importe quel nombre à une valeur comprise entre 0 et 1.

Pour un neurone à deux entrées, le calcul s'écrit ainsi :

$$\text{sortie} = \sigma(w_1 x_1 + w_2 x_2 + b)$$

où $x_1$ et $x_2$ sont les entrées, $w_1$ et $w_2$ les poids, $b$ le biais et
$\sigma$ la sigmoïde.

{{< image src="/images/module3/neurone-schema.svg" alt="De gauche à droite : deux entrées, x1 et x2, reliées chacune par une flèche qui porte un poids, w1 et w2, à un neurone. Le neurone fait la somme pondérée des entrées, à laquelle s'ajoute le biais b, puis applique la fonction d'activation sigmoïde. Une flèche sort du neurone vers la sortie, un nombre entre 0 et 1." title="Un neurone artificiel : une somme pondérée des entrées, puis une fonction d'activation." loading="lazy" >}}

Les poids et le biais sont les **paramètres** du neurone, au sens du Module 2. Un
poids élevé donne beaucoup d'importance à l'entrée correspondante, un poids proche
de zéro la fait presque ignorer, et un poids négatif la fait compter contre la
conclusion. Comme pour tous les modèles du Module 2, on ne fixe pas ces paramètres
à la main. On les règle par
[descente de gradient](docs/module2/50-entrainer-un-modele/#apprendre-cest-descendre-la-pente),
à partir d'exemples.

Un neurone peut avoir beaucoup plus que deux entrées. Prenons l'exemple qui servira
dans tout ce module, la **reconnaissance de chiffres manuscrits**. Une image de
chiffre de 28 pixels sur 28 est une liste de 784 nombres, un par pixel, comme l'a
montré le chapitre
« [Regarder les données](docs/module2/30-les-donnees/#une-maison-cest-une-liste-de-nombres) ».
Un neurone qui reçoit cette image a donc 784 entrées et 784 poids. Sa sortie peut se
lire comme une réponse à une question simple, par exemple « cette image est-elle un
zéro ? ».

{{< image src="/images/module3/chiffre-vers-neurone.svg" alt="À gauche, une image de 28 pixels sur 28 qui montre un zéro manuscrit ; chaque pixel est un nombre. Des lignes relient les pixels à un neurone, chacune avec son poids. À droite, la sortie du neurone : 0,97, lue comme la réponse à la question « est-ce un zéro ? »." title="Une image de chiffre manuscrit donne 784 entrées à un neurone, qui répond par un nombre entre 0 et 1." loading="lazy" >}}
