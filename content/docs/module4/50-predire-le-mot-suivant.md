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
comptage par un réseau de neurones, avec une idée décisive : les
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

Les [réseaux récurrents](docs/module3/60-reseaux-recurrents/#ce-que-les-réseaux-récurrents-ont-permis)
présentés au Module 3 ont ensuite permis de tenir compte d'un contexte plus long,
en résumant tout le texte déjà lu dans leur mémoire. Autour de 2015, les meilleurs
modèles de langage et de traduction sont des réseaux récurrents. Ils ont cependant
deux défauts : leur mémoire s'efface sur les longs textes, et ils lisent un mot après
l'autre, ce qui rend leur entraînement lent.

## Trois façons d'assembler le Transformer

Le [Transformer](docs/module3/70-attention-transformer/#le-transformer) de 2017,
présenté au Module 3, est conçu pour la traduction. Il a deux colonnes : un encodeur
lit la phrase d'origine, et un décodeur écrit la traduction en consultant l'encodeur
par l'attention croisée. Les deux colonnes peuvent aussi servir séparément. Trois
familles de modèles en sont nées.

| Variante | Ce qu'on garde | Exemples | Pour quoi faire |
|---|---|---|---|
| encodeur et décodeur | les deux colonnes | le Transformer de 2017, T5 (Google, 2019) | transformer un texte en un autre : traduire, résumer |
| encodeur seul | la colonne de gauche ; chaque mot voit toute la phrase | BERT (Google, 2018) | comprendre un texte : le classer, y chercher, calculer des [plongements contextuels](docs/module4/45-des-mots-aux-nombres/#le-même-mot-plusieurs-sens) |
| décodeur seul | la colonne de droite, sans attention croisée | GPT (OpenAI, 2018) et les grands modèles de langue | générer du texte, jeton après jeton |

{{< image src="/images/module4/transformer-variantes.svg" alt="Trois silhouettes simplifiées du Transformer. Première : encodeur et décodeur, les deux colonnes reliées par l'attention croisée ; c'est le Transformer de 2017 et T5, pour traduire et résumer. Deuxième : encodeur seul, le décodeur est grisé ; l'encodeur donne un vecteur par mot ; c'est BERT, pour comprendre et classer. Troisième : décodeur seul, l'encodeur et l'attention croisée sont grisés ; le décodeur donne le mot suivant ; c'est GPT et les grands modèles de langue, pour générer du texte." title="Les mêmes pièces, assemblées de trois façons : on garde les deux colonnes, ou seulement l'une des deux." loading="lazy" >}}

C'est la troisième qui l'a emporté, et c'est elle que décrit la suite de cette page.
Un décodeur assez grand, entraîné à prédire le jeton suivant, apprend aussi à
traduire, à résumer et à classer.

## GPT : un Transformer qui prédit le jeton suivant

En juin 2018, l'entreprise OpenAI publie GPT (*Generative Pre-trained Transformer*),
un modèle de langage qui ne garde que le décodeur du Transformer. Le principe reste le même que celui des n-grammes : prédire le jeton
suivant. Ce qui change, c'est la façon de calculer la distribution.

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
pendant une conversation : à chaque réponse, toute la conversation précédente lui est
présentée de nouveau comme un texte à continuer.

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
de surface, sans représentation du monde. Le chapitre du [Module 4](docs/module4/94-comprendre-et-rater/#perroquets-ou-modèles-du-monde) sur
ce que les modèles de langage comprennent présente ce débat.

Un modèle entraîné seulement à prédire le jeton suivant n'est pas encore un
assistant. Si on lui écrit « Quelle est la capitale du Canada ? », il peut tout aussi
bien continuer par une autre question, comme dans une liste de questions d'examen.
Le passage de ce modèle à un assistant qui répond fait l'objet d'un chapitre
ultérieur du [Module 4](docs/module4/70-du-modele-a-l-assistant). Le [chapitre suivant](docs/module4/60-passer-a-l-echelle) montre
d'abord ce qui s'est passé quand on a rendu ces modèles beaucoup plus grands.

## Pour voir le mécanisme en détail

Les deux vidéos suivantes, du vulgarisateur Grant Sanderson (chaîne 3Blue1Brown),
présentent les grands modèles de langage, puis le Transformer qui les fait
fonctionner. La vidéo sur
l'attention de la même série est proposée au chapitre
« [L'attention et le Transformer](docs/module3/70-attention-transformer/#pour-voir-le-mécanisme-en-détail) »
du Module 3.

{{< youtube LPZh9BOjkQs >}}

{{< youtube wjZofJX0v4M >}}
