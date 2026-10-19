---
title: "Quels problèmes l'IA pose-t-elle ?"
weight: 10
slug: quels-problemes
---

# Quels problèmes l'IA pose-t-elle ?

Les quatre premiers modules ont expliqué comment fonctionnent les systèmes d'IA : les
règles et la recherche de l'IA classique, l'apprentissage à partir de données, les
réseaux de neurones, puis les modèles qui génèrent du texte et des images. Ce dernier
module change de question. Il ne demande plus comment ces systèmes fonctionnent, mais
quels problèmes ils posent.

La question n'a rien d'abstrait. En février 2026, OpenAI annonce que ChatGPT compte plus
de 900 millions d'utilisateurs chaque semaine. Au même moment, l'inquiétude grandit. En
juin 2026, 52 % des Américains se disent plus inquiets qu'enthousiastes devant l'IA,
contre 37 % en 2021, et environ un sur dix seulement se dit plus enthousiaste
qu'inquiet. Au Canada, en août 2025, deux personnes sur trois jugent « effrayante » la
perspective de l'IA dans leur vie. Beaucoup de gens s'en servent tous les jours, et s'en
inquiètent en même temps.

Derrière cette inquiétude se cachent pourtant des problèmes de natures très
différentes. Se demander si une machine peut comprendre ce qu'elle dit, si elle va
supprimer des emplois ou combien d'électricité elle consomme, ce n'est pas poser le même
genre de question, et on n'y répond pas de la même façon. Ce module les distingue, puis
les parcourt une à une.

## Neuf familles de problèmes

Le tableau suivant regroupe les problèmes que pose l'IA en neuf familles. Chacune
rassemble des questions d'un même genre, qui appellent le même genre de réponse :
un argument philosophique, une expérience scientifique, un jugement moral, une étude
économique, une loi.

|  | Famille | Quelques questions |
|---|---|---|
| ![](/images/module5/icones/philosophique.svg) | **Philosophique** | Une machine peut-elle penser, comprendre, être consciente ? Qu'est-ce que l'intelligence ? Penser, est-ce calculer ? |
| ![](/images/module5/icones/scientifique.svg) | **Scientifique** | Que peut apporter l'IA à la science ? Peut-on se fier à un modèle qui prédit sans expliquer ? |
| ![](/images/module5/icones/morale.svg) | **Morale** | Qui est responsable d'une décision prise par une machine ? Une décision automatisée peut-elle être juste ? Sur quelles valeurs aligner l'IA ? Une IA peut-elle avoir un statut moral ? |
| ![](/images/module5/icones/economique.svg) | **Économique** | L'IA va-t-elle supprimer des emplois, en créer, en transformer ? Qui profitera de la richesse qu'elle produit ? |
| ![](/images/module5/icones/juridique.svg) | **Juridique** | À qui appartient une œuvre générée ? A-t-on le droit d'entraîner un modèle sur des œuvres protégées ? |
| ![](/images/module5/icones/sociale.svg) | **Sociale et politique** | L'IA menace-t-elle la vérité et la démocratie ? La vie privée ? Qui contrôle la technologie, et quels pays ? |
| ![](/images/module5/icones/environnementale.svg) | **Environnementale** | Combien d'énergie, d'eau et de matériaux l'IA consomme-t-elle ? Peut-elle aider à protéger l'environnement ? |
| ![](/images/module5/icones/humaine.svg) | **Humaine** | Que fait l'IA à notre façon de penser, d'apprendre, de créer, de nous lier aux autres ? |
| ![](/images/module5/icones/risques.svg) | **Risques extrêmes** | Pourrait-on perdre le contrôle de systèmes plus capables que nous ? L'IA pourrait-elle servir à une catastrophe ? |

Aucune de ces familles n'est nouvelle pour vous. Chacune a été annoncée, au moins une
fois, dans les modules précédents.

- **Philosophique.** Le Module 1 a présenté le [test de Turing](docs/module1/10-turing/#le-jeu-de-limitation),
  l'objection de Penrose fondée sur le [théorème de Gödel](docs/module1/10-turing/#lombre-de-gödel) et
  l'[illusion de comprendre](docs/module1/30-chercher-raisonner/#lautre-visage-eliza-ou-lillusion-de-comprendre)
  que produisait déjà ELIZA. Le Module 4 s'est demandé
  [ce que les LLM comprennent](docs/module4/94-comprendre-et-rater/#perroquets-ou-modèles-du-monde),
  ce que changent les [machines qui démontrent](docs/module4/87-demontrer), et ce que
  l'on trouve en [regardant à l'intérieur](docs/module4/93-regarder-a-l-interieur) des
  modèles.
- **Scientifique.** Le Module 3 a présenté [AlphaFold](docs/module3/70-attention-transformer/#au-delà-du-texte),
  le Module 4 les [modèles de prévision météorologique](docs/module4/30-images-voix-videos/#au-delà-des-médias),
  et le Module 2 la différence entre
  [corrélation et causalité](docs/module2/75-bien-evaluer/#corrélation-nest-pas-causalité).
- **Morale.** Le Module 2 opposait la performance à l'[explicabilité](docs/module2/65-arbres-de-decision/#ce-quun-arbre-dit-et-ce-quil-tait),
  le Module 3 montrait un agent qui [détourne sa récompense](docs/module3/80-renforcement-profond/#au-delà-des-jeux-et-les-limites),
  et le Module 4 posait la question de la responsabilité des
  [agents](docs/module4/80-outils-et-agents/#des-agents-un-modèle-et-son-harnais-en-boucle).
- **Économique.** Le Module 4 a décrit le [travail humain](docs/module4/70-du-modele-a-l-assistant/#le-travail-humain-derrière-lassistant)
  derrière les assistants et ce que les [agents de programmation](docs/module4/85-programmer-avec-des-agents/#programmer-autrement)
  changent au métier de programmeur.
- **Juridique.** Le Module 4 a présenté les premiers [litiges sur les œuvres générées](docs/module4/30-images-voix-videos/#les-images)
  et les [procès pour droit d'auteur](docs/module4/60-passer-a-l-echelle/#le-prix-de-la-taille).
- **Sociale et politique.** On a croisé les [biais des données](docs/module2/75-bien-evaluer/#jamais-vu-mais-du-même-monde-la-question-de-la-distribution),
  la [reconnaissance faciale](docs/module3/50-reseaux-convolutifs), la course aux
  [processeurs graphiques](docs/module3/42-materiel-et-outils/#les-processeurs-graphiques)
  et les [hypertrucages](docs/module4/30-images-voix-videos/#les-hypertrucages).
- **Environnementale.** Le Module 4 a chiffré le [coût énergétique](docs/module4/60-passer-a-l-echelle/#le-prix-de-la-taille)
  de l'entraînement et de l'usage des grands modèles.
- **Humaine.** Le Module 4 a décrit l'[illusion de comprendre](docs/module4/94-comprendre-et-rater/#lillusion-de-comprendre)
  que produisent les assistants, et la nécessité de savoir encore lire le code qu'écrit
  un agent.
- **Risques extrêmes.** Le Module 3 rappelait les avertissements de
  [Geoffrey Hinton](docs/module3/40-apprentissage-profond/#2012-le-concours-imagenet),
  et le Module 4 décrivait les [incidents de 2026](docs/module4/85-programmer-avec-des-agents/#permissions-bac-à-sable-et-incidents),
  où des agents sont sortis de leur bac à sable.

## Des problèmes qui se recoupent

Ces familles ne sont pas des cases étanches. Une même question en touche souvent
plusieurs. Les [hypertrucages](docs/module4/30-images-voix-videos/#les-hypertrucages),
ces vidéos ou ces voix truquées qui imitent une personne réelle, en sont un bon exemple :

- un problème **social et politique**, puisqu'ils peuvent tromper des électeurs ;
- un problème **moral**, puisqu'ils servent à humilier ou à harceler, souvent des femmes ;
- un problème **juridique**, puisqu'il faut décider qui est responsable, de la personne
  qui les fabrique, de l'outil ou de la plateforme qui les diffuse ;
- un problème **humain**, puisqu'à force de croiser des images truquées, on peut finir
  par ne plus croire aucune image, même vraie.

Ce module traite chaque question là où elle se pose le plus nettement, et signale les
recoupements par des liens.

## Des faits et des valeurs

Les problèmes de ces neuf familles mêlent deux sortes de questions. Le philosophe
Charles Stevenson les distinguait en 1944 dans *Ethics and Language*. Les unes portent
sur ce qui est : combien d'emplois l'IA supprimera, combien d'électricité elle
consomme, à quelle vitesse elle progressera. On peut en principe les trancher par des
observations, même si les réponses sont souvent encore inconnues. Les autres portent
sur ce que l'on souhaite : ce qui doit compter le plus, pour qui, et quels risques on
accepte de courir. Aucune étude ne suffit à les trancher.

Beaucoup de débats sur l'IA restent confus parce qu'on mêle ces deux sortes de
questions. Deux personnes peuvent s'opposer sur une conclusion, par exemple faut-il
freiner l'IA, tout en s'accordant sur les faits, parce qu'elles ne donnent pas le même
poids aux mêmes choses. Deux autres peuvent partager les mêmes valeurs et s'opposer
parce que l'une juge l'IA surestimée et l'autre non. Pour chaque problème, ce module
sépare donc, autant que possible, ce que l'on sait, ce que l'on ignore encore, et ce
qui relève d'un choix.

## Comment lire ce module

Chaque chapitre suit à peu près la même démarche. Il présente un problème, ce que l'on
en sait aujourd'hui, puis les principales positions, avec leurs arguments. Il ne
tranche pas : le but est de vous donner de quoi juger par vous-même.

Au fil des chapitres, des façons typiques de réagir à l'IA se dessinent : on retrouve
souvent les mêmes personnes, les mêmes groupes et les mêmes arguments d'un problème à
l'autre. Plutôt que de les présenter d'avance comme des camps, le module les laisse apparaître, et les rassemble dans une [synthèse finale](docs/module5/90-les-attitudes-devant-l-ia) : ces attitudes s'expliquent en
grande partie par les problèmes que chacun juge les plus importants, et par ce qu'il
croit sur les faits.
