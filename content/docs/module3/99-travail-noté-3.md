---
title: "Travail noté 3"
weight: 99
# bookToc: false
slug: travail-noté-3
---

# Apprivoisez un réseau de neurones (travail noté 3)

Voici l'application [Tensorflow Playground](https://playground.tensorflow.org),
offerte en [logiciel libre](https://github.com/tensorflow/playground), que nous
avons quelque peu adaptée pour les besoins de ce cours. Elle permet d'explorer
de manière interactive et intuitive le fonctionnement des réseaux de neurones.
Si l'application est coupée sur votre écran, ouvrez-la
[en pleine page]({{< rel "/html/playground/index.html#dataset=gauss&networkShape=&showTestData_hide=true&percTrainData_hide=true&batchSize_hide=true&dataset_hide=false&activation_hide=true&problem=classification&problem_hide=true&regularization_hide=true&regularizationRate_hide=true&learningRate_hide=true&discretize_hide=true" >}}).

## Consignes

1. En utilisant l'application interactive, effectuez les expériences proposées
   dans la section "Instructions et questions" ci-bas.

2. Répondez de manière claire et précise aux questions d'interprétation dans un fichier PDF (**Attention&nbsp;: aucun autre format que PDF ne sera accepté**).

{{< applet src="/html/playground/index.html#dataset=gauss&networkShape=&showTestData_hide=true&percTrainData_hide=true&batchSize_hide=true&dataset_hide=false&activation_hide=true&problem=classification&problem_hide=true&regularization_hide=true&regularizationRate_hide=true&learningRate_hide=true&discretize_hide=true" width="150%" scale="0.9" height="651" >}}

## Instructions et questions d'interprétation

1. Des 4 jeux de données proposés, lequel vous apparaît le plus facile à
   classifier (en deux classes distinctes, `orange` et `bleue`), pour un
   algorithme d'apprentissage automatique (pas seulement un réseau de neurones)?
   Expliquez pourquoi.

2. Considérez maintenant le jeu de données avec lequel deux petits groupes de
   points sont disposés en diagonale, l'un par rapport à l'autre.

   <p style="text-align: center;">
     <img src="{{< rel "/images/module3/tn3/prob1.png" >}}" alt="Le jeu de données des deux groupes : des points orange en bas à gauche, des points bleus en haut à droite." style="width: 50%; height: auto;" width="598" height="594">
   </p>

   Assurez-vous de n'avoir aucune couche cachée, et seulement les
   caractéristiques $X_1$ et $X_2$ activées. Quelle est l'erreur (ou perte)
   d’entraînement? Appuyez plusieurs fois sur le bouton de rafraîchissement, et
   constatez les variations de cette erreur initiale (avant tout
   entraînement):

   <p style="text-align: center;">
     <img src="{{< rel "/images/module3/tn3/refresh_button.png" >}}" alt="Le bouton de réinitialisation, une flèche circulaire, à gauche du bouton de lecture." style="width: 50%; height: auto;" width="684" height="364">
   </p>

   Que signifient ces erreurs et ces variations (pourquoi l'erreur initiale est
   parfois plus haute, et parfois plus basse), et de quelle manière peut-on les
   constater visuellement?

3. Quelle est la différence entre ce problème de classification et celui que
   nous avons vu dans le deuxième module avec la [régression logistique](docs/module2/60-classer/#tracer-une-frontière-la-régression-logistique)?

4. Ajustez maintenant la valeur de "bruit" à 25, et appuyez sur le bouton
   "régénérez" à quelques reprises. Est-ce que ceci rend la tâche de
   classification plus facile ou plus difficile pour un algorithme
   d'apprentissage? Expliquez pourquoi.

5. Remettez le "bruit" à 0, et choisissez maintenant ce jeu de données :

   <p style="text-align: center;">
     <img src="{{< rel "/images/module3/tn3/prob2.png" >}}" alt="Le jeu de données du XOR : quatre groupes de points aux coins, orange en haut à gauche et en bas à droite, bleus sur l'autre diagonale." style="width: 50%; height: auto;" width="616" height="620">
   </p>

   *A priori*, est-ce qu'il vous apparaît possible qu'un modèle ayant servi à
   classifier le précédent jeu de données puisse servir à classifier celui-ci?
   Expliquez pourquoi. Tentez l'expérience, que se passe-t-il?

6. Ajoutez maintenant une couche cachée avec trois neurones, quel est l'effet
   sur l’entraînement? N'oubliez pas que la fonction d’entraînement est démarrée
   en appuyant sur ce bouton :

   <p style="text-align: center;">
     <img src="{{< rel "/images/module3/tn3/train_button.png" >}}" alt="Le bouton de lecture, rond, qui lance l'entraînement." style="width: 50%; height: auto;" width="590" height="358">
   </p>

7. Ajoutez maintenant une deuxième couche cachée avec deux neurones cette fois.
   Effectuez quelques entraînements, en n'oubliant pas d'utiliser la fonction de
   rafraîchissement entre les entraînements (pour faire en sorte que les
   paramètres initiaux puissent varier). Qu'observez-vous, et que pouvez-vous en
   conclure?

8. Une fois qu'un entraînement a atteint un certain niveau d'erreur (assez bas,
   probablement, si l’entraînement a bien fonctionné), est-ce que le fait de le
   laisser continuer pendant une longue période (et donc d'atteindre un très
   grand nombre d'époques) fait une différence? Comment expliquez-vous cela?
   Quel mot pourrait-on utiliser pour illustrer ce phénomène particulier?

9. Comment expliquez-vous le fait que l’entraînement ne converge pas toujours
   vers la même solution, et par extension, la même valeur d'erreur?

10. Enlevez maintenant toutes les couches cachées, et ne laissez activée que la
    caractéristique $X_1X_2$. En entraînant le modèle à plusieurs reprises avec
    cette configuration, qu'observez-vous, et comment l'expliquez-vous?

11. Considérez maintenant ce troisième jeu de données :

    <p style="text-align: center;">
      <img src="{{< rel "/images/module3/tn3/prob3.png" >}}" alt="Le jeu de données du cercle : des points bleus au centre, entourés d'un anneau de points orange." style="width: 50%; height: auto;" width="624" height="618">
    </p>

    Sans aucune couche cachée, et seulement les caractéristiques $X_1$ et $X_2$
    activées, est-ce qu'il est possible de résoudre ce problème?

12. Est-ce que la situation change en remplaçant les caractéristiques $X_1$ et
    $X_2$ par les caractéristiques $X_1^2$ et $X_2^2$? Comment peut-on expliquer
    cela? Indice : considérez l'équation du [cercle](https://fr.wikipedia.org/wiki/Cercle).

13. En remettant seulement les caractéristiques $X_1$ et $X_2$, est-ce qu'il est
    possible de réduire l'erreur à l'aide de couches cachées?
