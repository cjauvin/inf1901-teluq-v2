---
title: "Travail noté 2"
weight: 99
slug: travail-noté-2
---

# Classification naïve bayésienne pour détecter les pourriels (travail noté 2)

La classification naïve bayésienne est un algorithme d'apprentissage supervisé
qui repose sur les probabilités. Nous avons vu deux variantes de cet
algorithme :

1. [La classification de simples points en 2d avec un modèle gaussien](docs/module2/60-classer/#renverser-le-problème-la-classification-bayésienne)
2. [La classification de vecteurs en haute dimension avec un modèle multinomial](docs/module2/60-classer/#le-cas-des-pourriels)

La classification de courriels est un problème classique qu'on peut traiter avec
cet algorithme. On cherche à estimer la probabilité qu'un courriel soit un
pourriel à partir des mots qu'il contient, parce que certains mots sont plus
souvent utilisés dans les pourriels et d'autres dans les courriels.

Comme nous l'avons vu, la classification naïve bayésienne est un algorithme
d'apprentissage *génératif*. On considère donc d'abord deux modèles (un pour
chaque classe, `pourriel` ou `courriel`), dont le rôle est de générer les données
observées plutôt que de les classifier directement :

$$P(\text{les mots générés} \mid \text{il s'agit d'un pourriel})$$
$$P(\text{les mots générés} \mid \text{il s'agit d'un courriel})$$

ou, de manière plus compacte :

$$P(\mathbf{x} \mid \mathtt{pourriel})$$
$$P(\mathbf{x} \mid \mathtt{courriel})$$

Comme ce qui nous intéresse ici est de classifier les courriels, nous utilisons
le [théorème de
Bayes](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Bayes) pour
« inverser » les modèles et obtenir une règle de classification simple, qui
prédit la classe plutôt que les mots :

$$
\text{classification}(\mathbf{x}) =
\left\{
\begin{array}{ll}
\mathtt{pourriel} \text{ si } P(\mathbf{x} \mid \mathtt{pourriel}) P(\mathtt{pourriel}) \ge P(\mathbf{x} \mid \mathtt{courriel}) P(\mathtt{courriel}) & \\
\mathtt{courriel} \text{ sinon } & \\
\end{array}
\right.
$$

## Consignes

1. Suivez les instructions ci-dessous pour construire d'abord le fichier Google Sheets avec toutes les données nécessaires.

2. Une fois le fichier complété et fonctionnel, [partagez votre fichier](docs/50-google-sheets/#fonction-de-partage-anonyme-dun-fichier) et copiez le lien vers celui-ci dans un document PDF (**Attention : aucun autre format que PDF ne sera accepté**).

3. Répondez aux questions d'interprétation de la dernière section dans le même fichier PDF, en fournissant des réponses claires et précises.

## Entraînement du modèle

Cette section montre comment calculer ces probabilités en entraînant un modèle
de classification sur une série de courriels.

Comme nous allons utiliser le tableur en ligne [Google Sheets](docs/50-google-sheets), assurez-vous d'abord qu'il est
correctement configuré.

Copiez d'abord ces 10 mini-courriels dans la colonne A d'une nouvelle
« feuille » Google Sheets, un courriel par rangée (si vous utilisez le
copier-coller, assurez-vous de bien appliquer la [fonction « copier-coller »](docs/50-google-sheets/#fonction-copier-coller)) :

```
voici le colis est arrivé
bonjour voici le lien
offre spéciale colis gratuit
merci pour votre colis
colis livré demain matin
voici votre carte gratuite
réunion demain à midi
voici le code pour carte
livraison spéciale pour vous
merci encore pour votre carte
```

Pour avoir un aperçu de la tâche d’étiquetage des données (qui, dans un scénario
réel, peut être très coûteuse et laborieuse), nous vous proposons d'abord de
catégoriser vous-mêmes les courriels dans la colonne `B`, en utilisant la valeur
`oui` si vous considérez qu'il s'agit d'un pourriel, ou `non` (ce n'est pas un
pourriel) sinon.

Si vous préférez ne pas faire cet exercice maintenant, vous pouvez copier ces
valeurs (dans la colonne `B`) :

```
non
non
oui
non
non
oui
non
non
oui
non
```

À ce stade, votre feuille devrait ressembler à ceci :

![](/images/module2/tn2/sheets_cols_a_et_b.png)

Calculez d'abord, dans la colonne `C`, la probabilité à priori qu'un courriel
quelconque soit un pourriel ou non (sans tenir compte des mots pour le
moment) :

```
=MAP(UNIQUE(B1:B10), LAMBDA(x, COUNTIF(B1:B10, x) / COUNTA(B1:B10)))
```

{{% hint warning %}}

Si vous obtenez une erreur avec la formule à ce stade, il est très possible que
les paramètres linguistiques de votre Google Sheets ne soient pas [correctement configurés](../50-google-sheets#parametres-linguistiques).

{{% /hint %}}

Ces probabilités à priori serviront plus loin. Définissez ensuite la colonne `D`
avec cette formule :

```
=UNIQUE(TRANSPOSE(SPLIT(TEXTJOIN(" ", TRUE, A:A), " ")))
```

La colonne `D` devrait maintenant contenir le vocabulaire des courriels :

![](/images/module2/tn2/sheets_col_d_voc.png)

La colonne `E` doit ensuite contenir le nombre de fois où les mots de la colonne
`D` apparaissent dans les courriels valides (ceux marqués `non`, qui ne sont pas
des pourriels) :

```
=SUMPRODUCT((B$1:B$10="non") * ISNUMBER(SEARCH(D1, A$1:A$10)))
```

De la même manière, la colonne `F` contient la fréquence des mots qui
apparaissent dans les courriels marqués `oui`, qui sont des pourriels :

```
=SUMPRODUCT((B$1:B$10="oui") * ISNUMBER(SEARCH(D1, A$1:A$10)))
```

{{% hint warning %}}

Notez que les colonnes `E` et `F` doivent avoir le même nombre d'éléments que la
colonne `D`. Il faut donc utiliser la fonction de remplissage automatique. Le
plus simple est de glisser (*drag*) la première cellule vers le bas, une fois
qu'elle a été calculée, ou de double-cliquer sur le petit « + » noir qui apparaît
en bas à droite de la première cellule.

{{% /hint %}}

![](/images/module2/tn2/sheets_col_e_drag.png)

![](/images/module2/tn2/sheets_cols_e_et_f.png)

À partir de ces fréquences de mots pour chaque classe (`oui` ou `non`), on peut
maintenant calculer la probabilité conditionnelle de chaque mot du vocabulaire,
selon que le courriel est un pourriel (`oui`) ou non (`non`). La colonne `G`
correspond à la probabilité des mots sachant que le courriel n'est pas un
pourriel (`non`) :

```
=(E1 + 1) / (SUM(E:E) + COUNTA(D:D))
```

De la même manière, la colonne `H` contient la probabilité des mots sachant que
le courriel est un pourriel (`oui`) :

```
=(F1 + 1) / (SUM(F:F) + COUNTA(D:D))
```

Les colonnes `G` et `H` doivent elles aussi avoir la même taille que le
vocabulaire (colonne `D`). Il faut donc utiliser le remplissage automatique
décrit plus haut.

![](/images/module2/tn2/sheets_cols_g_et_h.png)

Le modèle est maintenant entièrement entraîné et prêt à être utilisé.

---

## Utilisation du modèle (inférence)

Nous allons maintenant utiliser le modèle pour déterminer si un nouveau courriel
(qui n'a pas servi à l'entraînement) est un pourriel ou non. Dans la colonne `I`,
entrez un courriel à tester :

```
voici votre carte spéciale
```

Extrayez les mots du courriel dans la colonne `J` :

```
=TRANSPOSE(SPLIT(I1, " "))
```

Il faut ensuite, dans la colonne `K`, la probabilité des mots de ce courriel de
test dans l'hypothèse où ce n'est pas un pourriel (`non`) :

```
=IFERROR(XLOOKUP(J1, D:D, G:G), 1E-5)
```

De la même manière, la colonne `L` contient la probabilité des mots du courriel
dans l'hypothèse où il s'agit d'un pourriel (`oui`) :

```
=IFERROR(XLOOKUP(J1, D:D, H:H), 1E-5)
```

Les colonnes `K` et `L` doivent avoir la même taille que la colonne `J`.
Utilisez donc le remplissage automatique. Calculez ensuite, dans la colonne `M`,
la probabilité que le courriel ne soit pas un pourriel (`non`) :

```
=PRODUCT(K:K) * C1
```

Dans la colonne `N`, calculez la probabilité que le courriel soit un pourriel
(`oui`) :

```
=PRODUCT(L:L) * C2
```

La classification finale se trouve dans la colonne `O` :

```
=IF(M1 > N1; "non"; "oui")
```

![](/images/module2/tn2/sheets_toutes_les_cols.png)

## Questions d'interprétation

1. Que se passe-t-il si vous remplacez le mot « spéciale » par le mot
   « livrée » dans le courriel de test de la cellule `I1` ?

2. Après ce changement, expliquez les probabilités qu'on trouve aux cellules
   `K4` et `L4` associées au nouveau mot « livrée ». D'où proviennent ces nouvelles
   valeurs, et pourquoi a-t-on besoin d'y avoir recours dans le calcul ?

3. Est-ce que ce modèle est [paramétrique](docs/module2/70-generaliser/#paramétrique-ou-non-paramétrique) ou non ? Expliquez pourquoi.

4. S'il s'agit d'un modèle paramétrique, quels sont les paramètres du
   modèle (quelles colonnes) ?

5. Quelles colonnes constituent la partie *générative* du modèle ? Expliquez pourquoi.

6. Quelles colonnes constituent la partie *discriminative* du modèle ? Expliquez pourquoi.

7. Quelle est la signification des nombres dans les cellules `G11` et
   `H11` ? Comment peut-on les interpréter ?

8. Quelles sont les probabilités non conditionnelles (à priori) ? À quoi servent-elles ?

9. Est-ce qu'il serait possible d'utiliser seulement ces probabilités
   non conditionnelles pour faire un modèle de classification ? Quelles
   conséquences cela entraînerait-il ?

10. De quelle manière peut-on dire que ce modèle généralise ?

11. Est-ce que l'ordre des mots joue un rôle dans les décisions de ce
    modèle ? Expliquez pourquoi.

12. Si l'ordre des mots ne joue pas de rôle, comment pourrait-on
    modifier le modèle pour qu'il en joue un ?

13. Est-ce que certains mots aident particulièrement le modèle ? Si oui,
    pourquoi ?

14. Est-ce que certains mots sont moins utiles ? Si oui, pourquoi ?
