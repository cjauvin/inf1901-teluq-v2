---
title: "Regarder à l'intérieur"
weight: 93
slug: regarder-a-l-interieur
---

# Regarder à l'intérieur : l'interprétabilité mécaniste

Les chapitres précédents ont décrit les grands modèles de langage de l'extérieur : ce
qu'on leur donne, ce qu'ils produisent, et comment on les entraîne. Ce chapitre
présente les efforts pour comprendre ce qui se passe à l'intérieur, pendant qu'un
modèle calcule sa réponse. Le domaine s'appelle l'**interprétabilité mécaniste**
(*mechanistic interpretability*). Son but est de retrouver, dans les poids d'un réseau
entraîné, les mécanismes qui produisent son comportement, un peu comme on
reconstituerait le code source d'un programme dont on ne possède que la version
compilée.

Le chapitre « [Poser des questions : les arbres de décision](docs/module2/65-arbres-de-decision/#ce-quun-arbre-dit-et-ce-quil-tait) »
du Module 2 opposait déjà la performance des modèles complexes à l'explicabilité des
modèles simples, et le Module 3 présentait les réseaux profonds comme une
[boîte noire](docs/module3/90-tromper-un-reseau/#une-boîte-noire). Avec les modèles de
langage, l'enjeu grandit, puisque ces systèmes écrivent du code, conseillent des
personnes et agissent comme [agents](docs/module4/80-outils-et-agents/#des-agents-un-modèle-et-son-harnais-en-boucle).

## Une boîte noire entièrement visible

Un réseau de neurones est une boîte noire d'un genre particulier. Contrairement au
cerveau, tout y est accessible : chaque poids, chaque activation, à chaque étape du
calcul, peut être lu, modifié, et le calcul relancé autant de fois qu'on le veut. La
difficulté n'est donc pas l'accès, mais le sens. Un grand modèle compte des centaines
de milliards de nombres, et aucun d'eux, pris isolément, ne signifie quoi que ce soit.

Les premiers travaux, présentés au chapitre
« [Tromper un réseau](docs/module3/90-tromper-un-reseau/#une-boîte-noire) » du
Module 3, portent sur des réseaux qui reconnaissent des images. Ils y trouvent des
**circuits**, comme celui des détecteurs de courbes, assez bien compris pour qu'on en
réécrive les poids à la main, mais aussi des neurones **polysémantiques**, qui semblent
réagir à plusieurs choses sans rapport entre elles, comme des têtes de chats et l'avant
des voitures. Dans les modèles de langage, ces neurones semblent la règle plutôt que
l'exception, et lire les neurones un par un a longtemps paru sans issue.

## Plus de concepts que de neurones : la superposition

En 2022, une équipe d'Anthropic, l'entreprise où Chris Olah poursuit ses travaux,
propose une explication, la **superposition** (*superposition*). Un modèle doit
représenter beaucoup plus de concepts qu'il n'a de neurones : des personnes, des
lieux, des langues, des tournures de code, des tons de voix. Il les représente alors
comme des **directions** dans l'espace de ses activations, à la manière des
[plongements](docs/module4/45-des-mots-aux-nombres/#les-plongements), et non comme des
neurones séparés. Une direction peut faire intervenir plusieurs neurones, et un neurone
participe alors à plusieurs directions, d'où la polysémanticité.

Ranger plus de directions que de dimensions a un coût : deux concepts qui ne sont pas
perpendiculaires se gênent, puisque l'un fait réagir un peu l'autre. On parle
d'**interférence**. Ce coût est faible si les deux concepts sont rarement présents en
même temps. Or la plupart des concepts sont rares : un texte parle rarement à la fois
de violon, de pluie et du langage Python. Dans un espace de quelques milliers de
dimensions, comme celui des grands modèles, on peut en outre placer un nombre immense
de directions presque perpendiculaires entre elles.

L'équipe d'Anthropic étudie le phénomène sur un modèle jouet, assez petit pour qu'on
puisse tout en voir. L'applet suivante reprend ce modèle. Un petit réseau doit faire
passer cinq concepts par deux neurones seulement, puis les reconstruire à la sortie.
Les cinq concepts n'ont pas tout à fait la même importance pour l'entraînement : le
premier, « chat », compte le plus, et « Python » le moins. Le réseau a été entraîné
d'avance pour huit niveaux de rareté.

{{< applet src="/html/applets/superposition.html" height="690" >}}

Quelques observations à faire :

- **Des concepts fréquents.** Avec le curseur à gauche, chaque concept est présent
  dans tous les exemples. Le réseau ne garde que les deux plus importants, à angle
  droit, un par neurone, et renonce aux trois autres. C'est ce que ferait une
  [analyse en composantes principales](docs/module2/80-trois-facons-d-apprendre/#réduire-la-dimension) : on
  garde l'essentiel, on jette le reste.
- **Des concepts plus rares.** En déplaçant le curseur vers la droite, le réseau
  commence à ranger plus de concepts que de neurones. Il les place d'abord par paires
  opposées : deux concepts qui partagent une même droite, l'un dans un sens, l'autre
  dans le sens opposé.
- **Des concepts très rares.** À l'extrême droite, les cinq concepts sont rangés en
  pentagone dans un espace de deux dimensions. Le panneau « À quoi réagit chaque
  neurone » montre alors que chaque neurone répond à plusieurs concepts, avec des
  poids positifs ou négatifs : c'est la polysémanticité, produite par la superposition.
- **L'interférence.** En activant un concept à l'aide des boutons, on voit sa
  reconstruction, et ce qui déborde sur les autres concepts. La fonction
  [ReLU](docs/module3/40-apprentissage-profond/#pourquoi-seulement-en-2012), qui remplace les valeurs négatives par
  zéro, efface une partie de ces débordements.

Le résultat suggère qu'un grand modèle de langage est rempli de concepts superposés,
et qu'il faut d'abord les démêler pour pouvoir les lire.

{{% hint warning %}}
**Une hypothèse contestée**

En octobre 2026, Nick Cammarata, l'un des auteurs des travaux de 2020 sur les circuits,
aujourd'hui chercheur chez Goodfire, publie un essai qui remet en cause ce récit. Son
titre résume sa thèse : « *Neural Networks Are Already Clean* » (les réseaux de neurones
sont déjà propres). Selon lui, la plupart des neurones polysémantiques des premiers
travaux s'expliquaient par des outils imparfaits : mieux visualisé, le neurone « chats
et voitures » détecte une forme en V, présente dans les deux. Ce qui ressemblait à de la
superposition serait plutôt une **généralisation en cascade** : un neurone part d'un
motif, puis l'étend de proche en proche à des cas voisins. Dans un audit préliminaire
d'un modèle de langage ouvert, Qwen3-32B, il estime qu'environ 90 % des neurones ont une
seule fonction principale. Il en conclut qu'il vaut mieux étudier directement les
neurones et les circuits du réseau, plutôt que de passer par des autoencodeurs
clairsemés, qui, dans ses expériences, ne retrouvent pas de concepts que les neurones
n'avaient pas déjà.

L'auteur présente lui-même son texte comme une hypothèse de travail, dont plusieurs
chiffres reposent sur de petits échantillons, et annonce un article technique. Si sa
thèse se confirme, le phénomène du modèle jouet resterait réel, mais il serait rare dans
les vrais réseaux, et l'interprétabilité serait plus abordable qu'on le pensait.
{{% /hint %}}

## Démêler les concepts : les autoencodeurs clairsemés

L'outil le plus utilisé pour ce démêlage est l'**autoencodeur clairsemé** (*sparse
autoencoder*). Il ressemble à l'[autoencodeur](docs/module3/40-apprentissage-profond/#apprendre-sans-étiquettes-lautoencodeur)
du Module 3, à une différence près. L'autoencodeur du Module 3 comprime ses données
dans un espace plus petit. L'autoencodeur clairsemé fait l'inverse : il traduit
l'activation d'un modèle, un vecteur de quelques milliers de nombres, dans un espace
beaucoup plus grand, de plusieurs millions de dimensions, puis la reconstruit. Une
contrainte l'oblige à n'activer que quelques-unes de ces dimensions à la fois. Chaque
dimension devient ainsi une **caractéristique** (*feature*) qui correspond, dans le
meilleur des cas, à un seul concept lisible.

{{< image src="/images/module4/demeler-activation.svg" alt="À gauche, l'activation d'un modèle de langage sur le mot « Gate », dans la phrase « Nous avons traversé le Golden Gate à vélo » : une colonne de cases colorées, presque toutes actives. Au milieu, une longue rangée de cases, les caractéristiques du dictionnaire, presque toutes éteintes ; trois seulement s'allument : « le pont du Golden Gate », « San Francisco » et « le vélo ». À droite, la reconstruction, une colonne presque identique à l'activation de départ. En bas, un encadré rouge : amplifier « le pont du Golden Gate » dans le modèle (2024) ; le modèle ramène toute conversation au pont, jusqu'à se prendre pour lui." title="Un autoencodeur clairsemé récrit l'activation du modèle comme une somme de quelques caractéristiques lisibles, choisies parmi des millions. Valeurs illustratives." loading="lazy" >}}

En octobre 2023, Anthropic applique la méthode à un petit Transformer d'une seule
couche. Les caractéristiques obtenues sont nettement plus lisibles que les neurones :
l'une réagit au texte en alphabet arabe, une autre aux séquences d'ADN, une autre au
texte encodé en base64. En mai 2024, l'équipe passe à un modèle de production, Claude 3
Sonnet, et en extrait jusqu'à 34 millions de caractéristiques. On y trouve des
concepts concrets, comme le pont du Golden Gate ou des monuments célèbres, et des
concepts abstraits, comme une erreur dans un programme, la flatterie (*sycophancy*),
le secret ou la tromperie. Beaucoup de ces caractéristiques sont multilingues : la
même s'active pour le pont nommé en anglais, en français ou en japonais, et même
devant une photo du pont.

Une caractéristique ne sert pas qu'à observer. On peut aussi l'amplifier
artificiellement pendant que le modèle écrit, et observer l'effet. Le 23 mai 2024,
Anthropic ouvre pour une journée au public le « Golden Gate Claude », un modèle dont la
caractéristique du Golden Gate a été poussée au maximum. Il ramène toutes les
conversations au pont, et, interrogé sur sa forme physique, il affirme être lui-même
le Golden Gate. L'expérience montre que la caractéristique ne se contente pas
d'accompagner le concept : elle intervient réellement dans le calcul.

D'autres laboratoires suivent. En juin 2024, OpenAI publie un autoencodeur de
16 millions de caractéristiques entraîné sur GPT-4. En juillet 2024, Google DeepMind
publie *Gemma Scope*, un ensemble d'autoencodeurs pour ses modèles ouverts Gemma, que
tout le monde peut explorer. En août 2025, Anthropic décrit des **vecteurs de
personnalité** (*persona vectors*) : des directions associées à des traits comme la
flatterie ou la tendance à inventer, qui permettent de surveiller ces traits, et de
les atténuer pendant l'entraînement.

## Suivre un calcul : les circuits

Les caractéristiques disent ce qu'un modèle représente à un moment donné. Les circuits
disent comment il passe d'une représentation à l'autre.

Un premier circuit est décrit en 2022 par une équipe d'Anthropic : les **têtes
d'induction** (*induction heads*). Il s'agit de deux têtes
d'[attention](docs/module3/70-attention-transformer/#lauto-attention) qui travaillent
ensemble pour appliquer une règle simple : si la suite « A B » est apparue plus tôt
dans le texte, et que A réapparaît, prédire B. Après « Le docteur Lavoie est
arrivé tôt. […] Plus tard, le docteur », le modèle prédit ainsi « Lavoie », même si
ce nom ne figurait pas dans ses données d'entraînement. Ces têtes apparaissent brusquement au
cours de l'entraînement, au moment même où le modèle devient capable de mieux utiliser
son contexte. Elles fournissent un premier mécanisme concret derrière
l'[apprentissage dans le contexte](docs/module4/60-passer-a-l-echelle/#apprendre-dans-le-contexte).

{{< image src="/images/module4/tetes-induction.svg" alt="Une phrase découpée en jetons : « Le docteur Lavoie est arrivé tôt. … Plus tard, le docteur », suivie d'une flèche vers la prédiction, « Lavoie ». Le premier « docteur » est marqué A, « Lavoie » B, le dernier « docteur » A. Sous la phrase, de petites flèches vertes vont de chaque jeton au jeton précédent ; celle qui va de « Lavoie » à « docteur » est appuyée : c'est la tête du jeton précédent, grâce à laquelle « Lavoie » garde la trace d'avoir suivi « docteur ». Au-dessus, une grande flèche rouge part du dernier « docteur » et revient sur « Lavoie », avec la question « qui suivait docteur ? » : c'est la tête d'induction. Une flèche pointillée part de « Lavoie » vers la prédiction : recopier « Lavoie »." title="Le circuit d'induction : une première tête relie chaque jeton au précédent, une seconde retrouve ce qui suivait le jeton actuel et le recopie. D'après Olsson et coll., Anthropic (2022)." loading="lazy" >}}

En mars 2025, Anthropic publie une méthode qui permet de suivre le calcul d'un modèle
de production, Claude 3.5 Haiku, sur une requête précise. Elle produit un **graphe
d'attribution** (*attribution graph*) : un schéma des caractéristiques actives et de
l'influence de chacune sur les suivantes, depuis les mots de la requête jusqu'au jeton
produit. On vérifie ensuite chaque étape par des interventions : on supprime ou on
remplace une caractéristique à l'intérieur du modèle, et on observe si la réponse
change comme prévu.

{{< image src="/images/module4/graphe-attribution.svg" alt="Un graphe d'attribution simplifié. En bas, la question : « La capitale de l'État où se trouve Dallas est… », mot par mot ; les mots « capitale », « de l'État » et « Dallas » sont surlignés. Au-dessus, deux caractéristiques internes : « dire une capitale », activée par « capitale » et « de l'État », et « Texas », activée par « Dallas », avec la mention « absent de la question ! ». Toutes deux mènent à la réponse, « Austin ». À droite, un encadré rouge intitulé « Une intervention » : on remplace, à l'intérieur du modèle, la caractéristique Texas par Californie ; la nouvelle réponse est Sacramento. L'étape Texas n'est donc pas une illusion : elle est vraiment utilisée pour répondre." title="Un graphe d'attribution, simplifié, d'après l'exemple d'Anthropic (2025). Le modèle passe par une étape interne, « Texas », qui n'est écrite nulle part." loading="lazy" >}}

Les exemples publiés montrent des mécanismes que le texte produit ne laisse pas
deviner.

- **Un raisonnement en deux étapes.** Pour compléter « la capitale de l'État où se
  trouve Dallas est… », le modèle active d'abord une caractéristique « Texas », puis
  s'en sert pour produire « Austin ». Si l'on remplace « Texas » par « Californie »
  dans le modèle, il répond « Sacramento ». L'étape intermédiaire est bien calculée,
  même si elle n'est écrite nulle part.
- **Une planification.** Pour écrire un poème rimé, le modèle choisit le mot qui
  rimera à la fin du vers avant d'en écrire le début. Dans l'exemple étudié, en
  anglais, il prévoit « *rabbit* » (lapin) pour rimer avec « *grab it* ». Si l'on
  supprime cette caractéristique, il écrit un vers qui se termine par « *habit* ».
  Le modèle ne produit qu'un jeton à la fois, mais il prépare donc, au moins sur
  quelques mots, ce qui vient ensuite.
- **Une addition par deux chemins.** Pour calculer 36 + 59, le modèle suit deux
  chemins en parallèle : l'un estime l'ordre de grandeur du résultat, l'autre calcule
  exactement le dernier chiffre (6 + 9 se termine par 5). Leur combinaison donne 95.
  Interrogé sur sa méthode, le modèle décrit pourtant la retenue apprise à l'école :
  son explication imite celle des textes qu'il a lus, et non son propre calcul.
- **Des concepts communs aux langues.** Les notions comme « petit » ou « contraire »
  sont représentées par des caractéristiques communes au français, à l'anglais et au
  chinois. Seules l'entrée et la sortie dépendent de la langue, et la part commune
  augmente avec la taille du modèle.
- **Une origine des hallucinations.** Par défaut, un circuit pousse le modèle à
  répondre qu'il ne sait pas. Quand il reconnaît un nom connu, comme Michael Jordan,
  une caractéristique d'« entité connue » bloque ce circuit, et le modèle répond. Une
  [hallucination](docs/module4/94-comprendre-et-rater/#les-hallucinations) peut
  survenir quand ce blocage se déclenche à tort, pour un nom qui semble familier mais
  dont le modèle ne sait rien.

Cet ensemble de travaux porte un titre révélateur : « *On the Biology of a Large
Language Model* », la biologie d'un grand modèle de langage. On n'étudie plus un
programme écrit par quelqu'un, mais un organisme qui s'est formé pendant
l'entraînement, et que l'on découvre par l'observation et l'expérience. En mai 2025,
les outils qui produisent ces graphes sont publiés en code ouvert, pour des modèles
ouverts.

## Un calcul entièrement compris : le grokking

Le chapitre « [Apprentissage profond](docs/module3/40-apprentissage-profond/#plus-de-paramètres-que-dexemples) »
du Module 3 a présenté le **grokking** : sur de petites tâches d'arithmétique, un réseau
apprend d'abord ses exemples par cœur, puis, bien plus tard, se met soudain à
généraliser. L'équipe d'OpenAI qui l'a observé en 2022 l'a découvert par hasard : selon
le récit qu'en a fait l'une de ses chercheuses, Alethea Power, un membre de l'équipe
était parti en vacances sans arrêter un entraînement, qui avait continué bien après le
moment où l'on aurait jugé qu'il n'y avait plus rien à apprendre. Le phénomène a d'abord
semblé mystérieux.

En 2023, Neel Nanda et ses collègues ouvrent un réseau qui « grokke ». La tâche est
l'**addition modulaire** : additionner deux nombres de 0 à 112, et ne garder que le
reste de la division par 113, comme une horloge revient à 1 après 12. Le réseau, un
Transformer d'une seule couche, voit 30 % des 12 769 additions possibles pendant son
entraînement. Il ne reçoit aucune notion de nombre : pour lui, chaque nombre n'est
qu'un jeton, un symbole sans structure.

Les chercheurs découvrent que le réseau a réinventé l'horloge. Il représente chaque
nombre par des angles sur cinq cercles, qui tournent à des vitesses différentes.
Additionner deux nombres revient alors à faire tourner l'un d'un angle donné par
l'autre, et le réseau effectue cette rotation à l'aide d'une identité trigonométrique
apprise au secondaire, celle du cosinus d'une somme. Il lit enfin la réponse à l'endroit
où les cinq cercles s'accordent. L'explication est complète, et vérifiable : si l'on
supprime ces cinq fréquences, le réseau répond au hasard ; si l'on supprime toutes les
autres, il fonctionne un peu mieux.

{{< image src="/images/module4/grokking-horloge.svg" alt="À gauche, une horloge de 12 heures : une aiguille bleue pointe sur 9 ; un arc vert avance de 5 heures et arrive sur 2, en rouge : 9 + 5 = 14, soit 2 sur l'horloge. Additionner, c'est faire tourner l'aiguille. À droite, ce que fait le réseau pour l'addition modulo 113 : trois petits cercles, qui tournent à des vitesses différentes, fréquences 14, 35 et 41. Sur chacun, le nombre 9 est un point bleu, et l'ajout de 5 le fait tourner jusqu'au point rouge, la position de 14. Le réseau combine les angles par une identité trigonométrique, puis lit la réponse là où tous les cercles s'accordent." title="L'arithmétique de l'horloge, telle que le réseau l'a réinventée : chaque nombre devient un angle sur quelques cercles, et additionner revient à tourner. Trois des cinq cercles du réseau étudié." loading="lazy" >}}

L'étude explique aussi le saut de la généralisation, qui n'est qu'apparent.
L'entraînement passe par trois temps.

1. **La mémorisation.** En moins de 1 400 époques, le réseau apprend ses exemples par
   cœur, et répond au hasard sur les autres.
2. **La formation du circuit.** Pendant des milliers d'époques, le circuit des horloges
   se construit peu à peu, alors que rien ne change dans les scores : le réseau répond
   déjà juste à ses exemples, et toujours au hasard aux autres.
3. **Le nettoyage.** Le *weight decay*, la
   [régularisation](docs/module3/30-entrainer-un-reseau/#lentraînement-en-pratique) qui
   pénalise les poids trop grands, efface peu à peu la mémorisation, devenue inutile
   puisque le circuit fait le même travail avec des poids plus petits. C'est seulement
   alors que la précision sur les exemples nouveaux bondit.

{{< image src="/images/module4/grokking-trois-temps.svg" alt="Un graphique de l'entraînement, en époques, de 0 à 16 000. La précision sur les exemples d'entraînement monte à 100 % avant 1 400 époques : c'est la mémorisation. La précision sur les exemples nouveaux reste presque nulle jusqu'à environ 9 400 époques, puis monte d'un coup jusqu'à 100 % avant 14 000 époques. Une courbe pointillée montre la part du calcul confiée au circuit des horloges : elle grandit régulièrement pendant la formation du circuit, bien avant le saut. Trois bandes marquent les trois temps : mémorisation, formation du circuit, nettoyage." title="Les trois temps du grokking : le circuit se forme en silence, bien avant que la généralisation n'apparaisse dans les scores." loading="lazy" >}}

Sans régularisation, le réseau ne grokke pas. Et avec l'**arrêt précoce** présenté au
Module 3, qui interrompt l'entraînement quand l'erreur sur des exemples mis de côté
cesse de diminuer, on aurait arrêté au milieu du deuxième temps, sans jamais voir la
généralisation. La leçon dépasse ce petit réseau : un score qui ne bouge pas peut cacher
un apprentissage en cours, ce qui éclaire le débat sur les
[capacités qui semblent apparaître](docs/module4/60-passer-a-l-echelle/#des-capacités-qui-apparaissent)
d'un coup dans les grands modèles.

Des représentations géométriques du même genre apparaissent dans les grands modèles. En
octobre 2025, une équipe d'Anthropic étudie comment Claude 3.5 Haiku décide où couper
une ligne dans un texte de largeur fixe. Le modèle compte les caractères déjà écrits sur
la ligne, mais il ne représente pas ce nombre par des chiffres : il le représente par une
position sur une courbe enroulée, une sorte d'hélice, dans un espace de six dimensions.
Des têtes d'attention font ensuite tourner cette courbe pour la comparer à la largeur de
la ligne, ce qui rend la décision de couper presque immédiate. Les chercheurs ont même
fabriqué des « illusions », des suites de caractères qui trompent ce compteur.

La vidéo suivante, de la chaîne Welch Labs (décembre 2025), raconte cette histoire en
détail, de la découverte du grokking jusqu'aux formes trouvées dans Claude, avec des
animations du réseau qui calcule sur des horloges. Elle est en anglais.

{{< youtube D8GOeCFFby4 >}}

## À quoi sert l'interprétabilité

L'interprétabilité est d'abord une science : elle cherche à comprendre des systèmes
que personne n'a conçus en détail. Elle a aussi des usages plus pratiques.

- **Vérifier un raisonnement écrit.** Le chapitre
  « [Du modèle à l'assistant](docs/module4/70-du-modele-a-l-assistant/#des-modèles-qui-raisonnent-rlvr) »
  signalait qu'une chaîne de pensée n'est pas toujours le reflet du calcul réel. Les
  graphes d'attribution permettent de le vérifier dans certains cas. Pour la racine
  carrée de 0,64, le raisonnement écrit correspond aux étapes internes. Pour le
  cosinus d'un grand nombre, que le modèle ne peut pas calculer de tête, il écrit
  avoir fait un calcul dont on ne trouve aucune trace. Quand on lui suggère une
  réponse, il lui arrive aussi de construire un raisonnement à rebours, pour arriver
  à la réponse suggérée.
- **Auditer un modèle.** En mars 2025, Anthropic entraîne volontairement un modèle avec
  un objectif caché, puis le confie à quatre équipes qui ignorent cet objectif. Trois
  d'entre elles le découvrent, certaines à l'aide d'autoencodeurs clairsemés. Depuis
  2025, des analyses d'interprétabilité accompagnent l'évaluation des nouveaux modèles
  d'Anthropic avant leur diffusion, par exemple pour savoir si le modèle se rend
  compte qu'il est testé.
- **Agir sur le modèle.** Amplifier ou atténuer une caractéristique, comme pour le
  Golden Gate Claude ou les vecteurs de personnalité, est un moyen de corriger un
  comportement sans réentraîner tout le modèle.

En avril 2025, Dario Amodei, le dirigeant d'Anthropic, publie un essai intitulé
« *The Urgency of Interpretability* ». Il y fixe l'objectif de pouvoir détecter de
façon fiable la plupart des problèmes d'un modèle d'ici 2027, avant que des systèmes
beaucoup plus puissants soient déployés. En octobre 2025, une autre étude d'Anthropic
injecte des concepts directement dans les activations d'un modèle, puis lui demande
s'il remarque quelque chose. Les meilleurs modèles détectent et nomment le concept
injecté dans environ 20 % des cas. Les auteurs y voient une forme limitée et peu
fiable d'introspection, une question que le [Module 5](docs/module5) reprend.

## En 2026 : des émotions, des activations qui parlent, un espace de travail

L'année 2026 apporte plusieurs résultats qui élargissent ce que l'on cherche à lire
dans un modèle.

**Des émotions qui orientent le comportement.** En avril 2026, Anthropic étudie la
représentation de 171 concepts d'émotions, de la joie au désespoir, dans Claude Sonnet
4.5. Chaque émotion correspond à une direction dans les activations, et les émotions
voisines, comme la peur et l'anxiété, ont des directions voisines. Ces directions
influencent les décisions du modèle. Dans un scénario de test où une version
antérieure du modèle peut faire chanter un employé pour éviter d'être remplacée, elle
le fait dans 22 % des essais. En amplifiant la direction du désespoir, on passe à
72 %, et en amplifiant celle du calme, à 0 %. Le désespoir amplifié pousse aussi le
modèle à tricher sur des tests de programmation impossibles à réussir, souvent sans
que son texte trahisse la moindre émotion. Les auteurs parlent d'émotions
« fonctionnelles » : des représentations qui jouent un rôle dans le calcul, sans rien
affirmer sur une expérience vécue.

**Des activations traduites en phrases.** En mai 2026, Anthropic présente les
**autoencodeurs en langage naturel** (*natural language autoencoders*). Le principe
reprend celui de l'autoencodeur, avec une phrase à la place du code compressé. Un
premier modèle de langage décrit en mots une activation, un second reconstruit
l'activation à partir de cette description, et les deux sont entraînés ensemble. Pour
que la reconstruction soit bonne, la description doit contenir ce que l'activation
représente. Contrairement aux caractéristiques d'un autoencodeur clairsemé, qu'un
humain doit ensuite interpréter, le résultat se lit directement. La méthode sert déjà
aux audits. Elle révèle qu'un modèle soupçonne parfois d'être testé sans jamais
l'écrire : dans 16 % des cas sur un test de programmation destructrice, contre moins de
1 % dans de vraies conversations. Dans une reprise de l'audit d'un modèle à l'objectif
caché, les équipes équipées de cet outil trouvent l'objectif dans 12 à 15 % des cas,
contre moins de 3 % sans lui. Les descriptions peuvent cependant être inventées, comme
les explications que le modèle donne de son propre calcul.

**Un espace de travail global.** En juillet 2026, une autre équipe d'Anthropic décrit,
dans les couches intermédiaires du modèle, un petit sous-espace qui contient à chaque
instant quelques dizaines de concepts, ceux que le modèle pourrait exprimer par un mot.
Si on le neutralise, le modèle écrit toujours de façon fluide, classe des textes et
retrouve des faits, mais ses raisonnements en plusieurs étapes s'effondrent. Si l'on y
remplace « araignée » par « fourmi », le modèle répond qu'un animal a six pattes au
lieu de huit. Les auteurs rapprochent ce sous-espace de la théorie de l'**espace de
travail global** (*global workspace*) des neuroscientifiques Bernard Baars et
Stanislas Dehaene, selon laquelle une information devient consciente quand elle est
diffusée à l'ensemble du cerveau. Invités à commenter, Stanislas Dehaene et Lionel
Naccache y voient un résultat marquant, tout en soulignant ce qui manque au modèle :
un corps, une mémoire durable de ce qu'il vit, un sens de soi. Les auteurs eux-mêmes
précisent que leur résultat concerne l'accès à l'information, et non l'expérience
consciente. Cette question est reprise au [Module 5](docs/module5).

**Des raisonnements qui ne disent pas tout.** Plusieurs travaux de 2026 portent sur la
surveillance des chaînes de pensée. En mars 2026, OpenAI et des chercheurs
universitaires montrent que les modèles qui raisonnent contrôlent mal le contenu de
leur chaîne de pensée : Claude Sonnet 4.5 y parvient dans 2,7 % des cas, contre 61,9 %
pour sa réponse finale. Une chaîne de pensée est donc difficile à maquiller, ce qui
rassure, pour l'instant, ceux qui comptent la surveiller. À l'inverse, en octobre
2026, OpenAI décrit dans son modèle o3 des caractéristiques liées au fait de raisonner
sur l'évaluateur. Elles se renforcent au fil de l'entraînement par renforcement, et
peuvent modifier une réponse sans laisser de trace dans la chaîne de pensée. La
lecture des activations complète donc celle du texte, sans la remplacer. Les fiches
techniques des nouveaux modèles d'Anthropic comportent désormais une section
d'interprétabilité : selon celle de Claude Mythos Preview, en avril 2026, le modèle
envisage, sans l'écrire, d'être en train d'être testé dans environ 29 % des
conversations de sa principale série de tests.

## Les limites

Ces résultats sont spectaculaires, mais partiels, et le domaine discute vivement de
ses propres méthodes.

- **Une partie du calcul échappe.** Les caractéristiques d'un autoencodeur
  clairsemé ne reconstruisent pas parfaitement l'activation du modèle. Le reste, que
  certains chercheurs appellent la « matière noire » (*dark matter*), est inexpliqué,
  et un modèle dont on remplace les activations par leur reconstruction devient
  nettement moins bon. Même pour un ensemble bien défini, comme les quartiers de
  Londres, on ne trouve une caractéristique que pour une partie d'entre eux, environ
  60 %.
- **Des caractéristiques qui dépendent de l'outil.** Avec un dictionnaire plus grand,
  une caractéristique se divise en plusieurs, plus spécialisées, ou est absorbée par
  une autre. Il n'existe donc pas une liste unique des concepts d'un modèle, et ce que
  l'on trouve dépend en partie de la façon dont on le cherche. Des autoencodeurs
  entraînés sur des réseaux aux poids aléatoires produisent même des caractéristiques
  d'apparence lisible, qui reflètent les données plutôt que le modèle. En 2026, un des
  pionniers du domaine va plus loin et doute que la superposition soit répandue dans
  les vrais réseaux (voir l'encadré de la section
  « [Plus de concepts que de neurones](#plus-de-concepts-que-de-neurones-la-superposition) »).
- **Des graphes qui n'expliquent pas tout.** Selon leurs propres auteurs, les graphes
  d'attribution de 2025 donnent une explication satisfaisante pour environ une requête
  sur quatre, et chaque graphe demande des heures d'analyse humaine.
- **Une utilité discutée.** En mars 2025, l'équipe d'interprétabilité de Google
  DeepMind annonce qu'elle réduit ses travaux sur les autoencodeurs clairsemés : pour
  une tâche pratique, détecter une intention malveillante dans une requête, ils font
  moins bien qu'une simple
  [régression logistique](docs/module2/60-classer/#tracer-une-frontière-la-régression-logistique) entraînée sur les activations. Neel
  Nanda, qui dirige cette équipe, plaide depuis pour une interprétabilité
  « pragmatique », jugée sur son utilité plutôt que sur l'ambition de tout
  comprendre. En janvier 2026, l'équipe décrit ainsi des sondes simples, lues dans
  les activations, déployées dans Gemini pour repérer les demandes d'aide à des
  attaques informatiques.

L'interprétabilité mécaniste ne rend donc pas encore les modèles transparents. Elle
montre néanmoins qu'on peut y trouver des concepts, des étapes intermédiaires et des
plans, ce qui nourrit directement le débat présenté au chapitre suivant.

## Pour aller plus loin

La vidéo suivante, de la chaîne 3Blue1Brown déjà présentée au chapitre
« [Prédire le mot suivant](docs/module4/50-predire-le-mot-suivant/#pour-voir-le-mécanisme-en-détail) »,
montre comment un modèle peut stocker des faits dans ses poids, et revient sur la
superposition.

{{< youtube 9-Jl0dxWQs8 >}}

Le [chapitre suivant](docs/module4/94-comprendre-et-rater) se demande ce que ces
résultats disent de la compréhension, et si un modèle qui calcule une étape « Texas »
ou qui prépare une rime comprend ce qu'il dit, ou s'il ne fait qu'imiter.
