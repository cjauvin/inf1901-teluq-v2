---
title: "Démontrer"
weight: 87
slug: demontrer
---

# Démontrer

{{% hint info %}}
**Chapitre d'approfondissement.** Ce chapitre est facultatif. Il montre ce que les modèles de langage apportent aux mathématiques, mais
la suite du module et le travail noté ne supposent pas de l'avoir lu.
{{% /hint %}}

Les chapitres précédents ont montré le rôle de la vérification : les modèles qui
raisonnent sont entraînés par
[renforcement à partir de récompenses vérifiables](docs/module4/70-du-modele-a-l-assistant/#des-modèles-qui-raisonnent-rlvr),
et les [agents de programmation](docs/module4/85-programmer-avec-des-agents) se
guident sur le verdict des tests. Les mathématiques sont le terrain où cette idée va le plus loin, parce qu'une
démonstration peut être vérifiée sans aucun doute possible, par un programme. Ce
chapitre montre comment, en quelques années, des machines sont passées des problèmes
d'olympiades aux premiers résultats de recherche, et ce que ces résultats disent, ou
ne disent pas.

## Vérifier une preuve

Une démonstration mathématique est un enchaînement d'étapes, chacune justifiée par les
précédentes. Les mathématiciens la vérifient en la lisant, ce qui prend du temps et
laisse passer des erreurs : des démonstrations publiées, parfois célèbres, se sont
révélées fausses ou incomplètes. Depuis les années 1970, des logiciels appelés
**assistants de preuve** (*proof assistants*) permettent d'écrire une démonstration
dans un langage formel, si précis qu'un programme peut la vérifier étape par étape.

Le plus utilisé aujourd'hui, **Lean**, est créé en 2013 par Leonardo de Moura, chez
Microsoft Research. Sa bibliothèque Mathlib, écrite par des centaines de
mathématiciens bénévoles, contient en 2026 près de 300 000 théorèmes, de
l'arithmétique élémentaire à la géométrie algébrique. En 2020, le mathématicien Peter
Scholze, médaillé Fields, met la communauté au défi de vérifier en Lean l'un de ses
résultats les plus difficiles, dont il doutait lui-même ; le défi est relevé en 2022.

{{< image src="/images/module4/preuve-lean.svg" alt="À gauche, un énoncé en français, « la somme de deux nombres pairs est paire », et sa traduction en Lean, un langage de preuve : pour tous entiers naturels a et b, s'il existe x tel que a égale 2 fois x, et y tel que b égale 2 fois y, alors il existe z tel que a plus b égale 2 fois z. Suivent trois étapes de preuve : extraire x, extraire y, puis proposer z égal à x plus y, le calcul étant fait par une procédure automatique. Lean répond : aucune erreur, la preuve est acceptée. À droite, une boucle : le modèle de langage propose une preuve ; Lean la vérifie ; si elle est acceptée, c'est une récompense pour l'entraînement ; si elle est refusée, le message d'erreur revient au modèle, qui corrige. En bas : le vérificateur est un petit programme écrit par des humains, auquel on peut se fier ; il n'y a rien à croire sur parole." title="Une preuve vérifiée par une machine. Cette preuve est réellement acceptée par Lean ; en remplaçant x + y par x × y, Lean la refuse avec un message d'erreur." loading="lazy" >}}

Pour un modèle de langage, un assistant de preuve est le vérificateur idéal. Un
modèle peut écrire une démonstration fausse avec assurance, comme il peut
[halluciner](docs/module4/94-comprendre-et-rater/#les-hallucinations) un fait. Mais une
démonstration acceptée par Lean est juste, quel que soit son auteur : il n'y a rien à
croire sur parole. Le verdict de Lean fournit aussi une récompense parfaitement
exacte pour l'apprentissage par renforcement. Une précaution toutefois : Lean vérifie
qu'une preuve démontre bien l'énoncé écrit en Lean, pas que cet énoncé traduit
fidèlement la question que l'on se posait. La traduction de l'énoncé reste un travail
humain délicat. Et ces preuves vivent à l'intérieur d'un système formel, avec les
limites que Gödel a montrées, présentées au chapitre
« [Turing](docs/module1/10-turing/#lombre-de-gödel) » du Module 1.

## Les Olympiades : de la géométrie à l'or

Les Olympiades internationales de mathématiques (OIM) réunissent chaque année les
meilleurs élèves du secondaire du monde, autour de six problèmes à résoudre en deux
séances de quatre heures et demie. Elles sont devenues un banc d'essai de référence.

- **La géométrie, en 2024.** En janvier 2024, DeepMind présente AlphaGeometry, qui
  résout 25 des 30 problèmes de géométrie des Olympiades de 2000 à 2022, autant qu'un
  médaillé d'or moyen. Il associe un modèle de langage, qui propose des
  constructions auxiliaires, comme tracer une droite ou un cercle, et un moteur de
  déduction symbolique, qui en tire les conséquences. Il réunit ainsi les
  [deux paris](docs/module1/20-deux-paris) du Module 1. Il a été entraîné sur
  100 millions d'exemples engendrés automatiquement, sans aucune démonstration
  humaine.
- **L'argent, en juillet 2024.** Aux Olympiades de 2024, AlphaProof et une nouvelle
  version d'AlphaGeometry obtiennent 28 points sur 42, une médaille d'argent, à un
  point de l'or. Des humains ont traduit les problèmes en Lean, et certains ont
  demandé jusqu'à trois jours de calcul. AlphaProof apprend en Lean par renforcement,
  à la manière d'[AlphaZero](docs/module3/80-renforcement-profond/#alphazero-sans-parties-humaines),
  en s'entraînant sur des dizaines de millions d'énoncés traduits automatiquement.
- **L'or, en juillet 2025.** Un an plus tard, un modèle de Google DeepMind et un modèle
  expérimental d'OpenAI obtiennent chacun 35 points sur 42, le score d'une médaille
  d'or. Cette fois, ils lisent les problèmes et rédigent leurs démonstrations en
  langage naturel, sans Lean, dans le temps imparti aux élèves. Les copies de DeepMind
  sont corrigées et certifiées par les coordonnateurs des Olympiades.

## Découvrir : AlphaEvolve

Résoudre un problème d'olympiade, dont on sait qu'il a une solution, est une chose ;
trouver ce que personne ne sait encore en est une autre. En mai 2025, DeepMind
présente **AlphaEvolve**, un agent qui fait évoluer des programmes. Des modèles de
langage proposent des modifications d'un programme, des évaluateurs automatiques
mesurent la qualité de chaque version, et les meilleures servent de point de départ à
la génération suivante. C'est la boucle des
[agents de programmation](docs/module4/85-programmer-avec-des-agents), appliquée à des
problèmes dont on sait mesurer la réponse.

AlphaEvolve trouve ainsi une façon de multiplier deux matrices de taille 4 × 4 à
coefficients complexes en 48 multiplications au lieu de 49, le record tiré de
l'algorithme de Volker Strassen, de 1969. Sur plus de cinquante problèmes ouverts, il égale
les meilleurs résultats connus dans environ trois cas sur quatre, et les améliore
dans un cas sur cinq. Chez Google, une règle d'ordonnancement qu'il a découverte
récupère 0,7 % de la puissance de calcul des centres de données. En novembre 2025,
une étude menée avec le mathématicien Terence Tao l'applique à 67 problèmes, et
améliore le meilleur résultat connu pour 23 d'entre eux.

## Mesurer : FrontierMath

Les problèmes d'olympiades sont publics, et leurs solutions circulent : les scores
s'exposent à la [contamination](docs/module4/60-passer-a-l-echelle/#que-mesurent-les-scores).
En novembre 2024, l'organisme Epoch AI publie **FrontierMath**, plusieurs centaines de
problèmes inédits, rédigés par des mathématiciens, dont la réponse se vérifie
automatiquement. À la publication, les meilleurs modèles en résolvent moins de 2 %.
Peu après, on apprend qu'OpenAI, dont le modèle o3 vient d'atteindre 25 %, a
financé le banc d'essai et a accès à une grande partie des problèmes, ce que les
mathématiciens qui les avaient rédigés ignoraient. L'épisode rappelle qu'un banc
d'essai n'est fiable que si l'on sait qui en a vu les questions.

Les scores montent ensuite très vite. Au début de 2026, les meilleurs modèles
résolvent environ la moitié des problèmes ordinaires et plus du tiers des plus
difficiles, et à l'automne 2026, Epoch AI juge le niveau le plus difficile presque
épuisé.

## Vers la recherche

Le passage aux vrais problèmes de recherche a commencé par un faux départ. En
octobre 2025, un dirigeant d'OpenAI annonce que GPT-5 a résolu dix problèmes ouverts
posés par Paul Erdős, l'un des mathématiciens les plus prolifiques du XXᵉ siècle. Le
responsable du site qui recense ces problèmes répond qu'ils étaient déjà résolus dans
la littérature : le modèle avait retrouvé des solutions existantes, sans les créer. Ce
genre de **redécouverte** reste fréquent, et il faut le distinguer d'un résultat
nouveau. Les cas suivants sont, eux, des résultats nouveaux, vérifiés par des
mathématiciens.

- **Un problème d'Erdős, en janvier 2026.** Deux amateurs soumettent un problème encore
  ouvert à un modèle d'OpenAI, qui le résout ; sa démonstration est vérifiée en Lean.
  Terence Tao confirme qu'il s'agit d'une résolution autonome d'un problème que
  personne n'avait résolu.
- **Une conjecture réfutée, en mai 2026.** Un modèle d'OpenAI réfute une conjecture
  d'Erdős de 1946 sur le nombre de paires de points à distance un dans le plan. Sa
  démonstration, produite d'un seul coup selon ses auteurs, est vérifiée et
  simplifiée par un groupe de mathématiciens de premier plan, dont Noga Alon et
  Timothy Gowers.
- **Un contre-exemple, en juillet 2026.** Avec un modèle d'Anthropic, un chercheur
  trouve un contre-exemple à la conjecture jacobienne, posée en 1939, en dimension
  trois et plus. Le contre-exemple est une formule explicite, que chacun peut
  vérifier, et Terence Tao en publie aussitôt une analyse.
- **Le théorème de Fermat, en Lean, en septembre 2026.** Des dizaines d'agents
  d'Anthropic écrivent en onze jours la première démonstration complète en Lean du
  dernier théorème de Fermat, démontré par Andrew Wiles en 1994 : treize millions de
  lignes, vérifiées par Lean et examinées par Kevin Buzzard, qui dirige depuis 2024 un
  projet humain dans le même but. Ce n'est pas un résultat
  nouveau, mais la vérification complète d'une démonstration célèbre.

Les mathématiciens ont aussi construit leurs propres tests. En février 2026, onze
d'entre eux, dont le médaillé Fields Martin Hairer, publient **First Proof**, dix
lemmes tirés de leurs travaux en cours, dont les réponses restent secrètes une
semaine. Les modèles rédigent des démonstrations assurées pour les dix, mais selon les
organisateurs, deux seulement sont clairement justes, dont l'une figurait déjà dans la
littérature. Les résultats sont donc réels, mais inégaux, et souvent difficiles à
évaluer.

## Ce que cela dit, et ce que cela ne dit pas

En 2023, Terence Tao prédisait que l'IA de 2026, bien utilisée, serait un co-auteur
digne de confiance en recherche mathématique. Trois ans plus tard, il la décrit comme
un assistant qui fait gagner plus de temps qu'il n'en fait perdre, mais pas encore
comme un pair. Ses usages sont désormais réels : chercher dans la littérature, essayer
des pistes, vérifier des calculs, traduire une démonstration en Lean.

Ces progrès inquiètent aussi. En septembre 2026, vingt-cinq médaillés Fields, dont
Peter Scholze et Maryna Viazovska, signent une déclaration publiée par Terence Tao,
« *A Severe Misalignment of AI in Mathematics* ». Pour eux, résoudre des problèmes
n'est qu'un moyen, et un indicateur, au service de ce qui compte vraiment en
mathématiques, la compréhension. Une machine qui produit des démonstrations sans
expliquer pourquoi elles marchent ne fait pas avancer cette compréhension, et les
entreprises qui la conçoivent poursuivent d'autres buts que les mathématiciens.

Pour juger un résultat annoncé, trois niveaux de confiance se distinguent :

- une démonstration **vérifiée par Lean** est juste, pourvu que l'énoncé ait été bien
  traduit ;
- un résultat **vérifié par des mathématiciens**, comme la conjecture réfutée et le
  contre-exemple de 2026, est aussi solide que les autres résultats publiés ;
- une **annonce d'entreprise**, non vérifiée, reste une annonce, comme l'a montré le
  faux départ de 2025.

Restent les questions de fond. Le Module 1 présentait, dans
« [L'ombre de Gödel](docs/module1/10-turing/#lombre-de-gödel) », la lecture du
physicien Roger Penrose : selon lui, l'esprit humain voit des vérités mathématiques
qu'aucun système formel ne peut atteindre, et une machine ne fera donc jamais de
vraies mathématiques. Des machines qui démontrent des théorèmes inédits donnent à ce
débat une matière nouvelle, sans le trancher. Le [Module 5](docs/module5/22-penser-est-ce-calculer) le reprend.

Le [chapitre suivant](docs/module4/88-le-defi-arc) présente un test conçu pour
mesurer autre chose que la maîtrise de problèmes connus : la capacité à faire face à
du nouveau.
