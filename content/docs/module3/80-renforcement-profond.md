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
reçoit parfois une **récompense** (*reward*), souvent longtemps après les actions
qui l'ont produite. Il apprend la **valeur** de chaque situation, c'est-à-dire la
récompense qu'il peut en espérer, et doit trouver un équilibre entre **explorer** de
nouvelles actions et **exploiter** celles qu'il connaît.

La grille du Module 2 comptait une vingtaine de cases, et la table des valeurs
tenait sur un écran. Les situations réelles sont beaucoup plus nombreuses. Une
image d'un jeu vidéo peut prendre un nombre astronomique d'états différents. Au go,
le nombre de positions possibles dépasse le nombre d'atomes de l'univers
observable. On ne peut pas remplir une table de cette taille. Et même si on le
pouvait, on ne reverrait presque jamais deux fois la même situation : la table
n'apprendrait rien d'utile.

## Remplacer la table par un réseau

La solution consiste à remplacer la table par un réseau de neurones. Le réseau reçoit la situation, par exemple l'image de l'écran, et estime
la valeur de chaque action possible.

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
[réseau convolutif](docs/module3/50-reseaux-convolutifs/#du-filtre-au-réseau), apprend à jouer à 49 jeux vidéo de la console
Atari 2600. Il ne reçoit que les pixels de l'écran et le score. Personne ne lui
explique les règles, ni le but du jeu. Sur une bonne partie de ces jeux, il atteint
ou dépasse le niveau d'un joueur humain expérimenté.

L'exemple le plus connu est *Breakout*, où il faut détruire un mur de briques avec
une balle. Après quelques centaines de parties, le réseau découvre une stratégie que
ses concepteurs ne lui avaient pas indiquée : creuser un tunnel sur le côté du mur,
pour envoyer la balle derrière, où elle détruit les briques toute seule.

{{< youtube id="TmPfTpjtdgg" >}}

Le réseau échoue en revanche à *Montezuma's Revenge*, un jeu d'exploration où il
faut traverser plusieurs salles avant d'obtenir le moindre point. En jouant au
hasard, l'agent ne reçoit presque jamais de récompense, et n'a donc rien à
renforcer. Le compromis entre explorer et exploiter (*exploration-exploitation
trade-off*), vu au Module 2, reste une difficulté centrale.

## AlphaGo

Le go se joue sur un plateau de 19 lignes sur 19, le goban. Deux joueurs y posent
tour à tour des pierres noires et blanches, et cherchent à entourer le plus grand
territoire. Les règles sont simples, mais le jeu est d'une grande profondeur. En
2015, les meilleurs programmes n'atteignaient que le niveau d'un bon amateur.

La méthode de
[Deep Blue](docs/module1/30-chercher-raisonner/#lapogée-deep-blue-bat-kasparov-1997),
présentée au Module 1, ne suffisait pas, pour deux raisons. À chaque tour, un
joueur de go a environ 250 coups possibles, contre environ 35 aux échecs. L'arbre
des coups (*game tree*) grandit donc beaucoup trop vite. Surtout, personne ne savait
écrire une bonne fonction d'évaluation (*evaluation function*) pour une position de
go. Les meilleurs joueurs eux-mêmes jugent une position à l'intuition, sans pouvoir
l'expliquer en règles.

**AlphaGo**, de DeepMind, combine trois éléments :

- un **réseau de politique** (*policy network*), qui regarde la position et propose
  les coups prometteurs. Il évite d'explorer les 250 coups possibles ;
- un **réseau de valeur** (*value network*), qui regarde une position et estime qui
  va gagner. Il remplace la fonction d'évaluation que personne ne savait écrire ;
- une **recherche dans l'arbre des coups** (*tree search*), comme au Module 1,
  guidée par ces deux réseaux.

{{< image src="/images/module3/alphago-recherche.svg" alt="Un arbre de coups qui part de la position actuelle, en haut. Le réseau de politique désigne trois coups prometteurs, dont les branches sont explorées ; les autres coups possibles, en pointillé, sont laissés de côté. Au bout des branches explorées, le réseau de valeur estime la probabilité de gagner de chaque position. AlphaGo joue le coup dont les positions sont les mieux évaluées." title="AlphaGo : le réseau de politique choisit les coups à explorer, le réseau de valeur évalue les positions atteintes." loading="lazy" >}}

C'est la rencontre des deux traditions de ce cours : la
[recherche](docs/module1/30-chercher-raisonner/#résoudre-cest-explorer) du
Module 1, et l'apprentissage des Modules 2 et 3. AlphaGo montre aussi que
l'[assemblage](docs/module3/42-materiel-et-outils/#un-jeu-de-construction) ne se limite pas aux réseaux : on peut brancher des réseaux de
neurones sur un algorithme classique, ici une recherche, et chacun fait ce qu'il fait
le mieux. Les deux réseaux sont d'abord
entraînés sur des parties de joueurs humains, en apprentissage supervisé
(*supervised learning*) : le réseau de politique apprend à prédire le coup qu'un
expert jouerait. Ils sont ensuite améliorés par renforcement, AlphaGo jouant des millions de parties contre lui-même.

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

Le documentaire *AlphaGo* (2017), mis en ligne gratuitement par DeepMind, raconte ce
match. Il dure environ une heure et demie, en anglais.

{{< youtube WXuK6gekU1Y >}}

## AlphaZero : sans parties humaines

En 2017, DeepMind présente **AlphaGo Zero**. Il ne voit aucune partie humaine. Il
ne connaît que les règles du go, et apprend uniquement en jouant contre lui-même,
en partant de coups joués au hasard. En trois jours, il joue près de cinq millions
de parties contre lui-même, puis bat la version qui avait vaincu Lee Sedol par
100 parties à 0. Les joueurs qui ont étudié ses parties y ont trouvé des
ouvertures que les humains n'avaient jamais jouées en plusieurs siècles.

La même année, **AlphaZero** applique la même méthode, sans modification, aux
échecs et au shogi, les échecs japonais. Après quelques heures d'entraînement pour
chacun, il dépasse les meilleurs programmes de ces jeux.

Le contraste avec
[Deep Blue](docs/module1/30-chercher-raisonner/#lapogée-deep-blue-bat-kasparov-1997)
est instructif. La fonction d'évaluation de Deep Blue avait été réglée pendant des
années avec l'aide de grands maîtres, et Deep Blue examinait environ 200 millions
de positions par seconde. AlphaZero a appris seul sa fonction d'évaluation, et il
examine environ 80 000 positions par seconde, plus de deux mille fois moins, parce
que son réseau de politique lui indique où chercher. C'est l'illustration la plus
nette de la [leçon amère](docs/module3/40-apprentissage-profond/#la-leçon-amère) :
une méthode générale, l'apprentissage par auto-jeu (*self-play*), dépasse le savoir
humain inscrit à la main.

## Une machine qui apprend en jouant contre elle-même

L'applet ci-dessous applique ce principe au morpion. La machine ne connaît que les
règles. Elle tient une table : pour chaque position, une valeur entre −1 et +1, qui
indique si cette position mène plutôt à la défaite ou à la victoire du joueur qui
vient de jouer. À chaque partie d'entraînement contre elle-même, elle joue le coup
qui mène à la meilleure valeur connue, sauf de temps en temps où elle essaie un
coup au hasard. À la fin de la partie, elle rapproche la valeur de chaque position
jouée du résultat obtenu.

Le morpion ne compte que quelques milliers de positions. Une table suffit donc, et
il n'est pas nécessaire d'utiliser un réseau. Mais le principe de l'auto-jeu est
celui d'AlphaZero.

{{< applet src="/html/applets/morpion.html" height="420" >}}

1. Avant tout entraînement, mesurez le niveau de la machine. Elle joue au hasard,
   et perd la plupart de ses parties contre un joueur parfait.
2. Entraînez-la par étapes, 100 parties, puis 1 000, puis plusieurs fois 10 000, et
   observez son niveau progresser. Le « joueur parfait » de l'applet calcule tous
   les coups possibles jusqu'à la fin de la partie, avec la méthode
   [minimax](docs/module1/30-chercher-raisonner/#lexplosion-combinatoire) du
   Module 1. Contre lui, le mieux possible est la partie nulle.
3. Jouez contre elle après chaque étape. Cochez « voir ce qu'elle pense de chacun
   de vos coups » pour voir les valeurs de sa table.

Quelques dizaines de milliers de parties suffisent pour qu'elle ne perde plus.
Personne ne lui a montré de bon coup.

## Au-delà des jeux, et les limites

Les jeux sont un terrain d'essai commode : les règles sont claires, la récompense
est nette, et l'on peut jouer des millions de parties. Le renforcement profond
(*deep reinforcement learning*) a aussi trouvé des usages hors des jeux.

- En 2016, Google l'utilise pour piloter le refroidissement de ses centres de
  données, et annonce une réduction d'environ 40 % de l'énergie consacrée au
  refroidissement.
- En 2022, DeepMind et l'École polytechnique fédérale de Lausanne l'utilisent pour
  contrôler la forme du plasma dans un réacteur expérimental de fusion nucléaire.
- En robotique, des robots apprennent à marcher ou à manipuler des objets, d'abord
  dans une simulation, puis dans le monde réel.

La méthode a aussi des limites importantes.

**Elle demande énormément d'essais.** AlphaGo Zero a joué près de cinq millions de
parties contre lui-même en trois jours. Un joueur humain de haut niveau en joue
quelques dizaines de milliers dans toute sa vie. Dans le monde réel, où chaque
essai prend du temps ou peut causer des dégâts, ce besoin est un obstacle.

**Elle optimise exactement la récompense qu'on lui donne.** En 2016, OpenAI
entraîne un agent sur un jeu de course de bateaux, où l'on gagne des points en
passant sur des cibles. L'agent découvre qu'il peut tourner en rond autour de trois
cibles qui réapparaissent, et accumuler plus de points qu'en finissant la course.
Il fait exactement ce qu'on lui a demandé, et pas du tout ce qu'on voulait. Ce
problème de la récompense mal définie concerne tous les systèmes qui optimisent un
objectif. Le [Module 5](docs/module5) y reviendra, sous le nom d'**alignement**.

Le renforcement a enfin une place importante dans les grands modèles de langage, comme l'annonçait le
[Module 2](docs/module2/80-trois-facons-d-apprendre/#apprendre-par-lexpérience-le-renforcement).
Il sert à ajuster leurs réponses selon les préférences d'évaluateurs humains, et à
les entraîner à raisonner sur des problèmes dont la réponse peut être vérifiée. Le
[Module 4](docs/module4/70-du-modele-a-l-assistant/#le-renforcement-à-partir-de-préférences-humaines) présentera ces méthodes.

Les réseaux profonds voient, lisent et jouent désormais mieux que nous dans
plusieurs domaines. Le dernier chapitre, « [Tromper un réseau](docs/module3/90-tromper-un-reseau) », montre qu'ils
peuvent pourtant être trompés de façon surprenante.
