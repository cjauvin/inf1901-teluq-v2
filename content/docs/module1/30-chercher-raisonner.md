---
title: "L'âge d'or symbolique : chercher et raisonner"
weight: 30
slug: chercher-raisonner
---

# L'âge d'or symbolique : chercher et raisonner

## Résoudre, c'est explorer

Une fois le pari symbolique posé, il reste une question pratique : comment faire
raisonner une machine ? Les pionniers de l'IA trouvent une réponse très générale,
parce qu'elle s'applique à des problèmes très différents. Presque tout problème
peut se reformuler comme l'**exploration d'un espace de possibilités**.

Prenons l'exemple d'un labyrinthe. À chaque instant, vous êtes dans une certaine
position, qu'on appelle un **état**. À partir de cet état, quelques actions sont
possibles (avancer, tourner à gauche, tourner à droite), et chacune mène à un
nouvel état. L'ensemble de tous les états atteignables forme une grande
arborescence, l'**espace d'états** (*state space*). Résoudre le labyrinthe revient alors à
**trouver un chemin** dans cette arborescence, depuis l'état de départ jusqu'à
l'état-but (la sortie).

{{< image src="/images/module1/espace-etats.svg" alt="À gauche, un labyrinthe dessiné comme un arbre de couloirs dont les états sont étiquetés S, A, B, C, D, E, G ; à droite, exactement le même arbre dessiné avec des nœuds et des arêtes portant les mêmes étiquettes. Le chemin S→A→D→G vers le but est surligné à l'identique des deux côtés ; C et E sont des impasses." title="Un labyrinthe est un arbre d'états : résoudre, c'est trouver un chemin de S (départ) à G (but)." loading="lazy" >}}

Cette idée est utile parce que beaucoup de problèmes qui semblent sans rapport
prennent alors la même forme. Le taquin (un jeu de petites tuiles numérotées
qu'on fait glisser), une partie d'échecs, la planification d'un itinéraire et la
démonstration d'un théorème comportent tous un état de départ, des actions qui
font passer d'un état à un autre et un but à atteindre. Dans chaque cas, résoudre
le problème revient à **chercher un chemin** vers ce but. Newell et Simon, les
auteurs du Logic Theorist, poussent l'idée jusqu'à construire un programme appelé
*General Problem Solver* (« solutionneur général de problèmes »), conçu pour
traiter n'importe quel problème exprimé sous cette forme.

La recherche n'est pas une technique parmi d'autres. C'est le mécanisme
central de l'IA symbolique (*symbolic AI*). Pour démontrer un théorème, planifier un trajet,
diagnostiquer une panne ou lever l'ambiguïté d'une phrase, le GOFAI ramène le
problème à l'exploration d'un espace de possibilités, jusqu'à y trouver une
solution. Nous la retrouverons dans « [Représenter le
monde](docs/module1/40-representer-le-monde) » et « [Capturer
l'expertise](docs/module1/50-systemes-experts) ».
À la fin du module, dans [*Les hivers et la
bascule*](docs/module1/60-hivers/#la-bascule), c'est aussi elle qui marquera la
différence avec l'autre tradition : l'IA symbolique cherche une solution, alors
que l'apprentissage automatique (*machine learning*) apprend à partir d'exemples.

## L'explosion combinatoire

L'exploration d'un arbre de possibilités a cependant une limite importante. Pour
la plupart des problèmes intéressants, cet arbre est **extrêmement grand**.

Les échecs en sont l'exemple le plus connu. À chaque tour, un joueur dispose en
moyenne d'une trentaine de coups possibles. Chacun de ces coups permet une
trentaine de réponses de l'adversaire, et ainsi de suite. Regarder seulement
quelques coups à l'avance multiplie déjà fortement le nombre de branches à
examiner. Le nombre de toutes les parties d'échecs possibles, appelé **nombre de
Shannon**, vaut environ un 1 suivi de 120 zéros. Il dépasse de très loin le
nombre d'atomes dans l'univers observable. Aucune machine, aussi rapide soit-elle,
ne pourra jamais explorer un tel espace en entier.

{{< image src="/images/module1/explosion-combinatoire.svg" alt="Un arbre de jeu qui s'évase : une position donne environ 30 coups, chacun environ 900, puis environ 27 000, et ainsi de suite. En dessous, le nombre de parties d'échecs possibles (environ 10 puissance 120, le nombre de Shannon) est comparé au nombre d'atomes de l'univers observable (environ 10 puissance 80), qu'il dépasse de très loin." title="L'explosion combinatoire : à ~30 coups par tour, l'arbre des parties dépasse vite le nombre d'atomes de l'univers." loading="lazy" >}}

Pour les jeux à deux adversaires, les chercheurs mettent au point une stratégie
appelée **minimax**. La machine explore l'arbre des coups en supposant que son
adversaire jouera toujours le mieux possible. À chaque étape, elle cherche à
maximiser son avantage, en supposant que l'adversaire cherchera à le minimiser,
d'où le nom. En remontant les conséquences de chaque coup, elle choisit celui qui
lui garantit le meilleur résultat dans le pire des cas.

Comme l'arbre reste trop grand pour être exploré jusqu'au bout, il faut des
**raccourcis**. Au lieu d'aller jusqu'aux fins de partie, la machine s'arrête à
une certaine profondeur et estime la qualité d'une position à l'aide d'une
**règle empirique** (une « heuristique »), par exemple en comptant les pièces ou
en évaluant le contrôle du centre. D'autres techniques, comme l'**élagage**
(*pruning* : ignorer dès le départ les branches qui ne peuvent pas changer la décision),
évitent des explorations inutiles.

{{< image src="/images/module1/minimax-elagage.svg" alt="Un arbre de jeu à trois niveaux. À la racine, c'est à la machine (MAX) de jouer ; au niveau suivant, trois coups de l'adversaire (MIN) ; en bas, neuf positions estimées par une heuristique. Chaque nœud MIN prend le minimum de ses feuilles : 3, au plus 2, et 2. La racine prend le maximum : 3, et une flèche épaisse montre le coup choisi. Au deuxième nœud MIN, dès que la feuille 2 est vue, les deux autres feuilles sont barrées : c'est l'élagage, car ce coup ne peut plus battre le 3 déjà garanti." title="Minimax sur un petit arbre : les estimations remontent, en alternant le plus petit (l'adversaire) et le plus grand (la machine) ; au milieu, l'élagage évite d'examiner deux positions inutiles." loading="lazy" >}}

Le même principe s'applique en dehors des jeux, lorsqu'il faut **trouver un
chemin**, par exemple dans le labyrinthe du début ou pour calculer un itinéraire
routier. Au lieu d'explorer dans toutes les directions, un algorithme connu
nommé **A\*** (prononcé « A étoile ») se laisse guider par une heuristique. À
chaque embranchement, il privilégie la direction qui semble le rapprocher le plus
du but (par exemple, selon la distance à vol d'oiseau jusqu'à la destination). Le
GPS qui calcule une route utilise ce genre de stratégie. C'est aussi le cas de
l'**IA des jeux vidéo** : les personnages non joueurs (*non-player characters*) qui trouvent leur route sur
la carte, ou les ennemis qui poursuivent ou contournent le joueur, s'appuient le
plus souvent sur ces mêmes algorithmes de recherche de chemin (*pathfinding*), en particulier A\*.
La principale leçon de cette période est donc la suivante : un système efficace
n'explore pas tout, il explore **au bon endroit**. La qualité des heuristiques
est déterminante.

L'applet ci-dessous compare les deux stratégies sur le même labyrinthe. À gauche,
une recherche aveugle (*blind search*) s'étend dans toutes les directions à la fois. À droite, A*
est guidé par la distance qui le sépare du but. Lancez les deux recherches, puis
comparez le nombre de cases explorées : elles trouvent le même chemin, mais pas
avec le même effort. Ajoutez ou retirez des murs en cliquant sur la grille, et
observez dans quels cas l'heuristique aide beaucoup et dans quels cas elle mène
la recherche dans une mauvaise direction.

{{< applet src="/html/applets/astar.html" height="557" >}}

Nous retrouverons cette limite, sous un autre nom, quand il s'agira d'apprendre à
partir de données décrites par des milliers de caractéristiques. Ce sera la
[malédiction de la dimension](docs/module2/40-predire-par-ressemblance) (*curse of dimensionality*), au
[Module 2](docs/module2).


## L'apogée : Deep Blue bat Kasparov (1997)

En mai 1997, à New York, se joue un match devenu célèbre. D'un côté, **Garry
Kasparov**, champion du monde d'échecs en titre, considéré par beaucoup comme le
plus grand joueur de l'histoire. De l'autre, **Deep Blue**, un superordinateur
conçu par IBM. Au terme de six parties, la machine l'emporte. C'est la première
fois qu'un champion du monde en exercice perd contre un ordinateur dans un match
en conditions officielles. L'événement a un retentissement mondial, et la presse
y voit le jour où la machine a « dépassé » l'humain.

Deep Blue applique directement les techniques [décrites plus
haut](docs/module1/30-chercher-raisonner/#lexplosion-combinatoire). Il n'utilise
aucun réseau de neurones et aucun apprentissage. Il repose sur de la **recherche
par force brute** (la machine évalue jusqu'à 200 millions de positions par
seconde), guidée par des **heuristiques** mises au point avec l'aide de grands
maîtres, et sur de très grandes bibliothèques d'ouvertures et de fins de partie.
C'est du GOFAI typique, rendu très performant par la puissance de calcul.

Le match a été tendu. Au début de la rencontre, un coup subtil et inattendu de la
machine, qu'il jugeait trop « humain », a déstabilisé Kasparov. Il en est venu à
soupçonner une intervention humaine et a accusé IBM de tricherie. Il a réclamé une
revanche, que l'entreprise a refusée, et Deep Blue a été démonté peu après. Ce
coup inattendu aurait en réalité résulté d'un simple bogue dans le programme.

La vidéo suivante montre la réaction de Kasparov au moment où il abandonne la
sixième et dernière partie, le 11 mai 1997. Elle montre bien ce que représentait
cette défaite :

{{< youtube id="EsMk1Nbcs-s" >}}

Au-delà de l'anecdote, cette victoire pose de nouveau la question de
l'intelligence des machines. Deep Blue ne « comprend » pas les échecs comme
Kasparov les comprend. Il ne sait même pas qu'il joue aux échecs. Il ne perçoit
ni la beauté d'une combinaison ni la tension d'une partie, il ne sait rien faire
d'autre et il ne peut pas expliquer pourquoi il a joué tel coup. On peut donc se
demander s'il s'agit d'*intelligence* ou seulement d'une machine à calculer très
puissante qui joue aux échecs.

IBM a relevé un autre défi quatorze ans plus tard, dans un domaine beaucoup plus
difficile, le langage. En 2011, son système Watson a battu les meilleurs champions
du jeu télévisé *Jeopardy!*, en combinant le savoir structuré de l'IA symbolique et
l'apprentissage statistique. Nous le retrouverons à la fin du module, dans
[*Les hivers et la bascule*](docs/module1/60-hivers/#un-éclair-hybride-watson-2011).

{{% hint info %}}
Le cas Deep Blue illustre un constat qui revient dans toute l'histoire de l'IA.
Les tâches que nous jugeons les plus « intellectuelles » (jouer aux échecs,
démontrer un théorème) se sont révélées **relativement faciles** à mécaniser. À
l'inverse, ce qu'un enfant de trois ans fait sans effort (comprendre une phrase,
reconnaître une scène, faire preuve de bon sens) a longtemps résisté. C'est le
**paradoxe de Moravec**, sur lequel nous reviendrons au
[Module 2](docs/module2/10-le-probleme/#pourquoi-on-ne-peut-pas-simplement-le-programmer).
{{% /hint %}}

Ces difficultés montrent déjà les limites de cette période, sur lesquelles nous
reviendrons dans « [Les hivers et la bascule](docs/module1/60-hivers) ». La même époque a cependant produit un autre type de programme. Il ne
calcule pas pour gagner une partie, mais semble parler et écouter, et son cas est
encore plus surprenant.

## L'autre visage : ELIZA, ou l'illusion de comprendre

L'IA symbolique de cette période ne se limite pas à la recherche et au calcul.
L'un de ses épisodes les plus marquants concerne une machine qui semblait non pas
jouer, mais parler. En 1966, au MIT, l'informaticien **Joseph Weizenbaum** écrit
**ELIZA**, un programme qui imite un psychothérapeute. La conversation paraît
étonnamment naturelle. Si vous tapez « je me sens seul ces temps-ci », ELIZA
répond « depuis quand vous sentez-vous seul ? ».

Pourtant, le programme ne comprend rien. ELIZA se contente de repérer des
mots-clés et de **renvoyer les phrases de l'utilisateur sous forme de
questions**, selon quelques règles très simples. Si vous écrivez « ma mère ne
m'écoute jamais », le mot « mère » déclenche la réponse « parlez-moi de votre
famille ». Le programme ne possède aucun savoir sur le monde, sur la solitude ou
sur les mères.

{{< image src="/images/module1/eliza.svg" alt="Une fenêtre de conversation : l'utilisateur écrit « je me sens seul ces temps-ci » et ELIZA répond « depuis quand vous sentez-vous seul ? ». Sous le capot, le programme repère le mot-clé « seul » et le glisse dans un gabarit tout prêt, sans aucune compréhension." title="ELIZA : repérer un mot-clé et renvoyer la phrase en question, sans rien comprendre." loading="lazy" >}}

La réaction des utilisateurs est ce qui a le plus marqué. Les gens se sont
attachés à ELIZA. La secrétaire de Weizenbaum, qui savait pourtant qu'il
s'agissait d'un programme, lui a un jour demandé de quitter la pièce pour pouvoir
« parler en privé » avec la machine. Des utilisateurs lui ont confié des problèmes
personnels, persuadés d'être écoutés. Weizenbaum en a été si troublé qu'il est
devenu l'un des principaux critiques de l'IA. On appelle aujourd'hui **« effet
ELIZA »** cette forte tendance à *projeter* de la compréhension, et même des
émotions, sur n'importe quelle machine qui manie le langage.

ELIZA est en quelque sorte l'inverse du test de Turing. Elle montre qu'il peut
être facile de donner l'illusion de penser sans rien comprendre. Cette mise en
garde prendra toute son importance avec les agents conversationnels ([module 4](docs/module4/94-comprendre-et-rater/#lillusion-de-comprendre)) et
dans le débat, toujours ouvert, sur ce que « comprendre » veut dire pour une
machine ([module 5](docs/module5)).

Une dernière précision est importante pour la suite. On pourrait voir en ELIZA
l'ancêtre direct de ChatGPT, comme s'il s'agissait du même procédé à plus grande
échelle. C'est presque l'inverse. ELIZA n'est qu'un petit ensemble de règles
écrites à la main (repérer un mot, produire une réponse à partir d'un gabarit),
sans aucun apprentissage ni savoir sur le monde. C'est du GOFAI pur, entièrement
programmé par son auteur. Les grands **modèles de langage** (les *LLM*) sur
lesquels repose ChatGPT relèvent au contraire du **pari adverse**, celui du
perceptron et des réseaux de neurones. Personne ne leur a donné de règles. Ils ont
appris, à partir de très grandes quantités de textes, un modèle statistique du
langage qui comporte des milliards de paramètres, et ils produisent des réponses
nouvelles sur presque tous les sujets. La ressemblance n'est donc que
superficielle. ELIZA et ChatGPT représentent les **deux paris rivaux** de ce
module. Cela ne règle pas la question de fond, qui est de savoir si un LLM
comprend ou s'il n'est qu'un imitateur beaucoup plus habile. L'effet ELIZA
invite justement à ne pas trancher cette question trop vite.

**Un mot sur l'outil.** ELIZA, comme presque tous les programmes de cette
période, était écrite en **Lisp**, un langage inventé par John McCarthy en 1958,
l'année même du perceptron. C'est l'un des plus anciens langages de programmation
encore utilisés aujourd'hui, et il a beaucoup influencé l'informatique (la
récursion, le ramasse-miettes de mémoire, l'invite interactive et bien d'autres
idées aujourd'hui courantes y sont nées). Son nom vient de *LISt Processing*, le
« traitement de listes ». La plupart des langages sont d'abord conçus pour
calculer des nombres, alors que Lisp est conçu pour **manipuler des symboles**
(des mots, des concepts, des relations). C'était donc l'outil idéal pour le pari
symbolique.

{{% details "Pour aller plus loin : à quoi ressemble du Lisp ?" %}}
En Lisp, presque tout s'écrit sous forme de listes entre parenthèses, avec
l'opération placée en tête. Une addition s'écrit ainsi :

```lisp
(+ 1 2 3)      ; vaut 6
(* 3 (+ 2 4))  ; vaut 18, soit 3 × (2 + 4)
```

Jusqu'ici, rien de particulier. L'idée importante est qu'une liste peut contenir
des *symboles* (des mots) aussi bien que des nombres. On peut écrire une liste de
concepts :

```lisp
(chien chat oiseau)
```

On peut aussi représenter une connaissance, c'est-à-dire un fait sur le monde :

```lisp
(est-un Socrate humain)   ; « Socrate est un humain »
```

Le point essentiel est qu'en Lisp, **un programme a exactement la même forme que
les données qu'il manipule**, puisque dans les deux cas il s'agit de listes. Un
programme peut donc lire, transformer et même produire d'autres programmes aussi
facilement qu'il manipule une liste d'épicerie. Cette propriété (« le code est une
donnée comme une autre ») explique pourquoi Lisp convenait si bien à des systèmes
destinés à raisonner sur des symboles.
{{% /details %}}

Pendant des décennies, Lisp est resté le langage principal de l'IA symbolique. On
a même construit des ordinateurs spécialisés, les **« machines Lisp »**, pour
l'exécuter plus efficacement. Nous verrons dans « [Les hivers et la
bascule](docs/module1/60-hivers) » que leur effondrement, vers 1987,
marque l'un des hivers de l'IA.

Deep Blue cherchait et ELIZA manipulait du langage, mais aucun des deux ne
connaissait vraiment le monde. Pour aller plus loin, il fallait donner à la
machine une façon de **représenter ce qu'elle sait**. C'est le grand chantier de
« [Représenter le monde](docs/module1/40-representer-le-monde) », qui s'est
soldé par un échec important.
