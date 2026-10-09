---
title: "Des mots aux nombres : jetons et plongements"
weight: 45
slug: des-mots-aux-nombres
---

# Des mots aux nombres : jetons et plongements

Le chapitre « [Les outils statistiques](docs/module4/42-les-outils-statistiques/#ce-qui-manquait) »
s'achevait sur une limite : pour un modèle à n-grammes, « chat » et « chien » sont
deux symboles sans rapport. Ce chapitre ouvre l'ère des réseaux de neurones par
cette question. Le chapitre
« [Lire une séquence : les réseaux récurrents](docs/module3/60-reseaux-recurrents/#le-problème-des-séquences) »
du Module 3 en laissait d'ailleurs une autre de côté. Un réseau de neurones ne manipule que des
nombres, alors que le texte est fait de mots. Avant qu'un modèle de langage puisse
lire ou écrire une phrase, il faut donc convertir les mots en nombres.

Cette question paraît technique, mais elle touche au sens des mots. Elle demande deux
opérations. Il faut d'abord **découper** le texte en morceaux, puis **représenter**
chaque morceau par des nombres. Ce chapitre présente les deux, avec de vrais outils :
le découpage utilisé par un modèle d'OpenAI, et des représentations de mots apprises
sur des milliards de mots de français.

## Découper le texte : les jetons

Avant de représenter les mots par des nombres, il faut décider de ce qu'est un mot.
Un vocabulaire de mots entiers pose un problème pratique. Que faire d'un mot
qui n'y figure pas, comme un nom propre, un mot rare, une faute de frappe, un mot
d'une autre langue ou un mot inventé ? Aucune liste de mots ne peut tout prévoir.

Les modèles de langage découpent donc le texte en morceaux plus petits que les mots,
qu'on appelle des **jetons** (*tokens*). La méthode la plus utilisée, le **codage
par paires d'octets** (*byte pair encoding*, BPE), vient de la compression de
données. Elle a été adaptée à la traduction automatique en 2015 par Rico Sennrich et
ses collègues, à l'Université d'Édimbourg. Elle fonctionne ainsi :

1. on part des caractères individuels ;
2. on cherche, dans un très grand corpus de textes, la paire de morceaux voisins la
   plus fréquente, par exemple *e* suivi d'*s* ;
3. on fusionne cette paire en un nouveau morceau, *es*, qu'on ajoute au vocabulaire ;
4. on recommence, jusqu'à obtenir la taille de vocabulaire voulue.

Les mots fréquents finissent par devenir un seul jeton. Les mots rares restent
découpés en plusieurs morceaux, mais ils peuvent toujours être écrits, au pire
caractère par caractère. Les modèles actuels utilisent des vocabulaires de 100 000 à
200 000 jetons.

L'applet ci-dessous découpe un texte avec le vocabulaire de GPT-4o, un modèle
d'OpenAI.

{{< applet src="/html/applets/jetons.html" height="378" >}}

Quelques manipulations à faire :

1. Comparez la phrase en français et la même phrase en anglais. La phrase française
   demande nettement plus de jetons. Le vocabulaire a été construit sur des textes
   majoritairement anglais, où les mots anglais sont plus fréquents et sont donc
   devenus des jetons entiers. Comme l'usage de ces modèles est souvent facturé au
   jeton, un même texte coûte plus cher dans certaines langues que dans d'autres.
2. Regardez le mot rare et le verbe « découpent ». Ils sont coupés en morceaux qui
   ne correspondent pas toujours aux syllabes ni aux préfixes.
3. Choisissez l'exemple *strawberry*. Le mot est un seul jeton. Le modèle reçoit donc
   un seul numéro, et non les dix lettres du mot. C'est l'une des raisons pour
   lesquelles les modèles de langage ont longtemps eu du mal à répondre à la question
   « combien de *r* y a-t-il dans *strawberry* ? ». Ils ne voient pas les lettres.
4. Regardez les nombres. « 12 345 » et « 38 781,93 » sont coupés en groupes de
   chiffres, ce qui complique le calcul.

## La première idée : un numéro par mot

Une fois le texte découpé, il faut représenter chaque jeton par des nombres. Pour
simplifier, parlons de mots : les mots courants sont de toute façon des jetons
entiers. On pourrait se contenter de numéroter les mots du vocabulaire, de 1 à
100 000, et de donner au réseau le numéro de chaque mot. Cela ne fonctionne pas. Un
[neurone](docs/module3/10-un-neurone/#un-neurone-est-une-régression-logistique)
traite ses entrées comme des quantités : il les multiplie par des poids et les
additionne. Le numéro deviendrait donc une grandeur. Si « chat » porte le numéro
8 112 et « chaise » le numéro 8 113, le réseau les traiterait comme presque
identiques, simplement parce qu'ils se suivent dans la liste. Et le mot
numéro 40 000 pèserait cinq fois plus que le mot numéro 8 000. Or l'ordre de la
liste est arbitraire, et ces écarts ne veulent rien dire.

La solution consiste plutôt à numéroter les mots, puis à représenter chaque mot par
une liste de zéros, avec un seul 1 à la position de son
numéro. Si le vocabulaire compte 100 000 mots, chaque mot devient une liste de
100 000 nombres. On appelle ce code **un parmi *n*** (*one-hot encoding*). Le
[sac de mots](docs/module2/60-classer/#le-cas-des-pourriels) du Module 2, qui
représentait un courriel par les mots qu'il contient, était construit de cette
façon.

Ce code a un défaut. Tous les mots y sont à la même distance les uns des autres :
« chat » est aussi loin de « chien » que de « démocratie ». Le code identifie les
mots, mais il ne dit rien de leur sens. Un modèle qui a appris quelque chose sur les
chats ne peut rien en tirer pour les chiens.

{{< image src="/images/module4/un-parmi-n-ou-plongement.svg" alt="Deux panneaux. À gauche, trois mots, chat, chien et démocratie, codés chacun par une rangée de cases où une seule case est pleine, à une position différente : les trois paires de mots sont à la même distance. À droite, une carte calculée à partir de vrais plongements : chat, chien, lapin et cheval forment un groupe, rouge, bleu et vert un autre, démocratie, république et liberté un troisième, loin des deux premiers." title="À gauche, le code un parmi n ne dit rien du sens. À droite, de vrais plongements, projetés sur un plan : les mots de sens voisin sont proches." loading="lazy" >}}

## On reconnaît un mot à ses fréquentations

Pour que les nombres reflètent le sens des mots, il faut une autre idée. Elle vient
de la linguistique.

{{% hint info %}}
**Un mot inconnu**

Que signifie le mot *tezgüino*, dans les phrases suivantes&#8239;?

- Il y a une bouteille de tezgüino sur la table.
- Tout le monde aime le tezgüino.
- Le tezgüino rend ivre.
- On fabrique le tezgüino avec du maïs.

Personne n'a besoin d'une définition pour comprendre qu'il s'agit d'une boisson
alcoolisée, faite à partir de maïs. Les phrases où le mot apparaît suffisent. Cet
exemple, souvent repris en linguistique informatique, s'inspire d'une boisson
réelle, une bière de maïs fabriquée au Mexique.
{{% /hint %}}

C'est l'**hypothèse distributionnelle** : des mots qui apparaissent dans les mêmes
contextes ont des sens proches. Elle a été formulée dans les années 1950 par des
linguistes, notamment l'Américain Zellig Harris en 1954. Le Britannique John Rupert
Firth l'a résumée en 1957 par une formule souvent citée, « *You shall know a word by
the company it keeps* » (« on reconnaît un mot à ses fréquentations »).

Cette idée s'oppose à celle des
[réseaux sémantiques](docs/module1/40-representer-le-monde/#donner-un-savoir-à-la-machine)
du Module 1, où des humains décrivaient à la main le sens des mots et leurs
relations, comme « un chat est un animal ». Ici, le sens n'est décrit par personne :
il est déduit de l'usage, en observant quels mots apparaissent ensemble dans
d'énormes quantités de texte.

## Les plongements

En 2013, Tomas Mikolov et ses collègues, chez Google, publient **word2vec**, une
méthode simple et rapide pour appliquer cette idée à grande échelle. Chaque mot
reçoit une liste de quelques centaines de nombres, au départ tirés au hasard. Un
petit réseau de neurones est ensuite entraîné sur des milliards de mots de texte à
une tâche simple : à partir d'un mot, prédire les mots qui l'entourent. C'est un cas
d'[auto-supervision](docs/module2/80-trois-facons-d-apprendre/#fabriquer-soi-même-ses-réponses-lauto-supervision),
puisque le texte fournit lui-même les réponses. Pendant l'entraînement, la
rétropropagation ajuste les nombres de chaque mot. Deux mots qui apparaissent dans
les mêmes contextes, comme « chat » et « chien », finissent par recevoir des listes
de nombres voisines.

Chaque mot devient ainsi un point dans un espace de quelques centaines de
dimensions, où la distance entre deux points correspond à la différence de sens. On
parle de **plongement** (*embedding*), parce que les mots sont plongés dans un espace
géométrique. La ressemblance entre deux mots se mesure par l'angle entre leurs
vecteurs : deux vecteurs de même direction ont une ressemblance de 1, deux vecteurs
perpendiculaires une ressemblance de 0.

Certaines relations entre les mots deviennent alors des déplacements dans cet
espace. Le déplacement qui mène de « homme » à « roi » ressemble à celui qui mène de
« femme » à « reine ». On peut donc calculer *roi* − *homme* + *femme*, puis chercher
le mot le plus proche du résultat. On trouve « reine ». Ces **analogies** ont fait
la réputation de word2vec, mais elles ne fonctionnent pas toujours, comme le montre
l'applet ci-dessous.

L'applet utilise de vrais plongements, ceux que l'entreprise Facebook (aujourd'hui Meta) a publiés en 2018
pour 157 langues, avec une méthode proche de word2vec (fastText). Ceux du français
ont été appris sur des milliards de mots de pages Web. L'applet en contient 17 258,
les plus fréquents.

{{< applet src="/html/applets/plongements.html" height="531" >}}

Quelques manipulations à faire :

1. Dans l'onglet « Voisins d'un mot », cherchez les voisins de « chat », puis de
   « Montréal ». Les voisins de « Montréal » sont d'autres villes canadiennes,
   « Sherbrooke », « Toronto », « Québec ». Personne n'a indiqué au modèle qu'il
   s'agit de villes, ni qu'elles sont au Canada.
2. Dans l'onglet « Analogies », essayez *homme : roi :: femme : ?*. Essayez ensuite
   *France : Paris :: Italie : ?*. Le résultat contient des villes italiennes, Turin,
   Naples ou Milan, mais pas Rome en premier. L'analogie retrouve le type de relation
   (une grande ville du pays), sans la retrouver exactement.
3. Essayez *France : Paris :: Canada : ?*. La réponse est Toronto, avant Ottawa. Le
   modèle a appris ce que les textes associent le plus souvent au Canada et à une
   grande ville, pas la notion de capitale.
4. Dans l'onglet « Carte », choisissez le groupe « pays et capitales ». Les pays et
   les capitales se répartissent en deux régions. Essayez aussi vos propres mots.

## Les plongements héritent des préjugés

Les plongements reflètent les textes sur lesquels ils ont été appris, y compris
leurs stéréotypes. En 2016, Tolga Bolukbasi et ses collègues analysent des
plongements word2vec appris sur des articles de presse. Ils y trouvent des analogies
comme « homme est à programmeur ce que femme est à ménagère », qui a donné son titre
à leur article.

L'applet le montre aussi. Dans l'onglet « Analogies », essayez *homme : médecin ::
femme : ?*. La réponse est « infirmière ». Le modèle n'a pas de préjugé propre : il
reproduit les associations les plus fréquentes dans les textes. Mais un système
construit sur ces plongements, par exemple un outil de tri de candidatures, les
appliquerait de façon systématique. C'est le
[biais des données](docs/module2/75-bien-evaluer/#jamais-vu-mais-du-même-monde-la-question-de-la-distribution)
présenté au Module 2. Le [Module 5](docs/module5) revient sur ces questions.

## Le même mot, plusieurs sens

Le mot « avocat » désigne un juriste ou un fruit. Un plongement comme ceux de
word2vec ou de fastText n'attribue pourtant qu'un seul vecteur à chaque mot, quel
que soit son sens dans la phrase. Ce vecteur est une sorte de moyenne de tous les
emplois du mot. Comme « avocat » désigne bien plus souvent un juriste, son vecteur
se trouve du côté de la justice. Dans l'applet, ses plus proches voisins sont des
professions, surtout juridiques, et aucun fruit n'y figure.

{{< image src="/images/module4/avocat-deux-sens.svg" alt="Une carte calculée à partir de vrais plongements. Sur l'axe horizontal, de la justice vers les fruits : à gauche, tribunal, juge et procureur ; à droite, fruit, banane et tomate. Le point du mot avocat, un vecteur unique, se trouve plus près de la justice que des fruits. Deux flèches pointillées partent de ce point vers deux points vides, qui figurent les vecteurs contextuels du mot dans deux phrases : l'un rejoint le groupe de la justice, l'autre le groupe des fruits." title="Un plongement fixe donne un seul vecteur à « avocat », du côté de la justice. Un plongement contextuel calcule un vecteur différent pour chaque phrase." loading="lazy" >}}

La solution consiste à calculer le vecteur d'un mot **d'après la phrase où il
apparaît**. Dans « L'avocat plaide devant le juge », le vecteur d'« avocat » doit se
rapprocher de « juge » ; dans « Cet avocat est bien mûr », il doit se rapprocher des
fruits. En 2018, deux modèles le font pour la première fois à grande échelle : ELMo,
de l'Allen Institute for AI, avec des réseaux récurrents, puis BERT, de Google, avec
un Transformer. On parle de **plongements contextuels** (*contextual embeddings*).

C'est exactement ce que fait
l'[auto-attention](docs/module3/70-attention-transformer/#lauto-attention) présentée
au Module 3. Chaque mot interroge les autres mots de la phrase, et son vecteur est
modifié par ce qu'il y trouve. Dans un grand modèle de langage, chaque jeton entre
dans le Transformer avec son plongement fixe, puis ce vecteur est modifié couche
après couche, d'après tout le texte qui précède.

## Tout devient vecteur

Les plongements ne se limitent pas aux mots. On sait aujourd'hui représenter par un
vecteur une phrase, un paragraphe, une image, un son, une protéine ou un produit
dans un catalogue. Deux éléments de sens voisin reçoivent des vecteurs proches.

Cette idée a de nombreux usages.

- **La recherche par le sens.** Un moteur de recherche qui compare des vecteurs de
  phrases trouve un document qui répond à une question, même s'il n'utilise aucun
  des mots de la question. Le chapitre du [Module 4](docs/module4/80-outils-et-agents/#chercher-dabord-répondre-ensuite) sur les outils
  et les agents y reviendra.
- **La recommandation.** Les plateformes de musique ou de vidéo représentent chaque
  morceau et chaque utilisateur par un vecteur, et proposent les morceaux proches.
- **Les liens entre images et textes.** Si une image et sa légende reçoivent des
  vecteurs proches, on peut chercher une image avec une phrase, ou guider la
  génération d'une image par un texte. C'est le sujet du chapitre du
  [Module 4](docs/module4/90-mots-et-images) sur les mots et les images.

Les mots sont maintenant des vecteurs, et le Transformer sait les modifier d'après
leur contexte. Le [chapitre suivant](docs/module4/50-predire-le-mot-suivant) montre comment un modèle s'en
sert pour prédire le mot suivant d'un texte, et pour écrire.
