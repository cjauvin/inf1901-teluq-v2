---
title: "Généraliser"
weight: 70
slug: generaliser
---

# Généraliser

Le chapitre « [Poser des questions : les arbres de décision](docs/module2/65-arbres-de-decision/#et-sur-des-données-neuves) » s'est terminé sur un doute. Nous savons maintenant
entraîner plusieurs sortes de modèles (une droite qui prédit un prix, des
classificateurs qui rangent en catégories), et tous apprennent de la même façon,
en rendant leur erreur la plus petite possible sur les exemples qu'on leur
montre. Ce résultat ne prouve cependant rien. Ce qui compte n'est pas qu'un
modèle réussisse bien sur les données passées, mais qu'il se comporte bien sur
des données nouvelles.

Le problème tient à une distinction. Un modèle peut avoir vraiment **appris**
quelque chose des données, c'est-à-dire une régularité qu'il pourra appliquer
ailleurs, ou s'être contenté de les **retenir**. Les deux cas se ressemblent
beaucoup tant qu'on regarde les exemples d'entraînement. Ils ne se distinguent
que devant des données nouvelles, et on découvre parfois alors qu'un modèle qui
semblait bon ne vaut rien.

La capacité à bien se comporter au-delà des exemples appris s'appelle la
**généralisation**. C'est elle, et non l'erreur d'entraînement, qui mesure la
valeur réelle d'un modèle. Ce chapitre lui est consacré. Il explique comment la
mesurer, pourquoi elle est difficile à obtenir et ce qu'elle révèle sur la
nature des modèles.

## Un modèle se juge sur ce qu'il n'a jamais vu

La solution est simple : **on cache des exemples au modèle.** Avant
l'entraînement, on met de côté une partie des données, par exemple un cinquième.
Le modèle apprend sur le reste, sans jamais voir cette réserve. Une fois le
modèle entraîné, on l'évalue sur la réserve. Ces exemples sont nouveaux pour
lui, mais nous connaissons les bonnes réponses. Sa performance sur cette réserve
donne une estimation honnête de ce qu'il fera face à des données réellement
nouvelles.

{{< image src="/images/module2/jeu-de-test.svg" alt="L'ensemble des données est coupé en deux : un grand bloc « entraînement » sur lequel le modèle apprend, et un petit bloc « test » mis de côté, que le modèle ne voit jamais pendant l'entraînement et qui sert à mesurer sa généralisation." title="On sépare les données : le modèle apprend sur l'ensemble d'entraînement, et l'ensemble de test, mis de côté, sert à mesurer sa généralisation." loading="lazy" >}}

L'analogie de l'examen s'applique bien. Un enseignant qui noterait ses étudiants
uniquement sur les questions distribuées d'avance pour la révision ne mesurerait
pas grand-chose, parce qu'on peut apprendre ces réponses par cœur sans
comprendre. C'est le sur-apprentissage (*overfitting*) de l'étudiant, et le jeu
de test permet de le détecter. Pour évaluer la compréhension, il faut des
questions nouvelles. On procède de la même façon avec un modèle.

Ces deux parties des données ont un nom. L'**ensemble d'entraînement** sert à
l'apprentissage du modèle, et on y mesure l'**erreur d'entraînement**.
L'**ensemble de test** reste à l'écart jusqu'à la fin et sert à mesurer
l'**erreur de test**, la seule qui estime la généralisation. La règle d'or est
qu'*on ne touche jamais au jeu de test pendant l'entraînement.* Si le modèle
apprend, même indirectement, sur ses propres données d'examen, le test ne veut
plus rien dire.

{{% hint info %}}

Lorsqu'il faut *régler* quelque chose (la valeur de $k$ pour kNN, ou le taux
d'apprentissage vu dans [*Un modèle qui s'entraîne*](docs/module2/50-entrainer-un-modele)), on ne peut pas non plus utiliser le
jeu de test pour choisir, car il ne serait alors plus neuf. On réserve donc un
troisième ensemble, l'**ensemble de validation**, consacré à ces réglages. Le jeu
de test reste intact pour l'évaluation finale.

{{% /hint %}}

{{% hint warning %}}
**La règle d'or, à l'échelle d'aujourd'hui : les grands modèles de langage.**
Toute cette section suppose qu'on sait ce que le modèle a vu pendant
l'entraînement. Pour un LLM, ce n'est plus vraiment possible. Ses données
d'entraînement, des milliers de milliards de mots recueillis sur le Web, sont si
vastes que personne n'en connaît le contenu précis, pas même ceux qui l'ont
entraîné. Or les examens qu'on lui fait passer (un problème de mathématiques,
une question d'un test standardisé, un exercice de programmation) ont très
probablement circulé sur le Web, avec leur corrigé. On ne peut donc plus savoir
avec certitude si le modèle a raisonné ou s'il a retrouvé la réponse. C'est le
cas interdit par la règle d'or, un modèle qui a vu, même indirectement, ses
données d'examen, mais à une échelle où personne ne peut plus le contrôler. Il
faut donc se méfier des scores impressionnants qu'on annonce.

Le problème ne concerne pas seulement la mesure. Au début du module, la question
de la 1001ᵉ image reposait sur le fait de savoir si elle faisait partie des
1000. Pour un LLM, on ne peut plus répondre à cette question. Distinguer ce
qu'un modèle sait déjà (parce que c'était dans ses données) de ce qu'il apporte
de nouveau (parce qu'il généralise) est devenu, pour ces systèmes, une question
ouverte, et en partie philosophique : où finit la mémoire, et où commence la
compréhension ? Ce chapitre a posé cette question sur vingt maisons. Le
[Module 4](docs/module4) la reprendra à propos d'un modèle qui a lu une grande
partie de ce que l'humanité a écrit.
{{% /hint %}}

## Linéaire ou non-linéaire : ce qu'un modèle peut dessiner

Revenons sur les modèles que nous avons construits. La régression linéaire
d'[*Un modèle qui s'entraîne*](docs/module2/50-entrainer-un-modele) produit une droite. La frontière de la régression
logistique est une droite. Celle de Bayes naïf est aussi une droite, comme nous
l'avions remarqué. Même notre filtre anti-pourriel, malgré son grand nombre de
mots, prenait une décision linéaire. Ces modèles ont donc un point commun.

Ils tirent tous leur décision d'une **somme pondérée** des caractéristiques.
Chaque attribut pousse d'un côté ou de l'autre, proportionnellement à son poids,
et la décision dépend du total. Sur le plan géométrique, le résultat est
toujours une droite (un plan en trois dimensions, un *hyperplan* au-delà). On
appelle ces modèles des **modèles linéaires**.

La question est alors de savoir s'il existe des choses qu'**aucune droite** ne
peut apprendre.

La réponse est oui, et vous connaissez déjà l'exemple le plus célèbre de cette
limite. Le **perceptron**, présenté au [Module 1](docs/module1/60-hivers/#le-premier-hiver-la-mort-du-perceptron-1969), a été mis en échec sur ce
point en 1969. L'exemple en cause est le **XOR**, *l'un ou l'autre, mais pas les
deux*, la règle de l'interrupteur va-et-vient qui commande une lampe au bout
d'un couloir. Si on place ses quatre cas dans le plan, les deux cas « éteint »
se trouvent sur une diagonale et les deux cas « allumé » sur l'autre.

{{< image src="/images/module2/xor.svg" alt="Deux panneaux illustrant le XOR. Dans chacun, quatre points aux coins d'un carré : deux bleus sur une diagonale (bas-gauche et haut-droit), deux rouges sur l'autre (haut-gauche et bas-droit). Chaque panneau montre une droite différente traversant le plan pour tenter de séparer les couleurs ; dans les deux cas, un point bleu reste du côté des rouges, cerclé de rouge et marqué d'une croix. Aucune droite ne réussit." title="Le XOR : quelle que soit la droite tracée, un point reste du mauvais côté. C'est la limite d'un modèle linéaire." loading="lazy" >}}

Quelle que soit la droite choisie et son inclinaison, il reste toujours un point
du mauvais côté. Il ne s'agit pas d'un manque d'astuce, mais d'une
impossibilité.

Il faut bien distinguer ce point de tout ce qui précède : **cet échec n'a rien à
voir avec le bruit ni avec le manque de données**. Avec un million d'exemples
parfaits, sans aucune erreur de mesure, un modèle linéaire échouera de la même
façon. Le problème ne vient pas d'un mauvais réglage ni d'un manque
d'entraînement. Il vient du **répertoire de formes** du modèle, qui ne contient
pas la réponse. On appelle ce répertoire la **capacité** du modèle (ou son
*expressivité*), c'est-à-dire l'ensemble des frontières qu'il peut dessiner. Un
modèle linéaire ne peut dessiner qu'une seule famille de frontières, les
droites.

kNN, au contraire, a une frontière qui peut prendre n'importe quelle forme. Elle
peut entourer des îlots et contourner des groupes de points, car aucune
contrainte de forme ne s'applique à elle. kNN résout le XOR sans difficulté,
parce que chaque point regarde ses voisins et que les voisins d'un coin bleu sont
bleus. kNN est donc un modèle **non-linéaire**, et c'était le [premier que nous
avons vu](docs/module2/40-predire-par-ressemblance/#les-k-plus-proches-voisins).

L'arbre de décision de la [page précédente](docs/module2/65-arbres-de-decision) résout lui aussi le XOR, en deux
questions, « à droite ? » puis « en haut ? ». Il obtient quatre rectangles, un
par coin, soit la frontière que le perceptron ne pouvait pas tracer. Ses coupes
parallèles aux axes sont une autre façon d'être non-linéaire, très différente de
celle de kNN.

Il y a donc deux familles de modèles, et une question à se poser avant toute
autre devant un problème : *la vérité que je cherche peut-elle tenir dans le
répertoire de mon modèle ?* Si elle n'y est pas, aucun réglage et aucune donnée
supplémentaire ne l'y mettront.

L'apprentissage automatique classique offre deux moyens de contourner cette
limite. Le premier vient d'être présenté, il consiste à prendre un modèle
non-linéaire comme kNN. Le second consiste à **construire soi-même la bonne
caractéristique**. Si on ajoute aux deux entrées leur produit $x_1 \cdot x_2$,
le XOR devient séparable par une droite dans ce nouvel espace. Cependant, c'est
l'humain qui a dû trouver cette astuce, et il arrive que personne ne sache quelle
caractéristique construire.

Le Module 3 traitera cette question, dans « [Une couche cachée](docs/module3/20-une-couche-cachee/#ce-que-fait-la-couche-cachée-changer-de-point-de-vue) ». Les réseaux de neurones
apprennent à **construire eux-mêmes** les caractéristiques qui rendent le
problème séparable, en empilant des couches. La limite constatée en 1969 sera
dépassée en 1986. C'est la question que le [Module 1](docs/module1/60-hivers/#le-premier-hiver-la-mort-du-perceptron-1969) avait laissée ouverte, et le [Module 3](docs/module3/30-entrainer-un-reseau/#1986) y répondra.

Cependant, la capacité de produire des frontières courbes n'est pas un avantage
en soi. Un modèle capable de suivre n'importe quelle forme peut aussi suivre des
formes qui ne correspondent à rien. C'est le sujet de la [section suivante](#trop-coller-ou-trop-lisser-le-compromis-biais-variance).

## Trop coller, ou trop lisser : le compromis biais-variance

Nous venons de voir qu'un modèle doit être assez *expressif* pour que la vérité
tienne dans son répertoire. L'excès inverse pose aussi un problème : un modèle
trop souple finit par suivre le hasard autant que le signal. Pour observer ce
compromis (et le mesurer, puisque nous savons maintenant le faire), revenons à
kNN. Son seul réglage, le nombre de voisins $k$, contrôle directement la
souplesse du modèle. Dans l'applet ci-dessous, faites glisser lentement $k$
d'une extrémité à l'autre et observez la frontière.

{{< applet src="/html/applets/knn.html" height="692" >}}

Avec **$k = 1$**, chaque point ne consulte que son plus proche voisin. La
frontière se déforme pour entourer chaque exemple, forme des îlots autour des
points isolés et suit tous les détails. L'erreur d'entraînement est nulle,
puisque chaque exemple est son propre plus proche voisin. Cependant, cette
frontière tient compte de tous les accidents des données. Pour un point un peu
aberrant ou pour du bruit, elle se déforme quand même. C'est le
**sur-apprentissage** (*overfitting*). Il correspond à l'étudiant qui a appris le
corrigé par cœur, avec ses erreurs, sans le comprendre. Sur des données
nouvelles, il se trompe.

À l'autre extrême, avec **$k$ très grand**, chaque prédiction fait la moyenne de
tant de voisins que la frontière devient une courbe lisse, presque droite. Elle
peut alors effacer des structures qui existent réellement dans les données.
C'est le défaut inverse, le **sous-apprentissage** (*underfitting*) : le modèle
est trop rigide pour suivre la forme réelle des données.

Il y a donc deux façons d'échouer, qui ont chacune un nom :

- la **variance** est la sensibilité du modèle au hasard de l'échantillon (du
  côté des petites valeurs de $k$). Si on change quelques points
  d'entraînement, un modèle à haute variance change complètement ;
- le **biais** est la rigidité propre au modèle (du côté des grandes valeurs de
  $k$), c'est-à-dire son incapacité *systématique* à représenter la forme réelle
  des données, quels que soient les points qu'on lui montre.

{{% hint info %}}
**Qu'est-ce que le bruit ?** Nous disons qu'un modèle trop souple « suit le
bruit ». Cela signifie que les données ne sont jamais un signal pur. Le prix
d'une maison est une tendance (plus la maison est grande, plus elle est chère) à
laquelle s'ajoute une part aléatoire : l'humeur du vendeur, la saison, une
négociation et beaucoup d'autres facteurs que le registre n'a pas notés. Nos
vingt maisons ne sont pas sur la droite, elles sont autour, et l'écart de
chacune correspond à ce bruit. Un bon modèle apprend la tendance et ignore le
bruit. Un modèle trop souple apprend les deux, et le bruit qu'il a appris ne se
reproduira pas pour la maison suivante, puisqu'il est aléatoire. La courbe en U
présentée plus bas découle de cette idée : toute donnée contient une part qu'il
ne faut pas apprendre.
{{% /hint %}}

Voici l'une des idées les plus importantes du domaine. Quand on rend un modèle
plus souple (ici, en diminuant $k$), son erreur d'entraînement ne fait que
diminuer, car un modèle flexible s'ajuste toujours mieux aux données qu'il a
déjà vues. Son erreur de test suit au contraire une courbe en **U**. Elle
diminue d'abord, parce que le modèle représente mieux les régularités réelles,
puis elle **augmente** dès que le modèle commence à suivre le bruit. Le meilleur
modèle se trouve au bas du U, à l'équilibre entre biais et variance.

{{< image src="/images/module2/bias-vs-variance-with-errors.png" alt="Deux courbes en fonction de k. L'erreur d'entraînement (rouge) croît régulièrement de k=1 à k=21. L'erreur de test (bleu) a une forme en U : elle décroît, atteint un minimum, puis remonte. Deux droites diagonales figurent la variance (décroissante) et le biais (croissant) ; leur croisement marque le minimum de l'erreur de test." title="L'erreur de test (en bleu) suit une courbe en U : trop de variance à gauche, trop de biais à droite. Le meilleur modèle est au creux." loading="lazy" >}}

Ce phénomène **n'est pas propre à kNN.** Chaque modèle a un réglage de
souplesse : le nombre de termes d'une courbe plus souple qu'une droite ([nous le
verrons plus bas](#garder-un-modèle-riche-mais-le-tenir-en-laisse-la-régularisation)), la profondeur d'un arbre de décision ou le nombre de
paramètres d'un réseau de neurones. Chacun présente la même courbe en U et le
même arbitrage entre s'ajuster aux données et lisser. C'est le **compromis
biais-variance**, et savoir le régler est une compétence essentielle en
apprentissage automatique.


## Garder un modèle riche, mais le tenir en laisse : la régularisation

Le compromis biais-variance semble ne laisser qu'un seul moyen d'action,
diminuer la souplesse du modèle, comme nous l'avons fait avec kNN en augmentant
$k$ ou avec l'arbre en limitant sa profondeur. Cette solution a cependant des
limites. Elle restreint le modèle avant même qu'il ait vu les données, et le
réglage est grossier, puisqu'il se fait par paliers. Or on veut parfois un modèle
riche, capable de dessiner des formes compliquées si les données l'exigent, mais
qui ne suive pas les moindres accidents des données.

Il existe une troisième approche, plus fine, qui se résume ainsi : **au lieu de
limiter la souplesse du modèle, on la pénalise.** La fonction d'erreur vue dans
[*Un modèle qui s'entraîne*](docs/module2/50-entrainer-un-modele) mesure à quel
point le modèle se trompe sur les exemples, et l'entraînement consiste à la
faire diminuer. On y ajoute un second terme, une **pénalité** qui augmente avec
la *complexité* du modèle :

$$\text{erreur totale} = \text{erreur sur les données} + \lambda \times \text{complexité}$$

Le modèle doit alors trouver un équilibre. S'ajuster aux points fait diminuer le
premier terme, mais augmente le second. Le modèle ne prendra une forme
compliquée que si le gain le justifie. La descente de gradient va toujours vers
le point le plus bas, mais dans un paysage modifié où les régions qui
correspondent à des modèles trop compliqués ont été relevées.

Ce principe correspond à une idée vieille de sept siècles, le **rasoir
d'Occam** : entre deux explications qui rendent compte des mêmes faits, il faut
préférer la plus simple. La pénalité en est une traduction chiffrée. Elle
n'affirme pas que le monde est simple. Elle impose qu'un modèle reste simple
tant que les données n'exigent pas davantage, et que chaque complication
apporte un gain visible. La courbe en U de la [section précédente](#trop-coller-ou-trop-lisser-le-compromis-biais-variance) illustre
expérimentalement ce principe : au-delà d'un certain point, la complexité
supplémentaire ne sert qu'à apprendre du bruit.

Pour observer l'effet de la pénalité, il faut un modèle assez souple pour
faire du sur-apprentissage (*overfitting*). Reprenons la droite d'*Un modèle qui
s'entraîne* et rendons-la plus souple. Au lieu de
$\text{prix} = m \times \text{superficie} + b$, on autorise aussi des termes en
superficie², superficie³, et ainsi de suite jusqu'à la puissance 12. Une telle
courbe s'appelle un *polynôme*, et chaque terme ajouté apporte un paramètre de
plus, ce qui fait passer le modèle de deux à treize paramètres. Le réglage de
souplesse est ici le nombre de termes, appelé le *degré*. Avec treize
paramètres pour vingt maisons, la courbe peut facilement passer en zigzag entre
les points.

Il reste à définir concrètement la complexité. La réponse la plus courante est
simple : **la taille des paramètres.** Un polynôme qui passe en zigzag entre les
points doit monter et descendre rapidement. Pour cela, il lui faut des
coefficients très grands, qui se compensent presque entre eux et ne laissent
apparaître que de petites bosses. Obliger les coefficients à rester petits
oblige donc la courbe à rester régulière. La pénalité s'écrit alors comme la
somme des carrés des paramètres, et le reste ne change pas : même modèle, même
degré, même descente.

{{< image src="/images/module2/regularisation.svg" alt="Deux panneaux montrant le même nuage de maisons (superficie en abscisse, prix en ordonnée) et le même polynôme de degré 12 ajusté aux données. À gauche, sans pénalité : la courbe ondule pour passer au plus près de chaque point, avec des bosses et des creux entre eux, et s'envole aux bords. À droite, avec une pénalité sur la taille des coefficients : le même polynôme se calme et suit la tendance générale, presque une droite." title="Même modèle, même degré ; seule la pénalité change. À gauche, le polynôme sans pénalité suit le bruit ; à droite, avec la pénalité, il suit la tendance." loading="lazy" >}}

Le nombre $\lambda$ règle la sévérité de la pénalité. Avec une valeur nulle, on
retrouve le modèle sans contrainte. Avec une valeur trop grande, tous les
paramètres sont écrasés et on retombe dans le sous-apprentissage
(*underfitting*), avec au bout du compte une droite horizontale. C'est un
hyper-paramètre de plus, et on le choisit comme les autres, sur l'ensemble de
validation et jamais sur le jeu de test.

Cette idée porte des noms différents selon les modèles. Pour la droite et les
modèles apparentés, on parle de *régression ridge* (pénalité sur les carrés) ou
de *lasso* (pénalité sur les valeurs absolues, qui a la propriété de mettre
certains paramètres exactement à zéro, et donc d'*éliminer* des
caractéristiques). Pour les réseaux de neurones, on parle de *weight decay*, qui
désigne le même terme. D'autres méthodes ne passent pas par la fonction
d'erreur, mais visent le même but, empêcher le modèle de suivre le bruit. On
peut arrêter l'entraînement avant que le modèle s'ajuste trop aux données
(l'*arrêt précoce*) ou désactiver au hasard une partie des neurones à chaque
étape (le *dropout*). Pour l'arbre, l'**élagage** consiste à le laisser croître,
puis à couper les branches qui n'apportent que du détail. Le
[Module 3](docs/module3/30-entrainer-un-reseau/#lentraînement-en-pratique) reviendra sur ces méthodes. Elles reposent toutes sur
la même idée : la souplesse est une ressource, et un bon modèle est un modèle
riche dont on contrôle la souplesse.

{{% hint info %}}

Une question reste ouverte pour plus tard. Si trop de souplesse nuit, comment
les très grands réseaux de neurones actuels, qui ont des centaines de milliards
de paramètres et donc une souplesse considérable, parviennent-ils à généraliser ?
La réponse, qui remet en question la courbe en U, sera présentée au
[Module 3](docs/module3/40-apprentissage-profond/#plus-de-paramètres-que-dexemples).

{{% /hint %}}

## Paramétrique ou non-paramétrique

Il existe une seconde façon importante de classer les modèles. Elle ne porte pas
sur leur souplesse, mais sur ce qu'il en reste une fois l'entraînement terminé.
La question est de savoir si le modèle a **résumé** les données en un petit
nombre de réglages ou s'il les **conserve**.

kNN, comme on l'a vu à propos de son [angle mort](docs/module2/40-predire-par-ressemblance/#langle-mort-de-knn), n'a rien à apprendre à proprement
parler. Il n'a pas de paramètres à régler. Pour prédire, il consulte directement
les exemples mémorisés, et les données constituent donc le modèle. Par
conséquent, sa taille augmente avec le jeu de données. Avec mille exemples, il
faut conserver mille exemples, et avec un million, un million. On dit d'un tel
modèle qu'il est **non-paramétrique**, parce qu'il ne résume pas les données
dans un nombre fixe de réglages et qu'il s'appuie directement sur elles.

À l'opposé, une fois la pente et l'ordonnée à l'origine de notre droite de
régression trouvées, on peut **se débarrasser des données**. Il ne reste que
deux nombres, $m$ et $b$, et ils suffisent pour prédire. C'est aussi le cas de
la régression logistique (un poids par caractéristique) et de Bayes naïf (une
moyenne et une dispersion par classe, ou une probabilité par mot). Ces modèles
sont **paramétriques**. Ils résument toute leur connaissance dans un ensemble de
paramètres dont la taille est *fixée d'avance*, que l'apprentissage ait porté
sur cent exemples ou sur cent millions. Cette distinction était déjà présente
dans *Un modèle qui s'entraîne* : le modèle le plus bête résumait tout en *un*
nombre, la droite en *deux*, et kNN en *aucun*. Il s'agissait déjà de l'axe
paramétrique / non-paramétrique.

Chaque famille a ses avantages et ses inconvénients :

- le modèle **paramétrique** est léger et rapide pour la prédiction, et il
  généralise grâce à la compression qu'il impose aux données. Cependant, il
  *suppose une forme* (une droite, par exemple). Si la structure réelle des
  données n'a pas cette forme, aucun réglage ne corrigera le problème. C'est du
  **biais** ;
- le modèle **non-paramétrique** ne suppose presque rien sur la forme et peut
  représenter des structures très complexes. Cependant, il est lourd (il faut
  tout conserver), lent pour la prédiction et plus exposé au risque de suivre le
  bruit. C'est de la **variance**.

On retrouve ici le [compromis biais-variance](#trop-coller-ou-trop-lisser-le-compromis-biais-variance). Résumer les données ou
tout conserver, supposer une forme ou suivre les données : il n'existe pas de
réponse universelle. Il faut faire des choix adaptés au problème, et c'est une
part importante du travail dans la discipline.

{{< image src="/images/module2/parametrique-vs-non.svg" alt="À gauche, un nuage de points est résumé par une droite réduite à deux réglages m et b : le modèle paramétrique distille les données et peut ensuite les jeter. À droite, les mêmes points sont conservés tels quels : le modèle non-paramétrique garde toutes les données et s'appuie dessus pour prédire." title="Paramétrique : résumer les données en quelques réglages, puis s'en débarrasser. Non-paramétrique : conserver toutes les données et s'appuyer dessus." loading="lazy" >}}

Nous savons maintenant ce qu'un modèle peut dessiner, jusqu'à quel point il
faut le laisser se courber et comment contrôler sa souplesse. Il reste à
mesurer tout cela correctement, car un score peut être trompeur de plusieurs
façons. C'est l'objet de la page suivante, « [Bien évaluer un modèle](docs/module2/75-bien-evaluer) ».
