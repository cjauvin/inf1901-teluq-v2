---
title: "Ce que les LLM comprennent, et ce qu'ils ratent"
weight: 94
slug: comprendre-et-rater
---

# Ce que les LLM comprennent, et ce qu'ils ratent

Les chapitres précédents ont présenté ce que font les grands modèles de langage :
prédire le jeton suivant, à une échelle immense, puis être ajustés pour répondre,
raisonner, utiliser des outils, voir et parler. Ce dernier chapitre du module pose la
question que ces résultats rendent inévitable : ces modèles comprennent-ils ce qu'ils
disent ? Il commence par leurs erreurs les plus connues, qui renseignent sur leur
fonctionnement, puis il présente ce que les chercheurs ont découvert à l'intérieur des
modèles, et les deux grandes lectures qui s'opposent. Il fait enfin le lien avec des
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

La [recherche augmentée](docs/module4/80-outils-et-agents/#chercher-dabord-répondre-ensuite)
et les citations de sources réduisent les hallucinations, sans les supprimer. La
consigne pratique reste de vérifier toute information importante, surtout les
chiffres, les noms et les références.

## Des erreurs révélatrices

Certaines erreurs montrent bien la différence entre ces modèles et une intelligence
humaine.

- **Les lettres.** Compter les *r* de *strawberry* a longtemps été difficile, parce
  que le modèle reçoit des [jetons](docs/module4/40-des-mots-aux-nombres/#découper-le-texte-les-jetons),
  pas des lettres.
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

Ce dernier résultat rejoint la mise en garde du chapitre
« [Généraliser](docs/module2/70-generaliser/#un-modèle-se-juge-sur-ce-quil-na-jamais-vu) »
du Module 2. Ces modèles ont été entraînés sur une grande partie du Web, où circulent
aussi les questions des bancs d'essai et leurs réponses. On ne sait donc jamais
complètement si un modèle résout un problème ou s'il se souvient de sa solution. C'est
la **contamination** des bancs d'essai (*benchmark contamination*). Les chercheurs
construisent régulièrement de nouveaux tests, gardés secrets ou rédigés après
l'entraînement des modèles, comme *Humanity's Last Exam* (le « dernier examen de
l'humanité »), publié en janvier 2025, qui rassemble des questions de spécialistes de
nombreuses disciplines. Les modèles y progressent vite, et le débat recommence avec
chaque nouveau test.

Enfin, comme le montrait le chapitre
« [Des outils et des agents](docs/module4/80-outils-et-agents/#des-agents) », un
modèle distingue mal les consignes de son utilisateur des textes qu'il lit. Les
[exemples adverses](docs/module3/90-tromper-un-reseau/#se-défendre) du Module 3 ont
ainsi leur équivalent pour les modèles de langage, qu'il s'agisse de formulations qui
leur font ignorer leurs règles ou d'instructions cachées dans un document.

## Regarder à l'intérieur

Les poids d'un grand modèle sont des centaines de milliards de nombres, et ni ses
concepteurs ni personne d'autre ne peut les lire directement. Le chapitre
« [Poser des questions : les arbres de décision](docs/module2/65-arbres-de-decision/#ce-quun-arbre-dit-et-ce-quil-tait) »
du Module 2 opposait déjà la performance des modèles complexes à l'explicabilité des
modèles simples. Avec les modèles de langage, cette opposition atteint son maximum.
Un domaine de recherche, l'**interprétabilité** (*interpretability*), tente pourtant
d'ouvrir cette [boîte noire](docs/module3/90-tromper-un-reseau/#une-boîte-noire).

- **Des caractéristiques lisibles.** Un même neurone d'un modèle réagit souvent à des
  concepts sans rapport entre eux. En 2024, des chercheurs d'Anthropic extraient de
  leur modèle Claude des millions de « caractéristiques » plus lisibles, chacune liée
  à un concept, comme le pont du Golden Gate, le code informatique défectueux ou la
  flatterie. En amplifiant artificiellement la caractéristique du Golden Gate, ils
  obtiennent un modèle qui ramène toutes les conversations à ce pont, jusqu'à affirmer
  qu'il est lui-même le pont.
- **Des circuits.** En 2025, la même équipe suit le cheminement de l'information dans
  le modèle. Quand il écrit un poème rimé, le modèle choisit le mot qui rimera à la fin
  du vers avant d'écrire le début du vers. Il planifie donc, au moins sur quelques
  mots, alors qu'il ne produit qu'un jeton à la fois.

La vidéo suivante, de la chaîne 3Blue1Brown déjà présentée au chapitre
« [Prédire le mot suivant](docs/module4/50-predire-le-mot-suivant/#pour-voir-le-mécanisme-en-détail) »,
montre comment un modèle peut stocker des faits dans ses poids.

{{< youtube 9-Jl0dxWQs8 >}}

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

La question posée au Module 2, sur vingt maisons, prend ici sa forme la plus aiguë :
où finit la mémoire, et où commence la compréhension ? Pour un modèle qui a lu une
grande partie de ce que l'humanité a écrit, la réponse n'est pas tranchée. Le
[Module 5](docs/module5) reprend ces questions sous leur angle philosophique, avec
l'argument de la chambre chinoise de John Searle, qui soutient qu'aucune manipulation
de symboles, si habile soit-elle, ne suffit à produire du sens. Il aborde aussi les
conséquences de ces modèles pour la société.
