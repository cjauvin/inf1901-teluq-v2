---
title: "Travail noté 4"
weight: 99
slug: travail-noté-4
---

# Un modèle de langage dans un tableur (travail noté 4)

Ce travail construit, dans Google Sheets, un modèle de langage miniature : un modèle
à **bigrammes**, qui donne la probabilité de chaque mot d'après le mot qui le précède.
C'est le principe des [n-grammes](docs/module4/44-des-regles-aux-probabilites/#compter-les-n-grammes)
présenté au chapitre « Prédire le mot suivant », avec *n* = 2. Le modèle est ensuite
utilisé pour **générer** du texte, en tirant chaque mot au hasard selon ces
probabilités, comme le font, à une tout autre échelle, les grands modèles de langage.

{{% hint info %}}
**Avant de commencer**

- Un modèle de langage n'est pas une description abstraite de la langue. C'est un
  modèle statistique entraîné sur un texte particulier, le **corpus d'entraînement**.
  Deux modèles entraînés l'un sur des romans du XIXᵉ siècle, l'autre sur des messages
  de réseaux sociaux, donneraient des probabilités très différentes.
- Le modèle calcule une
  [probabilité conditionnelle](https://fr.wikipedia.org/wiki/Probabilit%C3%A9_conditionnelle),
  notée avec une barre verticale, qui se lit « étant donné » :

  $$P(\text{mot suivant} \mid \text{mot précédent})$$

- Le modèle du [travail noté 2](docs/module2/99-travail-noté-2) classait des courriels.
  Il reposait sur une description de chaque classe, retournée par le théorème de
  Bayes : c'était un modèle génératif utilisé pour
  [classer](docs/module2/60-classer/#renverser-le-problème-la-classification-bayésienne).
  Le modèle de ce travail est utilisé pour ce qu'il est : un modèle qui génère.
- Vérifiez d'abord que votre Google Sheets est
  [correctement configuré](docs/50-google-sheets/#paramètres-linguistiques).
{{% /hint %}}

Générer un texte avec ce modèle revient à tirer chaque mot au hasard, selon les
probabilités qui dépendent du mot précédent. La figure ci-dessous montre un tirage
après le mot « le », avec les probabilités que vous allez calculer.

{{< image src="/images/module4/tn4-tirer-le-mot-suivant.svg" alt="En haut, une bande horizontale de 0 à 1 découpée en trois segments, un par mot qui peut suivre « le » : chat de 0 à 0,5, chien de 0,5 à 0,9, fromage de 0,9 à 1. Une flèche marque un nombre tiré au hasard, 0,63, qui tombe dans le segment de chien. En bas, une chaîne de mots générés, le, chien, court, le, chat, chaque mot étant tiré d'après le mot qui le précède." title="Tirer le mot suivant : on place les probabilités bout à bout entre 0 et 1, on tire un nombre au hasard, et on prend le mot dans le segment duquel il tombe. La formule de génération du tableur fait exactement ce calcul." loading="lazy" >}}

## Consignes

1. Construisez le fichier Google Sheets en suivant les étapes ci-dessous.
2. Une fois le fichier complet et fonctionnel,
   [partagez-le](docs/50-google-sheets/#fonction-de-partage-anonyme-dun-fichier), et
   copiez son lien dans un document PDF (**aucun autre format ne sera accepté**).
3. Répondez aux questions de la fin de cette page dans le même document PDF, de façon
   claire et précise.

## Entraînement du modèle

Copiez les mots du texte suivant dans la colonne `A` d'une nouvelle feuille, un mot
par rangée. Utilisez correctement la
[fonction copier-coller](docs/50-google-sheets/#fonction-copier-coller) de Google
Sheets.

```
le
chat
dort
le
chien
mange
le
chat
mange
une
souris
le
chien
dort
la
souris
court
la
souris
mange
le
fromage
le
chat
court
le
chien
voit
le
chat
le
chat
voit
la
souris
le
chien
court
```

Ces 38 mots forment le corpus d'entraînement, le texte à partir duquel le modèle
calcule ses paramètres. Pour les vrais modèles de langage, ce corpus contient une
grande partie du texte disponible sur le Web, comme les archives de
[Common Crawl](https://commoncrawl.org).

Dans la cellule `B1`, entrez la formule suivante :

```
=A2
```

Étendez la colonne `B` jusqu'à la cellule `B37`, en double-cliquant sur le petit
carré qui apparaît au coin inférieur droit de la cellule `B1` quand on la
sélectionne. Google Sheets peut aussi proposer de le faire automatiquement.

Dans la cellule `C1`, entrez la formule suivante, puis étendez-la jusqu'à `C37` :

```
=A1 & " " & B1
```

{{< image src="/images/module4/tn4/sheets_3_first_cols.png" alt="Une capture de Google Sheets : la colonne A contient les mots du corpus, la colonne B le mot suivant de chacun, et la colonne C les deux mots réunis, comme « le chat », « chat dort », « dort le »." title="Les trois premières colonnes : chaque mot, le mot qui le suit, et le bigramme qu'ils forment." loading="lazy" >}}

La colonne `C` contient maintenant tous les **bigrammes** du corpus, c'est-à-dire
toutes les suites de deux mots consécutifs. La colonne `B` ne sert qu'à les obtenir
facilement.

Dans la colonne `D`, comptez combien de fois chaque bigramme apparaît dans le corpus,
avec la formule suivante, étendue jusqu'à `D37` :

```
=COUNTIF(C:C, C1)
```

{{% hint warning %}}
Si la formule produit une erreur, vérifiez les
[paramètres linguistiques](docs/50-google-sheets/#paramètres-linguistiques) de votre
Google Sheets.
{{% /hint %}}

Le bigramme `le chien` apparaît par exemple 4 fois, et le bigramme `fromage le` une
seule fois.

La colonne `E` calcule les **paramètres** du modèle, c'est-à-dire la probabilité d'un
mot étant donné le mot qui le précède :

$$P(\text{mot de la colonne B} \mid \text{mot de la colonne A}) =
\frac{\text{nombre de fois où le bigramme A B apparaît}}{\text{nombre de fois où le mot A apparaît}}$$

Entrez dans la cellule `E1` la formule suivante, et étendez-la jusqu'à `E37`. Elle
compte les mots de la colonne `A` sauf le dernier, qui n'est suivi d'aucun mot et
fausserait légèrement les probabilités :

```
=D1 / COUNTIF(A$1:INDEX(A:A, COUNTA(A:A)-1), A1)
```

Le dénominateur est toujours supérieur ou égal au numérateur, et chaque valeur est
donc une probabilité comprise entre 0 et 1.

Dans la colonne `F`, gardez une seule fois chaque bigramme, ce qui donne 26 bigrammes
différents :

```
=SORT(UNIQUE(C:C))
```

Séparez ensuite les deux mots de chacun de ces bigrammes, le premier dans la colonne
`G` :

```
=INDEX(SPLIT(F1, " "), 1)
```

et le second dans la colonne `H` :

```
=INDEX(SPLIT(F1, " "), 2)
```

Enfin, la colonne `I` reprend la probabilité correspondante de la colonne `E` :

```
=INDEX(E:E, MATCH(F1, C:C, 0))
```

On constate par exemple que le mot `la` est toujours suivi du mot `souris`, avec une
probabilité de 1, tandis que le mot `le` peut être suivi de `chat`, `chien` ou
`fromage`, avec des probabilités de 0,5, 0,4 et 0,1.

{{< image src="/images/module4/tn4/sheets_model_complete.png" alt="Une capture de Google Sheets avec les neuf colonnes du modèle : les bigrammes, leur nombre d'occurrences, leur probabilité, puis la liste des 26 bigrammes différents, séparés en premier et second mot, avec leur probabilité." title="Le modèle complet : les colonnes G, H et I donnent, pour chaque mot, les mots qui peuvent le suivre et leur probabilité." loading="lazy" >}}

## Utilisation du modèle (inférence)

Le modèle est maintenant entraîné : ses paramètres sont calculés. On peut s'en servir
pour générer un texte nouveau, en tirant les mots au hasard.

Entrez un premier mot dans la cellule `J1`, par exemple `le`. Ce mot doit faire partie
du vocabulaire du modèle. Entrez ensuite la formule suivante dans la cellule `K1` si
vous voulez générer les mots à l'horizontale, ou dans la cellule `J2` si vous voulez
les générer à la verticale :

```
=LET(
  next_word_mask, ARRAYFORMULA($G:$G = J1),
  next_words, FILTER($H:$H, next_word_mask),
  probs, FILTER($I:$I, next_word_mask),
  probs_cumul, SCAN(0, probs, LAMBDA(a, b, a + b)),
  sampled_word_idx, MATCH(RAND(), {0; probs_cumul}, 1),
  INDEX(next_words, sampled_word_idx)
)
```

{{% hint warning %}}
Cette formule s'étend sur plusieurs lignes. Entrez-la dans la barre de formule, en
haut de la feuille, plutôt que directement dans la cellule.
{{% /hint %}}

{{< image src="/images/module4/tn4/sheets_generate.png" alt="Une capture de Google Sheets. La formule de génération est affichée dans la barre de formule, encadrée en rouge. La cellule J1 contient le mot de départ, « le », et la cellule K1 le mot généré, « chat ». Une flèche rouge indique qu'on étend la formule vers la droite pour générer les mots suivants." title="La génération : la cellule K1 tire un mot d'après le mot de J1 ; en étendant la formule vers la droite, chaque cellule tire un mot d'après la précédente." loading="lazy" >}}

La formule fait trois choses.

1. Elle retrouve les mots qui peuvent suivre le mot de départ, et leurs probabilités.
2. Elle place ces probabilités bout à bout entre 0 et 1, en calculant leurs sommes
   successives (les probabilités cumulées).
3. Elle tire un nombre au hasard entre 0 et 1, avec `RAND()`, et choisit le mot dans le
   segment duquel ce nombre tombe, comme dans la figure du début de cette page.

Pour continuer la génération, étendez la formule vers la droite (à partir de `K1`) ou
vers le bas (à partir de `J2`). Chaque nouvelle modification de la feuille relance les
tirages, et produit donc un nouveau texte.

## Questions

### Le modèle et ses paramètres

1. Quels sont les paramètres du modèle ? Indiquez précisément les colonnes qui les
   contiennent.

2. Expliquez dans vos mots comment ces paramètres sont calculés.

3. En quoi la colonne `B` de ce modèle diffère-t-elle de la colonne `B` du modèle de
   classification des courriels du [travail noté 2](docs/module2/99-travail-noté-2) ?

4. Expliquez pourquoi le modèle de classification du travail noté 2 était utilisé
   comme un modèle discriminatif, alors que ce modèle de langage est utilisé comme un
   modèle génératif. (Voir « [Décrire plutôt que séparer](docs/module4/10-generer/#décrire-plutôt-que-séparer) ».)

### Ce que le corpus enseigne au modèle

5. Quelle est la conséquence du fait que le bigramme `le chat` apparaisse 5 fois dans
   le corpus d'entraînement ?

6. Quelle est la conséquence du fait que le bigramme `la souris` apparaisse 3 fois, et
   en quoi cette situation diffère-t-elle de celle de la question 5 ?

7. Certains bigrammes permettent-ils de générer des suites moins grammaticales ?
   Lesquels, en particulier ?

8. Certains bigrammes permettent-ils de générer des suites dont le sens est étrange ?
   Lesquels, en particulier ?

9. Le modèle peut-il générer un bigramme qui ne fait pas partie de ses exemples
   d'entraînement ? Expliquez.

### Générer

10. Supposons que le modèle ait généré le mot `voit`. Expliquez la conséquence du choix
    du mot suivant sur la suite de la phrase générée.

11. La longueur des phrases générées par le modèle est-elle limitée ? Expliquez.

12. Le chapitre « [Générer](docs/module4/10-generer/#la-température) » présente la
    température. Comment le texte généré changerait-il si l'on tirait toujours le mot
    le plus probable, ce qui correspond à une température très basse ? Donnez un
    exemple à partir du mot `le`.

### Les limites du modèle, et les grands modèles de langage

13. De quel type d'apprentissage s'agit-il : supervisé, non supervisé ou
    auto-supervisé ? Justifiez votre réponse. (Voir
    « [Trois façons d'apprendre](docs/module2/80-trois-facons-d-apprendre/#fabriquer-soi-même-ses-réponses-lauto-supervision) ».)

14. Qu'est-ce qui changerait si l'on utilisait un modèle à trigrammes plutôt qu'à
    bigrammes ? Quelles seraient les contraintes de ce choix ? Vous pouvez comparer les
    tailles 2 et 3 dans l'applet du chapitre
    « [Prédire le mot suivant](docs/module4/44-des-regles-aux-probabilites/#compter-les-n-grammes) ».

15. Expliquez les limites de ce modèle quant à sa capacité de généralisation. À quoi
    sont-elles dues, et comment le modèle neuronal de 2003 présenté au chapitre
    « [Prédire le mot suivant](docs/module4/50-predire-le-mot-suivant/#généraliser-les-modèles-neuronaux) »
    les dépasse-t-il ?

16. Comment pourrait-on faire en sorte que le modèle génère des phrases complètes, avec
    un début et une fin ? Indice : pensez au jeton spécial qui marque la fin d'un texte
    dans les grands modèles de langage.
