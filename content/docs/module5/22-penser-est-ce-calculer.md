---
title: "Penser, est-ce calculer ?"
weight: 22
slug: penser-est-ce-calculer
---

# Penser, est-ce calculer ?

Le chapitre « [Une machine peut-elle penser ?](docs/module5/20-une-machine-peut-elle-penser) »
demandait si une machine qui se comporte comme un être pensant comprend ce qu'elle fait.
Ce chapitre pose une question plus radicale. L'IA repose depuis ses débuts sur une
hypothèse, présentée au Module 1 sous le titre
« [La pensée comme calcul](docs/module1/10-turing/#la-pensée-comme-calcul) » : penser
serait une forme de calcul, et une machine assez puissante pourrait donc, en principe,
faire tout ce que fait un esprit. Une famille d'arguments, tirés du théorème de Gödel,
soutient au contraire que l'esprit humain dépasse par principe tout calcul.

## Ce que peut faire une machine

L'idée qu'un esprit puisse être un calcul suppose de savoir ce que « calculer » veut
dire. La réponse classique est la **thèse de Church-Turing** (*Church-Turing thesis*),
formulée en 1936 par Alonzo Church et Alan Turing : tout ce qui peut être calculé par une
procédure mécanique, étape par étape, peut l'être par une
[machine de Turing](docs/module1/10-turing/#la-pensée-comme-calcul). Ce n'est pas
un théorème, puisque l'idée de « procédure mécanique » n'a pas de définition précise en
dehors de cette thèse, mais personne n'a jamais trouvé de contre-exemple. En 1985, le
physicien David Deutsch en propose une version physique : tout système physique
réalisable pourrait être simulé par une machine de calcul universelle.

{{< image src="/images/module1/machine-de-turing.svg" alt="Schéma d'une machine de Turing : un ruban de cases, une tête de lecture/écriture, un état courant et une règle de transition." title="Rappel du Module 1 : une machine de Turing lit un symbole sur son ruban, en écrit un autre, se déplace d'une case et change d'état, selon une table de règles. Toute procédure mécanique se ramène à ces quelques opérations." loading="lazy" >}}

Si cette version physique est vraie, et si le cerveau est un système physique, un
ordinateur pourrait en principe simuler le cerveau, et donc tout ce qu'il fait. C'est
l'hypothèse que conteste l'argument de Gödel.

## L'argument de Gödel contre les machines

Le Module 1 a présenté le [théorème d'incomplétude](docs/module1/10-turing/#lombre-de-gödel)
de Kurt Gödel (1931) : tout système formel cohérent, assez riche pour faire de
l'arithmétique, contient un énoncé vrai qu'il ne peut pas démontrer, une phrase qui dit
en substance « je ne suis pas démontrable ».

En 1961, le philosophe britannique John Lucas en tire un argument contre l'IA, dans un
article dont la première phrase annonce la thèse : le théorème de Gödel prouverait que
« le mécanisme est faux », c'est-à-dire que les esprits ne peuvent pas être expliqués
comme des machines. Son raisonnement tient en trois étapes.

1. Toute machine qui fait des mathématiques équivaut à un système formel.
2. Ce système a sa phrase de Gödel, qu'il ne peut pas démontrer.
3. Un mathématicien humain, lui, peut voir que cette phrase est vraie.

L'esprit humain ferait donc toujours au moins une chose qu'aucune machine donnée ne peut
faire, et aucune machine ne pourrait être un modèle complet de l'esprit.

{{< image src="/images/module5/argument-de-lucas.svg" alt="Deux panneaux. À gauche, l'argument de Lucas en trois étapes : une machine qui fait des mathématiques équivaut à un système formel F ; ce système a sa phrase de Gödel G, « Je ne suis pas démontrable dans F », qu'il ne peut pas démontrer ; un humain, lui, voit que G est vraie. À droite, la régression : si l'on ajoute G à la machine, on obtient un nouveau système, F + G, qui a sa propre phrase de Gödel G′, puis F + G + G′, qui a la sienne, G″, et ainsi de suite. En bas, l'hypothèse cachée : pour voir que G est vraie, il faut savoir que F est cohérent." title="L'argument de Lucas (1961). Ajouter la phrase de Gödel à la machine ne règle rien : le nouveau système a la sienne, et pour Lucas l'humain la voit encore. L'argument repose toutefois sur une hypothèse cachée, que visent les objections présentées plus bas : savoir que le système est cohérent." loading="lazy" >}}

Turing avait anticipé l'objection dès 1950, sous le nom d'**objection mathématique**.
Sa réponse tient en deux remarques. D'abord, Gödel montre les limites de chaque machine
particulière, mais on a seulement affirmé, « sans aucune preuve », que l'esprit humain
échappait à de telles limites. Ensuite, nous nous trompons nous-mêmes trop souvent pour
tirer fierté des erreurs des machines. Il l'avait formulé plus tôt, en 1947, dans une
conférence : « si l'on attend d'une machine qu'elle soit infaillible, elle ne peut pas
être aussi intelligente ».

{{% hint info %}}
**La disjonction de Gödel**

Gödel lui-même s'est posé la question, dans une conférence de 1951 restée inédite jusqu'en
1995. Il n'en tire pas une conclusion, mais une alternative : ou bien l'esprit humain,
même en mathématiques pures, dépasse infiniment toute machine finie, ou bien il existe
des problèmes mathématiques absolument insolubles, que personne ne pourra jamais
trancher. Les deux branches peuvent même être vraies à la fois. Gödel penchait pour la
première, mais il reconnaissait que son théorème, à lui seul, ne permettait pas de
choisir.
{{% /hint %}}

## Penrose : l'esprit non calculable

Le physicien et mathématicien britannique Roger Penrose a donné à l'argument sa forme la
plus connue, dans *The Emperor's New Mind* (1989), puis dans *Shadows of the Mind*
(1994). Penrose est l'un des grands physiciens de son temps : il a reçu en 2020 le prix
Nobel de physique pour ses travaux sur la formation des trous noirs. Selon lui, la
compréhension mathématique humaine n'est pas algorithmique. Quand un mathématicien
saisit qu'une phrase de Gödel est vraie, il fait quelque chose qu'aucun algorithme dont on
connaît la fiabilité ne peut faire. Penrose en tire une conséquence physique : puisque
le cerveau est un objet physique, il doit s'y produire un processus physique non
calculable, qu'aucun ordinateur ne peut simuler.

{{< image src="/images/module5/portraits/penrose.jpg" alt="Portrait de Roger Penrose." title="Roger Penrose en 2011." class="portrait" loading="lazy" >}}

<p class="image-credit">Roger Penrose en 2011. Photo : Biswarup Ganguly, <a href="https://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>, via Wikimedia Commons.</p>

Pour situer ce processus, Penrose s'associe au médecin anesthésiste Stuart Hameroff.
Leur théorie, appelée **Orch-OR** (*orchestrated objective reduction*), publiée en
1996, situe l'origine de la conscience dans les **microtubules**, de minuscules tubes de
protéines présents dans les neurones. Des états quantiques s'y maintiendraient, puis
s'effondreraient sous l'effet de la gravité, selon une loi physique encore inconnue,
et chacun de ces effondrements serait un moment de conscience.

La théorie est restée très minoritaire. En 2000, le physicien Max Tegmark calcule que
le cerveau, chaud et humide, détruirait ces états quantiques en un temps des milliards
de fois trop court pour qu'ils jouent un rôle dans l'activité des neurones. Hameroff et
ses collègues contestent ce calcul. En 2020, une expérience menée sous le massif du Gran
Sasso, en Italie, cherche le faible rayonnement que prédit la forme la plus simple de
l'effondrement gravitationnel imaginé par Penrose, et ne le trouve pas. Le résultat
écarte cette version, sans exclure toute forme de l'idée.

Penrose, qui a eu 95 ans en 2026, continue de défendre sa thèse. Pour lui, les systèmes
d'IA actuels calculent remarquablement bien, mais ne comprennent pas ce qu'ils font,
puisque la compréhension suppose la conscience, et que la conscience n'est pas un
calcul.

## Les objections

L'argument de Lucas et de Penrose a suscité une abondante littérature, en grande partie
critique.

- **L'objection de la cohérence.** Pour « voir » qu'une phrase de Gödel est vraie, il
  faut savoir que le système dont elle parle est cohérent. Or nous ne savons pas si notre
  propre raisonnement l'est : les mathématiciens se trompent, et ont parfois cru à des
  théories contradictoires. Le philosophe Hilary Putnam l'objecte à Lucas, puis à
  Penrose en 1994. Paul Benacerraf en tire une conclusion plus modeste : si je suis une
  machine, l'argument montre seulement que je ne peux pas savoir laquelle. Le logicien
  Solomon Feferman relève, de son côté, des erreurs techniques dans les démonstrations
  de Penrose.
- **L'objection de l'infaillibilité.** C'est celle de Turing : l'argument compare une
  machine supposée parfaite à un humain idéalisé, qui ne se tromperait jamais. Un esprit
  faillible, comme le nôtre, n'est pas soumis au théorème de Gödel de la même façon.
- **L'objection du saut.** Dans *Gödel, Escher, Bach* (1979), Douglas Hofstadter
  remarque que « sortir du système » pour voir la vérité de sa phrase de Gödel est une
  opération que l'on peut, elle aussi, mécaniser. Aucune méthode, humaine ou mécanique,
  ne peut sortir de tous les systèmes à la fois. Pour Hofstadter, l'auto-référence de
  Gödel n'est pas une limite des machines, mais le modèle de ce qu'est un esprit : une
  [boucle étrange](docs/module1/10-turing/#lombre-de-gödel).

Ces objections ne prouvent pas que l'esprit est un calcul. Elles montrent que le théorème
de Gödel ne prouve pas le contraire.

## Des machines qui démontrent

Le débat a longtemps été purement théorique. Il a changé de nature depuis que des
machines font des mathématiques de haut niveau, comme l'a montré le chapitre
« [Démontrer](docs/module4/87-demontrer) » du Module 4. En 2025, des modèles obtiennent
le score d'une [médaille d'or](docs/module4/87-demontrer/#les-olympiades-de-la-géométrie-à-lor)
aux Olympiades internationales de mathématiques. En 2026, ils
[résolvent un problème ouvert](docs/module4/87-demontrer/#vers-la-recherche) posé par
Paul Erdős, réfutent une de ses conjectures de 1946, et des agents rédigent la première
démonstration complète du dernier théorème de Fermat dans
[Lean](docs/module4/87-demontrer/#vérifier-une-preuve), un langage où chaque étape d'une
preuve est vérifiée par la machine.

Le cas le plus spectaculaire est aussi le plus disputé. Le 8 septembre 2026, OpenAI
annonce qu'un de ses systèmes a résolu l'un des sept **problèmes du millénaire**, pour
lesquels l'Institut Clay offre depuis 2000 un million de dollars chacun : celui des
**équations de Navier-Stokes** (*Navier-Stokes equations*), qui décrivent l'écoulement des
fluides, de l'eau dans un tuyau à l'air autour d'une aile d'avion. La question est de
savoir si ces équations ont toujours une solution régulière, ou si un fluide parti d'un
état parfaitement lisse peut, en un temps fini, développer une singularité, un point où
sa vitesse deviendrait infinie. Le système d'OpenAI, des milliers d'agents qui ont
travaillé pendant 88 heures, produit une démonstration de 166 pages, accompagnée d'une
version en Lean : la singularité peut se produire si une force extérieure bien choisie
agit sur le fluide, l'une des formes de réponse que prévoit l'énoncé officiel du
problème. Le résultat reste à vérifier. L'Institut Clay juge que le problème « a
apparemment été réglé », mais n'attribuera le prix qu'après une publication dans une
revue scientifique. En octobre, des chercheurs soutiennent que la version en Lean ne
traduit pas fidèlement la démonstration écrite. Deux mathématiciens, Tristan Buckmaster
et Levent Alpöge, qui travaillaient depuis un an sur un problème voisin, accusent de plus
OpenAI d'avoir pu profiter de leurs travaux, ce que l'entreprise conteste. Le cas montre
jusqu'où vont désormais les machines, mais aussi ce que devient la vérification d'une
démonstration que presque personne ne peut lire en entier.

Ces résultats ne réfutent pas, à strictement parler,
[l'argument de Penrose](docs/module5/22-penser-est-ce-calculer/#penrose-lesprit-non-calculable). Celui-ci ne
dit pas que les machines ne peuvent pas démontrer de théorèmes, mais qu'aucune ne peut
voir la vérité de sa propre phrase de Gödel. Ils affaiblissent pourtant l'intuition sur
laquelle il repose. L'argument supposait que la compréhension mathématique, cette
capacité de « voir » une vérité, était ce qui distinguait l'esprit de la machine. Des machines qui trouvent des démonstrations inédites rendent cette distinction moins évidente. Penrose répond qu'elles trouvent
sans comprendre.

Une inquiétude voisine vient des mathématiciens eux-mêmes. En septembre 2026,
vingt-cinq médaillés Fields signent une déclaration pour rappeler que résoudre des
problèmes n'est qu'un moyen au service de la compréhension, comme le présente le
chapitre « [Démontrer](docs/module4/87-demontrer/#ce-que-cela-dit-et-ce-que-cela-ne-dit-pas) ».
Ils ne prétendent pas que les machines ne pourront jamais comprendre, mais que des
démonstrations qui n'expliquent rien ne font pas avancer les mathématiques. La question
de Penrose revient ainsi sous une autre forme : il ne s'agit plus de savoir si une
machine peut trouver la vérité, mais si elle peut la comprendre, et si cela compte.

{{% hint info %}}
**Dans la conversation**

Dans la [conversation](docs/module5/95-conversation) de l'été 2025, un passage
consacré à [Penrose (45:05)](https://www.youtube.com/watch?v=R8sqq_gJbUI&t=2705s)
rappelle que des penseurs très sérieux refusent de réduire l'esprit à un calcul. L'un
des interlocuteurs avoue n'avoir jamais tout à fait saisi l'argument, qui finit par
invoquer la mécanique quantique, et se demande s'il ne revient pas, au fond, à
réintroduire une part d'âme, ce que Penrose refuserait, puisqu'il cherche une
explication scientifique. Le passage enchaîne sur Chomsky, une autre thèse forte sur
l'esprit, que les modèles de langage ont mise à l'épreuve.
{{% /hint %}}

## Un pari

La question « penser, est-ce calculer ? » n'est pas tranchée. Ceux qui répondent oui
s'appuient sur la thèse de Church-Turing et sur les succès de l'IA, mais ne peuvent pas
prouver qu'aucun processus non calculable n'intervient dans l'esprit. Ceux qui répondent
non s'appuient sur Gödel et sur l'expérience intime de la compréhension, mais leurs
arguments formels n'ont pas convaincu la plupart des logiciens, et la physique qu'ils
supposent n'a pas été observée.

Pour la plupart des chercheurs en IA, l'hypothèse du calcul reste un pari, celui sur lequel la discipline s'est fondée [en 1956](docs/module1/20-deux-paris/#le-moment-lété-1956-à-dartmouth), et que ses progrès rendent de plus en plus
plausible sans le démontrer. Elle rejoint la question, plus difficile encore, de la [conscience](docs/module5/24-une-machine-peut-elle-etre-consciente) : Penrose lie la compréhension à la conscience, et sa théorie Orch-OR est
d'abord une théorie de la conscience.
