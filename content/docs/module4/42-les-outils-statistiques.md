---
title: "Les outils statistiques"
weight: 42
slug: les-outils-statistiques
---

# Les outils statistiques

Le chapitre « [Des règles aux probabilités](docs/module4/40-des-regles-aux-probabilites) »
a présenté le tournant statistique du traitement de la langue, et son premier outil,
le modèle de langage à n-grammes. Entre 1980 et 2012, d'autres outils statistiques
s'y ajoutent. Ils servent à étiqueter les mots, à transcrire la parole, à traduire,
à chercher des documents. Ce chapitre en présente quatre : les modèles de Markov
cachés, la traduction statistique, la représentation des documents, et les modèles
qui étiquettent les mots à partir de caractéristiques choisies à la main.

Chacun a été remplacé, autour de 2015, par des réseaux de neurones. Mais chacun a
laissé une idée que l'on retrouve dans les grands modèles de langage.

## Les modèles de Markov cachés

Un texte est une suite de mots, mais derrière cette suite se cache une structure
qu'on ne voit pas directement : le rôle grammatical de chaque mot. Dans « la petite
brise la glace », le premier « la » est un déterminant, et le second peut être un
déterminant ou un pronom. « Brise » peut être un nom ou un verbe. Retrouver ces
rôles s'appelle l'**étiquetage grammatical** (*part-of-speech tagging*), et c'est
souvent la première étape d'un système de traitement de la langue.

Un **modèle de Markov caché** (*hidden Markov model*, HMM) décrit cette situation.
Il suppose qu'une suite d'**états cachés**, ici les étiquettes grammaticales, se
déroule comme une [chaîne de Markov](docs/module4/40-des-regles-aux-probabilites/#compter-les-n-grammes) :
chaque étiquette dépend de la précédente. Chaque état caché produit, ou **émet**, un
mot visible. Le modèle tient donc deux tables de probabilités.

- Les **transitions** donnent la probabilité de passer d'une étiquette à une autre :
  après un déterminant, un nom est très probable, un verbe très improbable.
- Les **émissions** donnent la probabilité qu'une étiquette produise un mot donné :
  un nom peut être « brise », « glace », « porte », avec des probabilités
  différentes.

Les deux tables s'estiment en comptant dans un corpus annoté, comme le Penn
Treebank. On peut même les apprendre sans annotations, avec l'algorithme de
Baum-Welch, mis au point par Leonard Baum et ses collègues à la fin des années 1960.

{{< image src="/images/module4/hmm.svg" alt="Deux rangées. En haut, dans une bande marquée « caché », une suite d'étiquettes grammaticales : déterminant, nom, verbe, déterminant, nom, reliées par des flèches de transition, avec leur probabilité, par exemple 0,70 de passer d'un déterminant à un nom. En bas, dans une bande marquée « visible », les mots de la phrase « la petite brise la glace ». Chaque étiquette émet le mot placé sous elle, avec une probabilité d'émission, par exemple 0,005 pour qu'un nom soit le mot « petite »." title="Un modèle de Markov caché. La probabilité d'une lecture est le produit des transitions et des émissions le long de la phrase." loading="lazy" >}}

Pour étiqueter une phrase, il faut trouver la suite d'étiquettes la plus probable
compte tenu des mots observés. Le nombre de suites possibles explose : avec sept
étiquettes, une phrase de vingt mots en admet près de 80 millions de milliards. En
1967, Andrew Viterbi, un ingénieur en télécommunications qui fondera plus tard
l'entreprise Qualcomm, publie un algorithme qui contourne cette explosion. Pour
chaque mot et chaque étiquette, l'**algorithme de Viterbi** ne garde que le
meilleur chemin qui y mène, puis prolonge ces chemins d'un mot à l'autre. Le travail
ne croît plus qu'en proportion de la longueur de la phrase.

L'applet ci-dessous contient un petit HMM pour le français. Ses probabilités ont été
fixées à la main, pour l'exemple. Chaque colonne correspond à un mot, chaque rangée
à une étiquette, et les cases vides sont les étiquettes impossibles pour ce mot. Le
trait vert est le chemin trouvé par l'algorithme de Viterbi.

{{< applet src="/html/applets/hmm.html" height="752" >}}

Quelques manipulations à faire :

1. Avec « la petite brise la glace », le modèle lit « la petite (fille) brise la
   glace ». Cliquez sur la case « nom » de *brise* pour imposer cette étiquette. Le
   modèle trouve alors l'autre lecture, « la petite brise (vent) la glace (gèle) »,
   et indique combien elle est moins probable.
2. Choisissez « les poules du couvent couvent ». Le même mot reçoit deux étiquettes
   différentes, selon le mot qui le précède.
3. Observez la liste des facteurs sous le treillis. La probabilité d'une lecture est
   le produit des transitions et des émissions, mot après mot.

Les HMM ont été l'outil central de la **reconnaissance de la parole** pendant
trente ans. Les états cachés y sont les sons de la langue, et les observations, des
mesures du signal sonore prises toutes les quelques millisecondes. Ils ont aussi
servi à repérer les gènes dans l'ADN. Ils ont été remplacés par des réseaux de
neurones au début des années 2010. L'idée d'un **état caché** qui résume ce qui
précède, elle, est restée : c'est la mémoire des
[réseaux récurrents](docs/module3/60-reseaux-recurrents/#une-boucle-la-mémoire) du
Module 3, devenue un vecteur de nombres plutôt qu'une étiquette.

## La traduction comme un canal bruité

En 1949, peu après les travaux de Shannon sur la communication, le mathématicien
Warren Weaver propose de voir un texte russe comme un texte anglais chiffré, qu'il
suffirait de déchiffrer. L'idée reste sans suite pendant quarante ans, puis l'équipe
d'IBM qui a réussi la reconnaissance de la parole l'applique à la traduction, vers
1990.

Elle repose sur le **canal bruité** (*noisy channel*). On imagine que la phrase
française qu'on veut traduire était, au départ, une phrase anglaise, déformée en
traversant un canal qui la « brouille ». Traduire, c'est retrouver la phrase
anglaise la plus probable. Selon la
[règle de Bayes](docs/module2/60-classer/#renverser-le-problème-la-classification-bayésienne)
du Module 2, cela revient à chercher la phrase anglaise *e* qui rend le plus grand le
produit de deux probabilités :

- *P*(*e*), donnée par un **modèle de langage** de l'anglais, qui juge si la phrase
  est de l'anglais naturel ;
- *P*(*f* | *e*), donnée par un **modèle de traduction**, qui juge si la phrase
  française *f* en est une traduction plausible.

{{< image src="/images/module4/canal-bruite.svg" alt="En haut, le canal bruité : une phrase anglaise, « the house is small », traverse un canal qui la brouille et en sort en français, « la maison est petite ». Seule la phrase française est observée. Au milieu, les mots des deux phrases sont reliés par l'alignement que le modèle apprend sur le Hansard : la et the, maison et house, est et is, petite et small. En bas, la traduction consiste à retrouver la phrase anglaise e qui rend le produit P(e) × P(f | e) le plus grand : P(e), un modèle de langage de l'anglais, juge si la phrase est de l'anglais naturel ; P(f | e), le modèle de traduction, juge si la phrase française en est une traduction plausible." title="La traduction statistique d'IBM : un modèle de langage, qui juge si la phrase est naturelle, et un modèle de traduction, appris sur le Hansard, qui juge si elle correspond au texte d'origine." loading="lazy" >}}

Le modèle de traduction s'apprend sur des textes déjà traduits, comme le Hansard
canadien présenté au chapitre précédent. Personne n'y indique quel mot traduit quel
mot. Le modèle le découvre seul, en remarquant que « maison » apparaît presque
toujours dans les phrases anglaises qui contiennent « house ». Ces correspondances
s'appellent l'**alignement** des mots. Les cinq « modèles IBM », publiés entre 1990
et 1993, apprennent des alignements de plus en plus fins, en tenant compte de l'ordre
des mots et des mots qui se traduisent par plusieurs.

À partir de 2003, la traduction par **segments** (*phrase-based*) aligne des groupes
de mots plutôt que des mots isolés. C'est la technique de Google Traduction, lancé
en 2006, et du logiciel libre Moses, publié en 2007. Ce sont ces systèmes que la
[traduction neuronale](docs/module4/50-predire-le-mot-suivant) remplace à partir de
2016.

Le canal bruité a laissé une idée durable : combiner un modèle de langage, qui
assure que le texte produit est naturel, avec une information sur ce qu'on veut
obtenir. C'est la [génération conditionnelle](docs/module4/20-quatre-facons-de-generer/#générer-sur-demande)
présentée au début de ce module. Un LLM qui traduit fait la même chose, mais en un
seul modèle : il prédit la suite du texte en tenant compte de la phrase à traduire.

## Représenter des documents

Pour classer des courriels, chercher des pages Web ou recommander des articles, il
faut représenter un document entier par des nombres. La solution la plus simple est
le [sac de mots](docs/module2/60-classer/#le-cas-des-pourriels) du Module 2 : on
compte combien de fois chaque mot apparaît dans le document, sans tenir compte de
l'ordre.

Tous les mots ne se valent pas. « Le » apparaît dans tous les documents et ne dit
rien de leur sujet. « Photosynthèse » est rare, et sa présence en dit beaucoup. En
1972, l'informaticienne britannique Karen Spärck Jones propose de pondérer chaque
mot par sa rareté dans l'ensemble des documents. La pondération **TF-IDF**
(*term frequency – inverse document frequency*) donne un poids élevé aux mots
fréquents dans un document mais rares ailleurs. Avec la représentation des documents
par des vecteurs, développée par Gerard Salton à l'Université Cornell, elle est au
cœur des moteurs de recherche pendant des décennies.

{{< image src="/images/module4/tfidf.svg" alt="Deux tableaux, des mots en rangées et trois documents en colonnes : botanique, biologie et sport. À gauche, le sac de mots, avec le nombre d'occurrences : le mot « le » apparaît 12, 10 et 15 fois, photosynthèse 3, 1 et 0 fois, chlorophylle 2, 0 et 0 fois, match 0, 0 et 4 fois, but 0, 0 et 3 fois. À droite, les poids TF-IDF : « le », présent dans les trois documents, reçoit un poids nul partout ; chlorophylle, match et but, propres à un seul document, reçoivent les poids les plus élevés. En bas, la formule : le poids d'un mot dans un document est son nombre d'occurrences multiplié par le logarithme du nombre de documents divisé par le nombre de documents qui contiennent le mot." title="Le sac de mots compte les occurrences ; TF-IDF les multiplie par la rareté du mot. Un mot présent dans tous les documents, comme « le », ne distingue plus rien et son poids s'annule." loading="lazy" >}}

En 1990, une équipe des laboratoires Bellcore pousse l'idée plus loin avec
l'**analyse sémantique latente** (*latent semantic analysis*, LSA). On construit
un immense tableau qui indique combien de fois chaque mot apparaît dans chaque
document, puis on le réduit à quelques centaines de dimensions, par une méthode
proche de la [PCA](docs/module2/80-trois-facons-d-apprendre/#réduire-la-dimension)
du Module 2. Chaque mot y reçoit un vecteur, et deux mots qui apparaissent dans des
documents semblables, entourés des mêmes autres mots, reçoivent des vecteurs voisins,
même s'ils n'apparaissent jamais dans le même document. C'est le cas de « médecin » et
« hôpital » dans la figure ci-dessous. Ce sont les premiers vecteurs de mots,
fondés sur la même idée que les [plongements](docs/module4/45-des-mots-aux-nombres/#on-reconnaît-un-mot-à-ses-fréquentations)
modernes : on reconnaît un mot à ses fréquentations. Le mot « latent » a d'ailleurs
le même sens que dans l'[espace latent](docs/module4/10-generer/#lespace-latent)
des générateurs d'images.

{{< image src="/images/module4/lsa.svg" alt="À gauche, un tableau de 12 mots sur 8 petits documents, avec une case colorée quand le mot apparaît dans le document. Les quatre premiers documents parlent de santé, les quatre derniers de sport. « Médecin » n'apparaît que dans les documents 1 et 2, « hôpital » que dans les documents 3 et 4 : jamais ensemble. Une flèche indique la réduction à deux dimensions. À droite, la carte obtenue : chaque mot est un point. Les mots de la santé se regroupent d'un côté, ceux du sport de l'autre, « blessure », présent dans les deux thèmes, entre les deux, et « médecin » et « hôpital » sont voisins." title="Une LSA calculée sur huit petits documents. Réduit à deux dimensions, le tableau mots × documents donne à chaque mot un vecteur. « Médecin » et « hôpital » deviennent voisins parce qu'ils fréquentent les mêmes mots, sans jamais se rencontrer." loading="lazy" >}}

## Étiqueter avec des caractéristiques faites à la main

Dans les années 1990 et 2000, la plupart des tâches du traitement de la langue sont
traitées par des modèles **discriminants**, au sens du chapitre
« [Classer](docs/module2/60-classer) » du Module 2 : la régression logistique, que
les linguistes appellent alors modèle à **entropie maximale** (*maximum entropy*,
1996), les machines à vecteurs de support, et les **champs aléatoires
conditionnels** (*conditional random fields*, CRF), présentés en 2001 par John
Lafferty, Andrew McCallum et Fernando Pereira. Les CRF étiquettent une suite de mots
comme un HMM, mais en tenant compte d'autant d'indices qu'on veut.

Ces indices, les **caractéristiques**, sont écrits à la main par des spécialistes.
Pour repérer les **entités nommées** (*named entities*), c'est-à-dire les noms de
personnes, de lieux et d'organisations, un système typique utilise des
caractéristiques comme « le mot commence par une majuscule », « le mot précédent
est *M.* », « le mot se termine par *-ville* », « le mot figure dans une liste de
villes ». Un bon système en compte des centaines de milliers. Ce sont les
[caractéristiques](docs/module2/30-les-donnees/#une-maison-cest-une-liste-de-nombres)
du Module 2, choisies à la main et multipliées à l'extrême.

Les systèmes complets enchaînent plusieurs de ces modèles : découper le texte en
mots, étiqueter leur rôle grammatical, analyser la structure de la phrase, repérer
les entités, puis répondre à la question posée. Chaque étape repose sur les
résultats de la précédente, et ses erreurs se propagent à toutes les suivantes. Le
système Watson d'IBM, qui gagne le jeu télévisé *Jeopardy!* en 2011, présenté au
[Module 1](docs/module1/60-hivers/#un-éclair-hybride-watson-2011), assemble ainsi
des centaines de composants de ce genre.

## Ce qui manquait

Au début des années 2010, les outils statistiques ont transformé le traitement de la
langue. La reconnaissance de la parole fonctionne au téléphone, la traduction
automatique est utilisée par des millions de personnes, les moteurs de recherche
trouvent ce qu'on cherche. Quatre limites demeurent pourtant.

- **Un contexte très court.** Un modèle à trigrammes ne voit que deux mots en
  arrière, un HMM ne retient que l'étiquette précédente.
- **Des mots sans ressemblance.** Pour un modèle à n-grammes, « chat » et « chien »
  sont deux symboles sans rapport. Ce qu'il apprend sur l'un ne profite pas à
  l'autre.
- **Des caractéristiques faites à la main**, différentes pour chaque tâche et
  chaque langue, qui demandent des années de travail.
- **Un modèle par tâche**, et des chaînes de traitement fragiles.

Les réseaux de neurones vont lever ces quatre limites, une à une. Le
[chapitre suivant](docs/module4/45-des-mots-aux-nombres) commence par la deuxième :
donner aux mots des représentations qui se ressemblent quand leurs sens se
ressemblent. Le chapitre
« [Prédire le mot suivant](docs/module4/50-predire-le-mot-suivant) » présente les
autres.
