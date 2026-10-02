---
title: "Entraîner un réseau"
weight: 30
slug: entrainer-un-reseau
---

# Entraîner un réseau

Le chapitre « [Une couche cachée](docs/module3/20-une-couche-cachee/#qui-règle-tous-ces-poids) »
s'est terminé sur un réseau de près de 24 000 poids, que personne ne peut régler à
la main. Ce chapitre explique comment un réseau règle lui-même ses poids, à partir
d'exemples.

## Le même principe qu'au Module 2

La méthode a déjà été présentée dans
« [Apprendre, c'est descendre la pente](docs/module2/50-entrainer-un-modele/#apprendre-cest-descendre-la-pente) ».
Elle tient en trois étapes, qu'on répète :

1. on mesure l'**erreur** du modèle sur des exemples dont on connaît la bonne
   réponse ;
2. on cherche dans quel sens modifier chaque paramètre pour que l'erreur diminue ;
3. on modifie un peu chaque paramètre dans ce sens.

C'est la **descente de gradient**. Pour la droite du Module 2, il y avait deux
paramètres, et l'erreur formait un paysage qu'on pouvait dessiner. Pour un réseau,
les paramètres sont les poids et les biais. Le paysage a alors des milliers de
dimensions et on ne peut plus le dessiner, mais la méthode reste la même : mesurer
la pente, puis faire un pas vers le bas.

## Le problème des couches cachées

La deuxième étape est simple pour un neurone seul. On connaît la bonne réponse, on
voit donc directement si sa sortie est trop haute ou trop basse, et on corrige ses
poids en conséquence. C'est ce que faisait le perceptron dès 1958.

Dans un réseau, cela ne vaut que pour la couche de sortie. Pour un neurone caché,
les exemples ne donnent aucune bonne réponse. Reprenons le
[réseau du XOR](docs/module3/20-une-couche-cachee/#le-xor-résolu-avec-trois-neurones) :
la table de vérité dit ce que la sortie doit valoir, mais elle ne dit pas que le
premier neurone caché doit répondre à la question « au moins une ? ». Quand le
réseau se trompe, on ne sait pas quel neurone caché est en cause, ni dans quel sens
le corriger.

Ce problème s'appelle l'**attribution de la responsabilité** (*credit assignment*
en anglais). C'est lui qui a arrêté la recherche sur les réseaux de neurones après
[1969](docs/module1/60-hivers/#le-premier-hiver-la-mort-du-perceptron-1969) : on
savait qu'une couche cachée était nécessaire, et on ne savait pas l'entraîner.

## La rétropropagation

La solution consiste à calculer la responsabilité de chaque poids en partant de la
sortie et en remontant vers l'entrée. Pour chaque exemple, le calcul se fait en
deux temps.

**La propagation avant.** L'exemple entre dans le réseau. Chaque couche calcule ses
sorties et les passe à la suivante, jusqu'à la réponse du réseau. On compare cette
réponse à la bonne, ce qui donne l'erreur. Les poids sont utilisés, mais pas
modifiés.

**La rétropropagation.** L'erreur repart en sens inverse. Le neurone de sortie
reçoit l'erreur entière. Il la répartit entre les neurones cachés qui lui ont
envoyé un signal, selon le poids de chaque connexion : un neurone caché relié par
un poids élevé a beaucoup contribué à la réponse, et il reçoit donc une grande part
de l'erreur. Chaque neurone caché sait alors dans quel sens il aurait dû répondre,
et on peut corriger ses poids comme ceux d'un neurone seul.

{{< image src="/images/module3/retropropagation.svg" alt="Deux panneaux qui montrent le réseau du XOR : deux entrées, deux neurones cachés, un neurone de sortie. À gauche, la propagation avant : les flèches vont de l'entrée vers la sortie ; le réseau répond 0,62 alors que la bonne réponse est 1, soit une erreur de 0,38. À droite, la rétropropagation : les flèches vont de la sortie vers l'entrée ; le neurone 1, relié à la sortie par un poids élevé, reçoit une grande part de l'erreur, et le neurone 2, relié par un poids faible, une petite part." title="Les deux temps du calcul pour un exemple : la propagation avant donne la réponse et l'erreur, la rétropropagation répartit cette erreur entre les poids." loading="lazy" >}}

Une fois la part de chaque poids connue, on modifie tous les poids un peu, dans le
sens qui réduit l'erreur. Puis on passe à l'exemple suivant. Le nom complet de la
méthode est la **rétropropagation du gradient** (*backpropagation* en anglais).

Avec plusieurs couches cachées, le principe ne change pas : l'erreur remonte d'une
couche à la précédente, jusqu'à l'entrée.

{{% details "Pour aller plus loin : ce que calcule la rétropropagation" %}}
Un réseau est une suite de calculs emboîtés. La sortie dépend de la couche cachée,
qui dépend elle-même des entrées et des poids. La descente de gradient demande,
pour chaque poids, la pente de l'erreur par rapport à ce poids, c'est-à-dire une
dérivée. Pour des calculs emboîtés, cette dérivée s'obtient par la
[règle de dérivation en chaîne](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_d%C3%A9rivation_des_fonctions_compos%C3%A9es) :
on multiplie entre elles les dérivées de chaque étape, de la sortie jusqu'au poids
visé.

La rétropropagation est une façon efficace d'appliquer cette règle. En partant de
la sortie, elle réutilise les calculs faits pour une couche quand elle traite la
couche précédente. Le coût total est à peu près celui de deux propagations avant,
quel que soit le nombre de poids. Sans cette économie, il faudrait refaire un
calcul complet pour chaque poids, ce qui serait impraticable pour un grand réseau.

Cette méthode exige que chaque étape du calcul ait une dérivée. C'est la raison
pour laquelle les neurones utilisent une fonction d'activation lisse comme la
[sigmoïde](docs/module3/10-un-neurone/#un-neurone-est-une-régression-logistique),
et non le seuil brusque du perceptron d'origine.
{{% /details %}}
