---
title: "Ce que les LLM comprennent, et ce qu'ils ratent"
weight: 94
slug: comprendre-et-rater
---

# Ce que les LLM comprennent, et ce qu'ils ratent

Les chapitres précédents ont présenté ce que font les grands modèles de langage :
prédire le jeton suivant, à une échelle immense, puis être ajustés pour répondre,
raisonner, démontrer, utiliser des outils, voir et parler. Le chapitre
« [Le défi ARC](docs/module4/88-le-defi-arc) » a montré ce qui leur résiste encore
devant des problèmes nouveaux, et le chapitre
« [Regarder à l'intérieur](docs/module4/93-regarder-a-l-interieur) » ce que les
chercheurs ont découvert à l'intérieur des modèles. Ce dernier chapitre du module pose la
question que ces résultats rendent inévitable : ces modèles comprennent-ils ce qu'ils
disent ? Il commence par leurs erreurs les plus connues, qui renseignent sur leur
fonctionnement, puis il présente les deux grandes lectures qui s'opposent. Il fait enfin le lien avec des
questions posées tout au long du cours.

## Les hallucinations

Un modèle de langage peut affirmer avec assurance une chose fausse : une citation
inventée, une référence bibliographique qui n'existe pas, une date erronée. On parle
d'**hallucination** (*hallucination*), même si le terme est discuté, puisque le modèle
ne perçoit rien.

{{% hint warning %}}
**Deux affaires judiciaires**

En mai 2023, à New York, dans l'affaire *Mata c. Avianca*, des avocats déposent un
mémoire rédigé avec l'aide de ChatGPT. Il cite plusieurs jugements qui n'existent
pas, avec des citations inventées. Interrogé, ChatGPT avait assuré que ces décisions
existaient bel et bien. Les avocats sont condamnés à une amende de 5 000 dollars.

En février 2024, au Canada, un tribunal de la Colombie-Britannique donne raison à un
client d'Air Canada. L'assistant du site Web de la compagnie lui avait décrit une
politique de remboursement qui n'existait pas. La compagnie soutenait que l'assistant
était responsable de ses propres paroles. Le tribunal juge au contraire qu'elle est
responsable de toutes les informations publiées sur son site, y compris par un
assistant automatique.
{{% /hint %}}

L'origine des hallucinations découle de ce que fait le modèle. Il produit le texte le
plus plausible, et une référence inventée peut être aussi plausible qu'une vraie :
elle a la bonne forme, des auteurs crédibles et un titre vraisemblable. Le modèle n'a
pas, en général, de moyen fiable de distinguer ce qu'il sait de ce qu'il devine. En
septembre 2025, des chercheurs d'OpenAI ajoutent une explication liée à l'évaluation.
La plupart des tests notent une réponse juste par 1 et une réponse fausse ou une
abstention par 0. Comme à un examen à choix multiples sans pénalité, deviner rapporte
alors plus que d'avouer son ignorance, et l'entraînement renforce cette habitude.

La [recherche augmentée](docs/module4/80-outils-et-agents/#chercher-dabord-répondre-ensuite-rag)
et les citations de sources réduisent les hallucinations, sans les supprimer. La
consigne pratique reste de vérifier toute information importante, surtout les
chiffres, les noms et les références.

## Des erreurs révélatrices

Certaines erreurs montrent bien la différence entre ces modèles et une intelligence
humaine.

{{% hint info %}}
**Combien de *r* dans *strawberry* ?**

En 2024, la question devient célèbre : de nombreux modèles répondent « deux », alors
que le mot en compte trois. La raison tient au
découpage en jetons, qu'on peut observer dans l'applet du chapitre
« [Des mots aux nombres](docs/module4/45-des-mots-aux-nombres/#découper-le-texte-les-jetons) ».
Dans la question, GPT-4o reçoit *strawberry* comme un seul jeton, un simple numéro ;
écrit seul, le mot est découpé en trois morceaux, *st*, *raw* et *berry*. Dans les deux
cas, le modèle ne voit jamais les lettres elles-mêmes.

Pourtant, si on lui demande d'épeler *strawberry*, il y parvient. Pendant son
entraînement, il a lu d'innombrables textes où des mots sont épelés, et il connaît
l'orthographe de ses jetons comme on connaît un fait par cœur, sans la voir. Compter
les *r* lui demande donc de retrouver ce fait, puis de compter de tête, deux
opérations où il peut se tromper.

Deux remèdes, présentés dans d'autres chapitres, règlent le problème. Avec une
[chaîne de pensée](docs/module4/70-du-modele-a-l-assistant/#des-modèles-qui-raisonnent-rlvr),
le modèle écrit d'abord le mot lettre par lettre ; chaque lettre devient alors un
jeton du contexte, qu'il peut compter. Avec un
[outil](docs/module4/80-outils-et-agents/#le-harnais-et-lappel-doutils), il écrit une
ligne de programme, `"strawberry".count("r")`, et obtient la réponse exacte. Les
modèles de raisonnement apparus à partir de septembre 2024 ne se trompent plus sur
cette question. Elle reste un rappel utile : un modèle de langage ne voit pas le texte
comme nous.
{{% /hint %}}

{{< image src="/images/module4/strawberry.svg" alt="Trois rangées. En haut, ce que voit un humain : les dix lettres s, t, r, a, w, b, e, r, r, y, dont trois r, surlignés. Au milieu, ce que reçoit GPT-4o quand on lui pose la question « Combien de r dans strawberry ? » : sept jetons, Comb, ien, de, r, dans, strawberry et le point d'interrogation ; strawberry est un seul jeton, le numéro 101 830, où aucune lettre n'est visible. En bas, le mot épelé dans une chaîne de pensée, s-t-r-a-w-b-e-r-r-y : chaque lettre devient un jeton, et les trois jetons qui contiennent un r peuvent être comptés, un, deux, trois." title="Combien de r dans strawberry ? Le modèle ne voit pas les lettres d'un mot, sauf s'il l'épelle lui-même. Découpages réels de GPT-4o." loading="lazy" >}}

D'autres erreurs sont tout aussi révélatrices.

- **L'inversion.** En 2023, une équipe de chercheurs montre qu'un modèle entraîné sur
  des phrases de la forme « A est B » n'en déduit pas « B est A ». Un modèle qui sait
  que la mère de l'acteur Tom Cruise s'appelle Mary Lee Pfeiffer répond sans peine à
  cette question, mais peine à dire de qui Mary Lee Pfeiffer est la mère.
- **Les variantes d'un même problème.** En 2024, des chercheurs d'Apple reprennent des
  problèmes d'arithmétique d'un banc d'essai connu, en changeant seulement les noms
  et les nombres. Les performances de nombreux modèles baissent, et elles baissent
  davantage quand on ajoute une phrase sans rapport avec le problème. Les modèles
  semblent reconnaître des problèmes familiers plutôt que de raisonner sur chaque
  énoncé.

Ce dernier résultat rejoint le problème présenté dans la section
« [Que mesurent les scores ?](docs/module4/60-passer-a-l-echelle/#que-mesurent-les-scores) » :
on ne sait jamais complètement si un modèle résout un problème ou s'il se souvient de
sa solution. De nouveaux tests tentent d'y répondre, comme *Humanity's Last Exam*
(« le dernier examen de l'humanité »), publié en janvier 2025, ou ARC, présenté au
chapitre « [Le défi ARC](docs/module4/88-le-defi-arc) », qui vise la capacité à faire
face à du nouveau.

Enfin, un modèle distingue mal les consignes de son utilisateur des textes qu'il lit,
ce qui l'expose aux
[injections d'instructions](docs/module4/80-outils-et-agents/#des-agents-un-modèle-et-son-harnais-en-boucle),
l'équivalent pour les modèles de langage des
[exemples adverses](docs/module3/90-tromper-un-reseau/#se-défendre) du Module 3.

## Perroquets ou modèles du monde ?

Deux lectures de ces résultats s'opposent.

La première voit dans ces modèles des **perroquets stochastiques** (*stochastic
parrots*). L'expression vient d'un article publié en 2021 par les linguistes Emily
Bender et Angelina McMillan-Major et les chercheuses en informatique Timnit Gebru et
Margaret Mitchell. Google avait demandé le retrait de l'article, et le conflit a mené
au départ de Timnit Gebru de l'entreprise. Selon cette lecture, un modèle de langage
assemble des suites de mots selon leurs probabilités, sans accès au sens : il n'a
jamais vu un chat ni goûté une pizza, et il ne sait rien du monde que ses phrases
décrivent. C'est le [niveau de la syntaxe](docs/module1/40-representer-le-monde/#le-sens-angle-mort-de-la-machine),
au sens du Module 1, poussé à un degré de raffinement inédit, sans la sémantique.

La seconde lecture soutient que, pour prédire assez bien un texte, il faut en venir à
représenter ce dont il parle. En 2023, Kenneth Li et ses collègues entraînent un petit
Transformer sur des parties du jeu Othello, présentées seulement comme des suites de
coups, sans jamais lui montrer le plateau. En examinant ses vecteurs internes, ils
retrouvent pourtant une représentation de l'état du plateau, case par case, et en la
modifiant, ils changent les coups que le modèle propose. Le modèle s'est construit un
**modèle du monde**, au moins pour ce petit monde.

La notion avait été présentée au Module 1 avec
[SHRDLU](docs/module1/40-representer-le-monde/#shrdlu-ou-le-sommet-de-lambition) : en
1970, ce programme maintenait une représentation explicite de son monde de blocs,
écrite à la main, et c'est elle qui lui permettait de comprendre les phrases qu'on lui
adressait. Les modèles de langage actuels sont immenses, mais ils n'ont pas de
représentation explicite du monde. L'un des critiques les plus connus est Yann Le Cun,
le pionnier des [réseaux convolutifs](docs/module3/50-reseaux-convolutifs/#yann-le-cun-et-les-chèques)
du Module 3. Selon lui, un modèle qui prédit du texte jeton après jeton ne peut pas
acquérir une vraie compréhension du monde physique, que les enfants apprennent en
l'observant et en agissant, bien avant de parler. Il plaide pour des modèles qui
apprennent à prédire l'évolution du monde à partir de la vidéo et de l'action, et il
quitte Meta en décembre 2025 pour fonder une entreprise consacrée à ces modèles du
monde.

Ce débat remet en cause un schéma presque aussi ancien que l'IA elle-même. On a
longtemps supposé que comprendre une phrase se fait en deux temps : le système
construit d'abord une représentation interne de son sens, puis s'en sert pour agir ou
répondre. SHRDLU en est l'exemple parfait. Un modèle de langage semble court-circuiter
cette étape. Rien, dans son entraînement, ne lui demande de construire une
représentation du sens, et ses réponses sont pourtant souvent justes. Si une forme de
compréhension peut émerger de la seule prédiction du mot suivant, le schéma est à
revoir. L'auteur de ce cours développe cette idée dans un court billet,
« [Est-ce que ChatGPT sait ce qu'est une question ?](https://cjauvin.github.io/posts/llm-question-reponse/) ».
Il la rapproche de la [chambre chinoise](docs/module1/10-turing/#le-jeu-de-limitation)
de Searle et des jeux de langage de Wittgenstein.

Les deux lectures ne sont pas forcément exclusives. Un modèle peut contenir des
représentations partielles du monde, efficaces dans certains domaines et absentes dans
d'autres, ce qui expliquerait à la fois ses réussites et ses erreurs étranges.
Douglas Hofstadter, dont le Module 1 présentait l'[objection](docs/module1/40-representer-le-monde/#lobjection-de-hofstadter)
à l'IA symbolique, avait longtemps jugé que les machines resteraient loin de la
pensée humaine. En 2023, il déclare que les progrès rapides de ces modèles ont fait
s'effondrer certaines de ses convictions les plus profondes sur les limites de l'IA.

## L'illusion de comprendre

Une partie de la question tient aussi à nous. Le Module 1 présentait
[ELIZA](docs/module1/30-chercher-raisonner/#lautre-visage-eliza-ou-lillusion-de-comprendre),
le programme de 1966 qui imitait un psychothérapeute en repérant quelques mots-clés.
Ses utilisateurs lui prêtaient pourtant une compréhension et des sentiments. Cette
tendance à attribuer une intelligence et une intériorité à ce qui produit un langage
fluide porte le nom d'**effet ELIZA**. Les modèles actuels sont incomparablement plus
capables qu'ELIZA, mais la même tendance joue, d'autant plus fortement que leurs
réponses sont fluides, polies et sûres d'elles. Elle explique en partie l'attachement
de certains utilisateurs à des assistants présentés comme des compagnons, et la
confiance excessive accordée à leurs réponses.

## Deux façons de savoir

Le chapitre « [Les hivers et la bascule](docs/module1/60-hivers/#lhéritage-invisible) »
du Module 1 annonçait une comparaison entre deux conceptions du savoir. Les systèmes
experts et les graphes de connaissances contiennent un savoir **structuré à la main** :
chaque fait y est écrit, vérifiable et modifiable, mais il faut l'écrire, et le monde
déborde toujours ce qu'on a écrit. Un modèle de langage contient un savoir **absorbé**
dans d'énormes quantités de texte : il couvre presque tous les sujets et s'exprime avec
souplesse, mais on ne peut ni le lire, ni le vérifier fait par fait, ni le corriger
simplement. Les systèmes actuels combinent souvent les deux, par exemple quand un
modèle de langage consulte une base de faits avant de répondre.

La question posée au
[Module 2](docs/module2/70-generaliser/#un-modèle-se-juge-sur-ce-quil-na-jamais-vu), sur
vingt maisons, prend ici sa forme la plus aiguë :
où finit la mémoire, et où commence la compréhension ? Pour un modèle qui a lu une
grande partie de ce que l'humanité a écrit, la réponse n'est pas tranchée.

## Ce qu'il faut retenir du module

Ce module a commencé sur un paradoxe : un mécanisme d'une simplicité déconcertante,
prédire la suite d'un texte, et des capacités qui surprennent jusqu'à leurs auteurs.
Les chapitres l'ont décomposé en quelques idées.

1. **Générer, c'est imiter une distribution, puis y tirer des exemples.** C'est le
   principe commun à tous les modèles génératifs, des images aux voix
   (« [Générer : imiter une distribution](docs/module4/10-generer) »).
2. **Un modèle de langage prédit le mot suivant.** L'idée a soixante-dix ans
   d'histoire, des règles aux n-grammes, puis aux plongements et au Transformer
   (« [Des règles aux probabilités](docs/module4/40-des-regles-aux-probabilites) »,
   « [Prédire le mot suivant](docs/module4/50-predire-le-mot-suivant) »).
3. **L'échelle a tout changé, de façon en partie prévisible**
   (« [Passer à l'échelle](docs/module4/60-passer-a-l-echelle) »).
4. **Un modèle de base n'est pas un assistant.** L'ajustement, les préférences humaines
   et les récompenses vérifiables en font un
   (« [Du modèle à l'assistant](docs/module4/70-du-modele-a-l-assistant) »).
5. **Le modèle ne fait que du texte ; son harnais fait le reste.** La mémoire
   apparente, les outils et les actions viennent du programme qui l'entoure : le modèle
   propose, le harnais dispose
   (« [Des outils, un harnais et des agents](docs/module4/80-outils-et-agents) »).
6. **La vérification fait la fiabilité.** Les tests guident les agents de
   programmation, et une preuve acceptée par Lean n'a pas à être crue sur parole
   (« [Programmer avec des agents](docs/module4/85-programmer-avec-des-agents) »,
   « [Démontrer](docs/module4/87-demontrer) »). Mesurer l'intelligence elle-même reste
   difficile (« [Le défi ARC](docs/module4/88-le-defi-arc) »).
7. **Les mêmes idées s'étendent aux images et aux sons**, devenus eux aussi des
   jetons (« [Des modèles qui voient, entendent et parlent](docs/module4/92-voir-entendre-parler) »).
8. **L'intérieur des modèles commence à se lire.** On y trouve des concepts
   superposés, que l'on peut démêler, et des étapes de calcul que le texte produit ne
   montre pas
   (« [Regarder à l'intérieur](docs/module4/93-regarder-a-l-interieur) »).
9. **Ces modèles ont des limites caractéristiques** : ils hallucinent, ne voient pas
   les lettres de leurs jetons, et n'apprennent rien de leurs conversations.

Le mécanisme de départ n'a pas changé : prédire la suite. Ce qui a changé, c'est
l'échelle à laquelle on l'applique, ce qu'on apprend aux modèles ensuite, et ce qu'on
construit autour d'eux. Savoir si cela suffit pour comprendre reste une question
ouverte. Le [Module 5](docs/module5) la reprend sous son angle philosophique, avec
l'argument de la chambre chinoise de Searle, évoqué
[plus haut](#perroquets-ou-modèles-du-monde), et aborde les conséquences de ces
modèles pour la société.
