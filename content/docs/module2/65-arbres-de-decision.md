---
title: "Poser des questions : les arbres de décision"
weight: 65
slug: arbres-de-decision
---

# Poser des questions : les arbres de décision

Tous les modèles vus jusqu'ici raisonnent avec des nombres. kNN mesure des
distances, la droite multiplie et additionne, la régression logistique et Bayes
calculent des probabilités. Ces méthodes sont puissantes, mais ce n'est pas
ainsi que nous prenons la plupart de nos décisions. Un médecin devant un patient
ne fait pas de calcul : il pose des questions l'une après l'autre, et chaque
réponse oriente la suivante. Le [jeu des vingt questions](https://en.wikipedia.org/wiki/Twenty_questions)
fonctionne de la même façon. Un joueur pense à un objet, et l'autre doit le
deviner en posant au plus vingt questions auxquelles on ne répond que par oui ou
par non, comme « est-ce un animal ? » ou « est-il plus gros qu'un chat ? ».
Chaque réponse réduit l'ensemble des possibilités. Le guide de dépannage à la
fin d'un manuel suit le même principe : « l'appareil s'allume-t-il ? si non,
est-il branché ? ». Il s'agit chaque fois d'une suite de questions à réponse oui
ou non, qui se ramifie et aboutit à une conclusion.

Cette façon de décider correspond à l'un des modèles les plus anciens et les plus
intuitifs de l'apprentissage automatique, l'**arbre de décision**. Comme kNN, il
traite aussi bien la régression que la classification, et son principe peut se
dessiner. Il apporte cependant deux choses qu'aucun modèle du module n'offrait
encore : une frontière qui n'est pas une droite, et une décision qu'on peut
lire.

## Une question suffit presque

Reprenons la seconde question du module dans le plan où elle se représente : la
distance du centre en abscisse, l'année de construction en ordonnée, et la
couleur qui indique si la maison s'est vendue vite. Laissons un arbre apprendre
sur ces vingt maisons, avec une seule question permise. Voici le résultat :

{{< image src="/images/module2/arbre-maisons.svg" alt="Un arbre à une seule question, « à plus de 11 km du centre ? » : la branche « non » mène à une feuille bleue, 11 maisons sur 12 vendues vite ; la branche « oui » à une feuille rouge, 1 sur 8. Deux erreurs sur vingt, les deux exceptions." title="Un arbre à une question : une racine, deux branches, deux feuilles. Dix-huit maisons sur vingt bien classées." loading="lazy" >}}

La question est « à plus de 11 km du centre ? ». Si la réponse est non, la maison
va dans la feuille de gauche, où 11 maisons sur 12 se sont vendues vite, et
l'arbre répond *oui, vendue vite*. Si la réponse est oui, elle va dans la feuille
de droite, où 1 maison sur 8 seulement s'est vendue vite, et l'arbre répond
*non*. Avec une question et deux feuilles, 18 maisons sur 20 sont correctement
classées. Les deux maisons restantes sont les deux exceptions déjà repérées dans
le nuage coloré, chacune du mauvais côté de la question.

Le vocabulaire est celui d'un arbre dessiné à l'envers. La première question est
la **racine**, chaque réponse est une **branche**, et les cases du bas, où l'on
ne pose plus de question mais où l'on répond, sont les **feuilles**. Pour
prédire, on part de la racine avec une nouvelle maison, on répond aux questions
et on descend jusqu'à une feuille. La couleur majoritaire de cette feuille est la
prédiction.

Dans le plan, une question sur la distance correspond à une **coupe verticale** à
11 km : tout ce qui est à gauche est bleu, tout ce qui est à droite est rouge.
C'est le panneau de gauche de la figure ci-dessous, avec le même fond teinté que
pour kNN. Comparez cette frontière à [celle de
kNN](docs/module2/40-predire-par-ressemblance) sur les mêmes maisons. La
frontière de kNN était une ligne sinueuse entre les amas. Celle de l'arbre est
un trait droit et vertical, parce qu'une question ne porte que sur une seule
caractéristique à la fois.

On peut remarquer que l'arbre n'a rien demandé sur l'année de construction, alors
que le nuage coloré semblait indiquer que les maisons anciennes se vendent
lentement. Une question sur l'année aurait donné un résultat tout aussi bon,
comme le montre le panneau de droite. La question « construite après 1989 ? »
correspond à une **coupe horizontale**, et elle place les mêmes 11 maisons sur 12
d'un côté et 1 sur 8 de l'autre, avec les mêmes deux exceptions.

{{< image src="/images/module2/arbre-maisons-deux-coupes.svg" alt="Deux fois le même petit plan distance × année avec les vingt maisons. À gauche, la coupe verticale de la question « À plus de 11 km du centre ? » : bleu à gauche, rouge à droite. À droite, la coupe horizontale de la question « Construite après 1989 ? » : bleu en haut, rouge en bas. Dans les deux cas, les mêmes deux exceptions sont du mauvais côté : deux erreurs sur vingt, à égalité." title="Deux questions à égalité : la coupe sur la distance et la coupe sur l'année classent les mêmes dix-huit maisons, et ratent les deux mêmes." loading="lazy" >}}

L'arbre disposait donc de deux questions équivalentes. Il n'en a pris qu'une,
parce qu'une fois la première posée, la seconde n'apporte plus rien, sauf pour
corriger les deux exceptions. De plus, l'arbre ne conserve pas les vingt
maisons : une fois la question trouvée, il n'en a plus besoin. Il fait donc
partie des modèles qui résument les données, comme la droite, et ses seuls
paramètres sont un seuil et deux réponses. La [section suivante](#comment-larbre-choisit-ses-questions) explique comment
il a choisi entre les deux questions et, plus généralement, comment il choisit
ses questions.

## Comment l'arbre choisit ses questions

Le choix de la question repose sur un simple **comptage**. Pour chaque
caractéristique et chaque seuil possible, l'arbre fait un essai : il sépare les
vingt maisons en deux groupes et mesure, de chaque côté, à quel point les
couleurs sont **mélangées**. Une feuille où toutes les maisons sont de la même
couleur est dite *pure*. Une feuille où elles sont moitié-moitié est le pire
cas, puisqu'elle ne donne aucune information. La meilleure question est celle
dont les deux côtés sont, ensemble, les plus purs possible.

Le nombre de seuils candidats est limité. Entre deux maisons voisines sur une
caractéristique, toutes les coupes donnent le même résultat, et il suffit
d'essayer celle du milieu. Avec vingt maisons et deux caractéristiques, cela fait
une quarantaine de questions à essayer. Un ordinateur les évalue toutes très
rapidement et garde la meilleure. Sur nos maisons, la question « à plus de 11 km
du centre ? » donne d'un côté 11 bleues sur 12 et de l'autre 7 rouges sur 8,
soit deux feuilles presque pures. La question « construite après 1995 ? » aurait
laissé 2 rouges parmi 11 d'un côté et 2 bleues parmi 9 de l'autre. Le mélange
étant plus important, cette question est écartée.

Cela explique l'[observation précédente](#une-question-suffit-presque). Les questions « construite après
1989 ? » et « à plus de 11 km du centre ? » obtenaient exactement le même score,
11 sur 12 et 1 sur 8. En cas d'égalité parfaite, l'arbre prend la première
question trouvée. Il faut donc retenir que, lorsque deux caractéristiques
apportent la même information, l'arbre en choisit une et ignore l'autre, sans
que cela signifie que l'autre soit sans importance. Un arbre ne donne pas une
explication du monde, mais un chemin de décision qui fonctionne.

Une fois la première question posée, on recommence séparément dans chacune des
deux feuilles. On cherche la meilleure question pour les maisons proches du
centre, puis la meilleure pour les maisons éloignées, et ainsi de suite, jusqu'à
ce que les feuilles soient pures ou qu'on décide d'arrêter. Chaque question est
choisie sans tenir compte des suivantes. Les informaticiens appellent cela une
stratégie *gloutonne* (*greedy*, en anglais, le terme le plus souvent employé) :
on choisit la meilleure étape immédiate, sans regarder plus loin. Cette stratégie
ne garantit pas le meilleur arbre possible, mais elle est rapide et donne de très
bons résultats en pratique.

Cet apprentissage diffère de ceux vus précédemment. Le modèle le plus bête calculait
une moyenne. La droite et les modèles apparentés descendaient progressivement la
pente d'une fonction d'erreur. L'arbre, lui, **cherche** : il énumère des
questions, les essaie et garde la meilleure. Il n'y a ni paramètres ajustés de
façon continue, ni gradient, mais une exploration parmi des choix discrets,
semblable à la recherche dans un arbre de coups du [Module
1](docs/module1/30-chercher-raisonner), appliquée ici à l'apprentissage. C'est
la troisième façon d'apprendre présentée dans ce module, et elle a la même
structure que les deux autres : des données, une mesure de ce qui est bon (la
pureté) et une procédure qui maximise cette mesure.

{{% hint info %}}
**Pour aller plus loin : mesurer le mélange.** La mesure la plus courante est
l'*indice de Gini*. Dans une feuille où une proportion $p$ des maisons est bleue,
il vaut $2p(1-p)$, soit 0 pour une feuille pure et 0,5 pour une feuille
moitié-moitié. Le score d'une question est la moyenne des indices de ses deux
côtés, pondérée par leur taille. Sur nos maisons, l'indice de départ vaut 0,48,
et il descend à 0,18 après la question sur la distance. Une autre mesure,
l'*entropie*, issue de la théorie de l'information, donne presque toujours le
même arbre.
{{% /hint %}}

## Un arbre qui prédit un nombre

Rien de ce qui précède ne dépend du fait que la réponse soit une catégorie.
Reprenons la première question du module, le prix, avec une seule
caractéristique, la superficie. Un arbre peut la traiter de la même façon. Il
pose des questions sur la superficie et, dans chaque feuille, il donne le **prix
moyen** des maisons qui s'y trouvent au lieu d'une couleur majoritaire. Seule la
mesure du mélange change. On regarde à quel point les prix d'une feuille sont
dispersés autour de leur moyenne, et la meilleure question est celle qui réduit
le plus cette dispersion de chaque côté.

Voici l'arbre à deux niveaux appris sur nos vingt maisons. La première question
est « plus de 194 m² ? ». Pour les petites maisons, la question suivante est
« plus de 154 m² ? » et, pour les grandes, « plus de 237 m² ? ». On obtient
quatre feuilles et quatre prix : 308 000, 430 000, 557 000 et 706 000 \\$.

{{< image src="/images/module2/arbre-prix-escalier.svg" alt="Le nuage des maisons (superficie, prix) avec, en pointillé pâle, la droite ajustée, et en trait plein brun un escalier à quatre marches : l'arbre de régression à deux niveaux de questions coupe la superficie à 194 m², puis à 154 et à 237, et prédit dans chaque intervalle le prix moyen des maisons qui s'y trouvent." title="L'arbre de régression, dessiné sur le nuage : un escalier à quatre paliers, un par feuille. En pointillé, la droite, pour comparer." loading="lazy" >}}

Dessiné sur le nuage, l'arbre forme un **escalier** : quatre paliers
horizontaux, un par feuille, avec une marche à chaque seuil. Cette courbe ne
monte pas de façon continue, elle avance par sauts. Par exemple, entre 154 et
194 m², toutes les maisons valent 430 000 \\$, qu'elles fassent 155 ou 193 m².
Pourtant, avec ses quatre paliers, l'escalier suit déjà mieux le nuage que la
droite d'[*Un modèle qui s'entraîne*](docs/module2/50-entrainer-un-modele) :
son erreur moyenne est de 32 000 \\$, contre 41 000 pour la droite. Avec un
niveau de plus, soit huit paliers, l'erreur descend à 23 000 \\$.

Cette comparaison met en évidence les différences entre les deux modèles. La
droite suppose une forme précise, la ligne droite, et ne peut rien représenter
d'autre. Si les prix suivaient une courbe, elle ne pourrait pas la suivre.
L'escalier ne suppose aucune forme : avec assez de marches, il peut s'adapter à
n'importe quelle forme. C'est sa force. Cependant, chaque palier est calculé sur
un petit nombre de maisons, cinq ici, et c'est aussi sa faiblesse. La droite
résume ses vingt maisons en deux nombres, alors que l'escalier les découpe en
petits groupes traités séparément. De plus, l'escalier ne peut pas
extrapoler : au-delà de 280 m², il répond toujours 706 000 \\$, alors que la
droite continue de monter. Nous verrons dans [*Bien évaluer un
modèle*](docs/module2/75-bien-evaluer) qu'on ne peut pas dire lequel des deux a
raison hors du nuage, car aucun des deux n'offre de garantie dans cette zone.

Un arbre de régression utilise donc les mêmes questions et les mêmes feuilles
qu'un arbre de classification, avec une moyenne à la place d'un vote. C'est la
même distinction que celle que kNN avait présentée à sa dernière étape.

## Jusqu'où laisser pousser l'arbre ?

Revenons à la classification et laissons l'arbre poser d'autres questions. Après
« à plus de 11 km du centre ? », il cherche une question dans chaque feuille,
puis dans chaque nouvelle feuille, jusqu'à ce qu'aucune feuille ne mélange plus
les couleurs. Voici l'arbre obtenu sur trois niveaux :

{{< image src="/images/module2/arbre-maisons-profond.svg" alt="L'arbre laissé pousser sur trois niveaux : après « à plus de 11 km du centre ? », il pose des questions sur l'année puis sur la distance jusqu'à isoler chacune des deux exceptions dans une feuille à elle. Six feuilles, chacune annotée du nombre de maisons vendues vite sur le nombre de maisons de la feuille : plus aucune erreur sur les vingt maisons." title="Le même arbre, laissé pousser sur trois niveaux : six feuilles, zéro erreur, et une feuille sur mesure pour chaque exception." loading="lazy" >}}

L'arbre compte maintenant six feuilles et ne fait plus aucune erreur. Il a
trouvé le moyen de traiter les deux exceptions. Une question sur l'année, puis
une question sur la distance, isolent dans sa propre feuille la maison ancienne
qui s'est vendue vite. Deux questions de plus isolent de même la maison récente
qui s'est vendue lentement. Dans le plan, chaque question ajoute une coupe, et
la frontière devient un assemblage de rectangles :

{{< image src="/images/module2/arbre-maisons-frontiere-profond.svg" alt="Le même plan distance × année, découpé par plusieurs coupes verticales et horizontales en rectangles teintés : l'arbre a isolé chacune des deux exceptions dans un petit rectangle de sa couleur, au prix d'une frontière en escalier." title="La frontière de l'arbre à trois niveaux : des rectangles, dont deux taillés sur mesure autour des exceptions." loading="lazy" >}}

Observez les deux petits rectangles découpés autour des exceptions. Ils
correspondent aux îlots que kNN dessinait avec *k* = 1, dans [*Prédire par
ressemblance*](docs/module2/40-predire-par-ressemblance/#le-choix-de-k). Il
s'agit du même phénomène, dans un autre modèle. Un arbre sans limite continue de
pousser jusqu'à ce que chaque feuille soit pure, au besoin en donnant une feuille
à chaque maison. Il s'ajuste alors aux vingt maisons dans leurs moindres détails
et traite comme des règles les deux cas qui font exception. Une nouvelle maison,
ancienne et éloignée du centre, qui tomberait dans le rectangle de l'exception
serait déclarée « vendue vite » sur la base d'un seul exemple.

Il faut donc, pour l'arbre comme pour kNN, régler un paramètre : la
**profondeur**, c'est-à-dire le nombre de questions que l'arbre peut poser à la
suite. Avec une profondeur trop faible, l'arbre est grossier : sur des données où
les deux amas seraient moins nets, une seule coupe verticale ne suffirait pas.
Avec une profondeur trop grande, il apprend les exemples par cœur. C'est le
sur-apprentissage (*overfitting*) déjà observé avec kNN, sous une autre forme, et
[*Généraliser*](docs/module2/70-generaliser) en fera son sujet principal. La
bonne profondeur se situe entre les deux : elle permet de saisir les vraies
régularités sans reproduire les cas accidentels. Rien, dans les vingt maisons,
n'indique quelle est cette profondeur. Nous avons rencontré ce problème avec *k*,
et nous le retrouverons pour tous les modèles dans
[*Généraliser*](docs/module2/70-generaliser), où l'arbre servira d'exemple
principal. Pour l'instant, retenez les deux façons de limiter un arbre : fixer
une profondeur maximale, ou le laisser pousser puis **l'élaguer**, c'est-à-dire
supprimer après coup les branches qui n'apportent que du détail.

L'applet ci-dessous vous permet d'en faire l'expérience. Elle présente des points
rouges et bleus, un arbre appris en direct et le fond correspondant dans le plan.
À droite, l'arbre lui-même se redessine à chaque changement. Faites varier la
profondeur maximale de 1 à 8 et observez les rectangles se multiplier autour des
points isolés. Ajoutez un point d'une couleur au milieu de l'autre couleur et
observez comment l'arbre s'adapte. Survolez une zone du plan pour voir son chemin
s'allumer dans l'arbre.

{{< applet src="/html/applets/decision-tree.html" height="605" >}}

## L'arbre du *Titanic*

Passons maintenant de nos maisons à des données réelles, celles que nous
utiliserons à propos des fuites dans [*Bien évaluer un
modèle*](docs/module2/75-bien-evaluer) : la liste des 1309 passagers du
*Titanic*, avec pour chacun la classe, le sexe, l'âge et l'indication de sa
survie. Trente-huit pour cent des passagers ont survécu. Le modèle le plus
bête, qui répond « tout le monde meurt », obtient donc 62 % de bonnes réponses.
Il sert de point de comparaison. Laissons un arbre apprendre sur ces passagers,
avec deux niveaux de questions :

{{< image src="/images/module2/arbre-titanic.svg" alt="Un arbre à deux niveaux appris sur les 1309 passagers du Titanic. Première question : une femme ? Pour les hommes, la question suivante est « plus de 9 ans ? » : les garçons (43) ont survécu à 58 %, les hommes adultes (800) à 17 %. Pour les femmes, « en troisième classe ? » : celles de première ou deuxième classe (250) ont survécu à 93 %, celles de troisième (216) à 49 %." title="L'arbre du Titanic, appris sur les vraies données : trois questions, 79 % de bonnes réponses, et une histoire qu'on peut lire." loading="lazy" >}}

La première question que l'arbre trouve, sans aucune indication, est « une
femme ? ». À elle seule, elle donne 78 % de bonnes réponses, soit seize points de
plus que le modèle de comparaison. Les deux branches posent ensuite des questions
différentes. Pour les hommes, la question est « plus de 9 ans ? » : les
43 garçons ont survécu à 58 %, les 800 hommes adultes à 17 %. Pour les femmes, la
question est « en troisième classe ? » : celles de première et de deuxième classe
ont survécu à 93 %, celles de troisième classe à 49 %. Avec trois questions,
l'arbre obtient 79 % de bonnes réponses.

Ce que cet arbre a appris peut être lu par tous : « les femmes et les enfants
d'abord », la consigne donnée cette nuit-là, avec une nuance que les historiens
confirment. Les femmes de troisième classe, logées dans les entreponts, loin des
canots, ont eu une chance sur deux de survivre. L'arbre n'a utilisé aucune
source historique. Il a seulement compté, et il retrouve en trois questions ce
que les historiens décrivent. Cet exemple montre aussi le comptage appliqué à un
cas ambigu. La feuille des femmes de troisième classe, à 49 %, est presque
moitié-moitié, et l'arbre y répond « a péri » à une voix près. Un niveau de plus
la découperait selon l'âge, sans gain important : au-delà de trois questions, le
taux de bonnes réponses ne change presque plus. Sur ces données, l'essentiel tient
en trois questions, et le reste est du détail.

Un dernier point sera repris dans [*Bien évaluer un
modèle*](docs/module2/75-bien-evaluer) : ce taux de 79 % a été mesuré sur les
passagers qui ont servi à l'apprentissage. Sur un jeu de test, il serait un peu
plus bas, et avec un arbre plus profond, l'écart serait plus grand.

## Ce qu'un arbre dit, et ce qu'il tait

Comme l'a montré l'exemple du *Titanic*, la grande force de l'arbre est qu'il
peut **expliquer** ses décisions. Pour toute prédiction, le chemin de la racine à
la feuille constitue la justification, et elle se lit directement : « une femme,
en troisième classe, donc une chance sur deux ». Cette propriété s'appelle
l'**explicabilité** (ou *interprétabilité* ; en anglais *explainability*,
*interpretability*). C'est la capacité d'un modèle à rendre compte de ses
décisions dans des termes qu'un humain peut comprendre, vérifier et contester.
L'arbre est l'un des modèles les plus explicables, parce que le modèle est
lui-même son explication : en le lisant, on sait pourquoi il donne telle
réponse.

Aucun autre modèle de ce module n'offre cette propriété au même degré. La droite
donne une pente, qui se comprend facilement. La régression logistique donne des
poids associés à chaque caractéristique, qu'il faut interpréter. kNN donne une
liste de voisins, qui décrit la décision sans la justifier. Les grands réseaux de
neurones du [Module 3](docs/module3/90-tromper-un-reseau/#une-boîte-noire) n'offriront rien de comparable : ils
comptent des milliards de paramètres, dont aucun n'a de sens pris isolément. On
parle alors de **boîte noire** : le modèle répond, souvent très bien, mais
personne ne peut dire pourquoi. Tout un domaine de recherche, l'*IA explicable*
(*XAI*, pour *explainable AI*), cherche aujourd'hui à analyser ces modèles après
coup, en déterminant quelles caractéristiques ont compté dans une décision.
L'arbre, lui, n'a pas besoin de cette analyse.

L'enjeu n'est pas seulement théorique. Dans les domaines où une décision doit
pouvoir être contestée (un prêt refusé, un diagnostic, un dossier trié, une peine
évaluée), un modèle qui ne peut pas expliquer ses décisions est difficile à
accepter. La lisibilité compte alors davantage que quelques points de
performance. C'est l'une des raisons pour lesquelles les arbres, apparus dans les
années 1960 et mis au point en 1984 par quatre statisticiens (c'est la méthode
CART, celle que nous avons suivie ici), sont toujours utilisés. Nous retrouverons
cette opposition entre performance et explicabilité avec les grands modèles de
langage du [Module 4](docs/module4).

Les faiblesses de l'arbre découlent de sa méthode. D'abord, un arbre est
**instable**. Rappelez-vous l'[égalité entre la distance et l'année](#comment-larbre-choisit-ses-questions) : si l'on
retire deux maisons, la première question peut changer, et tout l'arbre avec
elle. Deux jeux de données presque identiques peuvent produire deux arbres très
différents, qui font pourtant à peu près les mêmes prédictions. Ensuite, ses
coupes sont toujours parallèles aux axes, puisqu'une question ne porte que sur
une caractéristique. Pour séparer deux amas le long d'une **diagonale**, l'arbre
doit construire un escalier de nombreuses coupes, alors qu'une simple droite,
comme celle de la régression logistique, y parviendrait en une fois. L'arbre est
donc un modèle non linéaire, mais d'un type particulier, fait de marches.

La solution à l'instabilité est l'une des idées les plus productives du domaine,
et elle se résume simplement : si un arbre est fragile, on en utilise **cent**.
On entraîne des centaines d'arbres, chacun sur une variante des données (un
tirage au sort des maisons, un sous-ensemble des caractéristiques), puis on les
fait voter ou on fait la moyenne de leurs réponses. Comme les erreurs des arbres
sont différentes, elles se compensent, et la réponse collective est plus stable
et plus juste que celle d'un arbre seul. C'est la **forêt aléatoire** (*random
forest*), proposée par Leo Breiman en 2001. Une méthode apparentée et plus
élaborée, le *gradient boosting*, construit chaque arbre de façon à corriger les
erreurs des précédents. Sur des données en tableau, comme nos maisons ou les
passagers du *Titanic*, ces méthodes restent aujourd'hui parmi les plus
performantes, et elles remportent la plupart des compétitions Kaggle dont parle
[*Bien évaluer un modèle*](docs/module2/75-bien-evaluer). Elles perdent
cependant la lisibilité de l'arbre seul, car on ne peut pas lire cent arbres
comme on en lit un.

La figure suivante illustre cette idée sur nos maisons. Trois arbres, chacun
appris sur une partie des vingt maisons tirée au sort et laissé pousser sans
limite, produisent trois frontières très différentes, avec des bandes et des
îlots à des endroits différents. Si l'on fait voter cinquante arbres de ce type,
ces particularités s'annulent, et il ne reste que ce sur quoi les arbres
s'accordent.

{{< image src="/images/module2/foret-aleatoire.svg" alt="En haut, trois petits plans distance × année : trois arbres, chacun appris sur une partie seulement des vingt maisons, tirée au sort (les maisons laissées de côté sont dessinées en creux, et un compte indique combien l'arbre en a vues), et laissé pousser librement, avec des frontières en rectangles toutes différentes et des îlots à des endroits différents. En bas, un plan plus grand : la frontière obtenue en faisant voter cinquante arbres de ce genre, plus régulière, où les bandes et les îlots des arbres isolés se sont fondus, ne laissant que deux petits îlots autour des exceptions." title="La forêt aléatoire : chaque arbre ne voit qu'une partie des maisons et se trompe différemment ; le vote de cinquante arbres garde ce sur quoi ils s'accordent." loading="lazy" >}}

{{% hint info %}}
**Deux cultures.** Leo Breiman, l'inventeur de la forêt aléatoire, était un
statisticien venu à l'apprentissage automatique. Il a tiré de ce parcours un
texte devenu classique, [« Statistical Modeling: The Two
Cultures »](https://projecteuclid.org/journals/statistical-science/volume-16/issue-3/Statistical-Modeling--The-Two-Cultures-with-comments-and-a/10.1214/ss/1009213726.full)
(2001), annoncé dans la page d'accueil de ce module. Selon sa thèse, deux
cultures se partagent l'analyse des données. La première, celle de la
statistique classique, suppose que les données ont été produites par un
mécanisme simple qu'un modèle lisible peut décrire, et elle évalue le modèle
selon sa fidélité supposée à ce mécanisme. La seconde, celle de l'apprentissage
automatique, considère le mécanisme comme inconnu et n'évalue un modèle que sur
la qualité de ses prédictions sur des données nouvelles. L'arbre seul appartient
à la première culture, la forêt à la seconde. Breiman parle d'un **dilemme
d'Occam**. Le rasoir d'Occam recommande de choisir le modèle le plus simple, mais
sur des données réelles le modèle le plus précis est rarement le plus simple, et
il faut alors choisir entre comprendre et prédire, alors qu'on voudrait les deux.
Breiman relevait aussi une conséquence qu'il appelait l'**effet Rashomon**, du
nom du film où quatre témoins racontent quatre versions du même crime : sur les
mêmes données, des modèles très différents sont souvent également bons. Vous
l'avez constaté avec nos maisons, que la distance et l'année séparaient aussi
bien l'une que l'autre. Il n'existe donc pas un seul bon modèle, et l'explication
fournie par un arbre n'est qu'une explication possible parmi d'autres. Il faut
donc rester prudent envers un modèle qui s'explique : il décrit un chemin de
décision qui fonctionne, et non le mécanisme réel du monde. Nous reviendrons sur
cette question au [Module 5](docs/module5), à propos de ce que signifie
expliquer.
{{% /hint %}}

## Et sur des données neuves ?

Récapitulons. Nous disposons maintenant de plusieurs modèles : une droite qui
prédit un nombre, deux classificateurs qui prédisent une catégorie, et un arbre
qui fait les deux en posant des questions. Nous avons aussi vu deux façons de les
entraîner : minimiser une fonction d'erreur, ou chercher la question la plus
pure. Chacun de ces modèles apprend en s'ajustant le mieux possible **aux
exemples qu'on lui a montrés**.

Or ce n'est pas ce qui nous intéresse vraiment. Un filtre anti-pourriel qui
classe parfaitement les courriels d'hier (ceux qui ont servi à l'entraîner) est
inutile s'il se trompe sur ceux qui arriveront demain. Depuis le début de ce
module, le but n'est pas de mémoriser des exemples, mais d'en tirer ce qu'il faut
pour traiter des cas **encore jamais vus**.

Il y a là une difficulté. Un modèle peut ne faire aucune erreur sur ses données
d'entraînement et faire beaucoup d'erreurs sur des données nouvelles, comme un
étudiant qui aurait appris par cœur les réponses du corrigé sans comprendre la
matière. C'est le sur-apprentissage (*overfitting*), déjà rencontré deux fois,
que la page suivante, « [Généraliser](docs/module2/70-generaliser) », traite en détail. Nous venons d'en voir l'exemple le plus
net : l'[arbre laissé pousser](#jusquoù-laisser-pousser-larbre) jusqu'à isoler chaque exception, qui ne se trompe
plus sur les vingt maisons mais n'en a retenu que ce qu'il peut reproduire. Nous
avions déjà rencontré ce problème [avec kNN](docs/module2/40-predire-par-ressemblance/#le-choix-de-k) et le réglage de $k$ : trop s'ajuster
aux exemples peut être une faiblesse plutôt qu'une force.

Il faut donc savoir mesurer si un modèle a vraiment appris ou s'il a seulement
retenu les exemples, et savoir éviter ce problème. C'est la question de la
**généralisation**, qui fait l'objet de la [page suivante](docs/module2/70-generaliser).
