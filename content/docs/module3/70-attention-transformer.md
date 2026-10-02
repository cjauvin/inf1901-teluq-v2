---
title: "L'attention et le Transformer"
weight: 70
slug: attention-transformer
---

# L'attention et le Transformer

Le chapitre
« [Lire une séquence](docs/module3/60-reseaux-recurrents/#les-limites) » s'est
terminé sur trois limites des réseaux récurrents : toute une phrase passe par un
seul état, le calcul avance une étape à la fois, et les éléments lointains
s'oublient. Ce chapitre présente le mécanisme qui a levé ces limites,
l'**attention**, puis l'architecture construite autour de lui, le **Transformer**.
Il traite le Transformer comme une architecture, au même titre que les réseaux
convolutifs ou récurrents. Ce qu'il permet de faire avec le langage est le sujet du
[Module 4](docs/module4).

## L'attention dans la traduction

Revenons à
l'[encodeur-décodeur](docs/module3/60-reseaux-recurrents/#ce-que-les-réseaux-récurrents-ont-permis).
Le décodeur écrit la traduction à partir d'un seul état, qui résume toute la phrase
d'origine. En 2014, Dzmitry Bahdanau, Kyunghyun Cho et Yoshua Bengio, à Montréal,
gardent l'état de l'encodeur après **chaque** mot, et non seulement le dernier. Le
décodeur peut alors consulter toute la phrase d'origine à chaque mot qu'il écrit.

Pour chaque mot à écrire, le décodeur procède en trois temps :

1. il compare ce qu'il cherche à chacun des mots de la phrase d'origine, ce qui
   donne un score par mot ;
2. il transforme ces scores en **poids**, positifs et de total égal à 1 ;
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

- la **requête** est ce que l'on cherche ;
- les **clés** sont ce à quoi on compare la requête, une par entrée ;
- les **valeurs** sont ce que l'on récupère, une par entrée.

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
mots de la phrase. On parle d'**auto-attention**.

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
