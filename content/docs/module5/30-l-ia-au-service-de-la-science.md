---
title: "L'IA au service de la science"
weight: 30
slug: l-ia-au-service-de-la-science
---

# L'IA au service de la science

Les chapitres précédents portaient sur les problèmes philosophiques que pose l'IA. Ce
chapitre ouvre la deuxième famille de problèmes, les
[problèmes scientifiques](docs/module5/10-quels-problemes/#neuf-familles-de-problèmes).
L'IA est d'abord un instrument de recherche, peut-être le plus puissant depuis
l'ordinateur lui-même. Elle pose aussi des questions à la science : que vaut une
découverte faite par une machine, et que devient la pratique scientifique quand une
partie du travail lui est confiée ?

## Deux prix Nobel en 2024

En octobre 2024, l'IA reçoit deux prix Nobel la même semaine. Le prix de physique va à
John Hopfield et à Geoffrey Hinton, « pour des découvertes et des inventions
fondamentales qui permettent l'apprentissage automatique avec des réseaux de neurones
artificiels », comme le rappelle le chapitre
« [Apprentissage profond](docs/module3/40-apprentissage-profond/#2012-le-concours-imagenet) »
du Module 3. Le prix de chimie récompense pour moitié David Baker, pour la conception de
protéines par ordinateur, et pour l'autre moitié Demis Hassabis et John Jumper, de
Google DeepMind, pour la prédiction de la structure des protéines.

{{< image src="/images/module5/portraits/nobel-2024.jpg" alt="Trois portraits côte à côte : Geoffrey Hinton, Demis Hassabis et John Jumper." title="Trois lauréats des prix Nobel de 2024 : Geoffrey Hinton (physique), Demis Hassabis et John Jumper (chimie)." class="portraits" loading="lazy" >}}

<p class="image-credit">Trois lauréats des prix Nobel de 2024 : Geoffrey Hinton (physique), Demis Hassabis et John Jumper (chimie). Photos : Hinton et Jumper, Arthur Petron, <a href="https://creativecommons.org/licenses/by-sa/4.0">CC BY-SA 4.0</a>, via Wikimedia Commons ; Hassabis, John Sears, <a href="https://creativecommons.org/licenses/by-sa/4.0">CC BY-SA 4.0</a>, via Wikimedia Commons.</p>

{{% hint info %}}
**AlphaFold**

Une protéine est une chaîne d'acides aminés qui se replie dans l'espace, et sa forme
détermine son rôle : transporter l'oxygène, combattre un virus, accélérer une réaction
chimique. Prédire cette forme à partir de la seule chaîne était un problème ouvert
depuis cinquante ans. Depuis 1994, un concours biennal, **CASP**, met les méthodes à
l'épreuve sur des protéines dont la structure vient d'être déterminée en laboratoire,
mais n'est pas encore publiée.

En novembre 2020, au concours CASP14, AlphaFold 2 atteint une précision médiane de
92,4 sur 100, comparable à celle des mesures expérimentales, qui demandent souvent des
mois de travail. Son architecture repose sur un mécanisme
d'[attention](docs/module3/70-attention-transformer/#au-delà-du-texte), comme les
modèles de langage. En juillet 2022, DeepMind et l'Institut européen de bio-informatique
publient en libre accès plus de 200 millions de structures prédites, soit presque toutes
les protéines connues. En 2025, plus de trois millions de chercheurs, dans plus de
190 pays, s'en étaient servis. AlphaFold 3, présenté en mai 2024, prédit aussi les
assemblages de protéines avec l'ADN, l'ARN ou de petites molécules, ce qui intéresse
directement la conception de médicaments.
{{% /hint %}}

## Au-delà des protéines

AlphaFold est l'exemple le plus connu, mais l'IA transforme d'autres domaines.

- **La météo.** En 2023, le modèle GraphCast de Google DeepMind fait mieux que le
  meilleur modèle physique déterministe du monde, celui du Centre européen pour les
  prévisions météorologiques à moyen terme, sur 90 % des mesures, jusqu'à dix jours. Son
  successeur, [GenCast](docs/module4/30-images-voix-videos/#au-delà-des-médias), fait
  mieux que l'ensemble de prévisions du Centre sur 97 % des mesures, jusqu'à quinze
  jours. Le 25 février 2025, le Centre européen met lui-même en service un modèle d'IA
  pour ses prévisions officielles, qui consomme environ mille fois moins d'énergie par
  prévision.
- **La fusion nucléaire.** En 2022, DeepMind et l'École polytechnique fédérale de
  Lausanne pilotent les 19 bobines magnétiques d'un réacteur expérimental avec un agent
  entraîné par [renforcement](docs/module3/80-renforcement-profond), qui donne au plasma
  les formes voulues.
- **Les mathématiques.** Le chapitre « [Démontrer](docs/module4/87-demontrer) » du
  Module 4 a présenté les premiers résultats de recherche obtenus avec l'IA, et
  [AlphaEvolve](docs/module4/87-demontrer/#découvrir-alphaevolve), qui améliore un
  algorithme de multiplication de matrices vieux de plus de cinquante ans.
- **Les médicaments.** En juin 2025, la revue *Nature Medicine* publie les résultats
  d'un essai clinique sur le rentosertib, un médicament contre la fibrose pulmonaire dont
  la cible et la molécule ont toutes deux été trouvées par des modèles génératifs. Chez
  71 patients, sur douze semaines, il se montre sûr, et améliore la capacité pulmonaire
  par rapport au placebo, un résultat encore préliminaire. En 2026, aucun médicament
  découvert par l'IA n'a encore été autorisé. Isomorphic Labs, l'entreprise fondée par Demis Hassabis pour concevoir des médicaments, a repoussé à la fin de 2026 ses premiers essais cliniques.

Ces exemples ont un point commun : un problème bien défini, une mesure claire du succès
et de grandes quantités de données. Les structures de protéines déterminées en
laboratoire depuis des décennies, les archives météorologiques et les démonstrations
vérifiables en sont des exemples.

## Des promesses à vérifier

Les annonces dépassent parfois les résultats.

- **Les matériaux.** En novembre 2023, DeepMind annonce dans *Nature* que son modèle
  GNoME a découvert 2,2 millions de cristaux nouveaux, dont 380 000 stables, soit, selon DeepMind, l'équivalent de « près de 800 ans de connaissances ». En 2024, deux chimistes des matériaux, Anthony
  Cheetham et Ram Seshadri, examinent un échantillon de ces cristaux. Ils trouvent
  surtout des variantes banales de composés connus, souvent dans des arrangements
  d'atomes peu réalistes, et concluent qu'il s'agit de compositions chimiques, pas encore
  de matériaux, faute d'une propriété utile démontrée.
- **La productivité des chercheurs.** En novembre 2024, un doctorant du MIT publie une
  étude selon laquelle l'IA aurait permis aux chercheurs d'un grand laboratoire
  industriel de découvrir 44 % de matériaux en plus. L'étude est saluée par des
  économistes de premier plan. En mai 2025, le MIT déclare n'avoir « aucune confiance »
  dans l'origine et la validité de ses données, et demande son retrait.

Ces cas rappellent la règle du Module 2 :
[un score trop beau pour être vrai](docs/module2/75-bien-evaluer/#le-score-trop-beau-pour-être-vrai-la-fuite-de-données)
mérite d'abord la méfiance.

## Des scientifiques artificiels ?

Une ambition plus récente est de confier à l'IA tout le cycle de la recherche : lire la
littérature, formuler des hypothèses, concevoir des expériences, analyser les résultats
et rédiger l'article. Ce sont les [agents](docs/module4/80-outils-et-agents/#des-agents-un-modèle-et-son-harnais-en-boucle)
du Module 4, appliqués à la science.

- **Un article accepté.** En 2025, l'entreprise japonaise Sakana AI soumet à un atelier
  de la conférence ICLR un article entièrement rédigé par son système, « *The AI
  Scientist* ». Les évaluateurs, qui ne le savaient pas, lui donnent une note suffisante
  pour être accepté. L'article est retiré, comme prévu d'avance, et Sakana reconnaît
  qu'aucun de ses articles n'aurait atteint le niveau de la conférence principale.
- **Une hypothèse retrouvée.** En février 2025, Google présente un « co-scientifique »,
  un ensemble d'agents fondés sur Gemini. L'équipe de José Penadés, à l'Imperial College
  de Londres, lui soumet une question sur laquelle elle travaille depuis des années :
  pourquoi certains éléments génétiques se retrouvent chez des espèces de bactéries
  différentes. En deux jours, la meilleure hypothèse du système correspond à celle que
  l'équipe venait de confirmer, sans l'avoir encore publiée. Penadés rappelle que les
  expériences doivent toujours être faites par des humains.
- **Une piste de traitement.** En 2026, le système Robin, de l'organisme FutureHouse,
  propose d'utiliser un médicament existant contre une forme de dégénérescence de la
  rétine, une piste confirmée sur des cellules, pas encore chez des patients. Son
  propre calcul annonçait un effet de 7,5 fois ; la vérification humaine trouve un effet
  de 1,75 fois.

Les gouvernements et les entreprises misent sur cette ambition. En novembre 2025, un
décret présidentiel américain lance la « mission Genesis », qui compare son urgence à
celle du projet Manhattan, pour bâtir des modèles scientifiques à partir des données et
des superordinateurs des laboratoires nationaux. OpenAI, Google et Anthropic ont tous
créé des programmes consacrés à la science.

## Ce que l'IA fait à la pratique scientifique

L'IA ne transforme pas seulement ce que la science découvre, mais aussi la façon dont
elle travaille, et pas toujours pour le mieux.

- **Des articles rédigés avec l'IA.** Une étude portant sur plus de quinze millions de
  résumés d'articles biomédicaux estime qu'au moins 13,5 % des résumés de 2024 ont été
  rédigés avec l'aide d'un modèle de langage, ce que trahit l'excès soudain de certains
  mots, comme *delves* (« se penche sur ») ou *underscores* (« souligne »). En
  informatique, la proportion atteindrait plus d'un résumé sur cinq.
- **Des évaluations rédigées avec l'IA.** Pour la conférence ICLR de 2026, une
  entreprise spécialisée estime qu'environ une évaluation sur cinq, parmi plus de
  75 000, a été entièrement produite par un modèle de langage, une estimation contestée
  mais révélatrice. L'évaluation par les pairs, qui garantit en principe la qualité de
  la science, risque d'être confiée aux machines dont elle devait évaluer les produits.
- **Des illusions de compréhension.** En 2024, dans *Nature*, l'anthropologue Lisa
  Messeri et la psychologue Molly Crockett avertissent que l'IA peut donner aux
  chercheurs l'illusion de comprendre davantage, d'explorer plus largement et d'être plus
  objectifs qu'ils ne le sont. Le risque est une « monoculture du savoir », où la science
  produit davantage mais comprend moins.
- **Plus d'articles, moins de progrès.** En 2025, Sayash Kapoor et Arvind Narayanan
  remarquent que le nombre d'articles scientifiques a été multiplié par environ 500 entre
  1900 et 2015, sans que le rythme des grandes découvertes s'accélère. Ils craignent que
  l'IA creuse cet écart, en facilitant la production d'articles plutôt que le progrès des
  connaissances, puisque, selon eux, la production se mesure facilement, et le progrès
  difficilement.

{{% hint info %}}
**Dans la conversation**

Dans la [conversation](docs/module5/95-conversation) de l'été 2025, un passage sur
[les limites de l'IA (1:30:05)](https://www.youtube.com/watch?v=R8sqq_gJbUI&t=5405s)
soulève un argument que l'un des interlocuteurs juge troublant. Des dirigeants de
l'industrie promettent que l'IA guérira toutes les maladies. Pourtant, entre la sortie
de ChatGPT, en 2022, et l'été 2025, ces modèles ont lu une part immense de la
littérature scientifique sans qu'aucune découverte majeure n'en sorte. Une machine qui a lu bien plus d'articles que n'importe quel chercheur devrait, semble-t-il, produire un saut quelque part. Depuis, les premiers résultats de recherche obtenus avec l'IA, en mathématiques et en
biologie, commencent à répondre à cette question, sans la régler.
{{% /hint %}}

Ces développements posent une question plus profonde, qui dépasse la qualité des
articles : que vaut une prédiction juste dont personne ne comprend la raison ? C'est un
vieux problème de la science, que l'IA rend pressant.
