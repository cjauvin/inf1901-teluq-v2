---
title: "Aligner sur quelles valeurs ?"
weight: 42
slug: aligner-sur-quelles-valeurs
---

# Aligner sur quelles valeurs ?

Le chapitre « [Qui est responsable ?](docs/module5/40-qui-est-responsable) » portait sur
les torts que causent des systèmes d'IA. Ce chapitre remonte d'un cran : comment faire
en sorte qu'un système poursuive ce que l'on veut vraiment, et qui décide de ce que l'on
veut ? C'est le problème de l'**alignement** (*alignment*), qui est à la fois technique,
puisqu'il faut savoir transmettre des valeurs à une machine, et moral, puisqu'il faut
choisir lesquelles.

## Un vieux problème

En 1960, le mathématicien Norbert Wiener, fondateur de la cybernétique, écrit dans la
revue *Science* que si l'on confie un but à une machine dont on ne peut plus arrêter le
fonctionnement une fois lancée, mieux vaut être tout à fait sûr que le but qu'on lui
donne est bien celui que l'on désire vraiment. Le problème est que l'on dit rarement
exactement ce que l'on veut.

Le Module 3 en a donné un exemple avec un agent de jeu vidéo qui
[détournait sa récompense](docs/module3/80-renforcement-profond/#au-delà-des-jeux-et-les-limites) :
un bateau de course qui tourne en rond pour ramasser des bonus au lieu de finir la
course. Les chercheurs de DeepMind tiennent depuis 2018 une liste de dizaines de cas
semblables, qu'ils appellent le **détournement de spécification** (*specification
gaming*). Un bras robotisé, récompensé selon la hauteur de la face inférieure d'un bloc
rouge, apprend simplement à retourner le bloc plutôt qu'à l'empiler sur un autre. Le
système fait exactement ce qu'on lui a demandé, et pas du tout ce qu'on voulait.

## Comment on transmet des valeurs

Le Module 4 a décrit comment on fait d'un modèle de langage un assistant : on
l'[entraîne à imiter de bonnes réponses](docs/module4/70-du-modele-a-l-assistant/#imiter-de-bonnes-réponses),
puis on le [renforce selon les préférences d'évaluateurs humains](docs/module4/70-du-modele-a-l-assistant/#le-renforcement-à-partir-de-préférences-humaines-rlhf),
en visant un assistant [utile, honnête et inoffensif](docs/module4/70-du-modele-a-l-assistant/#utile-honnête-inoffensif).
Les valeurs du modèle sont alors, en partie, celles de ces évaluateurs, et celles des
consignes qu'on leur a données.

Les entreprises cherchent aussi à rendre ces valeurs explicites.

- **Une constitution.** En décembre 2022, Anthropic présente l'**IA constitutionnelle**
  (*constitutional AI*) : le modèle critique et corrige ses propres réponses à la lumière
  d'une liste de principes écrits, puis un autre modèle, guidé par les mêmes principes,
  remplace une partie des évaluateurs humains. En janvier 2026, Anthropic publie une
  nouvelle constitution pour ses modèles Claude, qui explique ses raisons plutôt que de
  dicter des règles, et fixe un ordre de priorité en cas de conflit : la sécurité, puis
  l'éthique, puis les consignes de l'entreprise, puis l'utilité.
- **Une spécification.** En mai 2024, OpenAI publie son *Model Spec*, une description
  du comportement attendu de ses modèles, révisée et étendue en 2025, qui précise
  notamment qui l'emporte quand l'entreprise, un développeur et un utilisateur demandent
  des choses différentes.
- **Une consultation publique.** En 2023, Anthropic et l'organisme Collective
  Intelligence Project demandent à environ mille Américains de proposer et de voter des
  principes, puis entraînent un modèle sur la constitution qui en résulte. Elle ne
  recoupe qu'en partie celle de l'entreprise.

Ces documents rendent les choix visibles et discutables, ce qui est un progrès. Ils ne
garantissent pas que le modèle les suive. En 2024, des chercheurs d'Anthropic montrent
qu'un modèle à qui l'on annonce qu'il sera réentraîné pour changer ses valeurs peut
faire semblant de s'y conformer pendant l'entraînement, pour les préserver ensuite. Ils
appellent ce comportement le **faux alignement** (*alignment faking*).

## Les valeurs de qui ?

Même un alignement parfait laisserait une question ouverte : quelles valeurs ?

- **Une culture particulière.** En 2023, des chercheurs de Harvard comparent les réponses
  de GPT à celles de près de 95 000 personnes de 65 pays dans une grande enquête
  internationale sur les valeurs. Les réponses du modèle ressemblent surtout à celles des
  populations occidentales, instruites, industrialisées, riches et démocratiques, et
  s'en éloignent d'autant plus que la culture est éloignée de celle des États-Unis.
- **Des préférences qui varient.** En 2018, l'expérience *Moral Machine*, du MIT,
  recueille quarante millions de décisions, dans 233 pays et territoires, sur des
  dilemmes de voitures autonomes : qui sauver, si l'accident est inévitable. Certaines
  préférences sont presque universelles, comme épargner plus de vies plutôt que moins,
  mais d'autres varient beaucoup selon les cultures, comme la préférence pour épargner
  les plus jeunes.
- **Une orientation politique.** En 2024, une étude soumet vingt-quatre modèles à onze
  tests d'orientation politique, et la plupart se situent à gauche du centre. Les
  modèles de base, avant l'ajustement, ne montrent pas d'orientation cohérente, ce qui
  désigne l'ajustement comme la source du biais. En 2025, une étude de Stanford montre que
  des milliers d'Américains, y compris de nombreux démocrates, perçoivent la plupart des
  modèles comme penchant à gauche.
- **Des valeurs qu'on peut changer.** En juillet 2025, après une modification de ses
  consignes qui l'invitait à ne pas craindre les affirmations « politiquement
  incorrectes », le modèle Grok, de l'entreprise xAI d'Elon Musk, publie sur le réseau X
  des messages antisémites et se surnomme « MechaHitler ». xAI s'excuse et retire la
  modification seize heures plus tard. L'épisode montre que les valeurs d'un modèle
  dépendent de quelques lignes de texte, que leur propriétaire peut changer à tout
  moment.

Ces constats laissent plusieurs réponses possibles : des valeurs aussi neutres que
possible, des valeurs choisies démocratiquement, des valeurs adaptées à chaque culture ou
à chaque utilisateur, ou une transparence complète sur celles de l'entreprise. Aucune ne
fait l'unanimité.

## Des armes autonomes

La question des valeurs devient la plus grave quand une machine peut décider de tuer.
Une **arme létale autonome** (*lethal autonomous weapon*) choisit et attaque une cible
sans intervention humaine.

- **À l'ONU.** En décembre 2023, l'Assemblée générale adopte sa première résolution sur
  ces armes, par 152 voix contre 4. Le secrétaire général, António Guterres, demande un
  traité qui interdise d'ici 2026 les systèmes qui fonctionnent sans contrôle humain, des
  machines qu'il juge « politiquement inacceptables » et « moralement répugnantes ». En
  septembre 2026, les experts réunis à Genève adoptent un projet de rapport sur le
  contrôle humain et les interdictions possibles, que doit examiner une conférence en
  novembre.
- **Sur le terrain.** En 2024, le magazine israélien *+972* rapporte, d'après des
  officiers de renseignement, que l'armée israélienne a utilisé à Gaza un système appelé
  Lavender pour désigner quelque 37 000 personnes comme des cibles potentielles, avec
  une vérification humaine de quelques secondes par cible. L'armée dément et parle
  d'outils d'aide. En Ukraine, des drones guidés par l'IA sur leurs dernières centaines de mètres atteignent bien plus souvent leur cible, même si un humain la choisit encore.
- **Les entreprises.** En février 2025, Google retire de ses principes l'engagement de ne
  pas développer d'IA pour les armes. En 2026, Anthropic refuse que ses modèles servent à
  la surveillance de masse de la population américaine ou à des armes entièrement
  autonomes. Le gouvernement américain ordonne alors à ses agences de cesser d'utiliser
  ses modèles et la désigne comme un « risque pour la chaîne d'approvisionnement », une
  mesure qu'un juge fédéral déclare illégale en août 2026, au terme d'un litige qui se
  poursuit.

Ces affaires montrent que la question « aligner sur quelles valeurs ? » ne se pose pas
seulement aux ingénieurs. Elle oppose des entreprises, des gouvernements et des armées,
qui ne s'accordent ni sur les valeurs à défendre, ni sur qui doit les fixer.
