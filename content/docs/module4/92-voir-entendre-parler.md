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

Le Module 3 a présenté le
[*Vision Transformer*](docs/module3/70-attention-transformer/#au-delà-du-texte) (ViT),
publié par Google en 2020 sous le titre « *An Image is Worth 16x16 Words* » (« une
image vaut 16 × 16 mots »). Il découpe une image en carreaux de 16 pixels de côté et
les traite comme les mots d'une phrase. Une même architecture peut donc traiter le
texte et les images, à condition de transformer les deux en suites de jetons.

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
   plongements des mots. Ce sont des **jetons visuels** (*visual tokens*).
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

## Lire le texte dans les images

Lire le texte d'une image est l'un des plus vieux problèmes de l'IA. On l'appelle la
**reconnaissance optique de caractères** (*optical character recognition*, OCR). En
1976, Ray Kurzweil présente une machine qui lit à voix haute les livres imprimés pour
les personnes aveugles, en combinant pour la première fois un OCR capable de lire
toutes sortes de polices et une voix de synthèse. Le réseau convolutif de Yann Le Cun,
présenté au [Module 3](docs/module3/50-reseaux-convolutifs/#yann-le-cun-et-les-chèques),
lit les codes postaux, puis les chèques. Le logiciel Tesseract, développé chez
Hewlett-Packard de 1985 au milieu des années 1990, puis rendu libre en 2005 et repris
avec le soutien de Google, reste aujourd'hui un outil courant.

Un système d'OCR classique est une chaîne de pièces : repérer les lignes de texte,
isoler les caractères, reconnaître chacun, puis corriger les erreurs avec un
[modèle de langage](docs/module4/40-des-regles-aux-probabilites/#un-modèle-de-langage).
Celui-ci y joue son rôle d'arbitre : entre « vcrre » et « verre », il choisit le mot
qui ressemble à du vrai texte.

L'OCR a aussi nourri les grands modèles de langage. Une bonne partie des livres et des
documents anciens n'existe qu'en images. Le projet Google Livres, lancé en 2004, en a
numérisé plus de 40 millions, et c'est l'OCR qui en fait du texte. Ses erreurs se
retrouvent donc dans les données d'entraînement, et des études montrent qu'elles
dégradent les modèles qui en apprennent.

Les modèles multimodaux ont changé la donne. Ils lisent directement l'image, sans
chaîne séparée, et comprennent en même temps la mise en page, les tableaux, l'écriture
manuscrite et le sens du texte. Leurs erreurs changent aussi de nature. Un OCR
classique se trompe de lettre. Un modèle multimodal, lui, reconnaît souvent les mots
par leur sens plutôt que par la forme de leurs lettres : devant un mot flou, rare ou
dépourvu de sens, il peut écrire un mot plausible qui ne figure pas dans l'image, une
forme d'[hallucination](docs/module4/94-comprendre-et-rater/#les-hallucinations),
plus difficile à repérer qu'une lettre fausse.

{{< image src="/images/module4/deux-facons-de-lire.svg" alt="Deux rangées. En haut, l'OCR classique, une chaîne de quatre pièces : repérer les lignes de texte sur la page ; isoler les caractères du mot verre, chacun dans une petite boîte ; reconnaître chaque caractère, ce qui donne v, c, r, r, e, avec une erreur, un c à la place du e, à cause d'une tache ; puis corriger avec un modèle de langage, qui préfère verre, probable, à vcrre, improbable. Erreur typique : une lettre fausse. En bas, un modèle multimodal : l'image de la page devient des jetons visuels, que le modèle de langage lit d'un coup ; il écrit le texte, « Au serveur : Un verre d'eau, s'il vous plaît », et comprend en même temps la mise en page et le sens. Erreur typique : un mot ou une ligne plausible, inventé, qui ne figure pas dans l'image." title="Deux façons de lire le texte d'une image. Dans les deux cas, un modèle de langage intervient : comme arbitre à la fin d'une chaîne, ou comme lecteur unique." loading="lazy" >}}

En octobre 2025, DeepSeek renverse le problème. Son modèle DeepSeek-OCR montre qu'un
long texte, rendu sous forme d'image, peut être donné à un modèle avec environ dix fois
moins de jetons visuels qu'il n'y aurait de jetons de texte, et relu à 97 %. Les
auteurs y voient une piste pour faire tenir de plus longs contextes dans la
[fenêtre](docs/module4/50-predire-le-mot-suivant/#gpt-un-transformer-qui-prédit-le-jeton-suivant)
d'un modèle : l'image devient une façon de compresser le texte.

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

## Converser à voix haute

Pour qu'un modèle de langage parle vraiment, il faut d'abord faire du son des jetons.
Les **codecs audio neuronaux** (*neural audio codecs*) s'en chargent : SoundStream, présenté par Google
en 2021, puis EnCodec, présenté par Meta en 2022, compressent un enregistrement en une
suite de jetons discrets, quelques dizaines par seconde, à partir desquels on peut
reconstituer le son. Comme les jetons visuels, ce sont des morceaux de signal traités
comme des mots. En 2022, le modèle AudioLM, de Google, prédit ces jetons un à un : à
partir de quelques secondes d'une voix, il continue la phrase avec la même voix et la
même intonation, sans passer par aucun texte. Le principe de prédire le jeton suivant
s'applique tel quel à la parole.

Reste le **tour de parole** (*turn-taking*). Dans une conversation humaine, on ne s'attend pas en
silence : on se répond en général en moins d'un quart de seconde, comme l'a montré une
étude menée en 2009 sur dix langues, on glisse des « mm-hmm » pendant que l'autre
parle, et l'on s'interrompt. Les premiers modes vocaux, comme celui de GPT-4o à sa
sortie, attendaient que la personne se taise pour répondre. En juillet 2024, le
laboratoire parisien Kyutai présente **Moshi**, un modèle ouvert qui écoute et parle
en même temps. Il reçoit deux flux de jetons audio, celui de la personne et le sien,
et prédit, toutes les 80 millisecondes, son prochain jeton, qui peut être un silence.
Avant chaque morceau de sa propre parole, il écrit aussi le texte correspondant, une
sorte de monologue intérieur qui l'aide à rester cohérent. Il répond en environ
200 millisecondes. On parle de conversation en **duplex intégral** (*full duplex*),
comme au téléphone, par opposition au talkie-walkie, où l'on parle chacun son tour.
En juillet 2026, OpenAI adopte ce mode pour ChatGPT avec GPT-Live, qui confie les
questions difficiles à un modèle plus lent, qui raisonne en arrière-plan.

{{< image src="/images/module4/duplex.svg" alt="Six secondes d'une conversation à voix haute, sur une ligne du temps. En haut, la voix de la personne : « Je cherche un livre pour ma mère, elle aime les romans… ». Pendant qu'elle parle, le modèle glisse un « mm-hmm », sans l'interrompre. Environ deux cents millisecondes après la fin de sa phrase, il répond : « Je vous suggère Kamouraska, d'An… ». La personne l'interrompt, « Ah, elle l'a déjà lu ! », et le modèle s'arrête aussitôt, puis propose autre chose. En bas, deux rangées de petits carrés : les jetons audio de la personne, que le modèle écoute, et ses propres jetons, qu'il produit, un toutes les 80 millisecondes, en même temps ; les silences sont aussi des jetons." title="Une conversation en duplex intégral. Le modèle ne reçoit pas des répliques, mais deux flux continus de jetons audio ; à chaque pas, il décide de parler ou de se taire." loading="lazy" >}}

Le mécanisme reste celui d'[une conversation qui n'en est pas une](docs/module4/80-outils-et-agents/#une-conversation-qui-nen-est-pas-une) :
tout s'accumule dans le contexte, sous forme de jetons audio plutôt que de texte, et
le modèle ne garde rien d'une conversation à l'autre. Mais la voix change beaucoup
l'expérience, et ouvre des usages comme des risques.

- **La traduction simultanée.** En février 2025, Kyutai présente Hibiki, qui traduit
  en direct du français vers l'anglais en gardant la voix de la personne. Google, dans
  sa visioconférence Meet en mai 2025, puis Apple, dans ses écouteurs AirPods en
  septembre 2025, proposent ensuite leurs propres systèmes de traduction vocale
  simultanée.
- **L'illusion de comprendre.** Le ton, le rire et les hésitations renforcent
  l'[effet ELIZA](docs/module4/94-comprendre-et-rater/#lillusion-de-comprendre). Le
  13 mai 2024, pendant la présentation de GPT-4o, le patron d'OpenAI, Sam Altman,
  publie un seul mot, « her », allusion au film *Her* (Spike Jonze, 2013), où un
  homme tombe amoureux d'une voix artificielle. Une semaine plus tard, OpenAI suspend
  l'une de ses voix. L'actrice Scarlett Johansson, la voix du film, avait refusé de
  prêter sa voix à OpenAI, et elle jugeait celle-ci trop semblable à la sienne.
- **Le clonage de voix.** Le chapitre
  « [Des images, des voix, des vidéos](docs/module4/30-images-voix-videos/#les-voix-et-la-musique) »
  a présenté VALL-E, qui imite une voix à partir de quelques secondes
  d'enregistrement, et les fraudes par
  [hypertrucage](docs/module4/30-images-voix-videos/#les-hypertrucages), comme celle
  qui a visé la firme Arup. En janvier 2024, des électeurs du New Hampshire reçoivent
  un appel automatisé où une fausse voix de Joe Biden les incite à ne pas voter, et
  l'autorité américaine des télécommunications interdit ensuite les voix générées par
  l'IA dans ce genre d'appels. Kyutai a d'ailleurs choisi de ne pas publier la
  capacité de clonage de ses modèles.

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
  compter les intersections de deux lignes, ou compter les lignes d'une grille. Du
  côté du dessin, le test du [pélican à vélo](docs/module4/60-passer-a-l-echelle/#que-mesurent-les-scores)
  de Simon Willison suit les progrès des modèles qui doivent dessiner sans voir.
- **Le comptage et les positions.** Compter des objets nombreux, dire lequel est à
  gauche de l'autre, ou lire l'heure sur une horloge à aiguilles restent des
  difficultés fréquentes.
- **Les hallucinations visuelles.** Un modèle peut décrire avec assurance un objet
  absent de l'image, parce qu'il est fréquent dans des scènes semblables, comme une
  fourchette à côté d'une assiette.
- **Les instructions cachées dans les images.** Un texte écrit dans une image est lu
  comme le reste de la requête. Une image peut donc contenir une
  [injection d'instructions](docs/module4/80-outils-et-agents/#des-agents-un-modèle-et-son-harnais-en-boucle),
  comme une page Web.

Ces difficultés posent une question déjà rencontrée avec
[la vidéo](docs/module4/30-images-voix-videos/#la-vidéo) : un modèle qui décrit si bien
des images a-t-il une représentation du monde qu'elles montrent, ou reproduit-il les
associations les plus fréquentes entre images et mots ? Le
[chapitre suivant](docs/module4/93-regarder-a-l-interieur) regarde d'abord à
l'intérieur des modèles, et le chapitre
« [Ce que les LLM comprennent, et ce qu'ils ratent](docs/module4/94-comprendre-et-rater) »
aborde ensuite cette question pour l'ensemble des modèles de langage.
