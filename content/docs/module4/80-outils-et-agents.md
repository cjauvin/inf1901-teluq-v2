---
title: "Des outils et des agents"
weight: 80
slug: outils-et-agents
---

# Des outils et des agents

Un assistant comme ceux présentés au chapitre
« [Du modèle à l'assistant](docs/module4/70-du-modele-a-l-assistant) » ne fait que
produire du texte à partir du texte qu'on lui donne. Ce fonctionnement a trois
limites.

- **Ses connaissances sont figées.** Le modèle ne connaît que ce qui figurait dans
  ses données d'entraînement, jusqu'à une **date de coupure** (*knowledge cutoff*).
  Il ignore les événements plus récents, et les documents privés d'une entreprise ou
  d'une personne.
- **Il calcule mal.** Un modèle de langage prédit des jetons. Il peut écrire le
  résultat d'une multiplication sans l'avoir vraiment effectuée.
- **Il n'agit pas.** Il ne peut ni consulter une page Web, ni envoyer un courriel, ni
  modifier un fichier.

Ce chapitre présente les moyens qui ont été développés pour dépasser ces limites :
bien formuler les requêtes, donner au modèle des documents à consulter, lui confier
des outils, et enfin le laisser enchaîner lui-même les actions. Ces systèmes
s'appellent des **agents**.

## Formuler la requête

Le texte qu'on donne au modèle s'appelle la **requête** (*prompt*). Comme le modèle
continue ce texte, sa formulation a une grande influence sur la réponse. La rédaction
des requêtes (*prompt engineering*) repose sur quelques principes simples.

- Préciser la tâche, le public visé et la forme attendue : « Explique la
  photosynthèse à un élève de 12 ans, en cinq phrases. »
- Donner des exemples de ce qu'on attend, ce qui exploite
  l'[apprentissage en contexte](docs/module4/60-passer-a-l-echelle/#apprendre-dans-le-contexte).
- Fournir les informations nécessaires plutôt que de compter sur la mémoire du
  modèle, par exemple en collant le texte à résumer.
- Demander un raisonnement par étapes pour les problèmes difficiles, comme la
  [chaîne de pensée](docs/module4/70-du-modele-a-l-assistant/#des-modèles-qui-raisonnent).

Les assistants reçoivent aussi une **requête système** (*system prompt*), rédigée par
l'entreprise ou le développeur, que l'utilisateur ne voit généralement pas. Elle fixe
le rôle de l'assistant, son ton, ce qu'il doit refuser et les outils dont il dispose.
Toute la conversation, requête système comprise, doit tenir dans la
[fenêtre de contexte](docs/module4/50-predire-le-mot-suivant/#gpt-un-transformer-qui-prédit-le-jeton-suivant)
du modèle.

## Chercher d'abord, répondre ensuite

Pour répondre à une question sur des documents récents ou privés, on peut chercher
les passages utiles, puis les placer dans le contexte du modèle avec la question.
C'est la **génération augmentée par la recherche** (*retrieval-augmented generation*,
RAG), présentée en 2020 par Patrick Lewis et ses collègues, chez Facebook. La
recherche utilise des [plongements](docs/module4/45-des-mots-aux-nombres/#tout-devient-vecteur) :
chaque passage de la base de documents est représenté par un vecteur, et on retient
ceux dont le vecteur est le plus proche de celui de la question. On trouve ainsi un
passage qui répond à la question même s'il n'en reprend pas les mots.

{{< image src="/images/module4/rag.svg" alt="Un schéma. La question de l'utilisateur est transformée en plongement. On cherche, dans une base de documents déjà transformés en plongements, les passages dont le vecteur est le plus proche. Les trois passages trouvés sont ajoutés au contexte du modèle de langage, avec la question. Le modèle rédige une réponse appuyée sur ces passages, en les citant." title="La génération augmentée par la recherche : on cherche les passages utiles, on les place dans le contexte, et le modèle répond à partir de ces passages." loading="lazy" >}}

Cette méthode a deux avantages. Le modèle s'appuie sur des sources à jour, sans être
réentraîné, et il peut les citer, ce qui permet de vérifier sa réponse. Elle est
aujourd'hui utilisée par les moteurs de recherche qui répondent par un texte, et par
les assistants d'entreprise qui consultent la documentation interne. Elle ne supprime
pas les erreurs : si la recherche trouve un mauvais passage, le modèle peut s'en
servir avec assurance.

Une variante, présentée par Microsoft en 2024, organise d'abord les documents en un
**graphe de connaissances** (*GraphRAG*), où les personnes, les lieux et les concepts
sont reliés entre eux. On retrouve là les réseaux de concepts reliés de l'IA
symbolique, dont le chapitre « [Les hivers et la bascule](docs/module1/60-hivers/#lhéritage-invisible) »
du Module 1 montrait qu'ils structurent encore une grande partie du savoir sur le Web.
Deux conceptions du savoir s'y rejoignent : le savoir organisé à la main, ou
automatiquement, dans un graphe, et le savoir absorbé par un modèle de langage à
partir du texte.

## Confier des outils au modèle

Un modèle de langage ne peut qu'écrire du texte. Mais il peut écrire un texte qui
demande une action, dans un format convenu à l'avance, comme
`calculatrice("1 248 × 37")`. Un programme qui entoure le modèle reconnaît cette
demande, exécute l'outil, et ajoute le résultat au contexte. Le modèle reprend alors
sa rédaction en tenant compte du résultat. En février 2023, une équipe de Meta montre
avec Toolformer qu'un modèle peut apprendre de lui-même quand faire appel à une
calculatrice, à un moteur de recherche ou à un traducteur. Les principaux assistants
proposent depuis 2023 cet **appel d'outils** (*tool use*, ou *function calling*).

Les outils compensent les faiblesses du modèle. Une calculatrice ou un programme
exécuté donne un résultat exact. Une recherche sur le Web donne une information à
jour. Un outil de lecture de fichiers donne accès aux documents de l'utilisateur. En
novembre 2024, Anthropic propose une norme ouverte, le *Model Context Protocol*
(MCP), pour brancher n'importe quel outil sur n'importe quel assistant, à la façon
d'une prise universelle.

## Des agents

Un **agent** est un système qui enchaîne lui-même plusieurs étapes pour accomplir une
tâche : il raisonne, choisit un outil, observe le résultat, puis décide de l'étape
suivante, jusqu'à ce que la tâche soit terminée. Ce schéma, raisonner, agir, observer,
a été décrit en 2022 sous le nom de ReAct. Le mot *agent* reprend celui de
l'[apprentissage par renforcement](docs/module2/80-trois-facons-d-apprendre/#apprendre-par-lexpérience-le-renforcement)
du Module 2 : une entité qui agit dans un environnement et observe les conséquences
de ses actions.

L'applet ci-dessous montre, étape par étape, le contexte d'un agent. Les traces ont
été rédigées pour l'exercice, mais elles suivent la forme réelle de ces échanges.
Le premier scénario montre une question qui demande deux recherches et un calcul. Le
second montre ce qui peut mal tourner.

{{< applet src="/html/applets/agent.html" height="380" >}}

Le second scénario illustre une **injection d'instructions** (*prompt injection*).
Le modèle reçoit tout dans un même flux de texte : les consignes de l'utilisateur, et
le contenu des pages, des courriels ou des documents qu'il lit. Il distingue mal les
deux. Une instruction cachée dans une page peut donc détourner un agent, comme les
[exemples adverses](docs/module3/90-tromper-un-reseau/#se-défendre) du Module 3
détournaient un classificateur d'images. Plus un agent dispose d'outils puissants,
plus ce risque est grave. Les précautions habituelles consistent à demander la
confirmation de l'utilisateur avant toute action importante, à limiter les outils et
les accès de l'agent, et à traiter le contenu lu comme des données plutôt que comme
des ordres. Aucune de ces précautions n'est infaillible.

Les agents se sont multipliés à partir de 2024.

- **Les agents de programmation**, comme Claude Code (2025) ou Codex (2025), lisent le
  code d'un projet, le modifient, exécutent les tests et corrigent leurs erreurs, sur
  des tâches qui prenaient auparavant des heures à un programmeur.
- **Les agents qui utilisent un ordinateur** voient l'écran et manipulent la souris
  et le clavier, comme le fait un humain. Anthropic présente cette capacité en
  octobre 2024, et OpenAI l'année suivante.
- **Les agents de recherche** consultent des dizaines de sources et rédigent un
  rapport avec leurs références.

Un agent qui enchaîne des étapes accumule aussi les erreurs : une petite erreur au
début peut conduire à une longue suite d'actions inutiles ou nuisibles. La question
de savoir quelles décisions on peut confier à un agent, et qui est responsable de ses
actions, est l'une de celles que pose le [Module 5](docs/module5).

Les agents rappellent aussi la
[recherche dans un espace d'états](docs/module1/30-chercher-raisonner) du Module 1 :
explorer des actions possibles pour atteindre un but. La différence tient à la façon
de choisir l'action suivante. Les programmes du Module 1 suivaient des règles et
des heuristiques écrites à la main. Le modèle de langage choisit d'après tout ce qu'il a
appris en lisant.

Les assistants présentés jusqu'ici lisent et écrivent du texte. Le
[chapitre suivant](docs/module4/90-mots-et-images) montre comment on a relié les mots et les images.
