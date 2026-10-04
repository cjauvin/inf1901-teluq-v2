---
title: "Travail noté 3"
weight: 99
# bookToc: false
slug: travail-noté-3
---

# Apprivoiser un réseau de neurones (travail noté 3)

Ce travail utilise [TensorFlow Playground](https://playground.tensorflow.org), une
application en [logiciel libre](https://github.com/tensorflow/playground) que nous
avons adaptée pour ce cours. Elle entraîne sous vos yeux un petit réseau de
neurones à classer des points de deux couleurs, et montre à chaque instant la
frontière qu'il trace.

{{% hint info %}}
**Lire l'application**

- **À gauche**, le jeu de données. Chaque point est orange ou bleu. Le curseur
  « Bruit » mélange les deux groupes.
- **Au centre**, les **caractéristiques** (*features*) données au réseau. X₁ et X₂
  sont les deux coordonnées d'un point, et les autres (X₁², X₁X₂…) sont calculées
  à partir d'elles. À leur droite, les **couches cachées** (*hidden layers*), qu'on
  ajoute ou retire avec les boutons + et −.
- **À droite**, la réponse du réseau : la couleur du fond montre la classe qu'il
  prédit en chaque point. La **perte** (*loss*) est l'erreur du réseau, au sens de
  la [fonction d'erreur](docs/module2/50-entrainer-un-modele/#mesurer-lerreur) du
  Module 2. Plus elle est basse, mieux le réseau classe les points.
- **En haut**, le bouton de lecture lance l'entraînement. Le bouton de
  réinitialisation, la flèche circulaire, tire de nouveaux poids de départ au
  hasard. Le compteur indique le nombre d'**époques** (*epochs*), au sens de
  « [Entraîner un réseau](docs/module3/30-entrainer-un-reseau/#lentraînement-en-pratique) ».

Si l'application est coupée sur votre écran, ouvrez-la
[en pleine page]({{< rel "/html/playground/index.html#dataset=gauss&networkShape=&showTestData_hide=true&percTrainData_hide=true&batchSize_hide=true&dataset_hide=false&activation_hide=true&problem=classification&problem_hide=true&regularization_hide=true&regularizationRate_hide=true&learningRate_hide=true&discretize_hide=true" >}}).
{{% /hint %}}

## Consignes

1. Faites les expériences proposées dans les questions ci-dessous, avec
   l'application.
2. Répondez aux questions dans un fichier PDF (**aucun autre format ne sera
   accepté**). Les réponses doivent être claires et précises.

{{< applet src="/html/playground/index.html#dataset=gauss&networkShape=&showTestData_hide=true&percTrainData_hide=true&batchSize_hide=true&dataset_hide=false&activation_hide=true&problem=classification&problem_hide=true&regularization_hide=true&regularizationRate_hide=true&learningRate_hide=true&discretize_hide=true" width="150%" scale="0.9" height="651" >}}

## Questions

### Un problème facile

1. Parmi les quatre jeux de données proposés, lequel vous semble le plus facile à
   classer, en séparant les points orange des points bleus, pour un algorithme
   d'apprentissage automatique en général, et pas seulement pour un réseau de
   neurones ? Expliquez pourquoi.

2. Choisissez le jeu des deux groupes de points disposés en diagonale.

   <p style="text-align: center;">
     <img src="{{< rel "/images/module3/tn3/prob1.png" >}}" alt="Le jeu de données des deux groupes : des points orange en bas à gauche, des points bleus en haut à droite." style="width: 50%; height: auto;" width="598" height="594">
   </p>

   Vérifiez qu'il n'y a aucune couche cachée et que seules les caractéristiques
   X₁ et X₂ sont activées. Quelle est la perte d'entraînement ? Appuyez plusieurs
   fois sur le bouton de réinitialisation et observez comment varie cette perte
   initiale, avant tout entraînement.

   <p style="text-align: center;">
     <img src="{{< rel "/images/module3/tn3/refresh_button.png" >}}" alt="Le bouton de réinitialisation, une flèche circulaire, à gauche du bouton de lecture." style="width: 50%; height: auto;" width="684" height="364">
   </p>

   Que signifient ces variations ? Pourquoi la perte initiale est-elle parfois
   haute et parfois basse, et comment le voit-on sur le graphique ? (Voir
   « [Un réseau qui apprend le XOR](docs/module3/30-entrainer-un-reseau/#un-réseau-qui-apprend-le-xor) ».)

3. Sans couche cachée, ce réseau ne contient qu'un seul neurone de sortie. Lancez
   l'entraînement avec ce bouton :

   <p style="text-align: center;">
     <img src="{{< rel "/images/module3/tn3/train_button.png" >}}" alt="Le bouton de lecture, rond, qui lance l'entraînement." style="width: 50%; height: auto;" width="590" height="358">
   </p>

   Quel modèle du Module 2 retrouve-t-on ainsi, et pourquoi ? (Voir
   « [Un neurone est une régression logistique](docs/module3/10-un-neurone/#un-neurone-est-une-régression-logistique) ».)

4. Réglez le bruit à 25, puis appuyez plusieurs fois sur « Régénérer ». Ce
   changement rend-il la classification plus facile ou plus difficile pour un
   algorithme d'apprentissage ? Expliquez pourquoi.

### Le XOR

5. Remettez le bruit à 0 et choisissez le jeu du XOR, avec quatre groupes de
   points aux coins.

   <p style="text-align: center;">
     <img src="{{< rel "/images/module3/tn3/prob2.png" >}}" alt="Le jeu de données du XOR : quatre groupes de points aux coins, orange en haut à gauche et en bas à droite, bleus sur l'autre diagonale." style="width: 50%; height: auto;" width="616" height="620">
   </p>

   *A priori*, le réseau de la question précédente, sans couche cachée, peut-il
   classer ces points ? Expliquez pourquoi, puis faites l'essai. Que se passe-t-il ?
   (Voir le
   [XOR au Module 1](docs/module1/60-hivers/#le-premier-hiver-la-mort-du-perceptron-1969)
   et « [Linéaire ou non-linéaire](docs/module2/70-generaliser/#linéaire-ou-non-linéaire-ce-quun-modèle-peut-dessiner) »
   au Module 2.)

6. Ajoutez une couche cachée de trois neurones, puis lancez l'entraînement. Quel
   est l'effet ? Comment l'expliquer ? (Voir
   « [Une couche cachée](docs/module3/20-une-couche-cachee/#ce-que-fait-la-couche-cachée-changer-de-point-de-vue) ».)

7. Recommencez l'entraînement plusieurs fois, en appuyant sur le bouton de
   réinitialisation entre deux essais. Le réseau arrive-t-il toujours à la même
   frontière et à la même perte ? Comment l'expliquer ? (Voir
   « [Un réseau qui apprend le XOR](docs/module3/30-entrainer-un-reseau/#un-réseau-qui-apprend-le-xor) ».)

8. Ajoutez une deuxième couche cachée de deux neurones, et faites quelques
   entraînements. Qu'observez-vous par rapport à la question précédente ?

9. Retirez toutes les couches cachées, et n'activez que la caractéristique X₁X₂.
   Entraînez le modèle plusieurs fois. Qu'observez-vous, et comment l'expliquer ?
   Comparez avec la question 6 : dans chaque cas, qui a construit la
   caractéristique qui rend le problème séparable ? (Voir
   « [Linéaire ou non-linéaire](docs/module2/70-generaliser/#linéaire-ou-non-linéaire-ce-quun-modèle-peut-dessiner) ».)

### Le cercle

10. Choisissez le jeu du cercle, avec un groupe de points au centre entouré d'un
    anneau.

    <p style="text-align: center;">
      <img src="{{< rel "/images/module3/tn3/prob3.png" >}}" alt="Le jeu de données du cercle : des points bleus au centre, entourés d'un anneau de points orange." style="width: 50%; height: auto;" width="624" height="618">
    </p>

    Sans couche cachée, et avec seulement X₁ et X₂, est-il possible de résoudre ce
    problème ? Pourquoi ?

11. Remplacez X₁ et X₂ par X₁² et X₂². La situation change-t-elle ? Comment
    l'expliquer ? Indice : pensez à l'équation d'un
    [cercle](https://fr.wikipedia.org/wiki/Cercle). Quel lien faites-vous avec
    l'[astuce du noyau](docs/module2/70-generaliser/#ajouter-des-dimensions-sans-les-calculer-lastuce-du-noyau)
    du Module 2 ? Si la perte reste élevée, réinitialisez et relancez : il arrive
    que l'entraînement parte dans une mauvaise direction.

12. Revenez à X₁ et X₂ seulement. Peut-on réduire la perte en ajoutant des couches
    cachées ? Comparez avec la question précédente.

### Entraîner trop longtemps

L'application ci-dessous est réglée autrement. Le jeu des deux groupes est très
bruité, seuls 20 % des points servent à l'entraînement, et le réseau compte trois
couches cachées de huit neurones. Les autres points forment le **jeu de test**
(*test set*). Ils sont affichés avec un contour, et leur perte, la « perte de
test », est indiquée au-dessus de la perte d'entraînement. Ne modifiez pas le
ratio des données d'entraînement.

{{< applet src="/html/playground/index.html#dataset=gauss&noise=45&networkShape=8,8,8&percTrainData=20&showTestData=true&batchSize_hide=true&activation_hide=true&problem=classification&problem_hide=true&regularization_hide=true&regularizationRate_hide=true&learningRate_hide=true&discretize_hide=true" width="150%" scale="0.9" height="651" >}}

13. Lancez l'entraînement et laissez-le tourner longtemps, plusieurs milliers
    d'époques. Observez les deux pertes et la frontière. Que se passe-t-il ? Quel
    nom donne-t-on à ce phénomène ? Comment pourrait-on l'éviter ? (Voir
    « [Généraliser](docs/module2/70-generaliser/#trop-coller-ou-trop-lisser-le-compromis-biais-variance) »
    et « [L'entraînement en pratique](docs/module3/30-entrainer-un-reseau/#lentraînement-en-pratique) ».)
