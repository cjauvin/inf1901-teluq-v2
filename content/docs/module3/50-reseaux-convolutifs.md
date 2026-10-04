---
title: "Voir : les réseaux convolutifs"
weight: 50
slug: reseaux-convolutifs
---

# Voir : les réseaux convolutifs

Le réseau des chiffres du chapitre
« [Une couche cachée](docs/module3/20-une-couche-cachee/#plus-de-neurones-plus-de-formes) »
reçoit les 784 pixels d'une image comme une simple liste de nombres. Il ne sait pas
que ces pixels forment une grille, ni que deux pixels voisins sont liés. Ce
chapitre présente une forme de réseau qui tient compte de la disposition des
pixels, le **réseau convolutif**.

## Ce qu'un réseau ordinaire ignore dans une image

Un réseau dont chaque neurone est relié à toutes les entrées pose trois problèmes
quand ces entrées sont les pixels d'une image.

**Il ignore le voisinage.** Supposons qu'on mélange les pixels de toutes les
images, toujours de la même façon. Pour nous, les chiffres deviennent illisibles.
Pour ce réseau, rien ne change : il apprend aussi bien qu'avant. Il n'utilise donc
pas le fait que des pixels voisins forment ensemble un trait ou une courbe.

**Il ne reconnaît pas un motif déplacé.** Si un chiffre est décalé de quelques
pixels, il active d'autres entrées, reliées à d'autres poids. Pour le
réseau, c'est une image nouvelle. Il doit apprendre séparément le même chiffre à
chaque position.

{{< image src="/images/module3/chiffre-decale.svg" alt="En haut, deux grilles de 10 pixels sur 10. La première montre un « 1 » à gauche, la seconde le même « 1 » décalé de trois pixels vers la droite. En bas, chaque grille est mise à plat en une liste de 100 pixels, rangée après rangée. Les pixels allumés n'occupent pas les mêmes places dans les deux listes." title="Le même chiffre à deux positions : une fois mises à plat, les deux images n'ont presque aucun pixel allumé en commun." loading="lazy" >}}

**Il a trop de poids.** Une photo en couleur de 1 000 pixels sur 1 000 compte trois
millions de valeurs. Avec une couche cachée de 1 000 neurones, il
faudrait trois milliards de poids pour cette seule couche.

## Le filtre

La solution repose sur un petit élément, le **filtre** (*filter* ou *kernel*). Un
filtre est un carré de poids, par exemple de 3 sur 3. On le pose sur un coin de
l'image, où il recouvre neuf pixels. Il calcule la somme de ces neuf pixels, chacun
multiplié par le poids qui le recouvre. C'est le calcul d'un
[neurone](docs/module3/10-un-neurone/#un-neurone-est-une-régression-logistique),
limité à neuf entrées.

On fait ensuite glisser le filtre d'un pixel, et on recommence, jusqu'à avoir
parcouru toute l'image. Chaque position donne un nombre. Ensemble, ces nombres
forment une nouvelle image, presque de la même taille que la première. Cette
opération s'appelle une **convolution**.

La nouvelle image indique où se trouve le motif que le filtre détecte. Un filtre
dont la colonne du centre a des poids positifs et les colonnes voisines des poids
négatifs donne une somme élevée là où l'image contient un trait vertical, et une
somme faible ou négative ailleurs.

{{% details "Pour aller plus loin : le calcul à une position" %}}
Prenons le filtre des traits verticaux, et une zone de l'image où passe un trait
vertical. Les pixels du trait valent 1, les autres 0.

| Filtre | | | | Pixels | | |
|:---:|:---:|:---:|---|:---:|:---:|:---:|
| −1 | 2 | −1 | | 0 | 1 | 0 |
| −1 | 2 | −1 | | 0 | 1 | 0 |
| −1 | 2 | −1 | | 0 | 1 | 0 |

La somme vaut 2 + 2 + 2 = 6, la valeur la plus élevée possible pour ce filtre. Si
la même zone contient un trait horizontal, les pixels de la rangée du milieu valent
1. La somme vaut alors −1 + 2 − 1 = 0, et le filtre ne détecte rien.
{{% /details %}}

## Un filtre à manipuler

Dans l'applet ci-dessous, l'image d'un chiffre est à gauche, le filtre au centre,
et le résultat de la convolution à droite. Plus une case du résultat est foncée,
plus le motif du filtre est présent à cet endroit. Les sommes négatives sont
ramenées à zéro.

{{< applet src="/html/applets/convolution.html" height="548" >}}

1. Choisissez le chiffre 7, puis comparez les filtres « traits verticaux »,
   « traits horizontaux » et « obliques / ». Chacun fait ressortir une partie
   différente du chiffre.
2. Passez la souris sur l'image. Le carré rouge montre les neuf pixels recouverts
   par le filtre, et la somme obtenue s'affiche sous le filtre.
3. Déplacez le chiffre avec les flèches. Le résultat se déplace avec lui, sans
   changer de forme.
4. Modifiez vous-même les neuf poids du filtre, et observez l'effet.

## Ce que la convolution apporte

Le filtre répond aux trois problèmes de départ.

- **Le voisinage.** Le filtre ne regarde que neuf pixels voisins à la fois. Il est
  fait pour détecter des motifs locaux.
- **Le déplacement.** Le même filtre parcourt toute l'image. Un trait vertical est
  détecté de la même façon en haut à gauche et en bas à droite, comme le montrait
  la troisième manipulation.
- **Le nombre de poids.** Un filtre de 3 sur 3 a neuf poids, que l'image compte 784
  pixels ou trois millions. Les mêmes poids servent à toutes les positions. On
  parle de **partage des poids** (*weight sharing*).

## Du filtre au réseau

Un réseau convolutif est fait de plusieurs éléments, répétés.

Une **couche convolutive** (*convolutional layer*) contient plusieurs filtres, par
exemple 32. Chacun détecte un motif différent et produit sa propre image de
résultat. La couche transforme donc une image en 32 images.

Une étape de **réduction** (*pooling* en anglais) diminue ensuite la taille de ces
images. La méthode la plus courante découpe l'image en carrés de 2 sur 2 et ne
garde que la valeur la plus élevée de chaque carré. L'image devient deux fois plus
petite dans chaque direction. On conserve l'information « ce motif est présent dans
cette zone », et on perd sa position exacte.

On répète ces deux étapes plusieurs fois. Les filtres de la deuxième couche ne
s'appliquent plus aux pixels, mais aux résultats de la première. Ils combinent donc
des traits en formes. Ceux de la troisième combinent des formes en parties
d'objets. C'est la
[hiérarchie de caractéristiques](docs/module3/40-apprentissage-profond/#une-hiérarchie-de-caractéristiques)
du chapitre « L'apprentissage profond », obtenue ici par construction.

À la fin, les dernières images sont petites et nombreuses. On les donne à un réseau
ordinaire, à quelques couches, qui produit la réponse.

{{< image src="/images/module3/architecture-convolutive.svg" alt="De gauche à droite : l'image d'un chiffre ; une couche convolutive, représentée par une pile d'images de même taille ; une réduction, qui donne une pile d'images plus petites ; une seconde couche convolutive et une seconde réduction ; puis un réseau ordinaire et les dix sorties." title="L'architecture d'un réseau convolutif : convolutions et réductions en alternance, puis un réseau ordinaire." loading="lazy" >}}

Il reste un point essentiel. Dans l'applet, les filtres étaient choisis à la main.
Dans un réseau convolutif, personne ne les choisit. Les poids des filtres sont
tirés au hasard au départ, puis réglés par
[rétropropagation](docs/module3/30-entrainer-un-reseau/#la-rétropropagation), comme tous les autres poids. Le réseau trouve lui-même les
motifs utiles pour sa tâche. Entraîné sur des visages, il produit des filtres
adaptés aux visages. Entraîné sur des radiographies, il en produit d'autres.

## Yann Le Cun et les chèques

L'idée du filtre qui glisse sur l'image vient de la neurophysiologie. En 1979, le
chercheur japonais Kunihiko Fukushima s'inspire des travaux de Hubel et Wiesel sur
le cortex visuel, décrits dans
l'[encadré du chapitre précédent](docs/module3/40-apprentissage-profond/#une-hiérarchie-de-caractéristiques).
Il propose le **Neocognitron**, un réseau qui alterne déjà des couches de filtres
et des couches de réduction. Ses filtres ne sont pas réglés par rétropropagation,
qui n'est pas encore connue.

En 1988, le chercheur français Yann Le Cun entre aux Bell Labs, le laboratoire de
recherche de l'entreprise de télécommunications AT&T, dans le New Jersey. Il y
réunit les deux idées : un réseau convolutif, dont tous les filtres sont appris par
rétropropagation. En 1989, ce réseau lit les codes postaux manuscrits des lettres
du service postal américain.

{{< image src="/images/module3/yann-le-cun.jpg" alt="Portrait de Yann Le Cun, un homme aux cheveux gris, souriant, en veste sombre." title="Yann Le Cun en 2018 (photo : Jérémy Barande, Wikimedia Commons, CC BY-SA 2.0)." loading="lazy" >}}

La vidéo ci-dessous, publiée par Le Cun lui-même, montre ce réseau en 1989, lisant
en direct des chiffres écrits à la main.

{{< youtube id="FwFduRA_L6Q" >}}

Le travail se poursuit pendant une dizaine d'années, avec Léon Bottou, Yoshua
Bengio et Patrick Haffner. Il aboutit en 1998 à **LeNet-5**, un réseau à sept
couches, et à un système de lecture automatique des chèques. Vers la fin des années
1990, selon Le Cun, ce système lit entre 10 et 20 % des chèques déposés aux
États-Unis. C'est l'une des premières applications commerciales à grande échelle
d'un réseau de neurones.

Pour entraîner et comparer ces réseaux, l'équipe constitue une base de chiffres
manuscrits, **MNIST** : 60 000 images d'entraînement et 10 000 images de test, de
28 pixels sur 28. C'est l'origine des chiffres qui servent d'exemple tout au long
de ce module. MNIST est devenue la base d'essai (*benchmark*) la plus utilisée de
l'apprentissage automatique (*machine learning*).

{{< image src="/images/module3/mnist-exemples.png" alt="Une grille de petits chiffres manuscrits, blancs sur fond noir, rangés par ligne de 0 à 9. Chaque chiffre est écrit par une personne différente, avec des formes et des inclinaisons variées." title="Des chiffres de la base MNIST, une ligne par chiffre (image : Josef Steppan, Wikimedia Commons, CC BY-SA 4.0)." loading="lazy" >}}

Malgré ces succès, les réseaux convolutifs restent une méthode parmi d'autres
pendant quinze ans. Ils fonctionnent sur de petites images de chiffres, mais les
photos du monde réel demandent des réseaux plus grands, plus de données et plus de
calcul. Il faut attendre que ces trois conditions, décrites dans
« [Pourquoi seulement en 2012](docs/module3/40-apprentissage-profond/#pourquoi-seulement-en-2012) »,
soient réunies.

## Après 2012

[AlexNet](docs/module3/40-apprentissage-profond/#2012-le-concours-imagenet) est un
réseau convolutif. Son architecture reprend celle de LeNet, avec trois différences :
il est beaucoup plus grand, il utilise la ReLU, et il est entraîné sur GPU. Le Cun,
Hinton et Bengio ont reçu ensemble le prix Turing 2018, la plus haute distinction
en informatique, pour leurs travaux sur l'apprentissage profond.

Les réseaux convolutifs deviennent ensuite plus profonds : 8 couches pour AlexNet
en 2012, 22 pour GoogLeNet en 2014, 152 pour ResNet en 2015. Ce dernier introduit
des **raccourcis** (*skip connections*) qui laissent l'information sauter certaines
couches, ce qui limite
l'[évanouissement du gradient](docs/module3/40-apprentissage-profond/#pourquoi-seulement-en-2012) et permet d'entraîner des réseaux très profonds.

Ils servent aujourd'hui à de nombreuses tâches :

- **reconnaître et localiser des objets** (*object detection*) dans une image, par
  exemple les piétons et les autres véhicules pour l'aide à la conduite ;
- **analyser des images médicales**, comme des radiographies ou des images de la
  rétine ;
- **reconnaître des visages** (*face recognition*), un usage qui pose des questions
  de surveillance et de vie privée, traitées au [Module 5](docs/module5) ;
- **traiter des sons**, en les transformant d'abord en images de leurs fréquences.

## La leçon de la convolution

Ce chapitre nuance la
[leçon amère](docs/module3/40-apprentissage-profond/#la-leçon-amère) de Sutton. La
convolution est une connaissance humaine, inscrite dans la forme du réseau : dans
une image, ce qui compte est d'abord local, et un même motif peut apparaître
n'importe où. Le réseau convolutif doit une grande partie de son efficacité à cette
connaissance.

Mais c'est une connaissance très générale. Elle porte sur la structure des images
en général, et non sur les chats, les chiffres ou les visages. Le contenu des
filtres reste entièrement appris. C'est le type de savoir humain qui a survécu à
l'apprentissage profond : non pas des règles sur le monde, mais des hypothèses sur
la forme des données.

Le chapitre suivant applique la même démarche à un autre type de données. Une image
a une taille fixe, et tous ses pixels sont disponibles en même temps. Une phrase ou
un enregistrement sonore ont une longueur variable, et l'ordre de leurs éléments
compte. Le chapitre « [Lire une séquence : les réseaux récurrents](docs/module3/60-reseaux-recurrents) » présente les
réseaux conçus pour ces données.
