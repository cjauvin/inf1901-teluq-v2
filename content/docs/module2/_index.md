---
title: "Module 2 - Apprentissage automatique"
weight: 200
bookCollapseSection: true
---

# Module 2 — Apprentissage automatique

![](/images/machine-learning.webp)

## Qu'est-ce que l'apprentissage automatique ?

L'apprentissage automatique (AA, ou *machine learning*) est un ensemble de
techniques qui permettent à un ordinateur de résoudre des problèmes qu'il serait
très difficile de programmer à la main : reconnaître un chat sur une photo, estimer
le prix d'une maison, filtrer les pourriels, jouer aux échecs, converser, etc.

La différence avec la programmation classique est importante. Un programme
traditionnel encode une série de **règles** écrites par un humain. Un modèle d'AA,
au contraire, **dérive son fonctionnement à partir d'exemples** : on ne lui donne
pas la règle, on la lui fait découvrir dans les données. C'est ce passage des règles
aux exemples qui rapproche l'AA de ce qu'on appelle l'intelligence. Il le rattache
aussi au **connexionnisme**, présenté au [module
1](docs/module1/20-deux-paris) : l'hypothèse, rivale de l'approche symbolique,
selon laquelle l'intelligence ne s'écrit pas en règles explicites, mais **émerge
d'un réseau de connexions qui s'ajustent à l'expérience**. L'apprentissage
automatique reprend cette idée principale, sans nécessairement garder les neurones.
Ce qui s'ajuste ici s'appelle des **paramètres**, et c'est en les réglant sur des
exemples que le modèle finit par « savoir » quelque chose.

On peut aussi dire que les deux démarches **échangent leurs entrées et leurs
sorties**. En programmation classique, un humain écrit les règles, et l'ordinateur
les applique aux données pour produire des réponses. En apprentissage automatique,
on fournit à l'ordinateur les données **et** les réponses (ce sont les exemples), et
c'est l'ordinateur qui en dégage les règles, qu'on appelle alors le **modèle**. Ce
qui était fourni par l'humain (les règles) devient le résultat, et ce qui était le
résultat (les réponses) devient une donnée d'entrée. Le schéma ci-dessous montre
cette permutation : suivez les « règles » (en brun) et les « réponses » (en teal),
qui passent d'un côté à l'autre.

{{< image src="/images/module2/regles-vs-exemples.svg" alt="Deux schémas de flux. À gauche, « programmation classique » : on fournit à l'ordinateur les règles et les données, il produit les réponses. À droite, « apprentissage automatique » : on lui fournit les données et les réponses, il produit les règles, c'est-à-dire le modèle. Les « règles » (en brun) et les « réponses » (en teal) échangent leur place d'un panneau à l'autre." title="L'inversion au centre de l'apprentissage automatique : ce qu'on fournit et ce que l'ordinateur produit s'inversent. En programmation classique, on écrit les règles ; en AA, c'est l'ordinateur qui les découvre." loading="lazy" >}}

## Une seule grande idée, déclinée

Au lieu de présenter un catalogue d'algorithmes, ce module construit **un modèle
mental unique et transférable**, qui revient de page en page :

> partir de **données** → choisir un **modèle** (une fonction de prédiction,
> réglable par des paramètres) → mesurer son **erreur** de prédiction → régler
> les paramètres du modèle pour la **minimiser** → vérifier qu'il **généralise**
> à des cas nouveaux.

{{< image src="/images/module2/fil-conducteur.svg" alt="Le fil conducteur du module en quatre étapes, chacune expliquée sous son nom. « Données » (les exemples dont on dispose), représentées par un nuage de points. « Modèle » (une fonction de prédiction, réglable par des paramètres), représenté par une boîte-fonction « f », avec une flèche d'entrée et une flèche de sortie, surmontée de deux sliders. « Erreur » (à quel point le modèle est bon pour prédire les exemples), représentée par une cible dont le tir a manqué le centre, l'écart marqué en rouge. « Généraliser » (bien prédire des exemples jamais vus), représenté par un nouveau point marqué d'un « ? » devant une frontière. Une boucle de retour relie « erreur » à « modèle », avec l'étiquette : régler les paramètres du modèle pour minimiser l'erreur de prédiction, et répéter." title="La structure du module : données → modèle → erreur → généraliser, avec au centre la boucle d'entraînement (régler les paramètres du modèle pour minimiser l'erreur de prédiction, de façon répétée)." loading="lazy" >}}

Chaque algorithme classique présenté dans ce module, du plus simple au plus
élaboré, est une **variation** sur ce même schéma. Quand on comprend ce schéma,
l'apprentissage automatique n'est plus une boîte noire.

## Une vieille parenté : la statistique

Il faut préciser dès le départ un point que le vocabulaire actuel tend à cacher :
l'apprentissage automatique n'est pas né avec les ordinateurs, et encore moins avec
les années 2010. Presque tout ce que vous verrez dans ce module relève de la
**statistique**, parfois depuis deux siècles. La droite ajustée par les moindres
carrés date de Legendre et de Gauss, vers 1805. Le théorème de Bayes date de 1763,
et le mot *régression* lui-même a été introduit par Galton en 1886. Les plus proches
voisins, les arbres de décision et les forêts ont été développés par des
statisticiens, et les termes que nous emploierons (échantillon, distribution, biais,
variance, test) viennent de la statistique. L'autre discipline d'origine est la
**théorie des probabilités** : chaque modèle de ce module repose sur une
probabilité, une vraisemblance ou une croyance que l'on révise, et le théorème de
Bayes y joue un rôle central.

La différence entre les deux domaines tient moins aux outils qu'à la **question
posée**. La statistique classique cherche à expliquer, par exemple quel est l'effet
de la superficie sur le prix, et avec quelle certitude. L'apprentissage automatique
cherche à prédire, par exemple quel sera le prix d'une maison donnée. Pour bien
prédire, il accepte des modèles si complexes qu'on ne peut plus les interpréter,
à condition qu'ils fonctionnent bien sur des données nouvelles. Leo Breiman, un
statisticien devenu pionnier de l'apprentissage automatique, a décrit cette
divergence dans un texte connu, [« Statistical Modeling: The Two
Cultures »](https://projecteuclid.org/journals/statistical-science/volume-16/issue-3/Statistical-Modeling--The-Two-Cultures-with-comments-and-a/10.1214/ss/1009213726.full)
(2001) : il y décrit deux cultures qui partagent les mêmes fondements. Nous
signalerons cette parenté chaque fois qu'un modèle viendra directement de la
statistique.

## Le but ultime : généraliser

La notion la plus importante de l'AA, celle qui permet de l'associer au domaine de
l'intelligence, est la capacité à **généraliser**. Si on entraîne un modèle à
distinguer un chien d'un chat avec 1000 images, sa performance sur ces 1000 images a
peu d'intérêt, puisqu'il devrait les reconnaître par construction. En effet,
mémoriser ces 1000 images est **trivial** pour un ordinateur : ranger des données et
les restituer à l'identique est exactement ce qu'une machine fait sans effort, et
cela ne demande aucune intelligence. Ce qui compte, c'est la **1001ᵉ** image, que le
modèle n'a jamais vue. Un modèle qui a vraiment appris, au lieu de simplement
mémoriser, pourra la classer correctement. La question devient plus intéressante
encore si on lui montre une vache au lieu d'un chat ou d'un chien. Bien généraliser
est le véritable objectif de l'AA, et c'est l'un des sens les plus concrets qu'on
puisse donner au mot « apprendre ».

{{< image src="/images/module2/memoriser-vs-apprendre.svg" alt="Une image marquée d'un point d'interrogation se présente, et une question la trie : « fait-elle partie des 1000 images déjà vues ? ». À gauche, la branche « oui — elle est dans le lot » : une grille de vignettes dont l'une, en ambre, est celle qu'on cherchait ; « elle est là, il suffit de la retrouver ». Conclusion : facile et sans intérêt, puisqu'une machine range et retrouve des données sans effort. À droite, la branche « non — elle est inédite » : la même grille, mais l'image est à l'écart, séparée par un trait pointillé ; « elle n'est nulle part dans le lot ». Conclusion : difficile, et c'est l'enjeu principal, puisqu'il faut décider sans l'avoir jamais vue, autrement dit généraliser. En bas : un modèle s'évalue par ce qu'il fait dans le second cas." title="Les deux cas possibles pour une nouvelle image. Si elle fait partie des 1000 images déjà vues, la retrouver est trivial ; si elle est inédite, il faut décider sans précédent. C'est dans ce second cas qu'on évalue un modèle." loading="lazy" >}}

## Le parcours du module

Le module part du **modèle le plus simple possible**, puis l'améliore
progressivement : chaque étape rencontre une limite qui mène à l'idée suivante.

1. [*Le problème*](docs/module2/10-le-probleme) : prédire un prix, prédire une
   catégorie, et pourquoi c'est difficile.
2. [*Le modèle le plus bête*](docs/module2/20-modele-le-plus-bete) : toujours
   répondre la moyenne, et ce que ce point de référence nous apprend.
3. [*Regarder les données*](docs/module2/30-les-donnees) : une maison, une
   image, un courriel sont des listes de nombres, donc des points dans un
   espace.
4. [*Prédire par ressemblance*](docs/module2/40-predire-par-ressemblance) : les
   plus proches voisins, la distance, et la première frontière de décision.
5. [*Un modèle qui s'entraîne*](docs/module2/50-entrainer-un-modele) : la
   droite, la fonction d'erreur, la descente de gradient.
6. [*Classer*](docs/module2/60-classer) : la régression logistique, la marge
   des SVM, Bayes, et le filtre anti-pourriel.
7. [*Poser des questions : les arbres de décision*](docs/module2/65-arbres-de-decision) :
   un modèle qui cherche au lieu de descendre un gradient, et qui peut expliquer
   ses décisions.
8. [*Généraliser*](docs/module2/70-generaliser) : le jeu de test, ce qu'un
   modèle peut dessiner, le compromis biais-variance, la régularisation.
9. [*Bien évaluer un modèle*](docs/module2/75-bien-evaluer) : les fuites, la
   validation croisée, les métriques, la distribution.
10. [*Trois façons d'apprendre*](docs/module2/80-trois-facons-d-apprendre) :
    supervisé, non supervisé, par renforcement.

Pour situer ce module dans l'ensemble du cours : l'apprentissage automatique n'est
qu'une partie d'un domaine plus vaste, celui de l'intelligence artificielle, que le
cours parcourt module par module.

{{< image src="/images/module2/ai-venn.svg" alt="Carte en régions imbriquées de l'intelligence artificielle. À l'intérieur de « Intelligence artificielle (IA) » : d'un côté « IA classique » ; de l'autre « Apprentissage automatique (AA) » (machine learning), qui contient « Méthodes d'AA diverses » et « Réseaux de neurones / apprentissage profond », lesquels contiennent à leur tour « IA générative » et « ChatGPT ». Un repère « Module 2 » pointe vers l'ensemble « Apprentissage automatique » et vers les « Méthodes d'AA diverses », qui sont le sujet du module." title="La carte de l'IA : le Module 2 porte sur l'apprentissage automatique classique, c'est-à-dire l'ensemble « Apprentissage automatique » et, en particulier, les méthodes d'AA diverses." loading="lazy" >}}

## Objectifs

Au terme de ce module, vous devriez être en mesure de :

* distinguer clairement la programmation traditionnelle de l'apprentissage
  automatique, et situer celui-ci dans le paysage de l'IA ;
* expliquer le fil conducteur *données → modèle → erreur → minimisation →
  généralisation*, et le reconnaître dans n'importe quel algorithme ;
* décrire de l'intérieur les modèles classiques rencontrés (le modèle bête, les
  plus proches voisins, la régression linéaire et logistique, les machines à
  vecteurs de support, Bayes naïf,
  l'arbre de décision et la forêt aléatoire, k-means) et dire ce qui les
  distingue ;
* expliquer comment un modèle s'entraîne (fonction d'erreur, descente de
  gradient) et ce qu'est un hyperparamètre ;
* définir le sur-apprentissage (*overfitting*) et le sous-apprentissage, et les
  relier au compromis biais-variance, à la capacité d'un modèle (linéaire ou
  non) et à la régularisation ;
* évaluer correctement un modèle : jeu de test, fuites de données, validation
  croisée, matrice de confusion, précision et rappel, et la question de la
  distribution ;
* distinguer les trois grandes façons d'apprendre (supervisé, non supervisé,
  par renforcement) par la nature du signal dont le modèle apprend ;
* expliquer pourquoi l'explicabilité d'un modèle compte, et quels modèles
  l'offrent.

## Durée

Quatre semaines, soit environ 36 heures.

## Évaluation

Un [travail noté](docs/module2/99-travail-noté-2) (20 % de la note finale) où vous construirez, pas à pas, un
filtre anti-pourriel par classification bayésienne naïve, avec des questions
d'interprétation sur le fonctionnement de l'algorithme.
