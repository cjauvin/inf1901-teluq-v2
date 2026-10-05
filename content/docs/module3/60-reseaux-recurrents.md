---
title: "Lire une séquence : les réseaux récurrents"
weight: 60
slug: reseaux-recurrents
---

# Lire une séquence : les réseaux récurrents

Une image a une taille fixe, et tous ses pixels sont disponibles en même temps.
Beaucoup de données n'ont pas cette forme. Une phrase, un enregistrement de parole,
un morceau de musique ou le tracé d'un stylo sur une tablette arrivent élément par
élément. Leur longueur varie, et l'ordre de leurs éléments compte. On appelle ces
données des **séquences**. Ce chapitre présente les réseaux conçus pour les
traiter, les **réseaux récurrents** (*recurrent neural networks*, RNN).

## Le problème des séquences

Un réseau ordinaire a un nombre fixe d'entrées. Pour lui donner une séquence, on
peut essayer deux solutions simples.

**Tout donner d'un coup.** On réserve une entrée par élément de la séquence. Mais
la longueur varie : une phrase compte trois mots, la suivante quarante. Et si l'on
se contente de compter les mots présents, sans tenir compte de leur place, « le
chien mord l'homme » et « l'homme mord le chien » deviennent identiques.

**Regarder une fenêtre.** On ne donne au réseau que les derniers éléments, par
exemple les cinq derniers mots. La taille est fixe et l'ordre est conservé. Mais
tout ce qui précède la fenêtre est oublié. Dans « Le livre que tu m'as prêté la
semaine dernière était… », il faut se souvenir de « livre » pour bien accorder la
suite.

Il faut donc un réseau capable de lire une séquence de n'importe quelle longueur,
dans l'ordre, en gardant une trace de ce qu'il a déjà lu.

Pour traiter des mots, il faut d'abord les convertir en nombres. Le chapitre
« [Des mots aux nombres](docs/module4/40-des-mots-aux-nombres) » du Module 4
expliquera comment. Les exemples de ce chapitre portent
sur des suites de bits, qui sont déjà des nombres.

## Une boucle : la mémoire

Un réseau récurrent lit la séquence un élément à la fois. À chaque étape, il reçoit
deux choses : l'élément courant, et son propre **état** (*hidden state*) à l'étape
précédente. Il calcule à partir d'elles un nouvel état, qu'il se transmet à l'étape
suivante. Cet état est une liste de nombres qui résume ce que le réseau a lu
jusque-là. C'est sa mémoire.

On représente souvent ce réseau avec une boucle, l'état sortant de la cellule pour
y revenir. Pour comprendre son fonctionnement, il est plus simple de le
**dérouler** (*unroll*) : on dessine une copie de la cellule par étape, chacune
passant son état à la suivante.

{{< image src="/images/module3/reseau-recurrent-deroule.svg" alt="Deux panneaux. À gauche, une cellule reçoit un élément de la séquence par en dessous, et son état sort par la droite pour revenir dans la cellule par une boucle. À droite, la même cellule déroulée sur cinq étapes : chaque copie reçoit un élément de la séquence, de x1 à x5, et passe son état à la copie suivante. Les cinq copies ont les mêmes poids." title="Un réseau récurrent, avec sa boucle, puis déroulé sur cinq étapes." loading="lazy" >}}

Toutes les copies sont la même cellule, avec les mêmes poids. Le réseau applique le
même calcul à chaque étape, quelle que soit la longueur de la séquence. C'est le
[partage des poids](docs/module3/50-reseaux-convolutifs/#ce-que-la-convolution-apporte) des réseaux convolutifs, appliqué dans le temps plutôt que dans
l'espace : le filtre glissait sur l'image, la cellule glisse sur la séquence.

## Un réseau récurrent à manipuler

Voici une tâche qui demande de la mémoire. On reçoit une suite de bits, comme
1 0 1 1 0, et il faut dire si elle contient un nombre **pair** ou **impair** de 1.
Cette question s'appelle la **parité**. Un réseau ordinaire avec une fenêtre ne
peut pas y répondre : un seul 1 hors de la fenêtre change la réponse.

Un réseau récurrent la résout avec un état très simple, qui répond à la question
« le nombre de 1 lus jusqu'ici est-il impair ? ». À chaque nouveau bit, l'état
change si le bit vaut 1, et reste le même s'il vaut 0. C'est exactement le XOR de
l'état et du nouveau bit. La cellule de ce réseau est donc le
[petit réseau du XOR](docs/module3/20-une-couche-cachee/#le-xor-résolu-avec-trois-neurones)
du chapitre « Une couche cachée », avec les mêmes poids, appliqué à chaque étape.

{{< applet src="/html/applets/parite.html" height="523" >}}

1. Avancez d'un pas à la fois et suivez l'état. Il passe près de 1 (en rouge)
   quand le nombre de 1 lus jusque-là est impair, et revient près de 0 (en bleu)
   quand il est pair.
2. Passez la souris sur une cellule pour voir le calcul de ses trois neurones.
3. Lisez toute la suite, puis cliquez sur le premier bit pour le changer. La
   réponse finale change aussi : l'information du premier bit a traversé toutes
   les étapes.

Dans cette applet, les poids sont choisis à la main. Un vrai réseau récurrent les
apprend, et son état compte des dizaines ou des centaines de nombres, qui ne
correspondent à aucune question aussi lisible que « impair jusqu'ici ? ».

## Entraîner un réseau récurrent, et ce qu'il oublie

Un réseau récurrent s'entraîne par
[rétropropagation](docs/module3/30-entrainer-un-reseau/#la-rétropropagation), sur sa version déroulée. L'erreur, mesurée à la fin de la
séquence, remonte les étapes une à une jusqu'à la première. On parle de
**rétropropagation à travers le temps** (*backpropagation through time*).

Une séquence de 100 éléments donne un réseau déroulé de 100 étapes, donc un réseau
très profond. On retrouve alors
l'[évanouissement du gradient](docs/module3/40-apprentissage-profond/#pourquoi-seulement-en-2012) : l'erreur s'affaiblit à chaque étape qu'elle remonte. Les
premiers éléments de la séquence ont de moins en moins d'influence sur
l'apprentissage, et le réseau peine à apprendre les liens entre des éléments
éloignés.

{{< image src="/images/module3/influence-sequence.svg" alt="Un diagramme à barres pour une séquence de douze éléments. La barre du dernier élément, à droite, est la plus haute. Les barres diminuent vers la gauche, et celles des premiers éléments de la séquence sont presque nulles." title="Dans un réseau récurrent simple, l'influence d'un élément sur l'apprentissage diminue avec sa distance à la fin de la séquence." loading="lazy" >}}

Le langage contient beaucoup de liens de ce type. Dans « Les clés que j'avais
posées hier soir sur la table près de la fenêtre **sont** introuvables », le verbe
s'accorde avec « clés », placé une douzaine de mots plus tôt. Un réseau récurrent simple se
souvient bien des derniers mots, et mal des premiers.

## Le LSTM : une mémoire à portes

En 1997, Sepp Hochreiter et Jürgen Schmidhuber, à Munich, proposent une cellule
récurrente conçue pour ne pas oublier : la **mémoire à long et court terme**, ou
**LSTM** (*long short-term memory*).

La cellule LSTM contient une **mémoire** (*cell state*) séparée de son état, une
liste de nombres qui passe d'une étape à la suivante presque sans transformation. À
chaque étape, trois **portes** (*gates*) décident de ce qui arrive à cette mémoire :

- la **porte d'oubli** (*forget gate*) décide ce qu'il faut effacer ;
- la **porte d'entrée** (*input gate*) décide ce qu'il faut y écrire à partir de
  l'élément courant ;
- la **porte de sortie** (*output gate*) décide ce qu'il faut en lire pour produire
  l'état.

Chaque porte est un petit groupe de neurones, dont la sortie, entre 0 et 1, agit
comme un robinet : 0 bloque l'information, 1 la laisse passer. Les portes ont leurs
propres poids, appris par rétropropagation comme les autres. Le réseau apprend donc
lui-même quand retenir et quand oublier. Dans la phrase des clés, il peut apprendre
à écrire « sujet au pluriel » dans sa mémoire en lisant « Les clés », à le garder
pendant les mots suivants, puis à le lire au moment du verbe.

{{< image src="/images/module3/cellule-lstm.svg" alt="Une ligne horizontale, la mémoire, traverse la cellule de gauche à droite. Trois portes agissent sur elle : la porte d'oubli efface une partie de la mémoire, la porte d'entrée y écrit, la porte de sortie y lit pour produire le nouvel état. L'état précédent et l'élément courant arrivent par le bas et alimentent les trois portes." title="Une cellule LSTM, simplifiée : une mémoire qui traverse la cellule, et trois portes qui décident ce qu'on y efface, écrit et lit." loading="lazy" >}}

Comme la mémoire passe d'une étape à l'autre sans être recalculée, l'erreur peut
aussi la remonter sans s'affaiblir autant. Un LSTM apprend des liens sur des
centaines d'étapes, là où un réseau récurrent simple se limite à une dizaine.

{{% hint info %}}
**Des réseaux avec une mémoire externe**

En 2014, Alex Graves et ses collègues de DeepMind vont plus loin. Ils donnent à un
réseau récurrent une **mémoire externe**, une sorte de tableau où il peut écrire et
lire à n'importe quelle case. Ils l'appellent **machine de Turing neuronale**
(*neural Turing machine*), en référence au ruban de la
[machine de Turing](docs/module1/10-turing/#la-pensée-comme-calcul) du Module 1.
Le réseau apprend ainsi, à partir d'exemples, de petits algorithmes comme copier ou
trier une liste. L'idée est restée un sujet de recherche, mais le mécanisme qui
choisit où lire dans la mémoire annonce celui du chapitre suivant.
{{% /hint %}}

## Ce que les réseaux récurrents ont permis

Entre 2009 et 2017, les réseaux récurrents, et surtout les LSTM, deviennent la
méthode de référence pour les séquences.

**L'écriture manuscrite.** En 2009, un LSTM conçu par Alex Graves remporte des
concours de reconnaissance d'écriture manuscrite (*handwriting recognition*). Il lit
l'écriture comme une séquence, sans découper les mots en lettres à l'avance. Le fil
des chiffres manuscrits de ce module se prolonge ainsi des chiffres isolés à
l'écriture courante.

**La parole.** Un enregistrement de parole est une séquence de sons. En 2015,
Google adopte les LSTM pour la reconnaissance vocale (*speech recognition*) de ses
téléphones, et son taux d'erreur baisse nettement.

**La traduction.** En 2014, Ilya Sutskever, Oriol Vinyals et Quoc Le, chez Google,
proposent l'architecture **encodeur-décodeur** (*encoder-decoder*) pour la
traduction. Un premier réseau récurrent, l'encodeur, lit la phrase à traduire et la
résume dans son état final. Un second réseau récurrent, le décodeur, part de cet
état et écrit la traduction mot par mot. On retrouve l'idée de
l'[autoencodeur](docs/module3/40-apprentissage-profond/#apprendre-sans-étiquettes-lautoencodeur) : une représentation compacte au milieu, entre un encodeur et un
décodeur. En novembre 2016, Google Traduction adopte cette méthode. Selon le *New
York Times*, le gain obtenu d'un seul coup équivaut à peu près à tous les progrès
accumulés par l'ancien système depuis son lancement, une dizaine d'années plus tôt.

{{< image src="/images/module3/encodeur-decodeur.svg" alt="À gauche, l'encodeur, un réseau récurrent, lit les mots « le », « chat » et « dort » un à un. Son état final, au centre, résume la phrase. À droite, le décodeur, un second réseau récurrent, part de ce résumé et écrit « the », « cat » et « sleeps » un à un." title="L'architecture encodeur-décodeur : un réseau lit la phrase, un autre écrit la traduction à partir de son résumé." loading="lazy" >}}

## Les limites

Les réseaux récurrents ont trois limites, qui motivent le chapitre suivant.

**Le goulot** (*bottleneck*). Dans l'encodeur-décodeur, toute la phrase d'origine
est résumée en un seul état, de taille fixe, qu'elle compte cinq mots ou cinquante.
Plus la phrase est longue, plus la traduction se dégrade.

**La lenteur.** Un réseau récurrent ne peut calculer l'étape 10 qu'après l'étape 9.
Le calcul est séquentiel par nature, et ne profite donc pas des milliers de cœurs
d'un [GPU](docs/module3/42-materiel-et-outils/#les-processeurs-graphiques), qui
exigent des calculs simultanés. Cette limite devient décisive quand on veut
entraîner sur des milliards de mots.

**La mémoire lointaine.** Le LSTM a repoussé la limite de l'oubli, sans la
supprimer.

En 2014, à Montréal, Dzmitry Bahdanau, Kyunghyun Cho et Yoshua Bengio s'attaquent
au premier problème. Ils permettent au décodeur, à chaque mot qu'il écrit, de
regarder directement tous les mots de la phrase d'origine, et de choisir ceux qui
comptent à ce moment. Ce mécanisme s'appelle l'**attention**. Trois ans plus tard,
une équipe de Google montre qu'on peut garder l'attention et supprimer la
récurrence. Le chapitre suivant, « [L'attention et le Transformer](docs/module3/70-attention-transformer) », présente ce
résultat.
