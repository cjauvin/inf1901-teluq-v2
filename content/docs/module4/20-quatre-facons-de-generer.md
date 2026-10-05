---
title: "Quatre façons de générer"
weight: 20
slug: quatre-facons-de-generer
---

# Quatre façons de générer

Le chapitre « [Générer : imiter une distribution](docs/module4/10-generer) » a posé
le problème. Un modèle génératif doit apprendre la distribution de données très
complexes, comme des photos de visages, puis y tirer de nouveaux exemples. Pour
des images, cette distribution occupe une portion infime d'un espace immense, et
on ne peut pas la décrire en additionnant des cloches.

Depuis le début des années 2010, quatre familles de méthodes ont été proposées
pour résoudre ce problème. Chacune repose sur une idée différente, et chacune a
produit des systèmes marquants. Ce chapitre les présente l'une après l'autre, avec
leurs forces et leurs limites. Les quatre utilisent des réseaux de neurones, et
toutes s'entraînent par
[rétropropagation](docs/module3/30-entrainer-un-reseau/#la-rétropropagation),
comme les réseaux du [Module 3](docs/module3).

## Le faussaire et l'expert : les réseaux antagonistes génératifs

En 2014, Ian Goodfellow, alors doctorant à l'Université de Montréal dans le
laboratoire de Yoshua Bengio, propose une idée nouvelle avec ses collègues, les
**réseaux antagonistes génératifs** (*generative adversarial networks*, GAN). Elle
est issue de l'[école canadienne](docs/module3/40-apprentissage-profond/#2012-le-concours-imagenet)
de l'apprentissage profond présentée au Module 3.

Un GAN fait travailler deux réseaux l'un contre l'autre.

- Le **générateur** joue le rôle d'un faussaire. Il reçoit quelques nombres tirés
  au hasard, et il en fait une image.
- Le **discriminateur** joue le rôle d'un expert. Il reçoit une image, tantôt une
  vraie, tantôt une fausse produite par le générateur, et il doit dire laquelle
  c'est.

{{< image src="/images/module4/gan.svg" alt="Un schéma. En bas à gauche, des nombres tirés au hasard entrent dans le générateur, qui produit une image fausse. En haut, des vraies images. Les vraies images et l'image fausse entrent toutes deux dans le discriminateur, qui répond « vraie » ou « fausse ». Deux flèches pointillées repartent de ce verdict : l'une vers le discriminateur, qui apprend à mieux distinguer, l'autre vers le générateur, qui apprend à mieux tromper." title="Un réseau antagoniste génératif. Les deux réseaux s'entraînent ensemble, chacun à partir des erreurs de l'autre." loading="lazy" >}}

Les deux réseaux s'entraînent ensemble. Chaque fois que l'expert se trompe, il
ajuste ses poids pour mieux distinguer les vraies images des fausses. Chaque fois
que l'expert démasque une fausse image, le faussaire ajuste ses poids pour que ses
prochaines images trompent mieux l'expert. Au fil de l'entraînement, l'expert
devient plus exigeant, et le faussaire doit produire des images de plus en plus
réalistes pour le tromper. À la fin, on garde le faussaire.

Le discriminateur est un classificateur **discriminatif**, au sens du chapitre
« [Classer](docs/module2/60-classer/#renverser-le-problème-la-classification-bayésienne) »
du Module 2. Il trace une frontière entre les vraies images et les fausses. Un GAN
utilise donc un modèle discriminatif pour entraîner un modèle génératif.

Les GAN ont dominé la génération d'images pendant plusieurs années. En 2014, ils
produisaient des visages flous de quelques dizaines de pixels de côté. En 2019,
StyleGAN produisait les visages photoréalistes présentés au
[chapitre précédent](docs/module4/10-generer). Ils ont cependant deux défauts.

- Leur entraînement est **instable**. Les deux réseaux doivent progresser au même
  rythme. Si l'expert devient trop fort trop vite, le faussaire ne reçoit plus
  d'indication utile et cesse de progresser.
- Le faussaire peut se contenter de produire **quelques images** qui trompent bien
  l'expert, plutôt que toute la variété des données. Un GAN entraîné sur des
  chiffres peut ainsi ne produire que des 1 et des 7. Ce défaut s'appelle
  l'**effondrement des modes** (*mode collapse*).

## Remplir l'espace latent : les autoencodeurs variationnels

L'applet du [chapitre précédent](docs/module4/10-generer/#lespace-latent) utilise un
**autoencodeur variationnel** (*variational autoencoder*, VAE), proposé en 2013 par
Diederik Kingma et Max Welling, à l'Université d'Amsterdam. Comme l'autoencodeur du
[Module 3](docs/module3/40-apprentissage-profond/#apprendre-sans-étiquettes-lautoencodeur),
c'est un réseau en sablier, avec un encodeur et un décodeur. Il diffère de
l'autoencodeur ordinaire sur deux points.

1. L'encodeur ne place pas chaque image en un point précis de l'espace latent, mais
   dans une petite **zone floue** autour de ce point. Pendant l'entraînement, le
   décodeur reçoit un point tiré au hasard dans cette zone, et doit quand même
   reconstruire l'image. Il apprend ainsi à produire une image correcte pour tous
   les points voisins, et pas seulement pour un point isolé.
2. Une **pénalité** est ajoutée à l'erreur. Elle augmente quand les zones
   s'éloignent du centre de la carte ou deviennent trop petites. Toutes les zones
   sont donc ramenées autour du centre, où elles se chevauchent sans laisser de
   trous.

Le résultat est un espace latent organisé selon une distribution connue à
l'avance, une cloche centrée sur l'origine. Pour générer une image, il suffit de
tirer un point dans cette cloche et de le décoder. La figure ci-dessous compare
deux réseaux entraînés sur les mêmes chiffres de MNIST, un autoencodeur ordinaire
et le VAE de l'applet du chapitre précédent. Dans les deux cartes, dix points sont
tirés selon la même règle, dans la cloche centrée sur l'origine.

{{< image src="/images/module4/ae-vae.png" alt="Deux cartes de l'espace latent, côte à côte, avec dessous les dix chiffres produits par chacun des deux décodeurs. À gauche, l'autoencodeur ordinaire : ses chiffres s'étalent sur une très grande surface, et le cercle de tirage, minuscule, ne couvre qu'un coin où se mêlent des 3, des 5 et des 9 ; les dix chiffres produits sont presque tous des 3, des 5 et des 9. À droite, le VAE : ses chiffres sont regroupés autour du centre, le cercle de tirage couvre presque toute la carte, et les dix chiffres produits sont variés (8, 2, 7, 5, 4, 3, 6)." title="Avec la même règle de tirage, l'autoencodeur ordinaire ne produit presque que des 3, des 5 et des 9, car ses chiffres ne sont pas rangés autour du centre. Le VAE produit des chiffres variés." loading="lazy" >}}

L'autoencodeur ordinaire a rangé ses chiffres n'importe où, sur une très grande
surface. Le cercle de tirage n'en couvre qu'un petit coin, et les chiffres produits
se ressemblent tous. Il faudrait connaître la forme exacte de sa carte pour savoir
où tirer. Le VAE, lui, a rangé ses chiffres là où l'on tire.

Les VAE s'entraînent de façon stable, et leur espace latent est bien organisé. Leur
défaut principal se voit dans l'applet du chapitre précédent : leurs images sont
**floues**. Quand le décodeur hésite entre plusieurs images possibles, il produit
une moyenne de ces images, et une moyenne d'images est floue.

## Retirer le bruit pas à pas : la diffusion

La troisième famille part d'une observation simple. Il est facile de détruire une
image : il suffit de lui ajouter un peu de bruit, puis encore un peu, des centaines
de fois, jusqu'à ce qu'il ne reste qu'une neige où l'image d'origine a disparu.
Cette destruction ne demande aucun apprentissage. Un **modèle de diffusion**
(*diffusion model*) apprend l'opération inverse, c'est-à-dire retirer un peu de
bruit à la fois.

{{< image src="/images/module4/diffusion-visage.jpg" alt="Cinq versions du même visage, de gauche à droite, de plus en plus bruitées : l'image nette à l'étape 0, un léger grain à l'étape 60, un grain fort à l'étape 180, un visage à peine visible à l'étape 400, et une neige colorée sans aucune forme à l'étape 1 000. Une flèche orientée vers la droite indique « ajouter du bruit, étape par étape (sans apprentissage) ». Une flèche orientée vers la gauche indique « retirer du bruit, étape par étape : c'est ce que le réseau apprend »." title="Un visage brouillé en 1 000 étapes, selon le calendrier de bruit utilisé par Ho, Jain et Abbeel en 2020. Un modèle de diffusion apprend à parcourir ce chemin dans l'autre sens." loading="lazy" >}}

L'entraînement se fait ainsi. On prend une image du jeu de données, on la brouille
jusqu'à une étape choisie au hasard, et on demande au réseau d'estimer le bruit qui
a été ajouté. Comme on a soi-même ajouté ce bruit, on connaît la bonne réponse :
c'est un cas d'[auto-supervision](docs/module2/80-trois-facons-d-apprendre/#fabriquer-soi-même-ses-réponses-lauto-supervision),
comme l'autoencodeur. Le réseau qui estime le bruit est le plus souvent un
[U-Net](docs/module3/50-reseaux-convolutifs/#après-2012), le réseau convolutif
présenté au Module 3, et plus récemment un Transformer.

Pour générer une image, on part d'une neige nouvelle, tirée au hasard. Le réseau
estime le bruit qu'elle contient, et on en retire une petite partie. On recommence
avec l'image obtenue, des dizaines ou des centaines de fois. À chaque étape, une
forme se précise, et à la fin il reste une image nette, que personne n'a jamais
vue.

L'applet ci-dessous montre un modèle de diffusion entraîné sur des données beaucoup
plus simples que des images. Chaque exemple n'est qu'un point du plan, et les
exemples d'entraînement sont des milliers de points tirés dans la feuille d'érable
du drapeau du Canada. Le principe est exactement le même que pour des images de
millions de pixels.

{{< applet src="/html/applets/diffusion.html" height="614" >}}

Quelques manipulations à faire :

1. Cliquez sur « Brouiller la feuille ». Les points s'écartent de la feuille, étape
   par étape, jusqu'à former un nuage informe. Les six points suivis font chacun
   une marche au hasard.
2. Cliquez sur « Générer de nouveaux points ». Un nouveau nuage est tiré au hasard,
   puis le réseau le ramène, étape par étape, vers la forme qu'il a apprise.
3. Une fois la génération terminée, déplacez le curseur de l'étape 100 à
   l'étape 0. La forme n'apparaît pas d'un coup : elle se dessine d'abord dans
   ses grandes lignes, puis dans ses détails, comme les pointes de la feuille.
4. Décochez « Afficher le contour de la feuille ». Le réseau n'a jamais vu ce
   contour, seulement des points. Les points générés sont nouveaux : aucun n'est
   la copie d'un point d'entraînement.

L'idée de la diffusion a été publiée en 2015 par Jascha Sohl-Dickstein et ses
collègues, à l'Université Stanford, qui s'inspiraient de la thermodynamique. Elle
est devenue efficace en 2020, avec les travaux de Jonathan Ho, Ajay Jain et Pieter
Abbeel, à l'Université de Californie à Berkeley. En 2022, les modèles de diffusion
ont dépassé les GAN, avec DALL·E 2 (OpenAI) et Stable Diffusion (Stability AI et
l'Université de Munich), qui produisent des images à partir d'une phrase. Ils
s'entraînent de façon stable, et ils couvrent toute la variété des données, sans
effondrement des modes. Leur défaut est la **lenteur**, puisqu'une image demande de
nombreux passages dans le réseau, là où un GAN n'en demande qu'un. Une grande
partie de la recherche récente vise à réduire ce nombre d'étapes.

## Un élément après l'autre : les modèles autorégressifs

La quatrième famille découpe une donnée en éléments, et les génère **un par un**,
dans un ordre fixé. Chaque élément est tiré au hasard dans une distribution qui
dépend de tous les éléments déjà produits. On appelle ces modèles
**autorégressifs** (*autoregressive models*), parce que chaque élément est prédit à
partir des éléments précédents de la même donnée.

- Pour une image, on peut générer les pixels un par un, ligne par ligne. Chaque
  pixel est tiré en tenant compte de tous les pixels déjà placés au-dessus et à
  gauche. C'est ce que fait PixelCNN, publié par DeepMind en 2016.
- Pour un son, on peut générer les échantillons sonores un par un, à raison de
  plusieurs milliers par seconde. C'est ce que fait WaveNet, publié par DeepMind la
  même année, qui a nettement amélioré la voix des assistants vocaux.
- Pour un texte, on peut générer les mots un par un. Chaque mot est tiré dans une
  distribution qui dépend de tous les mots déjà écrits.

Cette dernière application est la plus importante. Le texte se prête naturellement
à cette méthode, puisqu'il se lit et s'écrit déjà dans un ordre, un mot après
l'autre. Les grands modèles de langage comme ceux de ChatGPT sont des modèles
autorégressifs. Ils tirent chaque mot dans une distribution, avec la
[température](docs/module4/10-generer/#la-température) présentée au chapitre
précédent. Le reste du [Module 4](docs/module4) leur est consacré.

Les modèles autorégressifs s'entraînent de façon stable, et la probabilité qu'ils
attribuent à chaque élément est calculée explicitement, ce qui permet de mesurer
précisément leur qualité. Leur défaut est le même que celui de la diffusion, en
plus marqué : générer élément par élément est lent, et une image de quelques
millions de pixels demanderait autant de passages dans le réseau. C'est pourquoi
cette méthode s'est imposée pour le texte, mais pas pour les images.

## Générer sur demande

Les modèles présentés jusqu'ici génèrent un exemple quelconque de la distribution :
un visage, un chiffre, une feuille. On veut souvent davantage, et préciser ce
qu'on veut obtenir, comme « un 7 », « un visage souriant » ou « un chat sur la
lune ».

Les quatre familles le permettent. On donne au réseau, en plus du hasard, une
information supplémentaire qu'il prend en compte à chaque étape : une étiquette,
une image de départ, ou une phrase. On parle de génération **conditionnelle**
(*conditional generation*). Un générateur d'images à partir de texte, comme
DALL·E ou Stable Diffusion, est un modèle de diffusion conditionné par une phrase.
Pour cela, il faut traduire la phrase en nombres que le réseau comprend, ce qui
demande de savoir représenter le sens d'un texte. Le chapitre du
[Module 4](docs/module4) consacré aux modèles multimodaux y reviendra, une fois
présentés les modèles de langage.

## Quatre familles, et leurs combinaisons

| | **GAN** | **VAE** | **Diffusion** | **Autorégressif** |
|---|---|---|---|---|
| Idée | un faussaire contre un expert | un espace latent rempli | retirer le bruit pas à pas | un élément après l'autre |
| Première publication | 2014 | 2013 | 2015 (efficace en 2020) | bien plus ancienne pour le texte ; 2016 pour les images et les sons |
| Points forts | images nettes, génération rapide | entraînement stable, espace latent organisé | qualité et variété | entraînement stable, probabilités explicites |
| Limites | entraînement instable, effondrement des modes | images floues | génération lente | génération très lente pour les images |
| Exemples | StyleGAN | l'autoencodeur de Stable Diffusion | DALL·E 2, Stable Diffusion | WaveNet, GPT |

Les systèmes actuels combinent souvent plusieurs de ces idées. Stable Diffusion,
par exemple, ne débruite pas directement les pixels. Un autoencodeur réduit
d'abord chaque image à une représentation latente beaucoup plus petite, et la
diffusion se fait dans cet espace latent, ce qui la rend bien plus rapide. Le
décodeur transforme ensuite le résultat en image.

Le [chapitre suivant](docs/module4) montre ce que ces méthodes ont permis de
produire depuis 2014 : des images, des voix, de la musique et des vidéos.
