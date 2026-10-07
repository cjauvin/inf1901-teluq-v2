---
title: "Des règles aux probabilités"
weight: 40
slug: des-regles-aux-probabilites
---

# Des règles aux probabilités

Les grands modèles de langage semblent apparus d'un coup, en 2022. Ils sont pourtant
l'aboutissement de soixante-dix ans de recherche en **traitement automatique de la
langue** (*natural language processing*, NLP), le domaine qui cherche à faire lire,
écrire, traduire ou transcrire la langue humaine par une machine. Cette recherche a
connu trois grandes approches : écrire des **règles**, compter des **statistiques**
dans de grandes collections de textes, puis entraîner des **réseaux de neurones**.

Ce chapitre et le suivant présentent les deux premières. Les chapitres
« [Des mots aux nombres](docs/module4/45-des-mots-aux-nombres) » et
« [Prédire le mot suivant](docs/module4/50-predire-le-mot-suivant) » présentent la
troisième. Plusieurs idées nées bien avant les réseaux de neurones sont encore au
cœur des LLM : le modèle de langage lui-même, la façon de le mesurer, et l'idée de
produire la suite la plus probable d'un texte.

{{< image src="/images/module4/frise-langage.svg" alt="Une frise chronologique verticale, de 1913 à 2022, avec trois ères qui se chevauchent, marquées par des bandes de couleur : les règles, d'environ 1950 à 1990 ; les statistiques, d'environ 1975 à 2014 ; les réseaux de neurones, depuis 2003. Les jalons : 1913, Markov compte les lettres d'Eugène Onéguine ; 1948, Shannon et le modèle de langage ; 1954, l'expérience Georgetown-IBM ; 1957, les grammaires de Chomsky ; 1966, le rapport ALPAC et ELIZA ; 1970, SHRDLU ; 1972, TF-IDF ; 1977, TAUM-MÉTÉO ; 1980, les HMM en reconnaissance vocale ; 1990, la traduction statistique d'IBM et la LSA ; 1993, le Penn Treebank ; 1995, le lissage de Kneser-Ney ; 2001, les CRF ; 2003, le modèle de langage neuronal ; 2006, Google Traduction statistique ; 2013, word2vec ; 2014, la traduction de séquence à séquence ; 2016, Google Traduction neuronal ; 2017, le Transformer ; 2018, BERT et GPT ; 2020, GPT-3 ; 2022, ChatGPT." title="Les trois ères du traitement de la langue. Les jalons sont présentés dans ce chapitre, le suivant et « Prédire le mot suivant »." loading="lazy" >}}

## Les règles (1954-1980)

Le 7 janvier 1954, à New York, IBM et l'Université de Georgetown présentent une
machine qui traduit du russe vers l'anglais. L'ordinateur IBM 701 traduit une
soixantaine de phrases choisies avec soin, à l'aide d'un vocabulaire de 250 mots et
de six règles de grammaire. La démonstration fait les manchettes, et ses
organisateurs prédisent que la traduction automatique sera au point d'ici trois à
cinq ans. C'est la guerre froide, et traduire automatiquement les publications
scientifiques soviétiques intéresse beaucoup le gouvernement américain.

En 1957, le linguiste Noam Chomsky publie *Structures syntaxiques* (*Syntactic
Structures*). Il y décrit une langue par une **grammaire générative** : un petit
ensemble de règles capable de produire toutes les phrases correctes de la langue, et
seulement celles-là. Il y conteste aussi l'idée de décrire la langue par des
probabilités, avec un exemple resté célèbre : « *Colorless green ideas sleep
furiously* » (« D'incolores idées vertes dorment furieusement »). La phrase n'a pas
de sens, mais elle est grammaticale, alors que les mêmes mots à l'envers,
« *Furiously sleep ideas green colorless* », ne le sont pas. Or aucune des deux
phrases n'avait jamais été écrite. Pour un modèle qui ne fait que compter les suites
de mots déjà vues, elles seraient donc toutes deux impossibles, au même titre.
L'argument pèse lourd. Pendant une vingtaine d'années, l'approche dominante consiste
à écrire des règles à la main : des dictionnaires, des grammaires, des règles pour
passer d'une langue à l'autre. Nous verrons [plus bas](#les-suites-jamais-vues-le-lissage)
comment les statistiques ont fini par répondre à Chomsky.

Les résultats déçoivent. En 1966, un comité consultatif du gouvernement américain,
l'ALPAC (*Automatic Language Processing Advisory Committee*), conclut que la
traduction automatique est plus lente, moins exacte et deux fois plus chère qu'un
traducteur humain. Le financement s'effondre. C'est l'un des premiers revers de
l'IA, avant les [hivers](docs/module1/60-hivers) présentés au Module 1. La même
année, [ELIZA](docs/module1/30-chercher-raisonner/#lautre-visage-eliza-ou-lillusion-de-comprendre)
imite un psychothérapeute avec quelques règles de reformulation, et en 1970,
[SHRDLU](docs/module1/40-representer-le-monde/#shrdlu-ou-le-sommet-de-lambition)
converse en anglais sur un petit monde de blocs. Les deux impressionnent, mais
aucun ne sort de son domaine.

Les systèmes à règles réussissent pourtant quand le domaine est étroit. À
l'Université de Montréal, le groupe TAUM (Traduction automatique de l'Université de
Montréal) met au point **TAUM-MÉTÉO**, qui traduit de l'anglais vers le français les
bulletins météorologiques d'Environnement Canada. La langue des bulletins est
répétitive et prévisible (« nuageux avec éclaircies », « possibilité d'averses »).
Mis en service à la fin des années 1970, le système traduit les bulletins de tout
le pays pendant plus de vingt ans, jusqu'en 2001.

## Le tournant statistique

Dans les années 1970, une autre approche naît dans les laboratoires d'IBM, autour de
la reconnaissance de la parole. Plutôt que d'écrire des règles de phonétique et de
grammaire, l'équipe de Frederick Jelinek apprend des **probabilités** à partir de
grandes quantités de parole enregistrée et de texte. Les résultats sont tels qu'on
attribue à Jelinek une boutade restée célèbre : « Chaque fois que je renvoie un
linguiste, la performance du système augmente. » C'est le renversement présenté au
[Module 2](docs/module2) : plutôt que de dire à la machine comment faire, on lui
donne des exemples, et elle apprend.

Cette approche demande des **corpus**, c'est-à-dire de grandes collections de
textes. Le Brown Corpus, réuni à l'Université Brown dans les années 1960, rassemble
un million de mots d'anglais américain publiés en 1961. Le Penn Treebank (1993)
annote des millions de mots, surtout tirés d'articles du *Wall Street Journal*, avec
la catégorie grammaticale de chaque mot et la structure de chaque phrase. Pour la
traduction, IBM utilise un corpus canadien, le **Hansard**, le compte rendu des
débats du Parlement du Canada, publié dans les deux langues officielles. Ses millions
de phrases traduites par des professionnels deviennent, vers 1990, la matière
première de la traduction statistique, présentée au
[chapitre suivant](docs/module4/42-les-outils-statistiques).

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

## Les suites jamais vues : le lissage

Un modèle à n-grammes qui ne fait que compter donne une probabilité nulle à toute
suite qu'il n'a jamais vue. C'est grave, parce que la probabilité d'une phrase est le
produit des probabilités de ses mots : une seule suite inconnue rend la phrase
entière impossible. Or presque tout texte nouveau contient des suites de trois mots
jamais vues, même dans un corpus immense.

Le **lissage** (*smoothing*) retire un peu de probabilité aux suites observées pour
la redistribuer aux suites jamais vues. Plusieurs méthodes se sont succédé.

- **Ajouter un.** On fait comme si chaque suite possible avait été vue une fois de
  plus qu'en réalité. C'est la règle de Laplace, du XVIIIᵉ siècle. Elle est simple,
  mais elle donne beaucoup trop de probabilité aux suites inconnues.
- **Good et Turing.** Pendant la Seconde Guerre mondiale, à Bletchley Park, en
  [déchiffrant Enigma](docs/module1/10-turing/#le-moment), Alan Turing et son
  assistant I. J. Good mettent au point une façon d'estimer la probabilité de
  rencontrer un élément jamais vu : elle dépend du nombre d'éléments vus une seule
  fois. Si beaucoup de suites n'ont été vues qu'une fois, il en reste sans doute
  beaucoup à découvrir. Good publie la méthode en 1953.
- **Le repli** (*backoff*, Slava Katz, 1987). Quand le contexte de trois mots n'a
  jamais été vu, on se replie sur les deux derniers mots, puis sur le dernier.
  C'est ce que fait l'applet ci-dessus.
- **Kneser et Ney** (1995). Leur méthode tient compte de la variété des contextes
  dans lesquels un mot apparaît. « Francisco » est un mot fréquent, mais il ne suit
  presque jamais autre chose que « San ». Dans un contexte inconnu, il doit donc
  recevoir une probabilité faible. Cette méthode reste la meilleure jusqu'à
  l'arrivée des réseaux de neurones.

Le lissage permet aussi de répondre à Chomsky. En 2000, Fernando Pereira entraîne
un modèle lissé qui regroupe les mots en classes de mots semblables. Ce modèle juge
« *Colorless green ideas sleep furiously* » environ 200 000 fois plus probable que la
même phrase à l'envers. Un modèle statistique peut donc distinguer deux phrases
qu'il n'a jamais vues, à condition de généraliser au-delà des suites observées.
C'est précisément ce que feront les modèles neuronaux du chapitre
« [Prédire le mot suivant](docs/module4/50-predire-le-mot-suivant/#généraliser-les-modèles-neuronaux) ».

## Mesurer un modèle : la perplexité

Comment comparer deux modèles de langage ? On leur présente un texte qu'ils n'ont
jamais vu, et on mesure la probabilité que chacun donne aux mots qui viennent
vraiment. Un bon modèle leur donne une probabilité élevée.

La mesure habituelle est la **perplexité** (*perplexity*). Elle s'interprète
simplement : une perplexité de 150 signifie que le modèle est, en moyenne, aussi
incertain que s'il devait choisir chaque mot au hasard parmi 150 mots également
probables. Plus elle est basse, mieux le modèle prédit. Sur des articles de
journaux en anglais, un bon modèle à trigrammes lissé atteint une perplexité
d'environ 150. Les modèles neuronaux l'ont fait baisser par étapes, et les grands
modèles actuels descendent à quelques dizaines, ou moins, selon les textes et la
façon de les découper en [jetons](docs/module4/45-des-mots-aux-nombres/#découper-le-texte-les-jetons).

La perplexité n'appartient pas au passé. L'erreur que les grands modèles de langage
réduisent pendant leur entraînement est directement liée à leur perplexité : un LLM
qui progresse est un LLM dont la perplexité baisse.

{{% details "La perplexité en formule (optionnel)" %}}

Pour un texte de $N$ mots $w_1, \dots, w_N$, la perplexité d'un modèle est

$$\mathrm{PP} = P(w_1, \dots, w_N)^{-1/N} = \exp\Big(-\frac{1}{N} \sum_{i=1}^{N} \log P(w_i \mid w_1, \dots, w_{i-1})\Big).$$

La quantité dans l'exponentielle est la moyenne, sur tous les mots du texte, de
$-\log P$ du mot qui vient vraiment. C'est l'**entropie croisée** (*cross-entropy*),
l'erreur que minimise l'entraînement d'un modèle comme GPT. Si le modèle donnait à
chaque mot une probabilité de $1/150$, la perplexité vaudrait exactement 150.

{{% /details %}}

## La suite de l'histoire

Les n-grammes ne voient que deux ou trois mots, et ils ne savent rien du sens. Le
[chapitre suivant](docs/module4/42-les-outils-statistiques) présente les autres
outils de l'ère statistique, qui ont dominé le traitement de la langue jusqu'au
début des années 2010 : les modèles de Markov cachés, la traduction statistique, la
représentation des documents, et les modèles qui étiquettent les mots.
