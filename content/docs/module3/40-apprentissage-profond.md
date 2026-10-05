---
title: "L'apprentissage profond"
weight: 40
slug: apprentissage-profond
---

# L'apprentissage profond

D'après le
[théorème d'approximation universelle](docs/module3/20-une-couche-cachee/#plus-de-neurones-plus-de-formes), une seule couche cachée suffit
pour approcher presque n'importe quelle fonction. Pourtant, les réseaux qui ont
transformé l'IA à partir de 2012 comptent des dizaines de couches. On les appelle
des réseaux **profonds**, et leur entraînement, l'**apprentissage profond** (*deep
learning* en anglais). Ce chapitre explique ce qu'on gagne à empiler les couches, et
pourquoi cela n'a fonctionné qu'à partir de 2012.

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
a montré qu'une couche cachée est une fabrique de caractéristiques.
Dans un réseau profond, chaque couche fabrique les siennes à partir de celles de la
couche précédente. Les caractéristiques deviennent plus complexes de couche en
couche.

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

On peut voir ce que cherche un neurone d'un réseau entraîné. On part d'une image de
bruit, et on la modifie pas à pas, par rétropropagation, pour activer le plus
possible un neurone choisi. L'image obtenue montre ce à quoi ce neurone réagit. Le
même procédé sert à fabriquer les
[exemples adverses](docs/module3/90-tromper-un-reseau/#comment-on-le-fabrique),
présentés plus loin, au chapitre « Tromper un réseau ». En 2017, Chris Olah, Alexander Mordvintsev et Ludwig Schubert, chez
Google, ont appliqué cette méthode à toutes les couches d'un réseau convolutif
entraîné sur ImageNet.

{{< image src="/images/module3/visualisation-neurones.jpg" alt="Cinq colonnes de trois images chacune, de la première couche à la dernière. Traits : des rayures fines, orientées. Textures : des surfaces répétitives, alvéoles et écailles. Motifs : des entrelacs, des pompons colorés. Parties d'objets : des fleurs, des morceaux de vêtements, des formes de boutons. Objets : des façades de bâtiments, des jambes en short, des assiettes de nourriture." title="Ce que cherchent des neurones de couches de plus en plus profondes d'un réseau entraîné sur ImageNet (d'après Olah, Mordvintsev et Schubert, Distill, 2017, CC BY 4.0)." loading="lazy" >}}

La progression décrite plus haut apparaît bien, sans que personne l'ait programmée.

{{% hint info %}}
**DeepDream**

En juin 2015, Alexander Mordvintsev, Christopher Olah et Mike Tyka, ingénieurs chez
Google, publient des images produites par un réseau convolutif entraîné sur
ImageNet. Ils partent d'une photo ordinaire et la modifient pas à pas, par
rétropropagation, pour **renforcer** ce que le réseau croit y voir. Si une tache
rappelle vaguement un œil à une couche du réseau, l'image est modifiée pour
ressembler davantage à un œil. On recommence, encore et encore. Comme ImageNet
contient beaucoup de photos de chiens, des têtes de chiens, des yeux et des pattes
finissent par apparaître partout : dans les nuages, sur les visages, dans les
feuillages.

{{< image src="/images/module3/deepdream-meduses.jpg" alt="Quatre images côte à côte. La première est une photo de méduses dans un aquarium bleu. Les trois suivantes sont la même photo transformée par DeepDream après 10, 50 puis 100 itérations : des créatures à plusieurs yeux, puis des chiens et d'autres animaux envahissent l'image, de plus en plus nets et colorés." title="Une photo de méduses transformée par DeepDream : à chaque itération, le réseau renforce les formes animales qu'il croit voir (images de Martin Thoma, Wikimedia Commons, CC0)." loading="lazy" >}}

Les chercheurs publient leur programme, et des milliers de personnes l'appliquent à
leurs propres photos. Les images circulent dans le monde entier, et beaucoup y
voient pour la première fois ce qui se passe à l'intérieur d'un réseau de neurones.
Le phénomène rappelle la **paréidolie** (*pareidolia*), notre tendance à voir des visages dans les
nuages ou les prises électriques. Le réseau fait de même avec ce qu'il a appris à
reconnaître, mais en l'exagérant à chaque itération. DeepDream a aussi ouvert la
voie à des usages artistiques des réseaux de neurones, qui annoncent l'IA
générative du [Module 4](docs/module4).
{{% /hint %}}

{{% hint info %}}
**La carte n'est pas le territoire**

Cette hiérarchie rappelle celle du cerveau. Dans les années 1960, David Hubel et
Torsten Wiesel ont montré que le cortex visuel traite l'image par étapes : certains
neurones réagissent à des traits orientés, d'autres, plus loin, à des formes. Les
réseaux profonds se sont inspirés de ce résultat.

La ressemblance s'arrête là. Comme l'expliquait
« [D'où vient le mot « neurone »](docs/module3/10-un-neurone/#doù-vient-le-mot-neurone) »,
un neurone artificiel est une formule. Un neurone biologique
émet des impulsions électriques dans le temps, et son comportement dépend de
nombreux signaux chimiques. Rien n'indique que le cerveau utilise la
rétropropagation. Enfin, un enfant reconnaît un chat après en avoir vu quelques-uns,
avec un cerveau qui consomme environ 20 watts, alors qu'un réseau a besoin de
milliers d'exemples et de beaucoup plus d'énergie.

Un réseau de neurones est un modèle mathématique inspiré du
cerveau. Ce n'est pas une copie du cerveau, et son fonctionnement ne nous apprend
que peu de choses sur le nôtre.
{{% /hint %}}

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
[rétropropagation](docs/module3/30-entrainer-un-reseau/#la-rétropropagation) s'applique à un réseau de n'importe quelle profondeur. Trois
obstacles ont pourtant bloqué les réseaux profonds pendant plus de vingt ans.

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
venue du jeu vidéo, avec les **processeurs graphiques** (*graphics processing
units*, GPU), qui entraînent un réseau des dizaines de fois plus vite qu'un
processeur ordinaire. Des bibliothèques logicielles ont ensuite automatisé la
rétropropagation. Le chapitre
« [Le matériel et les outils](docs/module3/42-materiel-et-outils) » raconte ces
deux histoires.

**Un premier contournement, en 2006.** Avant que ces trois obstacles soient levés,
Hinton propose un détour. Au lieu d'entraîner toutes les couches d'un coup, on les
entraîne une à une, sans étiquettes : chaque couche apprend à résumer ce que lui
transmet la précédente, un peu comme un
[autoencodeur](#apprendre-sans-étiquettes-lautoencodeur). Une fois toutes les
couches en place, la rétropropagation ajuste l'ensemble. Ce **préentraînement
couche par couche** (*greedy layer-wise pre-training*), publié par Hinton et ses
collègues en 2006 et repris aussitôt par l'équipe de Bengio, montre qu'on peut
enfin entraîner des réseaux à plusieurs couches cachées, et qu'ils font mieux que
les réseaux peu profonds sur plusieurs tâches. C'est à cette époque que le nom
*deep learning* s'impose. Quelques années plus tard, avec la ReLU, de grandes bases
de données et les GPU, le détour devient inutile : AlexNet s'en passe. Mais il
avait ramené l'attention sur les réseaux profonds.

## 2012 : le concours ImageNet

À partir de 2010, ImageNet sert de base à un concours annuel. Il faut classer des
images parmi 1 000 catégories, après un entraînement sur 1,2 million d'exemples.
Une réponse est comptée comme une erreur si la bonne catégorie ne figure pas parmi
les cinq propositions du système.

En 2010 et 2011, les meilleurs systèmes reposent sur des caractéristiques
fabriquées à la main (*hand-crafted features*), et leur taux d'erreur est de 28 %,
puis de 26 %. En 2012, Alex Krizhevsky, Ilya Sutskever et Geoffrey Hinton, de
l'Université de Toronto, présentent un réseau profond, **AlexNet**. Il compte huit
couches et 60 millions de paramètres, il utilise la ReLU, et il a été entraîné
pendant environ une semaine sur deux GPU.

Avec 60 millions de paramètres pour 1,2 million
d'images, le risque de
[sur-apprentissage](docs/module2/70-generaliser/#trop-coller-ou-trop-lisser-le-compromis-biais-variance)
(*overfitting*) est grand. AlexNet le limite par une forme de
[régularisation](docs/module2/70-generaliser/#garder-un-modèle-riche-mais-le-tenir-en-laisse-la-régularisation),
au sens du Module 2 : le réseau reste riche, mais on l'empêche de trop coller à ses
données d'entraînement. Il utilise une méthode toute récente, publiée par l'équipe
de Hinton la même année, le **dropout**. À chaque étape de l'entraînement, une
partie des neurones, tirés au hasard, est mise hors service. Le réseau ne peut donc
pas compter sur un neurone en particulier, et il apprend des caractéristiques plus
robustes, un peu comme une équipe où chacun doit pouvoir remplacer un absent. Les
images d'entraînement sont aussi recadrées et retournées au hasard, ce qui en
multiplie les variantes.

{{< image src="/images/module3/dropout.svg" alt="Quatre fois le même réseau, de quatre couches. Dans les trois premiers panneaux, trois étapes successives de l'entraînement : à chaque étape, la moitié des neurones des couches cachées, tirés au hasard, sont éteints, marqués d'une croix, et leurs connexions disparaissent ; ce ne sont pas les mêmes neurones d'une étape à l'autre. Dans le quatrième panneau, à l'utilisation, tous les neurones et toutes les connexions sont présents." title="Le dropout : à chaque étape de l'entraînement, d'autres neurones sont éteints au hasard. Une fois l'entraînement terminé, le réseau utilise tous ses neurones." loading="lazy" >}}

Le taux d'erreur d'AlexNet est de 15 %. Le deuxième système est à 26 %.

{{< image src="/images/module3/imagenet-erreur.svg" alt="Un diagramme à barres. En 2010 et 2011, les systèmes gagnants reposent sur des caractéristiques fabriquées à la main : 28,2 % puis 25,8 % d'erreur. En 2012, le réseau profond AlexNet obtient 15,3 %. Les gagnants suivants sont tous des réseaux profonds : 11,7 % en 2013, 6,7 % en 2014, 3,6 % en 2015, 3,0 % en 2016 et 2,3 % en 2017. Une ligne horizontale marque le niveau humain, estimé à 5 %, dépassé à partir de 2015." title="Le taux d'erreur du système gagnant au concours ImageNet, de 2010 à 2017." loading="lazy" >}}

L'écart est si grand que le domaine change de méthode en deux ans. Dès 2014, tous
les systèmes en compétition sont des réseaux profonds. En 2015, le réseau gagnant
compte 152 couches et son taux d'erreur, 3,6 %, est inférieur à celui d'un humain
sur la même tâche, estimé à 5 %. La même bascule se produit quelques années plus tard pour la
traduction. Pour la reconnaissance de la parole, elle avait même commencé un peu
plus tôt. Entre 2009 et 2012, des étudiants de Hinton, avec des équipes de
Microsoft, de Google et d'IBM, remplacent une partie des systèmes de reconnaissance
vocale par des réseaux profonds,
[préentraînés couche par couche](#pourquoi-seulement-en-2012). En 2012, la
recherche vocale des téléphones Android en profite. C'est le premier grand succès
industriel de l'apprentissage profond. ImageNet a pourtant davantage frappé les
esprits, parce que l'écart y était spectaculaire et mesuré lors d'un concours
public.

AlexNet est un réseau d'un type particulier, un réseau convolutif (*convolutional
neural network*, CNN), conçu pour les images. Le chapitre
« [Voir : les réseaux convolutifs](docs/module3/50-reseaux-convolutifs) » lui est
consacré.

{{% hint info %}}
**Une école canadienne**

AlexNet est sorti du laboratoire de Geoffrey Hinton, à l'Université de Toronto. Ce
n'est pas un hasard. Pendant les années 1990 et 2000, les réseaux de neurones
intéressaient peu, et les organismes qui finançaient la recherche s'en
détournaient. En 2004, l'Institut canadien de recherches avancées (CIFAR) lance un
programme intitulé « Calcul neuronal et perception adaptative » (*Neural
Computation and Adaptive Perception*), dirigé par Hinton. Le programme réunit un
petit groupe de chercheurs convaincus, dont Yoshua Bengio, à l'Université de
Montréal, et Yann Le Cun, à l'Université de New York. Ils continuent à travailler
sur les réseaux profonds quand presque personne d'autre ne le fait.

Le pari réussit en 2012. Hinton, Bengio et Le Cun reçoivent ensemble le prix Turing
2018. En 2024, Hinton reçoit le prix Nobel de physique avec l'Américain John
Hopfield, « pour des découvertes et des inventions fondamentales qui permettent
l'apprentissage automatique avec des réseaux de neurones artificiels ». Le comité
récompense deux réseaux des années 1980 qui empruntent leurs outils à la physique
statistique : le réseau de Hopfield (1982), une mémoire qui retrouve une image
complète à partir d'un fragment, et la machine de Boltzmann de Hinton, qui tire son
nom du physicien Ludwig Boltzmann. Le choix a surpris, et plusieurs physiciens se
sont demandé si l'on récompensait encore de la physique. Hinton, qui avait quitté
Google en 2023 pour parler librement des risques de l'IA, a profité de la tribune
pour les rappeler. Le [Module 5](docs/module5) revient sur ces risques. Le laboratoire fondé par Bengio en 1993 devient en 2017 **Mila**, l'Institut
québécois d'intelligence artificielle, l'un des plus grands centres de recherche
universitaire en apprentissage profond au monde. La même année, le gouvernement du
Canada confie au CIFAR la Stratégie pancanadienne en matière d'intelligence
artificielle, l'une des premières stratégies nationales consacrées à l'IA. Elle
s'appuie sur trois instituts : Mila à Montréal, l'Institut Vecteur à Toronto et
l'Amii à Edmonton, où travaille Richard Sutton, l'auteur de la
[leçon amère](#la-leçon-amère).
{{% /hint %}}

## La leçon amère

La [fin du Module 2](docs/module2/80-trois-facons-d-apprendre/#un-même-squelette-dun-bout-à-lautre)
a présenté l'essai de Richard Sutton,
« [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) »
(2019). Sa thèse est la suivante. Dans l'histoire de l'IA, les chercheurs ont
d'abord tenté d'inscrire leur propre savoir dans les systèmes. Cela aidait à court
terme. À long terme, ces systèmes ont été dépassés par des méthodes générales, qui
n'utilisent aucun savoir particulier, mais qui tirent parti de la puissance de
calcul disponible.

Le concours de 2012 en est l'exemple le plus net. Les caractéristiques d'images
mises au point par des experts pendant vingt ans ont été dépassées par un réseau
qui apprend les siennes. Le Module 1 en donnait un autre exemple, avec
[Deep Blue](docs/module1/30-chercher-raisonner/#lapogée-deep-blue-bat-kasparov-1997) :
la recherche à grande échelle l'avait emporté sur les programmes qui tentaient
d'imiter le raisonnement des grands maîtres.

Sutton qualifie cette leçon d'amère parce qu'elle va contre l'intuition des
chercheurs : le savoir qu'ils inscrivent dans un système finit par le limiter. Elle
a aussi un coût. Un réseau profond ne donne pas ses raisons, alors qu'on pouvait
lire les règles d'un [système expert](docs/module1/50-systemes-experts) ou les
questions d'un [arbre de décision](docs/module2/65-arbres-de-decision) (*decision
tree*). Et ses progrès dépendent de quantités de données et de calcul que peu
d'organisations possèdent.

La leçon ne dit pas que le savoir humain est inutile. Il reste présent, mais
ailleurs : dans le choix des données, et dans la forme donnée au réseau. Les
chapitres sur les réseaux convolutifs, les réseaux récurrents et l'attention en
donnent des exemples.

## Plus de paramètres que d'exemples

AlexNet a 60 millions de paramètres, pour 1,2 million d'images d'entraînement.
D'après « [Généraliser](docs/module2/70-generaliser/#trop-coller-ou-trop-lisser-le-compromis-biais-variance) »,
un modèle aussi souple devrait apprendre ses exemples par cœur et échouer sur des
images nouvelles. C'est le sur-apprentissage (*overfitting*). Or les réseaux
profonds généralisent bien. C'est la question que le
[Module 2](docs/module2/70-generaliser/#garder-un-modèle-riche-mais-le-tenir-en-laisse-la-régularisation)
avait laissée ouverte.

Une partie de la réponse tient à la régularisation, décrite dans
« [Entraîner un réseau](docs/module3/30-entrainer-un-reseau/#lentraînement-en-pratique) ».
Mais elle ne suffit pas à expliquer le phénomène. Quand on fait grossir un réseau,
on observe d'abord la courbe en U du Module 2 : l'erreur sur les exemples nouveaux
baisse, puis remonte. Si l'on continue au-delà du point où le réseau peut mémoriser
tous ses exemples, l'erreur redescend, parfois plus bas qu'avant. Ce phénomène
s'appelle la **double descente** (*double descent*).

{{< image src="/images/module3/double-descente.svg" alt="Un graphique. À l'horizontale, la taille du modèle ; à la verticale, l'erreur sur des exemples nouveaux. La courbe descend, remonte jusqu'à un pic, puis redescend plus bas qu'avant. La partie à gauche du pic est la courbe en U du Module 2. Le pic se trouve à la taille où le modèle peut mémoriser tous ses exemples. La partie à droite est celle des grands réseaux." title="La double descente : après le pic, un modèle plus grand généralise mieux." loading="lazy" >}}

Le phénomène est bien établi, mais son explication n'est pas complète. L'hypothèse
la plus courante est la suivante. Un très grand réseau dispose de nombreuses façons
de reproduire ses exemples, et la descente de gradient aboutit
le plus souvent à l'une des plus simples. C'est un cas où la pratique a précédé la
théorie.

## Apprendre sans étiquettes : l'autoencodeur

Tous les réseaux vus jusqu'ici sont entraînés avec des exemples étiquetés (*labeled
examples*). Un réseau peut aussi apprendre des caractéristiques sans étiquettes.
L'**autoencodeur** (*autoencoder*) en est l'exemple le plus simple.

Un autoencodeur est un réseau en forme de sablier. On lui donne une image en
entrée, et on lui demande de produire la même image en sortie. L'erreur est l'écart
entre les deux. La tâche serait sans intérêt si le réseau pouvait simplement
recopier son entrée, mais la couche du milieu est très étroite. Les 784 pixels d'un
chiffre doivent passer par quelques dizaines de neurones seulement.

{{< image src="/images/module3/autoencodeur.svg" alt="De gauche à droite : l'image d'un zéro manuscrit ; un réseau en forme de sablier, dont les couches comptent de moins en moins de neurones jusqu'à une couche centrale très étroite, puis de plus en plus ; l'image reconstruite, presque identique à l'image de départ. La première moitié du réseau est l'encodeur, la couche centrale est la représentation latente, la seconde moitié est le décodeur." title="Un autoencodeur : l'image doit passer par une couche étroite, puis être reconstruite." loading="lazy" >}}

- La première moitié, l'**encodeur**, réduit l'image à quelques nombres.
- La seconde moitié, le **décodeur**, reconstruit l'image à partir de ces nombres.

Pour réussir, le réseau doit garder l'essentiel de l'image dans la couche étroite :
quel chiffre, quelle inclinaison, quelle épaisseur de trait. Ces quelques nombres
forment une représentation compacte de l'image, qu'on appelle sa **représentation
latente** (*latent representation*). C'est un cas
d'[auto-supervision](docs/module2/80-trois-facons-d-apprendre/#fabriquer-soi-même-ses-réponses-lauto-supervision)
(*self-supervised learning*), présentée au Module 2 : les données fournissent
elles-mêmes la réponse attendue.

Le décodeur a une autre utilité. Si on lui donne des nombres qui ne viennent
d'aucune image réelle, il produit quand même une image. C'est une première façon de
générer du contenu, sur laquelle le [Module 4](docs/module4/10-generer/#lespace-latent) reviendra.

Un réseau profond peut donc apprendre ses propres caractéristiques, à condition
d'avoir assez de données et de calcul. Le chapitre suivant,
« [Le matériel et les outils](docs/module3/42-materiel-et-outils) », raconte
comment ce calcul est devenu possible.
