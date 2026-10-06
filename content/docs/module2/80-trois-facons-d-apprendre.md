---
title: "Trois façons d'apprendre"
weight: 80
slug: trois-facons-d-apprendre
---

# Trois façons d'apprendre

Le chapitre « [Bien évaluer un modèle](docs/module2/75-bien-evaluer/#tout-cela-portait-un-nom-lapprentissage-supervisé) » s'est terminé sur un constat. Tout ce que nous avons
construit dans ce module (régression, classification, la droite, Bayes)
appartient à une seule famille, l'**apprentissage supervisé**, dans laquelle
chaque exemple est accompagné de sa bonne réponse. Nous avons aussi vu que ce
n'est pas la seule façon d'apprendre.

Les grandes familles de l'apprentissage automatique se distinguent par la
nature du **signal** que le modèle utilise, c'est-à-dire ce qui, dans les
données, lui sert de guide. Il en existe trois grands types :

- une **réponse fournie** pour chaque exemple, ce qui correspond à
  l'apprentissage **supervisé**, étudié depuis le début du module ;
- **aucune réponse**, seulement des données brutes dans lesquelles il faut
  trouver une structure, ce qui correspond à l'apprentissage **non supervisé** (*unsupervised learning*) ;
- ni réponse ni structure donnée, mais une **récompense** qui arrive après
  coup, au fil des actions, ce qui correspond à l'apprentissage par
  **renforcement** (*reinforcement learning*).

{{< image src="/images/module2/trois-paradigmes.svg" alt="Trois panneaux. « Supervisé » : des points étiquetés en bleu et rouge, la réponse étant donnée. « Non supervisé » : les mêmes points, tous gris et sans étiquette, que l'algorithme regroupe en cercles pointillés pour former des groupes. « Renforcement » : une boucle entre un agent et son environnement, reliés par une flèche « action » et une flèche « récompense »." title="Les trois grandes familles, par la nature de leur signal : réponse donnée (supervisé), structure à découvrir (non supervisé), récompense au fil de l'action (renforcement)." loading="lazy" >}}

Nous avons passé tout le module dans la première famille. Ce dernier chapitre
présente les deux autres. Le but n'est pas de les maîtriser, mais de situer ce
que nous avons appris dans un ensemble plus large et de préparer les [modules
suivants](docs/module3).

## Apprendre avec un professeur : le supervisé

Commençons par ce que nous connaissons déjà. En apprentissage supervisé, le
signal est une **réponse fournie** avec chaque exemple, par exemple le prix
d'une maison, l'étiquette *pourriel* d'un courriel ou la couleur d'un point. Le
modèle apprend à relier l'entrée à cette réponse. Une fois entraîné, il
applique ce qu'il a appris à de nouveaux cas. On peut le comparer à un
professeur qui corrige : il connaît la bonne réponse, et l'élève progresse en
comparant sa réponse à celle-ci.

Nous en avons vu les deux formes : la **régression**, quand la réponse est un
nombre (un prix), et la **classification**, quand c'est une catégorie
(pourriel ou non). Malgré leurs différences, les deux utilisent le même signal
(une cible fournie d'avance) et le même mécanisme, qui consiste à régler des
paramètres pour minimiser l'écart à cette cible.

Cette dépendance à des réponses fournies est à la fois la principale force du
supervisé et sa principale limite. En effet, il faut que quelqu'un fournisse
ces étiquettes, souvent à la main, un exemple à la fois.

{{% hint info %}}
**Le socle humain du supervisé**

Nous avons vu, dans [*Bien évaluer un modèle*](docs/module2/75-bien-evaluer/#tout-cela-portait-un-nom-lapprentissage-supervisé),
que l'étiquetage des données est devenu une industrie à part entière. Cette
industrie a aussi des aspects difficiles. Décider des milliers de fois par jour
qu'un message est haineux et qu'un autre ne l'est pas, c'est aussi être exposé
aux contenus les plus violents du Web, et la modération de contenus est l'un
des métiers les plus éprouvants de cette chaîne. Les assistants les plus
récents en dépendent aussi : une partie de l'entraînement de ChatGPT repose sur
des humains qui notent et corrigent ses réponses (nous y reviendrons au
[Module 4](docs/module4/70-du-modele-a-l-assistant/#le-travail-humain-derrière-lassistant)). L'« intelligence » de ces systèmes repose donc en
partie sur un travail humain, ce qui soulève des questions que nous
retrouverons au [Module 5](docs/module5).
{{% /hint %}}

La [section suivante](#apprendre-sans-réponses-le-non-supervisé) traite du cas où personne n'a fourni ces réponses.

## Apprendre sans réponses : le non-supervisé

Souvent, les données n'ont pas d'étiquettes. On dispose d'un grand ensemble de
données brutes (des clients, des photos, des textes), sans aucune « bonne
réponse » à imiter. On peut quand même en apprendre quelque chose, mais le but
est différent. Il ne s'agit plus de prédire une réponse donnée, mais de
**découvrir une structure** présente dans les données elles-mêmes. C'est
l'apprentissage **non supervisé**.

La tâche la plus courante est le **regroupement** (ou *clustering*), qui
consiste à rassembler les exemples qui se ressemblent. Nous savons déjà ce que
« se ressembler » veut dire : c'est être **proches** dans l'espace des
caractéristiques, comme l'a expliqué
[*Prédire par ressemblance*](docs/module2/40-predire-par-ressemblance).
Regrouper consiste donc à repérer les amas naturels de points, c'est-à-dire les
zones denses séparées par des zones vides.

L'algorithme classique pour cette tâche s'appelle **k-means**. On peut
l'expliquer par une comparaison. Pour organiser une fête, on veut répartir les
invités autour de $k$ tables, en plaçant chaque table au centre de son groupe,
pour que chacun soit le plus près possible de la sienne. k-means procède de
cette façon, par ajustements successifs :

1. placer $k$ « centres » au hasard ;
2. rattacher chaque point au centre le plus proche (ce qui donne des groupes provisoires) ;
3. déplacer chaque centre au milieu de son groupe ;
4. répéter les étapes 2 et 3 jusqu'à ce que plus rien ne change.

Dans l'applet ci-dessous, choisissez le nombre de groupes et observez les
centres se déplacer, étape par étape, vers le centre des amas.

{{< applet src="/html/applets/kmeans.html" height="596" >}}

Ce résultat ressemble à de la classification, puisque les points sont répartis
en groupes de couleurs. La différence est cependant importante : ici, **les
points n'avaient aucune étiquette au départ.** Vous n'avez pas indiqué à
l'algorithme ce que représente chaque groupe. Vous lui avez seulement donné le
nombre de groupes, et il a déterminé le reste. Il n'y a pas de « bonne
réponse » à retrouver, seulement une structure à mettre en évidence.

Ce type de méthode est très répandu. On l'utilise pour segmenter une clientèle
en profils types pour le marketing, pour repérer une transaction anormale parmi
des millions d'autres (détection de fraude) ou pour compresser des données en
les résumant par leurs groupes.

Le regroupement n'est qu'une partie du non-supervisé. Celui-ci comprend aussi
la [réduction de dimension](#réduire-la-dimension), présentée ci-dessous, et l'**apprentissage de
représentations** (*representation learning*), qui consiste à découvrir sans étiquettes de bonnes
caractéristiques pour décrire les données. Cette idée, qui consiste à laisser
la machine construire ses propres descripteurs, joue un rôle central dans l'IA
moderne. Nous la retrouverons avec les **autoencodeurs** ([Module 3](docs/module3/40-apprentissage-profond/#apprendre-sans-étiquettes-lautoencodeur)) et les **plongements** (*embeddings*) de mots ([Module 4](docs/module4/40-des-mots-aux-nombres/#les-plongements)).

{{% details "Les mathématiques de k-means (optionnel)" %}}

k-means cherche à minimiser une fonction d'erreur, l'**inertie**, qui est la
somme des carrés des distances de chaque point à son centre :

$$J = \sum_{i=1}^{n} \min_{j=1}^{k} \lVert \mathbf{x}_i - \boldsymbol{\mu}_j \rVert^2$$

où $\mathbf{x}_i$ est le $i$-ème point et $\boldsymbol{\mu}_j$ le centre du groupe
$j$. L'algorithme alterne deux étapes :

- **assignation** : chaque point est rattaché au centre le plus proche,
  $c_i = \arg\min_j \lVert \mathbf{x}_i - \boldsymbol{\mu}_j \rVert^2$ ;
- **mise à jour** : chaque centre est placé à la moyenne de ses points,
  $\boldsymbol{\mu}_j = \frac{1}{n_j} \sum_{i : c_i = j} \mathbf{x}_i$.

On répète ces étapes jusqu'à convergence. Deux remarques s'imposent. Le nombre
de groupes $k$ est un **hyper-paramètre**, qu'on choisit d'avance comme le $k$
de kNN. De plus, l'algorithme peut s'arrêter dans un minimum local. C'est
pourquoi on le relance habituellement plusieurs fois avec des centres initiaux
différents, et on garde la meilleure solution.

{{% /details %}}

### Réduire la dimension

Les données ont souvent beaucoup de caractéristiques : des dizaines pour un client,
784 pour une image de chiffre manuscrit (une par pixel), des millions pour une
photo. On ne peut pas dessiner un nuage de points à 784 dimensions. Et la
[malédiction de la dimension](docs/module2/40-predire-par-ressemblance/#mesurer-la-ressemblance-la-distance)
rend les distances de moins en moins utiles à mesure que les dimensions s'ajoutent.

Heureusement, ces caractéristiques sont rarement indépendantes. Dans une image de
chiffre, deux pixels voisins ont presque toujours la même teinte. Chez un client,
le revenu et la valeur de la maison varient souvent ensemble. Une bonne partie de
l'information est donc redondante. La **réduction de dimension** (*dimensionality
reduction*) en tire parti : elle résume chaque exemple par quelques nombres
seulement, en perdant le moins d'information possible.

La méthode classique est l'**analyse en composantes principales** (ACP, *principal
component analysis*), proposée par le statisticien Karl Pearson en 1901. Elle
cherche la direction dans laquelle les données s'étalent le plus, puis la
suivante, perpendiculaire à la première, et ainsi de suite. On ne garde que les
premières directions, appelées **composantes principales**, et chaque exemple est
résumé par sa position le long de chacune.

Une comparaison aide à voir pourquoi on cherche l'étalement. Photographier un
objet, c'est le réduire de trois dimensions à deux. Une théière photographiée de
côté se reconnaît à son bec et à son anse. Photographiée de dessus, ce n'est plus
qu'un disque. Le bon angle est celui qui conserve le plus de différences entre les
points de l'objet. L'ACP choisit cet angle automatiquement, quel que soit le nombre
de dimensions.

Dans l'applet ci-dessous, un nuage de points en deux dimensions doit être réduit à
une seule. Faites tourner l'axe. Les points se projettent sur lui, et l'indicateur
montre la part de l'étalement conservée. Cherchez l'angle qui la rend la plus
grande, puis comparez-le avec celui que trouve le bouton « ACP ».

{{< applet src="/html/applets/acp.html" height="515" >}}

Appliquée aux 784 pixels des chiffres manuscrits, l'ACP donne la figure
ci-dessous. Chaque chiffre y est réduit à deux nombres, ses positions le long des
deux premières composantes principales. Les 0 et les 1 se séparent assez bien,
mais la plupart des chiffres se chevauchent. Ces deux nombres ne conservent
d'ailleurs que 17 % de l'étalement des données.

{{< image src="/images/module2/acp-mnist.svg" alt="Une carte en deux dimensions : 2 000 chiffres manuscrits de la base MNIST, chacun réduit de 784 pixels à deux nombres, ses positions le long des deux premières composantes principales. Chaque point est coloré selon le chiffre qu'il représente. Les 0 et les 1 occupent des régions assez distinctes, de part et d'autre de la carte ; les autres chiffres se chevauchent largement au centre." title="2 000 chiffres de la base MNIST, réduits par l'ACP de 784 pixels à deux nombres. L'ACP a été calculée sur les 60 000 images d'entraînement." loading="lazy" >}}

L'ACP a une limite : elle ne trouve que des directions droites. Elle revient à
regarder les données sous le meilleur angle, sans pouvoir les déformer. Or les
données réelles se trouvent souvent sur des surfaces courbes, repliées sur
elles-mêmes. Des méthodes plus récentes savent déplier ces surfaces, comme t-SNE
(2008), de Laurens van der Maaten et Geoffrey Hinton, et UMAP (2018). On les
utilise surtout pour visualiser des données en deux dimensions.

La réduction de dimension reviendra dans la suite du cours.
L'[autoencodeur](docs/module3/40-apprentissage-profond/#apprendre-sans-étiquettes-lautoencodeur)
du Module 3 est un réseau de neurones qui réduit lui aussi chaque image à quelques
nombres, puis la reconstruit. Il agit comme une ACP capable de suivre les courbes.
Ces quelques nombres forment l'**espace latent**, au cœur de
l'[IA générative](docs/module4/10-generer/#lespace-latent) du Module 4.

{{% details "Les mathématiques de l'ACP (optionnel)" %}}

On centre d'abord les données, en retranchant à chaque caractéristique sa moyenne.
L'étalement des données le long d'une direction $\mathbf{u}$ de longueur 1 est la
variance de leurs projections :

$$\mathrm{Var}(\mathbf{u}) = \frac{1}{n} \sum_{i=1}^{n} (\mathbf{u}^\top \mathbf{x}_i)^2 = \mathbf{u}^\top \Sigma \, \mathbf{u}$$

où $\Sigma$ est la **matrice de covariance** des données. La direction qui maximise
cette variance est le **vecteur propre** de $\Sigma$ associé à sa plus grande
**valeur propre**, et cette valeur propre est la variance conservée. Les
composantes suivantes sont les vecteurs propres suivants, par ordre de valeur
propre décroissante. La part de l'étalement conservée par les $k$ premières
composantes est la somme de leurs valeurs propres, divisée par la somme de toutes.

Un autoencodeur dont les couches n'ont pas de fonction d'activation, entraîné à
minimiser l'erreur de reconstruction au carré, retrouve exactement le même
sous-espace que l'ACP (Pierre Baldi et Kurt Hornik, 1989). Les fonctions
d'activation lui permettent d'aller au-delà, vers les surfaces courbes.

{{% /details %}}

### Fabriquer soi-même ses réponses : l'auto-supervision

Entre le supervisé, qui exige des étiquettes, et le non-supervisé, qui n'en
utilise pas, il existe une approche qui a beaucoup transformé le domaine :
**fabriquer les étiquettes à partir des données elles-mêmes**. On peut prendre
un texte, en cacher un mot et demander au modèle de le deviner. La « bonne
réponse » se trouve dans le texte, sans qu'aucun humain ait eu à étiqueter quoi
que ce soit. On peut aussi cacher une partie d'une photo et demander au modèle
de la reconstituer, ou faire pivoter une image et lui demander de quel angle.
Dans chaque cas, le problème a la forme d'un problème supervisé, avec une
entrée et une réponse attendue, mais la réponse est tirée de la donnée brute.
C'est l'apprentissage **auto-supervisé** (*self-supervised learning*).

Cette approche semble simple, mais elle a une portée considérable, parce
qu'elle supprime le besoin d'étiquetage. Le Web contient des milliers de
milliards de mots disponibles, qui ne demandent aucune heure de travail
humain : chaque phrase fournit un exercice avec son corrigé. C'est de cette
façon, en apprenant à prédire le mot suivant, que les grands modèles de langage
du [Module 4](docs/module4/50-predire-le-mot-suivant/#gpt-un-transformer-qui-prédit-le-jeton-suivant) sont entraînés, et c'est pour cette raison qu'ils
ont pu traiter une grande partie de ce que l'humanité a écrit. L'apprentissage
supervisé intervient ensuite, sur des quantités beaucoup plus petites, avec les
réponses notées par des humains dont parlait l'[encadré plus haut](#apprendre-avec-un-professeur-le-supervisé). Cependant,
l'essentiel de leurs connaissances provient de cette tâche de prédiction sur
les textes eux-mêmes.

## Apprendre par l'expérience : le renforcement

La troisième situation est très différente des deux premières. Il n'y a pas
d'étiquettes, et il n'y a pas non plus seulement un ensemble de données à
structurer. Le modèle, qu'on appelle ici un **agent**, doit agir, et il apprend
à partir des **conséquences** de ses actions. On peut penser à un enfant qui
apprend à faire du vélo, à un robot qui apprend à marcher ou à un joueur qui
découvre un jeu. Personne ne leur indique le bon mouvement à chaque instant.
Ils essaient, échouent, recommencent et retiennent ce qui fonctionne.

Le signal est ici une **récompense** (*reward*), par exemple un point gagné, une partie
remportée ou une chute évitée. Cette récompense arrive souvent **bien après**
les actions qui l'ont produite. Quand on gagne une partie d'échecs, il est
difficile de savoir quel coup a été décisif. Ce décalage est la principale
difficulté du renforcement, parce qu'il faut apprendre à relier une récompense
tardive aux actions qui l'ont rendue possible.

La stratégie utilisée est celle de l'**essai-erreur**. L'agent explore, reçoit
des récompenses et des punitions, et **renforce** peu à peu les actions qui
mènent au succès, d'où le nom de cette famille. Dans l'applet ci-dessous, un
agent (le point jaune) cherche la sortie (**+1**) d'une petite grille en
évitant un piège (**−1**), sans aucune connaissance au départ. Lancez
l'entraînement.

{{< applet src="/html/applets/reinforcement.html" height="728" >}}

Au début, l'agent se déplace au hasard. Puis, d'un épisode à l'autre, une
**carte de valeur** se forme (les cases se colorent selon leur valeur estimée)
et une **politique** (*policy*) apparaît. Les flèches, qui indiquent pour chaque case le
meilleur mouvement, finissent par former un chemin sûr vers le but. Le curseur
d'**exploration** (ε) est instructif. À zéro, l'agent ne fait qu'exploiter ce
qu'il croit déjà savoir, et il peut rester dans un chemin médiocre. Un peu de
hasard l'amène à explorer d'autres chemins, et parfois à en trouver de
meilleurs. Ce compromis entre **explorer et exploiter** (*exploration vs. exploitation*) est au centre du
renforcement.

Cette approche rappelle une notion déjà vue. Au [Module 1](docs/module1/30-chercher-raisonner/#lapogée-deep-blue-bat-kasparov-1997), nous avons étudié les machines qui
jouent aux échecs en cherchant dans l'arbre des coups possibles. Le
renforcement reprend cette recherche, mais la machine apprend elle-même à
évaluer les positions au lieu de tout calculer. C'est cette combinaison de la
recherche du GOFAI et de l'apprentissage qui a permis à **AlphaGo** de battre
les meilleurs joueurs de go humains, alors que la force brute seule n'y
parvenait pas.

Le renforcement est aussi la famille qui demande le plus de calcul, et il s'est
surtout développé lorsqu'on l'a combiné aux **réseaux de neurones** (le *deep reinforcement learning*, [Module 3](docs/module3/80-renforcement-profond)).
On le retrouve aussi dans les assistants modernes. Le comportement de ChatGPT
est en partie ajusté par renforcement, à partir des préférences d'évaluateurs
humains (le **RLHF**). Le renforcement sert également, avec des récompenses
vérifiables (un problème de mathématiques a une bonne réponse, un programme
réussit ou non ses tests, ce qu'on appelle le **RLVR**), à entraîner les
modèles les plus récents à « raisonner » longuement avant de répondre. Nous
verrons ces méthodes au [Module 4](docs/module4/70-du-modele-a-l-assistant/#des-modèles-qui-raisonnent).

## Un même squelette, d'un bout à l'autre

Les trois familles répondent de trois façons à une même question, celle de
savoir à partir de quoi le modèle apprend : une réponse fournie, une structure
à découvrir ou une récompense à obtenir. Ces trois familles partagent cependant
la même structure de base, celle qui a servi tout au long de ce module.

Cette structure comporte plusieurs étapes. On part de **données**, qu'on décrit
par des nombres, donc par des points dans un espace. On choisit un
**modèle**, c'est-à-dire une fonction de prédiction réglée par des paramètres.
On mesure son **erreur** de prédiction. On règle ensuite les paramètres du
modèle pour **minimiser** cette erreur, le plus souvent par descente de
gradient. On vérifie enfin que le modèle **généralise** au-delà des exemples
appris. Toutes les méthodes vues dans ce module sont des variantes de ce
schéma : le modèle simple et son unique nombre, kNN et ses zéro paramètre, la
droite et ses deux paramètres, l'arbre et ses questions, la régression
logistique et Bayes qui classent, k-means qui regroupe sans étiquettes et
l'agent qui apprend à partir d'une récompense. La démarche est la même, mais
elle s'applique à des problèmes différents.

C'est ce que ce module voulait montrer. Pour une machine, « apprendre » n'a
rien de magique : c'est **ajuster des réglages pour réduire une erreur sur des
exemples**. La question posée dès la première page, qui était de savoir en quoi
il s'agit d'intelligence, reste ouverte. Vous savez cependant maintenant,
concrètement, comment ces systèmes fonctionnent.

Il reste à revenir sur le lien avec la statistique annoncé au début du module.
Un statisticien reconnaîtrait tout ce que nous avons fait ici : ajuster une
droite, estimer une probabilité, tirer un échantillon, se méfier d'un score. Ce
qui a changé, ce n'est pas la base, mais l'accent et l'échelle. L'accent est
mis sur la prédiction d'abord, l'explication ensuite, et parfois jamais.
L'échelle se compte en millions d'exemples et en milliards de paramètres, avec
des modèles que personne ne lit plus. C'est à cette échelle que la statistique
a pris le nom d'apprentissage automatique, et qu'elle a produit des résultats
que ses fondateurs n'avaient pas prévus.

L'étape suivante est ce changement d'échelle. Richard Sutton, un chercheur qui
a consacré sa carrière à l'apprentissage par renforcement, a tiré de
soixante-dix ans d'histoire de l'IA une leçon qu'il qualifie d'amère, [« The Bitter
Lesson »](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)
(2019). Selon lui, à long terme, les méthodes générales qui exploitent la
puissance de calcul finissent toujours par l'emporter sur celles où l'on avait
inscrit à la main le savoir humain, et seules deux méthodes passent vraiment à
l'échelle, la **recherche**, celle du [Module 1](docs/module1/30-chercher-raisonner), et l'**apprentissage**, celui
de ce module. Le sens et le coût de cette leçon sont examinés au
[**Module 3**](docs/module3/40-apprentissage-profond/#la-leçon-amère). Nous y combinerons ces fonctions réglables en
**réseaux de neurones** profonds, et nous verrons pourquoi ces réseaux ont
permis de grands progrès dans le traitement de l'image et du langage. Au
[**Module 4**](docs/module4), ces mêmes réseaux deviendront **génératifs**,
capables de produire des textes et des images : ce sont les grands modèles de
langage. La structure de base restera la même, mais à une échelle beaucoup plus
grande.
