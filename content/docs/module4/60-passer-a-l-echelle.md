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
de **lois d'échelle** (*scaling laws*).

{{< image src="/images/module4/loi-d-echelle.svg" alt="Un schéma. L'axe horizontal donne la quantité de calcul utilisée pour l'entraînement, l'axe vertical l'erreur du modèle sur des textes qu'il n'a jamais vus, tous deux sur une échelle logarithmique. Des points, un par modèle entraîné, s'alignent sur une droite qui descend régulièrement. La droite est prolongée en pointillé vers la droite : on peut prédire l'erreur d'un modèle plus grand avant de l'entraîner." title="Le principe d'une loi d'échelle (schéma) : en prolongeant la droite, on prévoit l'erreur d'un modèle plus grand avant de l'entraîner." loading="lazy" >}}

Ces lois ont une conséquence pratique. Avant de dépenser des dizaines de millions de
dollars pour entraîner un très grand modèle, on peut entraîner une série de petits
modèles, tracer la droite, et prévoir le résultat. Elles confirment aussi la
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

Cette capacité s'appelle l'**apprentissage en contexte** (*in-context learning*). On
distingue la requête sans exemple (*zero-shot*), avec un seul exemple (*one-shot*) et
avec quelques exemples (*few-shot*). Elle est très différente de l'apprentissage
présenté au [Module 2](docs/module2/50-entrainer-un-modele) : aucun poids du modèle
n'est modifié. Le modèle reconnaît la tâche dans le texte qu'on lui donne, et ses
performances augmentent avec sa taille. GPT-3 réussit de nombreuses tâches de cette
façon, alors que les modèles plus petits n'y parviennent presque pas. La rédaction des
requêtes est devenue une compétence à part entière, présentée au chapitre du
[Module 4](docs/module4/80-outils-et-agents/#formuler-la-requête) sur les outils et les agents.

## Des capacités qui apparaissent ?

En 2022, Jason Wei et ses collègues, chez Google, décrivent des **capacités
émergentes** (*emergent abilities*). Sur certaines tâches, comme l'addition de nombres
de plusieurs chiffres ou certaines énigmes, les petits modèles échouent presque
complètement, puis, au-delà d'une certaine taille, les modèles réussissent soudain.
La capacité semble apparaître d'un coup, sans avoir été annoncée par les modèles
plus petits. L'idée a frappé les esprits, car elle suggère que des modèles plus
grands pourraient acquérir des capacités imprévisibles.

En 2023, Rylan Schaeffer et ses collègues, à l'Université Stanford, contestent cette
interprétation. Selon eux, l'apparition soudaine vient souvent de la façon de mesurer.
Si l'on compte une addition comme réussie seulement quand tous les chiffres sont
exacts, la note passe brusquement de 0 à 1. Si l'on compte les chiffres exacts un par
un, le progrès est régulier. Le débat n'est pas tranché : certaines capacités semblent
bien apparaître de façon abrupte, d'autres sont des effets de mesure.

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
entreprises se tournent donc vers des **données synthétiques**, produites par d'autres
modèles, et vers des textes sous licence. Le recours aux textes protégés par le droit
d'auteur fait l'objet de nombreux procès, comme celui que le *New York Times* a
intenté à OpenAI et à Microsoft en décembre 2023. Le [Module 5](docs/module5) revient
sur ces coûts environnementaux et juridiques.

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

Le Canada a aussi son entreprise du domaine. Cohere est fondée à Toronto en 2019,
notamment par Aidan Gomez, l'un des auteurs de l'article de 2017 qui a présenté le
[Transformer](docs/module3/70-attention-transformer/#le-transformer), qu'il avait
coécrit pendant un stage chez Google alors qu'il étudiait à l'Université de Toronto.

## Jusqu'où ?

Les lois d'échelle décrivent une tendance, pas une loi de la nature. À partir de 2024,
plusieurs observateurs constatent que les gains obtenus en agrandissant seulement les
modèles diminuent, et que les données de qualité se raréfient. Les entreprises
explorent alors une autre direction : consacrer davantage de calcul non plus à
l'entraînement, mais au moment de répondre, en laissant le modèle « réfléchir » plus
longtemps avant de donner sa réponse. Ces modèles de raisonnement sont présentés au
[chapitre suivant](docs/module4/70-du-modele-a-l-assistant), qui montre aussi comment un modèle qui complète du
texte devient un assistant qui répond.
