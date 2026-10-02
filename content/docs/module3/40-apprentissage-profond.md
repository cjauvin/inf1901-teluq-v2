---
title: "L'apprentissage profond"
weight: 40
slug: apprentissage-profond
---

# L'apprentissage profond

D'après le
[théorème d'approximation universelle](docs/module3/20-une-couche-cachee/#plus-de-neurones-plus-de-formes),
une seule couche cachée suffit pour approcher presque n'importe quelle fonction.
Pourtant, les réseaux qui ont transformé l'IA à partir de 2012 comptent des
dizaines de couches. On les appelle des réseaux **profonds**, et leur entraînement,
l'**apprentissage profond** (*deep learning* en anglais). Ce chapitre explique ce
qu'on gagne à empiler les couches, et pourquoi cela n'a fonctionné qu'à partir de
2012.

## Large ou profond

Le théorème dit qu'une couche suffit. Il ne dit pas combien de neurones elle doit
contenir. Pour certains problèmes, ce nombre est si grand que le réseau ne peut
être ni stocké ni entraîné.

Il y a deux façons d'agrandir un réseau. On peut l'élargir, en ajoutant des
neurones à sa couche cachée. On peut l'approfondir, en ajoutant des couches. Les
deux augmentent ce que le réseau peut représenter, mais pas au même coût. Dans un
réseau profond, chaque couche part de ce que la précédente a déjà construit, et le
réutilise. Un réseau large à une seule couche doit tout construire directement à
partir des entrées, sans étape intermédiaire. Pour beaucoup de problèmes, le réseau
profond obtient le même résultat avec beaucoup moins de neurones.

{{< image src="/images/module3/large-ou-profond.svg" alt="Deux réseaux qui ont les mêmes quatre entrées et les mêmes deux sorties. À gauche, un réseau large : une seule couche cachée de douze neurones. À droite, un réseau profond : trois couches cachées de quatre neurones chacune." title="Deux façons d'agrandir un réseau : ajouter des neurones à la couche cachée, ou ajouter des couches." loading="lazy" >}}

## Une hiérarchie de caractéristiques

Le chapitre « [Une couche cachée](docs/module3/20-une-couche-cachee/#ce-que-fait-la-couche-cachée-changer-de-point-de-vue) »
a montré qu'une couche cachée est une fabrique de caractéristiques. Dans un réseau
profond, chaque couche fabrique les siennes à partir de celles de la couche
précédente. Les caractéristiques deviennent plus complexes de couche en couche.

Prenons les chiffres manuscrits. Une première couche peut détecter de petits
traits, à différents endroits et selon différentes orientations. Une deuxième
couche combine ces traits en formes : une boucle, un angle, une barre verticale.
Une troisième combine ces formes en chiffres. Un 9 est une boucle au-dessus d'une
barre, un 8 est fait de deux boucles.

{{< image src="/images/module3/hierarchie-chiffres.svg" alt="Trois colonnes reliées par des traits. À gauche, la première couche détecte des traits simples : horizontal, vertical, oblique, arcs de cercle. Au centre, la deuxième couche les combine en formes : une boucle, une barre verticale, un angle. À droite, la troisième couche combine les formes en chiffres : le 8 est fait de deux boucles, le 9 d'une boucle au-dessus d'une barre." title="Une hiérarchie de caractéristiques : des traits, puis des formes, puis des chiffres." loading="lazy" >}}

Cette description est simplifiée. Personne n'indique au réseau quoi détecter dans
chaque couche. Il le trouve pendant l'entraînement, et les caractéristiques réelles
sont souvent moins nettes que dans ce schéma. Mais quand on examine les couches
d'un réseau entraîné sur des images, on observe bien cette progression, de motifs
simples vers des motifs complexes.

## La fin des caractéristiques fabriquées à la main

Jusqu'en 2012, un système de reconnaissance d'images se construisait en deux
étapes. Des spécialistes concevaient d'abord des caractéristiques : des détecteurs
de contours, de coins, de textures. Ces caractéristiques étaient ensuite données à
un modèle simple, du type de ceux du [Module 2](docs/module2). L'essentiel du
travail, et de la performance, tenait à la première étape. Elle demandait des
années de mise au point pour chaque type de données.

Un réseau profond supprime cette première étape. Il reçoit les pixels bruts, et il
apprend à la fois les caractéristiques et la décision. On parle d'apprentissage
**de bout en bout** (*end-to-end* en anglais). Le travail humain se déplace : il ne
consiste plus à concevoir des caractéristiques, mais à rassembler des données et à
choisir la forme du réseau.

## Pourquoi seulement en 2012

L'idée d'empiler des couches est ancienne, et la
[rétropropagation](docs/module3/30-entrainer-un-reseau/#la-rétropropagation)
s'applique à un réseau de n'importe quelle profondeur. Trois obstacles ont pourtant
bloqué les réseaux profonds pendant plus de vingt ans.

**Le gradient qui s'évanouit.** Pendant la rétropropagation, l'erreur remonte de
couche en couche. Avec la sigmoïde, elle s'affaiblit à chaque couche traversée.
Après quelques couches, il n'en reste presque rien, et les premières couches
n'apprennent plus. Ce problème s'appelle l'**évanouissement du gradient**
(*vanishing gradient*). Un des remèdes est de remplacer la sigmoïde par une
fonction plus simple, la **ReLU** : elle donne 0 quand son entrée est négative, et
laisse passer l'entrée telle quelle quand elle est positive. Avec elle, l'erreur
traverse les couches sans s'affaiblir autant.

{{< image src="/images/module3/sigmoide-relu.svg" alt="Deux graphiques. À gauche, la sigmoïde : une courbe en S, qui plafonne à 0 pour les entrées très négatives et à 1 pour les entrées très positives. À droite, la ReLU : elle vaut 0 pour toute entrée négative, puis monte en ligne droite pour les entrées positives, sans plafond." title="Deux fonctions d'activation : la sigmoïde, qui plafonne des deux côtés, et la ReLU." loading="lazy" >}}

**Les données.** Un réseau profond a des millions de paramètres, et il lui faut des
millions d'exemples. Ils n'existaient pas. En 2009, l'équipe de Fei-Fei Li, à
Stanford, publie **ImageNet** : 14 millions d'images, classées à la main dans plus
de 20 000 catégories. Ce travail a été réalisé par des dizaines de milliers de
personnes, sur la plateforme Mechanical Turk. C'est un exemple de
l'[industrie de l'étiquetage](docs/module2/75-bien-evaluer/#tout-cela-portait-un-nom-lapprentissage-supervisé)
décrite au Module 2.

{{< image src="/images/module3/imagenet-mosaique.jpg" alt="Une mosaïque de plusieurs centaines de petites photos très variées : véhicules, bâtiments, objets du quotidien, aliments, personnes, et de nombreux animaux. Les photos qui se ressemblent sont regroupées : les véhicules en haut, les chiens en bas à droite, les insectes et les oiseaux en bas." title="Quelques centaines d'images d'ImageNet. Elles sont disposées par un réseau profond, qui a placé côte à côte celles qu'il juge semblables (image : Andrej Karpathy)." loading="lazy" >}}

**Le calcul.** Entraîner un réseau profond sur des millions d'images demande une
quantité de calculs hors de portée des processeurs des années 2000. La solution est
venue du jeu vidéo. Les **processeurs graphiques** (GPU) sont conçus pour exécuter
en parallèle des milliers de calculs identiques, et les calculs d'un réseau de
neurones sont de ce type. Un GPU entraîne un réseau des dizaines de fois plus vite
qu'un processeur ordinaire. Des bibliothèques logicielles, comme PyTorch et
TensorFlow, ont ensuite automatisé la rétropropagation : on décrit le réseau, et le
calcul des corrections est fait par la bibliothèque.

## 2012 : le concours ImageNet

À partir de 2010, ImageNet sert de base à un concours annuel. Il faut classer des
images parmi 1 000 catégories, après un entraînement sur 1,2 million d'exemples.
Une réponse est comptée comme une erreur si la bonne catégorie ne figure pas parmi
les cinq propositions du système.

En 2010 et 2011, les meilleurs systèmes reposent sur des caractéristiques
fabriquées à la main, et leur taux d'erreur est de 28 %, puis de 26 %. En 2012,
Alex Krizhevsky, Ilya Sutskever et Geoffrey Hinton, de l'Université de Toronto,
présentent un réseau profond, **AlexNet**. Il compte huit couches et 60 millions de
paramètres, il utilise la ReLU, et il a été entraîné pendant environ une semaine
sur deux GPU. Son taux d'erreur est de 15 %. Le deuxième système est à 26 %.

{{< image src="/images/module3/imagenet-erreur.svg" alt="Un diagramme à barres. En 2010 et 2011, les systèmes gagnants reposent sur des caractéristiques fabriquées à la main : 28,2 % puis 25,8 % d'erreur. En 2012, le réseau profond AlexNet obtient 15,3 %. Les gagnants suivants sont tous des réseaux profonds : 11,7 % en 2013, 6,7 % en 2014, 3,6 % en 2015, 3,0 % en 2016 et 2,3 % en 2017. Une ligne horizontale marque le niveau humain, estimé à 5 %, dépassé à partir de 2015." title="Le taux d'erreur du système gagnant au concours ImageNet, de 2010 à 2017." loading="lazy" >}}

L'écart est si grand que le domaine change de méthode en deux ans. Dès 2014, tous
les systèmes en compétition sont des réseaux profonds. En 2015, le réseau gagnant
compte 152 couches et son taux d'erreur, 3,6 %, est inférieur à celui d'un humain
sur la même tâche, estimé à 5 %. La même bascule se produit ensuite pour la
reconnaissance de la parole, puis pour la traduction.

AlexNet est un réseau d'un type particulier, un réseau convolutif, conçu pour les
images. Le chapitre suivant lui est consacré.
