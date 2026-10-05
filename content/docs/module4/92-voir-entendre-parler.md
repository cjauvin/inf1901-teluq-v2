---
title: "Des modèles qui voient, entendent et parlent"
weight: 92
slug: voir-entendre-parler
---

# Des modèles qui voient, entendent et parlent

Le chapitre « [Relier les mots et les images](docs/module4/90-mots-et-images) » a
présenté CLIP, qui place images et textes dans un même espace. CLIP sait dire si une
légende convient à une image, mais il ne décrit pas une image avec ses propres mots,
et il ne répond pas à une question à son sujet. Depuis 2023, les grands assistants
le font : on peut leur montrer une photo, un graphique ou une page manuscrite, leur
parler à voix haute, et les entendre répondre. Ce chapitre présente comment un modèle
de langage a appris à voir et à entendre, ce que cela permet, et ce qui lui échappe
encore.

## Une image découpée en jetons

En octobre 2020, une équipe de Google publie un article intitulé « *An Image is Worth
16x16 Words* » (« une image vaut 16 × 16 mots »). Elle découpe chaque image en petits
carreaux de 16 pixels de côté, transforme chaque carreau en vecteur, et donne la
suite de ces vecteurs à un [Transformer](docs/module3/70-attention-transformer/#au-delà-du-texte),
exactement comme une suite de mots. Ce **Vision Transformer** (ViT) atteint les
performances des meilleurs réseaux convolutifs, à condition d'être entraîné sur assez
d'images. Il montre qu'une même architecture peut traiter le texte et les images : il
suffit de transformer les deux en suites de jetons.

L'applet ci-dessous découpe une photo de la même façon. Faites varier la taille des
carreaux et observez le nombre de jetons obtenus.

{{< applet src="/html/applets/jetons-visuels.html" height="502" >}}

Des carreaux plus petits conservent plus de détails, mais ils produisent beaucoup plus
de jetons. Avec des carreaux de 8 pixels, cette image de 448 pixels de côté donne
3 136 jetons, autant qu'un long texte. Comme le calcul de l'attention augmente avec
le carré du nombre de jetons, la résolution des images est un compromis entre
précision et coût. C'est l'une des raisons pour lesquelles ces modèles distinguent mal
les petits détails.

## Un modèle de langage qui lit des images

Pour qu'un modèle de langage lise une image, on combine trois éléments.

1. Un **encodeur d'images**, souvent un Vision Transformer préentraîné comme celui de
   CLIP, transforme l'image en une suite de vecteurs.
2. Une **projection** convertit ces vecteurs en vecteurs de même forme que les
   plongements des mots. Ce sont des **jetons visuels**.
3. Le **modèle de langage** reçoit les jetons visuels suivis des jetons de la question,
   et il prédit sa réponse jeton après jeton, comme d'habitude.

Ces modèles sont des assemblages, au sens du [jeu de construction](docs/module3/42-materiel-et-outils/#un-jeu-de-construction) du
Module 3 : un encodeur d'images et un modèle de langage, souvent entraînés
séparément, sont reliés par une projection, puis ajustés ensemble.

{{< image src="/images/module4/modele-qui-voit.svg" alt="Un schéma. Une image est découpée en carreaux, qui passent par un encodeur d'images. Une projection transforme chaque vecteur obtenu en un jeton visuel, de même forme que les jetons de mots. Les jetons visuels et les jetons de la question « Combien de personnes traversent ? » forment une seule séquence, que lit le modèle de langage. Le modèle répond par du texte, jeton après jeton." title="Un modèle de langage qui lit une image : l'image devient une suite de jetons visuels, placés devant la question." loading="lazy" >}}

Le modèle est ensuite entraîné sur des paires d'images et de textes, puis ajusté sur
des conversations à propos d'images, selon les étapes présentées au chapitre
« [Du modèle à l'assistant](docs/module4/70-du-modele-a-l-assistant) ». DeepMind
présente cette approche en 2022 avec Flamingo. En 2023, LLaVA, un modèle ouvert
construit par des chercheurs universitaires, montre qu'on peut l'appliquer à peu de
frais. La même année, OpenAI ouvre au public la vision de GPT-4, et Google présente
Gemini, entraîné dès le départ sur du texte, des images, du son et de la vidéo. On
parle de **modèles multimodaux** (*multimodal models*), parce qu'ils traitent
plusieurs types de données.

Ces modèles décrivent une photo, lisent un document scanné, interprètent un graphique,
transcrivent une page manuscrite ou expliquent une capture d'écran. En 2023,
l'application Be My Eyes, qui mettait les personnes aveugles en relation avec des
bénévoles voyants, intègre un assistant multimodal qui décrit ce que filme le
téléphone. En robotique, des modèles comme RT-2, présenté par Google DeepMind en 2023,
produisent directement des commandes de mouvement à partir d'une image et d'une
consigne en langage naturel, comme « ramasse l'objet qui pourrait servir de
marteau ».

## Entendre et parler

Le son peut être traité de la même façon. En 2022, OpenAI publie Whisper, un modèle
de reconnaissance de la parole entraîné sur 680 000 heures d'enregistrements dans de
nombreuses langues, avec leur transcription. Whisper transforme un enregistrement en
une image de ses fréquences, la découpe en morceaux, et un Transformer produit la
transcription jeton après jeton. Il comprend des accents variés et des enregistrements
bruités, et il traduit vers l'anglais.

Les premiers assistants vocaux enchaînaient trois modèles : la parole était transcrite
en texte, le texte était envoyé au modèle de langage, et la réponse était lue par une
voix de synthèse comme celles du chapitre
« [Des images, des voix, des vidéos](docs/module4/30-images-voix-videos/#les-voix-et-la-musique) ».
Ce relais perdait le ton de la voix, les hésitations et les émotions, et il ajoutait
plusieurs secondes d'attente. En mai 2024, OpenAI présente GPT-4o, où le *o* signifie
*omni*. Le même modèle reçoit et produit directement du texte, des images et du son.
Il répond à la voix en un tiers de seconde en moyenne, un délai proche de celui d'une
conversation humaine, et il peut rire, chanter ou changer d'intonation.

## Générer des images avec un modèle de langage

Un modèle multimodal peut aussi produire des jetons visuels. Si une image est une suite
de jetons, un modèle de langage peut la générer
[un élément après l'autre](docs/module4/20-quatre-facons-de-generer/#un-élément-après-lautre-les-modèles-autorégressifs),
comme un texte. En 2025, OpenAI et Google intègrent ainsi la génération d'images
directement dans leurs modèles de langage. Comme le modèle comprend toute la
conversation, il suit beaucoup mieux les consignes détaillées, modifie une image en
tenant compte des demandes précédentes, et écrit correctement du texte dans l'image.
Le dernier panneau d'arrêt de la
[figure du chapitre sur les images](docs/module4/30-images-voix-videos/#les-images),
qui vole enfin dans le ciel, a été produit de cette façon. Certains de ces systèmes
combinent une génération autorégressive avec une étape de
[diffusion](docs/module4/20-quatre-facons-de-generer/#retirer-le-bruit-pas-à-pas-la-diffusion)
qui affine les détails : on retrouve les familles de méthodes du début du module,
assemblées.

## Ce qui leur échappe encore

Les modèles multimodaux donnent une impression de vision humaine, mais leurs erreurs
montrent qu'ils voient autrement.

- **Les détails géométriques.** En 2024, une équipe de chercheurs publie une étude
  intitulée « *Vision language models are blind* ». Les meilleurs modèles de l'époque
  échouent à des tâches qu'un enfant réussit : dire si deux cercles se touchent,
  compter les intersections de deux lignes, ou compter les lignes d'une grille.
- **Le comptage et les positions.** Compter des objets nombreux, dire lequel est à
  gauche de l'autre, ou lire l'heure sur une horloge à aiguilles restent des
  difficultés fréquentes.
- **Les hallucinations visuelles.** Un modèle peut décrire avec assurance un objet
  absent de l'image, parce qu'il est fréquent dans des scènes semblables, comme une
  fourchette à côté d'une assiette.
- **Les instructions cachées dans les images.** Un texte écrit dans une image est lu
  comme le reste de la requête. Une image peut donc contenir une
  [injection d'instructions](docs/module4/80-outils-et-agents/#des-agents),
  comme une page Web.

Ces difficultés posent une question déjà rencontrée avec la vidéo : un modèle qui
décrit si bien des images a-t-il une représentation du monde qu'elles montrent, ou
reproduit-il les associations les plus fréquentes entre images et mots ? Le
[chapitre suivant](docs/module4/94-comprendre-et-rater) aborde cette question pour l'ensemble des modèles de
langage.
