---
title: "Une machine peut-elle penser ?"
weight: 20
slug: une-machine-peut-elle-penser
---

# Une machine peut-elle penser ?

C'est la plus ancienne des questions que pose l'IA, et la première des
[familles de problèmes](docs/module5/10-quels-problemes/#neuf-familles-de-problèmes)
de ce module, celle des problèmes philosophiques. En 1950, Alan Turing la jugeait
« trop dépourvue de sens pour mériter d'être discutée », et proposait de la remplacer
par une épreuve concrète, le [jeu de l'imitation](docs/module1/10-turing/#le-jeu-de-limitation)
présenté au Module 1. Soixante-quinze ans plus tard, des machines réussissent cette
épreuve. La question de départ ne disparaît pas pour autant : elle revient, plus
pressante que jamais.

## Le test de Turing, réussi

Dans son article de 1950, Turing faisait une prédiction : vers l'an 2000, un
interrogateur moyen n'aurait pas plus de 70 % de chances de reconnaître la machine
après cinq minutes de conversation. La prédiction a mis vingt-cinq ans de plus à se
réaliser, et elle a été dépassée.

En mars 2025, deux chercheurs de l'Université de Californie à San Diego, Cameron Jones
et Benjamin Bergen, publient les résultats d'un test de Turing dans sa forme
d'origine, à trois. Près de 300 participants conversent pendant cinq minutes, en même
temps, avec un humain et avec une IA, puis désignent celui qu'ils croient humain.
Quand on demande à GPT-4.5 de jouer un personnage, celui d'un jeune adulte un peu
introverti et familier de la culture Internet, il est pris pour l'humain dans 73 % des
cas, plus souvent que les vrais humains eux-mêmes. ELIZA, le programme de 1966 présenté
au [Module 1](docs/module1/30-chercher-raisonner/#lautre-visage-eliza-ou-lillusion-de-comprendre),
ne trompe les participants que dans 23 % des cas. Sans la consigne de jouer un
personnage, GPT-4.5 tombe à 36 %. L'étude, reprise et prolongée en 2026 dans la revue
*PNAS* avec des conversations de quinze minutes, conclut que les grands modèles de
langage réussissent le test de Turing.

Turing avait aussi prédit qu'à la fin du siècle, on pourrait parler de machines qui
pensent « sans s'attendre à être contredit ». Sur ce point, il s'est trompé. Jamais on
n'a autant débattu de la question.

## Ce que le test ne mesure pas

Les auteurs de l'étude eux-mêmes refusent d'y voir une preuve d'intelligence. Selon
Cameron Jones, pour les modèles, le test de Turing est « un jeu où il faut mentir » :
réussir, c'est se faire passer pour quelqu'un d'autre. Les participants jugeaient
d'ailleurs moins sur le savoir ou le raisonnement que sur le ton, l'humour ou les
émotions. Le test mesure la ressemblance avec un humain, et l'on sait depuis ELIZA
qu'il est [facile de donner l'illusion](docs/module4/94-comprendre-et-rater/#lillusion-de-comprendre)
de comprendre.

Le désaccord porte en réalité sur ce que « penser » veut dire. Le Module 1 a présenté
le [fonctionnalisme](docs/module1/10-turing/#le-jeu-de-limitation), la thèse selon
laquelle un état mental se définit par son rôle, ses causes et ses effets, et non par la
matière qui le réalise. Si elle est vraie, une machine qui se comporte en tout point
comme un être pensant pense, quelle que soit la matière dont elle est faite. Le
philosophe Daniel Dennett, mort en 2024, défendait une version de cette idée, la
**posture intentionnelle** (*intentional stance*) : on attribue des croyances et des
désirs à un système, humain ou non, quand cela permet de prédire son comportement, et
cette attribution est justifiée tant qu'elle prédit bien. Dennett n'en était pas pour
autant rassuré. En 2023, il qualifiait les IA conversationnelles qui se font passer
pour des humains de « fausses personnes » (*counterfeit people*), et de plus
dangereux artefacts de l'histoire humaine.

## La chambre chinoise

L'objection la plus célèbre au fonctionnalisme vient du philosophe américain John
Searle, mort en septembre 2025. Dans un article de 1980, « *Minds, Brains, and
Programs* », il imagine l'expérience de pensée de la **chambre chinoise** (*Chinese
room*).

Searle, qui ne connaît pas un mot de chinois, est enfermé dans une pièce. Par une fente,
on lui glisse des questions écrites en caractères chinois. Il dispose d'un gros livre
de règles, écrit en anglais, qui lui indique, pour chaque suite de caractères reçue,
quelle suite renvoyer. Il applique les règles, sans rien comprendre, et glisse ses
réponses par une autre fente. Si les règles sont assez bonnes, les réponses sont
parfaites : de l'extérieur, la chambre semble comprendre le chinois. Pourtant, personne
à l'intérieur ne le comprend.

{{< image src="/images/module5/chambre-chinoise.svg" alt="Deux panneaux. À gauche, la chambre chinoise : une personne enfermée dans une pièce, qui ne connaît pas le chinois, reçoit par une fente une question écrite en caractères chinois, consulte un livre de règles écrit dans sa langue, et renvoie par une autre fente une réponse parfaite. De l'extérieur, la chambre semble comprendre le chinois ; à l'intérieur, personne ne le comprend. À droite, un modèle de langage : des jetons, représentés par des numéros, entrent dans un bloc rempli de nombres, les poids du modèle, et un jeton en sort. Le même schéma : des symboles entrent, d'autres sortent, selon des règles, mais des règles apprises et non écrites." title="La chambre chinoise de Searle (1980), et le même schéma appliqué à un modèle de langage. Les caractères chinois sont stylisés." loading="lazy" >}}

Pour Searle, la personne dans la chambre fait exactement ce que fait un ordinateur : elle
manipule des symboles selon leur forme, en suivant un programme. Elle ne comprend
pourtant rien. Aucun programme ne peut donc, par lui-même, produire de la
compréhension. Il résume l'argument par une formule : **la syntaxe ne suffit pas à la
sémantique**. On retrouve les niveaux du langage présentés au Module 1, avec
[le sens comme angle mort de la machine](docs/module1/40-representer-le-monde/#le-sens-angle-mort-de-la-machine).
Searle ne prétend pas qu'une machine ne pourra jamais penser : le cerveau est lui-même
une machine, biologique. Il soutient que la pensée dépend des propriétés physiques du
cerveau, et non du seul programme qu'il exécute.

## Les réponses à Searle

L'article de 1980 a été publié avec près de trente commentaires de philosophes et de chercheurs, et le débat dure depuis. Les principales réponses, et ce que Searle leur
oppose, sont les suivantes.

- **La réponse du système.** La personne ne comprend pas le chinois, mais le système
  entier, la personne avec son livre, ses feuilles et ses crayons, le comprend.
  Searle répond qu'il suffit d'imaginer qu'il apprenne tout le livre par cœur et fasse
  les calculs de tête : il serait alors le système entier, et ne comprendrait toujours
  pas le chinois.
- **La réponse du robot.** Il faudrait relier la chambre au monde, par des caméras et
  des bras, pour que les symboles désignent des choses. Searle répond que les images
  des caméras ne seraient pour lui que d'autres symboles à manipuler.
- **La réponse du simulateur de cerveau.** Un programme qui reproduirait, neurone par
  neurone, le cerveau d'un locuteur chinois comprendrait. Searle imagine alors un
  système de tuyaux et de robinets qui imiterait les neurones : il ne comprendrait rien
  non plus.
- **La réponse des autres esprits.** Nous ne savons que les autres humains comprennent
  qu'en observant leur comportement. Refuser cette preuve à une machine serait
  incohérent. Searle répond que la question n'est pas de savoir comment on sait qu'un
  être comprend, mais ce qu'on lui attribue quand on dit qu'il comprend.

Beaucoup de philosophes jugent que la réponse du système n'a jamais été vraiment
réfutée : notre intuition qu'« il n'y a personne qui comprend » vaut peut-être pour la
personne dans la chambre, sans valoir pour l'ensemble. D'autres tiennent l'argument de
Searle pour décisif. Plus de quarante ans plus tard, aucun camp n'a convaincu l'autre.

## Le problème de l'ancrage

En 1990, le chercheur en sciences cognitives Stevan Harnad reformule l'objection sous la forme du **problème
de l'ancrage des symboles** (*symbol grounding problem*). Imaginez que vous deviez
apprendre le chinois avec, pour seul outil, un dictionnaire unilingue chinois. Chaque
mot y est défini par d'autres mots chinois, qui renvoient à d'autres encore : vous
tournez en rond, de définition en définition, sans jamais atteindre le sens. Pour
Harnad, les symboles d'un système doivent être ancrés quelque part, dans la perception
et l'action, pour avoir un sens qui leur soit propre, et non un sens emprunté à ceux
qui les lisent.

{{% hint info %}}
**La pieuvre de Bender et Koller**

En 2020, les linguistes Emily Bender et Alexander Koller transposent l'objection aux
modèles de langage. Deux personnes, naufragées sur deux îles, communiquent par un câble
sous-marin. Une pieuvre très intelligente écoute la ligne, apprend les régularités des
messages, puis coupe le câble et se fait passer pour l'une des deux. Tant que la
conversation reste banale, personne ne s'en aperçoit. Mais le jour où l'une des
naufragées, poursuivie par un ours, demande comment fabriquer une arme avec des
bâtons, la pieuvre ne peut pas l'aider : elle n'a jamais connu que la forme des
messages, jamais ce dont ils parlent. Leur conclusion est qu'un système entraîné
seulement sur la forme n'a, en principe, aucun moyen d'apprendre le sens. C'est la même
intuition que celle des
[perroquets stochastiques](docs/module4/94-comprendre-et-rater/#perroquets-ou-modèles-du-monde),
publiée l'année suivante par Bender et ses coautrices.
{{% /hint %}}

## La chambre chinoise à l'ère des modèles de langage

Un grand modèle de langage ressemble beaucoup à la chambre de Searle : des jetons
entrent, d'autres sortent, et entre les deux, il n'y a que des calculs sur des nombres.
Les deux situations diffèrent pourtant sur des points qui nourrissent le débat.

- **Les règles n'ont pas été écrites.** Le livre de Searle était rédigé par quelqu'un
  qui comprenait le chinois. Les poids d'un modèle ont été appris, en
  [prédisant le mot suivant](docs/module4/50-predire-le-mot-suivant/#ce-que-la-prédiction-exige)
  dans d'immenses quantités de textes. Si une compréhension s'y trouve, elle n'a été
  empruntée à personne.
- **On peut regarder dans la chambre.** Les travaux sur
  l'[interprétabilité](docs/module4/93-regarder-a-l-interieur) trouvent dans les
  modèles des concepts, des étapes de raisonnement intermédiaires et des plans, et
  l'expérience sur Othello montre qu'un modèle peut se construire une représentation de
  son [petit monde](docs/module4/94-comprendre-et-rater/#perroquets-ou-modèles-du-monde).
  Pour les uns, c'est une forme de compréhension. Pour Searle, ce ne serait encore que
  de la syntaxe, mieux organisée.
- **Le sens par l'usage.** Les chercheurs Steven Piantadosi et Felix Hill soutiennent
  en 2022 que le sens d'un mot tient en grande partie à ses relations avec les autres,
  à son rôle dans un réseau de concepts, ce que les
  [plongements](docs/module4/45-des-mots-aux-nombres/#on-reconnaît-un-mot-à-ses-fréquentations)
  capturent justement. Dans cette lecture, la référence au monde n'est pas la seule
  source du sens.
- **L'ancrage par les sens.** Les modèles récents ne lisent plus seulement du texte :
  ils [voient, entendent et parlent](docs/module4/92-voir-entendre-parler), ce qui
  répond en partie à la réponse du robot, et au problème de l'ancrage. Pour Harnad et
  Searle, ces images et ces sons ne seraient pourtant que d'autres symboles.

L'auteur de ce cours propose une autre façon de poser le problème dans un court
billet, « [Est-ce que ChatGPT sait ce qu'est une question ?](https://cjauvin.github.io/posts/llm-question-reponse/) ».
L'IA classique supposait qu'un système doit d'abord construire une représentation du
sens d'une phrase, puis s'en servir pour répondre. Un modèle de langage semble se
passer de cette étape : il répond en prédisant la suite, et ses réponses sont pourtant
souvent justes. Le billet rapproche cette situation de la chambre chinoise, mais aussi
des **jeux de langage** du philosophe Ludwig Wittgenstein, pour qui répondre à une
question n'est pas une opération unique, avec une essence cachée, mais une famille
d'usages qu'on apprend en participant à la vie d'une communauté. Si comprendre, c'est
savoir jouer ces jeux, la question devient moins « que se passe-t-il à l'intérieur ? »
que « que sait-il faire avec les mots ? ».

## Un débat ouvert

Les chercheurs eux-mêmes sont partagés, presque à parts égales. En 2022, avant même
ChatGPT, un sondage auprès de plus de 300 chercheurs en traitement de la langue leur
demande si un modèle entraîné seulement sur du texte pourrait, avec assez de données et
de calcul, comprendre la langue « en un sens non trivial ». 51 % répondent oui, 49 %
non. En 2023, Melanie Mitchell et David Krakauer, de l'Institut de Santa Fe, concluent
leur revue du débat en suggérant que ces modèles comprennent peut-être d'une autre
façon que nous, avec d'autres forces et d'autres limites, et qu'il faudrait une
nouvelle science de l'intelligence pour comparer ces formes de compréhension.

Les positions se répartissent à peu près ainsi.

| Position | L'argument principal | Quelques voix |
|---|---|---|
| **Oui, ces modèles pensent et comprennent** | Leur comportement est celui d'un agent qui comprend, et rien dans leur fonctionnement ne l'interdit | Herman Cappelen et Josh Dever (2025) |
| **En partie, autrement que nous** | Ils ont des représentations, des croyances en un sens affaibli, mais différentes des nôtres | David Chalmers, Melanie Mitchell |
| **Non, ils imitent** | Ils ne manipulent que la forme des mots, sans accès au sens ni au monde | John Searle, Emily Bender |
| **La question est mal posée** | « Penser » et « comprendre » désignent des familles d'usages, qu'il faut décrire plutôt que trancher | Alan Turing, et une lecture de Wittgenstein |

Ces positions ne s'opposent pas seulement sur les faits, comme ce que contiennent les
modèles, mais aussi sur les
[concepts](docs/module5/10-quels-problemes/#des-faits-et-des-valeurs), sur ce que l'on
accepte d'appeler comprendre. Douglas Hofstadter, qui jugeait les machines très loin
de la pensée humaine, déclarait en 2023 que les progrès des modèles de langage avaient
ébranlé ses convictions, comme le rappelle le chapitre
« [Ce que les LLM comprennent, et ce qu'ils ratent](docs/module4/94-comprendre-et-rater/#perroquets-ou-modèles-du-monde) ».
Penser et comprendre ne sont d'ailleurs pas les seules capacités en jeu. Une autre
objection, plus ancienne encore, soutient que l'esprit humain dépasse par principe tout
calcul : celle que Roger Penrose a tirée du
[théorème de Gödel](docs/module1/10-turing/#lombre-de-gödel).
