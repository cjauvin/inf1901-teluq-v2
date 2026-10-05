---
title: "Générer : imiter une distribution"
weight: 10
slug: generer
---

# Générer : imiter une distribution

{{< image src="/images/module4/visages-stylegan.jpg" alt="Quatre portraits photographiques en gros plan : une jeune femme aux cheveux châtains avec une frange, un homme aux cheveux courts sur fond bleu, un garçon souriant en chemise blanche, une femme souriante sur fond sombre. Rien ne les distingue de vraies photos." title="Ces quatre visages ont été produits par un réseau de neurones. Aucune de ces personnes n'existe (StyleGAN, 2019, et StyleGAN2, 2020 ; Wikimedia Commons, domaine public)." loading="lazy" >}}

Les quatre visages ci-dessus ont l'air de photos. Pourtant, aucune de ces personnes
n'existe. Chaque image a été produite par un réseau de neurones, StyleGAN, présenté
en 2019 par des chercheurs de l'entreprise Nvidia. Le site *This Person Does Not
Exist* (« cette personne n'existe pas ») en affiche un nouveau à chaque visite.

Tous les réseaux du [Module 3](docs/module3) **reconnaissent**. On leur donne une
image, et ils répondent « 7 » ou « panda ». On leur donne une phrase, et ils
proposent sa traduction. Le réseau qui a produit ces visages fait l'inverse : il
ne reçoit aucune image, et il en **produit** une. C'est ce qu'on appelle l'**IA
générative** (*generative AI*). Elle produit aujourd'hui des images, des textes,
des voix, de la musique, des vidéos et du code informatique.

Ce chapitre présente l'idée commune à tous ces systèmes. Un modèle génératif
apprend comment les données se répartissent, puis il tire au hasard de nouveaux
exemples qui se répartissent de la même façon.

## Décrire plutôt que séparer

Le chapitre « [Classer](docs/module2/60-classer/#renverser-le-problème-la-classification-bayésienne) »
du Module 2 a présenté deux façons de construire un classificateur.

- Une approche **discriminative** (*discriminative*) trace directement la frontière
  entre les classes. C'est le cas de la régression logistique. Elle répond à la
  question « de quel côté de la frontière ce point se trouve-t-il ? ».
- Une approche **générative** (*generative*) commence par décrire chaque classe,
  par exemple à quoi ressemble un pourriel typique. Pour classer un nouvel
  exemple, elle se demande à quelle description il ressemble le plus. C'est le cas
  de la classification bayésienne naïve.

Le [Module 2](docs/module2/60-classer/#renverser-le-problème-la-classification-bayésienne) remarquait qu'une description assez précise d'une classe permettrait,
en principe, d'en produire de nouveaux membres. C'est de là que vient le mot
*génératif*. Avec Bayes naïf, cette possibilité restait théorique : sa description
d'un pourriel est une liste de mots fréquents, prise mot par mot, et les
« pourriels » qu'on en tirerait seraient des suites de mots sans aucun sens. L'IA
générative actuelle repose sur la même idée, avec des descriptions beaucoup plus
riches. Un grand modèle de langage (*large language model*, LLM), comme celui de
ChatGPT, est une description très détaillée de la classe « texte écrit par des
humains ». Un générateur d'images comme StyleGAN est une description très détaillée
de la classe « photo de visage ».

## Une distribution, et tirer dedans

Ce que le modèle décrit s'appelle une **distribution** (*distribution*) : la façon
dont les exemples se répartissent entre toutes les valeurs possibles, avec leur
probabilité.

Un exemple simple est celui des lettres dans un texte en français. Le *e* y est la
lettre la plus fréquente, environ une lettre sur sept. Le *s*, le *a* et le *i*
suivent, chacun autour d'une lettre sur treize. Le *w* et le *k* sont très rares.
La liste de ces fréquences est la distribution des lettres en français.

Une fois cette distribution connue, on peut produire des lettres nouvelles en les
tirant au hasard, à condition de respecter les fréquences : le *e* doit sortir
souvent et le *k* presque jamais. Tirer des exemples au hasard en respectant une
distribution s'appelle **échantillonner** (*to sample*). C'est l'opération de base
de tous les modèles génératifs. Les lettres obtenues ne forment pas des mots, parce
que cette distribution ne dit rien de l'ordre des lettres. Elle ne décrit qu'une
seule chose, leur fréquence.

Le même principe s'applique à des données à plusieurs dimensions. La figure
ci-dessous reprend les vingt maisons du
[Module 2](docs/module2/10-le-probleme), dans le plan de la distance au centre et de
l'année de construction. Elles forment deux amas : des maisons récentes et
proches du centre, et des maisons anciennes et éloignées. Pour décrire leur
distribution, on place une petite cloche autour de chaque maison, puis on les
additionne. On obtient un **relief** (une densité de probabilité, *probability
density*), haut là où les maisons sont nombreuses, et plat là où il n'y en a
aucune. On tire ensuite de nouvelles maisons dans ce relief, en choisissant une
maison au hasard et en la déplaçant un peu, au hasard, selon sa cloche.

{{< image src="/images/module4/portrait-maisons.svg" alt="Le plan distance du centre × année de construction. Les vingt maisons du Module 2 forment deux amas, proches et récentes en haut à gauche, éloignées et anciennes en bas à droite. Autour d'elles, des bandes de plus en plus foncées dessinent le relief : deux collines, une par amas. Dix maisons nouvelles, dessinées en anneaux bruns, tombent presque toutes sur les collines, et aucune n'est la copie d'une maison existante." title="Le relief décrit la distribution des vingt maisons. Les dix maisons tirées dans ce relief tombent là où se trouvent les vraies, sans en copier aucune." loading="lazy" >}}

Les maisons tirées sont **plausibles**. Elles tombent là où se trouvent les vraies
maisons, et presque jamais dans le vide entre les deux amas. Elles sont aussi
**nouvelles**, car aucune n'est la copie d'une maison existante. Ce sont les deux
qualités qu'on attend de tout modèle génératif, qu'il produise des maisons, des
visages ou des phrases.

## La température

Pour une même distribution, un réglage modifie la façon de tirer. On l'appelle la
**température** (*temperature*), par analogie avec la physique, où une température
élevée rend le mouvement des particules plus désordonné.

- À **basse température**, on accentue les écarts entre les probabilités. Le choix
  le plus probable l'emporte presque toujours. Le résultat est sûr, mais répétitif.
- À **température 1**, on tire selon la distribution telle quelle.
- À **haute température**, on réduit les écarts. Les choix rares sortent plus
  souvent. Le résultat est plus varié, puis devient incohérent si on monte trop.

{{< image src="/images/module4/temperature-lettres.svg" alt="Trois diagrammes à barres superposés donnent la probabilité de tirer chaque lettre, de la plus fréquente à la plus rare. À température basse, la barre du e domine toutes les autres, et le tirage ne contient presque que des e. À température 1, les barres suivent les fréquences du français, et le tirage mêle des lettres courantes. À température haute, les barres sont presque toutes de la même hauteur, et le tirage contient des lettres rares comme k, j ou q." title="La même distribution des lettres, tirée à trois températures. Chaque rangée a sa propre échelle verticale, pour comparer la forme des distributions." loading="lazy" >}}

La température est un réglage des modèles génératifs actuels. Dans un modèle de
langage, une température basse donne des réponses prévisibles, qui conviennent à
une question factuelle. Une température plus haute donne des textes plus variés,
qui conviennent mieux à un poème ou à une liste d'idées. Le chapitre du [Module 4](docs/module4/50-predire-le-mot-suivant/#gpt-un-transformer-qui-prédit-le-jeton-suivant)
consacré aux modèles de langage reprendra ce réglage avec de vrais textes.

## Le vrai problème : les grandes dimensions

Pour des lettres ou pour des maisons décrites par deux nombres, il suffit de
compter et d'additionner des cloches. Pour des images, ce n'est plus possible.

Une image de chiffre manuscrit de la base MNIST, utilisée tout au long du
[Module 3](docs/module3), compte 28 × 28 = 784 pixels. C'est un point dans un
espace de 784 dimensions, une par pixel. Si l'on tire chaque pixel au hasard, on
obtient un point de cet espace, mais ce n'est jamais un chiffre : c'est de la
neige. On pourrait tirer des milliards d'images de cette façon sans jamais obtenir
un 7.

{{< image src="/images/module4/bruit-ou-chiffre.svg" alt="Deux grilles de 28 sur 28 pixels. À gauche, chaque pixel a reçu une teinte de gris tirée au hasard : on ne voit qu'une neige uniforme. À droite, un vrai chiffre manuscrit, un 7 : quelques pixels foncés forment un trait, tous les autres sont blancs." title="Deux points du même espace de 784 dimensions. Presque tous les points de cet espace ressemblent à celui de gauche." loading="lazy" >}}

Les vraies images de chiffres occupent donc une portion infime de cet espace.
C'est une conséquence de la
[malédiction de la dimension](docs/module2/40-predire-par-ressemblance/#mesurer-la-ressemblance-la-distance)
(*curse of dimensionality*), présentée au Module 2. Dans un espace de très grande
dimension, presque tout est vide. La méthode des cloches ne fonctionne plus non
plus : avec 60 000 chiffres dans un espace aussi vaste, chaque cloche resterait
isolée, et le relief serait nul partout sauf tout près des exemples connus. Le
modèle ne pourrait que les recopier.

La difficulté de l'IA générative est là. Il faut trouver, dans un espace immense,
la petite région où se trouvent les vraies images, et apprendre sa forme.

## L'espace latent

Le chapitre « [L'apprentissage profond](docs/module3/40-apprentissage-profond/#apprendre-sans-étiquettes-lautoencodeur) »
du Module 3 a présenté l'**autoencodeur**. C'est un réseau en forme de sablier,
qui réduit une image à quelques nombres (l'**encodeur**), puis la reconstruit à
partir de ces nombres (le **décodeur**). Ces quelques nombres forment la
**représentation latente** de l'image, et l'ensemble des valeurs qu'ils peuvent
prendre s'appelle l'**espace latent** (*latent space*).

Le décodeur fournit une solution au problème des grandes dimensions. Au lieu de
tirer 784 pixels au hasard, on tire quelques nombres dans l'espace latent, et le
décodeur les transforme en image. Comme il a appris à reconstruire de vrais
chiffres, ce qu'il produit ressemble à un chiffre. Générer revient à choisir un
point dans un petit espace bien organisé, plutôt que dans l'immense espace des
pixels.

L'applet ci-dessous contient le décodeur d'un autoencodeur entraîné sur les
60 000 chiffres de MNIST. Son espace latent n'a que **deux** dimensions, ce qui
permet de le dessiner comme une carte. Les petits points colorés sont de vrais
chiffres, placés à l'endroit où l'encodeur les range. Chaque chiffre occupe sa
propre région, sans que personne n'ait indiqué au réseau quel chiffre était quel
chiffre : il n'a vu aucune étiquette.

{{< applet src="/html/applets/espace-latent.html" height="544" >}}

Quelques manipulations à faire :

1. Promenez la souris au centre de la région d'un chiffre, puis vers ses bords.
   Le chiffre change d'inclinaison et d'épaisseur. Le réseau a appris à ranger ces
   variations le long de la carte.
2. Placez la souris entre deux régions. Le décodeur produit une forme
   intermédiaire, un chiffre qui hésite entre les deux.
3. Cliquez dans la région des 7, puis dans celle des 0. La bande sous l'image
   montre le chemin entre les deux points, et le passage progressif d'un chiffre à
   l'autre.
4. Cliquez plusieurs fois sur « Tirer un point au hasard ». C'est la génération
   proprement dite : un point est tiré au hasard dans l'espace latent, et le
   décodeur en fait un chiffre que personne n'a jamais écrit.

Un autoencodeur ordinaire, comme celui du
[Module 3](docs/module3/40-apprentissage-profond/#apprendre-sans-étiquettes-lautoencodeur),
range ses images n'importe où dans son espace latent. Certains chiffres
s'entassent, d'autres s'étalent très loin, et de grandes zones restent vides. On ne
sait donc pas où tirer un point au hasard pour obtenir des chiffres variés. Le
réseau de l'applet est un autoencodeur **variationnel** (*variational
autoencoder*, VAE). Il est entraîné pour ranger ses images autour du centre de la
carte, sans laisser de trous, de sorte qu'un point tiré au hasard près du centre
donne presque toujours un chiffre. Le
[chapitre suivant](docs/module4/20-quatre-facons-de-generer/#remplir-lespace-latent-les-autoencodeurs-variationnels)
explique comment.

Cette carte n'a que deux dimensions, ce qui limite la qualité des chiffres
produits : beaucoup sont flous. Les modèles qui ont produit les visages du début
de ce chapitre utilisent un espace latent de 512 dimensions. Le principe est le
même.

## Générer n'est pas recopier

Un modèle génératif utile produit des exemples **nouveaux**. Un modèle qui ne
ferait que restituer ses exemples d'entraînement serait une simple base de
données. C'est la forme que prend, pour un modèle génératif, le
sur-apprentissage (*overfitting*) présenté au chapitre
« [Généraliser](docs/module2/70-generaliser/#un-modèle-se-juge-sur-ce-quil-na-jamais-vu) »
du Module 2. Un modèle qui colle trop à ses données d'entraînement ne fait que les
recopier.

La frontière n'est pas toujours nette. Des chercheurs ont montré que certains
générateurs d'images peuvent restituer, presque à l'identique, des images de leurs
données d'entraînement, et que des modèles de langage peuvent réciter des passages
entiers de textes qu'ils ont lus. Le [Module 2](docs/module2/70-generaliser/#un-modèle-se-juge-sur-ce-quil-na-jamais-vu) posait déjà la question à propos
des grands modèles de langage : où finit la mémoire, et où commence la
compréhension ? Pour les modèles génératifs, elle a aussi une dimension juridique,
puisque ces modèles sont entraînés sur des œuvres protégées par le droit d'auteur.
Le [Module 5](docs/module5) revient sur cette question.

## Vers des modèles plus puissants

Ce chapitre a présenté l'idée commune à tous les modèles génératifs : apprendre
une distribution, puis y tirer de nouveaux exemples. Il a aussi présenté un
premier moyen d'y parvenir pour des images, l'espace latent d'un autoencodeur.

Les visages du début du chapitre ont été produits par une autre méthode. Il en
existe quatre grandes familles, qui ont chacune marqué l'histoire du domaine :
les réseaux antagonistes génératifs, les autoencodeurs variationnels, les modèles
de diffusion et les modèles qui génèrent élément par élément. Les grands modèles
de langage appartiennent à cette dernière famille. Le [chapitre suivant](docs/module4/20-quatre-facons-de-generer)
présente les quatre.
