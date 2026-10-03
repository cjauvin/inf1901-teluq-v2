---
title: "Apprendre à jouer : le renforcement profond"
weight: 80
slug: renforcement-profond
---

# Apprendre à jouer : le renforcement profond

Au
[Module 2](docs/module2/80-trois-facons-d-apprendre/#apprendre-par-lexpérience-le-renforcement),
un agent apprenait à sortir d'une petite grille par essais et erreurs. Il
remplissait une table, avec une valeur pour chaque case, et la récompense finale se
propageait peu à peu vers les cases de départ. Ce chapitre montre ce qui se passe
quand on remplace cette table par un réseau profond, et comment cette combinaison a
permis à une machine de battre les meilleurs joueurs de go.

## Les limites de la table

Rappelons le vocabulaire du Module 2. Un **agent** choisit des **actions**. Il
reçoit parfois une **récompense**, souvent longtemps après les actions qui l'ont
produite. Il apprend la **valeur** de chaque situation, c'est-à-dire la récompense
qu'il peut en espérer, et doit trouver un équilibre entre **explorer** de nouvelles
actions et **exploiter** celles qu'il connaît.

La grille du Module 2 comptait une vingtaine de cases, et la table des valeurs
tenait sur un écran. Les situations réelles sont beaucoup plus nombreuses. Une
image d'un jeu vidéo peut prendre un nombre astronomique d'états différents. Au go,
le nombre de positions possibles dépasse le nombre d'atomes de l'univers
observable. On ne peut pas remplir une table de cette taille. Et même si on le
pouvait, on ne reverrait presque jamais deux fois la même situation : la table
n'apprendrait rien d'utile.

## Remplacer la table par un réseau

La solution consiste à remplacer la table par un réseau de neurones. Le réseau
reçoit la situation, par exemple l'image de l'écran, et estime la valeur de chaque
action possible.

{{< image src="/images/module3/table-vers-reseau.svg" alt="Deux panneaux. À gauche, une grille de quatre cases sur cinq, avec une valeur écrite dans chaque case, comme la table du Module 2. À droite, un écran de jeu, avec un mur de briques, une balle et une raquette, est donné à un réseau de neurones ; le réseau produit une valeur pour chacune des trois actions possibles : aller à gauche, rester, aller à droite." title="La table du Module 2 donne une valeur par situation ; un réseau estime la valeur de chaque action, pour n'importe quelle situation." loading="lazy" >}}

Le réseau apporte ce que la table ne pouvait pas offrir : la
[généralisation](docs/module2/70-generaliser/#un-modèle-se-juge-sur-ce-quil-na-jamais-vu).
Deux situations semblables reçoivent des valeurs semblables, même si l'une d'elles
n'a jamais été rencontrée. L'agent peut donc profiter de son expérience dans des
situations nouvelles.

L'idée n'est pas nouvelle. Au début des années 1990, Gerald Tesauro, chez IBM, crée
**TD-Gammon**, un réseau de neurones qui apprend le backgammon en jouant contre
lui-même, au cours d'environ un million et demi de parties. Il atteint presque le
niveau des meilleurs joueurs du monde, et certains de ses choix modifient la façon
dont les experts humains jouent certaines positions. Mais la méthode semble alors
propre au backgammon, et elle est peu reprise pendant vingt ans.

## Atari : jouer à partir des pixels

En 2013, la jeune entreprise londonienne DeepMind présente **DQN** (*deep
Q-network*). En 2015, une version améliorée paraît dans la revue *Nature*. Le même
réseau, un
[réseau convolutif](docs/module3/50-reseaux-convolutifs/#du-filtre-au-réseau),
apprend à jouer à 49 jeux vidéo de la console Atari 2600. Il ne reçoit que les
pixels de l'écran et le score. Personne ne lui explique les règles, ni le but du
jeu. Sur une bonne partie de ces jeux, il atteint ou dépasse le niveau d'un joueur
humain expérimenté.

L'exemple le plus connu est *Breakout*, où il faut détruire un mur de briques avec
une balle. Après quelques centaines de parties, le réseau découvre une stratégie que
ses concepteurs ne lui avaient pas indiquée : creuser un tunnel sur le côté du mur,
pour envoyer la balle derrière, où elle détruit les briques toute seule.

{{< youtube id="TmPfTpjtdgg" >}}

Le réseau échoue en revanche à *Montezuma's Revenge*, un jeu d'exploration où il
faut traverser plusieurs salles avant d'obtenir le moindre point. En jouant au
hasard, l'agent ne reçoit presque jamais de récompense, et n'a donc rien à
renforcer. Le compromis entre explorer et exploiter, vu au Module 2, reste une
difficulté centrale.

## AlphaGo

Le go se joue sur un plateau de 19 lignes sur 19, le goban. Deux joueurs y posent
tour à tour des pierres noires et blanches, et cherchent à entourer le plus grand
territoire. Les règles sont simples, mais le jeu est d'une grande profondeur. En
2015, les meilleurs programmes n'atteignaient que le niveau d'un bon amateur.

La méthode de
[Deep Blue](docs/module1/30-chercher-raisonner/#lapogée-deep-blue-bat-kasparov-1997),
présentée au Module 1, ne suffisait pas, pour deux raisons. À chaque tour, un
joueur de go a environ 250 coups possibles, contre environ 35 aux échecs. L'arbre
des coups grandit donc beaucoup trop vite. Surtout, personne ne savait écrire une
bonne fonction d'évaluation pour une position de go. Les meilleurs joueurs
eux-mêmes jugent une position à l'intuition, sans pouvoir l'expliquer en règles.

**AlphaGo**, de DeepMind, combine trois éléments :

- un **réseau de politique**, qui regarde la position et propose les coups
  prometteurs. Il évite d'explorer les 250 coups possibles ;
- un **réseau de valeur**, qui regarde une position et estime qui va gagner. Il
  remplace la fonction d'évaluation que personne ne savait écrire ;
- une **recherche dans l'arbre des coups**, comme au Module 1, guidée par ces deux
  réseaux.

{{< image src="/images/module3/alphago-recherche.svg" alt="Un arbre de coups qui part de la position actuelle, en haut. Le réseau de politique désigne trois coups prometteurs, dont les branches sont explorées ; les autres coups possibles, en pointillé, sont laissés de côté. Au bout des branches explorées, le réseau de valeur estime la probabilité de gagner de chaque position. AlphaGo joue le coup dont les positions sont les mieux évaluées." title="AlphaGo : le réseau de politique choisit les coups à explorer, le réseau de valeur évalue les positions atteintes." loading="lazy" >}}

C'est la rencontre des deux traditions de ce cours : la
[recherche](docs/module1/30-chercher-raisonner/#résoudre-cest-explorer) du
Module 1, et l'apprentissage des Modules 2 et 3. Les deux réseaux sont d'abord
entraînés sur des parties de joueurs humains, en apprentissage supervisé : le
réseau de politique apprend à prédire le coup qu'un expert jouerait. Ils sont
ensuite améliorés par renforcement, AlphaGo jouant des millions de parties contre
lui-même.

En mars 2016, à Séoul, AlphaGo affronte Lee Sedol, l'un des meilleurs joueurs du
monde, en cinq parties. Il gagne 4 à 1.

Au 37e coup de la deuxième partie, AlphaGo pose une pierre sur la cinquième ligne à
partir du bord, un coup que les commentateurs prennent d'abord pour une erreur.
Selon DeepMind, AlphaGo estimait lui-même qu'un joueur humain n'aurait joué ce coup
qu'une fois sur dix mille. La suite de la partie montre qu'il était excellent.

{{< image src="/images/module3/go-coup-37.svg" alt="Un goban de 19 lignes sur 19, avec la position de la deuxième partie après 37 coups. AlphaGo a les noirs. Le coup 37, une pierre noire en P10, est entouré en rouge : elle est posée sur la cinquième ligne à partir du bord droit, loin des autres pierres de la zone." title="Le coup 37 de la deuxième partie (positions relevées d'après les diagrammes de Wikimedia Commons)." loading="lazy" >}}

Lee Sedol remporte la quatrième partie grâce à son 78e coup, au centre du goban,
que les commentateurs ont qualifié de « coup divin ». AlphaGo ne l'avait pas
envisagé, et il joue mal pendant plusieurs coups ensuite.

{{< image src="/images/module3/go-coup-78.svg" alt="Un goban de 19 lignes sur 19, avec la position de la quatrième partie après 78 coups. Lee Sedol a les blancs. Le coup 78, une pierre blanche en L11, est entourée en rouge, au milieu d'un groupe de pierres noires au centre du goban." title="Le coup 78 de la quatrième partie (positions relevées d'après une image de Axd, Wikimedia Commons, CC BY-SA 4.0)." loading="lazy" >}}

Le documentaire
[*AlphaGo*](https://www.youtube.com/watch?v=WXuK6gekU1Y) (2017), mis en ligne
gratuitement par DeepMind, raconte ce match.
