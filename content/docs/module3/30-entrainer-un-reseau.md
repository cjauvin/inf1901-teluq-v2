---
title: "Entraîner un réseau"
weight: 30
slug: entrainer-un-reseau
---

# Entraîner un réseau

Le chapitre « [Une couche cachée](docs/module3/20-une-couche-cachee/#qui-règle-tous-ces-poids) »
s'est terminé sur un réseau de près de 24 000 poids, que personne ne
peut régler à la main. Ce chapitre explique comment un réseau règle lui-même ses
poids, à partir d'exemples.

## Le même principe qu'au Module 2

La méthode a déjà été présentée dans
« [Apprendre, c'est descendre la pente](docs/module2/50-entrainer-un-modele/#apprendre-cest-descendre-la-pente) ».
Elle tient en trois étapes, qu'on répète :

1. on mesure l'**erreur** du modèle sur des exemples dont on connaît la bonne
   réponse ;
2. on cherche dans quel sens modifier chaque paramètre pour que l'erreur diminue ;
3. on modifie un peu chaque paramètre dans ce sens.

C'est la **descente de gradient**. Pour la droite du Module 2,
il y avait deux paramètres, et l'erreur formait un paysage qu'on pouvait dessiner.
Pour un réseau, les paramètres sont les poids et les biais. Le paysage a alors des
milliers de dimensions et on ne peut plus le dessiner, mais la méthode reste la
même : mesurer la pente, puis faire un pas vers le bas.

Pour un réseau qui classe, l'erreur mesurée est en général la même que celle de la
régression logistique. La réduire revient à rendre les bonnes réponses aussi
probables que possible : c'est le
[maximum de vraisemblance](docs/module2/60-classer/#sous-les-modèles-des-probabilités)
(*maximum likelihood*) présenté au Module 2.

## Le problème des couches cachées

La deuxième étape est simple pour un neurone seul. On connaît la bonne réponse, on
voit donc directement si sa sortie est trop haute ou trop basse, et on corrige ses
poids en conséquence. C'est ce que faisait le perceptron dès 1958.

Dans un réseau, cela ne vaut que pour la couche de sortie. Pour un
neurone caché, les exemples ne donnent aucune bonne réponse. Reprenons le
[réseau du XOR](docs/module3/20-une-couche-cachee/#le-xor-résolu-avec-trois-neurones) :
la table de vérité dit ce que la sortie doit valoir, mais elle ne
dit pas que le premier neurone caché doit répondre à la question « au moins une ? ».
Quand le réseau se trompe, on ne sait pas quel neurone caché est en cause, ni dans
quel sens le corriger.

Ce problème s'appelle l'**attribution de la responsabilité** (*credit assignment*
en anglais). C'est lui qui a arrêté la recherche sur les réseaux de neurones après
[1969](docs/module1/60-hivers/#le-premier-hiver-la-mort-du-perceptron-1969) : on
savait qu'une couche cachée était nécessaire, et on ne savait pas
l'entraîner.

## La rétropropagation

La solution consiste à calculer la responsabilité de chaque poids en partant de la
sortie et en remontant vers l'entrée. Pour chaque exemple, le calcul se fait en
deux temps.

**La propagation avant** (*forward pass*). L'exemple entre dans le réseau. Chaque
couche calcule ses sorties et les passe à la suivante, jusqu'à la réponse du réseau.
On compare cette réponse à la bonne, ce qui donne l'erreur. Les poids sont utilisés,
mais pas modifiés.

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
[règle de dérivation en chaîne](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_d%C3%A9rivation_des_fonctions_compos%C3%A9es)
(*chain rule*) : on multiplie entre elles les dérivées de chaque étape, de la sortie
jusqu'au poids visé.

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

## Un réseau qui apprend le XOR

L'applet ci-dessous reprend le réseau du XOR, avec ses deux neurones cachés. Les
poids de départ sont tirés au hasard. Quand vous lancez l'entraînement, le réseau
voit les quatre cas en boucle et corrige ses poids par rétropropagation. Les deux
droites sont celles des neurones cachés, comme dans
[l'applet du chapitre précédent](docs/module3/20-une-couche-cachee/#deux-droites-à-déplacer),
mais cette fois personne ne les déplace.

{{< applet src="/html/applets/xor-entrainement.html" height="561" >}}

1. Lancez l'entraînement. Observez les droites se placer et l'erreur descendre.
2. Repartez de nouveaux poids de départ, plusieurs fois, avec le bouton « Nouveaux
   poids ». Le réseau ne trouve pas toujours la même solution, et il lui arrive de
   rester bloqué avec une erreur élevée, environ une fois sur cinq.
3. Changez le taux d'apprentissage. S'il est très petit, l'apprentissage est très
   lent. S'il est trop grand, l'erreur oscille ou reste élevée, au lieu de
   descendre.

La deuxième manipulation montre une différence avec la droite du Module 2. Le
paysage d'erreur (*loss landscape*) d'un réseau n'est pas une cuvette unique. Il
comporte plusieurs creux, et la descente s'arrête dans celui qu'elle rencontre, qui
dépend du point de départ. Pour les grands réseaux, on constate en pratique que la
plupart des creux donnent des résultats comparables.

## 1986

La rétropropagation a été découverte plusieurs fois. Paul Werbos la décrit dans sa
thèse en 1974, sans que le résultat soit remarqué. En 1986, David Rumelhart,
Geoffrey Hinton et Ronald Williams publient dans la revue *Nature* un article qui
montre, expériences à l'appui, qu'un réseau entraîné de cette façon construit
lui-même des caractéristiques utiles dans ses couches cachées. C'est
cet article qui impose la méthode.

La question ouverte en
[1969](docs/module1/60-hivers/#le-premier-hiver-la-mort-du-perceptron-1969) est
alors réglée. Le XOR, que le perceptron ne pouvait pas apprendre, est appris par un
réseau à couche cachée. Les réseaux de neurones redeviennent un sujet de recherche
actif, sous le nom de **connexionnisme**.

Ce retour reste limité pendant une vingtaine d'années. Les réseaux de l'époque
sont petits, les données rares et les ordinateurs lents. D'autres méthodes
progressent plus vite. La plus influente est la
[machine à vecteurs de support](docs/module2/60-classer/#la-plus-grande-marge-les-machines-à-vecteurs-de-support) (SVM),
présentée au Module 2, dont la forme actuelle date de 1995. Grâce à
l'[astuce du noyau](docs/module2/70-generaliser/#ajouter-des-dimensions-sans-les-calculer-lastuce-du-noyau)
(*kernel trick*), elle trace des frontières courbes sans avoir à fabriquer de
caractéristiques. Son entraînement a un avantage décisif sur celui d'un réseau : il
n'y a qu'un seul creux dans le paysage d'erreur, et on est donc sûr de trouver la
meilleure solution, quel que soit le point de départ. La deuxième manipulation de
l'applet ci-dessus montre que ce n'est pas le cas pour un réseau. Le *boosting* et
les
[forêts aléatoires](docs/module2/65-arbres-de-decision/#ce-quun-arbre-dit-et-ce-quil-tait)
(*random forests*) complètent cette boîte à outils. Jusqu'au début des années 2010,
ces méthodes l'emportent souvent sur les réseaux de neurones, et les grandes
conférences du domaine publient peu de travaux sur ces derniers. Le chapitre suivant
explique ce qui a changé ensuite.

## L'entraînement en pratique

Quelques termes reviennent dans la suite du cours.

- Un **lot** (*batch* en anglais) est un petit groupe d'exemples traités ensemble.
  On ne corrige pas les poids après chaque exemple, ni après le jeu complet, mais
  après chaque lot.
- Une **époque** (*epoch*) est un passage complet sur tous les exemples
  d'entraînement. Un entraînement compte en général plusieurs époques.
- Le **taux d'apprentissage** (*learning rate*) règle la taille de chaque
  correction, comme au
  [Module 2](docs/module2/50-entrainer-un-modele/#apprendre-cest-descendre-la-pente).

Il faut aussi distinguer deux phases dans la vie d'un réseau.

- L'**entraînement** (*training*) règle les poids. Il demande beaucoup de calculs,
  parce qu'il répète l'aller et le retour sur des millions d'exemples. Il est fait
  une fois.
- L'**inférence** est l'utilisation du réseau entraîné. Les poids ne changent plus,
  et seule la propagation avant est exécutée. Elle est faite à chaque utilisation.

Cette distinction reviendra au Module 4 : entraîner un grand modèle de langage
(*large language model*) prend des semaines ou des mois, alors qu'une réponse est
produite en quelques secondes.

Un réseau a beaucoup de paramètres, et il est donc très exposé au sur-apprentissage
(*overfitting*). Les remèdes sont ceux de
« [Généraliser](docs/module2/70-generaliser/#garder-un-modèle-riche-mais-le-tenir-en-laisse-la-régularisation) » :
un jeu de test (*test set*), et la régularisation. Pour les réseaux, la
régularisation prend trois formes courantes. Le *weight decay* pénalise les poids
trop grands. Le *dropout* désactive au hasard une partie des neurones à chaque étape
de l'entraînement. L'**arrêt précoce** (*early stopping*) interrompt l'entraînement
quand l'erreur sur des exemples mis de côté cesse de diminuer.

## Pour voir le mécanisme en détail

La chaîne 3Blue1Brown, de Grant Sanderson, propose une série de vidéos sur les
réseaux de neurones, construite sur l'exemple des chiffres manuscrits. Les
explications sont visuelles et progressives. La vidéo ci-dessous porte sur la
rétropropagation.

{{< youtube id="Ilg3gGewQ5U" >}}

Deux autres vidéos de la série complètent ce chapitre :
[la première](https://www.youtube.com/watch?v=aircAruvnKk) présente la structure
d'un réseau, et [la deuxième](https://www.youtube.com/watch?v=IHZwWFHWa-w) la
descente de gradient. Les vidéos sont en anglais.

On sait maintenant entraîner un réseau à une couche cachée. Le chapitre suivant,
« [L'apprentissage profond](docs/module3/40-apprentissage-profond) », examine ce qu'on gagne à empiler plusieurs couches.
