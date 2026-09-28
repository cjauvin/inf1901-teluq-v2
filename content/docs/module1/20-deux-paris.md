---
title: "Deux paris rivaux (1956-1958)"
weight: 20
slug: deux-paris
---

# Deux paris rivaux (1956-1958)

## Le moment : l'été 1956 à Dartmouth

À l'été 1956, un petit groupe de chercheurs se réunit pendant deux mois sur le
campus du **Dartmouth College**, dans le New Hampshire, pour un atelier qui est
considéré comme l'**acte de naissance** de la discipline. L'expression
**« intelligence artificielle »** apparaît pour la première fois dans la
proposition de financement de cet atelier, rédigée l'année précédente par le jeune
mathématicien **John McCarthy**. Le mot est choisi en partie pour marquer une
rupture avec une étiquette alors dominante, la **cybernétique**.

{{< image src="/images/module1/dartmouth-hall.jpg" alt="Dartmouth Hall, un grand bâtiment géorgien en briques peintes en blanc, orné d'un fronton portant la date « 1784 » et surmonté d'un clocheton, sur le campus du Dartmouth College." title="Dartmouth Hall, sur le campus du Dartmouth College où se tint l'atelier de 1956." loading="lazy" >}}

<p class="image-credit">Dartmouth Hall (Dartmouth College). Photo : Kenneth C. Zirkel, <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>, via Wikimedia Commons.</p>

{{% hint info %}}
**La cybernétique.** Fondée en 1948 par le mathématicien Norbert Wiener (le mot
vient du grec *kubernêtês*, le pilote d'un navire), la cybernétique étudiait ce
que les machines et les êtres vivants ont en commun lorsqu'ils se **règlent
eux-mêmes**. Un thermostat qui maintient une température, un organisme qui
maintient la sienne et un missile qui corrige sa trajectoire obéissent au même
principe, la **rétroaction** (*feedback*). L'effet d'une action est mesuré et
renvoyé à celui qui agit, pour qu'il se corrige. Une bonne partie de ce qui suit
dans ce cours vient de là, en particulier l'idée d'une machine qui s'ajuste
d'après ses erreurs. Cependant, la cybernétique raisonnait en signaux continus, en
boucles et en organismes, à la frontière de la biologie et de l'ingénierie.
McCarthy voulait une science du raisonnement et des symboles et, selon certains
témoignages, ne tenait pas à devoir composer avec l'autorité de Wiener. Il a donc
choisi un nom nouveau.

*Le même mot grec a aussi donné son nom, en 2014, au logiciel
[Kubernetes](https://kubernetes.io/fr/), qui « pilote » des conteneurs dans les
centres de données, d'où son logo en forme de barre de navire. Les deux n'ont
en commun que l'étymologie.*
{{% /hint %}}

{{< image src="/images/module1/dartmouth-1956-participants.jpg" alt="Photo en noir et blanc de sept hommes souriants, assis sur la pelouse devant un bâtiment blanc aux volets sombres, Dartmouth Hall, à l'été 1956 : les organisateurs de l'atelier et quelques participants." title="Devant Dartmouth Hall, à l'été 1956 : les organisateurs de l'atelier et quelques participants." loading="lazy" >}}

<p class="image-credit">Devant Dartmouth Hall, été 1956. À l'arrière, de gauche à droite&nbsp;: Oliver Selfridge, Nathaniel Rochester, Marvin Minsky et John McCarthy&nbsp;; à l'avant&nbsp;: Ray Solomonoff, Peter Milner et Claude Shannon. Photo&nbsp;: famille Minsky.</p>

L'ambition affichée est très grande. La proposition postule que *« tout aspect
de l'apprentissage, ou de toute autre caractéristique de l'intelligence, peut en
principe être décrit avec une telle précision qu'une machine peut être construite
pour le simuler »* (en version originale : *« every aspect of learning or any
other feature of intelligence can in principle be so precisely described that a
machine can be made to simulate it »*). Les organisateurs sont McCarthy,
**Marvin Minsky**, **Claude Shannon** (le père de la théorie de l'information) et
**Nathaniel Rochester**, d'IBM. Ils pensent sincèrement qu'un groupe d'une dizaine
de personnes peut faire des progrès significatifs sur ce programme en un seul
été.

Ce travail, qu'ils pensaient mener en quelques étés, a occupé plusieurs
générations de chercheurs et n'est toujours pas terminé. L'atelier de Dartmouth a
cependant lancé le domaine. Très rapidement, deux familles d'idées sur la façon de
construire cette intelligence s'y dessinent.

{{% hint warning %}}
**Un mot qui a changé de sens.** Si vous abordez ce cours en pensant à ChatGPT,
il faut savoir que ce que McCarthy et ses collègues appelaient « intelligence
artificielle » en 1956 a très peu de rapport avec ce que ce mot désigne
aujourd'hui dans la conversation courante. Pour eux, l'IA consistait à faire
**raisonner** une machine : manipuler des symboles, appliquer des règles de
logique, explorer méthodiquement des possibilités, comme on le fait pour
démontrer un théorème ou jouer aux échecs. Aucune partie de ce programme
n'apprenait à partir de grandes quantités de données. Aujourd'hui, le mot « IA »
désigne presque toujours les **grands modèles de langage** et les modèles
apparentés qui génèrent des images. Ce sont d'immenses réseaux de neurones,
entraînés sur une bonne partie de ce que l'humanité a écrit, qui ne contiennent
aucune règle écrite à la main.

Ce module raconte ce renversement. L'expression a été créée par les partisans du
premier pari, celui de la logique. Elle est aujourd'hui associée aux héritiers du
second, celui du cerveau et de l'apprentissage, que les premiers ont longtemps
considéré comme une impasse. Entre les deux, il y a soixante-dix ans, deux
[« hivers »](docs/module1/60-hivers) et un renversement que rien ne laissait prévoir. Gardez
donc les deux sens à l'esprit. Dans les pages qui suivent, « IA » a d'abord le
sens qu'il avait à Dartmouth.
{{% /hint %}}

## Le premier pari : l'esprit comme logique

La première famille d'idées prolonge directement l'intuition de Turing. Si
penser consiste à calculer, alors **l'intelligence consiste à manipuler des
symboles selon des règles logiques**. Un symbole est ici un jeton qui représente
quelque chose (un mot, un objet, une idée). Raisonner consiste à combiner ces
jetons d'après des règles précises, comme un mathématicien enchaîne les étapes
d'une démonstration. Dans cette vision, il importe peu que la machine ressemble ou
non à un cerveau. Ce qui compte, c'est qu'elle possède les bons symboles et les
bonnes règles. On parle d'approche **descendante** (*top-down*), parce qu'on
programme le raisonnement explicitement, « par le haut ».

Cette approche a rapidement donné des résultats concrets. Dès 1956, un programme
nommé **Logic Theorist**, conçu par **Allen Newell** et **Herbert Simon** et
présenté à Dartmouth, démontre des théorèmes de logique mathématique tirés d'un
ouvrage de référence, les *Principia Mathematica* de Russell et Whitehead. Pour
l'une de ces démonstrations, il trouve même une solution plus élégante que celle
des auteurs. On le considère souvent comme le **premier programme d'intelligence
artificielle**, c'est-à-dire une machine qui ne calcule pas des nombres, mais qui
raisonne, du moins en apparence.

{{% hint info %}}
**Soixante-dix ans plus tard.** La démonstration de théorèmes par machine a
progressé d'une manière que Newell et Simon n'avaient pas prévue.
En 2025, des grands modèles de langage entraînés par renforcement ont atteint
le niveau d'une médaille d'or aux Olympiades internationales de mathématiques.
En septembre 2026, l'un d'eux a traduit toute la démonstration du dernier théorème
de Fermat dans **Lean**, un langage où chaque étape d'une preuve est vérifiée par la
machine. Les spécialistes estimaient ce travail à plusieurs années. Un autre système a annoncé avoir résolu une
version de l'un des sept problèmes du millénaire, celui des équations de
Navier-Stokes, un résultat que les mathématiciens sont encore en train de
vérifier. Ces machines raisonnent elles aussi, mais elles sont issues de l'autre
pari, celui de l'apprentissage, et ne contiennent aucune règle de logique écrite
à la main. Nous y reviendrons au [Module 4](docs/module4).
{{% /hint %}}

{{% hint info %}}
<img src="{{< rel "/images/module1/lean-logo.svg" >}}" alt="Le logo de Lean : le mot « LEAN » en capitales noires stylisées." class="logo-mono">

**Lean, un vérificateur de preuves.** Le langage **Lean**, dans lequel la
démonstration de Fermat a été traduite, a été créé en 2013 par Leonardo de Moura chez
Microsoft Research. Dans Lean, chaque étape d'une démonstration doit être justifiée
par une règle de logique précise. Un petit programme central, le *noyau*, vérifie
ensuite que chaque étape respecte ces règles. Si le noyau accepte la preuve, le
théorème est établi avec une certitude qu'aucune relecture humaine ne peut garantir
pour des démonstrations de centaines de pages. Par exemple, l'énoncé suivant est
vérifié par Lean :

```lean
theorem deux_plus_deux : 2 + 2 = 4 := by norm_num
```

Des mathématiciens du monde entier alimentent une bibliothèque commune,
**Mathlib**, qui contient déjà une grande partie des mathématiques enseignées à
l'université.

Lean appartient à la tradition symbolique présentée dans ce chapitre : des règles
explicites, appliquées mécaniquement. Il est aujourd'hui au centre d'une
combinaison des deux paris. Un modèle de langage, issu de l'apprentissage, propose
des étapes de démonstration, et Lean vérifie qu'elles sont correctes. Le modèle peut
se tromper, mais une erreur ne passe pas la vérification. C'est ainsi qu'ont été
obtenus plusieurs des résultats mentionnés ci-dessus. Pour en savoir plus :
[lean-lang.org](https://lean-lang.org/).
{{% /hint %}}

Ces succès suscitent un grand enthousiasme. Newell et Simon formulent une
hypothèse forte : un système qui manipule des symboles de la bonne manière
posséderait tout ce qu'il faut pour être intelligent. Pendant les décennies
suivantes, cette voie **symbolique** domine la recherche et obtient l'essentiel
des financements. Elle fait l'objet des chapitres suivants :
la [recherche](docs/module1/30-chercher-raisonner), la [représentation des
connaissances](docs/module1/40-representer-le-monde), les [systèmes
experts](docs/module1/50-systemes-experts).

## Le second pari : l'esprit comme cerveau

À la même époque, une idée très différente apparaît. Au lieu de programmer le
raisonnement explicitement, on pourrait construire une machine qui **apprend
seule, à partir d'exemples**, en s'inspirant de l'organe qui est déjà
intelligent, le **cerveau**.

Cette idée a une origine précise. En 1943, deux chercheurs, **Warren McCulloch**
et **Walter Pitts**, proposent un modèle mathématique très simplifié du neurone.
C'est une petite unité qui reçoit des signaux, les combine et « s'allume » ou non
selon que leur somme dépasse un certain seuil. Ils montrent qu'en reliant ces
unités en réseau, on peut en principe réaliser des opérations logiques. C'est le
premier lien établi entre le fonctionnement du cerveau et le calcul.

{{< image src="/images/module1/neurone-formel.svg" alt="Schéma d'un neurone formel : trois signaux d'entrée convergent vers un corps cellulaire qui les additionne (Σ) et compare la somme à un seuil ; en sortie, le neurone s'allume (1) si le seuil est dépassé, ou reste éteint (0)." title="Le neurone formel : combiner des signaux, puis s'activer si leur somme dépasse un seuil." loading="lazy" >}}

Il restait à expliquer comment un tel réseau pourrait apprendre. En 1949, le
psychologue **Donald Hebb** propose l'idée suivante : lorsque deux neurones
s'activent ensemble de façon répétée, le lien qui les unit se renforce
(« *neurons that fire together, wire together* »). Dans cette optique, apprendre
ne consiste pas à réécrire des règles, mais à **ajuster la force des
connexions**. C'est ce principe que Rosenblatt va appliquer dans sa machine.

{{< image src="/images/module1/regle-de-hebb.svg" alt="Schéma de la règle de Hebb : à gauche, deux neurones A et B au repos reliés par un lien fin ; à droite, lorsqu'ils s'activent ensemble, ils s'allument et le lien qui les unit s'épaissit, illustrant son renforcement." title="La règle de Hebb : deux neurones qui s'activent ensemble voient leur lien se renforcer." loading="lazy" >}}

En 1958, le psychologue **Frank Rosenblatt** construit une machine réelle fondée
sur cette idée, le **perceptron**. Au lieu de lui donner une règle, on montre au
perceptron des exemples, par exemple des images étiquetées « cercle » ou
« carré ». À chaque essai, s'il se trompe, il **ajuste légèrement ses réglages
internes** pour se rapprocher de la bonne réponse. Exemple après exemple, il
s'améliore, sans que personne ne lui ait jamais indiqué ce qui distingue un cercle
d'un carré. Il a appris. C'est l'approche **ascendante** (*bottom-up*) : on
n'écrit pas le savoir, on le laisse se former à partir des données.

Le perceptron suscite des attentes démesurées. En 1958, le *New York Times*,
rapportant les propos de Rosenblatt, annonce que la marine américaine a dévoilé
l'embryon d'une machine électronique qui « sera capable de marcher, parler, voir,
écrire, se reproduire et avoir conscience de son existence ». On était évidemment
très loin de ces capacités. L'idée centrale, celle d'une machine qui apprend de
ses erreurs, s'est cependant révélée très féconde. Elle est à la base de tout ce
que nous étudierons aux [modules 2](docs/module2), [3](docs/module3) et [4](docs/module4).

Le perceptron est l'**ancêtre direct des réseaux de neurones** actuels.
L'apprentissage profond d'aujourd'hui est, pour l'essentiel, un empilement de
perceptrons perfectionnés, en très grand nombre et sur de nombreuses couches.
Nous étudierons cette filiation au [**Module 3**](docs/module3).

## Deux univers parallèles

On pourrait croire que ces deux paris se sont succédé, d'abord l'un, puis
l'autre. Ce n'est pas le cas, et c'est l'une des idées les plus importantes de ce
cours. Ils sont nés **presque en même temps** et ont **coexisté en rivaux**
pendant plus d'un demi-siècle, chacun avec ses chercheurs, ses revues et ses
financements.

Ces deux paris reposent sur **deux conceptions de l'esprit**. Pour le camp
symbolique, l'esprit est essentiellement de la **logique**, c'est-à-dire des
symboles et des règles, indépendamment du support qui les réalise. Pour le camp
connexionniste, l'esprit est avant tout un **cerveau**, c'est-à-dire un réseau
qui s'ajuste à l'expérience. La question « qu'est-ce que penser ? » reçoit donc
deux réponses presque opposées.

Ces deux approches ne progressent pas en parallèle : elles **dominent tour à
tour**. Dès la fin des années 1960, comme nous le verrons dans « [Les hivers et la
bascule](docs/module1/60-hivers) », le camp symbolique met presque fin aux
recherches sur le perceptron, et
l'approche symbolique domine presque seule les vingt années suivantes. Il faut
attendre les années 2010, étudiées au [Module 3](docs/module3) de ce cours, pour que la tradition
connexionniste revienne au premier plan, sous le nom d'*apprentissage profond*.

{{% hint info %}}
La comparaison avec le cerveau est utile, mais il faut s'en méfier pour cette
raison même. Le « neurone » de McCulloch, Pitts et Rosenblatt est une version
extrêmement simplifiée du vrai neurone biologique. Nous y reviendrons en détail au [Module 3](docs/module3), au
moment où la tentation de confondre les deux sera la plus forte.
{{% /hint %}}

Pour le moment, nous laissons de côté le perceptron pour suivre le camp
symbolique, qui est le premier à connaître une période de succès, celle des
machines qui cherchent et qui raisonnent. C'est l'objet de « [Chercher et
raisonner](docs/module1/30-chercher-raisonner) ».
