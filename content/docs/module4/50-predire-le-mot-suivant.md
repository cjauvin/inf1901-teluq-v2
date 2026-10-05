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

Ce chapitre présente cette opération, de ses origines au début du XXᵉ siècle
jusqu'aux modèles actuels. Il s'appuie sur les jetons et les plongements présentés
au chapitre « [Des mots aux nombres](docs/module4/40-des-mots-aux-nombres) ».

## Un modèle de langage

Un **modèle de langage** (*language model*) est un modèle qui donne, pour un début
de texte, la probabilité de chaque mot qui pourrait venir ensuite. Après « Le chat
dort sur le », il donne une probabilité élevée à « canapé », « lit » ou « tapis »,
une probabilité faible à « toit », et une probabilité presque nulle à « démocratie ».
C'est une [distribution](docs/module4/10-generer/#une-distribution-et-tirer-dedans),
au sens du premier chapitre de ce module, et on peut y tirer des mots.

Les modèles de langage existaient bien avant ChatGPT. Ils servaient à choisir, parmi
plusieurs interprétations possibles, celle qui ressemble le plus à du vrai texte.

- En **reconnaissance de la parole**, « un verre d'eau » et « un vert d'eau » se
  prononcent de la même façon. Le modèle de langage sait que la première suite est
  beaucoup plus probable.
- En **traduction automatique**, il aide à choisir, parmi plusieurs traductions mot
  à mot, celle qui forme une phrase naturelle.
- Le **clavier prédictif** d'un téléphone propose les mots les plus probables après
  ceux qu'on vient de taper.

## Compter : les n-grammes

La façon la plus simple d'estimer ces probabilités est de compter. En 1913, le
mathématicien russe Andreï Markov analyse les 20 000 premières lettres du roman en
vers *Eugène Onéguine*, de Pouchkine. Il compte combien de fois une voyelle suit une
voyelle, ou une consonne, et montre que ces enchaînements obéissent à des
probabilités régulières. Ces suites où chaque élément dépend du précédent
s'appellent depuis des **chaînes de Markov**. En 1948, Claude Shannon, le fondateur
de la théorie de l'information, applique la même idée aux mots anglais. Il montre
que des mots tirés au hasard en tenant compte du mot précédent produisent des suites
qui ressemblent de plus en plus à de l'anglais.

On appelle **n-gramme** une suite de *n* mots consécutifs. Un modèle à n-grammes
prédit chaque mot d'après les *n* − 1 mots qui le précèdent, en comptant dans un
grand corpus de textes combien de fois chaque mot les a suivis. Le
[travail noté 4](docs/module4/99-travail-noté-4) construit un modèle à bigrammes
(*n* = 2) dans un tableur.

L'applet ci-dessous contient un modèle à n-grammes entraîné sur deux romans de Jules
Verne, *Le Tour du monde en quatre-vingts jours* et *Vingt mille lieues sous les
mers*. À droite, elle affiche le contexte utilisé et les mots suivants les plus
probables.

{{< applet src="/html/applets/ngrammes.html" height="469" >}}

Quelques manipulations à faire :

1. Avec des n-grammes de taille 1, cliquez sur « Générer 40 mots ». Le modèle tire
   chaque mot selon sa seule fréquence dans les romans, et le texte n'a aucun sens.
2. Passez à la taille 2 et recommencez. Les paires de mots deviennent correctes
   (« Le capitaine Nemo »), mais les phrases partent dans toutes les directions.
3. Passez aux tailles 3 et 4. Le texte devient plus fluide, mais les passages
   surlignés se multiplient. Ce sont des suites d'au moins huit mots recopiées telles
   quelles des romans. Avec trois mots de contexte, la plupart des contextes
   n'apparaissent qu'une fois dans le corpus, et le modèle ne peut que recopier ce
   qui les suivait.
4. Cliquez plusieurs fois sur « Mot suivant » et observez la colonne de droite. Quand
   le contexte n'a jamais été vu, le modèle se replie sur un contexte plus court.
5. Faites varier la température, présentée au
   [chapitre « Générer »](docs/module4/10-generer/#la-température).

L'applet montre la limite des n-grammes. Avec 20 000 mots de vocabulaire, il existe
8 000 milliards de suites possibles de trois mots, et même un corpus immense n'en
contient qu'une infime partie. Plus le contexte est long, plus il est rare, et plus
le modèle recopie au lieu de généraliser. C'est le
[sur-apprentissage](docs/module2/70-generaliser/#trop-coller-ou-trop-lisser-le-compromis-biais-variance)
(*overfitting*) présenté au Module 2. Surtout, un modèle à n-grammes ne sait rien de
la ressemblance entre les mots : avoir vu « le chat dort sur le canapé » ne l'aide
pas à prédire la suite de « le chien dort sur le ».

## Généraliser : les modèles neuronaux

En 2003, Yoshua Bengio et ses collègues, à l'Université de Montréal, publient un
article intitulé « A Neural Probabilistic Language Model ». Ils remplacent le
comptage par un réseau de neurones. Chaque mot y est représenté par un
[plongement](docs/module4/40-des-mots-aux-nombres/#les-plongements), appris en
même temps que le réseau, et le réseau prédit le mot suivant à partir des plongements
des mots précédents. Comme « chat » et « chien » reçoivent des plongements voisins,
ce que le modèle apprend sur l'un profite à l'autre. Le modèle peut ainsi donner une
probabilité raisonnable à des suites qu'il n'a jamais vues. C'est l'un des travaux
fondateurs de l'[école canadienne](docs/module3/40-apprentissage-profond/#2012-le-concours-imagenet)
de l'apprentissage profond.

Les [réseaux récurrents](docs/module3/60-reseaux-recurrents/#ce-que-les-réseaux-récurrents-ont-permis)
présentés au Module 3 ont ensuite permis de tenir compte d'un contexte plus long,
en résumant tout le texte déjà lu dans leur mémoire. Autour de 2015, les meilleurs
modèles de langage et de traduction sont des réseaux récurrents. Ils ont cependant
deux défauts : leur mémoire s'efface sur les longs textes, et ils lisent un mot après
l'autre, ce qui rend leur entraînement lent.

## GPT : un Transformer qui prédit le jeton suivant

En juin 2018, l'entreprise OpenAI publie GPT (*Generative Pre-trained Transformer*),
un modèle de langage construit avec le
[Transformer](docs/module3/70-attention-transformer/#le-transformer) présenté au
Module 3. Le principe reste le même que celui des n-grammes : prédire le jeton
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
de surface, sans représentation du monde. Le chapitre du [Module 4](docs/module4) sur
ce que les modèles de langage comprennent présente ce débat.

Un modèle entraîné seulement à prédire le jeton suivant n'est pas encore un
assistant. Si on lui écrit « Quelle est la capitale du Canada ? », il peut tout aussi
bien continuer par une autre question, comme dans une liste de questions d'examen.
Le passage de ce modèle à un assistant qui répond fait l'objet d'un chapitre
ultérieur du [Module 4](docs/module4). Le [chapitre suivant](docs/module4) montre
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
