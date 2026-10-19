---
title: "Le coût écologique de l'IA"
weight: 70
slug: le-cout-ecologique
---

# Le coût écologique de l'IA

Une requête à un assistant semble immatérielle. Elle passe pourtant par des centres de
données qui consomment de l'électricité, de l'eau et des métaux, et dont la construction
s'accélère. Ce chapitre, consacré à la famille des
[problèmes environnementaux](docs/module5/10-quels-problemes/#neuf-familles-de-problèmes),
cherche à mesurer ce coût, sans l'exagérer ni le minimiser, et à le comparer à ce que l'IA
peut apporter à l'environnement.

## L'électricité

Le Module 4 a présenté, dans « [Passer à l'échelle](docs/module4/60-passer-a-l-echelle/#le-prix-de-la-taille) »,
le coût énergétique de l'entraînement des grands modèles. À l'échelle mondiale, les ordres
de grandeur sont les suivants.

- Selon l'Agence internationale de l'énergie, les centres de données ont consommé environ
  415 térawattheures d'électricité en 2024, soit environ 1,5 % de l'électricité mondiale,
  autant qu'un pays comme la France. Leur consommation augmente de 17 % en 2025, bien plus
  vite que celle de l'électricité en général, et devrait doubler d'ici 2030. L'IA est le
  principal moteur de cette croissance.
- Aux États-Unis, qui comptent pour près de la moitié du total, les centres de données
  consommaient 4,4 % de l'électricité du pays en 2023, et pourraient en consommer de 6,7 à
  12 % en 2028.

## Le coût d'une requête

Rapporté à une seule requête, le coût paraît minime. En août 2025, Google estime qu'une
requête textuelle médiane à son assistant Gemini consomme 0,24 wattheure, l'équivalent de
moins de neuf secondes de télévision, et environ 0,26 millilitre d'eau, quelques gouttes.
Selon l'entreprise, cette consommation par requête a été divisée par 33 en un an. En juin
2025, Sam Altman avance un chiffre comparable pour ChatGPT, 0,34 wattheure, sans en
préciser la méthode. En juillet 2025, l'entreprise française Mistral publie une analyse du
cycle de vie de son modèle : environ 1,14 gramme d'équivalent CO₂ et 45 millilitres d'eau
par réponse, en comptant cette fois la fabrication des serveurs.

Ces chiffres, publiés par les entreprises elles-mêmes, ne comptent pas toujours la même
chose. Ils excluent souvent l'entraînement, le réseau ou les appareils des utilisateurs,
et ils portent sur des requêtes simples, alors que les
[modèles qui raisonnent](docs/module4/70-du-modele-a-l-assistant/#des-modèles-qui-raisonnent-rlvr)
et les [agents](docs/module4/80-outils-et-agents/#des-agents-un-modèle-et-son-harnais-en-boucle)
consomment beaucoup plus, puisqu'ils produisent des milliers de jetons pour une seule
tâche. Le coût d'une requête est faible ; ce qui pèse, c'est leur nombre, des milliards par
jour.

## L'eau

Les centres de données sont refroidis, souvent avec de l'eau qui s'évapore, et les centrales
qui les alimentent en consomment aussi. En 2023, des chercheurs de l'Université de
Californie à Riverside estiment que l'entraînement de GPT-3 a fait évaporer directement
environ 700 000 litres d'eau douce. Ils prévoient que l'IA pourrait prélever, en 2027, de
4,2 à 6,6 milliards de mètres cubes d'eau dans le monde, dont une partie seulement serait
réellement consommée, le reste retournant aux cours d'eau. Le problème est d'abord local :
un centre de données installé dans une région déjà sèche entre en concurrence avec les
habitants et l'agriculture.

## Des engagements climatiques qui reculent

Les grandes entreprises technologiques s'étaient engagées à atteindre la neutralité
carbone. L'IA rend ces engagements plus difficiles à tenir.

- Les émissions de Google augmentent de 51 % entre 2019 et 2024, selon sa propre mesure,
  et l'entreprise reconnaît en 2026 que son objectif climatique « devient plus difficile »
  à atteindre, sa consommation d'électricité ayant augmenté de 37 % en une seule année.
- Les émissions totales de Microsoft dépassent en 2024 de 23 % leur niveau de 2020, malgré
  la promesse de devenir « carbone négatif » en 2030, et augmentent encore de 25 % l'année
  suivante.
- Pour alimenter leurs centres de données, les entreprises se tournent vers le nucléaire.
  En 2024, Microsoft signe un contrat pour relancer un réacteur de la centrale de Three
  Mile Island, en Pennsylvanie, à partir de 2028, et Google et Amazon investissent dans de
  petits réacteurs modulaires, attendus au début des années 2030. En attendant, beaucoup
  de centres de données fonctionnent au gaz.

Les effets sont aussi locaux. À Memphis, l'entreprise xAI d'Elon Musk alimente son
superordinateur Colossus avec des dizaines de turbines au gaz, installées d'abord sans
permis, dans un quartier ouvrier à majorité noire déjà touché par la pollution. En 2026, des associations de défense des droits civiques poursuivent l'entreprise pour une autre centrale au gaz, construite pour son deuxième superordinateur.

## L'effet rebond

On pourrait espérer que les progrès de l'efficacité réduisent le problème. L'histoire de
l'énergie suggère le contraire. Au XIXᵉ siècle, l'économiste William Stanley Jevons
remarquait que des machines à vapeur plus efficaces n'avaient pas réduit la consommation
de charbon : en rendant son usage moins cher, elles l'avaient multipliée. C'est le
**paradoxe de Jevons**, ou **effet rebond**. En janvier 2025, après la sortie du modèle
DeepSeek, beaucoup moins coûteux, le dirigeant de Microsoft, Satya Nadella, l'invoque
lui-même : plus l'IA deviendra efficace et accessible, plus on s'en servira. Le chapitre
« [Passer à l'échelle](docs/module4/60-passer-a-l-echelle/#ce-que-coûte-une-réponse) » du
Module 4 en a donné un exemple : le prix d'une réponse s'effondre, et la consommation
totale augmente.

## Le Québec

Le Québec, qui produit une électricité abondante, peu chère et presque entièrement
renouvelable grâce à l'hydroélectricité, attire les centres de données. Cette électricité
n'est pourtant pas illimitée, et chaque mégawatt accordé à un centre de données n'est plus
disponible pour électrifier les transports, l'industrie ou le chauffage, comme l'exige la
transition énergétique. Depuis 2023, le gouvernement doit autoriser les nouveaux
raccordements de grande puissance, ce qui en fait un choix politique : il faut décider si l'IA est un meilleur usage de l'hydroélectricité québécoise que la décarbonation d'autres secteurs.

## Ce que l'IA peut apporter

L'IA peut aussi aider l'environnement.

- En 2016, DeepMind réduit de 40 % l'énergie consacrée au refroidissement des centres de
  données de Google, grâce à un système d'apprentissage automatique.
- Les [modèles de prévision météorologique](docs/module5/30-l-ia-au-service-de-la-science/#au-delà-des-protéines)
  présentés au chapitre « L'IA au service de la science » consomment environ mille fois
  moins d'énergie par prévision que les modèles physiques classiques, et aident à prévoir
  les événements extrêmes.
- L'IA sert à optimiser les réseaux électriques, à concevoir des matériaux pour les
  batteries ou à suivre la déforestation par satellite.

L'Agence internationale de l'énergie note toutefois, en 2026, que la consommation d'énergie
de l'IA progresse plus vite que le déploiement de ses applications climatiques. Le bilan
dépend moins de la technologie que de ce que l'on choisit d'en faire : des milliards de
requêtes de divertissement ne pèsent pas comme une prévision météorologique qui sauve des
vies.
