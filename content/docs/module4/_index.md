---
title: "Module 4 - IA générative et grands modèles de langage"
weight: 400
bookCollapseSection: true
---

# Module 4 — IA générative et grands modèles de langage

{{< image src="/images/module4/edmond-de-belamy.jpg" alt="Un portrait peint, flou et inachevé, à la manière d'un tableau ancien : un homme vêtu de noir, au col blanc, sur un fond sombre et une toile laissée claire. Son visage est à peine esquissé. En bas à droite, à la place de la signature, une formule mathématique manuscrite." title="Portrait d'Edmond de Belamy (2018), produit par un réseau générateur du collectif Obvious, et vendu 432 500 $ chez Christie's. Il est signé de la formule mathématique qui a servi à l'entraîner. Wikimedia Commons, domaine public." loading="lazy" >}}

## Reconnaître, puis produire

Les réseaux du [Module 3](docs/module3) **reconnaissent**. On leur donne une image,
et ils répondent « 7 » ou « panda ». On leur donne une phrase, et ils proposent sa
traduction. Depuis une dizaine d'années, les mêmes architectures apprennent aussi à
**produire** : des visages de personnes qui n'existent pas, des images à partir
d'une phrase, des voix, de la musique, des vidéos, et surtout du texte.

Le 30 novembre 2022, OpenAI ouvre au public ChatGPT. En deux mois, le service compte
100 millions d'utilisateurs. Pour beaucoup de gens, c'est la première fois qu'une
machine semble comprendre ce qu'on lui dit, et répondre comme le ferait une
personne. L'expression **IA générative** (*generative AI*) se répand alors pour
désigner l'ensemble de ces systèmes, et les **grands modèles de langage** (*large
language models*, LLM) comme celui de ChatGPT en deviennent la figure centrale.

{{< image src="/images/module4/cent-millions-utilisateurs.svg" alt="Un graphique à barres horizontales : le temps qu'a mis chaque service, après son lancement, à atteindre 100 millions d'utilisateurs. Threads, 2023 : 5 jours, en inscriptions. ChatGPT, 2022 : 2 mois. TikTok, 2017 : 9 mois. Instagram, 2010 : 2 ans et demi. Facebook, 2004 : 4 ans et demi. Twitter, 2006 : 5 ans. Spotify, 2008 : 7 ans et demi. Netflix, 2007, pour sa diffusion en ligne : 10 ans." title="ChatGPT a atteint 100 millions d'utilisateurs plus vite que tous les grands services en ligne avant lui. Seul Threads, adossé aux comptes Instagram, a fait mieux depuis. Sources : UBS et Similarweb, annonces des entreprises." loading="lazy" >}}

Ce module explique comment ces systèmes fonctionnent, ce qu'ils permettent, et ce
qui leur échappe.

## Une seule grande idée : imiter une distribution

Le chapitre « [Classer](docs/module2/60-classer/#renverser-le-problème-la-classification-bayésienne) »
du Module 2 distinguait deux façons de construire un modèle. Un modèle
**discriminatif** trace une frontière entre des classes. Un modèle **génératif**
décrit chaque classe, assez précisément pour pouvoir, en principe, en produire de
nouveaux exemples.

L'IA générative, c'est ce « en principe » devenu réalité. Un modèle génératif
apprend comment se répartissent les données, leur **distribution**, puis il tire au
hasard de nouveaux exemples qui se répartissent de la même façon. Un générateur
d'images a appris la distribution des photos. Un grand modèle de langage a appris
celle des textes écrits par des humains : il donne, pour chaque début de texte, la
probabilité de chaque mot qui pourrait suivre, et il écrit en tirant ces mots un par
un.

Le mécanisme est d'une simplicité déconcertante. Rien, dans cette description, ne
parle de comprendre une question, de raisonner ou de vérifier une réponse. Il est
pourtant difficile d'imaginer comment, en répétant cette seule opération, un mot
après l'autre, on obtient les réponses de ChatGPT : expliquer une notion, écrire un
programme, résumer un article ou traduire un poème. Ce contraste est l'une des
grandes surprises de l'IA récente, et il traverse tout ce module. Il revient dans
« [Ce que la prédiction exige](docs/module4/50-predire-le-mot-suivant/#ce-que-la-prédiction-exige) »,
puis dans « [Ce que les LLM comprennent, et ce qu'ils ratent](docs/module4/94-comprendre-et-rater) »,
qui se demande ce que ces modèles comprennent vraiment.

Pour le reste, rien ne change par rapport aux modules précédents. Ces modèles sont
des [réseaux de neurones](docs/module3), entraînés par
[descente de gradient](docs/module2/50-entrainer-un-modele/#apprendre-cest-descendre-la-pente),
et leur architecture la plus importante est le
[Transformer](docs/module3/70-attention-transformer) présenté au Module 3. Ce qui a
changé, c'est l'échelle : des milliards de paramètres, entraînés sur une grande
partie du texte et des images disponibles sur le Web.

## Ce que ce module n'est pas

Trois précisions évitent des malentendus fréquents.

- **Ce module ne demande aucune formule.** Les mécanismes sont expliqués par des
  figures et des applets, dont plusieurs utilisent de vrais modèles : un
  autoencodeur, un modèle de diffusion, de vrais plongements de mots, le découpage
  en jetons de GPT-4o, et CLIP.
- **Ce module explique, il ne tranche pas les grands débats.** La question de savoir
  si ces modèles comprennent est posée au
  [dernier chapitre](docs/module4/94-comprendre-et-rater), avec les arguments des
  deux côtés. Les questions de société, comme le droit d'auteur, l'emploi,
  l'environnement ou la désinformation, sont signalées au passage et traitées au
  [Module 5](docs/module5).
- **Ce module n'est pas un mode d'emploi.** Il présente quelques principes pour
  formuler des requêtes, mais son but est de comprendre ce que font ces systèmes,
  pour mieux juger ce qu'ils produisent.

## Le parcours du module

Le module compte trois parties : l'IA générative en général, puis les grands
modèles de langage, puis la rencontre du texte et de l'image.

**L'IA générative**

1. [*Générer : imiter une distribution*](docs/module4/10-generer) : la distribution,
   le tirage, la température, et l'espace latent d'un autoencodeur.
2. [*Quatre façons de générer*](docs/module4/20-quatre-facons-de-generer) : les GAN,
   les autoencodeurs variationnels, la diffusion et les modèles autorégressifs.
3. [*Des images, des voix, des vidéos*](docs/module4/30-images-voix-videos) : dix
   ans de génération, des protéines à la météo, et les hypertrucages.

**Les grands modèles de langage**

4. [*Des mots aux nombres : jetons et plongements*](docs/module4/40-des-mots-aux-nombres) :
   découper un texte, et représenter le sens des mots par des vecteurs.
5. [*Prédire le mot suivant*](docs/module4/50-predire-le-mot-suivant) : des
   n-grammes de Markov aux Transformers de GPT.
6. [*Passer à l'échelle*](docs/module4/60-passer-a-l-echelle) : les lois d'échelle,
   l'apprentissage en contexte, les coûts, les modèles ouverts.
7. [*Du modèle à l'assistant*](docs/module4/70-du-modele-a-l-assistant) :
   l'ajustement, le renforcement à partir de préférences humaines, et les modèles
   qui raisonnent.
8. [*Des outils et des agents*](docs/module4/80-outils-et-agents) : la recherche
   augmentée, l'appel d'outils, les agents et leurs risques.

**Le texte et l'image, et le bilan**

9. [*Relier les mots et les images*](docs/module4/90-mots-et-images) : CLIP, la
   classification sans exemple, et la génération d'images à partir d'une phrase.
10. [*Des modèles qui voient, entendent et parlent*](docs/module4/92-voir-entendre-parler) :
    les modèles multimodaux.
11. [*Ce que les LLM comprennent, et ce qu'ils ratent*](docs/module4/94-comprendre-et-rater) :
    hallucinations, interprétabilité, perroquets ou modèles du monde.

Le module compte dix applets, dont un espace latent à explorer, un modèle de
diffusion qui redessine une feuille d'érable, un test pour distinguer une vraie
photo d'un visage généré, un générateur de texte entraîné sur Jules Verne, et un
rôle d'évaluateur humain pour comprendre comment on entraîne un assistant.

Pour situer ce module dans l'ensemble du cours : l'IA générative repose sur
l'apprentissage profond du Module 3, lui-même une famille de méthodes
d'apprentissage automatique.

{{< image src="/images/module4/ai-venn.svg" alt="Carte en régions imbriquées de l'intelligence artificielle. À l'intérieur de « Intelligence artificielle (IA) » : d'un côté « IA classique » ; de l'autre « Apprentissage automatique (AA) » (machine learning), qui contient « Méthodes d'AA diverses » et « Réseaux de neurones / apprentissage profond », lesquels contiennent à leur tour « IA générative » et « ChatGPT ». Un repère « Module 4 » pointe vers l'« IA générative » et « ChatGPT », qui sont le sujet du module." title="La carte de l'IA : le Module 4 porte sur l'IA générative et les grands modèles de langage." loading="lazy" >}}

## Objectifs

Au terme de ce module, vous devriez être en mesure de :

* expliquer la différence entre un modèle qui reconnaît et un modèle qui génère, et
  ce que signifie tirer des exemples dans une distribution ;
* décrire le principe des quatre grandes familles de modèles génératifs : GAN,
  autoencodeurs variationnels, diffusion et modèles autorégressifs ;
* expliquer comment un texte est découpé en jetons, et comment des plongements
  représentent le sens des mots ;
* expliquer ce qu'est un modèle de langage, et comment un Transformer génère un texte
  jeton après jeton ;
* expliquer pourquoi la taille des modèles a tant compté, et ce que sont les lois
  d'échelle et l'apprentissage en contexte ;
* décrire les étapes qui transforment un modèle de base en assistant, et le rôle du
  travail humain dans ces étapes ;
* expliquer ce qu'apportent les outils et les agents, et les risques qu'ils posent ;
* expliquer comment des modèles relient les textes, les images et les sons ;
* identifier les principales limites de ces modèles, comme les hallucinations, et
  présenter les arguments du débat sur leur compréhension.

## Durée

Quatre semaines, soit environ 36 heures.

## Évaluation

Un [travail noté](docs/module4/99-travail-noté-4) (20 % de la note finale) où vous
construirez un modèle de langage miniature dans Google Sheets, puis l'utiliserez pour
générer du texte, avec des questions d'interprétation.
