---
title: "Les hivers et la bascule"
weight: 60
slug: hivers-et-bascule
---

# Les hivers et la bascule

{{< image src="/images/module1/bruegel-chasseurs-neige.jpg" alt="Tableau de Bruegel : trois chasseurs et leurs chiens rentrent au village par une colline enneigée ; en contrebas, des étangs gelés où patinent des villageois, et des montagnes au loin sous un ciel gris-vert." title="Pieter Bruegel l'Ancien, Les Chasseurs dans la neige (1565). L'expression « hiver de l'IA » désigne les périodes où l'intérêt et le financement pour la recherche en IA ont fortement diminué." loading="lazy" >}}

<p class="image-credit">Pieter Bruegel l'Ancien, <em>Les Chasseurs dans la neige</em> (1565), Kunsthistorisches Museum, Vienne. Domaine public, via Wikimedia Commons.</p>

## Le premier hiver : la mort du perceptron (1969)

Le chapitre « [Deux paris rivaux](docs/module1/20-deux-paris) » a présenté le
**perceptron** de Rosenblatt, une machine qui apprend de ses erreurs, que le *New
York Times* avait décrit comme le début d'une intelligence électronique. Ce chapitre
annonçait aussi que le perceptron allait subir une critique sévère. Cette section
présente cette critique.

En **1969**, deux chercheurs importants du camp symbolique, **Marvin Minsky** (l'un
des organisateurs de Dartmouth) et son collègue **Seymour Papert**, publient un livre
intitulé *Perceptrons*. Il ne s'agit pas d'un pamphlet, mais d'une analyse
mathématique rigoureuse. Minsky et Papert y démontrent que le perceptron a une limite
de principe : il est incapable d'apprendre certaines fonctions pourtant très simples.
L'exemple le plus connu est le **XOR**, le « ou exclusif ».

Le XOR correspond à la règle suivante : l'un ou l'autre, mais pas les deux à la fois.
C'est par exemple le principe du **va-et-vient**, où deux interrupteurs commandent
une même lampe, souvent aux deux bouts d'un couloir. Quand on bascule l'un ou l'autre
interrupteur, la lumière change d'état. Si les deux interrupteurs sont dans la même
position, la lampe est éteinte ; s'ils sont dans des positions opposées, elle est
allumée. La réponse dépend donc du désaccord entre les deux entrées.

On peut résumer le XOR dans une **table de vérité**, qui donne la réponse pour
chaque combinaison possible des deux entrées. On note 0 pour « bas » (ou « faux »)
et 1 pour « haut » (ou « vrai ») :

| Interrupteur A | Interrupteur B | Lampe (A XOR B) |
|:---:|:---:|:---:|
| 0 | 0 | 0 (éteinte) |
| 0 | 1 | 1 (allumée) |
| 1 | 0 | 1 (allumée) |
| 1 | 1 | 0 (éteinte) |

La sortie vaut 1 seulement quand les deux entrées diffèrent. Si l'on place ces
quatre cas sur un plan, avec A à l'horizontale et B à la verticale, les deux cas
« allumé » occupent deux coins opposés d'un carré, et les deux cas « éteint » les
deux autres coins. Cette règle est facile à comprendre pour un humain, mais le
perceptron ne peut pas l'apprendre, parce qu'il classe les cas en traçant une seule
droite, et qu'aucune droite ne sépare ces deux paires de coins. Le
[Module 2](docs/module2/70-generaliser/#linéaire-ou-non-linéaire-ce-quun-modèle-peut-dessiner)
reprend cet exemple avec une figure, et montre comment d'autres modèles réussissent
là où une droite échoue.

Le livre eut des conséquences importantes. Minsky avait une grande autorité, et il
appartenait au camp adverse. Sa démonstration, mathématiquement correcte, fut
interprétée comme une condamnation de toute l'approche. Les financements de la
recherche sur les réseaux de neurones diminuèrent très rapidement, les revues
publièrent moins de travaux sur le sujet et les étudiants choisirent d'autres
domaines. Le camp connexionniste connut un **hiver** d'une quinzaine d'années.
Rosenblatt n'en vit pas la fin : il mourut en 1971, à quarante-trois ans, dans un
accident de bateau.

Le premier hiver de l'IA ne toucha donc pas la tradition dominante, mais sa
**rivale**, et c'est un chercheur du camp symbolique qui en fut en partie la cause.
Comme le connexionnisme était mis de côté, les vingt années suivantes furent celles
d'une **domination symbolique** presque complète : la recherche dans un espace
d'états, les systèmes experts et l'ensemble des travaux présentés dans les chapitres
« [Chercher et raisonner](docs/module1/30-chercher-raisonner) », « [Représenter le
monde](docs/module1/40-representer-le-monde) » et « [Capturer
l'expertise](docs/module1/50-systemes-experts) ». Le déclin d'une tradition a ainsi favorisé le développement de l'autre.

La démonstration de Minsky et Papert avait cependant une limite. Elle ne valait que
pour le perceptron le plus simple, formé d'une **seule couche**. On pensait qu'en
**empilant plusieurs couches**, on pourrait traiter le XOR, mais on ne savait pas
comment faire apprendre un tel réseau. La solution n'apparut qu'en 1986, et c'est
elle qui permit la reprise des travaux connexionnistes. Avant d'y arriver, il faut
d'abord voir comment le camp symbolique connut lui aussi un hiver.

## Le second hiver : l'effondrement du symbolique (fin des années 1980)

L'âge d'or symbolique reposait sur une promesse ambitieuse : capturer l'expertise
humaine dans des règles. Les limites décrites dans « [Capturer
l'expertise](docs/module1/50-systemes-experts) » (le savoir tacite difficile à
extraire, la rigidité sans sens commun, les bases de règles difficiles à maintenir)
finirent par affaiblir l'ensemble de l'approche. Comme les systèmes experts livrés
décevaient souvent, l'écart grandit entre ce qu'on avait promis aux investisseurs et
ce que l'IA réalisait vraiment. Quand cet écart devint trop visible, les
investissements diminuèrent.

L'événement le plus représentatif de ce recul fut le **krach des machines Lisp**,
vers 1987. Ces ordinateurs spécialisés, conçus pour l'IA, coûtaient très cher. En peu
de temps, des stations de travail bon marché, puis les ordinateurs personnels,
offrirent des performances comparables pour une fraction du prix. Le marché
s'effondra et les entreprises qui en dépendaient disparurent. À la même époque, le
projet japonais de **Cinquième Génération**, lancé en 1982 avec beaucoup de
publicité, se terminait sans avoir atteint ses principaux objectifs.

Le découragement toucha tout le domaine. Les agences de financement réduisirent leurs
crédits, et l'étiquette « intelligence artificielle » devint si mal perçue que les
chercheurs évitaient de l'utiliser dans leurs demandes de subvention. On parle, pour
cette période, d'un second **hiver de l'IA**. Le terme s'appliquait maintenant au
camp symbolique, comme il s'était appliqué vingt ans plus tôt au perceptron. La leçon
était la même que dans « [Représenter le
monde](docs/module1/40-representer-le-monde) » et « [Capturer
l'expertise](docs/module1/50-systemes-experts) » : le monde réel se laisse
difficilement décrire par des règles écrites à la main.

Pendant que le camp symbolique déclinait, le camp connexionniste, qu'on croyait
abandonné depuis 1969, **reprenait de l'activité**. En 1986, un petit groupe de
chercheurs, dont **Geoffrey Hinton**, avait publié une méthode appelée
**rétropropagation**. Elle permettait de faire apprendre les réseaux à **plusieurs
couches**, c'est-à-dire justement ceux qui, selon les intuitions de l'époque,
pouvaient traiter le XOR. L'obstacle signalé dans *Perceptrons* était donc levé. Ce
retour resta toutefois discret au début : il fallut attendre les **données** et la
**puissance de calcul** des années 2010 pour qu'il devienne largement visible. Les
deux traditions échangeaient de nouveau leurs rôles : le déclin de l'une coïncidait
avec la reprise de l'autre.

## L'héritage invisible

Après deux hivers successifs, on pourrait conclure que le GOFAI a échoué. Cette
conclusion serait cependant incomplète, à cause d'un phénomène que les chercheurs
appellent l'**« effet IA »** : dès qu'une technique fonctionne bien, on cesse de
l'appeler « intelligence artificielle » et on la considère comme « juste un
algorithme ». La formule la plus courte est attribuée à l'informaticien Larry Tesler,
et c'est **Hofstadter** qui l'a popularisée : *« l'IA, c'est tout ce qui n'a pas
encore été fait. »*

De ce point de vue, le GOFAI n'a pas disparu : il s'est **intégré** à l'informatique
courante. Ses réussites sont devenues si ordinaires et si fiables qu'on a oublié
qu'elles venaient des laboratoires d'IA. Les quatre exemples suivants sont des
techniques que vous utilisez probablement chaque jour.

**[La recherche dans un arbre](docs/module1/30-chercher-raisonner)**. Les algorithmes d'exploration (minimax,
A\*) qui permettaient aux machines de jouer aux échecs sont aujourd'hui très répandus.
Ce sont eux qui calculent votre itinéraire **GPS** en une fraction de seconde, qui
dirigent les personnages des jeux vidéo et qui optimisent les tournées d'un
transporteur ou les mouvements d'un robot. Les personnes qui suivent un itinéraire
sur leur téléphone ne pensent généralement pas qu'elles utilisent une technique
d'« intelligence artificielle » des années 1960.

**[Les moteurs de règles](docs/module1/50-systemes-experts)**. Les systèmes experts n'ont pas disparu, mais ils
ont changé de nom. On parle aujourd'hui de « règles métier », et ces systèmes
décident automatiquement de l'octroi d'un prêt, du repérage d'une transaction
frauduleuse ou du calcul d'une prime d'assurance. Les **configurateurs** qui, sur un
site marchand, vérifient que les options d'une voiture ou d'un ordinateur sont
compatibles descendent directement de XCON. De même, un logiciel d'**impôts** qui
vous guide de question en question jusqu'au bon formulaire fait le même travail que
MYCIN.

**[Les idées de Lisp](docs/module1/30-chercher-raisonner)**. Cet héritage est
peut-être le plus important. Le langage de McCarthy a introduit dans la
programmation courante la **programmation fonctionnelle** : traiter les fonctions
comme des valeurs (les *lambdas*), enchaîner des opérations comme `map`, `filter`,
`reduce`, utiliser des *closures*. Ces constructions, courantes aujourd'hui en
Python, en JavaScript ou en Java, viennent des laboratoires d'IA. Lisp a aussi
introduit des outils qu'on considère maintenant comme normaux : le
**ramasse-miettes** (la gestion automatique de la mémoire) et le **REPL**, la console
qui permet d'essayer du code au fur et à mesure. L'autre grande tradition
fonctionnelle, celle des langages typés comme Haskell, descend du langage **ML**, que
Robin Milner avait créé pour programmer un **assistant de démonstration de
théorèmes**. Les deux sources de la programmation fonctionnelle moderne viennent donc
du raisonnement symbolique.

**[La représentation des connaissances](docs/module1/40-representer-le-monde)**. Les
réseaux sémantiques et les frames, [présentés plus
tôt](docs/module1/40-representer-le-monde/#donner-un-savoir-à-la-machine), ont eu des successeurs. Les
**ontologies** et les **knowledge graphs** qui structurent le savoir du web en sont
les héritiers directs. Quand Google affiche une fiche résumée à côté des résultats,
ou quand on interroge Wikidata, c'est la même idée qui est utilisée : relier des
concepts par des liens *est-un* ou *possède*. Entre les deux, il y a eu une tentative
ambitieuse, qui mérite d'être mentionnée : le [**web sémantique**](https://fr.wikipedia.org/wiki/Web_s%C3%A9mantique).
En 2001, Tim Berners-Lee, l'inventeur du Web, propose d'en faire une grande base de
connaissances lisible par les machines. Chaque page contiendrait non seulement du
texte pour les humains, mais aussi des faits structurés pour les programmes (*cette
personne est née en telle année*, *ce produit coûte tant*), reliés par des
vocabulaires communs, c'est-à-dire des ontologies. Des normes sont écrites dans ce
but (RDF, OWL). Le projet complet ne s'est pas réalisé, pour une raison déjà vue dans
« [Représenter le monde](docs/module1/40-representer-le-monde/#le-mur-du-sens-commun) » : il supposait que des millions d'auteurs décrivent soigneusement le sens
de ce qu'ils publient. C'est le même travail d'inscription à la main qui avait limité
CYC, mais à l'échelle de la planète. Certaines de ses composantes ont cependant été
conservées : les balises que les sites ajoutent aujourd'hui pour que les moteurs de
recherche comprennent une recette ou un horaire, ainsi que Wikidata, en sont les
héritiers directs. Quant aux frames, avec leurs cases à valeurs par défaut et leurs
hiérarchies d'héritage, elles sont **apparentées** à l'**objet** de la programmation
moderne. Elles n'en sont pas l'ancêtre (l'orienté-objet doit davantage à la
simulation qu'à l'IA), mais elles reposent sur la même intuition. Une dernière
remarque prépare le [module 4](docs/module4) : tout ce savoir est **structuré à la main** par des
humains. C'est l'opposé de la façon dont les grands modèles de langage acquièrent
leur savoir, en traitant d'énormes quantités de texte. Ces deux conceptions du savoir
seront comparées [plus loin dans le cours](docs/module4).

Ces quatre exemples ne sont pas les seuls. Aucune de ces techniques ne porte plus
l'étiquette « IA », parce qu'elles font maintenant partie de l'informatique
ordinaire. Le GOFAI n'a donc pas été une impasse : ses idées se sont **dispersées**
hors du domaine de l'intelligence artificielle et sont devenues des éléments courants
et indispensables de la programmation.

## Un éclair hybride : Watson (2011)

Un dernier exemple montre que le GOFAI ne s'est pas seulement intégré à
l'informatique courante, mais qu'il est aussi réapparu, combiné à d'autres méthodes.
En février **2011**, un système d'IBM nommé **Watson** affronte, au jeu télévisé
américain *Jeopardy!*, les deux meilleurs champions de l'histoire de l'émission, Ken
Jennings et Brad Rutter, et les bat nettement.

Cette réussite est d'une autre nature que celle de Deep Blue. Les échecs ont des
règles précises et un espace de recherche bien défini. *Jeopardy!*, au contraire,
repose sur un **langage** difficile, fait de calembours, d'allusions, de jeux de mots
et d'indices indirects. Comprendre ce que la question demande est déjà un problème
difficile. Watson y répond en quelques secondes, en utilisant une très grande base de
connaissances.

Watson n'est **ni du GOFAI pur, ni un réseau de neurones**. C'est un **hybride**.
D'une part, il reprend des éléments du symbolique : une grande base de connaissances
et des traitements du langage à base de règles. D'autre part, il pondère des
centaines d'indices et calcule sa **confiance** avec des méthodes **statistiques**,
apprises sur des milliers de questions passées. Quatorze ans après Deep Blue, ce n'est
donc plus seulement la force brute de la recherche qui permet de gagner, mais une
combinaison du savoir structuré du GOFAI et de l'apprentissage statistique. Watson
illustre ainsi la **charnière** où se trouve maintenant le module, entre deux
périodes.

{{% hint warning %}}
La suite de l'histoire de Watson ressemble à celle des systèmes experts. Après le
succès de 2011, IBM annonça que *Watson Health* allait **transformer la médecine** :
la machine devait conseiller les cancérologues mieux que leurs collègues. Les
résultats furent très différents. Certaines recommandations se révélèrent douteuses,
voire dangereuses. De grands hôpitaux partenaires abandonnèrent le projet après y
avoir dépensé des dizaines de millions de dollars, et IBM finit par **revendre**
Watson Health en 2022. Trente ans après MYCIN, qui avait bien fonctionné en
démonstration sans jamais être utilisé auprès de vrais patients, la même leçon se
répétait : l'écart reste très grand entre une réussite en laboratoire (ou sur un
plateau de télévision) et le monde réel. Une fois de plus, une promesse trop
ambitieuse avait précédé la déception.
{{% /hint %}}

## La bascule

Voici un résumé du chemin parcouru. Le chapitre « [Turing et la question
fondatrice](docs/module1/10-turing) » est parti d'une hypothèse : penser, c'est calculer. De cette hypothèse est née une famille d'idées
(manipuler des symboles selon des règles) qui a produit, pendant trois décennies,
des réussites importantes : des machines qui démontrent des théorèmes, qui jouent aux
échecs, qui dialoguent, qui représentent le monde et qui établissent des diagnostics
comme des médecins. Le programme symbolique n'a donc pas été un échec : il a fondé
l'informatique du raisonnement, qui est encore utilisée aujourd'hui.

Il s'est cependant heurté deux fois à la même difficulté. Dans « [Représenter le
monde](docs/module1/40-representer-le-monde) », il s'agissait du **sens commun**,
l'ensemble des évidences que personne ne pense à formuler et qu'on ne peut donc pas
écrire. Dans « [Capturer l'expertise](docs/module1/50-systemes-experts) », il
s'agissait du **goulot d'étranglement** : l'expertise est difficile à mettre en
règles, parce qu'une grande partie du savoir humain n'est pas exprimée. Ces deux
difficultés relèvent d'une même leçon, que Hofstadter avait peut-être formulée le
premier : on ne peut pas inscrire l'intelligence de l'extérieur, fait après fait,
parce que le savoir utile est trop vaste, trop tacite et trop changeant pour tenir
dans une liste de règles.

Si l'on ne peut pas dicter ce savoir à la machine, il faut qu'elle l'**acquière
elle-même**. Cette idée n'était pas nouvelle : elle se trouvait déjà en 1958 dans le
perceptron de Rosenblatt, une machine qui apprend de ses erreurs, que le camp
symbolique pensait avoir écarté en 1969. C'est ici que se termine le fil suivi depuis
« [Deux paris rivaux](docs/module1/20-deux-paris) ». Les deux traditions, symbolique
et connexionniste, ne se sont jamais simplement succédé : elles ont coexisté en
rivales, et chacune a dominé à son tour. L'hiver symbolique de la fin des années 1980
n'est donc pas la fin de l'histoire, mais le moment où l'avantage commence à revenir
vers l'autre tradition.

Une question, apparue avec les difficultés du GOFAI, va réorganiser le domaine : au
lieu de dicter ses règles à la machine, on peut la laisser les découvrir dans les
données. Ce changement d'approche s'appelle l'**apprentissage automatique**, et c'est
l'objet du **[Module 2](docs/module2)**. La tradition connexionniste, relancée par la
rétropropagation et la puissance des machines modernes, le mènera ensuite, au
**[Module 3](docs/module3)**, à des résultats que ni Turing, ni Rosenblatt, ni Minsky n'avaient
imaginés.

Le module peut se résumer par le passage d'un verbe à un autre. Pendant trois
décennies, être intelligent, pour une machine, a surtout voulu dire **chercher** :
explorer un espace de possibilités, guidé par des règles fixées à l'avance. La
période suivante remplace ce verbe par **apprendre**. Les deux verbes restent
cependant proches, et la [suite du
cours](docs/module2/50-entrainer-un-modele/#apprendre-cest-descendre-la-pente) y reviendra : apprendre, c'est encore
chercher, mais dans un autre espace. Au lieu d'explorer les coups d'une partie, on
explore l'ensemble des réglages possibles d'un modèle, jusqu'à trouver ceux qui
correspondent aux données. Le GOFAI cherchait la solution, alors que
l'apprentissage cherche de quoi la produire. La période de la recherche se termine
donc, et celle de l'apprentissage, qui est une autre forme de recherche, commence.
