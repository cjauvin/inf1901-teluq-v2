---
title: "Prédire le mot suivant"
weight: 50
slug: predire-le-mot-suivant
---

# Prédire le mot suivant

Le chapitre « [Quatre façons de générer](docs/module4/20-quatre-facons-de-generer/#un-élément-après-lautre-les-modèles-autorégressifs) »
a présenté la famille des modèles **autorégressifs**, qui génèrent une donnée un
élément après l'autre. Les grands modèles de langage en font partie. Tout ce qu'ils
font, répondre à une question, traduire, résumer, écrire un programme, repose sur
une seule opération, répétée des milliers de fois : prédire le jeton suivant d'un
texte.

Les chapitres « [Des règles aux probabilités](docs/module4/40-des-regles-aux-probabilites) »
et « [Les outils statistiques](docs/module4/42-les-outils-statistiques) » ont présenté
le modèle de langage et ses premières versions, fondées sur le comptage. Ce chapitre
présente la troisième ère, celle des réseaux de neurones, jusqu'aux modèles actuels.
Il s'appuie sur les jetons et les plongements présentés au chapitre
« [Des mots aux nombres](docs/module4/45-des-mots-aux-nombres) ».

## Généraliser : les modèles neuronaux

En 2003, Yoshua Bengio, Réjean Ducharme, Pascal Vincent et Christian Jauvin, à
l'Université de Montréal, publient un article intitulé « A Neural Probabilistic
Language Model » (Christian Jauvin est l'auteur de ce cours). Ils remplacent le
comptage par un réseau de neurones, avec une idée centrale : les
[plongements](docs/module4/45-des-mots-aux-nombres/#les-plongements) des mots ne
sont pas calculés d'avance, ils sont **appris** par le réseau, en même temps que
tout le reste.

Concrètement, le modèle contient une table qui associe à chaque mot du vocabulaire
une liste de quelques dizaines de nombres. Au départ, ces nombres sont tirés au
hasard. La table fait partie des **paramètres** du modèle, au même titre que les
poids de ses neurones. Le réseau lit les plongements des mots précédents et prédit
le mot suivant. À chaque erreur, la
[rétropropagation](docs/module3/30-entrainer-un-reseau/#la-rétropropagation) ajuste
les poids des neurones, mais aussi les nombres des plongements qui ont servi à la
prédiction. Il n'y a aucune étape séparée pour compter les voisins puis réduire un
tableau, comme dans la section
« [Compter les voisins](docs/module4/45-des-mots-aux-nombres/#compter-les-voisins) ».
Les plongements prennent simplement la forme qui aide le plus à prédire.

{{< image src="/images/module4/modele-neuronal-2003.svg" alt="Le contexte « chat dort sur » entre dans le modèle, dessiné comme un grand cadre. Dans le cadre, à gauche, la table des plongements : une rangée de nombres pour chaque mot du vocabulaire, aboie, canapé, chat, chien, dort, le, sur. Les rangées de chat, dort et sur sont surlignées. Leurs plongements sont mis bout à bout, puis passent dans une couche cachée de neurones, qui donne la probabilité de chaque mot suivant : le en tête, puis un, son et mon. Une flèche rouge, en bas, revient en sens inverse, de l'erreur jusqu'à la table : la rétropropagation ajuste les poids des neurones et aussi les plongements. Une étiquette sous le cadre indique que les paramètres du modèle sont la table des plongements et les poids des neurones, appris ensemble." title="Le modèle de langage neuronal de 2003. La table des plongements est à l'intérieur du modèle : comme les poids des neurones, elle part de valeurs tirées au hasard et s'ajuste à chaque erreur. Valeurs données à titre d'illustration." loading="lazy" >}}

Le résultat rejoint l'hypothèse distributionnelle. Comme « chat » et « chien »
apparaissent dans les mêmes contextes, la rétropropagation les pousse vers des
plongements voisins, et ce que le modèle apprend sur l'un profite à l'autre. Le
modèle peut ainsi donner une probabilité raisonnable à des suites qu'il n'a jamais
vues. C'est la généralisation que les n-grammes, même
[lissés](docs/module4/40-des-regles-aux-probabilites/#les-suites-jamais-vues-le-lissage),
ne pouvaient pas atteindre. Dix ans plus tard,
[word2vec](docs/module4/45-des-mots-aux-nombres/#les-plongements) reprend cette idée
en la simplifiant à l'extrême, pour l'appliquer à des milliards de mots. Aujourd'hui
encore, la table des plongements est la première couche de tout grand modèle de
langage : chaque jeton du vocabulaire y a son plongement, appris comme le reste.
C'est l'un des travaux fondateurs de
l'[école canadienne](docs/module3/40-apprentissage-profond/#2012-le-concours-imagenet)
de l'apprentissage profond.

{{< image src="/images/module4/plongements-rapprochent.svg" alt="Trois panneaux reliés par des flèches. 1, le corpus : le chat et le chien mangent, courent, jouent, sautent, boivent et grandissent ; seul le chat dort ; « le chien dort » n'a jamais été vu. Le camion et le tracteur partagent eux aussi six verbes. 2, une carte des plongements à deux dimensions : chaque mot part d'une position tirée au hasard, marquée par un cercle vide, et suit une flèche en pointillés jusqu'à sa position finale, marquée par un point plein. La distance entre chat et chien passe de 2,2 à 0,6 ; celle entre camion et tracteur, de 2,8 à 0,4 ; les deux paires restent éloignées l'une de l'autre. 3, la conséquence : la probabilité de « dort » après « le chat », une suite présente dans le corpus, vaut 8 % ; après « le chien », une suite jamais vue, 7 % ; après « le tracteur », 0 %. Un modèle à n-grammes donnerait 0 % à « le chien dort »." title="Une petite expérience réelle : un modèle du même type que celui de 2003, avec des plongements à deux dimensions, entraîné sur un corpus jouet où chat et chien partagent six verbes, et où seul le chat « dort ». Parce que les deux mots apparaissent dans les mêmes contextes, l'entraînement rapproche leurs plongements ; et parce que chien est placé près de chat, le modèle prête au chien ce qu'il a appris sur le chat." loading="lazy" >}}

## De 2003 à 2017 : des réseaux récurrents à l'attention

Le modèle de 2003 ne regardait qu'une courte fenêtre fixe de mots. En 2010, Tomáš
Mikolov, qui créera word2vec trois ans plus tard, remplace ce réseau par un
[réseau récurrent](docs/module3/60-reseaux-recurrents/#une-boucle-la-mémoire), présenté
au Module 3. Sa mémoire résume tout le texte déjà lu, sans limite fixe, et ses
modèles de langage font nettement mieux que les meilleurs n-grammes de l'époque.

En 2014, deux idées transforment la traduction automatique. Ilya Sutskever, Oriol
Vinyals et Quoc Le, chez Google, relient deux réseaux récurrents : le premier lit la
phrase d'origine, le second écrit la traduction, un mot après l'autre. C'est le
modèle **séquence à séquence** (*sequence-to-sequence*, ou *seq2seq*). La même année,
à Montréal, Dzmitry Bahdanau, Kyunghyun Cho et Yoshua Bengio lui ajoutent
l'[attention](docs/module3/70-attention-transformer/#lattention-dans-la-traduction) :
pour écrire chaque mot, le second réseau va chercher dans la phrase d'origine les
mots dont il a besoin. En 2016, Google Traduction adopte la traduction neuronale,
comme le raconte le chapitre
« [Les réseaux récurrents](docs/module3/60-reseaux-recurrents/#ce-que-les-réseaux-récurrents-ont-permis) ».

Ces réseaux ont cependant deux défauts : leur mémoire s'efface sur les longs textes,
et ils lisent un mot après l'autre, ce qui rend leur entraînement lent. En 2017, le
[Transformer](docs/module3/70-attention-transformer/#le-transformer) garde l'attention
et abandonne la récurrence : tous les mots d'un texte se regardent en même temps.

## Trois façons d'assembler le Transformer

Le [Transformer](docs/module3/70-attention-transformer/#le-transformer) de 2017,
présenté au Module 3, est conçu pour la traduction. Il a deux parties : un encodeur
lit la phrase d'origine, et un décodeur écrit la traduction en consultant l'encodeur
par l'attention croisée. Ces deux parties peuvent aussi servir séparément. Trois
familles de modèles en sont nées.

| Variante | Ce qu'on garde | Exemples | Pour quoi faire |
|---|---|---|---|
| encodeur et décodeur | les deux parties | le Transformer de 2017, T5 (Google, 2019) | transformer un texte en un autre : traduire, résumer |
| encodeur seul | l'encodeur ; chaque mot voit toute la phrase | BERT (Google, 2018) | comprendre un texte : le classer, y chercher, calculer des [plongements contextuels](docs/module4/45-des-mots-aux-nombres/#le-même-mot-plusieurs-sens) |
| décodeur seul | le décodeur, sans attention croisée | GPT (OpenAI, 2018) et les grands modèles de langage | générer du texte, jeton après jeton |

{{< image src="/images/module4/transformer-variantes.svg" alt="Trois silhouettes simplifiées du Transformer. Première : encodeur et décodeur, les deux colonnes reliées par l'attention croisée ; c'est le Transformer de 2017 et T5, pour traduire et résumer. Deuxième : encodeur seul, le décodeur est grisé ; l'encodeur donne un vecteur par mot ; c'est BERT, pour comprendre et classer. Troisième : décodeur seul, l'encodeur et l'attention croisée sont grisés ; le décodeur donne le mot suivant ; c'est GPT et les grands modèles de langage, pour générer du texte." title="Les mêmes pièces, assemblées de trois façons : on garde les deux colonnes, ou seulement l'une des deux." loading="lazy" >}}

C'est la troisième qui l'a emporté, et c'est elle que décrit la suite de cette page.
Un décodeur seul, dont l'[attention masquée](docs/module3/70-attention-transformer/#le-transformer)
ne laisse voir à chaque jeton que ceux qui le précèdent, est exactement un modèle de
langage : il prédit le jeton suivant. Assez grand, et entraîné seulement à cette
prédiction, il apprend aussi à traduire, à résumer et à classer. Trois raisons
l'expliquent.

- **Toute tâche peut s'écrire comme une suite de texte.** Traduire, c'est continuer
  « Traduis en anglais : La maison est petite. → ». Classer un avis, c'est continuer
  « Cet avis est-il positif ou négatif ? … Réponse : ». Un décodeur n'a pas besoin
  d'une architecture différente pour chaque tâche : il suffit de lui donner le bon
  début de texte.
- **Le Web regorge d'exemples de ces tâches.** On y trouve des pages bilingues, des
  articles suivis d'un résumé, des avis suivis d'une note, des questions suivies de
  leur réponse. Pour bien prédire la suite de ces textes, le modèle doit apprendre à
  faire ce qu'ils font. En 2019, les chercheurs d'OpenAI constatent ainsi que GPT-2
  produit un résumé si l'on termine un article par « TL;DR: », l'abréviation que les
  internautes placent avant un résumé.
- **Il n'a besoin d'aucune étiquette.** Un encodeur-décodeur s'entraîne sur des
  paires de textes, comme une phrase et sa traduction. Un encodeur comme BERT doit
  être ajusté sur des exemples annotés pour chaque tâche. Un décodeur s'entraîne
  sur n'importe quel texte, par
  [auto-supervision](docs/module2/80-trois-facons-d-apprendre/#fabriquer-soi-même-ses-réponses-lauto-supervision).
  Il peut donc profiter de tout le texte disponible, et grandir presque sans limite,
  comme le montre le chapitre
  « [Passer à l'échelle](docs/module4/60-passer-a-l-echelle/#des-lois-déchelle) ».

Plus le modèle grandit, mieux ces compétences se manifestent. En 2020, GPT-3
accomplit des tâches nouvelles à partir de quelques exemples donnés dans la
consigne, sans aucun entraînement supplémentaire : c'est
l'[apprentissage dans le contexte](docs/module4/60-passer-a-l-echelle/#apprendre-dans-le-contexte).
La section « [Ce que la prédiction exige](#ce-que-la-prédiction-exige) », plus bas,
revient sur ce que ce simple objectif oblige le modèle à apprendre.

## GPT : un Transformer qui prédit le jeton suivant

En juin 2018, l'entreprise OpenAI publie GPT (*Generative Pre-trained Transformer*),
qui ne garde que le décodeur du Transformer. C'est un
[modèle de langage](docs/module4/40-des-regles-aux-probabilites/#un-modèle-de-langage)
au sens exact du chapitre « Des règles aux probabilités » : il estime la même
probabilité que les n-grammes,

$$P(w_i \mid w_1, \dots, w_{i-1})$$

Mais là où un modèle à n-grammes ne gardait que les deux ou trois derniers mots, et
le modèle de 2003 une courte fenêtre fixe, GPT tient compte de tout le texte qu'il
peut lire d'un coup. Ce qui change, c'est la façon de calculer la distribution.

Le *P* de GPT désigne une idée qui s'impose cette année-là. En 2018, coup sur coup,
ULMFiT, ELMo, GPT et BERT montrent qu'on peut **préentraîner** un modèle une seule
fois, sur une grande quantité de texte et sans aucune étiquette, en lui faisant
prédire des mots, puis l'**ajuster** à peu de frais pour chaque tâche : classer des
avis, répondre à des questions, reconnaître des noms propres. C'est
l'[apprentissage par transfert](docs/module3/50-reseaux-convolutifs/#réutiliser-un-réseau-lapprentissage-par-transfert)
du Module 3, appliqué à la langue. Les modèles suivants iront plus loin : à partir de
GPT-2, un modèle assez grand accomplit beaucoup de tâches sans même être ajusté.

{{< image src="/images/module4/llm-jeton-apres-jeton.svg" alt="Un schéma en cinq étapes, de haut en bas. 1 : le texte « Le capitaine Nemo » est découpé en trois jetons. 2 : chaque jeton est remplacé par son plongement, une colonne de nombres. 3 : les plongements traversent les couches d'un Transformer, où chaque jeton ne peut regarder que les jetons qui le précèdent. 4 : à la sortie, le modèle donne une probabilité pour chacun des jetons du vocabulaire, par exemple 18 % pour « regarda », 11 % pour « sortit ». 5 : on tire un jeton, ici « regarda », on l'ajoute au texte, et on recommence avec le texte allongé." title="Comment un grand modèle de langage écrit : un jeton à la fois, en recommençant chaque fois avec le texte allongé." loading="lazy" >}}

1. Le texte est découpé en jetons, et chaque jeton est remplacé par son plongement.
2. Les plongements traversent les couches du Transformer. Dans chaque couche,
   l'[auto-attention](docs/module3/70-attention-transformer/#lauto-attention) permet
   à chaque jeton de consulter les jetons précédents et de modifier son vecteur en
   conséquence. Un jeton ne peut pas regarder les jetons qui le suivent : pendant
   l'entraînement, ce serait regarder la réponse.
3. À la sortie, le vecteur du dernier jeton est transformé en une probabilité pour
   chacun des jetons du vocabulaire, soit 200 000 nombres pour un modèle récent.
4. On tire un jeton dans cette distribution, avec la température choisie, on l'ajoute
   au texte, et on recommence. La génération s'arrête quand le modèle tire un jeton
   spécial qui marque la fin du texte.

L'entraînement suit le même principe. On présente au modèle des textes tirés d'un
immense corpus, et à chaque position, il doit prédire le jeton suivant. Son erreur
est d'autant plus grande qu'il a donné une faible probabilité au jeton qui suivait
vraiment. La rétropropagation ajuste ensuite ses milliards de poids pour réduire
cette erreur. C'est le principe du
[maximum de vraisemblance](docs/module2/60-classer/#sous-les-modèles-des-probabilités)
présenté au Module 2 : on cherche les paramètres qui rendent les textes observés les
plus probables. Comme le texte fournit lui-même toutes les réponses, aucun étiquetage
humain n'est nécessaire. C'est de
l'[auto-supervision](docs/module2/80-trois-facons-d-apprendre/#fabriquer-soi-même-ses-réponses-lauto-supervision),
et c'est ce qui permet d'entraîner ces modèles sur une grande partie du texte
disponible sur le Web. Contrairement à un réseau récurrent, le Transformer traite
toutes les positions d'un texte en même temps, ce qui permet d'utiliser pleinement les
[processeurs graphiques](docs/module3/42-materiel-et-outils/#les-processeurs-graphiques).

Le nombre de jetons que le modèle peut lire d'un coup s'appelle sa **fenêtre de
contexte** (*context window*). Elle était de 512 jetons pour le premier GPT, en 2018.
En 2024, Google présente Gemini 1.5, dont la fenêtre atteint un million de jetons,
soit plusieurs romans entiers. Cette fenêtre est aussi la seule mémoire du modèle
pendant une conversation, comme le montre la section
« [Une conversation qui n'en est pas une](docs/module4/80-outils-et-agents/#une-conversation-qui-nen-est-pas-une) »
du chapitre « Des outils, un harnais et des agents ».

## Ce que la prédiction exige

La tâche paraît modeste. On compare souvent ces modèles à la fonction de complétion
automatique d'un téléphone. La comparaison est juste pour le principe, mais elle
trompe sur ce que la tâche exige quand on cherche à la réussir très bien.

Pour prédire le mot suivant de « La capitale du Canada est », il faut connaître un
fait. Pour prédire la suite de « 17 × 24 = », il faut savoir calculer. Pour prédire
le nom du coupable à la dernière page d'un roman policier, il faudrait avoir suivi
l'intrigue et les indices. Plus un modèle devient bon à cette tâche, plus il doit,
d'une façon ou d'une autre, capter la grammaire, des connaissances sur le monde, des
styles d'écriture et des formes de raisonnement. Certains chercheurs, comme Ilya
Sutskever, cofondateur d'OpenAI, en concluent que bien prédire le texte demande une
forme de compréhension. D'autres estiment que le modèle n'apprend que des régularités
de surface, sans représentation du monde. Le chapitre
« [Ce que les LLM comprennent, et ce qu'ils ratent](docs/module4/94-comprendre-et-rater/#perroquets-ou-modèles-du-monde) »
présente ce débat.

Un modèle entraîné seulement à prédire le jeton suivant n'est pas encore un
assistant. Si on lui écrit « Quelle est la capitale du Canada ? », il peut tout aussi
bien continuer par une autre question, comme dans une liste de questions d'examen.
Le passage de ce modèle à un assistant qui répond fait l'objet du chapitre
« [Du modèle à l'assistant](docs/module4/70-du-modele-a-l-assistant) ». Le [chapitre suivant](docs/module4/60-passer-a-l-echelle) montre
d'abord ce qui s'est passé quand on a rendu ces modèles beaucoup plus grands.

## Ce qui a changé, ce qui est resté

Les chapitres « [Des règles aux probabilités](docs/module4/40-des-regles-aux-probabilites) »
et « [Les outils statistiques](docs/module4/42-les-outils-statistiques) » annonçaient
que les idées de l'ère statistique survivent dans les grands modèles de langage. Le
tableau suivant les met côte à côte.

| Notion classique | Ce qu'elle devient dans un grand modèle de langage |
|---|---|
| le [modèle de langage](docs/module4/40-des-regles-aux-probabilites/#un-modèle-de-langage), la probabilité du mot suivant | inchangé : c'est exactement ce qu'estime GPT |
| l'hypothèse de Markov : deux ou trois mots de contexte | la fenêtre de contexte : des milliers, voire des millions de jetons |
| le [lissage](docs/module4/40-des-regles-aux-probabilites/#les-suites-jamais-vues-le-lissage), pour les suites jamais vues | la généralisation par les plongements : des mots voisins partagent ce qu'on sait d'eux |
| la [perplexité](docs/module4/40-des-regles-aux-probabilites/#mesurer-un-modèle-la-perplexité) | la mesure d'erreur que l'entraînement fait baisser, l'entropie croisée (*cross-entropy*), dont elle est l'exponentielle |
| le [canal bruité](docs/module4/42-les-outils-statistiques/#la-traduction-comme-un-canal-bruité), où le modèle de langage arbitre | un seul modèle, qui écrit directement la traduction ou la réponse |
| les [vecteurs de documents](docs/module4/42-les-outils-statistiques/#représenter-des-documents) et la LSA | les plongements, appris plutôt que comptés |
| les [caractéristiques faites à la main](docs/module4/42-les-outils-statistiques/#étiqueter-avec-des-caractéristiques-faites-à-la-main) | les représentations que le réseau apprend lui-même |
| les chaînes de pièces : étiqueter, analyser, traduire, corriger | un seul modèle, entraîné de bout en bout |

Le but n'a donc pas changé depuis Shannon et Markov : estimer la probabilité de la
suite d'un texte. Ce qui a changé, c'est la façon de l'estimer, et l'échelle.

## Pour voir le mécanisme en détail

Les deux vidéos suivantes, du vulgarisateur Grant Sanderson (chaîne 3Blue1Brown),
présentent les grands modèles de langage, puis le Transformer qui les fait
fonctionner. La vidéo sur
l'attention de la même série est proposée au chapitre
« [L'attention et le Transformer](docs/module3/70-attention-transformer/#pour-voir-le-mécanisme-en-détail) »
du Module 3.

{{< youtube LPZh9BOjkQs >}}

{{< youtube wjZofJX0v4M >}}
