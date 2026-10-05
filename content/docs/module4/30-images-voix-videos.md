---
title: "Des images, des voix, des vidéos"
weight: 30
slug: images-voix-videos
---

# Des images, des voix, des vidéos

Le chapitre « [Quatre façons de générer](docs/module4/20-quatre-facons-de-generer) »
a présenté les méthodes. Celui-ci présente ce qu'elles ont produit en une dizaine
d'années, type de contenu par type de contenu : les images, les voix et la
musique, la vidéo, puis des domaines plus inattendus, comme la conception de
protéines ou la prévision météorologique. Il se termine par les problèmes que ces
contenus posent, en particulier les hypertrucages.

Beaucoup de ces systèmes produisent un contenu à partir d'une phrase, comme « un
chat sur la lune ». Leur fonctionnement demande de savoir représenter le sens d'un
texte, ce qui sera présenté avec les modèles de langage. Les chapitres du
[Module 4](docs/module4/90-mots-et-images) consacrés aux modèles multimodaux expliqueront comment le
texte et l'image sont reliés.

## Les images

Les premiers visages produits par un GAN, en 2014, étaient flous, en noir et blanc,
et mesuraient quelques dizaines de pixels de côté. En 2017, une équipe de Nvidia
produisait des visages en couleur de 1 024 pixels de côté, en faisant grandir
progressivement le générateur et le discriminateur pendant l'entraînement. En 2019,
StyleGAN produisait les visages présentés au début du chapitre
« [Générer : imiter une distribution](docs/module4/10-generer) ».

La génération d'images à partir d'une phrase a suivi une progression semblable. En
2015, Elman Mansimov et ses collègues de l'Université de Toronto présentent
alignDRAW, l'un des premiers modèles capables de produire une image à partir d'une
description. Leur exemple le plus connu est « *A stop sign is flying in blue
skies* » (« un panneau d'arrêt vole dans un ciel bleu »). La figure ci-dessous
montre la même phrase traitée par des générateurs successifs.

{{< image src="/images/module4/panneau-stop.jpg" alt="Quatre images produites à partir de la phrase « A stop sign is flying in blue skies ». En 2015, alignDRAW produit de minuscules images floues de 32 pixels, où l'on devine une tache rouge sur un fond bleuté. En 2022, DALL·E 2 produit un panneau d'arrêt réaliste, planté sur un poteau. En 2023, DALL·E 3 produit un panneau net et brillant, lui aussi sur un poteau, devant un ciel lumineux. En 2025, GPT Image 1 produit un panneau d'arrêt qui flotte réellement dans un ciel bleu parsemé de nuages." title="La même phrase, traitée par quatre générateurs de 2015 à 2025. DALL·E 2 et DALL·E 3 produisent une image réaliste, mais plantent le panneau sur un poteau : ils ne respectent pas toute la phrase." loading="lazy" >}}

Les étapes principales sont les suivantes.

- **Janvier 2021** : OpenAI présente DALL·E. Son « fauteuil en forme d'avocat »
  fait le tour du Web, parce qu'il combine deux idées que personne n'avait
  dessinées ensemble.
- **Avril 2022** : DALL·E 2, un modèle de diffusion, produit des images réalistes
  de 1 024 pixels de côté.
- **Juillet 2022** : Midjourney ouvre son service au public.
- **Août 2022** : Stable Diffusion est publié avec ses poids. N'importe qui peut
  le télécharger et le faire tourner sur un ordinateur personnel muni d'une bonne
  carte graphique, ce qui multiplie les usages et les variantes.
- **2025** : les grands modèles de langage génèrent eux-mêmes des images, comme
  GPT Image 1, intégré à ChatGPT en mars 2025. Ils suivent beaucoup mieux les
  consignes détaillées, comme le montre le dernier panneau de la figure.

{{% hint info %}}
**Un prix d'art pour une image générée**

Le 29 août 2022, l'image *Théâtre D'opéra Spatial* remporte le premier prix de la
catégorie des arts numériques, pour les artistes non professionnels, au concours
d'art de la foire de l'État du Colorado. Son auteur, Jason M. Allen, l'a produite
avec Midjourney, à partir d'au moins 624 consignes et retouches successives, puis
l'a modifiée dans un logiciel de retouche. L'annonce provoque une vive polémique
chez les artistes.

{{< image src="/images/module4/theatre-opera-spatial.jpg" alt="Une scène de science-fiction aux tons dorés, dans le style d'une peinture : des personnages en longues robes se tiennent dans une salle immense, face à une ouverture circulaire qui donne sur un paysage lumineux." title="Théâtre D'opéra Spatial, Jason M. Allen avec Midjourney, 2022. Domaine public : le Bureau du droit d'auteur des États-Unis a refusé de l'enregistrer." loading="lazy" >}}

Jason M. Allen a ensuite demandé à enregistrer les droits d'auteur de l'image. En
septembre 2023, le Bureau du droit d'auteur des États-Unis (*U.S. Copyright
Office*) a rejeté sa demande, au motif que la contribution humaine était trop
faible par rapport à celle du générateur. C'est pour cette raison que l'image est
reproduite ici. La question de savoir à qui appartient une œuvre générée reste
ouverte, et le [Module 5](docs/module5) y revient.
{{% /hint %}}

## Retoucher plutôt que créer

Les modèles génératifs ne servent pas seulement à produire des images complètes.
Ils servent aussi à modifier des images existantes.

- **Le transfert de style** (*style transfer*). En 2015, Leon Gatys et ses
  collègues, à l'Université de Tübingen, montrent qu'un réseau convolutif peut
  redessiner une photo dans le style d'un tableau, par exemple *La Nuit étoilée*
  de Van Gogh. La méthode est proche de celle de
  [DeepDream](docs/module3/40-apprentissage-profond/#une-hiérarchie-de-caractéristiques),
  présenté au Module 3 la même année : on modifie une image pas à pas, à partir de
  ce que voient les couches d'un réseau.
- **Le remplissage** (*inpainting*). On efface une partie d'une image, par exemple
  un passant dans une photo de vacances, et le modèle la remplace par un contenu
  plausible. L'**extension** (*outpainting*) prolonge une image au-delà de son
  cadre.
- **La super-résolution** (*super-resolution*). Le modèle augmente la résolution
  d'une image en inventant des détails plausibles, qui n'étaient pas dans l'image
  d'origine.

Ces fonctions sont aujourd'hui intégrées aux logiciels de retouche, comme le
remplissage génératif de Photoshop depuis 2023, et aux applications photo des
téléphones. Elles rendent la frontière entre une photo et une image générée de
plus en plus floue : une photo retouchée par un modèle génératif contient des
pixels que l'appareil n'a jamais enregistrés.

## Les voix et la musique

En 2016, [WaveNet](docs/module4/20-quatre-facons-de-generer/#un-élément-après-lautre-les-modèles-autorégressifs)
produisait une voix de synthèse beaucoup plus naturelle que les méthodes
précédentes. Les progrès suivants ont surtout porté sur l'**imitation** d'une voix
particulière. En janvier 2023, Microsoft présente VALL-E, qui imite la voix d'une
personne à partir d'un enregistrement de trois secondes, en reproduisant son
timbre et même l'ambiance sonore de l'enregistrement. Ces outils permettent de
rendre la voix à des personnes qui l'ont perdue, ou de doubler un film dans une
autre langue avec la voix des acteurs. Ils permettent aussi des fraudes. En 2019,
des escrocs ont imité la voix du dirigeant d'une entreprise allemande pour obtenir
d'une filiale britannique un virement de 220 000 euros.

La génération de musique a suivi. En 2020, Jukebox, d'OpenAI, produisait des
chansons avec des voix chantées, dans le style de musiciens connus, mais avec une
qualité sonore médiocre. Fin 2023 et début 2024, Suno et Udio produisent des
chansons complètes, avec paroles, voix et instruments, à partir d'une simple
phrase. En avril 2023, une chanson intitulée *Heart on My Sleeve*, dont les voix
imitent celles des musiciens canadiens Drake et The Weeknd, est publiée sur les
plateformes d'écoute et y est écoutée des millions de fois avant d'être retirée
à la demande de leur maison de disques. En 2024, les grandes maisons de disques
poursuivent Suno et Udio, qu'elles accusent d'avoir entraîné leurs modèles sur des
enregistrements protégés.

## La vidéo

Une vidéo est une suite d'images, à raison de 24 à 30 images par seconde. La
générer est plus difficile que générer une image, pour deux raisons. Il y a
beaucoup plus de données à produire, et les images successives doivent rester
**cohérentes** entre elles : un personnage ne doit pas changer de visage, et un
objet ne doit pas disparaître quand un autre passe devant.

En février 2024, OpenAI présente Sora, qui produit des vidéos d'une minute à
partir d'une phrase. La vidéo ci-dessous, publiée par OpenAI, montre des exemples.
Sora est un modèle de
[diffusion](docs/module4/20-quatre-facons-de-generer/#retirer-le-bruit-pas-à-pas-la-diffusion).
La vidéo est découpée en petits blocs, chacun couvrant une petite zone de l'image
pendant quelques images consécutives, et un Transformer retire le bruit de tous ces
blocs à la fois.

{{< youtube HK6y8DAPN_0 >}}

En mai 2025, Google présente Veo 3, qui génère aussi le son synchronisé avec
l'image : les dialogues, les bruits et l'ambiance. En septembre 2025, OpenAI
présente Sora 2, qui fait de même.

Ces vidéos restent imparfaites. Les objets s'y comportent parfois d'une façon
physiquement impossible : un verre qui tombe ne se brise pas correctement, une
personne mord dans un biscuit qui reste intact. Ces erreurs posent une question
importante. Pour produire une vidéo réaliste, un modèle doit-il comprendre les
lois de la physique, ou lui suffit-il d'imiter l'apparence des vidéos qu'il a
vues ? On retrouve la notion de
[modèle du monde](docs/module1/40-representer-le-monde/#shrdlu-ou-le-sommet-de-lambition) présentée au Module 1.
Le chapitre du [Module 4](docs/module4/94-comprendre-et-rater/#perroquets-ou-modèles-du-monde) sur ce que les modèles comprennent
reprendra cette question.

## Au-delà des médias

Les mêmes méthodes s'appliquent à des données qui ne sont ni des images ni des
sons.

- **Les protéines.** Une protéine est une longue chaîne de molécules qui se replie
  dans l'espace, et sa forme détermine ce qu'elle fait dans l'organisme. En 2023,
  l'équipe de David Baker, à l'Université de Washington, publie RFdiffusion, un
  modèle de diffusion qui génère des formes de protéines qui n'existent pas dans
  la nature, conçues pour accomplir une tâche précise, comme se fixer sur un virus.
  David Baker reçoit la moitié du prix Nobel de chimie 2024 pour la conception de
  protéines par ordinateur. L'autre moitié récompense AlphaFold, qui prédit la
  forme des protéines existantes, et que le [Module 5](docs/module5) présentera.
- **La météo.** En 2024, Google DeepMind publie GenCast, un modèle de diffusion qui
  génère plusieurs évolutions possibles du temps qu'il fera sur quinze jours. Sur la
  plupart des mesures, ses prévisions sont plus précises que celles du meilleur
  système classique, celui du Centre européen pour les prévisions météorologiques à
  moyen terme.
- **Les matériaux et les médicaments.** Des modèles génératifs proposent des
  molécules et des matériaux nouveaux, qui sont ensuite testés en laboratoire.
- **Le code informatique.** Les programmes sont des textes. Leur génération relève
  des modèles de langage, présentés dans la suite du [Module 4](docs/module4/50-predire-le-mot-suivant).

Dans ces domaines, l'intérêt d'un modèle génératif est le même que pour les
images : il propose rapidement un grand nombre de candidats plausibles, que l'on
vérifie ensuite.

## Les hypertrucages

Un **hypertrucage** (*deepfake*) est une image, un enregistrement sonore ou une
vidéo générés ou modifiés pour faire croire qu'une personne réelle a dit ou fait
quelque chose qu'elle n'a pas dit ou fait. Le mot anglais apparaît fin 2017, sur
le forum Reddit, comme pseudonyme d'un utilisateur qui publiait des vidéos où le
visage d'actrices avait été placé sur celui d'autres personnes, la plupart du temps
dans des vidéos pornographiques.

Les usages malveillants se sont multipliés depuis.

- **La pornographie non consentie**, qui reste l'usage le plus répandu et vise
  surtout des femmes.
- **La désinformation.** En mars 2022, une fausse vidéo du président ukrainien
  Volodymyr Zelensky, appelant ses soldats à déposer les armes, a circulé sur les
  réseaux sociaux.
- **La fraude.** En 2024, un employé du bureau de Hong Kong de l'entreprise
  d'ingénierie Arup a transféré l'équivalent d'environ 25 millions de dollars
  américains après une visioconférence où ses collègues, dont le directeur
  financier, étaient tous des hypertrucages.

Peut-on distinguer à l'œil une image générée d'une vraie photo ? L'applet
ci-dessous propose dix portraits. Cinq sont de vraies photos, cinq ont été générés
par des modèles de différentes époques, de 2019 à 2026. Pour chacun, décidez s'il
s'agit d'une vraie photo, puis lisez l'explication.

{{< applet src="/html/applets/vraie-ou-generee.html" height="442" >}}

Les visages produits par les modèles de 2019 et 2020 se trahissent encore par des
défauts visibles, surtout dans le fond et les accessoires. Ceux des modèles
récents n'en ont presque plus. Deux autres moyens sont donc à l'étude.

- **Marquer les contenus générés.** SynthID, présenté par Google DeepMind en 2023,
  insère dans les images, les sons et les textes générés une marque invisible,
  qu'un logiciel peut détecter. La coalition C2PA, créée en 2021 par des
  entreprises comme Adobe, Microsoft et la BBC, définit une façon d'attacher à
  chaque fichier l'historique de sa création et de ses modifications.
- **Détecter automatiquement.** Des classificateurs sont entraînés à distinguer les
  contenus générés des contenus réels. Ce sont des modèles
  [discriminatifs](docs/module2/60-classer/#renverser-le-problème-la-classification-bayésienne),
  et le problème rappelle celui du GAN : chaque progrès des détecteurs peut servir à
  entraîner des générateurs plus difficiles à détecter.

Aucune de ces solutions n'est fiable à elle seule. Les marques et les historiques
peuvent être effacés : une semaine après la sortie de Sora 2, des logiciels
permettaient déjà de retirer la marque visible de ses vidéos. Les détecteurs se
trompent, dans les deux sens.

Enfin, ces modèles ont été entraînés sur des millions d'œuvres, souvent sans
l'accord de leurs auteurs. En 2023, des illustratrices et la banque d'images Getty
Images ont poursuivi Stability AI, l'entreprise qui diffuse Stable Diffusion, et
d'autres procès ont suivi pour la musique et les textes. Le
[Module 5](docs/module5) traite ces questions de droit d'auteur, de consentement et
de confiance dans les contenus.

## Le texte, au premier plan

Parmi tous ces contenus, c'est pourtant le texte qui a le plus transformé l'usage
de l'IA. Depuis la sortie de ChatGPT, en novembre 2022, des centaines de millions
de personnes utilisent chaque semaine un modèle qui génère du texte. Ces modèles
appartiennent à la famille
[autorégressive](docs/module4/20-quatre-facons-de-generer/#un-élément-après-lautre-les-modèles-autorégressifs) :
ils produisent un texte un élément après l'autre. Le
[chapitre suivant](docs/module4/40-des-mots-aux-nombres) commence leur étude par une question préalable :
comment transformer des mots en nombres.
