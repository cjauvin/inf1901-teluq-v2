---
title: "Travail noté 1"
weight: 99
slug: travail-noté-1
---

# Vous êtes le moteur d'inférence : un système expert (travail noté 1)

Au [Module 1](docs/module1), nous avons vu qu'avant l'apprentissage automatique (que nous commencerons à étudier en détail au [module 2](docs/module2)), la grande idée de
l'IA « classique » (le GOFAI) était de **capturer la connaissance dans des règles
explicites**. Les **[systèmes experts](docs/module1/50-systemes-experts)** sont
l'aboutissement de cette idée. Ils comportent une **base de règles** `si… alors…`,
une **base de faits** (le cas qu'on traite) et un **moteur d'inférence**, qui
compare les deux, déclenche les règles applicables et en tire de nouvelles
conclusions, jusqu'au diagnostic final.

Dans ce travail, vous allez jouer le rôle de ce moteur d'inférence sur un petit
système expert qui **identifie des animaux** à partir de leurs caractéristiques.
Vous allez le faire fonctionner, trouver un cas où il échoue, puis tenter de
l'améliorer. Vous observerez ainsi directement ce qu'on a appelé le **[goulot
d'étranglement de la connaissance](docs/module1/50-systemes-experts)**.

Une règle a la forme suivante :

```
SI  (mammifère)  ET  (mange de la viande)   ALORS  (carnivore)
```

Les conditions d'une règle sont **toujours reliées par des ET, jamais par des OU**.
Une règle ne se déclenche donc que si **toutes** ses conditions sont vraies en même
temps. Dans l'exemple ci-dessus, `mammifère` **et** `mange de la viande` doivent
être vrais tous les deux pour qu'on conclue `carnivore`. Une seule des deux
conditions ne suffit pas. Pour exprimer un « OU » (par exemple `a du poil` **ou**
`allaite ses petits` → `mammifère`), on écrit **deux règles séparées**. C'est ce
que fait la base avec R1 et R2.

Le « savoir » du système n'est qu'un ensemble de règles de ce type. Son
« raisonnement » est un mécanisme simple qui vérifie quelles règles ont toutes
leurs conditions réunies. Comme nous le verrons, toute l'intelligence du système
tient dans une seule formule.

## Consignes

1. Ouvrez le [fichier Google Sheets fourni pour ce travail](https://docs.google.com/spreadsheets/d/1R6-yobTFy5XE9eUPg_XhnjEZ3efEQU0V76uQSBtPwIc/edit?usp=sharing)
   et **faites-en une copie** (*Fichier ▸ Créer une copie*). Vous ferez tout votre
   travail à partir de **votre copie**.

2. Une fois vos manipulations terminées, [partagez votre fichier](docs/50-google-sheets/#fonction-de-partage-anonyme-dun-fichier) et copiez le lien vers celui-ci dans un document PDF (**Attention&nbsp;: aucun autre format que PDF ne sera accepté**).

3. Répondez aux questions d'interprétation de la dernière section dans le même
   fichier PDF, en fournissant des réponses claires et précises.

## Le système

Le classeur ne comporte que **deux onglets**. Il constitue le système expert réduit
à l'essentiel, c'est-à-dire une base de faits et une base de règles.

- **Faits** : la liste de toutes les caractéristiques possibles (les *attributs
  observables* comme `a du poil`, mais aussi les *catégories* déduites comme
  `mammifère` et les *espèces*). Chaque fait a une case **Vrai ?** à cocher.
- **Base de règles** : les 11 règles `si… alors…`, sous forme de conditions et d'une
  conclusion.

L'élément central du système est la colonne **« Activable ? »** de la *Base de
règles*. Pour chaque règle, cette formule vérifie que **toutes ses conditions sont
vraies** dans l'onglet *Faits* et que sa conclusion n'a pas déjà été établie :

```
=IF($F3="","",AND(
   IF($B3="",TRUE,VLOOKUP($B3,Faits!$A:$B,2,FALSE)=TRUE),
   IF($C3="",TRUE,VLOOKUP($C3,Faits!$A:$B,2,FALSE)=TRUE),
   IF($D3="",TRUE,VLOOKUP($D3,Faits!$A:$B,2,FALSE)=TRUE),
   IF($E3="",TRUE,VLOOKUP($E3,Faits!$A:$B,2,FALSE)=TRUE),
   VLOOKUP($F3,Faits!$A:$B,2,FALSE)<>TRUE))
```

Cette formule est celle de la règle R1, qui occupe la ligne 3 du tableau. Chaque
`VLOOKUP` cherche un fait dans l'onglet *Faits* et lit sa case **Vrai ?**. La
colonne voisine, **« Déjà conclue ? »**, indique si la conclusion de la règle est
déjà cochée. Un **bandeau d'état**, sur la première ligne de l'onglet, résume où
vous en êtes : il vous invite à continuer tant qu'une règle est verte, il annonce
l'animal identifié, ou il signale que le système est bloqué.

Quand une règle est activable, sa ligne est **surlignée en vert**, ce qui signifie
qu'elle est prête à se déclencher. C'est vous qui jouez le rôle du moteur. Vous
choisissez une règle verte et vous **cochez sa conclusion** dans l'onglet *Faits*.
Cette action rend d'autres règles vertes, et ainsi de suite.

Dans un vrai système expert, ce travail est entièrement **automatique**. Un
programme, le *moteur d'inférence*, parcourt la base de règles, repère celles dont
toutes les conditions sont réunies, les déclenche, ajoute leurs conclusions à la
base de faits, puis recommence, jusqu'à ce qu'aucune règle ne s'applique plus.
L'humain n'intervient pas. Ici, **pour des raisons pédagogiques, c'est vous qui
tenez ce rôle**. Vous exécutez à la main l'algorithme que la machine exécuterait
seule. Le but est de vous faire constater à quel point ce raisonnement est
mécanique. Il s'agit d'une simple boucle qui applique des règles, sans aucune
compréhension de ce qu'est un guépard ou un manchot.

{{< image src="/images/module1/tn1-regle-verte.png" alt="L'onglet Base de règles : le bandeau jaune « Continuez : déclenchez une règle surlignée en vert », puis les onze règles ; la ligne de R1 (a du poil, alors mammifère) est surlignée en vert et sa colonne Activable ? affiche TRUE." title="Le Cas 1 au départ : seule la règle R1 est activable, et sa ligne est surlignée en vert." loading="lazy" >}}

## Manipulation 1 — Tracer le raisonnement

Voici le **Cas 1** : cochez `a du poil`, `mange de la viande`, `robe fauve` et
`taches sombres` dans l'onglet *Faits* (laissez tout le reste à FAUX).

Une seule règle devient verte, **R1**. Déclenchez-la (cochez sa conclusion,
`mammifère`, dans l'onglet *Faits*). Une nouvelle règle s'active. Déclenchez-la à
son tour, et continuez jusqu'à ce qu'une **espèce** passe à VRAI.

Au fur et à mesure, **notez la trace** de votre raisonnement directement dans votre
document PDF, sous la forme d'un petit tableau, avec une ligne par règle
déclenchée :

| Étape | Règle déclenchée | Nouveau fait établi | Pourquoi (conditions réunies) |
|-------|------------------|---------------------|-------------------------------|
| 1     | R1               | `mammifère`         | `a du poil` est vrai          |
| 2     | …                | …                   | …                             |

Recommencez ensuite avec le **Cas 2**, le manchot (`a des plumes`,
`incapable de voler`, `nage`, `plumage noir et blanc`), après avoir remis tous les
faits à FAUX.

{{% hint warning %}}
**Pour remettre les faits à FAUX**, décochez les cases une à une en cliquant dessus.
N'utilisez pas la touche Suppr (ou Retour arrière) sur les cases, parce qu'elle
supprime la case à cocher au lieu de la décocher. Si cela vous arrive, annulez avec
Ctrl+Z (Cmd+Z sur Mac), ou recréez les cases avec *Insertion ▸ Case à cocher*.
{{% /hint %}}

## Manipulation 2 — Casser le système

Remettez tous les faits à FAUX, puis chargez le **Cas 3** : `a du poil`,
`a des sabots`, `rumine`.

Faites fonctionner le moteur. Vous obtenez `mammifère`, puis plus aucune règle ne
s'active. Aucune règle d'espèce ne devient verte. Le système est **bloqué**, parce
qu'il ne sait pas identifier cet animal (il s'agit, par exemple, d'une
**antilope**).

## Manipulation 3 — Étendre la base de règles

Vous devez maintenant ajouter le savoir manquant. Sur la première ligne vide de la
*Base de règles*, écrivez une nouvelle règle qui conclut `antilope`. Utilisez les
**menus déroulants** pour les conditions.

L'espèce `antilope` n'est pas encore dans l'onglet *Faits*. Ajoutez-la sur la
première ligne vide, en remplissant les trois colonnes :

- son nom, `antilope`, dans la colonne *Fait* ;
- une case à cocher dans la colonne *Vrai ?* (*Insertion ▸ Case à cocher*) ;
- la mention `espèce (conclusion)` dans la colonne *Catégorie*. Sans cette mention,
  le bandeau d'état ne reconnaît pas l'antilope comme une espèce, et il continue
  d'afficher que le système est bloqué.

Procédez de la même façon pour tout nouvel attribut dont vous auriez besoin, avec
la mention `observable` dans la colonne *Catégorie*.

Vérifiez que votre règle identifie bien le Cas 3. Ensuite, **testez sa solidité** :
chargez un autre animal (par exemple le **zèbre** : `a du poil`, `a des sabots`,
`rayures noires`). Votre nouvelle règle se déclenche-t-elle aussi, par erreur&nbsp;?
Modifiez-la si nécessaire.

{{< image src="/images/module1/tn1-nouvelle-regle.png" alt="L'onglet Base de règles avec une douzième ligne : R12, mammifère, a des sabots, rumine, alors antilope. Cette ligne est surlignée en vert." title="Une nouvelle règle, R12, ajoutée sur la première ligne vide : elle devient activable pour le Cas 3." loading="lazy" >}}

## Questions d'interprétation

1. Pour le Cas 1, combien de règles se sont déclenchées, et dans quel ordre&nbsp;?
   Décrivez la **cascade** : en quoi la conclusion d'une règle sert-elle de condition
   à une autre&nbsp;?

2. Dans ce système, le « savoir » (la base de règles) et le « raisonnement » (le
   moteur) sont **séparés**. Si l'on remplaçait entièrement la base de règles par des
   règles de diagnostic automobile, qu'est-ce qui changerait, et qu'est-ce qui
   resterait identique&nbsp;?

3. Le système peut **expliquer** sa conclusion (le tableau de trace que vous avez
   rempli le montre). En quoi est-ce une force&nbsp;? Comparez avec ce que vous
   anticipez d'un réseau de neurones ([Module 3](docs/module3)).

4. Vous avez fait fonctionner le moteur « vers l'avant » (des faits vers la
   conclusion), ce qu'on appelle le **chaînage avant**. Comment auriez-vous procédé
   pour vérifier une hypothèse précise (« et si c'était un tigre&nbsp;? ») sans tout
   cocher d'avance, c'est-à-dire en **chaînage arrière**&nbsp;?

5. Au Cas 3, pourquoi exactement le système s'est-il bloqué&nbsp;? Qu'est-ce que cela
   révèle sur sa capacité à gérer un cas **imprévu**&nbsp;?

6. La règle que vous avez ajoutée risquait-elle de **mal classer** d'autres
   animaux&nbsp;? Décrivez ce que vous avez observé en la testant sur le zèbre, et ce
   que cela indique sur la difficulté de maintenir une grosse base de règles.

7. Supposons qu'on veuille étendre ce système pour identifier **tous les animaux du
   monde**. Décrivez concrètement ce qui se passerait pour la base de règles. Quel
   concept des chapitres « [Capturer l'expertise](docs/module1/50-systemes-experts) »
   et « [Les hivers et la bascule](docs/module1/60-hivers) » cela illustre-t-il&nbsp;?

8. Un zoologiste reconnaît souvent un animal « d'un coup d'œil », sans pouvoir
   énoncer la règle exacte qu'il applique. Quel nom donne-t-on à ce type de savoir,
   et pourquoi pose-t-il problème à un système expert&nbsp;?

9. Ce système **apprend-il** de son expérience&nbsp;? Si on lui présentait mille
   animaux, ses règles s'amélioreraient-elles d'elles-mêmes&nbsp;? Quelle conséquence
   cela a-t-il, et vers quel changement de paradigme ([Module 2](docs/module2)) cela conduit-il&nbsp;?

10. Toute « l'intelligence » du moteur tient dans la formule de la colonne
    *Activable ?*. Diriez-vous que ce système pense&nbsp;? Reliez votre réponse au
    [test de Turing](docs/module1/10-turing) et à l'[« effet IA »](docs/module1/60-hivers).

11. Les systèmes experts ont presque disparu sous ce nom, mais leur mécanisme
    existe toujours (voir « [Les hivers et la bascule](docs/module1/60-hivers) »).
    Donnez un exemple, tiré de la vie courante, d'un endroit où
    une base de règles `si… alors…` décide encore quelque chose à votre sujet.
