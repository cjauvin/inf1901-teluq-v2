---
title: "Tromper un réseau"
weight: 90
slug: tromper-un-reseau
---

# Tromper un réseau

Les chapitres précédents ont montré des réseaux qui reconnaissent des images,
traduisent des phrases et battent les meilleurs joueurs de go. Ce dernier chapitre
montre une faiblesse surprenante de ces systèmes : une modification invisible pour
nous peut leur faire dire n'importe quoi. Il explique comment c'est possible, et ce
que cela révèle de leur fonctionnement.

## Le panda devenu gibbon

En 2014, Ian Goodfellow, Jonathon Shlens et Christian Szegedy, chez Google,
publient l'exemple suivant. Un réseau convolutif (*convolutional neural network*,
CNN) entraîné sur ImageNet reconnaît un panda, avec 58 % de confiance. Les
chercheurs ajoutent à l'image une perturbation très faible, calculée avec soin. À
l'œil, l'image modifiée est identique à l'originale. Le réseau y voit maintenant un
gibbon, avec 99 % de confiance.

{{< image src="/images/module3/panda-gibbon.png" alt="Trois vignettes. À gauche, la photo d'un panda, que le réseau reconnaît comme un panda avec 57,7 % de confiance. Au centre, la perturbation, un bruit coloré, amplifiée pour être visible. À droite, la somme des deux, une photo identique à l'œil à la première, que le réseau classe comme un gibbon avec 99,3 % de confiance." title="L'exemple du panda : une perturbation invisible fait passer la réponse de « panda » à « gibbon » (d'après Goodfellow, Shlens et Szegedy, 2014)." loading="lazy" >}}

Une image modifiée de cette façon s'appelle un **exemple adverse** (*adversarial
example*). Le phénomène n'est pas propre à ce réseau ni à ce panda. On peut
fabriquer un exemple adverse pour presque n'importe quelle image et n'importe quel
réseau.

## Comment on le fabrique

La méthode utilise la
[rétropropagation](docs/module3/30-entrainer-un-reseau/#la-rétropropagation), mais à l'envers.

À l'entraînement, on garde l'image fixe et on modifie les poids, dans le
sens qui réduit l'erreur. Pour tromper un réseau déjà entraîné, on garde les poids
fixes et on modifie l'image. La rétropropagation indique, pour chaque pixel, dans
quel sens le modifier pour augmenter la probabilité d'une réponse choisie, par
exemple « gibbon ». On déplace alors chaque pixel d'une quantité minuscule, toujours
dans le sens le plus utile.

Aucun pixel ne change de façon visible. Mais une image de 224 pixels sur 224 en
couleur compte environ 150 000 valeurs. Des changements minuscules, tous orientés
dans le même sens, finissent par s'additionner et faire basculer la réponse.

## Tromper un réseau à manipuler

Dans l'applet ci-dessous, un classifieur de chiffres est entraîné quand la page
s'ouvre, sur des chiffres dessinés par l'ordinateur. C'est un modèle simple, une
[régression logistique](docs/module2/60-classer/#tracer-une-frontière-la-régression-logistique) à dix sorties, sans couche cachée, et non
un réseau profond. Le principe de l'attaque est le même.

{{< applet src="/html/applets/adverse.html" height="444" >}}

1. La force est à zéro, et le classifieur reconnaît le 3. Augmentez lentement la
   force. Observez la perturbation, et le moment où la réponse bascule vers 8.
2. Regardez l'image modifiée au moment où la réponse bascule. Le 3 reste
   parfaitement lisible pour nous.
3. Essayez d'autres paires de chiffres. Certaines demandent une force beaucoup plus
   grande que d'autres. Par exemple, faire dire 1 à un 6 est difficile.

## Pourquoi c'est possible

Plusieurs explications se complètent.

**La dimension.** Une image est un point dans un espace qui compte autant de
dimensions que de valeurs de pixels, des centaines de milliers. Dans un espace
aussi grand, une frontière de décision (*decision boundary*) passe presque toujours
tout près de chaque image, dans une direction ou une autre. L'attaque trouve cette
direction.

**Le réseau ne voit pas comme nous.** Il utilise tous les indices qui l'aident à
réduire son erreur d'entraînement, y compris des indices que nous ne remarquons pas
ou que nous jugerions sans importance. En 2019, Robert Geirhos et ses collègues
montrent que les réseaux entraînés sur ImageNet se fient surtout à la **texture**
des objets, alors que nous nous fions surtout à leur forme. Une silhouette de chat
couverte d'une texture de peau d'éléphant est classée « éléphant ».

{{< image src="/images/module3/texture-chat-elephant.png" alt="Trois images, avec sous chacune les trois réponses les plus probables d'un réseau convolutif, en anglais. À gauche, une texture de peau d'éléphant : « Indian elephant » à 81,4 %. Au centre, la photo d'un chat roux : « tabby cat » à 71,1 %. À droite, la silhouette du même chat couverte de la texture de peau d'éléphant : « Indian elephant » à 63,9 %." title="Une texture, un chat, et un chat à texture d'éléphant : le réseau suit la texture plutôt que la forme (Geirhos et collègues, 2019)." loading="lazy" >}}

**Le réseau peut réussir pour de mauvaises raisons.** En 2016, Marco Ribeiro,
Sameer Singh et Carlos Guestrin présentent une méthode pour expliquer les réponses
d'un classifieur. Pour la tester, ils entraînent volontairement un classifieur
biaisé, qui distingue les loups des huskies : dans ses photos d'entraînement, les
loups sont presque toujours sur de la neige. Le classifieur atteint une bonne
précision, et leur méthode révèle qu'il regarde surtout l'arrière-plan. Il est
devenu un détecteur de neige. Avant de voir cette explication, une partie des
personnes interrogées faisaient confiance au classifieur. Après, presque aucune. La neige est **corrélée** aux loups dans ces photos, mais
elle n'en est pas la cause, une distinction présentée au Module 2 dans
« [Corrélation n'est pas causalité](docs/module2/75-bien-evaluer/#corrélation-nest-pas-causalité) ».

{{% hint info %}}
**Hans le Malin**

Au début des années 1900, à Berlin, un cheval nommé Hans semblait savoir compter.
On lui posait une addition, et il frappait du sabot le bon nombre de fois. En 1907,
le psychologue Oskar Pfungst montre que Hans ne compte pas. Il observe la personne
qui l'interroge, et s'arrête quand il perçoit chez elle une réaction involontaire,
un léger mouvement de tête, au moment où il atteint le bon nombre. Hans réussissait
vraiment, mais pour une autre raison que celle qu'on croyait. On parle aujourd'hui
d'**effet Hans le Malin** (*Clever Hans effect*) pour un modèle d'apprentissage qui
réussit en s'appuyant sur un indice imprévu, comme la neige derrière les loups.

{{< image src="/images/module3/hans-le-malin.jpg" alt="Une photographie ancienne en noir et blanc : un cheval dans une cour, entouré d'une foule d'hommes en chapeau." title="Hans le Malin et son public, à Berlin, vers 1904 (photo du domaine public, Wikimedia Commons)." loading="lazy" >}}
{{% /hint %}}

## Dans le monde réel

Un exemple adverse sur une image numérique demande de modifier chaque pixel, ce qui
suppose un accès direct à l'image. Les chercheurs ont montré que les attaques
fonctionnent aussi dans le monde physique.

- **Le panneau d'arrêt.** En 2018, une équipe universitaire colle quelques bandes
  noires et blanches sur un vrai panneau d'arrêt. Pour un humain, ce sont des
  autocollants sans importance. Le réseau qui lit les panneaux, photographiés sous
  différents angles et à différentes distances, y voit le plus souvent une limite
  de vitesse.
- **La tortue.** En 2017, une équipe du MIT imprime en 3D une tortue dont la
  texture a été calculée pour tromper un réseau. Sous presque tous les angles, le
  réseau y voit un fusil.
- **Les lunettes.** En 2016, des chercheurs montrent qu'une monture de lunettes
  imprimée avec un motif particulier peut empêcher un système de reconnaissance
  faciale (*facial recognition*) de reconnaître une personne, ou lui faire croire
  qu'il s'agit de quelqu'un d'autre.
- **La voix.** Des commandes vocales peuvent être cachées dans un enregistrement de
  musique ou de parole, sans qu'un humain les remarque, et être comprises par un
  assistant vocal.

{{< image src="/images/module3/tortue-adverse.jpg" alt="Deux photographies d'une tortue de mer imprimée en 3D, aux couleurs vives, l'une vue de dessous, l'autre posée sur de l'herbe." title="La tortue imprimée en 3D, qu'un réseau prend pour un fusil sous presque tous les angles (photo : LabSix, MIT, 2017)." loading="lazy" >}}

{{< image src="/images/module3/stop-adverse.png" alt="Deux photos du même panneau d'arrêt. À gauche, le panneau intact : un humain et la machine le reconnaissent. À droite, le même panneau avec quelques bandes noires et blanches collées dessus : l'humain le reconnaît toujours, la machine ne lui accorde plus que 0,9 % de chances d'être un panneau d'arrêt." title="Illustration de l'attaque du panneau d'arrêt : quelques autocollants suffisent à tromper la machine, pas l'humain." loading="lazy" >}}

## Se défendre

La défense la plus utilisée s'appelle l'**entraînement adverse** (*adversarial
training*). On fabrique des exemples adverses pendant l'entraînement, et on les
ajoute aux données avec leur bonne réponse. Le réseau apprend à ne plus se laisser
tromper par ces perturbations. Il devient plus robuste, mais il reste vulnérable à
des attaques plus fortes ou d'un autre type, et sa précision sur les images normales
baisse souvent un peu.

Depuis 2014, de nombreuses autres défenses ont été proposées. La plupart ont été
contournées, parfois quelques mois après leur publication. C'est une course entre
attaques et défenses, sans solution complète à ce jour.

Le problème ne se limite pas aux images. Les grands modèles de langage ont leurs propres attaques : des formulations conçues pour
leur faire ignorer leurs consignes, ou des instructions cachées dans un document
qu'on leur demande de lire. Le [Module 4](docs/module4/80-outils-et-agents/#des-agents) y reviendra.

## Une boîte noire

Les exemples adverses et l'effet Hans le Malin ont une cause commune. On ne sait
pas exactement ce qu'un réseau a appris.

Le contraste avec les systèmes des modules précédents est net. On pouvait lire les
règles d'un
[système expert](docs/module1/50-systemes-experts/#lanatomie-dun-système-expert)
du Module 1 et suivre son raisonnement. On pouvait lire les questions d'un
[arbre de décision](docs/module2/65-arbres-de-decision/#ce-quun-arbre-dit-et-ce-quil-tait) du Module 2. Un réseau profond compte des millions de poids, et
aucun d'eux n'a de signification isolée. Il donne une réponse, souvent très bonne,
sans donner ses raisons. On dit que c'est une **boîte noire** (*black box*).

L'**IA explicable** (*explainable AI*, XAI) cherche à retrouver ces raisons. Une de
ses méthodes produit une **carte de saillance** (*saliency map*) : pour une image
donnée, elle indique quels pixels ont le plus pesé sur la réponse. C'est ainsi que
l'on découvre qu'un classifieur de loups regarde la neige, ou qu'un classifieur de
radiographies s'appuie sur une marque propre à l'hôpital qui a pris l'image plutôt
que sur les poumons du patient.

{{< image src="/images/module3/saillance-7.svg" alt="Deux grilles de 28 pixels sur 28. À gauche, l'image d'un 7. À droite, sa carte de saillance : en vert, les pixels qui ont poussé le classifieur vers la réponse « 7 », surtout les extrémités de la barre horizontale et le haut du trait vertical ; en rouge, ceux qui l'ont poussé vers « 2 », sa deuxième réponse, surtout le bas du trait." title="La carte de saillance d'un 7, calculée sur le classifieur de l'applet : en vert ce qui plaide pour « 7 », en rouge ce qui plaide pour « 2 »." loading="lazy" >}}

Ces méthodes donnent des indices, pas une explication complète. La question de
savoir ce qu'un réseau a vraiment appris reste en grande partie ouverte. Le
[Module 5](docs/module5) reviendra sur ses conséquences : peut-on confier une
décision importante, un diagnostic ou un prêt bancaire, à un système qui ne peut
pas expliquer sa réponse ?

## Ce que ce module a montré

Ce module est parti d'un neurone, qui n'est qu'une
[régression logistique](docs/module3/10-un-neurone/#un-neurone-est-une-régression-logistique).
En reliant des neurones en couches, on obtient un réseau qui fabrique ses propres
caractéristiques, et qui résout le XOR, le problème qui avait arrêté le
perceptron en 1969. La rétropropagation permet d'entraîner ces réseaux. Avec des
données et du calcul en quantité suffisante, des réseaux profonds de formes adaptées
ont dépassé toutes les autres méthodes pour les images, les séquences et les jeux.

Ce module a aussi montré leurs limites. Ces réseaux ne voient pas, ne lisent pas
et ne jouent pas comme nous. Ils peuvent être trompés par des perturbations
invisibles, réussir pour de mauvaises raisons, et ils n'expliquent pas leurs
réponses.

Tous les réseaux de ce module **reconnaissent** et **prédisent** : ils associent
une réponse à une entrée. Le [Module 4](docs/module4) montre comment les mêmes
architectures, et en particulier le Transformer, apprennent à **produire** des
textes, des images et des sons.
