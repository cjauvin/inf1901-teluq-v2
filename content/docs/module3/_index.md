---
title: "Module 3 - Réseaux de neurones et apprentissage profond"
weight: 300
bookCollapseSection: true
---

# Module 3 — Réseaux de neurones et apprentissage profond

{{< image src="/images/neural-network.jpg" alt="Un réseau de neurones dessiné sur fond noir. À gauche, l'image pixelisée d'un 3 manuscrit, dont chaque pixel alimente un neurone de la couche d'entrée. Des connexions bleues et rouges relient les couches successives jusqu'à dix neurones de sortie, dont celui du chiffre 3 est allumé." title="Un réseau qui reconnaît un 3 manuscrit (image tirée de la série de vidéos de 3Blue1Brown sur les réseaux de neurones)." loading="lazy" >}}

## Le retour d'une idée ancienne

Le [Module 1](docs/module1/20-deux-paris) a présenté deux paris sur la nature de
l'intelligence, nés presque en même temps dans les années 1950. Le pari symbolique
voit l'esprit comme de la logique, des symboles et des règles. Le pari
connexionniste le voit comme un cerveau, un réseau qui s'ajuste à l'expérience. Le
perceptron de Rosenblatt, en 1958, en était la première machine.

Ce second pari a connu une longue éclipse. En 1969, Minsky et Papert montrent qu'un
perceptron ne peut pas apprendre une fonction aussi simple que le
[XOR](docs/module1/60-hivers/#le-premier-hiver-la-mort-du-perceptron-1969), et la
recherche sur les réseaux de neurones s'arrête presque. Elle reprend en 1986, avec
une méthode pour entraîner des réseaux à plusieurs couches. Elle reste pourtant
secondaire jusqu'en 2012, quand un réseau profond dépasse de loin toutes les autres
méthodes de reconnaissance d'images. En quelques années, les réseaux de neurones
deviennent la méthode dominante de l'IA. Ils sont aujourd'hui au cœur de la
reconnaissance d'images et de la parole, de la traduction automatique, et des
grands modèles de langage comme ChatGPT.

Ce module raconte ce retour, et explique comment ces réseaux fonctionnent.

## Une seule grande idée : apprendre ses propres caractéristiques

Au [Module 2](docs/module2), un modèle recevait des données décrites par des
caractéristiques choisies par un humain : la superficie d'une maison, la présence
d'un mot dans un courriel. Quand un problème résistait, comme le XOR, c'était
encore à l'humain de
[fabriquer la bonne caractéristique](docs/module2/70-generaliser/#linéaire-ou-non-linéaire-ce-quun-modèle-peut-dessiner).

Un réseau de neurones fabrique lui-même ses caractéristiques. Chacune de ses
couches transforme les données en une nouvelle description, plus utile que la
précédente. Un réseau qui reconnaît des chiffres manuscrits reçoit seulement des
pixels. Il apprend seul à y repérer des traits, puis des formes, puis des chiffres.
Personne ne lui indique quoi chercher.

Pour le reste, rien ne change. Un réseau s'entraîne avec le même schéma qu'au
Module 2 : des données, un modèle réglable, une erreur à réduire, et la
[descente de gradient](docs/module2/50-entrainer-un-modele/#apprendre-cest-descendre-la-pente)
pour la réduire. La différence est l'échelle. Une droite avait deux paramètres. Un
réseau en a des milliers, des millions, et parfois des centaines de milliards.

## Un fil conducteur : les chiffres manuscrits

Un même exemple revient tout au long du module : reconnaître un chiffre écrit à la
main, sur une image de 28 pixels sur 28. On le retrouve dans le premier neurone,
dans le réseau à une couche cachée, dans les réseaux convolutifs de Yann Le Cun,
qui lisaient les chèques dans les années 1990, et dans les exemples adverses qui
trompent un réseau.

{{< image src="/images/module3/reseau-chiffres.svg" alt="De gauche à droite : une image de 28 pixels sur 28 qui montre un zéro ; une couche d'entrée de 784 valeurs, une par pixel ; une couche cachée de 30 neurones ; une couche de sortie de dix neurones, numérotés de 0 à 9. Chaque sortie donne un nombre entre 0 et 1. La sortie du chiffre 0 est la plus élevée, 0,96 : c'est la réponse du réseau." title="Le réseau des chiffres, qui sert d'exemple tout au long du module." loading="lazy" >}}

## Ce que ce module n'est pas

Trois précisions évitent des malentendus fréquents.

- **Un réseau de neurones n'est pas un cerveau.** Il s'en inspire, mais un neurone
  artificiel est une formule simple. Le module y revient deux fois, dans les pages
  [*Un neurone*](docs/module3/10-un-neurone/#doù-vient-le-mot-neurone) et
  [*L'apprentissage profond*](docs/module3/40-apprentissage-profond/#une-hiérarchie-de-caractéristiques).
- **Les réseaux de ce module reconnaissent et prédisent.** Ils associent une
  réponse à une entrée : quel chiffre, quel mot traduit, quel coup jouer. La
  génération de textes et d'images est le sujet du [Module 4](docs/module4), qui
  s'appuie sur les architectures présentées ici, en particulier le Transformer.
- **Aucune formule n'est nécessaire.** Les mécanismes sont expliqués par des
  figures et des applets. Les calculs, pour qui veut les voir, sont dans des blocs
  dépliables « Pour aller plus loin ».

## Le parcours du module

Comme au Module 2, chaque page rencontre une limite qui mène à la suivante.

1. [*Un neurone*](docs/module3/10-un-neurone) : le retour du perceptron. Un neurone
   est une régression logistique, et il ne trace qu'une droite.
2. [*Une couche cachée*](docs/module3/20-une-couche-cachee) : quelques neurones
   reliés résolvent le XOR, en fabriquant eux-mêmes la bonne caractéristique.
3. [*Entraîner un réseau*](docs/module3/30-entrainer-un-reseau) : la
   rétropropagation, et la question de 1969 réglée en 1986.
4. [*L'apprentissage profond*](docs/module3/40-apprentissage-profond) : pourquoi
   empiler les couches, et pourquoi cela n'a fonctionné qu'à partir de 2012.
5. [*Le matériel et les outils*](docs/module3/42-materiel-et-outils) : l'histoire
   des processeurs graphiques et de la différentiation automatique.
6. [*Voir : les réseaux convolutifs*](docs/module3/50-reseaux-convolutifs) : le
   filtre qui glisse sur l'image, Yann Le Cun et les chèques.
7. [*Lire une séquence : les réseaux récurrents*](docs/module3/60-reseaux-recurrents) :
   un réseau avec une mémoire, le LSTM, la traduction.
8. [*L'attention et le Transformer*](docs/module3/70-attention-transformer) :
   regarder toute la séquence à la fois, l'architecture des grands modèles
   actuels.
9. [*Apprendre à jouer : le renforcement profond*](docs/module3/80-renforcement-profond) :
   Atari, AlphaGo, AlphaZero.
10. [*Tromper un réseau*](docs/module3/90-tromper-un-reseau) : les exemples
    adverses, et la boîte noire.

Le module compte huit applets, dont un neurone à régler, un réseau qui apprend le
XOR sous vos yeux, un filtre de convolution, une machine qui apprend le morpion en
jouant contre elle-même, et un classifieur à tromper.

Pour situer ce module dans l'ensemble du cours : les réseaux de neurones sont une
famille de méthodes d'apprentissage automatique, devenue la plus importante depuis
2012, et sur laquelle reposent l'IA générative et les grands modèles de langage du
Module 4.

{{< image src="/images/module3/ai-venn.svg" alt="Carte en régions imbriquées de l'intelligence artificielle. À l'intérieur de « Intelligence artificielle (IA) » : d'un côté « IA classique » ; de l'autre « Apprentissage automatique (AA) » (machine learning), qui contient « Méthodes d'AA diverses » et « Réseaux de neurones / apprentissage profond », lesquels contiennent à leur tour « IA générative » et « ChatGPT ». Un repère « Module 3 » pointe vers les « Réseaux de neurones » et l'« Apprentissage profond », qui sont le sujet du module." title="La carte de l'IA : le Module 3 porte sur les réseaux de neurones et l'apprentissage profond." loading="lazy" >}}

## Objectifs

Au terme de ce module, vous devriez être en mesure de :

* expliquer ce qu'est un neurone artificiel, et pourquoi un neurone seul ne trace
  qu'une frontière droite ;
* expliquer comment une couche cachée permet de résoudre le XOR, en fabriquant de
  nouvelles caractéristiques ;
* décrire le principe de la rétropropagation, et le distinguer de l'inférence ;
* expliquer ce qu'apporte la profondeur, et les trois conditions du succès de
  2012 : les données, le calcul et de meilleures méthodes d'entraînement ;
* décrire l'idée principale des réseaux convolutifs, des réseaux récurrents et du
  Transformer, et le type de données auquel chacun est adapté ;
* expliquer comment le renforcement profond combine la recherche du Module 1 et
  l'apprentissage ;
* expliquer ce qu'est un exemple adverse, et pourquoi un réseau profond est une
  boîte noire ;
* situer ces développements dans l'histoire du connexionnisme, de 1958 à
  aujourd'hui.

## Durée

Quatre semaines, soit environ 36 heures.

## Évaluation

Un [travail noté](docs/module3/99-travail-noté-3) (20 % de la note finale) où vous
manipulerez des réseaux de neurones dans une application interactive, TensorFlow
Playground, avec des questions d'interprétation.
