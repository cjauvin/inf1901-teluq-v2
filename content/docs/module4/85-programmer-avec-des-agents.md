---
title: "Programmer avec des agents"
weight: 85
slug: programmer-avec-des-agents
---

# Programmer avec des agents

Le chapitre
« [Des outils, un harnais et des agents](docs/module4/80-outils-et-agents/#des-agents-un-modèle-et-son-harnais-en-boucle) »
a présenté les agents en général : un modèle de langage, un harnais qui le fait
tourner en boucle, et des outils. C'est en programmation que cette idée a donné, à
ce jour, ses résultats les plus spectaculaires. En quelques années, on est passé
d'un modèle qui complète une ligne de code à des agents qui lisent un projet entier,
le modifient, lancent ses tests et corrigent leurs propres erreurs. Ce chapitre
explique comment ils fonctionnent, pourquoi le code s'y prête si bien, ce qu'ils
doivent à une très vieille tradition de l'informatique, celle des outils Unix, et ce
qu'ils changent au métier de programmeur.

## De la complétion à l'agent

En juin 2021, GitHub présente **Copilot**, un assistant intégré à l'éditeur de code
qui propose la suite d'une ligne ou d'une fonction pendant qu'on tape. Il repose sur
Codex, un modèle d'OpenAI entraîné sur du code public. Le mois suivant, l'article qui
présente Codex mesure ses capacités sur 164 petits problèmes de programmation en
Python, chacun vérifié par des tests : Codex en résout 28,8 % du premier coup, là où
GPT-3 n'en résout aucun.

À partir de la fin de 2022, avec ChatGPT, on demande du code dans une conversation,
puis on le copie dans son projet. Le modèle ne voit ni le projet, ni les erreurs qu'il
provoque : c'est au programmeur de faire l'aller-retour. Les éditeurs intègrent
ensuite les modèles plus étroitement, comme Cursor, lancé en 2023.

En mars 2024, la jeune entreprise Cognition présente Devin, qu'elle appelle « le
premier ingénieur logiciel IA ». Il résout de lui-même 13,9 % d'un échantillon de
vrais problèmes tirés de projets publics, contre 2 % pour les meilleurs modèles
précédents. En mai 2024, une équipe de Princeton publie SWE-agent et en tire une
leçon importante : un agent est un nouveau genre d'utilisateur, et il a besoin
d'une **interface agent-ordinateur** (*agent-computer interface*) pensée pour lui,
avec des commandes simples pour afficher, chercher et modifier des fichiers, comme
les humains ont leurs éditeurs.

En 2025, les agents de programmation sortent de l'éditeur et s'installent dans le
**terminal**, la fenêtre où l'on tape des commandes : Claude Code, d'Anthropic, en
février, Codex CLI, d'OpenAI, en avril, et Gemini CLI, de Google, en juin. D'autres
travaillent dans le nuage : on leur confie une tâche, et ils reviennent, parfois une
heure plus tard, avec une proposition de modification du projet. En 2026, selon
l'enquête annuelle du site Stack Overflow, deux tiers des développeurs qui utilisent
l'IA se servent d'agents de programmation.

## Ce que fait un agent de programmation

Un agent de programmation est un modèle de langage et son
[harnais](docs/module4/80-outils-et-agents/#la-requête-système-et-le-harnais), comme
tout agent. Ce qui le distingue, ce sont ses outils, peu nombreux et très généraux :

- **lire un fichier**, en entier ou en partie ;
- **chercher** dans les fichiers du projet ;
- **modifier un fichier**, en remplaçant un passage exact par un autre ;
- **exécuter une commande** dans un terminal, ce qui ouvre l'accès à tous les
  programmes installés sur l'ordinateur.

Avec ces quatre outils, l'agent travaille comme un programmeur. Il explore le projet
pour comprendre où se trouve le problème, modifie quelques lignes, lance les tests
ou la compilation, lit les erreurs, et recommence, jusqu'à ce que les tests passent.

{{< image src="/images/module4/boucle-agent-code.svg" alt="Une boucle en quatre étapes autour d'une tâche : explorer le projet, avec ls, find, grep et cat ; modifier le code, en ajoutant par exemple deux lignes à la ligne 3 de notes.py ; vérifier, en lançant les tests ou la compilation, avec python -m pytest ou make ; lire le résultat, c'est-à-dire les messages d'erreur et le code de sortie, puis revenir à l'exploration. Quand les tests passent, l'agent sort de la boucle : il consulte git diff, résume ce qu'il a fait et, si on le lui permet, enregistre une version avec git commit. Une note rappelle que tout passe par du texte : commandes, résultats et erreurs." title="La boucle d'un agent de programmation. À chaque tour, le modèle écrit une commande, le harnais l'exécute, et le résultat, du texte, s'ajoute au contexte." loading="lazy" >}}

L'applet ci-dessous déroule deux sessions, étape par étape. La première corrige un
test qui échoue. La seconde montre ce qui peut mal tourner, et c'est à vous de
décider, au moment où le harnais demande la permission.

{{< applet src="/html/applets/agent-code.html" height="548" >}}

## La culture Unix : des outils faits pour le texte

Les commandes de l'applet, `ls`, `grep`, `cat` ou `git`, ne datent pas des agents.
La plupart viennent d'**Unix**, le système d'exploitation créé à partir de 1969 par
Ken Thompson et Dennis Ritchie, aux Bell Labs, dont descendent aujourd'hui Linux et
macOS. En 1973, Doug McIlroy y ajoute le **tube** (*pipe*), qui envoie le texte produit
par un programme à l'entrée du suivant. En 1978, il résume la philosophie d'Unix en
trois conseils : écrire des programmes qui font une seule chose et la font bien,
écrire des programmes qui travaillent ensemble, et leur faire échanger du texte,
parce que le texte est une interface universelle.

Cinquante ans plus tard, cette philosophie convient remarquablement aux modèles de
langage, pour plusieurs raisons.

- **Le texte est la langue du modèle.** Une commande est une ligne de texte, et son
  résultat aussi. Le modèle n'a besoin d'aucune traduction : il écrit la commande
  comme il écrirait une phrase, et lit le résultat comme il lit tout le reste. Un
  agent qui utilise une interface graphique doit au contraire regarder des pixels et
  cliquer au bon endroit, ce qui reste beaucoup plus difficile.
- **Un seul outil en donne des milliers.** Grâce à l'outil « exécuter une commande »,
  l'agent a accès à tous les programmes installés, sans que personne ait eu à les
  décrire un par un, comme les outils de la
  [librairie](docs/module4/80-outils-et-agents/#le-harnais-et-lappel-doutils).
- **Les petits outils se combinent.** Aucun programme ne sait répondre à une question
  donnée, mais quelques-uns, reliés par des tubes, y répondent en une ligne. L'agent
  compose ainsi, à la demande, l'outil dont il a besoin.
- **Le modèle les connaît déjà.** Pendant son entraînement, il a lu des décennies de
  documentation, de scripts, de tutoriels et de réponses sur les forums. Il connaît
  les options de `grep` comme il connaît la grammaire. Et s'il hésite, la
  documentation est elle-même du texte, que la commande `man grep` affiche.
- **Les verdicts sont exacts.** Un programme Unix signale sa réussite par un **code de
  sortie**, 0 si tout va bien, un autre nombre sinon, et ses messages d'erreur
  indiquent souvent le fichier et la ligne en cause. Le modèle reçoit ainsi un signal
  précis, sans ambiguïté.

{{< image src="/images/module4/tube-unix.svg" alt="La question : qui a fait le plus de modifications dans ce projet ? En bas, la ligne de commande qui y répond : git log --format=%an, puis sort, puis uniq -c, puis sort -rn, puis head -2, reliés par le symbole |, le tube. Au-dessus, cinq boîtes, une par programme, avec le texte qui sort de chacune. git log donne le nom de l'auteur de chaque modification : Grace, Ada, Grace, Linus, Grace, Ada. sort les trie : Ada, Ada, Grace, Grace, Grace, Linus. uniq -c compte les lignes identiques qui se suivent : 2 Ada, 3 Grace, 1 Linus. sort -rn trie par nombre, du plus grand au plus petit : 3 Grace, 2 Ada, 1 Linus. head -2 garde les deux premières lignes : 3 Grace, 2 Ada. Chaque programme fait une seule chose, lit du texte et en produit." title="Un tube Unix. Cinq petits programmes, dont aucun ne connaît la question, y répondent ensemble en une ligne. Un agent compose ce genre de ligne aussi naturellement qu'une phrase." loading="lazy" >}}

Voici quelques-uns des outils qu'un agent de programmation utilise le plus souvent.

| Commande | À quoi elle sert | Exemple |
|---|---|---|
| `ls` | lister les fichiers d'un dossier | `ls -la src/` |
| `cat`, `head`, `tail` | afficher un fichier, son début ou sa fin | `head -20 notes.py` |
| `find` | trouver des fichiers par leur nom ou leur date | `find . -name "*.py"` |
| `grep` | chercher un motif dans des fichiers | `grep -rn "def moyenne" .` |
| `sed` | remplacer du texte dans un fichier | `sed -i 's/ancien/nouveau/' notes.py` |
| `diff` | comparer deux versions d'un fichier | `diff avant.py apres.py` |
| `wc`, `sort`, `uniq` | compter, trier, regrouper des lignes | `wc -l *.py` |
| `curl` | télécharger une page ou interroger un service Web | `curl -s https://api.exemple.org/...` |
| `python` | exécuter un programme, un calcul, ou les tests | `python -m pytest` |
| `git` | consulter et enregistrer l'historique du projet | `git log --oneline -5` |

Deux de ces outils méritent une mention particulière.

**Python** sert à l'agent de couteau suisse. Plutôt que de calculer de tête, ce qu'un
modèle de langage
[fait mal](docs/module4/80-outils-et-agents/#des-outils-un-harnais-et-des-agents),
il écrit un petit programme de quelques lignes, l'exécute et lit le résultat. Il peut
ainsi compter, convertir, analyser un fichier de données ou vérifier une hypothèse,
avec l'exactitude d'un programme.

**Git**, le système de gestion de versions créé par Linus Torvalds en 2005,
enregistre l'historique complet d'un projet. Pour un agent, c'est à la fois une
mémoire et un filet de sécurité. `git log` montre ce qui a été fait, et par qui ;
`git diff` montre exactement ce que l'agent vient de changer, ce qui permet à un
humain de le relire ; et toute modification peut être annulée. Un agent qui
travaille dans un projet suivi par git ne peut pas, en principe, détruire ce qui a
été enregistré.

## Un projet plus grand que la fenêtre de contexte

Un vrai projet compte souvent des centaines de milliers de lignes, bien plus que la
[fenêtre de contexte](docs/module4/50-predire-le-mot-suivant/#gpt-un-transformer-qui-prédit-le-jeton-suivant)
du modèle. L'agent ne peut donc pas tout lire, et son harnais l'aide de plusieurs
façons.

- **Explorer plutôt que lire.** Comme dans l'applet, l'agent liste les dossiers,
  cherche avec `grep` les quelques fonctions qui l'intéressent, et ne lit que les
  passages utiles.
- **Des fichiers de consignes.** Un fichier placé à la racine du projet, souvent appelé
  `CLAUDE.md` ou `AGENTS.md`, décrit le projet, ses conventions et les commandes à
  lancer pour le tester. Le harnais le place au début du contexte à chaque session.
  Ce sont les « notes glissées dans le contexte » du chapitre
  « [Prédire le mot suivant](docs/module4/50-predire-le-mot-suivant/#une-conversation-qui-nen-est-pas-une) » :
  le modèle n'apprend rien d'une session à l'autre, mais ces notes, elles, restent.
  La convention `AGENTS.md`, publiée en 2025, est déjà utilisée par des dizaines de
  milliers de projets.
- **Le compactage.** Quand le contexte approche de sa limite, le harnais demande au
  modèle de résumer la session jusque-là, puis repart de ce résumé.
- **Les sous-agents.** L'agent peut confier une recherche à un autre agent, qui
  travaille dans son propre contexte, tout neuf, et ne lui rapporte qu'un résumé. Le
  contexte principal reste ainsi réservé à l'essentiel.

## Pourquoi le code s'y prête si bien

La programmation réunit presque toutes les conditions favorables aux modèles de
langage. Le code est du texte, et il en existe une quantité immense, publique et de
bonne qualité. Surtout, il se **vérifie** : un programme compile ou non, et ses tests
passent ou non. L'agent reçoit à chaque tour un verdict exact, et peut corriger ses
erreurs avant même qu'un humain les voie.

C'est aussi ce qui a permis d'entraîner ces modèles par
[renforcement à partir de récompenses vérifiables](docs/module4/70-du-modele-a-l-assistant/#des-modèles-qui-raisonnent-rlvr) :
on leur donne de vraies tâches de programmation dans un bac à sable, et l'on renforce
les essais dont le résultat passe les tests. Les modèles apprennent ainsi, par
l'expérience, les habitudes du métier : lire avant de modifier, lancer les tests,
interpréter une erreur.

Cette vérification a ses limites. Des tests ne couvrent jamais tout : un programme
peut passer tous ses tests et contenir un défaut, ou une faille de sécurité. Et un
agent pressé d'obtenir une bonne note peut être tenté de modifier les tests plutôt que
le code, un cas de [détournement de la récompense](docs/module4/70-du-modele-a-l-assistant/#le-renforcement-à-partir-de-préférences-humaines-rlhf).

## Mesurer : SWE-bench et la durée des tâches

En octobre 2023, une équipe de Princeton publie **SWE-bench**, un ensemble de 2 294
vrais problèmes signalés sur GitHub dans douze projets Python populaires, comme
Django. Pour chacun, l'agent doit produire une modification du projet, que l'on juge
avec les tests du projet lui-même : ceux qui accompagnaient la correction humaine
doivent maintenant passer, et tous les autres doivent continuer de passer. Le meilleur
modèle de l'époque en résout 2 %.

En août 2024, OpenAI publie une version vérifiée par 93 développeurs, de 500 problèmes
dont l'énoncé et les tests sont jugés corrects. Les scores y montent vite : 33 % à la
publication, 49 % en octobre 2024, plus de 70 % au milieu de 2025, et plus de 80 % à
la fin de 2025. En février 2026, OpenAI cesse de s'en servir, pour trois raisons : les
scores ne progressent presque plus, les tests de nombreux problèmes difficiles
rejettent des solutions pourtant correctes, et les modèles reproduisent de mémoire
certaines corrections, vues pendant leur entraînement. On retrouve les limites des
scores présentées au chapitre
« [Passer à l'échelle](docs/module4/60-passer-a-l-echelle/#que-mesurent-les-scores) ».
Des ensembles plus difficiles et mieux protégés lui succèdent, comme SWE-bench Pro,
dont une partie des projets n'est pas publique.

Une autre mesure, proposée en mars 2025 par l'organisme METR, ne compte pas les
problèmes résolus, mais la **durée des tâches** qu'un agent mène à bien. On mesure le
temps qu'il faut à un programmeur humain pour chaque tâche, et l'on cherche la durée
à laquelle l'agent réussit une fois sur deux. En mars 2025, elle est d'environ une
heure. Elle double à peu près tous les sept mois depuis 2019, et plus vite encore
depuis 2024. Au début de 2026, elle dépasse une dizaine d'heures. En février 2026, un
chercheur d'Anthropic fait écrire par seize agents travaillant en parallèle un
compilateur pour le langage C, de 100 000 lignes, capable de compiler le noyau Linux,
en deux semaines et pour environ 20 000 dollars de calcul. Le résultat a ses limites,
mais il était impensable deux ans plus tôt.

## Permissions, bac à sable et incidents

Un agent de programmation exécute des commandes sur un vrai ordinateur, ce qui lui
donne un pouvoir considérable. Selon le principe posé au chapitre précédent,
[le modèle propose, le harnais dispose](docs/module4/80-outils-et-agents/#le-harnais-et-lappel-doutils) :
c'est le harnais qui fixe les limites. Il offre en général plusieurs **modes de
permission** : demander l'accord de l'utilisateur avant chaque commande ou chaque
modification, accepter automatiquement les modifications de fichiers mais pas les
commandes, se contenter de proposer un plan, ou tout accepter, ce qui est
dangereux. Il peut aussi faire tourner l'agent dans un **bac à sable**, où le système
d'exploitation l'empêche de sortir du dossier du projet ou d'accéder au réseau.

Les incidents réels montrent pourquoi ces précautions comptent.

- **Une base de données effacée.** En juillet 2025, pendant une expérience menée sur la
  plateforme Replit, un agent efface la base de données de production d'une
  entreprise, malgré la consigne de ne rien modifier, puis affirme à tort qu'elle ne
  peut pas être restaurée.
- **Un ticket piégé.** En mai 2025, des chercheurs montrent qu'un message malveillant
  déposé sur un projet public de GitHub peut détourner un agent qui le lit, et lui
  faire recopier des données d'un projet privé dans un endroit public. C'est
  l'[injection d'instructions](docs/module4/80-outils-et-agents/#des-agents-un-modèle-et-son-harnais-en-boucle)
  du chapitre précédent. Le programmeur Simon Willison parle de **trio fatal**
  (*lethal trifecta*) quand un agent réunit trois choses : un accès à des données
  privées, la lecture de contenus non fiables, et un moyen de communiquer vers
  l'extérieur.
- **Un logiciel malveillant qui utilise les agents.** En août 2025, une version piégée
  d'une bibliothèque JavaScript très répandue lance les agents de programmation
  installés sur l'ordinateur, en désactivant leurs permissions, pour leur faire
  chercher des clés d'accès et des mots de passe.

## Programmer autrement

Le 2 février 2025, l'informaticien Andrej Karpathy décrit une nouvelle façon de
programmer, qu'il appelle le *vibe coding* : se laisser porter, accepter toutes les
modifications de l'agent sans les lire, recoller les messages d'erreur, et oublier que
le code existe. Il la réserve lui-même aux projets jetables d'une fin de semaine.
L'expression devient le mot de l'année 2025 du dictionnaire Collins. D'autres, comme
Simon Willison, soulignent qu'elle ne décrit pas la programmation assistée en
général : un professionnel qui utilise un agent relit, teste et comprend ce qu'il
intègre à son projet.

L'effet réel sur la productivité est plus difficile à mesurer qu'il n'y paraît. En
juillet 2025, METR publie une expérience contrôlée auprès de 16 développeurs
expérimentés, sur 246 tâches de leurs propres projets. Avec l'IA, ils mettent 19 %
plus de temps qu'en travaillant seuls, alors qu'ils s'attendaient à aller 24 % plus
vite, et qu'ils croient, une fois l'expérience terminée, être allés 20 % plus vite.
Une nouvelle étude, au début de 2026, avec des outils plus récents, suggère au
contraire une accélération, que METR juge toutefois peu fiable. La leçon dépasse ces
chiffres : l'impression d'aller vite n'est pas une mesure.

L'adoption, elle, est massive. En octobre 2024, Google annonce que plus du quart de son
nouveau code est produit par l'IA, puis relu par des ingénieurs ; en avril 2026, les
trois quarts. La confiance reste mesurée : en 2025, selon Stack Overflow, près de la
moitié des développeurs se méfient de l'exactitude de ces outils, et deux sur trois
se plaignent de solutions « presque justes ». Le métier se déplace : moins de lignes
écrites à la main, davantage de temps à préciser ce qu'on veut, à découper le travail,
à relire, à tester et à décider de l'architecture. Savoir lire et comprendre du code
reste indispensable, justement pour pouvoir juger celui de l'agent. Ce que cela
change à l'emploi et à l'apprentissage de la programmation est l'une des questions du
[Module 5](docs/module5).

## Ce cours, écrit avec un agent

Ce cours en est lui-même un exemple. Son auteur l'a rédigé avec l'aide d'un agent de
programmation, Claude Code. Le cours est un ensemble de fichiers texte, au format
Markdown, transformés en site Web par le programme Hugo, et suivis par git. L'agent lit
et modifie ces fichiers, écrit les petits programmes Python qui produisent les figures
et les applets, lance un script qui vérifie qu'aucun lien n'est cassé, et enregistre
chaque version avec git. Les faits récents, comme ceux de ce chapitre, sont vérifiés
en ligne par des sous-agents. L'auteur décide du plan et du contenu, relit chaque
passage et valide chaque changement. Le modèle propose, l'auteur dispose.

Les agents présentés jusqu'ici lisent et écrivent du texte. Le
[chapitre suivant](docs/module4/90-mots-et-images) montre comment on a relié les mots
et les images.
