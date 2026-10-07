---
title: "Relier les mots et les images"
weight: 90
slug: mots-et-images
---

# Relier les mots et les images

Le chapitre « [Des images, des voix, des vidéos](docs/module4/30-images-voix-videos/#les-images) »
a montré des générateurs qui produisent une image à partir d'une phrase, comme « un
panneau d'arrêt vole dans un ciel bleu ». Pour y parvenir, un modèle doit relier deux
mondes : celui des mots et celui des pixels. Ce chapitre présente la méthode qui l'a
rendu possible, l'**apprentissage contrastif**, et le modèle qui l'a popularisée,
CLIP. Il montre ensuite comment ce lien sert à chercher des images, à les classer
sans exemples, et à les générer à partir d'un texte.

## Apprendre à voir sans étiquettes

Les réseaux convolutifs du Module 3 apprenaient à voir à partir de millions d'images
étiquetées à la main, comme celles d'[ImageNet](docs/module3/40-apprentissage-profond/#2012-le-concours-imagenet).
Cet étiquetage est long et coûteux. Peut-on apprendre de bonnes caractéristiques
visuelles sans aucune étiquette ?

En 2020, Ting Chen, Geoffrey Hinton et leurs collègues, chez Google, proposent une
méthode simple, SimCLR. On prend une photo, et on en fabrique deux versions
modifiées : recadrée, retournée, aux couleurs altérées. On demande au réseau de
donner à ces deux versions des vecteurs proches, puisqu'elles montrent la même chose,
et des vecteurs éloignés à toutes les autres photos du lot. C'est un cas
d'[auto-supervision](docs/module2/80-trois-facons-d-apprendre/#fabriquer-soi-même-ses-réponses-lauto-supervision) :
les réponses sont fabriquées à partir des données elles-mêmes. On parle
d'**apprentissage contrastif** (*contrastive learning*), parce que le réseau apprend
en opposant des paires semblables et des paires différentes. Les caractéristiques
apprises de cette façon se révèlent presque aussi bonnes que celles d'un réseau
entraîné sur des images étiquetées.

## CLIP : images et légendes dans un même espace

En janvier 2021, OpenAI présente CLIP (*Contrastive Language-Image Pre-training*), qui
applique la même idée à des paires formées d'une image et de sa légende. Le Web en
contient des milliards : les photos y sont souvent accompagnées d'un texte qui les
décrit. OpenAI en rassemble 400 millions.

CLIP comprend deux réseaux. Un **encodeur d'images** transforme une image en vecteur,
et un **encodeur de textes** transforme une légende en vecteur de même taille. On les
entraîne ensemble, par lots de milliers de paires. Dans chaque lot, le vecteur de
chaque image doit être proche de celui de sa propre légende, et éloigné de ceux de
toutes les autres légendes du lot.
C'est un nouvel exemple du [jeu de construction](docs/module3/42-materiel-et-outils/#un-jeu-de-construction) du Module 3 : deux
réseaux d'architectures différentes, un réseau pour les images et un Transformer pour
les textes, entraînés ensemble.

{{< image src="/images/module4/apprentissage-contrastif.svg" alt="Un schéma. Quatre images, à gauche, passent par un encodeur d'images ; quatre légendes, en haut, passent par un encodeur de textes. Chaque image et chaque légende devient un vecteur. Une grille de quatre sur quatre compare chaque image à chaque légende. Les quatre cases de la diagonale, qui associent chaque image à sa propre légende, sont marquées « rapprocher » ; les douze autres cases sont marquées « éloigner »." title="L'apprentissage contrastif de CLIP : dans chaque lot, chaque image doit ressembler à sa propre légende plus qu'à toutes les autres." loading="lazy" >}}

Après l'entraînement, images et textes vivent dans un même espace. Une photo de chat
et la phrase « une photo d'un chat » y reçoivent des vecteurs proches. On retrouve
l'idée des [plongements](docs/module4/45-des-mots-aux-nombres/#tout-devient-vecteur)
du chapitre sur les mots, étendue à deux types de données à la fois.

L'applet ci-dessous utilise le vrai modèle CLIP. Il a placé douze images et vingt
légendes dans son espace, et l'applet affiche la ressemblance entre chaque image et
chaque légende.

{{< applet src="/html/applets/clip.html" height="660" >}}

Quelques manipulations à faire :

1. Dans l'onglet « Chercher une image par une phrase », choisissez des légendes
   précises, puis des légendes générales comme « un animal » ou « un instrument de
   musique ». CLIP trouve la bonne image même quand la légende ne la décrit
   qu'indirectement.
2. Choisissez « le drapeau du Canada ». Aucune image ne montre le drapeau, mais la
   feuille d'érable rouge arrive en tête, parce que les deux apparaissent souvent
   ensemble dans les textes et les images du Web.
3. Dans l'onglet « Décrire une image », choisissez la Joconde, puis le tableau de
   science-fiction. Les légendes sont classées comme le ferait un classificateur.
4. Dans l'onglet « La matrice », observez la diagonale : chaque image ressemble
   d'abord à sa propre légende, comme dans la figure précédente.

## Classer sans exemples

CLIP permet de classer des images dans des catégories qu'il n'a jamais apprises comme
telles. Pour savoir si une image montre un chat, un chien ou un avion, on écrit les
phrases « une photo d'un chat », « une photo d'un chien » et « une photo d'un
avion », et on choisit celle dont le vecteur est le plus proche de celui de l'image.
Aucun exemple étiqueté n'est nécessaire. On parle de classification **sans exemple**
(*zero-shot*), comme pour l'[apprentissage en contexte](docs/module4/60-passer-a-l-echelle/#apprendre-dans-le-contexte)
des modèles de langage.

Sur ImageNet, CLIP atteint ainsi environ 76 % de bonnes réponses, autant qu'un réseau
convolutif classique entraîné sur 1,28 million d'images étiquetées de ce même
concours. Surtout, il résiste mieux aux changements de distribution présentés au
chapitre « [Bien évaluer un modèle](docs/module2/75-bien-evaluer/#jamais-vu-mais-du-même-monde-la-question-de-la-distribution) »
du Module 2 : il reconnaît une banane aussi bien sur une photo que sur un croquis ou
une peinture, alors qu'un réseau entraîné sur les seules photos d'ImageNet échoue
souvent sur les dessins.

## Du texte à l'image

Le lien entre texte et image permet aussi de guider la génération. Le chapitre
« [Quatre façons de générer](docs/module4/20-quatre-facons-de-generer/#générer-sur-demande) »
présentait la génération **conditionnelle** : on donne au générateur, en plus du
hasard, une information sur ce qu'on veut obtenir. Pour un générateur d'images à
partir de texte, cette information est le vecteur de la phrase, calculé par un
encodeur de textes comme celui de CLIP.

**DALL·E 2** (2022) transforme d'abord le vecteur de la phrase en un vecteur d'image
de l'espace de CLIP, puis un modèle de diffusion produit une image qui correspond à
ce vecteur.

Le fonctionnement de **Stable Diffusion** (2022) est le mieux connu, parce que son
code et ses poids sont publics. Il assemble trois réseaux, en quatre étapes.

1. **Lire la phrase.** L'encodeur de textes de CLIP transforme la consigne, par
   exemple « un chat astronaute sur la lune », en une suite de vecteurs, un par
   [jeton](docs/module4/45-des-mots-aux-nombres/#découper-le-texte-les-jetons).
2. **Partir du bruit, dans un espace latent.** Le modèle ne travaille pas
   directement sur les pixels. Une image en couleurs de 512 × 512 pixels compte
   786 432 nombres. Stable Diffusion travaille plutôt sur sa version compressée par
   un [autoencodeur](docs/module4/20-quatre-facons-de-generer/#remplir-lespace-latent-les-autoencodeurs-variationnels),
   une grille de 64 × 64 × 4 = 16 384 nombres, 48 fois moins. Au départ, cette
   grille est remplie de bruit tiré au hasard.
3. **Retirer le bruit en consultant la phrase.** Le réseau débruiteur est appliqué
   une cinquantaine de fois. À chaque passage, il estime le bruit présent et en
   retire une partie. Pour choisir la direction, chaque zone de l'image en cours
   consulte les vecteurs des mots par **attention croisée**. C'est le mécanisme qui,
   dans le [Transformer](docs/module3/70-attention-transformer/#le-transformer),
   permet à la traduction de consulter la phrase d'origine. Une zone qui devient un
   casque va chercher son information dans « astronaute ».
4. **Décoder.** Le décodeur de l'autoencodeur transforme la grille finale en une
   image de 512 × 512 pixels.

{{< image src="/images/module4/texte-image.svg" alt="Un schéma. En haut, la consigne « un chat astronaute sur la lune » entre dans l'encodeur de textes de CLIP, qui en fait six vecteurs, un par mot. En bas, de gauche à droite : une petite grille de bruit dans l'espace latent, de 16 384 nombres ; le débruiteur, appliqué cinquante fois, qui consulte les vecteurs des mots par attention croisée ; la grille débruitée, toujours dans l'espace latent ; le décodeur de l'autoencodeur ; et l'image finale de 512 sur 512 pixels, soit 786 432 nombres, qui montre un chat en combinaison spatiale sur la Lune." title="Stable Diffusion assemble trois réseaux : un encodeur de textes, un débruiteur qui travaille dans l'espace latent, et le décodeur d'un autoencodeur. L'image finale est une vraie sortie du modèle ; les deux petites grilles sont des illustrations." loading="lazy" >}}

La figure ci-dessous montre les vraies étapes du débruitage. À chaque étape, la
grille en cours est décodée en image. Le chat et son scaphandre émergent peu à peu
du bruit, puis les détails se précisent.

{{< image src="/images/module4/stable-diffusion-etapes.jpg" alt="Cinq images côte à côte. La première n'est que du bruit coloré. Après 20 passages, on devine une silhouette claire au centre. Après 30 passages, un astronaute se dessine, avec une lune jaune à droite. Après 40 passages, on reconnaît un chat dans un scaphandre blanc, sur un sol gris, sous un ciel étoilé. Après 50 passages, l'image est nette : un chat astronaute dessiné, sur un sol lunaire, entouré d'étoiles." title="Les étapes du débruitage dans Stable Diffusion 1.5, pour la consigne « a cat astronaut on the moon, digital painting » (ce modèle ne comprend que l'anglais). À chaque étape, la grille latente en cours est décodée en image." loading="lazy" >}}

On retrouve ici le
[jeu de construction](docs/module3/42-materiel-et-outils/#un-jeu-de-construction) du
Module 3 : un encodeur de textes entraîné par CLIP, un autoencodeur et un
débruiteur, trois réseaux assemblés en un seul système.

Un réglage permet de doser l'influence du texte. On estime le bruit à retirer deux
fois, avec la phrase et sans elle, puis on amplifie la différence entre les deux.
C'est le **guidage sans classificateur** (*classifier-free guidance*), présenté en
2021 par Jonathan Ho et Tim Salimans. Plus l'**échelle de guidage** est forte, plus
l'image respecte la phrase, au prix d'une moindre diversité et parfois d'un aspect
artificiel. La plupart des générateurs d'images proposent ce réglage à leurs
utilisateurs, comme les modèles de langage proposent la
[température](docs/module4/10-generer/#la-température).

## Les limites

L'association entre mots et images reste approximative.

- **La composition.** Ces modèles saisissent bien les objets présents dans une
  phrase, mais moins bien leurs relations. Une demande comme « un cheval qui monte
  sur un astronaute » produisait souvent, dans les premiers générateurs, un astronaute
  à cheval, la scène la plus fréquente dans les images d'entraînement. Le
  [panneau d'arrêt](docs/module4/30-images-voix-videos/#les-images) planté sur un
  poteau, au lieu de voler, en est un autre exemple.
- **Le comptage et le texte.** Demander exactement sept pommes, ou une pancarte
  portant un mot précis, a longtemps donné de mauvais résultats. Les modèles récents
  ont beaucoup progressé sur ce point.
- **L'attaque typographique.** En 2021, OpenAI montre qu'une pomme sur laquelle on a
  collé une étiquette portant le mot « iPod » est classée par CLIP comme un iPod. Le
  modèle a appris à lire, et le mot écrit l'emporte sur l'objet. C'est une variante
  des attaques présentées au chapitre
  « [Tromper un réseau](docs/module3/90-tromper-un-reseau) » du Module 3.
- **Les données du Web.** Ces modèles héritent des biais et des contenus de leurs
  données. LAION-5B, un ensemble de près de six milliards de paires d'images et de
  légendes recueillies sur le Web, a servi à entraîner Stable Diffusion. En
  décembre 2023, des chercheurs de l'Université Stanford y ont découvert plus d'un
  millier d'images d'abus pédosexuels, et l'ensemble a été retiré pour être nettoyé.
  Le [Module 5](docs/module5) revient sur ces questions.

CLIP relie un texte et une image, mais il ne décrit pas une image avec ses propres
mots, et il ne converse pas. Le [chapitre suivant](docs/module4/92-voir-entendre-parler) présente les modèles
qui voient, entendent et parlent.
