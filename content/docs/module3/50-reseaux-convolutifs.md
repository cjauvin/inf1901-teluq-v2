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
pixels, il active d'autres entrées, reliées à d'autres poids. Pour le réseau, c'est
une image nouvelle. Il doit apprendre séparément le même chiffre à chaque position.

{{< image src="/images/module3/chiffre-decale.svg" alt="En haut, deux grilles de 10 pixels sur 10. La première montre un « 1 » à gauche, la seconde le même « 1 » décalé de trois pixels vers la droite. En bas, chaque grille est mise à plat en une liste de 100 pixels, rangée après rangée. Les pixels allumés n'occupent pas les mêmes places dans les deux listes." title="Le même chiffre à deux positions : une fois mises à plat, les deux images n'ont presque aucun pixel allumé en commun." loading="lazy" >}}

**Il a trop de poids.** Une photo en couleur de 1 000 pixels sur 1 000 compte trois
millions de valeurs. Avec une couche cachée de 1 000 neurones, il faudrait trois
milliards de poids pour cette seule couche.

## Le filtre

La solution repose sur un petit élément, le **filtre**. Un filtre est un carré de
poids, par exemple de 3 sur 3. On le pose sur un coin de l'image, où il recouvre
neuf pixels. Il calcule la somme de ces neuf pixels, chacun multiplié par le poids
qui le recouvre. C'est le calcul d'un
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
  parle de **partage des poids**.

## Du filtre au réseau

Un réseau convolutif est fait de plusieurs éléments, répétés.

Une **couche convolutive** contient plusieurs filtres, par exemple 32. Chacun
détecte un motif différent et produit sa propre image de résultat. La couche
transforme donc une image en 32 images.

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
[rétropropagation](docs/module3/30-entrainer-un-reseau/#la-rétropropagation),
comme tous les autres poids. Le réseau trouve lui-même les motifs utiles pour sa
tâche. Entraîné sur des visages, il produit des filtres adaptés aux visages.
Entraîné sur des radiographies, il en produit d'autres.
