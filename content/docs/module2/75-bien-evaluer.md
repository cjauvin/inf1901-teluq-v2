---
title: "Bien évaluer un modèle"
weight: 75
slug: bien-evaluer
---

# Bien évaluer un modèle

La page « [Généraliser](docs/module2/70-generaliser/#un-modèle-se-juge-sur-ce-quil-na-jamais-vu) » a posé la règle d'or : on juge un modèle sur des exemples
qu'il n'a jamais vus. Cette règle est nécessaire, mais elle ne suffit pas. Un
score sur le jeu de test n'a de valeur que s'il est **honnête** (le modèle
n'a-t-il vraiment rien vu du test ?), **fiable** (le score dépend-il du hasard du
partage entre entraînement et test ?), **pertinent** (mesure-t-il ce qui coûte
vraiment en cas d'erreur ?) et **valable** (s'applique-t-il aux données qu'on
rencontrera réellement ?). Les quatre sections de cette page traitent ces quatre
questions. Aucune ne demande de nouveau modèle. Toutes demandent de la méthode,
et c'est surtout la méthode, bien plus que le choix d'un algorithme, qui
distingue un modèle qui fonctionne d'un modèle qui semble fonctionner.

## Le score trop beau pour être vrai : la fuite de données

Le premier piège est le plus courant et le plus difficile à repérer. Un modèle
obtient 99 % de bonnes réponses sur le jeu de test, on le met en service, et ses
résultats deviennent très mauvais. La cause est le plus souvent une **fuite de
données** : une information qui n'aurait pas dû être disponible a été utilisée
pendant l'entraînement, et le test n'était plus vraiment nouveau.

La fuite prend deux formes. La première est la **contamination** : le jeu de
test contient, sous une autre forme, des exemples que le modèle a déjà vus. Par
exemple, la même maison vendue deux fois en trois ans, une fois dans chaque
ensemble, la même photo en deux résolutions ou le même courriel transféré à
trois personnes. Le modèle ne généralise pas, il *reconnaît* les exemples, et le
score récompense sa mémoire. À grande échelle, c'est le problème des grands
modèles de langage présenté dans [l'encart de la page précédente](docs/module2/70-generaliser/#un-modèle-se-juge-sur-ce-quil-na-jamais-vu) :
quand les données d'entraînement couvrent tout le Web, on ne sait plus ce qui a
fui.

La seconde forme est moins évidente. Il s'agit d'**une caractéristique qui
contient la réponse**, ou dont on ne disposera pas au moment de prédire.
L'exemple le plus connu vient du naufrage du *Titanic*, dont la liste des
passagers est un classique des cours d'apprentissage automatique. On y prédit
qui a survécu à partir de la classe, du sexe, de l'âge et du tarif payé. La
[version complète de cette liste](https://hbiostat.org/data/repo/titanic.html),
compilée à partir de l'*Encyclopedia Titanica* et hébergée par l'Université
Vanderbilt, comporte deux colonnes de plus, le numéro du canot de sauvetage et
le numéro d'identification du corps repêché. Si on les donne au modèle, il
devient parfait, parce qu'avoir un numéro de canot signifie avoir survécu et
qu'avoir un numéro de corps signifie être mort. Le modèle n'a rien deviné, il a
lu la réponse, à peine cachée, dans les données. Nos maisons présentent le même
piège. Pour prédire le prix, la « taxe foncière » donnerait d'excellents
résultats, parce qu'elle est calculée à partir de la valeur de la maison.

{{< image src="/images/module2/fuite-de-donnees.svg" alt="Le même découpage entraînement / test que dans la page précédente, mais deux exemples du bloc de test ont un jumeau dans le bloc d'entraînement, reliés par un trait pointillé rouge : les mêmes exemples, sous une autre forme. Le modèle les reconnaît au lieu de généraliser, et le score du test est trompeur." title="Une fuite par contamination : deux exemples du test ont un jumeau dans l'entraînement. Le modèle les reconnaît, et le score récompense sa mémoire." loading="lazy" >}}

Il n'existe pas de détecteur automatique de fuites, mais il existe une méthode.
D'abord, il faut se méfier : un score exceptionnel est un signal d'alerte avant
d'être une bonne nouvelle, et la première question à poser est « qu'est-ce qui
pourrait avoir fui ? ». Ensuite, il faut appliquer une règle systématique :
**tout ce qu'on calcule à partir des données se calcule sur l'ensemble
d'entraînement seulement**, qu'il s'agisse de moyennes, d'écarts, du choix des
caractéristiques ou des réglages. Le jeu de test ne sert qu'une fois, à la fin,
comme un examen qu'on ne corrige pas en cours de route.

{{% hint info %}}
**Le jeu de test sous clé : Kaggle.** Cette méthode existe aussi sous une forme
institutionnelle. Sur [Kaggle](https://www.kaggle.com/), la plateforme de
compétitions d'apprentissage automatique, les participants reçoivent les données
d'entraînement avec leurs réponses et les données de test *sans* leurs réponses.
Les vraies réponses du test restent **privées**, et ce sont les organisateurs
qui calculent le score de chaque soumission. Personne ne peut donc, même par
erreur, entraîner son modèle sur l'examen. La plateforme va plus loin. Pendant
la compétition, le classement public n'est calculé que sur une *partie* du jeu
de test, et le classement final est calculé sur l'autre partie, gardée secrète
jusqu'à la fin. Cette mesure empêche une fuite encore moins évidente, qui
consiste à ajuster son modèle, soumission après soumission, au score affiché,
jusqu'à s'ajuster au jeu de test sans l'avoir jamais vu. Les participants
connaissent bien les changements importants de classement qui se produisent à
la fin quand les deux parties donnent des résultats différents.
{{% /hint %}}

{{% hint info %}}
**Une unité n'est pas l'autre : mettre à l'échelle.** Cette règle a une
application très concrète, que nous avons évitée sans la mentionner. Dans le
plan des maisons, kNN mesure une distance qui combine une différence de
kilomètres et une différence d'années. Or rien n'indique qu'un kilomètre
« vaut » une année. Si on avait placé la superficie en mètres carrés à côté du
nombre de chambres, un écart de 50 m² aurait été beaucoup plus important qu'un
écart d'une chambre, et la distance n'aurait plus eu beaucoup de sens. On
corrige ce problème en **mettant à l'échelle** chaque caractéristique, par
exemple en la ramenant entre 0 et 1, ou en soustrayant sa moyenne et en
divisant par son écart-type. La descente de gradient en profite aussi, car elle
fonctionne mal dans une cuvette très étirée dans une direction. La règle
s'applique ici aussi : les moyennes et les écarts utilisés pour la mise à
l'échelle se calculent sur l'entraînement, puis s'appliquent tels quels au
test.
{{% /hint %}}

## Quand les données sont rares : la validation croisée

La deuxième question porte sur la fiabilité du score. Reprenons nos vingt
maisons. Suivre la règle d'or revient à en mettre quatre de côté et à
n'apprendre que sur seize. Cela pose deux problèmes. D'abord, seize maisons,
c'est peu pour apprendre, et on voudrait utiliser les vingt. Ensuite, et
surtout, le score dépend beaucoup du choix des quatre maisons mises de côté. Si
ce sont les deux exceptions du nuage coloré, le modèle paraîtra mauvais. Si ce
sont quatre maisons typiques, il paraîtra excellent. Le hasard d'un seul
partage a donc trop d'influence.

La solution consiste à faire une **rotation** plutôt qu'un seul partage. On
divise les vingt maisons en cinq groupes de quatre. Au premier tour, le premier
groupe sert de test et les seize autres maisons servent à l'apprentissage. Au
deuxième tour, c'est le deuxième groupe qui sert de test, et ainsi de suite. On
obtient cinq tours et cinq scores, dont on calcule la moyenne. Chaque maison a
servi de test exactement une fois, et chacune a servi à l'entraînement quatre
fois sur cinq. C'est la **validation croisée**, et le nombre de groupes se
choisit librement. On en utilise le plus souvent cinq ou dix, et jusqu'à *n*
groupes d'un seul exemple quand les données sont très rares.

{{< image src="/images/module2/validation-croisee.svg" alt="Cinq rangées de vingt points, une par tour. Dans chaque rangée, seize points en vert-bleu forment l'ensemble d'entraînement et quatre points en brun, encadrés, l'ensemble de test ; le bloc de test se déplace de quatre places d'une rangée à l'autre, si bien que chaque maison sert de test exactement une fois. À droite de chaque rangée, un score ; en bas, leur moyenne." title="La validation croisée sur nos vingt maisons : cinq tours, chaque maison testée une fois, et le score final est la moyenne des cinq." loading="lazy" >}}

La validation croisée demande cinq entraînements au lieu d'un. C'est peu pour
une droite, mais beaucoup pour un très grand réseau de neurones. C'est pourquoi
on l'utilise souvent sur de petits jeux de données et presque jamais sur les
très grands, pour lesquels un seul jeu de test suffit, parce qu'il est lui-même
très grand.

La validation croisée est aussi le cadre habituel d'une opération que nous
avons faite plusieurs fois sans vraiment la nommer, le réglage de ce qui ne
s'apprend pas. Le nombre de voisins *k*, la sévérité λ de la pénalité et le
taux d'apprentissage de la descente ne sont pas des paramètres du modèle, et
aucun n'est ajusté par la descente de gradient avec les autres. Ce sont des
**hyperparamètres**, c'est-à-dire des réglages *de la procédure*, fixés avant
l'entraînement. On les choisit en essayant plusieurs valeurs et en gardant
celle qui donne le meilleur score de validation croisée. Ensuite seulement, on
utilise le jeu de test pour l'évaluation finale. C'est le rôle de l'ensemble de
validation de la [page précédente](docs/module2/70-generaliser/#un-modèle-se-juge-sur-ce-quil-na-jamais-vu), appliqué en rotation.

## Compter juste : les métriques

La troisième question est de savoir si le score mesure ce qui coûte vraiment.
Jusqu'ici, pour une catégorie, nous avons compté le **taux de bonnes
réponses**. Nous connaissons déjà son défaut. Dans [*Le modèle le plus
bête*](docs/module2/20-modele-le-plus-bete), un filtre qui ne signalait
*jamais* de pourriel obtenait 99 % de bonnes réponses, parce que les pourriels
étaient rares. Un seul nombre ne peut pas indiquer à la fois combien de
pourriels on intercepte et combien de vrais courriels on élimine. Il faut
compter ces deux quantités séparément.

Prenons 1000 courriels, dont 50 pourriels, et un filtre qui en élimine une
partie. Quatre cas sont possibles pour chaque courriel, et on les range dans un
tableau appelé la **matrice de confusion** : un pourriel éliminé (**vrai
positif**), un pourriel qui passe (**faux négatif**), un vrai courriel éliminé
(**faux positif**) et un vrai courriel conservé (**vrai négatif**). Ici,
« positif » signifie « signalé par le filtre » et n'indique pas un résultat
favorable.

Ces deux types d'erreur ne sont pas propres à l'intelligence artificielle. La
statistique les a nommés bien avant, en 1933, dans les travaux de Jerzy Neyman
et Egon Pearson. L'**erreur de première espèce** consiste à voir un effet là où
il n'y en a pas (notre faux positif), et l'**erreur de seconde espèce** consiste
à manquer un effet réel (notre faux négatif). En anglais, on parle de [*type I
and type II errors*](https://en.wikipedia.org/wiki/Type_I_and_type_II_errors).
Ces notions s'appliquent à tout test, de l'essai clinique au contrôle de qualité
en usine. Un tribunal qui condamne un innocent ou acquitte un coupable commet
ces deux types d'erreur. L'apprentissage automatique a repris ces notions avec
son propre vocabulaire.

{{< image src="/images/module2/matrice-confusion.svg" alt="Un tableau à quatre cases croisant la réalité (pourriel ou courriel légitime, en lignes) et la décision du filtre (jeté ou gardé, en colonnes), pour 1000 courriels dont 50 pourriels. Vrais positifs : 40 pourriels jetés. Faux négatifs : 10 pourriels gardés. Faux positifs : 20 courriels légitimes jetés. Vrais négatifs : 930 courriels légitimes gardés. Les deux cases d'erreur sont teintées en rouge ; sous le tableau, le taux de bonnes réponses (97 %), la précision (67 %) et le rappel (80 %)." title="La matrice de confusion : quatre cases au lieu d'un seul score. Les deux cases rouges sont les deux types d'erreur, qui n'ont pas le même coût." loading="lazy" >}}

Ce filtre obtient 97 % de bonnes réponses, alors qu'un filtre qui ne signale
jamais de pourriel en obtiendrait 95 %. Le taux global cache donc presque tout.
Le tableau permet de répondre à deux questions plus précises, qui ont chacune un
nom. La **précision** est la part de vrais pourriels parmi les courriels que le
filtre a éliminés. Ici, elle est de 40 sur 60, soit 67 %, et le reste
correspond à des courriels légitimes perdus. Le **rappel** est la part des vrais
pourriels que le filtre a interceptés. Ici, il est de 40 sur 50, soit 80 %, et
le reste est passé. On obtient ainsi deux nombres au lieu d'un, et ils varient
en sens contraire.

{{< image src="/images/module2/precision-rappel.svg" alt="À gauche, des courriels figurés par des points, rouges pour les pourriels, bleus pour les légitimes, et un lasso pointillé autour de ce que le filtre a jeté : 40 rouges et 20 bleus à l'intérieur, 10 rouges restés dehors. À droite, deux barres. La barre de la précision représente les 60 courriels jetés, dont 40 rouges : 67 %. La barre du rappel représente les 50 vrais pourriels, dont 40 attrapés : 80 %." title="Précision et rappel, avec les nombres de la matrice : deux questions, deux dénominateurs. La précision se lit à l'intérieur du lasso ; le rappel, parmi les points rouges." loading="lazy" >}}

Ces deux termes ne viennent pas non plus de l'IA, mais de la **recherche
d'information**, la discipline des catalogues de bibliothèque puis des moteurs
de recherche. Pour une requête, un bon système retourne des documents
*pertinents* sans y mêler de documents inutiles (la précision), et n'en oublie
pas (le rappel). Dès les années 1960, on a fait de ces deux mesures la
référence pour comparer les systèmes de recherche documentaire, et elles le
sont restées. [Précision et
rappel](https://fr.wikipedia.org/wiki/Précision_et_rappel) forment aujourd'hui
le vocabulaire commun de tous les systèmes qui *trient*. Un filtre
anti-pourriel est d'ailleurs une forme de recherche, puisqu'il retrouve les
pourriels parmi les courriels.

Ces deux mesures varient en sens contraire. La régression logistique de
[*Classer*](docs/module2/60-classer) donne une probabilité, et nous avons placé
le seuil de décision à 0,5. Rien n'oblige à choisir cette valeur. Avec un seuil
de 0,9, le filtre n'élimine que les courriels pour lesquels il est presque sûr,
donc la précision augmente et le rappel diminue fortement. Avec un seuil de
0,1, il élimine un courriel au moindre doute, donc le rappel augmente et la
précision diminue fortement. Le même modèle, sans nouvel entraînement, peut être
strict ou tolérant, et ce choix dépend du problème et non des mathématiques.
Pour un filtre anti-pourriel, un vrai courriel éliminé coûte plus cher qu'un
pourriel qui passe, et on favorise donc la précision. Pour un test de
dépistage, un malade non détecté coûte plus cher qu'une fausse alerte qu'un
second examen permettra d'écarter, et on favorise donc le rappel.

Le cas d'un système d'**alerte** illustre bien ce choix. Un détecteur de fumée
peut commettre deux erreurs, sonner pour un toast brûlé ou rester silencieux
pendant un incendie. La première erreur cause un désagrément. La seconde peut
coûter la maison, et parfois des vies. En raison de cette **asymétrie**, on
règle l'appareil pour qu'il ne commette *jamais* la seconde erreur, même s'il
commet souvent la première. Un détecteur de fumée se déclenche sans raison
plusieurs fois par année, et c'est voulu. Sa tolérance aux faux positifs n'est
pas un défaut de conception. C'est le prix, accepté d'avance, d'un rappel
proche de 100 %. Le filtre anti-pourriel suit le raisonnement inverse, parce
que dans son cas c'est le faux positif qui coûte cher. Avec le même modèle et
le même seuil réglable, on choisit des réglages opposés selon l'erreur qu'on ne
peut pas se permettre. Ce réglage reste toutefois délicat, parce qu'il a deux
extrêmes absurdes. Une alarme qui sonnerait *en permanence* ne manquerait aucun
incendie, et un filtre qui n'éliminerait *aucun* courriel ne perdrait aucun
message. L'une aurait un rappel parfait et l'autre une précision parfaite, mais
les deux seraient inutiles, puisqu'ils ne trieraient plus rien. Tolérer
l'erreur la moins grave ne veut donc pas dire l'accepter sans limite. On
déplace le seuil du côté le plus sûr, mais seulement jusqu'au point où l'alerte
garde un sens.

{{< image src="/images/module2/erreurs-asymetriques.svg" alt="Deux panneaux. À gauche, le détecteur de fumée : le faux positif (une alarme pour un toast brûlé) coûte un agacement, le faux négatif (un incendie sans alarme) coûte la maison ; le curseur du seuil d'alerte est placé du côté indulgent, pour ne rater aucun incendie. À droite, le filtre anti-pourriel : le faux positif (un vrai courriel jeté) coûte un message perdu, le faux négatif (un pourriel dans la boîte) coûte une seconde d'agacement ; le curseur est placé du côté strict, pour ne jeter que ce dont on est sûr." title="Le seuil se règle en fonction de l'erreur la plus grave. L'alarme tolère les fausses alertes pour ne rien manquer ; le filtre tolère les pourriels qui passent pour ne rien éliminer à tort." loading="lazy" >}}

Le [travail noté](docs/module2/99-travail-noté-2) vous posera cette question,
*quelle erreur coûte le plus ?*, à propos d'un vrai filtre.

Pour une prédiction numérique, la même question se pose, de façon plus simple.
L'erreur quadratique moyenne d'[*Un modèle qui s'entraîne*](docs/module2/50-entrainer-un-modele)
est conçue pour être *minimisée*. Ses carrés sont pratiques pour la descente de
gradient, mais difficiles à interpréter (ils sont exprimés en dollars au carré).
Pour présenter les résultats, on préfère l'**erreur absolue moyenne**. Sur nos
vingt maisons, la droite se trompe de 41 000 \\$ en moyenne, et de 59 000 \\$ au
maximum. Ces valeurs sont faciles à comprendre et permettent de juger si le
modèle convient *à l'usage prévu*. Il est excellent pour obtenir un ordre de
grandeur, mais insuffisant pour fixer un prix de vente.

Une métrique est donc un choix, qui définit ce qu'on considère comme une
réussite. Avant de lire un score, il faut toujours savoir de quelle métrique il
s'agit.

## Jamais vu, mais du même monde : la question de la distribution

La dernière question est la plus facile à oublier. Il s'agit de savoir si le
score s'applique aux données qu'on rencontrera réellement. Les sondages
permettent de bien la comprendre. Interroger mille personnes pour connaître
l'opinion de millions d'autres suppose que l'échantillon **ressemble** à la
population, c'est-à-dire qu'il en est une version réduite. Quand ce n'est pas le
cas, le sondage se trompe, même s'il paraît très sûr. L'exemple le plus connu
date de 1936. Un grand magazine américain, le [*Literary Digest*](https://en.wikipedia.org/wiki/The_Literary_Digest),
avait recueilli plus de deux millions de réponses et prédisait une nette
défaite de Roosevelt. Roosevelt fut réélu avec une large majorité. Les réponses
provenaient de listes d'abonnés au téléphone et de propriétaires d'automobiles,
en pleine crise économique. L'échantillon était très grand, mais il ne
représentait pas l'ensemble des électeurs. Ce n'est pas la quantité qui garantit
la qualité d'un sondage, c'est la **représentativité**.

Un jeu de données fonctionne comme un sondage. Nos vingt maisons ne sont pas
l'ensemble des maisons. Ce sont vingt tirages dans un ensemble beaucoup plus
vaste, celui de toutes les maisons qu'un tel modèle pourrait rencontrer, et les
statisticiens appellent cet ensemble une **distribution**. Le jeu
d'entraînement en est un échantillon, et le jeu de test en est un autre. Toute
la méthode de ce chapitre repose sur une hypothèse implicite : les deux
proviennent de la même distribution, et les données futures aussi. On dit alors
que le test est **en distribution**. Un modèle généralise toujours à cette
distribution, jamais au monde entier.

Quand cette hypothèse n'est plus vraie, c'est-à-dire quand une donnée est **hors
distribution**, le problème peut prendre trois formes.

- **L'extrapolation.** Nos maisons vont de 112 à 280 m². Si on demande à la
  droite le prix d'un manoir de 600 m², elle répond 1 696 000 \\$, avec la même
  assurance que pour une maison de 180 m². Cependant, aucune donnée ne justifie
  cette réponse. La droite est prolongée hors de la zone couverte par les
  données, et rien n'indique que les manoirs suivent la même règle que les
  bungalows.
- **Le changement de lieu ou de population.** Un modèle entraîné sur les ventes
  de Montréal est appliqué à Vancouver, ou un test de dépistage mis au point
  sur des adultes est appliqué à des enfants. Les caractéristiques sont les
  mêmes, mais la distribution est différente, et le score obtenu dans un
  contexte ne dit rien de l'autre.
- **La dérive dans le temps.** Un filtre anti-pourriel entraîné sur les
  pourriels de 2010 est confronté à ceux de 2025. Les mots et les procédés ont
  changé. La distribution s'est modifiée sans que le modèle le détecte, et son
  score passé ne dit plus rien de sa performance actuelle.

{{< image src="/images/module2/hors-distribution.svg" alt="Le nuage des vingt maisons (de 112 à 280 m²) et sa droite, avec la zone couverte par les données ombrée. Loin à droite, un manoir de 600 m² pour lequel la droite, prolongée en pointillé, annonce environ 1 696 000 dollars, accompagné d'un point d'interrogation : le modèle répond avec la même assurance, mais aucune donnée ne le justifie." title="Hors distribution : dans la zone couverte par les données, le score du test a un sens ; au-delà, la droite donne encore une réponse, mais rien ne la justifie." loading="lazy" >}}

Ces trois cas reproduisent la situation du *Literary Digest* : un échantillon,
parfois très grand, mais qui ne provient pas de la population sur laquelle on
fait les prédictions. On en tire deux règles pratiques. D'abord, le jeu de test
doit ressembler aux données du **déploiement**, et pas seulement à celles de
l'entraînement. Si le modèle doit servir à Vancouver, il faut des maisons de
Vancouver dans le test, et on constatera rapidement qu'il en faut aussi dans
l'entraînement. Ensuite, un modèle mis en service doit être **surveillé**,
parce que le monde change et que rien, dans le modèle, n'indiquera que la
distribution a changé.

Au début du module, la question de la 1001ᵉ image était de savoir si elle
faisait partie des 1000. Une autre question s'y ajoutait : l'image provient-elle
de la même distribution que les 1000 autres ? Une photo prise de nuit, alors que
toutes les autres ont été prises de jour, est nouvelle d'une façon que le modèle
ne sait pas traiter. Pour les grands modèles de langage présentés dans l'encart
de [*Généraliser*](docs/module2/70-generaliser/#un-modèle-se-juge-sur-ce-quil-na-jamais-vu),
la question devient très difficile : quand l'entraînement porte sur tout le Web,
où se trouve la limite de ce qui est « en distribution » ?

Une dernière conséquence dépasse le plan technique. Un modèle apprend *ce qui se
trouve* dans ses données, et non ce qui devrait s'y trouver. Si les vingt
maisons du registre viennent toutes des mêmes quartiers, le modèle reproduira
leurs particularités. De même, si des décisions humaines passées ont laissé des
traces dans les exemples (des prêts refusés plus souvent à certains groupes, des
dossiers triés selon des habitudes que personne n'a jamais écrites), le modèle
apprendra ces habitudes avec le reste, sans que cela soit visible, et les
appliquera de façon systématique. C'est le **biais des données**. Il ne se
mesure sur aucun jeu de test, puisque le test provient des mêmes données. Un
score honnête, fiable, pertinent et valable peut donc correspondre à un modèle
injuste. C'est une raison de plus d'examiner la provenance des données, et pas
seulement leur quantité. Le [Module 5](docs/module5) reviendra sur cette
question.

## Tout cela portait un nom : l'apprentissage supervisé

Depuis la [première page de ce module](docs/module2/10-le-probleme), un élément n'a jamais changé, et nous
l'avons à peine remarqué : **la bonne réponse était toujours fournie.** Chaque
maison avait son prix, chaque courriel son étiquette (pourriel ou non) et chaque
point sa couleur. Le modèle devait seulement apprendre à passer de la question
à une réponse *fournie d'avance*.

Cette situation porte un nom, que nous pouvons maintenant introduire après
l'avoir étudiée en détail : l'**apprentissage supervisé**. Le terme
« supervisé » renvoie à un élève corrigé par un professeur qui connaît la
réponse attendue. Régression ou classification, droite ou Bayes, paramétrique
ou non, tout ce que nous avons construit appartient à cette grande famille,
celle de l'apprentissage à partir d'exemples **étiquetés**.

Il reste à savoir d'où vient cette réponse fournie d'avance. Quelqu'un a dû
étiqueter ces milliers d'exemples un à un, un travail souvent long et coûteux,
et parfois impossible. Ce travail est si important qu'il est devenu une
**industrie à part entière**, celle de l'*étiquetage de données*. Des
entreprises comme Scale AI (dans laquelle Meta a investi une quinzaine de
milliards de dollars en 2025), Appen, Sama ou Labelbox, ou des plateformes comme
le Mechanical Turk d'Amazon, emploient ou mobilisent des centaines de milliers
de personnes pour tracer des contours sur des images, transcrire des
enregistrements, classer des textes et, depuis l'arrivée des grands modèles de
langage, comparer et noter des réponses générées. Ce travail, souvent invisible
et mal payé, est réalisé en bonne partie au Kenya, aux Philippines ou au
Venezuela. Il constitue la face cachée de l'apprentissage supervisé, puisque
chaque « bonne réponse » fournie au modèle a été produite par un humain. Par
ailleurs, la plupart des données disponibles n'ont *pas* d'étiquette : des
millions de photos que personne n'a triées, des historiques d'achats sans
catégories, des textes non classés. On peut se demander si un modèle peut
apprendre quelque chose de données brutes, sans aucune bonne réponse. À
l'inverse, quand un robot apprend à marcher, personne ne lui indique le « bon »
mouvement à chaque instant. Il reçoit seulement un encouragement ou constate une
chute, souvent bien plus tard. On peut se demander s'il s'agit encore
d'apprentissage.

C'est bien de l'apprentissage, mais d'un autre type. Ces situations se
distinguent par la nature du **signal** à partir duquel le modèle apprend : une
réponse fournie, une structure à découvrir sans guide ou une récompense
différée. Le chapitre suivant, « [Trois façons d'apprendre](docs/module2/80-trois-facons-d-apprendre) », présente cette typologie et les nouvelles
possibilités qu'elle ouvre.
