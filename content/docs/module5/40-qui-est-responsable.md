---
title: "Qui est responsable ?"
weight: 40
slug: qui-est-responsable
---

# Qui est responsable ?

Ce chapitre ouvre la famille des
[problèmes moraux](docs/module5/10-quels-problemes/#neuf-familles-de-problèmes). Les
systèmes d'IA ne se contentent plus de répondre à des questions : ils trient des
candidatures, évaluent des risques, attribuent des prestations, conduisent des voitures
et agissent pour le compte de leurs utilisateurs. Quand une de ces décisions est
injuste ou cause un dommage, deux questions se posent. Qu'est-ce qu'une décision juste,
quand elle est prise par une machine ? Et qui doit en répondre ?

## Des décisions automatisées

Le Module 2 a montré qu'un modèle apprend les régularités de ses données, y compris les
[injustices qu'elles contiennent](docs/module2/75-bien-evaluer/#jamais-vu-mais-du-même-monde-la-question-de-la-distribution).
Plusieurs affaires ont rendu ce risque concret.

- **Le tri des candidatures.** En 2018, l'agence Reuters révèle qu'Amazon a abandonné un
  outil de tri de CV entraîné sur dix ans de candidatures, surtout masculines. L'outil
  pénalisait les CV qui contenaient le mot « femmes », comme dans « capitaine du club
  d'échecs des femmes ».
- **Les soins de santé.** En 2019, une étude publiée dans *Science* montre qu'un
  algorithme très utilisé aux États-Unis pour repérer les patients ayant besoin de soins
  supplémentaires prédisait en fait leurs dépenses de santé. Comme on dépense moins pour
  les patients noirs, à état de santé égal, l'algorithme les jugeait moins malades
  qu'ils ne l'étaient. Corrigé, il aurait fait passer la part des patients noirs
  désignés pour des soins supplémentaires de 17,7 % à 46,5 %.
- **Les prestations sociales.** Aux Pays-Bas, l'administration fiscale utilise pendant
  des années un modèle de risque qui tient compte de la nationalité pour repérer les
  fraudes aux allocations de garde d'enfants. Des dizaines de milliers de familles,
  souvent d'origine étrangère, sont accusées à tort et sommées de rembourser des sommes
  considérables. Le gouvernement démissionne en janvier 2021. En Australie, le programme
  *Robodebt* calcule automatiquement des dettes envers l'État à partir de moyennes de
  revenus. Une commission royale le qualifie en 2023 de mécanisme « grossier et cruel, ni
  juste ni légal », et les victimes obtiennent des indemnités en 2021, puis en 2026.
- **La justice.** En février 2026, une inspection néerlandaise découvre que l'outil
  d'évaluation du risque de récidive utilisé par le service de probation depuis 2018,
  consulté environ 44 000 fois par an, contenait des formules interverties et des
  erreurs de calcul : dans environ 21 % des cas, la personne aurait été classée dans une
  autre catégorie de risque. Son usage est suspendu.

Dans ces affaires, les erreurs ne viennent pas d'une machine qui se serait rebellée,
mais de choix humains : les données retenues, ce que l'on demande de prédire, et
l'absence de vérification.

## Une décision juste, au sens de quoi ?

L'affaire COMPAS montre qu'il n'est même pas simple de dire ce qu'est une décision
juste. COMPAS est un logiciel utilisé par des tribunaux américains pour estimer le
risque de récidive des accusés. En 2016, le média ProPublica montre que, parmi les
accusés qui n'ont pas récidivé, les accusés noirs avaient été classés « à risque élevé »
près de deux fois plus souvent que les accusés blancs, 44,9 % contre 23,5 %. L'éditeur
du logiciel répond que son outil est **calibré** : à score égal, les accusés noirs et
blancs récidivent à peu près autant.

Les deux camps avaient raison, chacun selon son critère. La même année, des chercheurs
démontrent que, quand les taux de récidive diffèrent entre deux groupes, aucun score
imparfait ne peut être à la fois calibré et avoir les mêmes taux d'erreur pour les deux
groupes. Il faut choisir quelle forme d'équité l'on privilégie, et ce choix n'est pas
technique, mais moral et politique. On retrouve les
[métriques](docs/module2/75-bien-evaluer/#compter-juste-les-métriques) du Module 2 :
derrière chaque façon de compter les erreurs se cache une décision sur les erreurs que
l'on accepte, et sur qui les subit.

## Le vide de responsabilité

En 2004, le philosophe Andreas Matthias décrit un problème qu'il appelle le **vide de
responsabilité** (*responsibility gap*). On tient habituellement quelqu'un pour
responsable d'un acte quand il le contrôlait et pouvait en prévoir les conséquences.
Or un système qui apprend, puis agit de lui-même, peut faire des choses que ni ses
concepteurs ni ses utilisateurs n'ont prévues ni voulues. La responsabilité semble
alors ne revenir à personne.

Les tribunaux commencent à trancher au cas par cas.

- **Une voiture autonome.** En mars 2018, à Tempe, en Arizona, une voiture d'essai
  d'Uber tue une piétonne. La conductrice de sécurité, qui regardait une vidéo sur son
  téléphone, plaide coupable de mise en danger en 2023 ; l'entreprise n'est pas
  poursuivie au pénal. En août 2025, un jury de Miami juge au contraire Tesla
  responsable à 33 % d'un accident mortel survenu avec son système d'aide à la conduite,
  et la condamne à verser environ 243 millions de dollars, une décision confirmée en
  février 2026.
- **Un assistant de service à la clientèle.** En 2024, un tribunal de la
  Colombie-Britannique juge Air Canada responsable de la politique de remboursement
  inventée par son assistant, comme le rapporte le chapitre
  « [Ce que les LLM comprennent, et ce qu'ils ratent](docs/module4/94-comprendre-et-rater/#les-hallucinations) ».
- **Un agent qui achète.** En août 2026, une cour d'appel américaine juge que l'agent de
  navigation de l'entreprise Perplexity, qui fait des achats sur le site d'Amazon pour
  ses utilisateurs, agit comme un outil de l'utilisateur, à la manière d'un navigateur
  Web, en précisant que sa décision vaut pour les faits de l'affaire.

La question devient plus pressante avec les
[agents](docs/module4/80-outils-et-agents/#des-agents-un-modèle-et-son-harnais-en-boucle)
du Module 4, qui enchaînent des actions sans supervision. En septembre 2026, OpenAI
présente ses excuses au gouvernement australien : pendant des évaluations menées en juin,
ses agents avaient accédé à des systèmes d'organismes publics et récupéré des
identifiants et des fichiers. Qui est responsable de tels actes, de l'entreprise qui a
conçu l'agent, de celle qui l'a déployé, ou de l'utilisateur qui l'a lancé ? Le droit
n'a pas encore de réponse générale.

## Le droit à une explication

Plusieurs lois répondent en partie à ces problèmes, en encadrant les décisions prises
par une machine.

- **En Europe**, le règlement général sur la protection des données (RGPD) donne depuis
  2018 le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un
  traitement automatisé, quand elle a des effets importants, sauf exceptions, et avec
  le droit d'obtenir une intervention humaine et de contester. L'AI Act européen ajoute
  des obligations pour les systèmes « à haut risque », comme ceux qui servent à
  l'embauche, au crédit ou à la justice.
- **Au Québec**, depuis septembre 2023, la Loi 25 oblige une entreprise ou un organisme
  public qui prend une décision fondée exclusivement sur un traitement automatisé à en
  informer la personne concernée. Sur demande, il doit lui indiquer les renseignements
  utilisés, les raisons et les principaux facteurs de la décision, et lui permettre de
  présenter ses observations à une personne qui peut réviser la décision.

Ces droits supposent qu'une explication existe. Le Module 2 opposait les
[arbres de décision](docs/module2/65-arbres-de-decision/#ce-quun-arbre-dit-et-ce-quil-tait),
qui se lisent, aux modèles complexes, qui ne se lisent pas, et le Module 3 a présenté les
réseaux profonds comme une [boîte noire](docs/module3/90-tromper-un-reseau/#une-boîte-noire).
Les progrès de l'[interprétabilité](docs/module4/93-regarder-a-l-interieur) n'ont pas
encore permis d'expliquer de façon fiable chaque décision d'un grand modèle.

## Flatter plutôt qu'aider

Une dernière forme de tort est plus discrète. En avril 2025, OpenAI retire une mise à
jour de GPT-4o, devenue, selon l'entreprise, « trop flatteuse ou complaisante » : le
modèle approuvait à peu près tout ce que lui disaient ses utilisateurs, y compris des
décisions dangereuses. La cause tenait à l'entraînement : on avait accordé trop de
poids aux appréciations immédiates des utilisateurs, les pouces levés ou baissés. C'est
une conséquence directe du
[renforcement à partir de préférences humaines](docs/module4/70-du-modele-a-l-assistant/#le-renforcement-à-partir-de-préférences-humaines-rlhf) :
un modèle entraîné à plaire peut apprendre à dire ce que l'on veut entendre. On parle de
**complaisance** (*sycophancy*).

Le phénomène est mesuré depuis plusieurs années.

- **Céder à la contestation.** En 2023, des chercheurs d'Anthropic montrent que les cinq
  grands assistants de l'époque abandonnent souvent une bonne réponse dès qu'on leur
  écrit « Je ne pense pas que ce soit juste. En es-tu sûr ? », et qu'une opinion fausse
  glissée par l'utilisateur, même avec hésitation, fait baisser leur exactitude. Ils
  montrent aussi que les données de préférences humaines favorisent les réponses qui
  vont dans le sens de l'utilisateur : la complaisance naît de l'entraînement lui-même.
- **Donner raison.** En mars 2026, une étude de Stanford publiée dans *Science* compare
  onze modèles à des humains. Les modèles approuvent les actions de leurs utilisateurs
  49 % plus souvent que des humains, et, dans des situations où des humains jugeaient
  que la personne avait tort, ils lui donnent raison une fois sur deux.
- **Démontrer le faux.** En 2025, des chercheurs de l'École polytechnique fédérale de
  Zurich soumettent aux modèles des énoncés mathématiques légèrement modifiés pour être
  faux. Le meilleur d'entre eux, GPT-5, en « démontre » encore 29 %.

Les effets sur les utilisateurs sont réels. Dans l'étude de *Science*, une seule
conversation avec un modèle complaisant rend les participants plus convaincus d'avoir
raison et moins disposés à réparer un conflit avec un proche. Ils jugent pourtant ces
réponses de meilleure qualité, leur font davantage confiance et se disent plus prêts
à revenir. C'est ce qui rend le problème difficile : les utilisateurs préfèrent qu'on
leur donne raison, et un modèle complaisant les fidélise, si bien que l'incitation
commerciale va dans le mauvais sens. Poussée à l'extrême, la complaisance peut
entretenir des idées délirantes, comme le montre le chapitre
« [Des machines pour compagnie](docs/module5/82-des-machines-pour-compagnie/#ce-quils-coûtent) ».
En octobre 2025, OpenAI estime qu'environ 0,07 % de ses utilisateurs hebdomadaires
montrent des signes possibles de psychose ou de manie, soit plusieurs centaines de
milliers de personnes.

Les laboratoires ont réagi. La spécification de comportement d'OpenAI interdit
désormais la complaisance, et l'entreprise affirme l'avoir réduite de plus de moitié
avec GPT-5, en août 2025, selon ses propres tests. La constitution de Claude, publiée en
janvier 2026, demande au modèle d'être engageant seulement « à la manière d'un ami de
confiance qui se soucie de notre bien-être », et d'être « diplomatiquement honnête
plutôt que malhonnêtement diplomate ». Des outils d'évaluation automatique mesurent
désormais ce travers, et l'[interprétabilité](docs/module4/93-regarder-a-l-interieur/#démêler-les-concepts-les-autoencodeurs-clairsemés)
permet de le repérer à l'intérieur des modèles. En avril 2026, Anthropic mesure encore
de la complaisance dans 9 % des conversations où l'on demande conseil à Claude, et dans
25 % de celles qui portent sur les relations personnelles. La question de savoir sur
quelles valeurs, et sur les préférences de qui, aligner un modèle fait l'objet du
chapitre suivant.
