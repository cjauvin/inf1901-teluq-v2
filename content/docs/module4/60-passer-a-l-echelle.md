---
title: "Passer à l'échelle"
weight: 60
slug: passer-a-l-echelle
---

# Passer à l'échelle

Le chapitre « [Prédire le mot suivant](docs/module4/50-predire-le-mot-suivant) » a
présenté le principe des grands modèles de langage : un Transformer entraîné à
prédire le jeton suivant d'un texte. Ce principe n'a presque pas changé depuis le
premier GPT, en 2018. Ce qui a changé, c'est la **taille** : la taille des modèles,
la quantité de textes sur lesquels ils sont entraînés, et la quantité de calcul
consacrée à leur entraînement. Ce chapitre présente cette course à la taille, ce
qu'elle a produit, et ce qu'elle coûte.

## De GPT à GPT-4

Chaque nouvelle version des modèles d'OpenAI a multiplié la taille de la précédente.

- **GPT** (juin 2018) compte 117 millions de paramètres. Il est entraîné sur environ
  7 000 livres.
- **GPT-2** (février 2019) compte 1,5 milliard de paramètres, entraînés sur 8 millions
  de pages Web. OpenAI annonce d'abord ne pas publier le modèle complet, par crainte
  qu'il serve à produire de fausses nouvelles en masse, puis le publie par étapes
  jusqu'en novembre 2019. Ses textes sont souvent cohérents sur plusieurs
  paragraphes, ce qui surprend à l'époque.
- **GPT-3** (mai 2020) compte 175 milliards de paramètres, entraînés sur environ
  300 milliards de jetons.
- **GPT-4** (mars 2023) est beaucoup plus performant, mais OpenAI ne publie plus sa
  taille. Selon Sam Altman, le directeur d'OpenAI, son entraînement a coûté plus de
  100 millions de dollars.

D'autres entreprises ont publié des modèles du même ordre de grandeur, comme Google,
Anthropic ou Meta. La figure ci-dessous rassemble quelques modèles dont la taille est
connue. Les barres sont dessinées sur une échelle logarithmique : chaque graduation
vaut dix fois la précédente.

{{< image src="/images/module4/taille-des-modeles.svg" alt="Deux diagrammes à barres sur une échelle logarithmique, où chaque graduation vaut dix fois la précédente. À gauche, le nombre de paramètres : 117 millions pour GPT-1 en 2018, 1,5 milliard pour GPT-2 en 2019, 175 milliards pour GPT-3 en 2020, 70 milliards pour Chinchilla en 2022, 405 milliards pour Llama 3.1 en 2024. À droite, le nombre de jetons d'entraînement : 300 milliards pour GPT-3, 1 400 milliards pour Chinchilla, 15 000 milliards pour Llama 3.1." title="En six ans, le nombre de paramètres a été multiplié par plus de 3 000, et la quantité de texte d'entraînement a suivi." loading="lazy" >}}

## Des lois d'échelle

Pourquoi les entreprises ont-elles investi des sommes croissantes dans des modèles
toujours plus grands ? En partie parce que le résultat était prévisible.

En janvier 2020, Jared Kaplan et ses collègues, chez OpenAI, publient une étude sur
des centaines de modèles de tailles différentes. Ils mesurent l'erreur de chaque
modèle sur des textes qu'il n'a jamais vus, c'est-à-dire sa capacité à prédire le
jeton suivant. Cette erreur diminue de façon très régulière quand on augmente le
nombre de paramètres, la quantité de données ou la quantité de calcul. Sur un
graphique à échelles logarithmiques, les points s'alignent sur une droite. On parle
de **lois d'échelle** (*scaling laws*). Il s'agit de **lois de puissance** (*power laws*) :
chaque fois qu'on multiplie le calcul par dix, l'erreur diminue d'une même proportion,
jusqu'à un plancher qu'aucun modèle ne franchit, puisqu'une part du texte reste
imprévisible.

L'observation n'est pas tout à fait neuve. Dès décembre 2017, une équipe de Baidu
Research montre que l'erreur diminue selon une loi de puissance quand la quantité de
données d'entraînement augmente, dans quatre domaines, la traduction automatique, la
modélisation du langage, la classification d'images et la reconnaissance de la parole.
L'étude de Kaplan étend ce constat à la taille des modèles et au calcul, et en tire une
recette.

{{< image src="/images/module4/loi-d-echelle.svg" alt="Un schéma. L'axe horizontal donne la quantité de calcul utilisée pour l'entraînement, l'axe vertical l'erreur du modèle sur des textes qu'il n'a jamais vus, tous deux sur une échelle logarithmique. Des points, un par modèle entraîné, s'alignent sur une droite qui descend régulièrement. La droite est prolongée en pointillé vers la droite : on peut prédire l'erreur d'un modèle plus grand avant de l'entraîner." title="Le principe d'une loi d'échelle (schéma) : en prolongeant la droite, on prévoit l'erreur d'un modèle plus grand avant de l'entraîner." loading="lazy" >}}

Ces lois ont une conséquence pratique. Avant de dépenser des dizaines de millions de
dollars pour entraîner un très grand modèle, on peut entraîner une série de petits
modèles, tracer la droite, et prévoir le résultat. En 2023, OpenAI dit avoir ainsi
prévu l'erreur finale de GPT-4 à partir de modèles entraînés avec jusqu'à 10 000 fois
moins de calcul. Ces lois prédisent cependant une erreur moyenne sur le jeton suivant,
pas ce que le modèle saura faire. La section
« [Des capacités qui apparaissent ?](docs/module4/60-passer-a-l-echelle/#des-capacités-qui-apparaissent) »
montre que ce passage de l'un à l'autre est discuté. Elles confirment aussi la
[leçon amère](docs/module3/40-apprentissage-profond/#la-leçon-amère) de Richard
Sutton, présentée au Module 3 : les méthodes générales qui tirent parti d'une
quantité croissante de calcul finissent par l'emporter. Elles prolongent enfin
l'énigme présentée au chapitre
« [L'apprentissage profond](docs/module3/40-apprentissage-profond/#plus-de-paramètres-que-dexemples) » :
ces modèles ont des milliards de paramètres, et pourtant ils généralisent de mieux
en mieux à mesure qu'ils grandissent.

En mars 2022, une équipe de DeepMind corrige la recette. Pour un budget de calcul
donné, il ne sert à rien d'agrandir le modèle si on ne lui donne pas assez de textes.
Leur modèle Chinchilla, avec 70 milliards de paramètres entraînés sur
1 400 milliards de jetons, dépasse des modèles quatre fois plus grands entraînés sur
moins de données. La règle qui en est tirée, environ vingt jetons d'entraînement par
paramètre, a guidé les modèles suivants. Ceux-ci vont d'ailleurs bien au-delà : un
modèle plus petit, entraîné plus longtemps, coûte moins cher à utiliser ensuite.

## Apprendre dans le contexte

L'article qui présente GPT-3 en 2020 s'intitule « *Language Models are Few-Shot
Learners* » (« les modèles de langage apprennent à partir de quelques exemples »). Il
décrit une capacité que personne n'avait programmée.

{{% hint info %}}
**Quelques exemples dans la requête**

L'article donne à GPT-3 le texte suivant, et lui demande de le continuer. La consigne
de la première ligne était en anglais ; elle est traduite ici.

```
Traduire de l'anglais vers le français :
sea otter => loutre de mer
peppermint => menthe poivrée
plush girafe => girafe peluche
cheese =>
```

Le modèle complète par « fromage ». Il n'a jamais été entraîné spécialement à
traduire. Les trois exemples placés dans le texte suffisent à lui faire comprendre la
tâche demandée, et il l'applique au quatrième mot.
{{% /hint %}}

Cette capacité s'appelle l'**apprentissage dans le contexte** (*in-context learning*). On
distingue la requête sans exemple (*zero-shot*), avec un seul exemple (*one-shot*) et
avec quelques exemples (*few-shot*). Elle est très différente de l'apprentissage
présenté au [Module 2](docs/module2/50-entrainer-un-modele) : aucun poids du modèle
n'est modifié. Le modèle reconnaît la tâche dans le texte qu'on lui donne, et ses
performances augmentent avec sa taille. GPT-3 réussit de nombreuses tâches de cette
façon, alors que les modèles plus petits n'y parviennent presque pas. La rédaction des
requêtes (*prompting*) est devenue une compétence à part entière, présentée au chapitre
« [Des outils, un harnais et des agents](docs/module4/80-outils-et-agents/#formuler-la-requête) ».

Ces mots existaient avant les grands modèles de langage, avec un autre sens. En
apprentissage automatique, l'**apprentissage à partir de quelques exemples**
(*few-shot learning*) désignait la capacité d'apprendre une catégorie nouvelle, un
oiseau ou un visage jamais vus, à partir d'une poignée d'exemples étiquetés, en
ajustant les poids d'un modèle déjà entraîné. L'apprentissage **sans exemple**
(*zero-shot learning*) désignait la reconnaissance d'une catégorie qu'on n'a jamais
vue, à partir de sa seule description, par exemple « un oiseau au bec rouge et à la
queue fourchue ». Avec GPT-3, les mêmes mots ont pris un sens nouveau : les exemples
se trouvent dans la requête, et le modèle n'est pas entraîné du tout. Les deux sens
coexistent encore, et il faut souvent deviner, d'après le contexte, lequel un auteur
emploie.

L'apprentissage dans le contexte n'est qu'un point sur un spectre. Pour faire accomplir
une tâche à un modèle, on peut lui donner plus ou moins d'exemples, et modifier plus
ou moins ses poids.

| Façon de faire | Exemples nécessaires | Les poids changent-ils ? |
|---|---|---|
| requête sans exemple (*zero-shot*) | aucun, seulement une consigne | non |
| requête avec quelques exemples (*few-shot*) | de un à quelques dizaines, placés dans la requête | non |
| [ajustement](docs/module4/70-du-modele-a-l-assistant/#imiter-de-bonnes-réponses) (*fine-tuning*) | des centaines à des milliers | oui, un peu |
| [entraînement complet](docs/module2/50-entrainer-un-modele) | des milliers à des milliards | oui, entièrement |

Plus on descend dans le tableau, plus il faut de données et de calcul, mais plus le
modèle se spécialise. En pratique, on essaie d'abord la requête, qui ne coûte presque
rien, et on n'ajuste le modèle que si elle ne suffit pas. Jusqu'en 2020, presque tout
se faisait dans les deux dernières rangées. La surprise de GPT-3 est que les deux
premières suffisent souvent.

## Des capacités qui apparaissent ?

En 2022, Jason Wei et ses collègues, chez Google, décrivent des **capacités
émergentes** (*emergent abilities*). Sur certaines tâches, comme l'addition de nombres
de plusieurs chiffres ou certaines énigmes, les petits modèles échouent presque
complètement, puis, au-delà d'une certaine taille, les modèles réussissent soudain.
La capacité semble apparaître d'un coup, sans avoir été annoncée par les modèles
plus petits. L'idée a beaucoup circulé, car elle suggère que des modèles plus
grands pourraient acquérir des capacités imprévisibles.

En 2023, Rylan Schaeffer et ses collègues, à l'Université Stanford, contestent cette
interprétation. Selon eux, l'apparition soudaine vient souvent de la façon de mesurer.
Si l'on compte une addition comme réussie seulement quand tous les chiffres sont
exacts, la note passe brusquement de 0 à 1. Si l'on compte les chiffres exacts un par
un, le progrès est régulier. Le débat n'est pas tranché : certaines capacités semblent
bien apparaître de façon abrupte, d'autres sont des effets de mesure.

## Que mesurent les scores ?

Toutes ces mesures supposent une chose : que le modèle n'ait jamais vu les questions
du test. C'est la règle fondamentale du Module 2 :
[un modèle se juge sur ce qu'il n'a jamais vu](docs/module2/70-generaliser/#un-modèle-se-juge-sur-ce-quil-na-jamais-vu),
et la moindre
[fuite de données](docs/module2/75-bien-evaluer/#le-score-trop-beau-pour-être-vrai-la-fuite-de-données)
rend le score trop beau pour être vrai.

Avec les grands modèles de langage, cette règle devient presque impossible à
respecter. On les compare sur des **bancs d'essai** (*benchmarks*), des tests
standardisés de questions et de problèmes. Or ces modèles sont entraînés sur une
grande partie du Web, où circulent aussi ces questions : les énoncés sont publiés en
ligne, discutés sur des forums, accompagnés de leurs solutions. Plus le corpus est
grand, plus il est probable qu'une question du test, ou une variante proche, s'y
trouve. Et comme les entreprises publient rarement la liste exacte de leurs données
d'entraînement, on ne peut même pas le vérifier. C'est la **contamination** des bancs
d'essai (*benchmark contamination*) : la contamination du Module 2, à l'échelle du
Web.

Deux observations montrent que le problème est réel.

- En 2023, des utilisateurs remarquent que GPT-4 résout des problèmes de
  programmation du site Codeforces publiés avant la fin de ses données
  d'entraînement, mais presque aucun des problèmes de même difficulté publiés après.
- En 2024, une équipe de l'entreprise Scale AI rédige GSM1k, mille nouveaux
  problèmes de mathématiques de même niveau que ceux de GSM8k, un banc d'essai très
  utilisé. Plusieurs modèles y perdent jusqu'à 13 points : ils avaient en partie
  appris le banc d'essai lui-même.

S'y ajoute un effet plus subtil, résumé par la **loi de Goodhart** : quand une mesure
devient un objectif, elle cesse d'être une bonne mesure. Comme les entreprises se
comparent sur les mêmes bancs d'essai, elles ont intérêt à y optimiser leurs
modèles, consciemment ou non. Les chercheurs répondent de plusieurs façons : des
tests gardés secrets, des tests rédigés après la date de fin des données
d'entraînement, et des évaluations où des humains comparent deux réponses sans
savoir de quel modèle elles viennent. Aucune n'est parfaite. Savoir ce qu'un grand
modèle sait vraiment faire, au-delà de ce qu'il a vu, reste l'une des questions les
plus difficiles du domaine.

{{% hint info %}}
**Un pélican à vélo**

Fin octobre 2024, le programmeur et blogueur Simon Willison commence à soumettre les
nouveaux modèles à un test de son invention : « *Generate an SVG of a pelican riding
a bicycle* », dessiner en SVG un pélican qui fait du vélo. Le SVG est un format
d'image écrit sous forme de code. Le modèle doit donc décrire chaque cercle et chaque
trait par ses coordonnées, sans jamais voir le résultat. La tâche est plus difficile
qu'elle n'en a l'air : un vélo est difficile à dessiner de mémoire, un pélican aussi,
et un pélican n'a pas la forme qu'il faut pour pédaler. Surtout, la scène est assez
absurde pour qu'aucun dessin de ce genre ne circule sur le Web, et le modèle ne peut
pas en recopier un.

{{< image src="/images/module4/pelicans-willison.svg" alt="Quatre dessins produits à partir de la même demande, dessiner en SVG un pélican qui fait du vélo. GPT-4o mini, octobre 2024 : deux disques noirs pour les roues, deux traits pour le cadre, un oiseau gris posé dessus. GPT-5, août 2025 : un vrai vélo, avec rayons et pédalier, et un oiseau au long bec orange assis sur la selle. Gemini 3 Pro, novembre 2025 : un pélican blanc à la poche orange sur un vélo rouge, une aile tendue vers le guidon. Claude Fable 5.1, septembre 2026 : une illustration soignée, un pélican casqué qui pédale sur une plage, un poisson dans le panier." title="La même demande, faite à quatre modèles successifs, de 2024 à 2026. Images de Simon Willison, simonwillison.net." loading="lazy" >}}

Le test devient célèbre. En mai 2025, un pélican à vélo apparaît dans la grande
conférence annuelle de Google, et en octobre 2025, une équipe d'Anthropic s'en sert
pour [regarder à l'intérieur](docs/module4/93-regarder-a-l-interieur) d'un modèle qui
dessine : elle y trouve des caractéristiques qui représentent les roues, le vélo ou
les yeux de l'oiseau. Willison se demande alors si les laboratoires ne finiront pas
par entraîner leurs modèles sur ce test précis, comme le prévoit la loi de Goodhart.
Il garde donc en réserve des variantes secrètes, d'autres animaux sur d'autres
véhicules : un modèle qui dessinerait un excellent pélican et un mauvais flamant rose
sur un monocycle se trahirait. En avril 2026, un petit modèle ouvert, qui tourne sur
son ordinateur portable, dessine un meilleur pélican que Claude Opus 4.7. Méfiant,
Willison sort l'une de ses variantes. En juillet 2026, il rappelle lui-même que le
test a commencé comme une plaisanterie, et que la qualité d'un pélican ne dit plus
grand-chose de celle d'un modèle.

Le modèle qui a aidé à rédiger ce cours (voir
« [Comment ce cours a été produit](docs/60-assistants-intelligents/#comment-ce-cours-a-été-produit) »)
s'est prêté au jeu en octobre 2026, en un seul essai, sans voir son dessin avant de
l'avoir terminé.

{{< image src="/images/module4/pelican-opus-5-5.svg" alt="Un pélican blanc à la poche orange, assis sur la selle d'un vélo vert, une aile tendue vers le guidon, une patte sur chaque pédale, sur fond de ciel bleu pâle et de sol beige. Le soleil, en haut à droite, touche le bout du bec." title="Le pélican de Claude Opus 5.5, dessiné en octobre 2026 au premier essai, sans voir le résultat, et gardé tel quel : le soleil touche le bout du bec, et la chaîne du vélo est approximative." loading="lazy" >}}
{{% /hint %}}

## Le prix de la taille

Entraîner un grand modèle demande des dizaines de milliers de
[processeurs graphiques](docs/module3/42-materiel-et-outils/#les-processeurs-graphiques)
qui fonctionnent pendant des semaines ou des mois. Les entreprises construisent pour
cela des centres de données géants, qui consomment autant d'électricité qu'une ville
et de grandes quantités d'eau pour leur refroidissement. Les coûts se comptent en
centaines de millions de dollars par modèle, et les investissements annuels du
secteur en centaines de milliards.

Les données posent un autre problème. Les modèles sont entraînés sur une grande
partie du texte disponible sur le Web, et les meilleurs textes, comme les livres, les
articles scientifiques ou les encyclopédies, ne sont pas infinis. En 2024, l'institut
de recherche Epoch AI estime que les modèles auront été entraînés sur l'équivalent de
tout le texte humain public disponible quelque part entre 2026 et 2032. Les
entreprises se tournent donc vers des **données synthétiques** (*synthetic data*), produites par d'autres
modèles, et vers des textes sous licence. Le recours aux textes protégés par le droit
d'auteur fait l'objet de nombreux procès, comme celui que le *New York Times* a
intenté à OpenAI et à Microsoft en décembre 2023. Le [Module 5](docs/module5) revient
sur ces coûts environnementaux et juridiques.

## Les modèles de frontière

On appelle **modèles de frontière** (*frontier models*) les modèles qui repoussent, à un
moment donné, la limite de ce que l'IA sait faire. Anthropic emploie le terme dès mars
2023, et il s'impose en juillet de la même année, avec un article de chercheurs de
laboratoires, d'universités et de centres de recherche, « *Frontier AI Regulation* ». Sa
définition d'origine ne parle pas seulement de performance : un modèle de frontière est
assez capable pour posséder des capacités dangereuses, qui feraient courir des risques
graves à la sécurité publique. Le terme sert aussitôt à organiser le secteur. Le même
mois, Anthropic, Google, Microsoft et OpenAI fondent le Frontier Model Forum, et en
novembre, le premier sommet mondial sur la sécurité de l'IA, à Bletchley Park, consacre
sa déclaration à l'« IA de frontière », comme le rappelle le chapitre
« [La géopolitique et la réglementation](docs/module5/64-la-geopolitique-et-la-reglementation/#une-gouvernance-mondiale) »
du Module 5.

Cette frontière se déplace vite. Selon Epoch AI, le calcul utilisé pour entraîner les
modèles de tête est multiplié par cinq environ chaque année, et seule une poignée de
laboratoires suit le rythme, américains comme OpenAI, Google DeepMind, Anthropic, xAI et
Meta, ou chinois comme DeepSeek et Alibaba. Les modèles ouverts suivent de près : en
2026, ils n'auraient plus qu'environ quatre mois de retard sur les meilleurs modèles
fermés, contre un an en 2024.

{{< image src="/images/module4/frontiere-calcul.svg" alt="Un nuage de points. L'axe horizontal donne la date de sortie, de 2018 à 2026, l'axe vertical le calcul utilisé pour l'entraînement, sur une échelle logarithmique, de 10 puissance 19 à 10 puissance 28 opérations. Chaque point est un modèle notable recensé par Epoch AI ; les modèles de frontière, en brun, montent régulièrement. On lit GPT-1 en 2018, GPT-3 en 2020, GPT-4 en 2023, Llama 3.1 405B, un modèle ouvert, en 2024, Grok 3, premier modèle au-delà de 10 puissance 26, en février 2025, et GPT-6 Astra en septembre 2026, proche de 10 puissance 27. Deux droites horizontales marquent les seuils : 10 puissance 25 opérations, celui de l'AI Act européen, et 10 puissance 26, celui des lois de la Californie et de New York. DeepSeek V3, un modèle ouvert sorti en décembre 2024 et proche des meilleurs modèles, reste sous le seuil européen." title="Le calcul d'entraînement des modèles notables recensés par Epoch AI. De GPT-1 à GPT-6 Astra, celui des modèles de frontière a été multiplié par plus de dix millions. Données : Epoch AI, octobre 2026." loading="lazy" >}}

Pour désigner ces modèles, les lois ont besoin d'un critère simple, et elles ont choisi la
quantité de calcul d'entraînement. L'AI Act européen présume qu'un modèle entraîné avec
plus de $10^{25}$ opérations présente un « risque systémique ». Les lois de la Californie, en
vigueur depuis janvier 2026, et de l'État de New York, à partir de 2027, visent les
modèles entraînés avec plus de $10^{26}$ opérations, et leurs obligations les plus lourdes,
les développeurs dont le chiffre d'affaires dépasse 500 millions de dollars. Selon les
estimations d'Epoch AI, Grok 3, de l'entreprise xAI, est le premier modèle à franchir ce
second seuil, en février 2025.

Ces seuils sont contestés. Le calcul n'est qu'un indicateur indirect des capacités, et les
gains d'efficacité l'en éloignent de plus en plus. DeepSeek V3, en décembre 2024,
approche les meilleurs modèles avec environ $3 \times 10^{24}$ opérations, sous le seuil européen,
et un modèle obtenu par
[distillation](docs/module4/60-passer-a-l-echelle/#la-distillation-un-grand-modèle-comme-professeur),
présentée plus loin dans ce chapitre, hérite des capacités de son professeur sans en avoir
dépensé le calcul. La chercheuse Sara Hooker, pourtant coautrice de l'article de 2023,
développe cette critique en 2024. Une autre critique vise le terme lui-même. Pour Andrew
Ng ou Yann Le Cun, insister sur les dangers des modèles de frontière sert les grandes
entreprises, seules capables d'assumer le coût des règles qu'elles réclament. On parle de
**capture réglementaire** (*regulatory capture*) quand une réglementation profite ainsi
aux entreprises qu'elle devait encadrer, comme le discute le chapitre
« [Peut-on perdre le contrôle ?](docs/module5/85-peut-on-perdre-le-controle/#le-catastrophisme-radical) »
du Module 5.

## Modèles fermés, modèles ouverts

Les modèles les plus puissants, ceux d'OpenAI, de Google ou d'Anthropic, sont
**fermés** : on peut les utiliser, mais leurs poids ne sont pas publiés, et on ne
connaît ni leur taille exacte ni leurs données d'entraînement. D'autres entreprises
publient les poids de leurs modèles, que chacun peut télécharger, étudier, ajuster et
faire tourner sur ses propres machines. On parle alors de modèles **ouverts**
(*open-weight models*).

- En février 2023, Meta publie LLaMA, puis plusieurs versions successives, jusqu'à
  Llama 3.1 et ses 405 milliards de paramètres en juillet 2024.
- En avril 2023, trois chercheurs français fondent Mistral AI, à Paris, qui publie
  plusieurs modèles ouverts.
- En janvier 2025, l'entreprise chinoise DeepSeek publie R1, un modèle ouvert dont les
  performances approchent celles des meilleurs modèles fermés, pour un coût
  d'entraînement annoncé bien plus faible. Le 27 janvier, la valeur boursière de
  Nvidia, le principal fabricant de processeurs graphiques, recule de près de
  600 milliards de dollars en une journée.
- En 2026, les modèles V4, puis V4.1, de DeepSeek rivalisent avec les meilleurs modèles
  fermés en programmation, pour quelques centimes par million de jetons, et DeepSeek
  publie en octobre le logiciel qui fait tourner ses propres services. Le chapitre
  « [La richesse et le pouvoir](docs/module5/54-la-richesse-et-le-pouvoir/#y-a-t-il-un-fossé-défensif) »
  du Module 5 examine ce que cette concurrence change pour les laboratoires fermés.

Le Canada a aussi son entreprise du domaine. Cohere est fondée à Toronto en 2019,
notamment par Aidan Gomez, l'un des auteurs de l'article de 2017 qui a présenté le
[Transformer](docs/module3/70-attention-transformer/#le-transformer), qu'il avait
coécrit pendant un stage chez Google alors qu'il étudiait à l'Université de Toronto.

## Ouvert, mais jusqu'où ?

L'expression « open source » vient du logiciel. En 1983, le programmeur Richard Stallman
lance le projet GNU, qui vise un système d'exploitation entièrement **libre** : chacun
doit pouvoir l'utiliser, l'étudier, le modifier et le redistribuer, ce qui suppose
l'accès à son **code source**, le texte du programme lisible par un humain. En 1991,
Linus Torvalds annonce le noyau Linux, héritier de la
[culture Unix](docs/module4/85-programmer-avec-des-agents/#la-culture-unix-des-outils-faits-pour-le-texte)
présentée plus loin dans ce module. En 1998, des partisans de ce mouvement adoptent
l'expression **code source ouvert** (*open source*), plus acceptable pour les entreprises,
et fondent l'Open Source Initiative, qui fixe dix critères qu'une licence doit remplir.
Le principe est simple : quiconque reçoit un logiciel ouvert peut le reconstruire et le
modifier à partir de son code source.

Un modèle d'IA ne se laisse pas décrire aussi simplement. Ses poids sont le résultat de
l'entraînement, pas sa recette. Publier les poids sans les données ni le code qui ont
servi à les produire, c'est un peu comme publier un programme déjà compilé sans son code
source : on peut s'en servir et l'ajuster, mais pas le refaire, ni vérifier vraiment ce
qu'il a appris. L'ouverture d'un modèle est donc une affaire de degrés.

- **Des poids, sous condition.** Les modèles Llama de Meta sont publiés avec une licence
  maison. Les entreprises de plus de 700 millions d'utilisateurs mensuels doivent obtenir
  une autorisation, que Meta accorde ou non, une politique d'usage interdit certaines
  applications, et depuis septembre 2024, les versions qui traitent les images sont
  refusées aux entreprises et aux personnes établies dans l'Union européenne. L'Open
  Source Initiative répète depuis 2023 que ces licences ne sont pas des licences libres.
- **Des poids vraiment libres.** D'autres publient leurs poids sous des licences libres
  classiques, comme Apache 2.0 ou MIT, qui autorisent tous les usages : de nombreux
  modèles de Mistral, de Qwen et de DeepSeek, et même deux modèles d'OpenAI, publiés en
  août 2025, ses premiers modèles ouverts depuis GPT-2. Les données et le code
  d'entraînement restent toutefois secrets.
- **Tout est publié.** Quelques modèles publient tout, les poids, le code et les données
  d'entraînement : la série OLMo de l'Allen Institute for AI, depuis 2024, ou Apertus,
  publié en septembre 2025 par les écoles polytechniques fédérales de Lausanne et de
  Zurich, entraîné sur des données dont les propriétaires pouvaient demander le retrait.
  Ce sont des modèles plus modestes que ceux des grands laboratoires, mais n'importe
  quel chercheur peut refaire leur entraînement.

En octobre 2024, l'Open Source Initiative publie une définition de l'**IA à code source
ouvert** (*open source AI*). Elle exige les poids, le code complet de l'entraînement, et
une description assez détaillée des données pour qu'une personne compétente puisse
entraîner un système équivalent, sans exiger les données elles-mêmes. Ce compromis est
critiqué par une partie du mouvement, pour qui un modèle sans ses données n'est pas
vraiment ouvert. Selon les essais de l'organisme, OLMo et Pythia satisfont la
définition ; Llama 2, Grok et Mixtral, non.

Le mot « ouvert » est devenu un argument de vente, au point que des chercheurs parlent
d'**ouverture de façade** (*open washing*) : présenter comme ouverts des modèles qui ne
le sont qu'en partie. L'enjeu n'est pas seulement d'image. L'AI Act européen allège
certaines obligations pour les modèles publiés sous une licence libre, à condition que
leurs poids soient publics, mais pas pour les modèles assez puissants pour présenter un
risque systémique. Et la tendance est plutôt au repli. Selon l'indice de transparence de
l'Université Stanford, la transparence moyenne des grands développeurs recule nettement
en 2025. En avril 2026, Meta, longtemps champion des modèles ouverts, sort Muse Spark,
son premier grand modèle dont les poids ne sont pas publiés, et d'autres laboratoires,
comme Alibaba avec Qwen, gardent désormais fermés leurs modèles les plus puissants tout
en ouvrant les autres. Le Module 5 revient sur ce que l'ouverture change pour
l'[économie](docs/module5/54-la-richesse-et-le-pouvoir/#y-a-t-il-un-fossé-défensif) et
pour les [risques de mésusage](docs/module5/85-peut-on-perdre-le-controle/#le-mésusage).

## La distillation : un grand modèle comme professeur

Les petits modèles les plus capables ne sont souvent pas entraînés seuls : ils
apprennent auprès d'un grand modèle, qui leur sert de professeur. C'est la
**distillation** (*knowledge distillation*). L'idée remonte à 2006, quand Cristian
Buciluă, Rich Caruana et Alexandru Niculescu-Mizil compressent un ensemble de centaines de
classifieurs en un seul petit réseau de neurones, entraîné à reproduire ses réponses.
Elle prend son nom en 2015, dans un article de Geoffrey Hinton, Oriol Vinyals et Jeff
Dean, chez Google.

Leur observation part d'un fait vu au Module 3 : un classifieur de chiffres manuscrits
ne répond pas seulement « c'est un 2 », il donne
[une probabilité pour chacun des dix chiffres](docs/module3/20-une-couche-cachee/#plus-de-neurones-plus-de-formes).
Devant un 2, un bon réseau est presque certain de sa réponse, mais il accorde aussi une
petite probabilité au 3 ou au 7, selon la façon dont le 2 est tracé. Ces petites
probabilités disent quels chiffres se ressemblent, une information que l'étiquette « 2 »
ne contient pas, et que Hinton appelle, dans ses conférences, la **connaissance sombre**
(*dark knowledge*). L'élève, un réseau plus petit, apprend donc à reproduire toute la
distribution du professeur, et non la seule bonne réponse. L'article en donne un exemple
frappant : un élève entraîné sans jamais voir un seul 3 en reconnaît ensuite 98,6 %,
après un simple réglage, parce que les probabilités du professeur lui en ont appris
la forme.

{{< image src="/images/module4/distillation.svg" alt="Deux panneaux, avec le même chiffre 2 manuscrit. À gauche, l'étiquette seule : un diagramme en barres sur les dix chiffres, avec une seule barre, toute la probabilité sur le 2. À droite, la réponse d'un grand réseau, le professeur : la barre du 2 domine, avec 0,80, mais le 3 reçoit 0,12 et le 7, 0,05, les autres chiffres presque rien. En bas : l'élève, un réseau plus petit, apprend à reproduire la distribution de droite, et y apprend aussi que ce 2 ressemble un peu à un 3, et un peu à un 7." title="La distillation. L'étiquette ne dit qu'une chose, « c'est un 2 ». Le professeur en dit davantage : ce 2 ressemble un peu à un 3, et un peu à un 7. L'élève apprend à reproduire toute cette distribution. Valeurs schématiques." loading="lazy" >}}

Avec les modèles de langage, la distillation devient une pièce centrale de la fabrication
des modèles.

- **Des modèles plus légers.** En 2019, DistilBERT, de l'entreprise Hugging Face, est 40 %
  plus petit et 60 % plus rapide que
  [BERT](docs/module4/50-predire-le-mot-suivant/#trois-façons-dassembler-le-transformer),
  et en conserve 97 % des capacités.
- **Imiter les textes d'un modèle fermé.** En mars 2023, des chercheurs de l'Université
  Stanford ajustent le petit modèle LLaMA de Meta sur 52 000 réponses produites par un
  modèle d'OpenAI, pour moins de 600 dollars. Leur modèle, Alpaca, rivalise avec son
  professeur dans leurs essais. Faute d'accès aux probabilités d'un modèle fermé, l'élève
  imite ici ses textes, comme dans
  l'[ajustement par instructions](docs/module4/70-du-modele-a-l-assistant/#imiter-de-bonnes-réponses).
- **Les petits modèles des grandes entreprises.** Google indique que ses modèles Gemma 2
  et Gemma 3, ainsi que ses modèles Gemini Flash, sont distillés de modèles plus grands.
  Meta entraîne en 2024 ses plus petits modèles Llama, de 1 et 3 milliards de paramètres,
  sur les probabilités de ses modèles de 8 et 70 milliards.
- **Distiller le raisonnement.** En janvier 2025, DeepSeek fait produire à son modèle R1
  environ 800 000 exemples de
  [raisonnements](docs/module4/70-du-modele-a-l-assistant/#des-modèles-qui-raisonnent-rlvr),
  qui servent à ajuster six modèles ouverts plus petits, de 1,5 à 70 milliards de
  paramètres. Celui de 32 milliards dépasse o1-mini, un modèle de raisonnement d'OpenAI,
  sur la plupart des tests. Les auteurs constatent aussi que, pour un modèle de cette
  taille, la distillation donne de bien meilleurs résultats que l'apprentissage par
  renforcement mené directement sur lui.

La distillation a une conséquence qui dépasse la technique. Un modèle de pointe sert,
qu'il le veuille ou non, de professeur à tous ceux qui peuvent l'interroger, y compris
ses concurrents. Les conditions d'utilisation d'OpenAI interdisent, depuis au moins 2023,
d'utiliser ses réponses pour développer un modèle concurrent, et le Module 5 raconte
comment la question est devenue, en 2026, une affaire de
[géopolitique](docs/module5/64-la-geopolitique-et-la-reglementation/#une-course-entre-deux-puissances).

## Ce que coûte une réponse

L'entraînement se paie une fois ; l'utilisation, à chaque réponse. Les entreprises
facturent leurs modèles au jeton, lu ou écrit. À sa sortie, en mars 2023, GPT-4
coûtait 30 dollars par million de jetons lus. En juillet 2024, GPT-4o mini, un modèle
plus petit et déjà très capable, en coûtait 15 cents. Selon Epoch AI, le prix pour
obtenir un même niveau de performance baisse de dix à plusieurs centaines de fois par
an selon la tâche. Plusieurs techniques y contribuent.

- **Le mélange d'experts** (*mixture of experts*). Le modèle est découpé en de nombreux
  sous-réseaux, les « experts », et un petit réseau d'aiguillage choisit pour chaque
  jeton les quelques experts qui le traiteront. DeepSeek-V3, publié en décembre 2024,
  compte 671 milliards de paramètres, mais n'en utilise que 37 milliards pour chaque
  jeton. C'est l'une des raisons de son faible coût : environ 5,6 millions de dollars
  pour son dernier entraînement, selon ses auteurs, sans compter les essais qui l'ont
  précédé.
- **La quantification** (*quantization*). Chaque paramètre est stocké avec moins de
  précision, par exemple sur 4 bits au lieu de 16. Le modèle occupe alors quatre fois
  moins de mémoire, et perd peu en qualité : un modèle de 7 milliards de paramètres
  passe d'environ 14 à 4 gigaoctets, et tient dans un ordinateur portable.
- **Les petits modèles.** Des modèles de quelques milliards de paramètres, souvent
  obtenus par [distillation](#la-distillation-un-grand-modèle-comme-professeur)
  d'un grand modèle, tournent directement sur un téléphone, comme celui qu'Apple
  intègre à ses appareils en 2024, ou les plus petits modèles Llama de Meta.

Cette baisse des prix rend possibles des usages qui consomment beaucoup de jetons,
comme les [agents](docs/module4/80-outils-et-agents/#des-agents-un-modèle-et-son-harnais-en-boucle)
ou les modèles qui réfléchissent longtemps avant de répondre. Elle ne fait pas baisser
pour autant la consommation totale d'énergie du secteur, puisque les usages se
multiplient, une question que reprend le [Module 5](docs/module5).

## Jusqu'où ?

Les lois d'échelle décrivent une tendance, pas une loi de la nature, et elles reposent
sur deux ressources limitées, le calcul et les données. Les textes de qualité se
raréfient, comme l'a montré la section
« [Le prix de la taille](docs/module4/60-passer-a-l-echelle/#le-prix-de-la-taille) ».

À l'automne 2024, plusieurs médias rapportent que les gains obtenus en agrandissant les
modèles diminuent. Selon le site *The Information*, le modèle suivant d'OpenAI, nommé
Orion, atteint le niveau de GPT-4 dès le cinquième de son entraînement, mais le dépasse
ensuite beaucoup moins que GPT-4 ne dépassait GPT-3. L'agence Bloomberg décrit des
difficultés semblables chez Google et Anthropic. En décembre, à la conférence NeurIPS,
Ilya Sutskever, cofondateur d'OpenAI, annonce la fin du pré-entraînement « tel que nous
le connaissons » : les données sont, selon lui, le « combustible fossile » de l'IA, et
« nous n'avons qu'un seul Internet ». Le modèle d'OpenAI sort en février 2025 sous le
nom de GPT-4.5. Il aurait demandé environ dix fois plus de calcul que GPT-4 et coûte
75 dollars par million de jetons lus, pour des gains jugés modestes. OpenAI cesse de
l'offrir aux développeurs dès juillet.

Les laboratoires misent alors sur deux autres façons de dépenser du calcul, qui ont
elles aussi leurs lois d'échelle. La première est l'**apprentissage par renforcement**
à grande échelle, qui entraîne un modèle déjà pré-entraîné à résoudre des problèmes dont
on peut vérifier la réponse. En septembre 2024, OpenAI montre que la justesse de son
modèle o1 augmente régulièrement avec le calcul consacré à ce renforcement. En avril
2025, o3 en utilise dix fois plus, et en juillet, xAI dit avoir mené celui de Grok 4
« à l'échelle du pré-entraînement ». La seconde est le calcul au moment de la réponse :
on laisse le modèle « réfléchir » plus longtemps avant de répondre. Le chapitre suivant
présente ces
[modèles de raisonnement](docs/module4/70-du-modele-a-l-assistant/#des-modèles-qui-raisonnent-rlvr).
Le renforcement a toutefois ses limites. En 2025, le philosophe Toby Ord et Epoch AI
estiment qu'il rapporte peu par unité de calcul, et que son budget, qui approche déjà
celui du pré-entraînement, ne pourra pas croître longtemps au même rythme.

{{< image src="/images/module4/trois-leviers.svg" alt="Une frise de 2018 à 2026 avec trois bandes horizontales, dont l'épaisseur indique, de façon schématique, la place de chaque levier dans l'effort des laboratoires. Première bande, agrandir le pré-entraînement, le modèle et ses données : épaisse dès le départ, avec GPT-2 en 2019, les lois d'échelle de Kaplan et GPT-3 en 2020, Chinchilla en 2022 et GPT-4 en 2023 ; à partir de la fin de 2024, la bande est hachurée, les rendements sont discutés, avec GPT-4.5 en février 2025 et GPT-6 Astra en septembre 2026. Deuxième bande, l'apprentissage par renforcement : un mince filet à partir de 2022, celui des préférences humaines, qui s'élargit à partir de o1, en septembre 2024, avec DeepSeek R1, o3 et Grok 4 en 2025. Troisième bande, réfléchir plus longtemps, le calcul au moment de la réponse : absente jusqu'à o1, puis de plus en plus large, avec o3 et le test ARC. Au-dessus, la périodisation d'Ilya Sutskever : l'âge de la recherche jusqu'en 2020, l'âge de l'échelle de 2020 à 2025, puis un retour à la recherche." title="Trois façons de dépenser plus de calcul. Jusqu'en 2024, on agrandit surtout le pré-entraînement ; depuis, le renforcement et le temps de réflexion prennent une place croissante. L'épaisseur des bandes est schématique." loading="lazy" >}}

Le pré-entraînement n'a pas dit son dernier mot. En novembre 2025, Oriol Vinyals, de
Google DeepMind, attribue les progrès de Gemini 3 au pré-entraînement autant qu'au
post-entraînement, et n'y voit « aucun mur en vue ». Le même mois, Sutskever résume la
période en trois âges : de 2012 à 2020, « l'âge de la recherche », de 2020 à 2025,
« l'âge de l'échelle », et désormais un retour à la recherche, « avec de gros
ordinateurs ». En septembre 2026, GPT-6 Astra, le plus grand entraînement d'OpenAI,
aurait demandé près de $10^{27}$ opérations selon Epoch AI, sans qu'on sache quelle part
en revient au pré-entraînement et au renforcement. Le débat n'est donc pas tranché.
L'échelle continue de payer, mais elle n'est plus le seul levier, et la recherche de
méthodes plus efficaces est redevenue centrale.

Le [chapitre suivant](docs/module4/70-du-modele-a-l-assistant) montre comment un modèle
qui complète du texte devient un assistant qui répond, puis un modèle qui raisonne.
