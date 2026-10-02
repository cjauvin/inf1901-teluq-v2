---
title: "Module 1 - Aux origines : l'intelligence artificielle symbolique"
weight: 100
bookCollapseSection: true
---

![](/images/gofai.webp)

# Module 1 - Aux origines : l'intelligence artificielle symbolique

Avant les réseaux de neurones et avant ChatGPT, l'IA a d'abord cherché à
**fabriquer une machine qui pense en manipulant des symboles et des règles**,
comme le ferait un logicien ou un joueur d'échecs méthodique. On appelle
aujourd'hui cette approche l'**IA symbolique**, ou *GOFAI* (pour *Good
Old-Fashioned AI*, la « bonne vieille IA »). Pendant près de quarante ans, elle a
dominé le domaine et obtenu des succès importants, puis elle a rencontré des
limites qui l'ont fait paraître démodée.

Ce module présente cette histoire en **six chapitres**. Chacun associe un
*moment historique* à une *idée technique*. Le but n'est pas de vous rendre
capable de programmer ces systèmes, mais de comprendre l'**idée** sur laquelle ils
reposent et les **difficultés** qu'ils ont rencontrées. En comprenant pourquoi
cette première IA a atteint ses limites, on comprend mieux pourquoi la suite (les
modules [2](docs/module2), [3](docs/module3) et [4](docs/module4)) est si différente.

Dans l'ensemble du domaine de l'intelligence artificielle, l'IA symbolique
correspond à l'**IA « classique »**, qui se distingue de l'apprentissage
automatique que le cours étudiera ensuite.

{{< image src="/images/module1/ai-venn.svg" alt="Carte en régions imbriquées de l'intelligence artificielle. À l'intérieur de « Intelligence artificielle (IA) » : d'un côté « IA classique » ; de l'autre « Apprentissage automatique (AA) » (machine learning), qui contient « Méthodes d'AA diverses » et « Réseaux de neurones / apprentissage profond », lesquels contiennent à leur tour « IA générative » et « ChatGPT ». Un repère « Module 1 » pointe vers l'ensemble « IA classique », qui est le sujet du module." title="La carte de l'IA : le Module 1 porte sur l'IA « classique » (symbolique), antérieure à l'apprentissage automatique." loading="lazy" >}}

Une idée traverse tout le module. Dès les années 1950, **deux grandes hypothèses
rivales** sur la nature de l'intelligence apparaissent presque en même temps.
L'une considère l'esprit comme de la **logique** (manipuler des symboles,
appliquer des règles). L'autre le considère comme un **cerveau** (un réseau qui
apprend de ses expériences). Le Module 1 présente cette opposition, et le [Module 3](docs/module3)
montrera comment elle a évolué.

## Le parcours du module

Le module suit l'ordre chronologique. Chaque chapitre présente une idée, puis la
limite qui mène au chapitre suivant.

1. [*Turing et la question fondatrice (1950)*](docs/module1/10-turing) : une
   machine peut-elle penser, le jeu de l'imitation, et la pensée vue comme un
   calcul.
2. [*Deux paris rivaux (1956-1958)*](docs/module1/20-deux-paris) : la naissance
   de l'IA à Dartmouth, l'esprit comme logique et l'esprit comme cerveau.
3. [*L'âge d'or symbolique : chercher et raisonner*](docs/module1/30-chercher-raisonner) :
   résoudre un problème en explorant un espace d'états, l'explosion combinatoire,
   Deep Blue et ELIZA.
4. [*Représenter le monde*](docs/module1/40-representer-le-monde) : donner un
   savoir à la machine, SHRDLU et son micro-monde, le problème du sens commun.
5. [*Capturer l'expertise : les systèmes experts*](docs/module1/50-systemes-experts) :
   les règles *si… alors…*, le moteur d'inférence, MYCIN, et le goulot
   d'étranglement de la connaissance.
6. [*Les hivers et la bascule*](docs/module1/60-hivers) : les deux périodes de
   recul de l'IA, ce qui reste du GOFAI aujourd'hui, et le passage à
   l'apprentissage.

Le [travail noté 1](docs/module1/99-travail-noté-1) clôt le module.

## Objectifs

À la fin de ce module, vous devriez être en mesure de :

* Expliquer ce qu'est l'IA symbolique et en quoi elle se distingue de
  l'apprentissage automatique étudié dans les modules [2](docs/module2) à [4](docs/module4);
* Situer les grandes étapes et les figures marquantes de l'histoire de l'IA, du
  test de Turing (1950) aux systèmes experts et aux « hivers » de l'IA;
* Décrire les idées algorithmiques centrales du GOFAI (recherche dans un espace
  d'états, règles, représentation des connaissances) à un niveau intuitif;
* Distinguer les deux hypothèses rivales sur la nature de l'intelligence,
  l'approche symbolique et l'approche connexionniste, et situer chacune dans
  l'histoire du domaine;
* Comprendre pourquoi cette approche a fini par atteindre ses limites (problème
  du sens commun, goulot d'étranglement de la connaissance), ce qui a ouvert la voie
  à l'apprentissage automatique;
* Reconnaître ce qui reste de l'IA symbolique dans l'informatique d'aujourd'hui
  (recherche de chemins, moteurs de règles, représentation des connaissances).

## Durée

Deux semaines, soit environ 18 heures.

## Évaluation

Le [travail noté 1](docs/module1/99-travail-noté-1), qui compte pour 15 % de l'évaluation
finale, vous fait jouer le rôle d'un **système expert**. À partir d'une base de
règles `si… alors…`, vous suivez le raisonnement de la machine sur des cas
concrets, vous trouvez un cas qu'elle ne sait pas traiter, puis vous ajoutez une règle
pour combler ce manque. Ce travail vous permet de constater par vous-même les forces et la
fragilité de l'IA symbolique.
