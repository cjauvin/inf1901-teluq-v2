---
title: "Le matériel et les outils"
weight: 42
slug: materiel-et-outils
---

# Le matériel et les outils

Le chapitre « [L'apprentissage profond](docs/module3/40-apprentissage-profond/#pourquoi-seulement-en-2012) »
a nommé trois conditions du succès de 2012 : une meilleure fonction d'activation, des données, et du calcul. Ce chapitre revient sur la
troisième. Deux progrès techniques ont rendu l'apprentissage profond (*deep
learning*) praticable : des processeurs capables de faire les calculs, et des
bibliothèques logicielles qui écrivent la rétropropagation à la
place du programmeur.

{{< image src="/images/module3/frise-materiel-logiciel.svg" alt="Une frise chronologique à deux rangées. En haut, le matériel : fondation de Nvidia en 1993, GeForce 256 en 1999, CUDA en 2007, un réseau entraîné 70 fois plus vite sur GPU en 2009, premières machines conçues pour l'apprentissage profond en 2016. En bas, le logiciel : la méthode de Linnainmaa en 1970, Torch en 2002, Theano en 2007, Caffe en 2013, TensorFlow et Keras en 2015, PyTorch en 2016. Au centre, en 2012, AlexNet, où les deux histoires se rejoignent." title="Le matériel et le logiciel de l'apprentissage profond : deux histoires qui se rejoignent en 2012." loading="lazy" >}}

## Les processeurs graphiques

Un réseau de neurones répète toujours le même calcul : multiplier
des entrées par des poids et additionner les résultats, pour chaque
neurone, des millions de fois. Ces calculs sont indépendants les uns des autres, et
peuvent donc être faits en même temps.

Un processeur ordinaire (CPU) a quelques cœurs puissants, conçus pour exécuter des
tâches variées l'une après l'autre. Un **processeur graphique** (GPU) a des milliers de cœurs simples, qui exécutent tous le même
calcul en parallèle. Il a été conçu pour l'affichage des jeux vidéo, où il faut
calculer la couleur de millions de pixels des dizaines de fois par seconde, ce qui
est un problème du même type.

{{< image src="/images/module3/cpu-gpu.svg" alt="Deux panneaux. À gauche, un processeur ordinaire (CPU) : huit gros cœurs, de couleurs différentes, qui traitent chacun une tâche différente. À droite, un processeur graphique (GPU) : une grille de plusieurs centaines de petits cœurs identiques, qui font tous le même calcul en même temps." title="Un processeur ordinaire a quelques cœurs puissants ; un processeur graphique a des milliers de cœurs simples." loading="lazy" >}}

Voici les principales étapes de cette histoire.

- **1993.** Fondation de Nvidia, qui fabrique des cartes graphiques pour le jeu
  vidéo.
- **1999.** Nvidia lance la GeForce 256 et la présente comme le premier « GPU ».
- **Début des années 2000.** Les cartes deviennent programmables. Des chercheurs
  s'en servent pour des calculs scientifiques, en présentant leurs calculs comme
  des images à afficher. La méthode est laborieuse.
- **2007.** Nvidia publie CUDA, un outil qui permet de programmer un GPU
  directement, pour n'importe quel calcul. L'entreprise investit dans cet usage
  alors qu'il n'a presque aucun marché.
- **2009.** À Stanford, l'équipe d'Andrew Ng montre qu'un GPU entraîne un réseau de
  neurones jusqu'à 70 fois plus vite qu'un CPU.
- **2012.** [AlexNet](docs/module3/40-apprentissage-profond/#2012-le-concours-imagenet)
  est entraîné sur deux cartes de jeu vidéo vendues environ 500 \\$ chacune, dans la
  chambre d'Alex Krizhevsky, chez ses parents.
- **2016.** Nvidia vend ses premières machines conçues pour l'apprentissage
  profond. Google présente ses propres puces spécialisées, les TPU.
- **Années 2020.** Les grands modèles sont entraînés dans des centres de données
  qui contiennent des dizaines de milliers de GPU. Nvidia fournit la majorité de
  ces puces. En 2025, elle devient la première entreprise dont la valeur en bourse
  dépasse 4 000, puis 5 000 milliards de dollars. L'accès à ces puces devient un
  enjeu politique : depuis 2022, les États-Unis en limitent l'exportation vers la
  Chine. Le [Module 5](docs/module5) reviendra sur ces questions.

{{< image src="/images/module3/geforce-gtx-580.jpg" alt="Une carte graphique noire, de forme allongée, avec un ventilateur rond à droite et l'inscription GeForce GTX 580." title="Une carte GeForce GTX 580, conçue pour le jeu vidéo. AlexNet a été entraîné sur deux cartes de ce modèle (photo : TheStriker, Wikimedia Commons, CC BY-SA 4.0)." loading="lazy" >}}

## La différentiation automatique

Le second progrès est logiciel. La
[rétropropagation](docs/module3/30-entrainer-un-reseau/#la-rétropropagation)
demande de calculer des dérivées à travers toutes les couches du réseau. Pendant
longtemps, ce calcul a été fait à la main : pour chaque nouveau réseau, il fallait
établir les formules sur papier, puis les programmer. Le travail prenait des
semaines, et les erreurs étaient fréquentes et difficiles à repérer.

La **différentiation automatique** (*automatic differentiation*) supprime ce
travail. Le programmeur décrit seulement la propagation avant,
c'est-à-dire le calcul qui mène des entrées à l'erreur. La bibliothèque enregistre
chaque opération, et en déduit elle-même le calcul de la rétropropagation.

- **1970.** Le Finlandais Seppo Linnainmaa décrit la méthode mathématique générale,
  dont la rétropropagation est un cas particulier.
- **2002.** Torch, une des premières bibliothèques destinées aux réseaux de
  neurones. Elle fournit des couches toutes faites, mais les dérivées de chaque
  type de couche sont encore écrites à la main par ses auteurs.
- **2007.** Theano, développée à l'Université de Montréal dans le laboratoire de
  Yoshua Bengio. C'est la première bibliothèque largement utilisée qui réunit les
  deux progrès : elle calcule les dérivées automatiquement, et elle exécute les
  calculs sur GPU.
- **2013.** Caffe, à Berkeley, conçue pour les réseaux qui traitent des images.
  Elle se répand vite après le succès d'AlexNet.
- **2015.** Google publie TensorFlow en code ouvert (*open source*). La même année
  paraît Keras, qui permet de décrire un réseau en quelques lignes.
- **2016.** Facebook publie PyTorch. On y écrit un réseau comme un programme Python
  ordinaire. Elle devient en quelques années l'outil le plus utilisé en recherche.

## Un réseau en quelques lignes

Voici à quoi ressemble aujourd'hui le
[réseau des chiffres](docs/module3/20-une-couche-cachee/#plus-de-neurones-plus-de-formes)
du chapitre « Une couche cachée », écrit avec PyTorch. Il n'est pas nécessaire de
comprendre le détail du code. Il suffit de constater sa longueur.

```python
reseau = nn.Sequential(
    nn.Linear(784, 30),    # 784 entrées vers 30 neurones cachés
    nn.ReLU(),             # la fonction d'activation
    nn.Linear(30, 10),     # 30 neurones cachés vers 10 sorties
)

sorties = reseau(images)                     # la propagation avant
erreur = cross_entropy(sorties, etiquettes)  # l'écart avec les bonnes réponses
erreur.backward()                            # la rétropropagation, faite par la bibliothèque
optimiseur.step()                            # la correction de tous les poids
```

La ligne `erreur.backward()` remplace les semaines de calcul à la main. La
conséquence est importante pour la suite. Essayer une nouvelle forme de réseau ne
demande plus que quelques heures. Les chercheurs ont donc pu en essayer beaucoup,
et c'est ainsi que se sont répandues les architectures des chapitres suivants. La
première, présentée dans « [Voir : les réseaux convolutifs](docs/module3/50-reseaux-convolutifs) », est conçue pour les
images.
