---
title: "L'attention et le Transformer"
weight: 70
slug: attention-transformer
---

# L'attention et le Transformer

Le chapitre
« [Lire une séquence](docs/module3/60-reseaux-recurrents/#les-limites) » s'est
terminé sur trois limites des réseaux récurrents (*recurrent neural networks*,
RNN) : toute une phrase passe par un seul état, le calcul avance une étape à la
fois, et les éléments lointains s'oublient. Ce chapitre présente le mécanisme qui a
levé ces limites, l'**attention**, puis l'architecture construite autour de lui, le
**Transformer**. Il traite le Transformer comme une architecture, au même titre que
les réseaux convolutifs ou récurrents. Ce
qu'il permet de faire avec le langage est le sujet du [Module 4](docs/module4).

Le Transformer est lui aussi fait des mêmes briques. Son
[biais inductif](docs/module3/50-reseaux-convolutifs) est le plus faible des trois :
chaque élément peut consulter tous les autres, quelle que soit leur distance, et
l'architecture ne suppose presque rien sur l'ordre ou le voisinage. Le Transformer
doit donc presque tout apprendre des données, ce qui demande d'énormes quantités
d'exemples, mais il s'adapte ainsi à presque tout : le texte, les images, le son, et
même les protéines. On retrouve la
[leçon amère](docs/module3/40-apprentissage-profond/#la-leçon-amère) de Richard
Sutton : moins on impose d'hypothèses, plus on dépend des données et du calcul, et
plus la méthode est générale.

## L'attention dans la traduction

Revenons à
l'[encodeur-décodeur](docs/module3/60-reseaux-recurrents/#ce-que-les-réseaux-récurrents-ont-permis). Le décodeur écrit la traduction à partir d'un seul état, qui
résume toute la phrase d'origine. En 2014, Dzmitry Bahdanau, Kyunghyun Cho et Yoshua
Bengio, à Montréal, gardent l'état de l'encodeur après **chaque** mot, et non
seulement le dernier. Le décodeur peut alors consulter toute la phrase d'origine à
chaque mot qu'il écrit.

Pour chaque mot à écrire, le décodeur procède en trois temps :

1. il compare ce qu'il cherche à chacun des mots de la phrase d'origine, ce qui
   donne un score par mot ;
2. il transforme ces scores en **poids**, positifs et de total égal à
   1 ;
3. il fait un mélange des mots d'origine selon ces poids, et s'en sert pour choisir
   le mot à écrire.

Les poids indiquent où le décodeur « regarde » au moment d'écrire chaque mot. C'est
pourquoi on parle d'**attention**.

L'article de 2014 montre un exemple de traduction de l'anglais vers le français.
« The European Economic Area » devient « la zone économique européenne ». L'ordre
des mots s'inverse : « European » vient avant « Economic » en anglais,
« européenne » vient après « économique » en français. Les poids de l'attention
suivent cette inversion. En écrivant « économique », le décodeur regarde surtout
« Economic ». En écrivant « européenne », il regarde surtout « European ».

{{< image src="/images/module3/attention-traduction.svg" alt="Une grille de quatre colonnes et quatre lignes. Les colonnes portent les mots anglais « the European Economic Area », les lignes les mots français « la zone économique européenne ». Chaque case est d'autant plus foncée que le décodeur regarde ce mot anglais en écrivant ce mot français. « la » regarde « the », « zone » regarde « Area », « économique » regarde « Economic » et « européenne » regarde « European » : les deux dernières cases foncées se croisent." title="Les poids de l'attention pour la traduction de « the European Economic Area ». Les valeurs sont redessinées d'après l'exemple de Bahdanau, Cho et Bengio (2014)." loading="lazy" >}}

Personne n'a indiqué au réseau quel mot correspond à quel mot. Ces correspondances
sont apprises, comme tous les poids, par
[rétropropagation](docs/module3/30-entrainer-un-reseau/#la-rétropropagation).

## Une recherche floue

L'attention est une forme de recherche. Dans une recherche ordinaire, par exemple
dans un dictionnaire, on cherche un mot, on le compare aux entrées, et on récupère
la définition de l'entrée qui correspond exactement. Le Module 1 décrivait de la
même façon la recherche d'un fait dans la
[base de faits d'un système expert](docs/module1/50-systemes-experts/#lanatomie-dun-système-expert).

L'attention procède de la même façon, avec une différence : elle ne choisit pas une
seule entrée. Elle compare la question à toutes les entrées, et récupère un peu de
chacune, en proportion de leur ressemblance avec la question. C'est une recherche
floue.

On donne un nom à chacun des trois éléments :

- la **requête** (*query*) est ce que l'on cherche ;
- les **clés** (*keys*) sont ce à quoi on compare la requête, une par entrée ;
- les **valeurs** (*values*) sont ce que l'on récupère, une par entrée.

Dans un réseau, les requêtes, les clés et les valeurs sont des listes de nombres
calculées par des neurones. Leurs poids sont appris. Le réseau apprend donc à la
fois quoi chercher, comment se décrire pour être trouvé, et quoi transmettre.

{{% details "Pour aller plus loin : le calcul sur un petit exemple" %}}
Prenons une requête et trois entrées, chacune décrite par deux nombres.

| | Clé | Valeur |
|---|:---:|:---:|
| Entrée A | (1, 0) | 10 |
| Entrée B | (0, 1) | 20 |
| Entrée C | (1, 1) | 30 |

La requête est (2, 0). On la compare à chaque clé en multipliant les nombres deux à
deux et en additionnant : 2 pour A, 0 pour B, 2 pour C. On transforme ensuite ces
scores en poids qui totalisent 1, en favorisant les scores élevés. On obtient
environ 0,47 pour A, 0,06 pour B et 0,47 pour C. Le résultat est le mélange des
valeurs selon ces poids : 0,47 × 10 + 0,06 × 20 + 0,47 × 30, soit environ 20. La
requête a surtout récupéré les valeurs de A et de C, dont les clés lui ressemblent.
{{% /details %}}

## L'auto-attention

Dans la traduction, le décodeur porte son attention sur la phrase d'origine.
L'étape suivante consiste à appliquer l'attention à l'intérieur d'une même phrase.
Chaque mot émet une requête, et va chercher l'information utile chez les autres
mots de la phrase. On parle d'**auto-attention** (*self-attention*).

Prenons la phrase « Le chien n'est pas monté dans le camion parce qu'il était trop
fatigué. » Le mot « il » peut désigner le chien ou le camion. Pour le comprendre,
il faut aller chercher l'information dans « chien ». Si la phrase se termine par
« trop haut », « il » désigne le camion. Le sens d'un mot dépend de son contexte,
et l'auto-attention calcule ce lien.

Après une couche d'auto-attention, chaque mot n'est plus représenté seul. Sa
représentation contient une part de l'information des mots qu'il a regardés. Le
« il » de la première phrase porte maintenant une part de « chien ».

## Une attention à manipuler

Dans l'applet ci-dessous, cliquez sur un mot pour voir où il porte son attention.
Les arcs le relient aux autres mots, d'autant plus épais que le poids est grand, et
les poids s'affichent sous chaque mot. Ces poids ont été choisis pour l'exemple.
Dans un vrai Transformer, ils sont calculés par le réseau, et ils sont en général
moins nets.

{{< applet src="/html/applets/attention.html" height="530" >}}

1. Le mot « il » est choisi. Observez où il porte son attention.
2. Remplacez la fin de la phrase par « … trop haut. » L'attention de « il » se
   déplace vers « camion ».
3. Cliquez sur « fatigué », puis sur « haut » dans la seconde phrase. Chacun
   regarde le nom qu'il qualifie.
4. Cliquez sur « monté ». Il regarde surtout « chien » et « camion », son sujet et
   son complément.

## Le Transformer

En 2017, huit chercheurs de Google, dont Ashish Vaswani, publient un article
intitulé « Attention Is All You Need » (« L'attention suffit »). L'idée tient dans
le titre. On supprime la récurrence et on ne garde que l'attention. L'architecture
qui en résulte s'appelle le **Transformer**.

Un Transformer est fait de **blocs** identiques, empilés. Chaque bloc contient deux
étapes :

1. une couche d'**auto-attention**, où chaque mot va chercher l'information utile
   chez les autres mots ;
2. un petit réseau ordinaire, appliqué à chaque mot séparément, qui transforme
   l'information recueillie.

Le texte traverse les blocs l'un après l'autre. À chaque bloc, la représentation de
chaque mot s'enrichit de son contexte. L'article de 2017 empile six blocs. Les
grands modèles actuels en empilent une centaine.

{{< image src="/images/module3/transformer-blocs.svg" alt="Deux panneaux. À gauche, un bloc : les mots entrent par le bas, passent par une couche d'auto-attention, où chaque mot regarde les autres, puis par un petit réseau appliqué à chaque mot, et ressortent enrichis par le haut. À droite, une pile de six blocs identiques : les mots entrent en bas et ressortent en haut, enrichis de leur contexte." title="Le Transformer : chaque bloc combine l'auto-attention et un petit réseau ; on empile les blocs." loading="lazy" >}}

Deux précisions complètent ce schéma.

**Plusieurs têtes.** Chaque couche d'auto-attention contient plusieurs mécanismes
d'attention en parallèle, appelés **têtes** (*attention heads*), par exemple huit.
Chacune a ses propres requêtes, clés et valeurs, et peut apprendre un type de lien
différent : une tête relie un verbe à son sujet, une autre un pronom au nom qu'il
désigne, une autre un mot à son voisin.

**La position.** Un réseau récurrent connaissait l'ordre des mots, puisqu'il les
lisait un à un. L'auto-attention, elle, traite tous les mots en même temps et ne
connaît pas leur ordre. Pour elle, « le chien mord l'homme » et « l'homme mord le
chien » seraient identiques. On ajoute donc à chaque mot, à l'entrée du réseau, une
indication de sa position dans la phrase (*positional encoding*).

On retrouve aussi dans le Transformer les
[raccourcis](docs/module3/50-reseaux-convolutifs/#après-2012)
de ResNet, qui laissent l'information sauter une étape et facilitent l'entraînement
d'une pile très profonde.

## Pourquoi il a tout changé

Le Transformer règle les trois limites des réseaux récurrents, et en ajoute une.

**Le parallélisme.** Tous les mots d'un texte sont traités en même temps, et non
l'un après l'autre. Les calculs de l'attention sont des multiplications répétées,
le type de calcul pour lequel les
[GPU](docs/module3/42-materiel-et-outils/#les-processeurs-graphiques) sont conçus.
Un Transformer s'entraîne donc beaucoup plus vite qu'un réseau récurrent de même
taille.

**La distance.** Dans un réseau récurrent, l'information du premier mot doit
traverser toutes les étapes pour atteindre le centième. Dans un Transformer, le
centième mot regarde directement le premier, en une seule étape. La mémoire
lointaine n'est plus un problème de principe.

**L'échelle.** Ces deux propriétés permettent d'entraîner des réseaux beaucoup plus
grands, sur beaucoup plus de texte. Les Transformers des années 2020 comptent des
centaines de milliards de poids, entraînés sur une grande partie du texte
disponible sur le Web. Ce changement d'échelle est celui que décrivait la
[leçon amère](docs/module3/40-apprentissage-profond/#la-leçon-amère).

**Un coût.** Dans l'auto-attention, chaque mot regarde tous les autres. Pour un
texte de 1 000 mots, cela fait un million de comparaisons. Pour 2 000 mots, quatre
millions. Le calcul croît avec le carré de la longueur du texte. C'est pourquoi un
Transformer ne peut traiter qu'un texte de longueur limitée à la fois, sa
**fenêtre de contexte** (*context window*). Le Module 4 reviendra sur cette notion.

## Au-delà du texte

Le Transformer a été conçu pour la traduction, mais rien dans son fonctionnement
n'est propre au langage. Il suffit de découper les données en éléments, et de
laisser chaque élément regarder les autres.

**Les images.** En 2020, une équipe de Google découpe une image en petits carrés de
16 pixels sur 16 et les traite comme les mots d'une phrase. Ce *Vision Transformer*
n'a pas la connaissance inscrite dans un réseau convolutif : il ne sait pas
d'avance que les pixels voisins sont liés, et doit l'apprendre. Avec peu d'images,
il fait moins bien qu'un réseau convolutif. Avec des centaines de millions
d'images, il fait mieux. C'est un nouvel exemple de la
[leçon amère](docs/module3/40-apprentissage-profond/#la-leçon-amère), et une
nuance à la
[leçon de la convolution](docs/module3/50-reseaux-convolutifs/#la-leçon-de-la-convolution) :
une connaissance inscrite dans le réseau aide quand les données sont rares, et peut
gêner quand elles sont abondantes.

{{< image src="/images/module3/vision-transformer.svg" alt="En haut, une petite image de paysage, avec un ciel, un soleil et des collines, découpée par une grille en seize carrés. En bas, ces seize carrés sont alignés l'un après l'autre, numérotés de 1 à 16, comme les mots d'une phrase, et entrent dans un Transformer." title="Le Vision Transformer découpe une image en carrés et les traite comme les mots d'une phrase." loading="lazy" >}}

**La biologie.** Une protéine est une chaîne d'acides aminés qui se replie dans
l'espace, et sa forme détermine son rôle. Prédire cette forme à partir de la chaîne
était un problème ouvert depuis cinquante ans. En 2020, le système **AlphaFold 2**,
de DeepMind, le résout pour la plupart des protéines, avec un mécanisme d'attention
au cœur de son architecture. Ce travail a valu à Demis Hassabis et John Jumper une
moitié du prix Nobel de chimie 2024.

**La parole, la musique, le code.** Tous les types de séquences se prêtent à la
même méthode.

## Vers le Module 4

Dès 2018, deux usages du Transformer apparaissent. **BERT**, chez Google, lit un
texte en entier pour en produire une représentation, utile par exemple aux moteurs
de recherche. **GPT**, chez OpenAI, est entraîné à une tâche plus simple : prédire
le mot suivant d'un texte. Agrandi de version en version, ce second type de modèle
est à l'origine des grands modèles de langage, comme
ChatGPT. Le [Module 4](docs/module4/50-predire-le-mot-suivant) leur est consacré.

## Pour voir le mécanisme en détail

La vidéo ci-dessous, de la série de 3Blue1Brown déjà présentée dans
« [Entraîner un réseau](docs/module3/30-entrainer-un-reseau/#pour-voir-le-mécanisme-en-détail) »,
explique l'attention pas à pas, avec ses requêtes, ses clés et ses valeurs. Elle
est en anglais.

{{< youtube id="eMlx5fFNoYc" >}}

Le chapitre suivant, « [Apprendre à jouer : le renforcement profond](docs/module3/80-renforcement-profond) », quitte les
séquences. Il revient à
l'[apprentissage par renforcement](docs/module2/80-trois-facons-d-apprendre/#apprendre-par-lexpérience-le-renforcement)
(*reinforcement learning*) du Module 2 et montre ce qu'il devient avec les réseaux
profonds.
