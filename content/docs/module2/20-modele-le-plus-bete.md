---
title: "Le modèle le plus bête"
weight: 20
slug: modele-le-plus-bete
---

# Le modèle le plus bête

À la fin de la page « [Le problème](docs/module2/10-le-probleme) », nous avons posé une question qui peut sembler
absurde : quelle est la prédiction la plus bête qu'on puisse imaginer ? Cette
question mérite d'être prise au sérieux, parce que la pire réponse possible est
instructive. Elle nous obligera aussi à préciser ce qu'est un *modèle*.

## Toujours prédire la moyenne

Le pire « prédicteur » qu'on puisse concevoir est le suivant : pour n'importe
quelle maison, on ignore toutes ses caractéristiques (sa superficie, son âge, son
nombre de chambres) et on annonce toujours le **même** prix, le **prix moyen** de
toutes les maisons de notre liste.

Dans notre exemple, ce prix moyen est d'environ **500 000 \\$**. La prédiction ne
dépend donc plus de rien. Elle est de 500 000 \\$ pour un très petit studio, et
de 500 000 \\$ aussi pour un grand manoir. C'est évidemment absurde.

Ce prédicteur est cependant parfaitement défini, il ne tombe jamais en panne et
il donne toujours une réponse. Sur le nuage de points de la [page précédente](docs/module2/10-le-probleme/#notre-fil-rouge-des-maisons-à-vendre), il
correspond à une simple **ligne horizontale**, à la même hauteur (500 000 \\$)
quelle que soit la superficie. Cette ligne traverse le nuage en son milieu,
au-dessus des maisons bon marché et en dessous des plus chères.

{{< image src="/images/module2/maisons-baseline.svg" alt="Le nuage de maisons traversé par une droite horizontale à 500 000 $ : un modèle qui prédit toujours le prix moyen, sans tenir compte de la superficie." title="Le modèle le plus bête : une droite plate à 500 000 $, qui ignore complètement la superficie." loading="lazy" >}}

## La même bêtise, pour l'autre question

Le prédicteur le plus bête existe aussi pour la **seconde question** du chapitre
« [Le problème](docs/module2/10-le-probleme/#une-seconde-question-dune-tout-autre-nature) », *cette maison partira-t-elle vite ?* Il suit la même logique : il
ignore la maison qu'on lui présente et répond toujours la même chose.

Il ne peut cependant pas répondre la moyenne, parce qu'on ne peut pas faire la
moyenne de « oui » et de « non ». L'équivalent consiste à donner **la réponse la
plus fréquente**, celle qui revient le plus souvent dans nos registres. Si 60 %
des maisons déjà vendues ont trouvé preneur en moins de trente jours, ce
prédicteur répondra toujours « oui », aussi bien pour une maison neuve proche du
centre que pour une vieille maison des années 1970 située loin en banlieue.

Les deux questions sont de nature très différente, mais les deux prédicteurs ont
la **même structure** : une entrée qu'on ignore, une sortie constante et une
réponse tirée uniquement des données. Nous retrouverons souvent cette
ressemblance entre les deux questions.

## Qu'est-ce qu'un modèle, au juste ?

Nous venons d'appeler ce prédicteur un « modèle ». Il faut préciser le sens de ce
mot, qui sera central dans tout le module.

> Un **modèle**, c'est une recette qui transforme une description (l'entrée) en
> une prédiction (la sortie).

Notre prédicteur bête correspond à cette définition : on lui donne une maison en
entrée, et il renvoie un prix en sortie. Le fait qu'il ignore cette entrée ne
l'empêche pas d'être un modèle. C'est seulement un très mauvais modèle.

Ce modèle est composé d'**un seul nombre**, le prix moyen (500 000 \\$). Ce
nombre représente ce que le modèle a « retenu » des données ; on l'appelle son
**paramètre**. Le calcul de ce nombre (la moyenne des prix observés) est déjà une
forme simple d'*apprentissage*, puisque le modèle a tiré sa seule connaissance
des exemples qu'on lui a fournis.

Ce nombre n'est donc pas arbitraire. On aurait pu annoncer 12 \\$, ou un
milliard. Ce modèle aurait été tout aussi bête, puisqu'il ignorerait lui aussi la
maison présentée, mais il se tromperait beaucoup plus. Le prix moyen a été
**calculé** à partir des ventes passées, et il a un sens : parmi tous les nombres
qu'on pourrait annoncer pour toutes les maisons à la fois, c'est celui qui se
trompe le moins, en moyenne. La faiblesse du modèle vient de ce qu'il ignore, et
non de ce qu'il retient. Le modèle jumeau fonctionne de la même façon. Son unique
paramètre est la réponse majoritaire (« oui »), obtenue en comptant plutôt qu'en
calculant une moyenne. Ce choix est lui aussi justifié, puisque c'est la réponse
qui a le plus de chances d'être correcte quand on ne sait rien d'autre.

Le reste du module développe cette idée. Les modèles que nous construirons
auront davantage de paramètres : un, puis deux, puis des milliers, puis des
milliards. La principale difficulté consistera à trouver les bonnes valeurs pour
ces paramètres, celles qui correspondent le mieux aux données. La structure
restera cependant toujours la même : une entrée, une recette réglée par des
paramètres, une sortie.

## Pourquoi un modèle aussi bête est utile

Ce modèle est très mauvais, mais il est utile parce qu'il fournit un **étalon**,
c'est-à-dire un point de comparaison pour juger tous les modèles suivants.

Les mots « bon » et « mauvais » n'ont pas de sens dans l'absolu. Pour savoir si
un modèle a de la valeur, il faut une référence. La référence la plus élémentaire
consiste à vérifier s'il fait mieux qu'un modèle qui ne regarde rien du tout. Un
modèle, même sophistiqué, qui ne fait pas mieux que « toujours 500 000 \\$ » n'a
rien appris d'utile.

On peut faire cette comparaison concrètement, sans formule, en mesurant **de
combien un modèle se trompe, en moyenne**. Pour le prédicteur bête, l'écart entre
le prix annoncé (toujours 500 000 \\$) et le vrai prix dépasse 250 000 \\$ pour
les maisons situées aux extrêmes. C'est cette « distance à la vérité » qu'un
meilleur modèle cherchera à réduire. Nous lui donnerons au chapitre « [Un modèle qui s'entraîne](docs/module2/50-entrainer-un-modele/#mesurer-lerreur) » un nom et une
définition précise, la *fonction d'erreur*, mais l'idée suffit pour l'instant :
un bon modèle est un modèle qui se trompe moins.

{{< image src="/images/module2/maisons-erreurs.svg" alt="Le nuage de maisons et la droite plate à 500 000 $, avec un segment vertical rouge reliant chaque maison à la droite : c'est l'erreur du modèle sur cette maison, longue aux extrêmes et courte près du centre." title="L'erreur du modèle, maison par maison : l'écart vertical entre le vrai prix et la prédiction." loading="lazy" >}}

En pratique, ce rôle d'étalon évite bien des erreurs d'interprétation. Un chiffre
de performance ne signifie rien à lui seul. Devant un modèle, la première
question à poser est toujours de savoir s'il fait vraiment mieux que de prédire
bêtement la moyenne. La réponse est assez souvent non, et c'est l'étalon qui
permet de le constater.

Pour la question en oui/non, le principe est le même, mais on compte autrement.
Au lieu d'un écart en dollars, on regarde **quelle proportion des réponses le
modèle obtient justes**. Le prédicteur jumeau, qui répond « oui » à tout, a donc
raison dans 60 % des cas. C'est l'étalon à battre.

{{< image src="/images/module2/maisons-erreurs-oui-non.svg" alt="Le nuage coloré de la page précédente : les mêmes maisons, aux mêmes places, la distance du centre-ville en abscisse et l'année de construction en ordonnée. Toutes sont maintenant bleues, parce que le modèle répond « oui » (vendue en moins de 30 jours) pour chacune, sans tenir compte de leurs caractéristiques. Un ✗ rouge marque celles qui s'étaient en réalité vendues lentement, c'est-à-dire celles qui étaient rouges sur la figure d'origine. Ce sont ses erreurs, et elles occupent presque tout l'amas du bas à droite, celui des maisons éloignées et anciennes." title="Le prédicteur jumeau colore toutes les maisons en « oui », et les ✗ marquent celles où il se trompe. On ne mesure plus un écart en dollars, on compte les réponses justes." loading="lazy" >}}

Il s'agit du nuage coloré de la [page précédente](docs/module2/10-le-probleme/#une-seconde-question-dune-tout-autre-nature), sans modification : les **mêmes
maisons**, aux mêmes places. Seule leur couleur a changé. Comme le modèle répond
« oui » partout, il les colore toutes en bleu, et les ✗ indiquent celles qui
étaient rouges. Presque tous les ✗ se trouvent dans l'amas du bas à droite,
celui des maisons éloignées et anciennes. Le prédicteur bête se trompe sur
presque tout cet amas, ce qui est normal, puisqu'il répond « oui » sans tenir
compte de la distance ni de l'année.

On peut comparer cette figure avec le graphique des écarts de prix [présenté plus
haut](#pourquoi-un-modèle-aussi-bête-est-utile). Les axes sont différents (ils ne peuvent pas être les mêmes, parce que les
deux questions ne se lisent pas dans le même plan), mais la différence principale
est ailleurs. Dans le graphique des prix, chaque maison portait un segment plus
ou moins long, et l'erreur se **mesurait**. Ici, chaque réponse est simplement
juste ou fausse, et l'erreur se **compte**.

{{% hint warning %}}
Cet étalon peut être trompeur, et ce cas est instructif. Prenons une question
beaucoup plus déséquilibrée, *ce courriel est-il un pourriel ?*, dans une boîte
où 99 % des messages sont légitimes. Le prédicteur le plus bête, qui répond « ce
n'est jamais un pourriel », obtient **99 % de bonnes réponses**, tout en étant
inutile, puisqu'il ne détecte aucun pourriel. Un chiffre élevé peut donc cacher
un modèle sans valeur. Nous y reviendrons dans « [Bien évaluer un modèle](docs/module2/75-bien-evaluer/#compter-juste-les-métriques) », car bien mesurer la qualité d'un
modèle est plus difficile qu'il n'y paraît.
{{% /hint %}}

## Leur défaut, et ce qu'il révèle

Les deux modèles ont le **même** défaut, qui est évident. Le premier attribue le
même prix à un studio et à un manoir. Le second prévoit une vente rapide aussi
bien pour une maison neuve près du centre que pour une vieille maison à vingt
kilomètres de là. Aucun des deux ne tient compte de la maison qu'on lui présente.
Toute l'information utile (la superficie, l'âge, la distance) est disponible, et
ils ne l'utilisent pas.

Les deux dernières figures montrent aussi un point important : **les erreurs ne
sont pas dispersées au hasard**. Les segments les plus longs se trouvent aux
extrémités du nuage, du côté des maisons très bon marché ou très chères, et les
✗ se concentrent dans un seul coin du graphique, celui des maisons éloignées et
anciennes. Or une erreur qui se concentre à un endroit est une erreur qu'on peut
**prévoir**, donc corriger. Si les modèles se trompaient de façon totalement
imprévisible, on ne pourrait rien en tirer. C'est parce que leurs erreurs forment
un motif qu'il est possible de les améliorer.

C'est là que se trouve la marge de progression. Si la moyenne (ou la réponse
majoritaire) est le meilleur point de départ quand on ne sait rien d'une maison,
la seule façon de faire mieux est de **cesser de l'ignorer**, c'est-à-dire de
tenir compte de ses caractéristiques. Une grande maison devrait faire monter la
prédiction de prix, et une vieille maison devrait la faire baisser. Une maison
éloignée du centre devrait faire pencher la réponse du second modèle vers le
« non ». Un bon modèle est donc un modèle qui tient compte de l'entrée.

Il faut cependant d'abord préciser ce que signifie concrètement « tenir compte de
l'entrée », c'est-à-dire ce qu'est une « donnée » pour une machine, et comment
une maison, une image ou un courriel est transformé en quelque chose qu'un modèle
peut manipuler. C'est l'objet de la [page
suivante](docs/module2/30-les-donnees).
