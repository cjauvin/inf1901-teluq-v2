---
title: "Prédire par ressemblance"
weight: 40
slug: predire-par-ressemblance
---

# Prédire par ressemblance

La page « [Regarder les données](docs/module2/30-les-donnees) » s'est terminée sur l'idée suivante : si décrire des objets par
des nombres transforme leur ressemblance en une distance, il doit exister une
façon très simple de prédire. Cette façon est sans doute l'idée la plus intuitive
de l'apprentissage automatique : **pour deviner la réponse sur un nouveau cas, on
regarde les cas connus qui lui ressemblent le plus, et on reprend leur réponse.**

Pour estimer le prix d'une maison qu'on n'a jamais vue, on cherche les maisons
déjà vendues qui lui ressemblent le plus (même quartier, même taille, même âge),
et on s'attend à un prix comparable. C'est ce que fait un agent immobilier quand
il utilise des « comparables ». Il faut maintenant transformer cette intuition en
une procédure précise. Tout repose sur la notion de ressemblance, qu'il faut
d'abord rendre mesurable.

## Mesurer la ressemblance : la distance

Pour deux objets décrits par des nombres, « se ressembler » a une traduction
géométrique directe : être **proches** dans leur espace. La proximité entre deux
points se mesure par la **distance**.

Pour deux points dans un plan, il s'agit de la distance ordinaire, c'est-à-dire la
longueur du segment droit qui les relie, celle qu'on mesurerait avec une règle.
(Les mathématiciens l'appellent la *distance euclidienne*, mais c'est la même
notion que dans la vie courante.)

{{< image src="/images/module2/distance_2d.png" alt="Deux points dans un plan reliés par un segment droit : la distance euclidienne entre eux." title="La distance entre deux points : la longueur du trait droit qui les relie." loading="lazy" >}}

Cette longueur se calcule avec le théorème de Pythagore. Pour deux points d'un
plan, on prend l'écart entre eux sur le premier axe et l'écart sur le second, on
élève chacun au carré, on additionne les deux carrés et on prend la racine carrée
du résultat :

$$\text{distance} = \sqrt{(\text{écart sur l'axe 1})^2 + (\text{écart sur l'axe 2})^2}$$

Rien dans cette méthode ne dépend du nombre d'axes. Si nos maisons ont six
caractéristiques, on calcule six écarts au lieu de deux, on les élève au carré, on
les additionne et on prend la racine carrée du total. On compare les objets
coordonnée par coordonnée et on obtient un seul nombre, petit s'ils se
ressemblent, grand s'ils diffèrent. Comme on l'a vu au chapitre « [Regarder les données](docs/module2/30-les-donnees/#quand-il-y-a-trop-de-dimensions-pour-les-voir) », la même
formule s'applique à une image, dont les millions de pixels forment autant de
coordonnées. Pour deux photos, l'écart sur un axe est simplement la différence
entre la valeur d'un même pixel dans l'une et dans l'autre. On note $A_1$ la
valeur du premier pixel de la photo $A$, $B_1$ celle du premier pixel de la photo
$B$, et ainsi de suite jusqu'au $n$-ième :

$$\text{distance}(A, B) = \sqrt{(A_1 - B_1)^2 + (A_2 - B_2)^2 + \cdots + (A_n - B_n)^2}$$

Deux photos identiques donnent une distance nulle, puisque chaque écart est nul.
Deux photos qui ne diffèrent que par un pixel donnent un très petit nombre. Plus
les pixels diffèrent, en nombre ou en intensité, plus la distance augmente. La
même formule vaut donc du plan à la photo, et *n* peut valoir deux ou plusieurs
millions.

{{< image src="/images/module2/distance_high_dim.png" alt="La même idée de distance, transposée à un espace de haute dimension." title="La même distance se calcule, quel que soit le nombre de dimensions." loading="lazy" >}}

{{% hint warning %}}
**Une nuance importante.** Le fait que la distance se calcule sur des pixels ne
signifie pas qu'elle mesure bien la ressemblance entre images. Sur des
caractéristiques choisies par un humain (superficie, nombre de pièces…), la
proximité a un sens clair. Sur des pixels bruts, elle en a beaucoup moins. Deux
photos du même chat, dans deux poses différentes, peuvent être très éloignées
pixel à pixel. Une photo et sa version simplement assombrie, presque identiques
pour notre œil, peuvent l'être tout autant. Obtenir une distance qui reflète la
ressemblance réelle d'objets complexes est un problème à part entière, celui des
**bonnes représentations**, que nous retrouverons avec les réseaux de neurones
(Module&nbsp;3) et les plongements (Module&nbsp;4). Pour des données tabulaires
comme nos maisons, en revanche, la distance brute convient déjà très bien.
{{% /hint %}}

{{% hint warning %}}
**La malédiction de la dimension.** Une autre raison, plus mathématique, explique
pourquoi la distance perd de son sens quand le nombre de dimensions augmente. Dans
un plan, vingt maisons suffisent à occuper l'espace, et chacune a des voisines
proches. Dans un espace à un million de dimensions, comme celui des pixels, vingt
exemples, ou même vingt millions, sont dispersés dans un espace presque vide, et
tous les points sont loin les uns des autres. Les distances entre les points
deviennent presque toutes égales, et le « plus proche voisin » n'est plus
vraiment proche. C'est la **malédiction de la dimension** (*curse of
dimensionality*). Chaque caractéristique ajoutée multiplie la taille de l'espace,
et le nombre d'exemples nécessaire pour le remplir croît très rapidement. Ce
problème touche directement kNN. C'est l'une des raisons pour lesquelles, sur des
images ou du texte, on cherche d'abord à réduire le nombre de dimensions à
quelques-unes qui comptent, une idée que les [Modules 3](docs/module3) et
[4](docs/module4) développeront. Vous avez déjà rencontré ce phénomène sous un
autre nom, l'[explosion
combinatoire](docs/module1/30-chercher-raisonner/#lexplosion-combinatoire) du
Module 1. Dans ce cas, chaque coup supplémentaire multipliait le nombre de parties
à explorer. Ici, chaque caractéristique supplémentaire multiplie l'espace à
remplir. Il s'agit de la même croissance exponentielle, que la force brute ne
permet pas de traiter et qui demande une méthode plus astucieuse.
{{% /hint %}}

Nous disposons donc d'une mesure de ressemblance fiable pour des données
tabulaires comme nos maisons. Il reste à l'utiliser pour prédire.

## Les k plus proches voisins

Pour prédire le prix d'une maison inconnue, la méthode est très simple. On calcule
sa distance à toutes les maisons connues, on retient celles qui lui ressemblent le
plus et on prédit la moyenne de leurs prix. On utilise plusieurs voisins plutôt
qu'un seul parce qu'un unique voisin serait une base fragile : il pourrait s'agir
d'un cas exceptionnel, une aubaine ou une arnaque. En faisant la moyenne de
plusieurs voisins, on atténue l'effet de ces cas particuliers.

Le nombre de voisins consultés se note **k**, d'où le nom de l'algorithme : les
**k plus proches voisins** (*k-nearest neighbors*, ou kNN). L'idée a été
formalisée en 1951 par deux statisticiens, Evelyn Fix et Joseph Hodges, dans un
rapport rédigé pour l'armée de l'air américaine. Elle relève donc de la
statistique avant de relever de l'informatique.

Nous venons de faire une **régression**, puisque la cible était un prix, donc un
nombre, et que nous l'avons obtenu en faisant la moyenne des voisins. Pour une
**classification**, il suffit de changer la dernière étape. Au lieu de faire la
moyenne des réponses des voisins, on retient la réponse la plus fréquente, par un
**vote majoritaire**. Pour prédire si une maison partira vite, on regarde ce qui
s'est passé pour ses plus proches voisines et on suit la majorité.

kNN a donc la particularité de faire les deux sans rien changer d'essentiel. La
distance et les voisins sont les mêmes, et seule la façon de combiner leurs
réponses diffère. La plupart des algorithmes que nous verrons ensuite se
spécialiseront dans l'une ou l'autre tâche.

{{< image src="/images/module2/knn-regression-vs-classification.svg" alt="La recette kNN, illustrée comme un tronc commun qui se sépare en deux à la fin. Tronc commun : une nouvelle maison, puis les distances à tous les exemples connus, puis les k plus proches voisins. Ces étapes sont communes aux deux tâches. Puis une seule bifurcation, à l'étape d'agrégation : en haut, la moyenne des prix des voisins donne un nombre (250 000 $), la régression ; en bas, le vote majoritaire des réponses des voisins donne une catégorie (« vendue vite »), la classification." title="kNN suit les mêmes étapes pour la régression et la classification ; seule la dernière (moyenne ou majorité) les distingue." loading="lazy" >}}

{{% hint info %}}
**La recette des _k_ plus proches voisins**, pour prédire à propos d'une nouvelle maison :

1. Calculer la **distance** entre cette maison et *chacune* des maisons déjà connues (à partir de leurs caractéristiques).
2. Garder les **k** maisons les plus proches, ses « voisins ».
3. Combiner les réponses de ces voisins :
   - pour un **nombre** (régression) → prendre leur **moyenne** ;
   - pour une **catégorie** (classification) → prendre leur **majorité**.

Seule cette dernière étape distingue les deux tâches ; tout le reste est identique.
{{% /hint %}}

Revenons à nos maisons, dans le plan de la seconde question (distance du centre,
année de construction). On peut demander à kNN sa réponse pour une nouvelle maison
placée à n'importe quel endroit de ce plan. En posant la question pour chaque
point du plan et en colorant ce point selon la réponse obtenue, on obtient une
carte : bleu pâle si les *k* voisins votent « vendue vite », rouge pâle s'ils
votent « a traîné ». Voici le résultat pour *k* = 3 :

{{< image src="/images/module2/maisons-frontiere-k3.svg" alt="Le nuage coloré des maisons, dans le plan distance du centre × année de construction, avec le fond teinté : bleu pâle là où kNN (k = 3) répondrait « vendue vite » à une maison qui s'y trouverait, rouge pâle là où il répondrait « a traîné ». La ligne où la teinte change passe dans la bande vide entre les deux amas : c'est la frontière de décision. Les deux exceptions se trouvent dans la zone de la couleur opposée." title="La frontière de décision de kNN (k = 3) sur nos maisons : le fond donne la réponse du modèle en chaque point du plan, et la ligne où la couleur change est la frontière." loading="lazy" >}}

Le plan est ainsi divisé en deux **régions**. La ligne où la couleur change, qui
passe dans la bande vide entre les deux amas, s'appelle la **frontière de
décision**. Personne ne l'a tracée : elle résulte de l'application de la règle en
chaque point. C'est elle qui détermine la prédiction. Une maison située d'un côté
sera classée « vendue vite », et une maison située de l'autre côté sera classée
« a traîné », sans autre nuance. On peut aussi observer ce qui arrive aux deux
exceptions du [premier chapitre](docs/module2/10-le-probleme/#une-seconde-question-dune-tout-autre-nature). Avec *k* = 3, chacune se trouve dans la région de
la couleur opposée, puisque ses trois voisins les plus proches votent pour l'autre
catégorie.

Cette observation vaut pour tout classificateur, et pas seulement pour kNN :
**classer revient à diviser l'espace en régions, et un modèle de classification
est entièrement décrit par la frontière qu'il trace.** C'est pour cette raison que
la classification est plus facile à visualiser que la régression : en deux
dimensions, on voit la frontière d'un seul coup d'œil. Au chapitre « [Classer](docs/module2/60-classer/#tracer-une-frontière-la-régression-logistique) »,
nous verrons des modèles dont la frontière est une simple droite. Celle de kNN
peut prendre n'importe quelle forme.

L'applet ci-dessous permet de manipuler cette frontière. Il y a deux catégories,
des points rouges et des points bleus. Chaque point coloré est un exemple connu,
et le fond montre, comme plus haut, la prédiction de kNN pour tout nouveau point.
Ajoutez des points, déplacez-les, faites varier *k* et observez comment la
frontière de décision change.

{{< applet src="/html/applets/knn.html" height="692" >}}

## Le choix de k

L'applet soulève rapidement une question : quelle valeur faut-il donner à **k** ?

Les deux extrêmes sont instructifs. Avec **k = 1**, chaque prédiction ne s'appuie
que sur le voisin le plus proche. La frontière suit alors le moindre détail, fait
le tour de chaque point individuel et devient très irrégulière. Le modèle suit les
exemples connus de si près qu'il réagit au moindre point aberrant. Ce défaut porte
un nom, et il est central dans tout ce qui suit : le **sur-apprentissage**
(*overfitting*), qui consiste à apprendre les exemples eux-mêmes au lieu
d'apprendre à partir d'eux. Nous y reviendrons en détail dans
[*Généraliser*](docs/module2/70-generaliser). Nos maisons le montrent : avec
*k* = 1, chacune des deux exceptions crée autour d'elle une petite zone de sa
couleur dans la région opposée, et la frontière se découpe en cellules anguleuses.

{{< image src="/images/module2/maisons-frontiere-k1.svg" alt="Même plan, même fond teinté, mais avec k = 1 : chaque maison impose sa couleur à tout ce qui l'entoure. Les deux exceptions créent chacune une petite zone de leur couleur dans la région opposée, et la frontière se découpe en cellules anguleuses." title="La même frontière avec k = 1 : chaque exception crée sa propre petite zone, et la frontière suit chaque point." loading="lazy" >}}

À l'autre extrême, avec un **k très grand**, chaque prédiction fait la moyenne de
tant de voisins que les particularités locales disparaissent. La frontière devient
lisse, parfois au point d'ignorer des structures qui existent réellement dans les
données.

Une « bonne » valeur se trouve entre les deux, ni trop petite ni trop grande. La
façon de la trouver est une question qui paraît simple, mais qui est l'une des
plus importantes de l'apprentissage automatique. Elle ne concerne pas seulement
kNN : tout modèle doit être assez souple pour saisir les vraies régularités des
données, sans l'être au point de reproduire leurs variations dues au hasard.

Cette question est assez centrale pour que nous lui consacrions une page entière,
[*Généraliser*](docs/module2/70-generaliser), une fois que nous connaîtrons
quelques modèles de plus. Pour l'instant, retenez seulement l'idée suivante :
**k règle un compromis entre « coller aux exemples » et « lisser à l'excès ».**

## L'angle mort de kNN

kNN a une particularité : il n'a, à proprement parler, **rien à apprendre**. Il n'y
a ni entraînement ni paramètres à régler. Il suffit de garder en mémoire tous les
exemples connus et de les consulter au moment de prédire. Les données constituent
le modèle.

Cette simplicité a cependant deux inconvénients, qui motivent la suite du module.

Le premier est que kNN est **coûteux**. Pour chaque nouvelle prédiction, il doit
calculer la distance à tous les exemples connus, sans exception. Avec quelques
dizaines de maisons, ce n'est pas un problème. Pour un système qui doit reconnaître
un visage parmi des millions d'images, ou répondre en une fraction de seconde à
des millions d'utilisateurs, tout recalculer à chaque fois devient très coûteux.
kNN reporte tout le travail au moment de la prédiction, qui est le moment où il
coûte le plus cher.

Le second inconvénient est plus fondamental : kNN **ne dégage aucune
compréhension** des données. Il n'en tire aucune règle, aucune tendance, aucune
forme générale. Il ne « sait » pas que les grandes maisons coûtent plus cher : il
se contente de retrouver des voisins. [Le modèle le plus
bête](docs/module2/20-modele-le-plus-bete) avait, lui, résumé toute sa
connaissance en **un seul nombre**, le prix moyen. kNN fait l'inverse : il ne
résume rien et garde tout.

Or c'est justement ce résumé qui nous intéresse. On voudrait qu'un modèle
**apprenne** quelque chose des données, c'est-à-dire qu'il en extraie quelques
paramètres qui représentent la tendance générale, quitte à ne plus avoir besoin
des exemples ensuite. Un tel modèle serait léger à utiliser et contiendrait une
forme de compréhension des données.

Le prochain chapitre, « [Un modèle qui s'entraîne](docs/module2/50-entrainer-un-modele) », montre comment construire un tel modèle.
