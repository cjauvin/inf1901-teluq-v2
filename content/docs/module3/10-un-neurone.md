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

## D'où vient le mot « neurone »

Le terme vient d'une analogie avec le cerveau. Un neurone biologique reçoit des
signaux d'autres neurones par ses **dendrites**. Il les combine dans son **corps
cellulaire**. Si le signal combiné est assez fort, il envoie à son tour un signal
le long de son **axone**, vers d'autres neurones. Les points de contact entre
neurones s'appellent des **synapses**, et leur force varie avec l'expérience.

Le neurone artificiel reprend ce schéma en le simplifiant beaucoup. Les entrées
jouent le rôle des dendrites, les poids celui des synapses, la somme et la fonction
d'activation celui du corps cellulaire, et la sortie celui de l'axone.

{{< image src="/images/module3/neurone-biologique-artificiel.svg" alt="En haut, un neurone biologique : des dendrites ramifiées à gauche, terminées par des synapses, un corps cellulaire au centre, et un long axone vers la droite. En bas, un neurone artificiel : des entrées et leurs poids à gauche, la somme et la fonction d'activation au centre, la sortie à droite. Les mêmes couleurs relient les éléments qui se correspondent." title="Du neurone biologique au neurone artificiel : les entrées pour les dendrites, les poids pour les synapses, le calcul pour le corps cellulaire, la sortie pour l'axone." loading="lazy" >}}

Cette analogie a guidé les premiers chercheurs, mais elle est très approximative.
Un neurone biologique est beaucoup plus complexe qu'une somme suivie d'une
fonction. Le chapitre « L'apprentissage profond » reviendra sur ce que cette
comparaison permet de dire, et sur ce qu'elle ne permet pas.

## Un neurone à manipuler

Dans l'applet ci-dessous, vous réglez vous-même les entrées et les paramètres d'un
neurone, et vous observez sa sortie.

{{< applet src="/html/applets/neuron.html" height="547" >}}

Essayez les trois manipulations suivantes :

1. Fixez les deux entrées à 1. Trouvez des poids qui donnent une sortie proche de
   1, puis des poids qui donnent une sortie proche de 0.
2. Donnez un poids de zéro à la première entrée. Faites varier cette entrée, et
   observez que la sortie ne change plus.
3. Donnez un poids négatif à la seconde entrée. Augmentez cette entrée, et
   observez que la sortie diminue.

## Ce qu'un neurone seul ne peut pas faire

Un neurone seul a la même limite que la régression logistique. Sa somme pondérée
définit une **frontière droite** : d'un côté, la sortie est supérieure à 0,5, et de
l'autre, elle est inférieure. Un neurone ne peut donc séparer deux catégories que
si une droite suffit à les séparer.

Ce n'est pas toujours le cas. Le XOR, présenté avec sa
[table de vérité](docs/module1/60-hivers/#le-premier-hiver-la-mort-du-perceptron-1969)
au Module 1, en est l'exemple le plus simple. Ses quatre cas occupent les coins
d'un carré, et
[aucune droite](docs/module2/70-generaliser/#linéaire-ou-non-linéaire-ce-quun-modèle-peut-dessiner)
ne sépare les deux cas « vrai » des deux cas « faux ». C'est exactement la limite
que Minsky et Papert ont démontrée en 1969.

Au Module 2, on contournait cette limite de deux façons : en changeant de modèle,
ou en fabriquant à la main une nouvelle caractéristique. Les réseaux de neurones
apportent une troisième réponse. On relie plusieurs neurones entre eux, et le
réseau fabrique lui-même la caractéristique qui manque. C'est le sujet du chapitre
suivant, « Une couche cachée ».
