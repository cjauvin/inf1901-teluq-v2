---
title: "Des outils, un harnais et des agents"
weight: 80
slug: outils-et-agents
---

# Des outils, un harnais et des agents

Un assistant comme ceux présentés au chapitre
« [Du modèle à l'assistant](docs/module4/70-du-modele-a-l-assistant) » ne fait que
produire du texte à partir du texte qu'on lui donne. Ce fonctionnement a trois
limites.

- **Ses connaissances sont figées.** Le modèle ne connaît que ce qui figurait dans
  ses données d'entraînement, jusqu'à une **date de coupure** (*knowledge cutoff*).
  Il ignore les événements plus récents, et les documents privés d'une entreprise ou
  d'une personne. Le laisser apprendre en continu est plus difficile qu'il n'y paraît,
  comme l'explique la section « [Pourquoi ne pas le laisser apprendre ?](#pourquoi-ne-pas-le-laisser-apprendre) ».
- **Il calcule mal.** Un modèle de langage prédit des jetons. Il peut écrire le
  résultat d'une multiplication sans l'avoir vraiment effectuée.
- **Il n'agit pas.** Il ne peut ni consulter une page Web, ni envoyer un courriel, ni
  modifier un fichier.

Ce chapitre commence par expliquer ce qu'est vraiment une conversation avec un
assistant, et pourquoi il n'apprend rien de ses échanges. Il présente ensuite les
moyens qui ont été développés pour dépasser ces limites : bien formuler les requêtes, donner au modèle des documents à consulter, lui confier
des outils. Il présente ensuite les systèmes qui enchaînent eux-mêmes les actions,
en boucle, jusqu'à ce qu'une tâche soit accomplie : les **agents**.

## Formuler la requête

Le texte qu'on donne au modèle s'appelle la **requête** (*prompt*). Comme le modèle
continue ce texte, sa formulation a une grande influence sur la réponse. La rédaction
des requêtes (*prompt engineering*) repose sur quelques principes simples.

- Préciser la tâche, le public visé et la forme attendue : « Explique la
  photosynthèse à un élève de 12 ans, en cinq phrases. »
- Donner des exemples de ce qu'on attend, ce qui exploite
  l'[apprentissage dans le contexte](docs/module4/60-passer-a-l-echelle/#apprendre-dans-le-contexte).
- Fournir les informations nécessaires plutôt que de compter sur la mémoire du
  modèle, par exemple en collant le texte à résumer.
- Demander un raisonnement par étapes pour les problèmes difficiles, comme la
  [chaîne de pensée](docs/module4/70-du-modele-a-l-assistant/#des-modèles-qui-raisonnent-rlvr).

## Une conversation qui n'en est pas une

Une conversation avec un assistant ressemble à un échange entre deux
interlocuteurs : on pose une question, il répond, on enchaîne, il se souvient de ce
qu'on a dit. Le mécanisme est pourtant tout autre.

Le modèle n'a aucune mémoire d'une réplique à l'autre. Ses paramètres sont fixés une
fois pour toutes à la fin de l'entraînement, et rien de ce qu'on lui dit ne les
modifie. Ce qui donne l'illusion de la continuité, c'est le programme qui
l'entoure, son harnais, présenté dans la
[section suivante](#la-requête-système-et-le-harnais).
À chaque nouvelle réplique, il reconstitue un seul long texte, qui
contient les instructions de départ, tous les messages échangés depuis le début et
toutes les réponses déjà données par le modèle. Il le lui présente comme un texte
à continuer. Le modèle prédit alors un jeton, qu'on ajoute au texte, puis le
suivant, en tenant compte chaque fois de la totalité de ce qui précède. À la
réplique suivante, tout recommence. En pratique, les calculs déjà faits sont
conservés pour aller plus vite, mais le principe ne change pas : le modèle ne voit
qu'un texte.

{{< image src="/images/module4/conversation.svg" alt="Deux rangées de trois répliques. En haut, une personne : à chaque réplique, seule la nouvelle question entre ; ce qui change, c'est un état intérieur, dessiné dans une tête, qui grandit et évolue d'une réplique à l'autre. En bas, un modèle de langage : à la première réplique, il reçoit les instructions de départ et la première question, et produit la première réponse ; à la deuxième, il reçoit tout cela de nouveau, plus la deuxième question ; à la troisième, encore tout, plus la troisième question. La barre de texte s'allonge à chaque réplique, alors que le modèle, au milieu, reste identique, avec des paramètres fixes." title="Pour une personne, seule la nouvelle phrase entre, et c'est son état intérieur qui porte la conversation. Pour le modèle, chaque réplique repart de zéro : toute la conversation lui est présentée de nouveau, comme un texte à continuer." loading="lazy" >}}

Une conversation humaine fonctionne autrement. Nous ne relisons pas la
transcription de l'échange avant chaque réplique. Ce que l'autre dit modifie au fur
et à mesure notre état intérieur, ce que nous comprenons, croyons et voulons. Nous
oublions vite les mots exacts, mais nous retenons l'essentiel, et nous nous en
souviendrons demain. Le modèle fait presque l'inverse.

- Il dispose de chaque mot exact de la conversation, tant qu'elle tient dans sa
  [fenêtre de contexte](docs/module4/50-predire-le-mot-suivant/#gpt-un-transformer-qui-prédit-le-jeton-suivant).
- Il n'a rien d'autre : aucun souvenir de la veille, sauf si le harnais glisse
  des notes dans le texte qu'il lui présente.
- Quand la conversation dépasse la fenêtre, les passages les plus anciens sont
  simplement retirés, et il les oublie d'un coup.

On peut se représenter chaque réplique comme si l'on remettait la transcription
complète à un nouvel interlocuteur, qui ne vous a jamais rencontré, en lui demandant
d'écrire la suite. C'est la situation du héros de *Memento* (Christopher Nolan,
2000) : incapable de former de nouveaux souvenirs, il ne s'y retrouve qu'en relisant
ses notes.

C'est pourquoi la taille de la fenêtre compte autant, et pourquoi elle est passée de
512 jetons en 2018 à un million en 2024. Une fenêtre plus grande permet :

- de tenir de longues conversations sans que le début s'efface ;
- de confier au modèle un document entier (un contrat, un mémoire, un livre, tout le
  code d'un logiciel) et de l'interroger sur l'ensemble plutôt que sur des extraits ;
- de lui donner de nombreux exemples dans la requête, pour
  l'[apprentissage dans le contexte](docs/module4/60-passer-a-l-echelle/#apprendre-dans-le-contexte) ;
- de laisser un [agent](#des-agents-un-modèle-et-son-harnais-en-boucle) accumuler le
  résultat de ses actions au fil d'une longue tâche.

Tout ce que le modèle doit savoir pour répondre, et qu'il n'a pas appris pendant
l'entraînement, doit se trouver dans cette fenêtre. Quand les documents n'y tiennent
pas, il faut choisir les passages à y placer. C'est la
[génération augmentée par la recherche](#chercher-dabord-répondre-ensuite-rag).

Une grande fenêtre a toutefois un prix. Dans l'attention, chaque jeton est comparé à
tous ceux qui le précèdent : doubler la longueur du texte multiplie à peu près par
quatre ces calculs. C'est le
[coût de l'auto-attention](docs/module3/70-attention-transformer/#pourquoi-il-a-tout-changé)
déjà signalé au Module 3. Plus une conversation est longue, plus chaque réponse coûte cher.
De plus, les modèles n'exploitent pas toute leur fenêtre aussi bien. En 2023, Nelson
Liu et ses collègues, à Stanford, montrent qu'ils retrouvent mieux une information
placée au début ou à la fin d'un long texte qu'au milieu (*lost in the middle*).

{{% hint warning %}}
**Deux idées à bien saisir**

Les deux idées suivantes vont à l'encontre de l'intuition. Elles comptent parmi les
aspects des grands modèles de langage que le grand public comprend le plus souvent
mal.

1. **Une conversation avec un modèle de langage n'en est pas une, au sens
   habituel.** Le modèle ne suit pas l'échange. À chaque réplique, toute la
   conversation lui est présentée de nouveau, depuis le début, comme un texte à
   continuer.
2. **Le modèle n'apprend rien de ses conversations.** Au cours d'un échange, il peut
   sembler retenir une correction, s'adapter à une préférence ou apprendre une façon
   de faire. C'est l'[apprentissage dans le contexte](docs/module4/60-passer-a-l-echelle/#apprendre-dans-le-contexte).
   Mais tout cela n'existe que dans le texte qu'on lui présente : ses paramètres ne
   changent pas. Une nouvelle conversation repart de zéro, et une erreur corrigée
   dans un échange pourra être refaite dans le suivant. Les fonctions de « mémoire »
   de certains assistants ne changent rien au principe, puisqu'elles glissent des
   notes dans ce texte. Seul un nouvel entraînement modifie un modèle. Une entreprise
   peut se servir des conversations pour entraîner une version suivante, mais ce sera
   un autre modèle, publié des mois plus tard. La section
   « [Pourquoi ne pas le laisser apprendre ?](#pourquoi-ne-pas-le-laisser-apprendre) », plus bas,
   explique pourquoi.
{{% /hint %}}

## La requête système et le harnais

Les assistants reçoivent aussi une **requête système** (*system prompt*), rédigée par
l'entreprise ou le développeur, que l'utilisateur ne voit généralement pas. Elle fixe
le rôle de l'assistant, son ton, ce qu'il doit refuser et les outils dont il dispose.
Toute la conversation, requête système comprise, doit tenir dans la
[fenêtre de contexte](docs/module4/50-predire-le-mot-suivant/#gpt-un-transformer-qui-prédit-le-jeton-suivant)
du modèle.

Il n'y a pas de canal séparé pour cette requête. Comme toute la
[conversation](#une-conversation-qui-nen-est-pas-une),
elle est simplement placée **au début du texte** que le modèle reçoit. Le programme qui
entoure le modèle, qu'on appelle son **harnais** (*harness*), assemble ce texte selon un **gabarit de conversation** (*chat template*), qui délimite
chaque partie par des jetons spéciaux. Ces jetons ne correspondent à aucun texte qu'un
utilisateur pourrait taper. Schématiquement, le modèle reçoit ceci :

```
<|début|>système
Tu es l'assistant de la librairie Le Signet. Réponds en français, avec courtoisie.
Ne donne jamais d'avis médical. Tu peux utiliser l'outil chercher_catalogue(titre).
<|fin|>
<|début|>utilisateur
Avez-vous Kamouraska, d'Anne Hébert ?
<|fin|>
<|début|>assistant
```

Le texte s'arrête après la marque qui ouvre la réplique de l'assistant. Le modèle fait
alors ce qu'il a toujours fait : il prédit la suite, jeton après jeton, jusqu'à
produire la marque de fin de réplique, qui rend la main à l'utilisateur. La
description des outils disponibles est elle aussi écrite dans la partie système, sous
forme de texte.

{{< image src="/images/module4/gabarit-conversation.svg" alt="En haut, trois sources : la requête système, rédigée par l'entreprise, que l'utilisateur ne voit pas, avec la description des outils ; les échanges précédents ; le nouveau message de l'utilisateur. Le harnais les assemble en un seul texte, selon un gabarit de conversation. Ce texte est dessiné au milieu : chaque partie commence par une marque spéciale, début système, début utilisateur, début assistant, et se termine par une marque de fin. Le texte s'arrête après la marque qui ouvre la réplique de l'assistant. Le modèle, à droite, le continue jeton après jeton, « Oui, nous l'avons en format poche », jusqu'à produire la marque de fin, qui rend la main à l'utilisateur. En bas, la priorité apprise pendant le post-entraînement : la requête système d'abord, puis l'utilisateur, puis le contenu des documents et des outils." title="Le gabarit de conversation. La requête système n'est qu'un début de texte ; c'est le post-entraînement qui apprend au modèle à lui donner priorité." loading="lazy" >}}

Rien, dans le mécanisme, n'oblige le modèle à respecter la requête système plutôt que
les messages de l'utilisateur. C'est le
[post-entraînement](docs/module4/70-du-modele-a-l-assistant/#un-modèle-de-base-ne-répond-pas)
qui lui apprend, par des exemples, à donner priorité à la partie système quand les
deux se contredisent. En 2024, une équipe d'OpenAI décrit cette **hiérarchie des
instructions** (*instruction hierarchy*) : d'abord la requête système, puis
l'utilisateur, puis le contenu des documents et des outils. Comme tout ce qui est
appris, cette priorité est imparfaite, et c'est pourquoi les
[injections d'instructions](#des-agents-un-modèle-et-son-harnais-en-boucle) restent possibles.

## Pourquoi ne pas le laisser apprendre ?

On pourrait imaginer un modèle qui continue d'ajuster ses paramètres après
l'entraînement. Il intégrerait les nouvelles connaissances au fur et à mesure,
retiendrait les corrections de ses utilisateurs, et n'aurait plus de date de coupure, la limite présentée au début de ce chapitre.
C'est l'**apprentissage continu** (*continual learning*). Les humains apprennent ainsi
toute leur vie, mais les réseaux de neurones y parviennent mal, pour plusieurs
raisons.

- **L'oubli catastrophique** (*catastrophic forgetting*). Dans un réseau, chaque
  connaissance est répartie sur un grand nombre de poids, et chaque poids participe à
  un grand nombre de connaissances. Si on entraîne le réseau sur de nouveaux exemples
  seulement, la [descente de gradient](docs/module2/50-entrainer-un-modele/#apprendre-cest-descendre-la-pente)
  modifie ces poids sans tenir compte de ce qu'ils encodaient déjà, et les anciennes
  connaissances se dégradent. Michael McCloskey et Neal Cohen le décrivent dès 1989.
  Pendant l'entraînement initial, ce problème ne se pose pas : les exemples sont
  mélangés, et chaque pas d'apprentissage voit un peu de tout. Les remèdes connus
  atténuent le problème sans le régler. On peut rejouer d'anciens exemples parmi les
  nouveaux, ou protéger les poids les plus importants pour les tâches déjà apprises
  (James Kirkpatrick et ses collègues, chez DeepMind, en 2017).
- **Le coût.** Ajuster les paramètres demande la rétropropagation, plusieurs fois plus
  coûteuse que la simple prédiction. Surtout, un même modèle sert des millions de
  personnes à la fois. Pour qu'il apprenne de chacune, il faudrait garder une version distincte
  du modèle par utilisateur. Ce serait une copie de ses centaines de milliards de
  paramètres, ou au moins d'une partie d'entre eux, puisqu'on sait adapter un modèle
  en ne modifiant qu'une petite fraction de ses paramètres.
- **La fiabilité.** Ce que les utilisateurs disent au modèle peut être faux, ou
  malveillant. En 2016, Microsoft met en ligne Tay, un robot conversationnel qui
  apprend de ses échanges sur Twitter. Des internautes lui font tenir des propos
  racistes en quelques heures, et Microsoft le retire au bout de seize heures. Ce
  qu'un modèle apprend d'une personne pourrait aussi ressortir chez une autre, y
  compris des renseignements privés.
- **L'évaluation.** Un modèle est testé longuement avant d'être publié. Un modèle qui
  change sans cesse ne pourrait jamais l'être tout à fait.

{{< image src="/images/module4/oubli-catastrophique.svg" alt="Un graphique de la justesse d'un petit réseau au fil de l'entraînement. Pendant la première moitié, il apprend à reconnaître les chiffres manuscrits 0 à 4 (tâche A), et sa justesse sur cette tâche monte à 99 %. Pendant la seconde moitié, on ne lui montre plus que les chiffres 5 à 9 (tâche B). Sa justesse sur la tâche B monte à 97 %, mais celle sur la tâche A s'effondre, jusqu'à 0 % : il a oublié. Une courbe en pointillés montre la même expérience quand on mêle à chaque lot 8 anciens exemples de la tâche A sur 32 : la justesse sur la tâche A reste alors à 87 %." title="Une petite expérience réelle d'oubli catastrophique. Un réseau à une couche cachée apprend les chiffres 0 à 4, puis seulement les chiffres 5 à 9 : en quelques dizaines de pas, il ne reconnaît plus aucun des premiers. Rejouer quelques anciens exemples suffit ici à limiter l'oubli, mais à l'échelle d'un grand modèle de langage, aucun remède ne règle complètement le problème." loading="lazy" >}}

Le cerveau, lui, semble disposer de deux systèmes complémentaires. L'hippocampe
enregistre rapidement les expériences nouvelles, et le néocortex les intègre
lentement, en les entremêlant aux anciennes, notamment pendant le sommeil (James
McClelland, Bruce McNaughton et Randall O'Reilly, 1995). En attendant de savoir faire
de même, on contourne le problème : de nouvelles versions du modèle, entraînées tous
les quelques mois, des notes glissées dans le contexte, et la recherche de documents
présentée au chapitre
« [Chercher d'abord, répondre ensuite](#chercher-dabord-répondre-ensuite-rag) ».
Une piste de recherche, l'**entraînement au moment du test**
(*test-time training*), ajuste temporairement les poids du modèle sur le problème à
résoudre, puis les oublie ; le chapitre
« [Le défi ARC](docs/module4/88-le-defi-arc/#le-prix-arc-de-2024-et-lentraînement-au-moment-du-test) »
en montre l'efficacité. L'apprentissage continu reste un problème de recherche ouvert.

## Chercher d'abord, répondre ensuite (RAG)

Pour répondre à une question sur des documents récents ou privés, on peut chercher
les passages utiles, puis les placer dans le contexte du modèle avec la question.
C'est la **génération augmentée par la recherche** (*retrieval-augmented generation*,
RAG), présentée en 2020 par Patrick Lewis et ses collègues, chez Facebook. La
recherche utilise des [plongements](docs/module4/45-des-mots-aux-nombres/#tout-devient-vecteur) :
chaque passage de la base de documents est représenté par un vecteur, et on retient
ceux dont le vecteur est le plus proche de celui de la question. On trouve ainsi un
passage qui répond à la question même s'il n'en reprend pas les mots.

{{< image src="/images/module4/rag.svg" alt="Un schéma. La question de l'utilisateur est transformée en plongement. On cherche, dans une base de documents déjà transformés en plongements, les passages dont le vecteur est le plus proche. Les trois passages trouvés sont ajoutés au contexte du modèle de langage, avec la question. Le modèle rédige une réponse appuyée sur ces passages, en les citant." title="La génération augmentée par la recherche : on cherche les passages utiles, on les place dans le contexte, et le modèle répond à partir de ces passages." loading="lazy" >}}

Concrètement, la recherche se prépare d'avance. On découpe les documents en passages
de quelques centaines de mots, et un modèle de plongements calcule le vecteur de
chacun. Ces vecteurs sont rangés, avec le texte de leur passage, dans une **base de
données vectorielle** (*vector database*). Au moment de la question, on calcule le
vecteur de la question et on demande à la base les passages dont le vecteur est le
plus proche. C'est exactement la recherche des
[k plus proches voisins](docs/module2/40-predire-par-ressemblance/#les-k-plus-proches-voisins)
du Module 2, appliquée à des vecteurs de plusieurs centaines de dimensions.

La difficulté est l'échelle. Comparer la question à des millions de vecteurs, un par
un, serait trop lent. Les bases vectorielles font donc une recherche
**approximative** : elles acceptent de manquer parfois un voisin, en échange d'une
réponse en quelques millisecondes. La méthode la plus répandue, HNSW (Yury Malkov et
Dmitry Yashunin, 2016), relie les vecteurs en un graphe à plusieurs étages. On part
d'un étage clairsemé, où l'on fait de grands sauts, comme sur une autoroute, puis on
descend vers des étages de plus en plus denses, comme dans les rues d'un quartier,
jusqu'aux voisins de la question. La bibliothèque Faiss, publiée par Meta en 2017, et
des bases spécialisées comme Pinecone, Milvus ou Chroma, ou l'extension pgvector de
PostgreSQL, offrent ce type de recherche.

{{< image src="/images/module4/hnsw.svg" alt="Trois plans superposés, les étages d'un graphe de vecteurs. L'étage du bas contient tous les vecteurs, reliés à leurs voisins proches ; l'étage du milieu en contient une quinzaine, reliés à des voisins plus éloignés ; l'étage du haut, seulement quatre. Une étoile rouge marque la position de la question, au même endroit à chaque étage. La recherche part d'un point d'entrée à l'étage du haut, fait deux grands sauts vers la question, descend à l'étage du milieu, se rapproche encore, puis descend à l'étage du bas, où quelques petits pas l'amènent au plus proche voisin de la question. Les trois plus proches voisins trouvés sont entourés." title="La recherche dans un graphe à étages (HNSW), réellement calculée sur des points tirés au hasard : quelques grands sauts en haut, quelques petits pas en bas, au lieu de comparer la question à tous les vecteurs." loading="lazy" >}}

Les plongements ont aussi un point faible : ils saisissent le sens, mais distinguent
mal un nom propre rare, un numéro de produit ou un code d'erreur. On combine donc
souvent la recherche par vecteurs avec une recherche par mots-clés, héritière du
[tf-idf](docs/module4/42-les-outils-statistiques/#représenter-des-documents) présenté
au chapitre « Les outils statistiques ». C'est la **recherche hybride** (*hybrid search*).

Cette méthode a deux avantages. Le modèle s'appuie sur des sources à jour, sans être
réentraîné, et il peut les citer, ce qui permet de vérifier sa réponse. Elle est
aujourd'hui utilisée par les moteurs de recherche qui répondent par un texte, et par
les assistants d'entreprise qui consultent la documentation interne. Elle ne supprime
pas les erreurs : si la recherche trouve un mauvais passage, le modèle peut s'en
servir avec assurance.

Une variante, présentée par Microsoft en 2024, organise d'abord les documents en un
**graphe de connaissances** (*knowledge graph*), où les personnes, les lieux et les
concepts sont reliés entre eux. Cette méthode s'appelle GraphRAG. On retrouve là les réseaux de concepts reliés de l'IA
symbolique, dont le chapitre « [Les hivers et la bascule](docs/module1/60-hivers/#lhéritage-invisible) »
du Module 1 montrait qu'ils structurent encore une grande partie du savoir sur le Web.
Deux conceptions du savoir s'y rejoignent : le savoir organisé à la main, ou
automatiquement, dans un graphe, et le savoir absorbé par un modèle de langage à
partir du texte.

## Le harnais et l'appel d'outils

Un modèle de langage ne peut qu'écrire du texte. Il ne peut ni consulter une base de
données, ni faire un calcul exact, ni envoyer un courriel. Mais il peut écrire un texte
qui **demande** une action, dans un format convenu à l'avance. Son harnais, présenté
[plus haut](#la-requête-système-et-le-harnais), lit cette demande, l'exécute, et lui
rapporte le résultat.
C'est l'**appel d'outils** (*tool use*, ou *function calling*). Quand on dit qu'un
modèle « décide d'appeler un outil », voici exactement ce qui se passe.

**1. L'outil est décrit au modèle, en texte.** La requête système contient, pour
chaque outil, son nom, une phrase qui dit à quoi il sert, et la liste de ses
paramètres, avec leur type :

```
Outil : chercher_catalogue
Description : cherche un livre dans le catalogue de la librairie
              et donne son prix et sa disponibilité.
Paramètres : titre (texte, obligatoire)
```

Le modèle ne voit jamais le code de l'outil, seulement cette description.

**2. Le modèle écrit un appel, au lieu d'une réponse.** L'utilisateur demande
« Combien coûte Kamouraska ? ». Après la marque qui ouvre la réplique de l'assistant,
le jeton le plus probable n'est pas un mot, mais une marque spéciale d'appel d'outil,
suivie d'un petit texte structuré :

```
<|début|>assistant
<|appel|>{"outil": "chercher_catalogue", "arguments": {"titre": "Kamouraska"}}<|fin|>
```

Rien ne s'est encore passé. Le modèle a seulement prédit des jetons, comme toujours,
et la génération s'arrête à la marque de fin.

**3. Le harnais exécute l'appel.** Il reconnaît la marque d'appel et lit le nom de
l'outil et ses arguments. Il vérifie qu'ils sont valides, puis exécute la fonction
correspondante, ici une requête dans la base de données de la librairie. C'est lui,
et non le modèle, qui agit sur le monde.

**4. Le résultat est ajouté au texte, et le modèle est appelé de nouveau.** Le
harnais ajoute au texte une nouvelle partie, marquée comme venant de l'outil,
puis rouvre une réplique de l'assistant :

```
<|début|>outil
{"titre": "Kamouraska", "auteur": "Anne Hébert", "format": "poche", "prix": 14.95, "en stock": 3}
<|fin|>
<|début|>assistant
```

Le modèle relit
[tout le texte](#une-conversation-qui-nen-est-pas-une),
y compris le résultat, et écrit cette fois sa réponse : « Oui, nous l'avons en format
poche, à 14,95 \\$, et il nous en reste trois exemplaires. »

{{< image src="/images/module4/appel-outil.svg" alt="Un diagramme en trois colonnes : le modèle, le harnais et l'outil, avec le temps qui s'écoule vers le bas. 1, le harnais envoie au modèle le texte assemblé : la requête système avec la description des outils, la question « Combien coûte Kamouraska ? », et l'ouverture de la réplique de l'assistant. 2, le modèle prédit des jetons qui forment un appel : chercher_catalogue, avec le titre Kamouraska, puis s'arrête à la marque de fin. 3, le harnais vérifie l'appel. 4, il interroge le catalogue. 5, l'outil répond : format poche, 14,95 $, trois en stock. 6, le harnais ajoute ce résultat au texte et rouvre une réplique de l'assistant. 7, il rappelle le modèle avec tout le texte. 8, le modèle écrit la réponse : « Oui, nous l'avons en format poche, à 14,95 $. » 9, le harnais l'affiche à l'utilisateur. À côté des étapes 1 et 7, le texte envoyé au modèle est dessiné comme une barre de segments, plus longue la seconde fois." title="Un appel d'outil, pas à pas. Le modèle passe deux fois : la première, il écrit l'appel ; la seconde, il lit le résultat et rédige sa réponse. Entre les deux, c'est le harnais qui agit." loading="lazy" >}}

**Qui fait quoi.** Un assistant qui utilise des outils réunit des composants de nature
très différente. Un seul est un modèle d'apprentissage automatique ; tous les autres
sont des programmes ordinaires, écrits par des humains, comme ceux du
[Module 1](docs/module1).

- **Le modèle** est un très grand ensemble de paramètres, des nombres appris à
  l'entraînement, que des serveurs équipés de
  [processeurs graphiques](docs/module3/42-materiel-et-outils/#les-processeurs-graphiques)
  font tourner, en général chez l'entreprise qui l'a entraîné. Il ne sait faire
  qu'une chose : recevoir un texte et produire la suite, jeton après jeton. Il n'a ni
  accès au réseau, ni accès aux fichiers, ni horloge, et rien ne lui reste d'un appel
  à l'autre. Il ne sait même pas quels outils existent vraiment, seulement ce que leur
  description en dit.
- **Le harnais**, présenté [plus haut](#la-requête-système-et-le-harnais), est un
  programme classique, écrit par exemple en Python ou en JavaScript. Le mot vient de l'équipement qui relie la force d'un cheval à la
  charrue : le modèle fournit la force, le harnais la dirige. C'est l'interface Web de
  ChatGPT, le robot conversationnel d'une banque, ou un assistant de programmation
  installé sur un ordinateur. Il tient la conversation, assemble le texte selon le
  gabarit, envoie ce texte au modèle par le réseau, et reçoit sa suite. Si cette suite
  contient un appel, il lit l'appel, le vérifie, exécute l'outil et rappelle le
  modèle. C'est aussi lui qui applique les règles : quels outils sont branchés,
  quelles actions demandent la confirmation de l'utilisateur, ce qui est interdit.
- **Les outils** sont, eux aussi, des programmes ordinaires : une requête dans une
  base de données, l'interface d'un moteur de recherche, un calcul, l'envoi d'un
  courriel. Ils font exactement ce pour quoi ils ont été programmés, avec la fiabilité
  d'un programme classique. Un outil puissant, comme l'exécution de code, tourne
  souvent dans un **bac à sable** (*sandbox*), un environnement isolé d'où le code ne
  peut pas atteindre le reste de la machine.

Ces composants ne tournent pas forcément au même endroit. Le modèle tourne chez son
fournisseur. Pour la librairie, le harnais et le catalogue tournent sur les serveurs
de la librairie : le fournisseur du modèle ne voit que le texte qu'on lui envoie, et
n'a jamais accès à la base de données. Dans ChatGPT, l'interpréteur de code tourne
chez OpenAI, dans un bac à sable. Un assistant de programmation, lui, exécute ses
commandes sur l'ordinateur même de l'utilisateur.

{{< image src="/images/module4/modele-harnais-outils.svg" alt="Trois zones côte à côte, séparées par des frontières en pointillés. À gauche, chez le fournisseur du modèle : le modèle, des milliards de paramètres sur des processeurs graphiques ; il sait prolonger un texte, mais n'a ni réseau, ni fichiers, ni horloge, et rien ne lui reste d'un appel à l'autre. Au milieu, chez l'entreprise qui offre l'assistant, ou sur l'ordinateur de l'utilisateur : le harnais, un programme classique, relié à l'utilisateur ; il tient la conversation, assemble le texte, lit et vérifie les appels, exécute les outils, applique les permissions, demande des confirmations et affiche la réponse. Le harnais envoie le texte au modèle et reçoit sa suite, parfois un appel. À droite, le monde : les outils, des programmes ordinaires, comme une base de données, une recherche sur le Web, une messagerie et un bac à sable pour exécuter du code. Le harnais les exécute et reçoit leurs résultats. En bas : le modèle propose, le harnais dispose." title="Le modèle, le harnais et les outils. Seul le modèle a été appris ; le harnais et les outils sont des programmes classiques, et c'est le harnais qui décide de ce que l'assistant peut faire." loading="lazy" >}}

Il en découle un principe simple : **le modèle propose, le harnais dispose**. Ce qu'un
assistant peut faire dans le monde ne dépend pas du modèle, mais des outils que son
harnais lui branche et des permissions qu'il lui accorde. Le même modèle est
inoffensif sans outils, et peut devenir dangereux si son harnais lui donne accès à une
messagerie ou à un compte bancaire sans demander de confirmation.

**Pourquoi le modèle « décide » d'appeler un outil.** Il n'y a pas de module de
décision séparé. L'appel est une suite de jetons comme une autre, et il est écrit quand
il est la suite la plus probable. Le modèle l'a appris au
[post-entraînement](docs/module4/70-du-modele-a-l-assistant/#un-modèle-de-base-ne-répond-pas),
sur des milliers de conversations où un outil est décrit et utilisé à bon escient. À la
question « Quel temps fait-il à Québec ? », avec un outil météo décrit dans le
contexte, la marque d'appel devient très probable. À la demande « Écris-moi un poème
sur l'hiver », elle ne l'est pas. En février 2023, une équipe de Meta montre avec
Toolformer qu'un modèle peut même apprendre seul quand appeler un outil. Il insère des
appels dans des textes, puis ne garde, pour s'entraîner, que ceux dont le résultat
l'aide à mieux prédire la suite du texte.

**Ce qui peut mal tourner.** Puisque l'appel est prédit, il peut être mal formé,
appeler un outil qui n'existe pas, ou inventer un argument. Le harnais doit donc
tout vérifier. Il peut aussi contraindre la génération : à chaque jeton, elle
n'autorise que ceux qui respectent le format de l'appel. Et puisque c'est
le harnais qui exécute, c'est lui qui décide de ce qui est permis, par exemple en
demandant la confirmation de l'utilisateur avant d'envoyer un courriel.

**Plusieurs outils, plusieurs appels.** Dans une même réponse, le modèle peut appeler
plusieurs outils, l'un après l'autre ou en même temps. Chaque résultat s'ajoute au
texte avant l'étape suivante. Il peut chercher le livre, puis appeler une calculatrice
pour le prix de trente exemplaires avec les taxes, puis rédiger sa réponse. Cette
boucle est le cœur des [agents](#des-agents-un-modèle-et-son-harnais-en-boucle), présentés plus bas.

Les outils compensent les faiblesses du modèle. Une calculatrice ou un programme
exécuté donne un résultat exact. Une recherche sur le Web donne une information à
jour. Une base de données donne des faits précis et vérifiables. Un outil de lecture
de fichiers donne accès aux documents de l'utilisateur. Un outil peut même être un
autre modèle, par exemple un générateur d'images. Les principaux assistants offrent
l'appel d'outils depuis 2023.

Chaque harnais devait d'abord décrire et brancher ses outils à sa manière. En
novembre 2024, Anthropic propose une norme ouverte, le *Model Context Protocol* (MCP),
à la façon d'une prise universelle. Un **serveur MCP** présente un ensemble d'outils,
comme un agenda, une messagerie ou une base de données, avec leurs descriptions. Tout
assistant compatible peut s'y brancher, lire ces descriptions et les placer dans son
contexte. OpenAI et Google adoptent la norme au printemps 2025.

## Des agents : un modèle et son harnais, en boucle

Un **agent** est un système qui enchaîne lui-même plusieurs étapes pour accomplir une
tâche : il raisonne, choisit un outil, observe le résultat, puis décide de l'étape
suivante, jusqu'à ce que la tâche soit terminée. Ce schéma, raisonner, agir, observer,
a été décrit en 2022 sous le nom de ReAct. Le mot *agent* reprend celui de
l'[apprentissage par renforcement](docs/module2/80-trois-facons-d-apprendre/#apprendre-par-lexpérience-le-renforcement)
du Module 2 : une entité qui agit dans un environnement et observe les conséquences
de ses actions. Le modèle, lui, ne fait toujours que prédire des jetons. C'est le harnais qui fait
tourner la boucle : il rappelle le modèle tant que celui-ci demande des outils, et
s'arrête quand il donne sa réponse finale.

{{< image src="/images/module4/agent.svg" alt="À gauche, une tâche donnée par l'utilisateur : trouver trois articles récents sur ARC et les résumer. Elle entre dans l'agent, dessiné comme un grand cadre. Au centre de l'agent, un grand modèle de langage. Autour de lui, une boucle en trois temps : raisonner, agir, observer. Pour agir, le modèle appelle un outil, à droite : recherche Web, exécution de code, documents et fichiers, courriel et agenda, mémoire. Le résultat de l'outil revient, et le modèle l'observe avant de raisonner de nouveau. En bas de l'agent, le contexte s'allonge à chaque tour : la tâche, un raisonnement, une action, un résultat, un autre raisonnement, et ainsi de suite. Quand le modèle juge la tâche terminée, il sort de la boucle et donne sa réponse finale, à gauche." title="Le principe d'un agent. Le modèle de langage ne change pas : c'est la boucle, les outils et le contexte qui s'allonge qui en font un agent." loading="lazy" >}}

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

- **Les agents de programmation**, comme Claude Code ou Codex, lisent le code d'un
  projet, le modifient, exécutent les tests et corrigent leurs erreurs. Le chapitre
  « [Programmer avec des agents](docs/module4/85-programmer-avec-des-agents) » leur est consacré.
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

Le [chapitre suivant](docs/module4/85-programmer-avec-des-agents) présente
l'application la plus aboutie de ces idées : les agents de programmation.
