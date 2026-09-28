---
title: "Capturer l'expertise : les systèmes experts"
weight: 50
slug: systemes-experts
---

# Capturer l'expertise : les systèmes experts

## Rétrécir et codifier le monde pour réussir

Le chapitre « [Représenter le monde](docs/module1/40-representer-le-monde) » s'est
terminé sur un constat : on ne peut pas écrire le sens commun, parce qu'il n'a pas
de limite. Les chercheurs des années 1970 en tirent une conclusion pratique. Si le
savoir général est hors d'atteinte, il faut viser un savoir plus **étroit**.

L'idée est la suivante. Au lieu de chercher une intelligence générale, on choisit
**un seul domaine** bien délimité (diagnostiquer une infection, configurer un
ordinateur, prospecter un gisement minier) et on tente d'y reproduire la compétence
d'**un seul expert**. Dans un domaine spécialisé, le savoir-faire d'un expert
ressemble souvent à un grand ensemble de règles de la forme *si telles conditions,
alors telle conclusion*. Le médecin qui raisonne « *si* le patient a de la fièvre
**et** telle bactérie dans le sang, *alors* prescrire tel antibiotique » applique
une règle. Si on recueille assez de ces règles et qu'on les inscrit dans la
machine, celle-ci devrait raisonner comme l'expert, du moins dans ce domaine. C'est
le principe des **systèmes experts**, qu'on peut résumer par la formule suivante :
**connaissance = règles explicites**.

La démarche est la même que celle de SHRDLU, qui ne « comprenait » son monde de
blocs que parce que ce monde était très petit. Les systèmes experts réduisent eux
aussi le monde à un domaine restreint, mais il s'agit cette fois de domaines réels,
qui ont une valeur commerciale. Cette approche va fonctionner. L'IA symbolique va
sortir des universités, produire des revenus et convaincre le monde des affaires
que l'intelligence artificielle est utilisable. La [section
suivante](docs/module1/50-systemes-experts/#lanatomie-dun-système-expert) explique
comment une machine peut raisonner avec des règles.

## L'anatomie d'un système expert

Un système expert comporte **trois composantes**. La première est une **base de
règles**, qui contient la connaissance du domaine sous forme d'énoncés *si… alors…*.
La deuxième est une **base de faits** (ou « mémoire de travail »), qui rassemble ce
qu'on sait du cas traité, par exemple les symptômes d'un patient ou l'état d'une
voiture. La troisième est un **moteur d'inférence**, un mécanisme général qui
compare les faits aux règles, applique celles dont les conditions sont remplies et
en tire de nouveaux faits, jusqu'à une conclusion.

L'intérêt de cette architecture tient à la **séparation** entre ces composantes. Le
moteur d'inférence ne contient aucune connaissance de médecine, d'automobile ou de
minéralogie. Il se contente d'enchaîner des règles. Toute la compétence se trouve
dans la base de règles, qu'on peut remplacer comme une cartouche. Avec d'autres
règles, le même moteur devient un système de diagnostic médical, mécanique ou
géologique. Comme le savoir est séparé du raisonnement, on peut construire
plusieurs systèmes experts sans tout reprogrammer à chaque fois.

Prenons un exemple simple, **une voiture qui refuse de démarrer**. On donne au
système les règles suivantes :

> **R1** : *si* le moteur ne se lance pas du tout **et** les phares sont faibles,
> *alors* la batterie est déchargée.
>
> **R2** : *si* la batterie est déchargée, *alors* recharger ou remplacer la batterie.
>
> **R3** : *si* le moteur se lance normalement mais ne démarre pas **et** le réservoir
> est vide, *alors* refaire le plein.
>
> **R4** : *si* le moteur se lance normalement **et** le réservoir n'est pas vide,
> *alors* faire vérifier l'allumage.

On lui fournit aussi deux faits observés, *le moteur ne se lance pas* et *les phares
sont faibles*. Le moteur d'inférence parcourt alors les règles. Les deux conditions
de **R1** sont satisfaites, donc R1 se **déclenche** et ajoute un fait nouveau, *la
batterie est déchargée*. Ce fait satisfait la condition de **R2**, qui se déclenche
à son tour et donne la conclusion *recharger ou remplacer la batterie*. Les
conditions de R3 et de R4 ne sont pas remplies, et ces règles ne font rien. En deux
étapes, le système a établi un diagnostic à partir des symptômes. Il peut aussi
**retracer son raisonnement** : il conclut à la batterie à cause de R1, donc à cause
des phares faibles.

Ce mode de raisonnement, qui part des faits pour arriver à une conclusion, s'appelle
le **chaînage avant**. Il convient bien quand on dispose déjà de nombreux faits et
qu'on veut savoir ce qui en découle.

On peut aussi procéder dans l'autre sens. Supposons qu'on soupçonne la batterie et
qu'on veuille vérifier cette hypothèse. Le moteur d'inférence part alors de
l'**hypothèse**, traitée comme un but, et remonte les règles. Pour conclure
« recharger la batterie » (R2), il faut que la batterie soit déchargée. Pour cela
(R1), il faut que le moteur ne se lance pas **et** que les phares soient faibles.
Aucune règle ne produit ces deux derniers faits, qu'il faut donc **observer**. Le
système pose alors la question à l'utilisateur (« les phares sont-ils faibles ? »)
et n'examine que ce qui concerne l'hypothèse étudiée. C'est le **chaînage arrière**.

{{% hint info %}}
**Prolog, un langage fondé sur le chaînage arrière.** En 1972, on a fait de ce
principe (déclarer des faits et des règles *si… alors…*, puis laisser un moteur
général les enchaîner) un **langage de programmation**, **Prolog**. Le programmeur
n'y écrit que des faits et des règles, et le langage fournit lui-même le moteur
d'inférence, un chaînage arrière comme celui qu'on vient de décrire. On n'indique
pas au programme comment calculer, mais ce qui est vrai. Cette approche s'appelle la
**programmation logique**. Elle est différente de la programmation fonctionnelle du
langage Lisp (celui des machines de la photo [plus
bas](docs/module1/50-systemes-experts/#lâge-dor-mycin-xcon-et-le-boom)). Prolog a longtemps été le
langage de référence de l'IA symbolique en Europe. Le projet japonais de
**Cinquième Génération**, [présenté plus
bas](docs/module1/50-systemes-experts/#lâge-dor-mycin-xcon-et-le-boom), l'a choisi comme langage principal, et
ses principes se retrouvent aujourd'hui dans Datalog et dans les moteurs de règles.
{{% /hint %}}

{{% details "Pour aller plus loin : à quoi ressemble du Prolog ?" %}}
Reprenons l'exemple de la voiture. En Prolog, on écrit d'abord les **faits**
observés, puis les **règles**. Dans une règle, la conclusion est placée avant le
symbole `:-`, qui se lit « *si* », et les conditions sont séparées par des virgules,
qui se lisent « *et* » :

```prolog
% Les faits observés :
moteur_ne_se_lance_pas.
phares_faibles.

% Les règles R1 et R2, « si … alors … » :
batterie_dechargee   :- moteur_ne_se_lance_pas, phares_faibles.
recharger_batterie   :- batterie_dechargee.
```

On **interroge** ensuite le programme en lui soumettant un but à prouver (`?-` est
l'invite) :

```prolog
?- recharger_batterie.
true.
```

Pour répondre, Prolog effectue le chaînage arrière décrit plus haut. Pour établir
`recharger_batterie`, il lui faut `batterie_dechargee`. Pour établir
`batterie_dechargee`, il lui faut les deux faits `moteur_ne_se_lance_pas` et
`phares_faibles`, qui sont connus. Le but est donc atteint, et Prolog répond
`true`. Le programme n'indique nulle part comment mener cette recherche, puisque le
moteur du langage s'en charge.
{{% /details %}}

Une même base de règles peut donc être parcourue dans deux sens, **vers l'avant**, à
partir des faits, ou **vers l'arrière**, à partir d'un but. Le chaînage arrière est
mieux adapté au diagnostic, parce qu'il ne pose que les questions utiles à
l'hypothèse examinée, au lieu de demander toutes les mesures d'avance. C'est pour
cette raison que le plus connu des systèmes experts, le système de diagnostic
médical **MYCIN**, l'utilisait. Il est présenté dans la [section
suivante](docs/module1/50-systemes-experts/#lâge-dor-mycin-xcon-et-le-boom).

Dans l'applet ci-dessous, choisissez ce que vous observez sur la voiture, puis
faites avancer le moteur d'inférence règle par règle. Vous le verrez examiner
chaque règle, déclencher celles dont les conditions sont réunies et ajouter des
faits à la base, jusqu'au diagnostic. Essayez plusieurs combinaisons, et trouvez
celle pour laquelle le système ne peut rien conclure.

{{< applet src="/html/applets/moteur-inference.html" height="640" >}}

## L'âge d'or : MYCIN, XCON et le boom

Le premier système expert est généralement considéré comme étant **DENDRAL**,
développé à Stanford à partir de 1965. Il identifiait des **molécules** à partir de
données de spectrométrie, comme le ferait un chimiste expérimenté. Le plus connu
est cependant **MYCIN**, conçu au début des années 1970 par **Edward Shortliffe**.
MYCIN diagnostiquait les **infections bactériennes du sang** et recommandait un
antibiotique et une dose. Il comptait environ **600 règles** et utilisait le
**chaînage arrière** [décrit plus
haut](docs/module1/50-systemes-experts/#lanatomie-dun-système-expert). Il partait d'une hypothèse sur le germe en
cause et posait des questions au médecin jusqu'à sa conclusion. Grâce à ce même
mécanisme, il pouvait **justifier** sa démarche. Quand on lui demandait pourquoi il
posait une question, il indiquait la règle qu'il cherchait à vérifier.

En médecine, cependant, peu de choses sont certaines. Un symptôme peut suggérer un
germe sans le confirmer. MYCIN utilisait donc des **facteurs de certitude** (un
nombre associé à chaque règle, qui indique à quel point sa conclusion est fiable)
et les combinait au cours du raisonnement. Cette méthode était approximative. Plus
tard, une théorie plus rigoureuse de l'incertitude, celle des **réseaux
bayésiens**, l'a remplacée (voir le [Module
2](docs/module2/60-classer/#sous-les-modèles-des-probabilités)). MYCIN montrait
déjà qu'un système qui raisonne doit aussi tenir compte de l'incertitude.

{{% hint info %}}
**La logique floue.** Les règles d'un système expert emploient souvent des mots
imprécis : une fièvre « élevée », un moteur « chaud », une vitesse « faible ». En
logique classique, un énoncé est vrai ou faux. À partir de quel degré une fièvre
devient-elle « élevée » ? Fixer un seuil à 38,5 °C revient à dire que 38,4 °C n'est
pas une fièvre élevée du tout. En 1965, le mathématicien **Lotfi Zadeh** propose la
**logique floue** (*fuzzy logic*), où un énoncé peut être vrai à un certain degré,
entre 0 et 1. Une fièvre de 38,4 °C peut ainsi être « élevée » à 0,6, et une fièvre
de 40 °C à 1. Les règles *si… alors…* s'appliquent alors plus ou moins fortement
selon ce degré.

{{< image src="/images/module1/logique-floue.svg" alt="Deux graphiques du degré auquel une température est une « fièvre élevée », de 0 à 1. À gauche, en logique classique, une marche d'escalier : 0 sous 38,5 °C, 1 au-dessus ; 38,4 °C vaut 0. À droite, en logique floue, une rampe de 37,5 °C à 39 °C ; 38,4 °C vaut 0,6." title="« Fièvre élevée » : un seuil en logique classique, un degré en logique floue." loading="lazy" >}}

La logique floue ne traite pas le même problème que les facteurs de certitude de
MYCIN. Ceux-ci mesurent à quel point on est sûr d'une conclusion. La logique floue
mesure à quel point un mot s'applique à une situation. Elle a connu un grand succès
industriel, surtout au Japon à partir de la fin des années 1980, dans des systèmes
de commande : le métro de Sendai, des machines à laver, des autocuiseurs à riz, des
stabilisateurs de caméras. Elle est encore utilisée aujourd'hui en automatique.
{{% /hint %}}

MYCIN donnait de bons résultats. En 1979, une évaluation a soumis ses
recommandations à un jury d'experts, qui les a comparées à celles de médecins sans
savoir lesquelles venaient du programme. Le jury a jugé les recommandations de
MYCIN **aussi bonnes, voire meilleures**, que celles des spécialistes. Pourtant,
**MYCIN n'a jamais été utilisé pour soigner un patient.** Les obstacles étaient
humains et pratiques plutôt que scientifiques. On ne savait pas qui serait
**responsable** en cas d'erreur (le médecin, l'hôpital ou le programmeur). Il était
difficile de l'**intégrer** au travail clinique, à une époque où il n'y avait pas
d'ordinateur au chevet des patients et où tout devait être saisi sur un terminal.
Enfin, les médecins n'étaient pas prêts à **déléguer** leur jugement à un
programme. Le cas de MYCIN montre que les difficultés des systèmes experts
n'étaient pas seulement techniques.

L'industrie a adopté les systèmes experts plus facilement que la médecine. À la fin
des années 1970, le constructeur informatique **DEC** devait configurer sur mesure
chaque commande de ses ordinateurs **VAX**, ce qui impliquait d'assembler des
centaines de composants sans erreur ni oubli. Cette tâche a été confiée à un
système expert, **XCON**. XCON configurait les commandes plus rapidement et avec
moins d'erreurs que les employés, et il faisait **économiser des dizaines de
millions de dollars par an** à DEC. Ce succès a montré que les systèmes experts
pouvaient être rentables en dehors des laboratoires. Un problème est cependant
apparu : le nombre de règles de XCON augmentait sans cesse, jusqu'à plusieurs
milliers, et il fallait constamment les ajuster les unes aux autres. Nous y
reviendrons [plus bas](docs/module1/50-systemes-experts/#le-goulot-détranglement).

Après XCON, les investissements se sont multipliés. Au début des années 1980, l'IA
est devenue pour la première fois une **industrie**. On vendait des **coquilles**
(*shells*), c'est-à-dire des moteurs d'inférence vides, prêts à recevoir la base de
règles de n'importe quel domaine. Un nouveau métier est apparu, celui d'**ingénieur
de la connaissance**, chargé de recueillir le savoir des experts. Des entreprises
ont été créées et ont attiré des capitaux. On a même construit des ordinateurs
spécialisés pour ces programmes, les **machines Lisp**. Le Japon a lancé un grand
projet national, la **Cinquième Génération**, pour devenir le leader de ce type
d'informatique. Les limites des systèmes experts commençaient toutefois à
apparaître.

{{< image src="/images/module1/symbolics-3620.jpg" alt="Un poste de travail Lisp Symbolics 3620 : un moniteur beige marqué « symbolics », un clavier et une souris posés sur une tablette, et une haute unité centrale nervurée à droite. Un cartel de musée indique « 3620 LISP Workstation CPU, Symbolics, US, 1983 »." title="Une « machine Lisp » : le poste de travail Symbolics 3620 (1983), un ordinateur spécialisé conçu pour faire tourner les programmes d'IA symbolique." loading="lazy" >}}

<p class="image-credit">Une machine Lisp Symbolics 3620 (1983), Computer History Museum. Photo : leighklotz, <a href="https://creativecommons.org/licenses/by/2.0/">CC BY 2.0</a>, via Wikimedia Commons.</p>

## Le goulot d'étranglement

La première limite, et la plus importante, concerne l'origine des règles. Quelqu'un
doit les écrire. C'est le travail de l'**ingénieur de la connaissance**, qui
interroge longuement un expert pour traduire son savoir en règles *si… alors…*. Ce
travail s'est révélé très lent. De plus, une grande partie de l'expertise est
difficile à exprimer. Le médecin expérimenté qui reconnaît un diagnostic au premier
coup d'œil, ou le mécanicien qui identifie une panne au bruit du moteur, ne savent
pas toujours expliquer ce qu'ils savent. Leur compétence est un **savoir tacite**,
fondé sur l'intuition et l'expérience, et non une liste de règles qu'il suffirait
de noter. On ne peut pas codifier ce qui n'a jamais été formulé. Ce problème est
connu sous le nom de **goulot d'étranglement de l'acquisition des connaissances**.

La deuxième limite, déjà évoquée dans « [Représenter le
monde](docs/module1/40-representer-le-monde) », est la **rigidité**. Un système
expert ne connaît que ses règles. Il fonctionne bien à l'intérieur de son domaine,
mais dès qu'on en sort, il ne donne plus de résultats utiles, et il ne signale pas
qu'il est hors de son domaine. MYCIN diagnostiquait les infections du sang. Si on
lui avait décrit une jambe cassée, il aurait cherché un microbe, parce qu'il
n'avait aucun moyen de savoir ce qu'il ignorait. Faute de **sens commun**, il
pouvait aussi accepter des données absurdes (un patient âgé de moins de zéro an, une
dose mille fois trop forte) qu'un étudiant en médecine aurait repérées
immédiatement. Réduire le monde à un domaine restreint ne réglait donc pas le
problème du sens commun.

La troisième limite est la difficulté de **maintenance**. Un système de quelques
dizaines de règles reste gérable. XCON en a accumulé des milliers, et on a constaté
qu'au-delà d'un certain nombre, les règles **interagissent** de façon imprévisible.
Ajouter une règle pour corriger un cas pouvait en perturber plusieurs autres, sans
qu'on s'en aperçoive. Maintenir une grande base de règles demandait plus de temps
pour corriger ces effets de bord que pour ajouter des connaissances. La
connaissance explicite, écrite à la main, ne **passait pas à l'échelle**.

La quatrième limite est la plus fondamentale : un système expert n'**apprend
rien**. Chacune de ses règles a été écrite par une personne. Le programme peut
traiter mille cas sans en tirer une seule règle nouvelle, et il ne corrige pas de
lui-même les règles erronées. Toute sa connaissance lui est fournie de l'extérieur,
et elle reste figée. C'est à partir de cette limite que des chercheurs ont commencé
à poser la question autrement. Puisqu'il est coûteux, voire impossible, d'extraire
les règles des experts et de les maintenir à la main, on pourrait confier ce
travail à la machine, en la laissant découvrir les règles à partir des données.

Cette approche ne s'imposera que plus tard. À la fin des années 1980, les résultats
des systèmes experts restent en deçà des promesses. Les investisseurs se retirent,
des entreprises ferment, et les machines Lisp sont abandonnées. L'IA entre dans une
longue période de déclin, un **hiver**, décrit dans le chapitre « [Les hivers et la
bascule](docs/module1/60-hivers) ».
