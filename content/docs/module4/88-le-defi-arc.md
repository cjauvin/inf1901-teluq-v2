---
title: "Le défi ARC"
weight: 88
slug: le-defi-arc
---

# Le défi ARC

{{% hint info %}}
**Chapitre d'approfondissement.** Ce chapitre est facultatif. Il présente un test conçu pour mesurer l'intelligence par des tâches nouvelles, mais
la suite du module et le travail noté ne supposent pas de l'avoir lu.
{{% /hint %}}

Les chapitres précédents ont présenté des modèles qui réussissent des examens de droit,
des concours de mathématiques et des exercices de programmation. Le chapitre
« [Passer à l'échelle](docs/module4/60-passer-a-l-echelle/#que-mesurent-les-scores) »
a toutefois montré la limite de ces scores : un modèle entraîné sur une grande partie du
Web a peut-être déjà vu les questions. Ce chapitre présente un test conçu pour mesurer
autre chose, la capacité à faire face à du nouveau. Il s'appelle ARC, pour
*Abstraction and Reasoning Corpus* (« corpus d'abstraction et de raisonnement »), et
son histoire, de 2019 à aujourd'hui, résume bien les progrès des grands modèles de
langage et ce qui leur manque encore.

## Mesurer l'intelligence, pas les compétences

En novembre 2019, François Chollet, chercheur chez Google et auteur de la bibliothèque
[Keras](docs/module3/42-materiel-et-outils/#la-différentiation-automatique), publie un
long article, « *On the Measure of Intelligence* » (« De la mesure de
l'intelligence »). Il y distingue deux choses que l'on confond souvent : la
**compétence** et l'**intelligence**.

Une compétence, comme jouer aux échecs ou traduire, peut s'acheter de deux façons :
avec des connaissances écrites d'avance par des humains, ou avec une immense quantité
d'expérience. [Deep Blue](docs/module1/30-chercher-raisonner) jouait aux échecs mieux
que Kasparov, mais ne savait rien faire d'autre. Un modèle de langage qui a lu des
milliers de milliards de mots peut réussir un examen sans que l'on sache s'il a
compris ou s'il a reconnu. Pour Chollet, l'intelligence est autre chose :
l'**efficacité avec laquelle un système acquiert des compétences nouvelles**, compte
tenu de ce qu'il savait au départ et de l'expérience dont il a disposé. Un système est
d'autant plus intelligent qu'il apprend vite, à partir de peu d'exemples, des tâches
qu'il n'a jamais rencontrées.

Cette définition prolonge la question de la
[généralisation](docs/module2/70-generaliser/#un-modèle-se-juge-sur-ce-quil-na-jamais-vu)
posée au Module 2. Elle en tire trois exigences pour un bon test : des tâches
réellement nouvelles, que l'on ne peut pas préparer en mémorisant ; très peu
d'exemples par tâche ; et aucune connaissance particulière, sinon celles que partagent
tous les humains.

## Le corpus ARC

ARC, publié avec l'article, applique ces exigences. Chaque tâche est formée de
quelques **paires d'exemples**, en général trois, puis d'une **entrée de test**.
Chaque grille compte de 1 × 1 à 30 × 30 cases, chacune d'une couleur parmi dix. Une
règle transforme chaque entrée en sortie ; elle n'est écrite nulle part, et il faut la
découvrir à partir des exemples, puis produire la grille de sortie du test, case par
case. La réponse est juste ou fausse, sans crédit partiel, et on a droit à deux essais
(trois dans la version originale).

{{< image src="/images/module4/arc-tache.svg" alt="Une vraie tâche du corpus ARC. Trois exemples, chacun formé d'une grille d'entrée et d'une grille de sortie de neuf cases sur neuf, sur fond noir. Dans les entrées, quelques cases isolées de couleur : rouge, bleu, et parfois bleu clair ou magenta. Dans les sorties, chaque case rouge est entourée de quatre cases jaunes en diagonale, chaque case bleue de quatre cases orange en croix, et les autres couleurs ne changent pas. À droite, une entrée de test, avec un point d'interrogation à la place de la sortie : il faut trouver la règle à partir des trois exemples, puis l'appliquer." title="Une tâche du corpus ARC. Un humain trouve la règle en quelques secondes : chaque case rouge reçoit quatre voisines jaunes en diagonale, chaque case bleue quatre voisines orange en croix." loading="lazy" >}}

Les tâches ne demandent ni langage, ni culture, ni connaissance du monde. Elles
supposent seulement les **connaissances de base** (*core knowledge*) que la
psychologue Elizabeth Spelke a observées chez les jeunes enfants :

- les **objets** : une forme d'une seule couleur forme un tout, qui persiste et qui
  peut en toucher ou en pousser un autre ;
- les **nombres** : compter, comparer, ajouter, toujours avec de petites quantités ;
- la **géométrie** : lignes, rectangles, symétries, rotations, agrandissements,
  l'intérieur et l'extérieur d'une forme ;
- les **intentions** : certaines tâches se lisent plus facilement si l'on imagine un
  objet qui cherche à atteindre un but.

Le corpus d'origine compte 400 tâches d'entraînement et 400 tâches d'évaluation
publiques, auxquelles s'ajoutent des tâches gardées secrètes. Les tâches publiques
servent à se préparer ; les scores officiels se mesurent sur les tâches secrètes, que
personne ne peut avoir vues. Le corpus et ses outils sont distribués sous une licence
libre, sur le dépôt [fchollet/ARC-AGI](https://github.com/fchollet/ARC-AGI). Le
corpus a depuis été renommé **ARC-AGI-1**, quand d'autres versions ont suivi.

## À vous de jouer

L'applet ci-dessous reprend l'interface de test officielle, traduite. Les douze
premières tâches viennent du jeu d'entraînement d'ARC-AGI-1, de la plus facile à la
plus difficile. La dernière vient d'ARC-AGI-2, présenté plus bas.

{{< applet src="/html/applets/arc.html" height="627" >}}

En 2024, une équipe de l'Université de New York fait passer les 800 tâches publiques à
plus de 1 700 personnes. En moyenne, une personne réussit 76 % des tâches
d'entraînement et 64 % des tâches d'évaluation, qui sont plus difficiles, avec trois
essais. Surtout, 790 des 800 tâches sont réussies par au moins une personne : la
difficulté varie d'un individu à l'autre, mais presque aucune tâche ne résiste à tous.

## Pourquoi les machines échouaient

Pour un programme, chaque tâche ARC est un problème nouveau, et c'est précisément ce
qui le rend difficile. On ne peut pas l'entraîner sur les tâches du test, puisqu'elles
sont secrètes, et ce qu'il a appris sur les autres ne s'y applique pas directement :
chaque tâche a sa propre règle.

Les grands modèles de langage ont en plus un handicap particulier. Ils lisent une
grille comme une suite de [jetons](docs/module4/45-des-mots-aux-nombres/#découper-le-texte-les-jetons),
rangée après rangée. Deux cases l'une au-dessus de l'autre, voisines pour un humain,
sont séparées par toute une rangée de jetons. Une colonne, un rectangle ou une symétrie
verticale, évidents pour l'œil, doivent être reconstitués à partir d'une longue suite
de nombres.

Les résultats en témoignent. En 2020, le premier concours ARC, sur la plateforme
Kaggle, est remporté par un programme qui essaie en force brute des combinaisons de
transformations écrites à la main, une [recherche](docs/module1/30-chercher-raisonner/#résoudre-cest-explorer)
dans l'esprit du Module 1 : il résout 20 % des tâches secrètes. En 2024, GPT-4o en
résout 5 %.

## Le prix ARC de 2024 et l'entraînement au moment du test

En juin 2024, Mike Knoop et François Chollet lancent le **prix ARC** (*ARC Prize*),
doté de plus d'un million de dollars, dont 600 000 dollars pour le premier système qui
atteindra 85 % sur les tâches secrètes. Les solutions tournent sur les serveurs de
Kaggle, sans accès à Internet et avec une puissance de calcul limitée, et elles
doivent être publiées.

En novembre 2024, plus de 1 400 équipes ont participé. L'équipe gagnante, The
ARChitects, atteint 53,5 % ; l'équipe MindsAI obtient 55,5 %, mais n'est pas classée,
faute d'avoir publié sa solution. Le grand prix n'est pas attribué. La plupart des
meilleures équipes partagent une même idée : l'**entraînement au moment du test**
(*test-time training*), présenté au chapitre
« [Des outils, un harnais et des agents](docs/module4/80-outils-et-agents/#pourquoi-ne-pas-le-laisser-apprendre) ».
Pour chaque tâche, avant de répondre, on ajuste les poids d'un modèle de langage sur
ses quelques paires d'exemples, multipliées par des transformations qui ne changent pas
la règle : rotations, symétries, permutations de couleurs. Le modèle se spécialise un
instant sur la tâche, puis on jette ces poids. Une équipe du MIT, dirigée par Ekin
Akyürek, montre la même année qu'un modèle de 8 milliards de paramètres passe ainsi à
53 % des tâches d'évaluation publiques.

## o3 et le calcul au moment de la réponse

Le 20 décembre 2024, OpenAI présente o3, un
[modèle de raisonnement](docs/module4/70-du-modele-a-l-assistant/#des-modèles-qui-raisonnent-rlvr).
Sur les tâches semi-privées d'ARC-AGI-1, il atteint 75,7 %, pour environ 26 dollars
par tâche. En lui laissant environ 172 fois plus de calcul, soit plusieurs milliers de
dollars par tâche, il atteint 87,5 %. C'est une illustration nette du
[calcul au moment de la réponse](docs/module4/70-du-modele-a-l-assistant/#des-modèles-qui-raisonnent-rlvr) :
le même modèle, en réfléchissant plus longtemps, réussit beaucoup plus de tâches.

Chollet parle d'un saut réel et important, tout en mettant en garde : réussir ARC
n'est pas atteindre l'intelligence artificielle générale, et o3 échoue encore à
certaines tâches très faciles pour un humain. Il note aussi que le modèle a été
entraîné sur une partie des tâches d'entraînement publiques, et que son coût reste
sans commune mesure avec celui d'un humain.

## ARC-AGI-2

En mars 2025, la fondation ARC Prize publie **ARC-AGI-2**, conçu pour rester facile
pour les humains, mais beaucoup plus difficile pour les machines. Ses tâches visent
trois faiblesses des systèmes de l'époque :

- **interpréter des symboles** : une couleur ou une forme y a un sens à découvrir, comme
  dans une légende ;
- **composer des règles** : plusieurs règles s'appliquent en même temps et
  interagissent ;
- **appliquer une règle selon le contexte** : la même situation appelle des
  transformations différentes selon ce qui l'entoure.

La dernière tâche de l'applet en est un exemple : une petite légende, dans un coin de
la grille, associe des paires de couleurs, et indique de quelle couleur remplir chaque
forme.

Pour la première fois, les tâches sont calibrées sur des humains. À San Diego, 407
personnes en essaient plus de 1 800 candidates ; une tâche n'est retenue que si au
moins deux personnes la réussissent en deux essais au plus. En moyenne, une personne
réussit environ 66 % des tâches qu'elle tente, en moins de trois minutes chacune. À la
publication, les grands modèles de langage sans raisonnement obtiennent 0 %, et o3
environ 4 %. Le classement tient désormais compte du **coût par tâche** : un système
qui réussit en dépensant mille fois plus qu'un humain n'est pas aussi intelligent,
au sens de Chollet, qu'un système efficace.

Les progrès sont ensuite rapides. Selon le classement tenu par ARC Prize, les meilleurs
modèles commerciaux passent d'environ 10 % à l'été 2025 à plus de 50 % à la fin de
l'année, puis dépassent 85 % au printemps 2026, pour quelques dollars par tâche. Ces
scores sont toutefois mesurés sur des tâches semi-privées, avec de très grands modèles.
Au concours sur Kaggle de 2025, où le calcul est limité et les solutions publiques, la
meilleure équipe, NVARC, de NVIDIA, atteint 24 %, avec un modèle de 4 milliards de
paramètres et de l'entraînement au moment du test. Le premier prix d'article de
l'année va à un réseau minuscule de 7 millions de paramètres, le *Tiny Recursive Model*
d'Alexia Jolicoeur-Martineau, de Samsung à Montréal, qui raffine sa réponse en
boucle.

## ARC-AGI-3 : apprendre en jouant

Dès 2019, Chollet notait qu'un test fait de questions et de réponses fixes restait
limité, et suggérait un format interactif. C'est celui d'**ARC-AGI-3**, présenté en
juillet 2025, puis publié en mars 2026. Il ne contient plus de grilles à compléter,
mais 135 petits jeux au tour par tour, sans aucune consigne. Le joueur doit explorer,
découvrir à quoi servent ses actions, deviner le but, puis l'atteindre, sur plusieurs
niveaux de difficulté croissante. On retrouve les questions de
l'[apprentissage par renforcement](docs/module3/80-renforcement-profond) du Module 3,
et celle du [modèle du monde](docs/module4/94-comprendre-et-rater/#perroquets-ou-modèles-du-monde) :
pour bien jouer, il faut comprendre comment fonctionne le petit monde du jeu.

Le score ne mesure pas seulement la réussite, mais l'**efficacité** : le nombre
d'actions dont le système a besoin, comparé à celui d'un humain. Chaque jeu a été
essayé par une dizaine de personnes, et au moins deux l'ont réussi du premier coup.
À la publication,
les meilleurs modèles obtenaient moins de 1 %. Quelques mois plus tard, à
l'automne 2026, les meilleurs systèmes dépassent 60 %, en dépensant toutefois des
dizaines de milliers de dollars pour l'ensemble des jeux.

Les jeux publics d'ARC-AGI-3 se jouent dans un navigateur, sur le site d'ARC Prize. Le
jeu [ls20](https://arcprize.org/tasks/ls20) permet d'en faire l'expérience : quelques
minutes suffisent pour sentir ce qu'on demande au système, découvrir seul les règles
d'un monde inconnu.

## Ce qu'ARC dit, et ce qu'il ne dit pas

Chollet lui-même présentait ARC, dès 2019, comme un travail en cours plutôt qu'une
mesure définitive. Le corpus est petit, la difficulté de ses tâches n'est pas mesurée
précisément, et rien ne garantit qu'on ne puisse pas les résoudre par des raccourcis.
En 2024, la chercheuse Melanie Mitchell fait remarquer qu'une recherche en force brute
parmi des milliers de programmes peut résoudre des tâches sans rien qui ressemble à de
l'abstraction, et qu'un prix d'un million de dollars attaché à un score est une
invitation à la [loi de Goodhart](docs/module4/60-passer-a-l-echelle/#que-mesurent-les-scores) :
on finit par optimiser le score plutôt que la capacité qu'il devait mesurer.

L'histoire d'ARC suit un cycle. Un test est conçu pour résister aux méthodes du
moment ; des méthodes nouvelles le font céder, par la recherche, l'entraînement au
moment du test, le raisonnement ou la puissance de calcul ; un test plus difficile
lui succède. On y reconnaît l'[« effet IA »](docs/module1/60-hivers/#lhéritage-invisible)
du Module 1 : dès qu'une machine réussit, on se demande si la tâche mesurait vraiment
l'intelligence. ARC a toutefois le mérite de poser la question avec précision. Il ne
demande pas seulement si un système réussit, mais à partir de combien d'exemples, et à
quel prix, là où un enfant y parvient en quelques secondes, avec trois exemples et
très peu d'énergie. Le chapitre
« [Qu'est-ce que l'intelligence ?](docs/module5/26-qu-est-ce-que-l-intelligence) » du
Module 5 replace ARC parmi les autres façons de définir l'intelligence.

Le dernier chapitre du module,
« [Ce que les LLM comprennent, et ce qu'ils ratent](docs/module4/94-comprendre-et-rater) »,
reprend ces questions à partir des erreurs des modèles et de ce que l'on découvre à
l'intérieur. Le [chapitre suivant](docs/module4/90-mots-et-images) quitte d'abord le
texte, pour montrer comment on a relié les mots et les images.
