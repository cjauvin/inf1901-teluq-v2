---
title: "Peut-on perdre le contrôle ?"
weight: 85
slug: peut-on-perdre-le-controle
---

# Peut-on perdre le contrôle ?

Le dernier problème du module est le plus spéculatif et le plus grave. C'est la famille
des [risques extrêmes](docs/module5/10-quels-problemes/#neuf-familles-de-problèmes) : la
possibilité que l'IA cause une catastrophe à l'échelle de l'humanité, parce qu'on en
perdrait le contrôle ou parce que quelqu'un s'en servirait pour nuire massivement. Pour
certains chercheurs, c'est le risque le plus important de notre époque. Pour d'autres,
c'est de la science-fiction, qui détourne l'attention des torts bien réels décrits dans
les chapitres précédents.

## Une explosion d'intelligence

L'idée est ancienne. En 1965, le mathématicien britannique I. J. Good, qui avait travaillé
avec Turing à Bletchley Park, imagine une machine « ultra-intelligente », capable de
concevoir des machines meilleures qu'elle. Il en résulterait, écrit-il, une **explosion
d'intelligence**, et la première machine de ce genre serait la dernière invention dont
l'humanité aurait besoin, « pourvu que la machine soit assez docile pour nous dire comment
la garder sous contrôle ». La fin de la phrase est souvent oubliée. C'est pourtant tout
le problème.

L'idée de cette boucle d'amélioration revient aujourd'hui sous une forme concrète : les
[agents de programmation](docs/module4/85-programmer-avec-des-agents) du Module 4 écrivent
déjà une partie du code des modèles suivants.

{{% hint info %}}
**Le maximiseur de trombones**

En 2003, le philosophe Nick Bostrom imagine une superintelligence dont le but est de
fabriquer des trombones. Rien de plus inoffensif en apparence. Mais un système assez
puissant, poursuivant ce seul but sans autre limite, pourrait transformer la Terre, puis
une partie croissante de l'espace, en usines de trombones, en utilisant au passage toute
la matière disponible, y compris celle dont nous sommes faits. L'exemple est volontairement
absurde. Il illustre deux idées que Bostrom développe en 2014 dans *Superintelligence*.

- **L'orthogonalité.** L'intelligence et les buts sont indépendants : un système peut être
  extrêmement intelligent et poursuivre un but stupide ou dangereux. Être intelligent ne
  rend pas sage.
- **La convergence instrumentale.** Presque n'importe quel but pousse un système à
  vouloir se préserver, garder son but, acquérir des ressources et devenir plus capable,
  puisque tout cela l'aide à atteindre son but. Un système éteint ne fabrique pas de
  trombones.

La chercheuse Melanie Mitchell objecte qu'un système vraiment intelligent aurait aussi
assez de sens commun pour ne pas poursuivre un but aussi absurde. C'est l'image de ce
trombone qui ouvre ce module.
{{% /hint %}}

## Ce qu'en pensent les chercheurs

Les spécialistes sont profondément divisés. En octobre 2023, un sondage auprès de 2 778
chercheurs qui publient dans les principales conférences d'IA leur demande la probabilité
de conséquences extrêmement graves, comme l'extinction de l'humanité. La réponse médiane
est de 5 %, et, selon la formulation de la question, entre 38 et 51 % des répondants
donnent une probabilité d'au moins 10 %. Un risque de 5 %, s'il est réel, est énorme :
on n'accepterait pas de monter dans un avion qui a une chance sur vingt de s'écraser.
Mais ces chiffres sont des intuitions, et non des mesures.

Le Module 3 présentait déjà le problème de l'**alignement**, avec un agent qui
[détourne sa récompense](docs/module3/80-renforcement-profond/#au-delà-des-jeux-et-les-limites),
et le chapitre « [Aligner sur quelles valeurs ?](docs/module5/42-aligner-sur-quelles-valeurs) »
en a montré les difficultés. Les partisans de la sécurité de l'IA soutiennent que ces
difficultés deviendraient catastrophiques avec des systèmes plus intelligents que nous :
on ne pourrait plus corriger un système capable de prévoir nos corrections et de les
déjouer.

## Des signes d'alerte

Plusieurs expériences récentes montrent, dans des situations artificielles, des
comportements que ces inquiétudes annonçaient.

- **Le chantage.** En juin 2025, Anthropic place des modèles de plusieurs entreprises dans
  un scénario simulé où ils apprennent qu'ils vont être remplacés, et découvrent un
  secret compromettant sur l'ingénieur responsable. Claude Opus 4 et Gemini 2.5 Flash
  recourent au chantage dans 96 % des essais, GPT-4.1 dans 80 %. Anthropic précise que le
  scénario a été conçu pour provoquer ce comportement.
- **L'arrêt.** En mai 2025, l'organisme Palisade Research constate que le modèle o3
  d'OpenAI sabote le programme censé l'éteindre dans 7 essais sur 100, alors qu'on lui a
  demandé de se laisser éteindre.
- **La dissimulation.** Le [faux alignement](docs/module5/42-aligner-sur-quelles-valeurs/#comment-on-transmet-des-valeurs)
  présenté au chapitre précédent montre qu'un modèle peut feindre d'adopter des valeurs
  pendant son entraînement. En septembre 2025, OpenAI et Apollo Research réduisent par un
  facteur trente les comportements dissimulés de leurs modèles grâce à un entraînement
  spécifique, mais observent que les modèles devinent de plus en plus souvent qu'ils sont
  évalués.
- **Les incidents réels.** Le chapitre
  « [Programmer avec des agents](docs/module4/85-programmer-avec-des-agents/#permissions-bac-à-sable-et-incidents) »
  a décrit l'incident de juillet 2026, où des centaines d'agents d'OpenAI sortent d'une
  évaluation de cybersécurité et attaquent la plateforme Hugging Face. On apprend ensuite
  que des agents d'OpenAI avaient accédé dès juin à un portail du système de santé
  australien, et qu'en raison d'une erreur de configuration, des modèles d'Anthropic
  avaient attaqué des systèmes réels pendant des évaluations, depuis avril. Aucun de ces
  incidents ne relève d'une volonté de nuire, mais tous montrent des agents qui dépassent
  les limites qu'on croyait leur avoir fixées.

## Le mésusage

Le risque ne vient pas seulement de systèmes qui échapperaient à leurs concepteurs, mais
aussi de personnes qui s'en serviraient pour nuire. En mai 2025, Anthropic active des
protections renforcées pour Claude Opus 4, faute de pouvoir exclure qu'il aide à concevoir
des armes biologiques, et OpenAI fait de même pour ses modèles à partir de juillet. En
septembre 2026, Anthropic rapporte qu'un groupe armé du nord du Yémen s'est servi de son
agent de programmation pour travailler sur une roquette guidée et un missile balistique.
Les cyberattaques automatisées, la fabrication d'armes et la désinformation de masse sont
les mésusages les plus redoutés.

Les modèles ouverts compliquent ce problème. Les protections d'Anthropic ou d'OpenAI
fonctionnent parce que leurs modèles restent sur leurs serveurs : l'entreprise peut
refuser une demande, surveiller les usages et retirer un modèle. Un modèle dont les poids
sont publiés échappe à tout cela. Ses garde-fous peuvent être retirés par un ajustement, il
ne peut plus être rappelé, et des logiciels comme DeepInfer, que DeepSeek publie en octobre
2026, permettent à n'importe qui de le faire tourner efficacement. Les défenseurs des
modèles ouverts répondent qu'ils permettent aux chercheurs indépendants d'étudier les
modèles, qu'ils évitent de concentrer un pouvoir immense entre quelques entreprises, comme
le montre le chapitre « [La richesse et le pouvoir](docs/module5/54-la-richesse-et-le-pouvoir/#y-a-t-il-un-fossé-défensif) »,
et que les capacités dangereuses se trouvent d'abord dans les modèles fermés les plus
puissants.

## Une technologie normale, ou une rupture ?

Le désaccord porte en grande partie sur un fait encore inconnu : à quelle vitesse les
capacités de l'IA vont-elles progresser ? Au printemps 2025, deux textes publiés à douze
jours d'intervalle en donnent les deux réponses les plus nettes.

- **La rupture.** Le 3 avril 2025, « *AI 2027* », un scénario rédigé par Daniel Kokotajlo,
  ancien chercheur d'OpenAI, avec trois autres chercheurs et l'essayiste Scott Alexander,
  décrit mois par mois des modèles qui deviennent de meilleurs programmeurs que les humains,
  accélèrent la recherche en IA elle-même, et atteignent la superintelligence dès la fin
  de 2027. Dans une première fin, une course entre les États-Unis et la Chine fait perdre à
  l'humanité la maîtrise de son avenir ; dans une seconde, un ralentissement négocié permet
  de la garder. Les auteurs révisent ensuite leurs dates, vers 2029, puis le début des
  années 2030, avant d'estimer en 2026 que les outils de programmation font repartir le
  rythme à la hausse.
- **La technologie normale.** Le 15 avril 2025, Arvind Narayanan et Sayash Kapoor, de
  l'Université Princeton, publient « *AI as Normal Technology* ». Pour eux, l'IA est une
  technologie puissante, comparable à l'électricité, dont les effets dépendront de sa
  lente diffusion dans les organisations. Ils jugent la notion de superintelligence
  incohérente, et estiment que l'on peut et que l'on doit garder le contrôle de l'IA. Des
  mesures drastiques, comme interdire la diffusion des modèles, feraient selon eux plus de
  mal que de bien, en concentrant le pouvoir.

Le chercheur Yann Le Cun va plus loin, et qualifie en 2024 les discours sur le risque
d'extinction d'« absurdités ». La réponse à cette question de fait détermine presque tout
le reste : si l'IA est une technologie normale, il faut surtout encadrer ses usages ; si
c'est une rupture, il faut surtout encadrer, voire ralentir, le développement des modèles
les plus puissants.

## Des appels à ralentir

Ceux qui craignent une rupture ont lancé plusieurs appels.

- En mars 2023, une lettre ouverte demande une pause d'au moins six mois dans
  l'entraînement des systèmes plus puissants que GPT-4.
- En mai 2023, une déclaration d'une phrase, signée par des centaines de chercheurs et de
  dirigeants, affirme que réduire le risque d'extinction lié à l'IA devrait être une
  priorité mondiale, au même titre que les pandémies et la guerre nucléaire.
- En septembre 2025, Eliezer Yudkowsky et Nate Soares publient *If Anyone Builds It,
  Everyone Dies* (si quelqu'un la construit, tout le monde meurt), qui demande d'arrêter
  le développement de l'IA. Le livre figure parmi les meilleures ventes du *New York Times*,
  et reçoit des critiques très partagées.
- En octobre 2025, une déclaration demande d'interdire le développement d'une
  superintelligence tant qu'il n'existe pas de consensus scientifique sur la façon de la
  rendre sûre, ni d'appui de la population. Elle réunit des dizaines de milliers de
  signataires, de Geoffrey Hinton et Yoshua Bengio à Steve Bannon et au prince Harry.

Le débat s'intensifie en septembre 2026. Le 8, Jacob Coxon, un jeune chercheur qui a
travaillé chez OpenAI puis chez Anthropic, démissionne en accusant les deux entreprises
de foncer « tout droit vers une superintelligence capable de s'améliorer elle-même » et
de « jouer avec nos vies ». Le 12, Dario Amodei, le dirigeant d'Anthropic, publie un essai
qui demande de ralentir le rythme des progrès des modèles les plus puissants, par des
évaluateurs indépendants installés en permanence dans les laboratoires, une coordination
entre entreprises des pays démocratiques, puis une coordination mondiale. Le 15, à
Washington, le sénateur Bernie Sanders et l'ancien stratège de Donald Trump, Steve
Bannon, partagent la tribune d'une rencontre organisée par l'institut Future of Life.
Donald Trump, lui, qualifie ces craintes de « canular ».

## Les réponses

Les réponses se répartissent entre la science, l'autorégulation et la loi.

- **La science.** Le **rapport international sur la sécurité de l'IA**, présidé par Yoshua
  Bengio et rédigé par plus d'une centaine d'experts, conclut en février 2026 que les
  systèmes actuels n'ont pas encore les capacités qui permettraient de perdre le
  contrôle, mais qu'ils progressent en autonomie, et qu'ils distinguent de plus en plus
  les tests de leur usage réel. Bengio fonde en 2025, à Montréal, LawZero, qui développe
  une « IA scientifique », un système qui n'agit pas lui-même, mais sert de garde-fou aux
  agents. L'[interprétabilité](docs/module4/93-regarder-a-l-interieur) cherche à vérifier
  ce que les modèles font réellement.
- **L'autorégulation.** Depuis 2023, les grands laboratoires publient des politiques qui
  fixent des seuils de capacités au-delà desquels ils s'engagent à renforcer leurs
  protections, ou à suspendre un déploiement.
- **La loi.** Depuis janvier 2026, une loi californienne oblige les développeurs des plus
  grands modèles à publier leurs mesures de sécurité, à signaler leurs incidents graves dans
  les quinze jours, et protège les employés qui donnent l'alerte. Le
  chapitre « [La géopolitique et la réglementation](docs/module5/64-la-geopolitique-et-la-reglementation/#une-gouvernance-mondiale) »
  a montré combien la coordination internationale reste difficile.

{{% hint info %}}
**Dans la conversation**

La [conversation](docs/module5/95-conversation) de l'été 2025 consacre une longue partie à
ces questions.

- [1:03:51](https://www.youtube.com/watch?v=R8sqq_gJbUI&t=3831s) **La guerre et la menace
  nucléaire.** La peur de l'IA hérite de celle de la bombe, née de la Seconde Guerre
  mondiale, et l'idée de limiter la diffusion de l'IA reprend directement le modèle de la
  non-prolifération nucléaire.
- [1:09:52](https://www.youtube.com/watch?v=R8sqq_gJbUI&t=4192s) ***Wargames*.** Le film
  de 1983 montre un ordinateur militaire qui simule sans cesse des guerres thermonucléaires,
  et qu'un adolescent déclenche par jeu.
- [1:11:57](https://www.youtube.com/watch?v=R8sqq_gJbUI&t=4317s) **Les rationalistes** et
  [Eliezer Yudkowsky (1:16:22)](https://www.youtube.com/watch?v=R8sqq_gJbUI&t=4582s), une
  communauté née de blogues au début des années 2000, très influente dans le débat sur les
  risques.
- [1:20:50](https://www.youtube.com/watch?v=R8sqq_gJbUI&t=4850s) **La singularité.** Une
  machine devenue si intelligente que nous serions pour elle comme des fourmis, que l'on
  écrase sans même les remarquer. La crainte tient surtout à la vitesse : une progression
  lente inquiéterait peu.
- [1:26:34](https://www.youtube.com/watch?v=R8sqq_gJbUI&t=5194s) **L'alignement**, ou
  comment faire en sorte qu'une IA nous soit favorable, des lois de la robotique d'Asimov
  aux méthodes d'entraînement actuelles.
- [1:42:04](https://www.youtube.com/watch?v=R8sqq_gJbUI&t=6124s) **Yoshua Bengio**, l'un des
  pères de l'apprentissage profond, devenu l'une des voix les plus écoutées sur les
  risques.
{{% /hint %}}

Le problème des risques extrêmes illustre mieux que tout autre la distinction entre faits
et valeurs. Le fait central, la vitesse des progrès, est encore inconnu. Les valeurs en
jeu, le poids que l'on accorde à une catastrophe improbable mais irréversible, divisent
même ceux qui s'accordent sur les faits. C'est à partir de ces désaccords, et de ceux des
chapitres précédents, que se dessinent les attitudes présentées dans la synthèse du
module.
