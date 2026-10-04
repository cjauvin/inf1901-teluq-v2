---
title: "Représenter le monde"
weight: 40
slug: representer-le-monde
---

# Représenter le monde

## Le sens, angle mort de la machine

Les chapitres précédents ont présenté plusieurs programmes. Le [Logic
Theorist](docs/module1/20-deux-paris) démontrait des théorèmes, [Deep
Blue](docs/module1/30-chercher-raisonner/#lapogée-deep-blue-bat-kasparov-1997)
gagnait aux échecs et [ELIZA](docs/module1/30-chercher-raisonner/#lautre-visage-eliza-ou-lillusion-de-comprendre)
tenait une conversation. Tous faisaient cependant la même chose : ils
**manipulaient des symboles d'après leur forme**, selon des règles. Par exemple,
ELIZA repérait le mot « mère » sans savoir ce qu'est une mère. On parle dans ce cas
du niveau de la **syntaxe**, qui consiste à agencer correctement des symboles sans
tenir compte de leur sens.

Comprendre le monde demande davantage. Les spécialistes du langage distinguent
trois niveaux, qu'on peut illustrer par un exemple simple. À table, quelqu'un vous
dit **« Pouvez-vous me passer le sel ? »**

- La **syntaxe** concerne la *forme*. La phrase est une question grammaticalement
  bien construite. Une machine peut le vérifier sans rien comprendre.
- La **sémantique** concerne le *sens littéral*. La phrase porte sur votre
  *capacité* à passer le sel. Pour la comprendre à ce niveau, il faut savoir ce que
  signifient « sel », « passer » et « pouvoir ».
- La **pragmatique** concerne l'*intention réelle en contexte*. Tout le monde
  comprend qu'il ne s'agit pas d'une question sur vos aptitudes (« oui, je peux
  passer le sel! »), mais d'une **demande** polie, « passez-moi le sel ». Pour
  comprendre cela, il faut connaître le contexte et un grand nombre de
  sous-entendus que nous partageons tous.

On peut résumer ainsi la situation de l'IA symbolique : elle réussissait bien au
niveau de la **syntaxe**, atteignait difficilement la **sémantique** et échouait
au niveau de la **pragmatique**. Pour passer de la forme au sens, une machine a
besoin de **connaissances** sur le monde, et Deep Blue et ELIZA n'en avaient
aucune. Ce chapitre porte sur les tentatives pour fournir ces connaissances aux
machines et sur leur échec. La question de départ est la suivante : comment
mettre dans une machine ce que tout le monde sait ?

## Donner un savoir à la machine

Si l'intelligence exige des connaissances, il faut trouver un moyen de les
**inscrire dans la machine** sous une forme qu'elle puisse exploiter. Entre la fin
des années 1960 et les années 1970, trois grandes façons de structurer le savoir
sont proposées.

**Les réseaux sémantiques** (*semantic networks*, Ross Quillian). On représente les connaissances comme
un **réseau de concepts reliés** par des relations. « Canari » est relié à
« oiseau » par un lien *est-un* (*is-a*), et « oiseau » est relié à « animal » de la même
façon. « Oiseau » est relié à « ailes » par un lien *possède*. La machine peut
alors **déduire** des faits qu'on ne lui a pas donnés explicitement. Par exemple,
pour savoir si un canari a des ailes, il suffit de suivre les liens (*canari est-un
oiseau*, *oiseau possède ailes*) pour conclure que oui. Ces réseaux portent le mot
**sémantique** dans leur nom parce que leur objectif est de passer de la forme au
sens.

{{< image src="/images/module1/reseau-semantique.svg" alt="Réseau sémantique reliant canari, oiseau et animal par des liens « est-un », avec héritage des propriétés." title="Un réseau sémantique : les propriétés s'héritent en remontant les liens « est-un »." loading="lazy" >}}

**Les frames, ou « cadres »** (Marvin Minsky, 1974). Au lieu de concepts isolés,
Minsky propose de regrouper le savoir en **situations types** qui comportent des
« cases » à remplir, avec des valeurs par défaut. Le cadre « chambre d'hôtel »
comporte des cases pour le lit, la porte et la salle de bain. Par défaut, on
s'attend à y trouver un lit. Quand vous entrez dans une chambre d'hôtel inconnue,
vous n'analysez pas toute la scène. Vous utilisez ce cadre déjà connu et vous ne
corrigez que ce qui ne correspond pas. Les frames permettent donc de représenter
nos **attentes**.

{{< image src="/images/module1/frame-chambre-hotel.svg" alt="Le cadre « chambre d'hôtel » sous forme de fiche : des cases (lit, salle de bain, porte, fenêtre, téléviseur) avec leurs valeurs par défaut." title="Un frame : une situation type dont les cases ont des valeurs par défaut." loading="lazy" >}}

**Les scripts** (Roger Schank et Robert Abelson). L'idée est la même, mais elle
s'applique à des **enchaînements d'actions**. Le « script du restaurant » décrit la
séquence attendue : entrer, s'asseoir, consulter le menu, commander, manger, payer,
partir. Grâce à ce script, une machine peut **compléter** un récit. Si on lui dit
« Jean est allé au restaurant et a commandé un steak », elle en déduit qu'il s'est
assis, qu'il a mangé et qu'il a payé, même si le récit ne le dit pas.

{{< image src="/images/module1/script-restaurant.svg" alt="Le script du restaurant en sept étapes ; seules « entrer » et « commander » sont dites, les autres sont comblées par le script." title="Un script : la séquence attendue, dont la machine complète les étapes non dites." loading="lazy" >}}

Ces trois approches ont en commun une capacité qui manquait à Deep Blue et à
ELIZA, celle d'**inférer l'implicite**, c'est-à-dire d'utiliser un savoir de fond
pour aller au-delà de ce qui est dit littéralement. Elles représentent un progrès
réel vers la sémantique.

Ces représentations ont un ancêtre plus rigoureux, la **logique formelle**. Depuis
Boole et Frege, la logique cherche à réduire le raisonnement à un *calcul* sur des
symboles : « Socrate est un homme ; tous les hommes sont mortels ; donc Socrate est
mortel ». Ce syllogisme semble porter sur le sens, mais on l'obtient par une
opération mécanique sur la *forme* des énoncés. Le problème est là. Qu'on enchaîne
des règles logiques ou qu'on suive des liens dans un réseau, on manipule toujours
la **forme** des symboles. La question est de savoir si la forme suffit à
représenter le **sens**. Comme on va le voir, ce progrès vers la sémantique
s'accompagne d'une fragilité importante.

{{% hint info %}}
Ces façons de structurer le savoir (réseaux de concepts, cases à remplir,
hiérarchies *est-un*) n'ont pas disparu avec le GOFAI. Elles ont été reprises
ailleurs. Le **web sémantique**, les **ontologies** et les
**knowledge graphs** utilisés
par la recherche de Google ou par Wikidata en sont les descendants directs, et les
*cases héritées* des frames ressemblent aux **objets** de la
programmation moderne. Nous y reviendrons dans « [Les hivers et la
bascule](docs/module1/60-hivers) », pour évaluer ce que le GOFAI a laissé.
{{% /hint %}}

## SHRDLU, ou le sommet de l'ambition

C'est dans ce contexte optimiste qu'un jeune chercheur du MIT, **Terry Winograd**,
réalise vers **1970** un programme qu'on considère encore comme l'un des résultats
les plus avancés de l'IA symbolique, **SHRDLU**. Le programme dialogue en anglais
ordinaire avec un humain à propos d'un petit monde de **blocs colorés** (cubes,
pyramides, boîtes posés sur une table), qu'il peut déplacer à l'aide d'un bras
robotique virtuel. Pour l'époque, la conversation est très impressionnante :

> — *Prends un gros bloc rouge.*
> — D'accord.
> — *Saisis la pyramide.*
> — Je ne sais pas de **quelle** pyramide vous parlez.
> — *Trouve un bloc plus haut que celui que tu tiens et place-le dans la boîte.*
> — Par « **le** », je suppose que vous parlez du bloc plus haut que celui que je
>   tiens.

Dans cet échange, SHRDLU **lève une ambiguïté** (quelle pyramide), **résout un
pronom** (ce à quoi renvoie « le »), **agit** sur le monde et **se souvient** de ce
qu'il vient de faire. On peut aussi lui demander « Pourquoi as-tu fait ça ? », et
il **explique** son raisonnement.

{{< image src="/images/module1/micromonde-shrdlu.svg" alt="Le micro-monde de SHRDLU : un cube rouge, une pile de blocs, une pyramide et une boîte posés sur une table, avec un bras robotique." title="Le « micro-monde » de SHRDLU : un univers très petit, entièrement décrit à la main." loading="lazy" >}}

Le film de démonstration d'époque ci-dessous (en anglais) montre SHRDLU en
fonctionnement : les ordres tapés au clavier, les réponses du programme et le bras
virtuel qui déplace les blocs.

{{< youtube id="bo4RvYJYOzI" >}}

SHRDLU y parvient parce qu'il maintient un **modèle du monde** (*world model*),
c'est-à-dire une représentation interne de sa petite scène : quel bloc repose sur
quel autre, lequel est rouge, lequel est libre, ce que le bras tient à ce moment.
À chaque action, il **met ce modèle à jour**, et à chaque question, il le
**consulte**. C'est ce modèle interne qui lui permet de résoudre « le », de se
rappeler son action précédente et de justifier ce qu'il a fait. SHRDLU ne se
contente donc pas de parler des blocs, il en possède une représentation exacte.
Cette idée est importante : **un modèle du monde est une représentation interne de
la réalité, sur laquelle on peut raisonner**. Nous la retrouverons [beaucoup plus
loin dans le cours](docs/module4), au centre d'un débat important sur les IA actuelles.

Cette réussite repose cependant sur une simplification. Le modèle du monde de
SHRDLU est exact parce qu'il a très peu de choses à représenter : quelques blocs,
une table, une boîte, quelques formes et couleurs. Dans un univers aussi petit, on
peut tout décrire à la machine, c'est-à-dire la liste complète des objets, des
propriétés et des actions possibles. Le « monde » de SHRDLU tient entièrement dans
une représentation **codée à la main**. Winograd l'appelait d'ailleurs un
**micro-monde** (*blocks world*), et le préfixe *micro* indique bien sa taille.
L'intérêt du micro-monde est qu'il rend le problème **traitable** (*tractable*, en
anglais). En informatique, un problème est traitable quand une machine peut le
résoudre en un temps raisonnable, sans être freinée par l'[explosion
combinatoire](docs/module1/30-chercher-raisonner/#lexplosion-combinatoire) des
possibilités. Avec quelques blocs, tout peut être représenté et chaque question
obtient une réponse immédiatement. C'est ce qui explique la réussite de SHRDLU, et
c'est aussi sa limite, parce que le monde réel n'est pas traitable en ce sens,
comme le montre la [section suivante](docs/module1/40-representer-le-monde/#le-mur-du-sens-commun).

En dehors de la table à blocs, SHRDLU ne peut rien faire. Son modèle du monde ne
contient rien sur la pluie, un mensonge ou un escalier. Il ne peut pas être étendu
au monde réel, parce qu'il faudrait alors y représenter tout ce qui existe. Toutes
les approches de ce chapitre ont la même limite. Elles fonctionnent tant qu'on
reste dans un domaine assez petit pour être entièrement décrit, et elles échouent
dès qu'il faut tenir compte de la très grande quantité de choses que les humains
considèrent comme évidentes. Cette quantité de savoir évident a un nom, et elle
constitue la principale limite du GOFAI.

## Le mur du sens commun

Cette limite s'appelle le **sens commun** (*common sense*). Il s'agit de l'ensemble très vaste des
choses si évidentes que personne ne prend la peine de les dire. Par exemple, l'eau
mouille, un objet qu'on lâche tombe, on ne peut pas pousser une corde, votre mère
est plus âgée que vous, et si Jean entre dans un restaurant, il y entre par la
porte et non par le plafond. Nous utilisons en permanence des millions de
certitudes de ce genre. Comme elles vont **sans dire**, personne ne les a jamais
écrites.

Or toute l'IA symbolique repose sur un principe : pour qu'une machine sache
quelque chose, il faut lui **inscrire** ce savoir. Les réseaux sémantiques, les
frames, les scripts et SHRDLU fonctionnent tant que ce savoir tient dans un domaine
assez petit pour être décrit à la main. La machine ne sait que ce qu'on lui a
fourni explicitement. Le sens commun, lui, **n'a pas de limite**. Pour le donner à
une machine, il faudrait lui décrire le monde entier.

Un chercheur a tenté de le faire. En **1984**, **Douglas Lenat** lance **CYC** (de
l'anglais *encyclopedia*), un projet très ambitieux dont l'objectif est
d'**encoder à la main**, fait après fait et règle après règle, la totalité du sens
commun humain. Des équipes y ont consacré des **décennies** et des dizaines de
millions de dollars, et ont saisi des millions d'assertions, comme « un café chaud
refroidit si on le laisse » ou « on ne peut pas être à deux endroits à la fois ».
C'est le projet le plus ambitieux de l'histoire du GOFAI.

{{< image src="/images/module1/cyc-assertions.svg" alt="Cinq entrées de la base de CYC, écrites dans son langage, CycL, avec leur traduction en français : Bill Clinton fait partie des présidents des États-Unis ; tous les arbres sont des plantes ; Paris est la capitale de la France ; tout animal à colonne vertébrale a une mère biologique ; et une règle générale : si un objet appartient à une catégorie, il appartient aussi à toutes celles qui la contiennent." title="Le sens commun écrit à la main : quelques entrées de CYC dans son langage, CycL, et leur signification." loading="lazy" >}}

CYC n'a jamais atteint son objectif. La raison n'est pas un manque d'argent ou de
compétence, mais le fait que la tâche n'a **pas de fin**. Chaque évidence saisie
en fait apparaître dix autres, et chacune de celles-ci en suppose cent. On ne peut
pas compléter le sens commun par petites quantités, parce qu'il s'étend à mesure
qu'on l'écrit. CYC s'est heurté au même problème que le reste de ce chapitre :
**le savoir implicite d'un humain ordinaire est trop vaste pour être énuméré**.

Le GOFAI atteint donc ici sa limite. On pensait qu'il suffisait de donner des
connaissances à la machine, mais les connaissances les plus importantes sont
justement celles que personne ne formule. Cependant, en dehors du courant
dominant, un chercheur affirmait depuis longtemps qu'on abordait le problème dans
le mauvais sens et qu'on cherchait le sens au mauvais endroit. Avant de terminer
sur l'âge d'or symbolique, il faut présenter ce point de vue dissident.

## L'objection de Hofstadter

Ce chercheur est **Douglas Hofstadter**, l'auteur de la notion de *boucle étrange*,
déjà présenté dans « [Turing et la question
fondatrice](docs/module1/10-turing) » à propos de Gödel.
Pendant que ses collègues construisaient des moteurs d'échecs et des bases de
règles (*rule bases*), il répétait que l'IA dominante ne s'attaquait pas au bon problème. Selon
Hofstadter, battre Kasparov par force brute ou accumuler des millions d'assertions
comme CYC ne concerne pas l'essentiel de la pensée.

Pour lui, l'essentiel de la pensée est l'**analogie**. Penser ne consiste pas à
appliquer des règles, mais à *percevoir des ressemblances*, à adapter des
**concepts fluides** (*fluid concepts*) à des situations nouvelles et à comprendre l'inconnu à partir
de ce qu'on connaît déjà. Quand vous parlez du *pied* d'une montagne, des *jambes*
d'une table ou de la *bouche* d'un fleuve, vous faites de l'analogie sans y penser.
C'est l'opération de l'esprit la plus courante et aussi la plus fondamentale. Or
une analogie ne peut pas être inscrite d'avance dans une base de connaissances (*knowledge base*).
Elle se construit au moment où on en a besoin, selon le contexte. C'est
précisément ce qu'un projet comme CYC ne pouvait pas représenter.

Pour le démontrer, Hofstadter et sa collaboratrice **Melanie Mitchell** ont conçu
un programme, **Copycat**, qui fonctionne lui aussi dans un micro-monde, mais d'un
genre très différent de celui de SHRDLU. Son univers est constitué de simples
**chaînes de lettres**. On lui pose des problèmes d'analogie, par exemple : si
`abc` devient `abd`, que devient `ijk` ? La réponse naturelle est `ijl`, parce
qu'on remplace la dernière lettre par la suivante dans l'alphabet. Cependant,
Copycat n'applique pas une règle fixe. Il *perçoit* une structure, et il peut en
percevoir plusieurs. Si on lui demande ce que devient **`xyz`** selon la même
analogie, le problème est plus difficile, parce que le `z` n'a pas de lettre
suivante. Il n'y a plus de réponse unique. On peut proposer `xyd`, ou `wyz`, ou
recommencer au début de l'alphabet. La « bonne » réponse dépend de la façon dont
on perçoit la situation. C'est ce que Hofstadter veut montrer : l'intelligence
n'est pas l'exécution d'une règle, mais une **perception fluide, sensible au
contexte**.

{{< image src="/images/module1/copycat-analogie.svg" alt="L'énigme de Copycat : abc devient abd, ijk devient ijl, puis le cas xyz qui admet plusieurs réponses (xyd, wyz, xya)." title="L'énigme de Copycat : pour « xyz », la réponse dépend de la façon dont on perçoit la suite." loading="lazy" >}}

Les deux micro-mondes ont donc des rôles opposés. SHRDLU utilisait un micro-monde
pour **simplifier** le problème, c'est-à-dire pour avoir un univers assez petit
pour tout y énumérer d'avance. Hofstadter réduit le sien pour la raison
**inverse**. Il écarte tout le savoir encyclopédique afin d'**isoler l'essentiel**,
l'analogie elle-même. Ces deux micro-mondes correspondent à deux conceptions
opposées de l'intelligence.

Reste la question qui traverse tout ce chapitre, celle de savoir comment le sens
peut apparaître à partir de simples symboles. La réponse de Hofstadter prolonge
son idée de **boucle étrange**. Selon lui, le sens n'est pas **injecté** de
l'extérieur, fait après fait, comme CYC l'espérait. Il **émerge** d'un système
assez riche pour s'observer lui-même, percevoir ses propres structures et établir
des analogies entre ses propres états. On ne remplit pas un esprit de
significations. On met en place un mécanisme dont la signification émerge. C'est
l'opposé de la démarche du GOFAI, qui voulait tout écrire à la main.

Hofstadter avait en partie raison. Sa **vision** était juste. Comme on le verra,
c'est par l'émergence, et non par l'inscription, que l'IA finira par progresser.
Cependant, sa **solution** n'a jamais eu l'ampleur de son ambition. Copycat est
resté un petit programme de laboratoire, remarquable mais limité. Hofstadter ne
travaillait pas non plus sur les réseaux de neurones. Il a indiqué la bonne
direction sans construire l'outil qui permettrait de la suivre.

Cet outil existait déjà, mais il était alors peu développé. Depuis « [Deux paris
rivaux](docs/module1/20-deux-paris) », nous savons qu'il existe une **autre
tradition**, qui ne cherche pas à décrire le monde à la machine, mais qui la laisse
l'**apprendre** elle-même à partir d'exemples. Le GOFAI a atteint sa limite, le
sens commun lui a résisté, et l'idée d'émergence, proposée par l'un de ses
critiques, va déjà dans cette direction. L'idée de laisser la machine apprendre
plutôt que de tout lui dire ne s'imposera toutefois qu'après une longue période
de recul de l'IA. Avant ce déclin, l'IA symbolique connaîtra encore sa période de
plus grand succès.

{{% details "Pour aller plus loin : le fonctionnement de Copycat" %}}
Copycat ne contient aucune règle du genre « remplace la dernière lettre ». Il
explore en parallèle un grand nombre de petits rapprochements possibles (une
lettre est-elle un début, une fin, le successeur d'une autre ?), qui se renforcent
ou s'inhibent mutuellement. Une mesure interne, que ses auteurs appellent la
**« température »**, indique à quel point une interprétation cohérente a émergé.
Tant que tout reste flou, la température est élevée et le programme continue
d'explorer presque au hasard. Quand une structure d'ensemble se forme, la
température baisse et la réponse se stabilise. Le sens n'est donc pas *calculé* en
une seule étape, mais **construit** peu à peu, par une compétition entre des
perceptions partielles. Selon Hofstadter, ce mécanisme illustre à petite échelle
ce qui caractérise la cognition.
{{% /details %}}
