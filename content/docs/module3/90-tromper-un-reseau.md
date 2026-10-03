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
publient l'exemple suivant. Un réseau convolutif entraîné sur ImageNet reconnaît un
panda, avec 58 % de confiance. Les chercheurs ajoutent à l'image une perturbation
très faible, calculée avec soin. À l'œil, l'image modifiée est identique à
l'originale. Le réseau y voit maintenant un gibbon, avec 99 % de confiance.

{{< image src="/images/module3/panda-gibbon.png" alt="Trois vignettes. À gauche, la photo d'un panda, que le réseau reconnaît comme un panda avec 57,7 % de confiance. Au centre, la perturbation, un bruit coloré, amplifiée pour être visible. À droite, la somme des deux, une photo identique à l'œil à la première, que le réseau classe comme un gibbon avec 99,3 % de confiance." title="L'exemple du panda : une perturbation invisible fait passer la réponse de « panda » à « gibbon » (d'après Goodfellow, Shlens et Szegedy, 2014)." loading="lazy" >}}

Une image modifiée de cette façon s'appelle un **exemple adverse** (*adversarial
example*). Le phénomène n'est pas propre à ce réseau ni à ce panda. On peut
fabriquer un exemple adverse pour presque n'importe quelle image et n'importe quel
réseau.

## Comment on le fabrique

La méthode utilise la
[rétropropagation](docs/module3/30-entrainer-un-reseau/#la-rétropropagation), mais
à l'envers.

À l'entraînement, on garde l'image fixe et on modifie les poids, dans le sens qui
réduit l'erreur. Pour tromper un réseau déjà entraîné, on garde les poids fixes et
on modifie l'image. La rétropropagation indique, pour chaque pixel, dans quel sens
le modifier pour augmenter la probabilité d'une réponse choisie, par exemple
« gibbon ». On déplace alors chaque pixel d'une quantité minuscule, toujours dans
le sens le plus utile.

Aucun pixel ne change de façon visible. Mais une image de 224 pixels sur 224 en
couleur compte environ 150 000 valeurs. Des changements minuscules, tous orientés
dans le même sens, finissent par s'additionner et faire basculer la réponse.

## Tromper un réseau à manipuler

Dans l'applet ci-dessous, un classifieur de chiffres est entraîné quand la page
s'ouvre, sur des chiffres dessinés par l'ordinateur. C'est un modèle simple, une
[régression logistique](docs/module2/60-classer/#tracer-une-frontière-la-régression-logistique)
à dix sorties, sans couche cachée, et non un réseau profond. Le principe de
l'attaque est le même.

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
aussi grand, une frontière de décision passe presque toujours tout près de chaque
image, dans une direction ou une autre. L'attaque trouve cette direction.

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
personnes interrogées faisaient confiance au classifieur. Après, presque aucune.

{{% hint info %}}
**Hans le Malin**

Au début des années 1900, à Berlin, un cheval nommé Hans semblait savoir compter.
On lui posait une addition, et il frappait du sabot le bon nombre de fois. En 1907,
le psychologue Oskar Pfungst montre que Hans ne compte pas. Il observe la personne
qui l'interroge, et s'arrête quand il perçoit chez elle une réaction involontaire,
un léger mouvement de tête, au moment où il atteint le bon nombre. Hans réussissait
vraiment, mais pour une autre raison que celle qu'on croyait. On parle aujourd'hui
d'**effet Hans le Malin** pour un modèle d'apprentissage qui réussit en s'appuyant
sur un indice imprévu, comme la neige derrière les loups.

{{< image src="/images/module3/hans-le-malin.jpg" alt="Une photographie ancienne en noir et blanc : un cheval dans une cour, entouré d'une foule d'hommes en chapeau." title="Hans le Malin et son public, à Berlin, vers 1904 (photo du domaine public, Wikimedia Commons)." loading="lazy" >}}
{{% /hint %}}
