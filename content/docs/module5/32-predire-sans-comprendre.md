---
title: "Prédire sans comprendre"
weight: 32
slug: predire-sans-comprendre
---

# Prédire sans comprendre

Le chapitre « [L'IA au service de la science](docs/module5/30-l-ia-au-service-de-la-science) »
a montré ce que l'IA apporte à la recherche. Ce chapitre pose une question plus
ancienne, que ces succès rendent pressante : que vaut une prédiction juste, si personne
ne comprend pourquoi elle est juste ? La science a longtemps cherché à la fois à
prédire et à expliquer. L'IA permet, de plus en plus souvent, de faire l'un sans
l'autre.

## « La fin de la théorie »

En juin 2008, Chris Anderson, rédacteur en chef du magazine *Wired*, publie un essai
provocateur intitulé « *The End of Theory* » (la fin de la théorie). Sa thèse : avec des
quantités énormes de données, on n'a plus besoin de modèles ni de théories. « La
corrélation suffit », écrit-il ; les nombres parlent d'eux-mêmes. Il cite Google
Traduction, qui traduisait sans rien savoir de la grammaire, ou le séquençage massif de
l'ADN, qui découvrait de nouvelles espèces sans rien savoir de leur biologie.

{{< image src="/images/module5/portraits/anderson.jpg" alt="Portrait de Chris Anderson." title="Chris Anderson en 2011." class="portrait" loading="lazy" >}}

<p class="image-credit">Chris Anderson en 2011. Photo : Campus Party Brasil, <a href="https://creativecommons.org/licenses/by-sa/2.0">CC BY-SA 2.0</a>, via Wikimedia Commons.</p>

L'idée n'était pas neuve. En 2001, le statisticien Leo Breiman opposait déjà **deux
cultures** de la modélisation. La première, majoritaire chez les statisticiens,
suppose un modèle des données, une équation qui décrit comment elles sont produites, et
cherche à en estimer les paramètres. La seconde traite le mécanisme comme inconnu, et
cherche seulement l'algorithme qui prédit le mieux. C'est la culture de
l'[apprentissage automatique](docs/module2/50-entrainer-un-modele), et Breiman la jugeait
déjà plus efficace. Il en voyait aussi le prix : les modèles qui prédisent le mieux,
comme les forêts aléatoires, sont aussi ceux que l'on comprend le moins.

## Corrélation et causalité

La réponse classique à la « fin de la théorie » tient en une phrase du Module 2 :
[corrélation n'est pas causalité](docs/module2/75-bien-evaluer/#corrélation-nest-pas-causalité).
Un modèle peut prédire très bien qu'un patient qui a reçu tel traitement guérira, sans
que le traitement soit la cause de la guérison, parce que les médecins le donnent aux
patients qui avaient déjà de meilleures chances. Pour décider s'il faut donner le
traitement, il faut savoir ce qui arriverait si on le donnait, et la seule corrélation ne
le dit pas.

Le chercheur Judea Pearl, prix Turing 2011 pour ses travaux sur le
[raisonnement probabiliste et causal](docs/module2/60-classer/#raisonner-sous-incertitude-les-réseaux-bayésiens),
propose en 2018 une **échelle de la causalité** à trois barreaux.

{{< image src="/images/module5/portraits/pearl.jpg" alt="Judea Pearl, lunettes et cravate, parle devant une affiche scientifique couverte de graphes causaux." title="Judea Pearl en 2013, devant une affiche sur les modèles graphiques et les données manquantes." class="portrait" loading="lazy" >}}

<p class="image-credit">Judea Pearl en 2013, devant une affiche sur les modèles graphiques et les données manquantes. Photo : Better Than Bacon, <a href="https://creativecommons.org/licenses/by/2.0">CC BY 2.0</a>, via Wikimedia Commons.</p>

1. **L'association** : observer que deux choses vont ensemble. C'est ce que fait la
   prédiction.
2. **L'intervention** : savoir ce qui arrive si l'on agit. C'est ce que mesure une
   expérience contrôlée.
3. **Le contrefactuel** : imaginer ce qui serait arrivé si l'on avait agi autrement.
   C'est ce que demandent la responsabilité, le regret ou l'explication.

Pour Pearl, l'apprentissage automatique, aussi puissant soit-il, reste sur le premier
barreau. Les grands modèles de langage semblent en partie le démentir : en 2023, des
chercheurs de Microsoft montrent que GPT-4 répond juste à la plupart des questions de
causalité tirées de manuels. Mais une autre étude, la même année, leur demande de tirer
des conclusions causales à partir d'énoncés de corrélations, et ils répondent à peu près
au hasard. Les modèles semblent avoir appris ce que les textes disent des causes, plus
qu'une façon de les déduire.

## Prédire n'est pas comprendre

Le cas des planètes illustre bien la différence. Pendant plus d'un millénaire, le système
de Ptolémée, avec ses cercles qui tournent sur d'autres cercles, les **épicycles**,
prédisait les positions des planètes avec une bonne précision. Kepler, puis Newton, ne
l'ont pas remplacé parce qu'il prédisait mal, mais parce que leur théorie expliquait
tout avec une seule loi, la gravitation, qui valait aussi pour la chute d'une pomme.

En 2025, des chercheurs de Harvard et du MIT reprennent l'exemple pour tester un
Transformer. Ils l'entraînent sur des millions de systèmes solaires simulés, et le
modèle apprend à prédire la position suivante des planètes avec une précision presque
parfaite. Mais quand ils lui demandent de calculer les forces en jeu, il produit, d'un
système à l'autre, des lois différentes et absurdes, au lieu de la loi de Newton. Le
modèle prédit comme Ptolémée, sans avoir trouvé ce qu'a trouvé Newton. C'est la question
du [modèle du monde](docs/module4/94-comprendre-et-rater/#perroquets-ou-modèles-du-monde)
du Module 4, posée avec précision.

AlphaFold soulève la même question. Il prédit la forme finale d'une protéine, mais une
étude de 2022 montre que les chemins de repliement qu'on peut en tirer ne correspondent
pas à ceux que l'on observe en laboratoire : il ne dit rien, ou presque, de la façon dont
la protéine se replie. Ces prédictions sont extrêmement utiles, mais elles ne remplacent
pas une théorie du repliement.

## Quand la prédiction se trompe

Une prédiction sans compréhension a aussi un risque plus prosaïque : on ne sait pas
quand elle se trompe. En 2023, Sayash Kapoor et Arvind Narayanan recensent 294 articles
scientifiques, dans dix-sept disciplines, dont les résultats sont faussés par une
[fuite de données](docs/module2/75-bien-evaluer/#le-score-trop-beau-pour-être-vrai-la-fuite-de-données),
l'erreur présentée au Module 2 : une partie de l'information du test s'était glissée dans
l'entraînement. Dans un des cas étudiés, la prédiction des guerres civiles, les modèles
d'apprentissage automatique, une fois l'erreur corrigée, ne font pas mieux qu'une simple
[régression logistique](docs/module2/60-classer/#tracer-une-frontière-la-régression-logistique).
Le statisticien George Box l'avait résumé en 1979 : « tous les modèles sont faux, mais
certains sont utiles ». Encore faut-il savoir dans quelles conditions ils le sont.

## Retrouver des lois

Des chercheurs tentent aussi d'utiliser l'IA pour retrouver des explications, et non
seulement des prédictions. En 2020, le système AI Feynman, du physicien Max Tegmark et
de son étudiant Silviu-Marian Udrescu, retrouve, à partir de données, les cent équations
de physique du célèbre cours de Richard Feynman, en cherchant des formules simples plutôt
que des réseaux opaques. Les réseaux de Kolmogorov-Arnold, proposés en 2024, cherchent à
garder des modèles lisibles, dont on peut extraire des lois mathématiques. Et
l'[interprétabilité](docs/module4/93-regarder-a-l-interieur) du Module 4 tente d'ouvrir
les modèles eux-mêmes, pour comprendre ce qu'ils ont appris.

Ces efforts reposent sur une conviction que partagent la plupart des scientifiques : une
prédiction, même parfaite, n'est pas encore une connaissance. Comprendre, c'est pouvoir
expliquer pourquoi, prévoir ce qui arriverait dans des conditions nouvelles, et relier un
phénomène à d'autres. C'est aussi ce que réclamaient, en 2026, les médaillés Fields
inquiets de voir des machines produire des
[démonstrations qui n'expliquent rien](docs/module4/87-demontrer/#ce-que-cela-dit-et-ce-que-cela-ne-dit-pas).
