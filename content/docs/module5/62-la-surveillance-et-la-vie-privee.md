---
title: "La surveillance et la vie privée"
weight: 62
slug: la-surveillance-et-la-vie-privee
---

# La surveillance et la vie privée

L'IA a besoin de données, et elle sait en tirer ce que personne n'avait remarqué. Ces
deux propriétés en font un outil de surveillance d'une puissance inédite. Ce chapitre
examine trois façons dont elle touche la vie privée : la reconnaissance des visages, les
données qui servent à entraîner les modèles, et ce que nous confions aux assistants.

## Reconnaître les visages

Le Module 3 a présenté la [reconnaissance faciale](docs/module3/50-reseaux-convolutifs)
comme une application des réseaux convolutifs. Ses usages vont du déverrouillage d'un
téléphone à l'identification de suspects, et posent deux problèmes distincts.

- **Elle se trompe davantage pour certains.** En 2018, l'étude *Gender Shades* de Joy
  Buolamwini et Timnit Gebru montre que trois systèmes commerciaux de classification
  du genre se trompaient jusqu'à 34,7 % du temps pour les femmes à la peau foncée, contre
  au plus 0,8 % pour les hommes à la peau claire. En 2019, l'institut américain des
  normes, le NIST, trouve chez de nombreux algorithmes des taux de faux positifs de 10 à
  plus de 100 fois plus élevés selon les groupes. Aux États-Unis, au moins huit personnes
  ont été arrêtées à tort à cause d'une fausse identification, dont sept étaient noires.
  En 2020, à Detroit, Robert Williams est arrêté devant sa famille et détenu une trentaine
  d'heures ; un règlement interdit depuis 2024 à la police de Detroit d'arrêter quelqu'un
  sur la seule foi d'une correspondance faciale.
- **Elle fonctionne trop bien.** L'entreprise Clearview AI a constitué, en recueillant
  des photos sur le Web sans consentement, une base de plus de 50 milliards d'images, que
  la police peut interroger pour identifier n'importe qui à partir d'une photo. En février
  2021, le commissaire fédéral à la protection de la vie privée et ses homologues du
  Québec, de la Colombie-Britannique et de l'Alberta concluent qu'il s'agit de
  « surveillance de masse », illégale au Canada. L'Italie, la Grèce et la France lui
  infligent chacune une amende de 20 millions d'euros, et les Pays-Bas une amende de
  30,5 millions.

{{< image src="/images/module5/portraits/gender-shades.jpg" alt="Deux portraits côte à côte : Joy Buolamwini et Timnit Gebru." title="Joy Buolamwini et Timnit Gebru, en 2018." class="portraits" loading="lazy" >}}

<p class="image-credit">Joy Buolamwini et Timnit Gebru, en 2018. Photos : Buolamwini, Niccolò Caranti, <a href="https://creativecommons.org/licenses/by-sa/4.0">CC BY-SA 4.0</a>, via Wikimedia Commons ; Gebru, TechCrunch, <a href="https://creativecommons.org/licenses/by/2.0">CC BY 2.0</a>, via Wikimedia Commons.</p>

Les deux problèmes se combinent : un système imparfait est dangereux pour ceux qu'il
identifie à tort, et un système parfait est dangereux pour tous, puisqu'il rend
l'anonymat impossible dans l'espace public.

## Des usages qui se multiplient

La surveillance par l'IA dépasse les visages.

- **En Chine**, une plateforme policière déployée au Xinjiang, analysée en 2019 par Human
  Rights Watch, signale comme suspects des comportements parfaitement légaux, comme éviter
  ses voisins ou ne pas utiliser la porte d'entrée de sa maison, dans le cadre de la
  répression des Ouïghours. Le « crédit social » chinois, souvent décrit comme une note
  attribuée à chaque citoyen, est en réalité un ensemble de listes noires, surtout
  destinées aux entreprises et aux mauvais payeurs ; une note unique de ce genre n'existe
  pas.
- **Aux États-Unis**, la police de l'immigration utilise depuis 2025 une application qui
  identifie sur le terrain, par le visage ou les empreintes, les personnes contrôlées,
  sans qu'elles puissent refuser. Des réseaux de caméras de lecture de plaques
  d'immatriculation, partagés entre des milliers de corps policiers, permettent de suivre
  des déplacements à l'échelle du pays, et de nombreuses villes ont mis fin à leur contrat avec leur principal fournisseur.
- **Les escroqueries.** Le clonage de la voix permet de se faire passer pour un proche ou
  un dirigeant au téléphone. En mai 2025, le FBI avertit que des fraudeurs imitent ainsi
  de hauts responsables américains.

## Les données qui entraînent les modèles

Les modèles s'entraînent sur ce que nous publions. En mai 2025, Meta commence à entraîner
ses modèles sur les publications publiques de ses utilisateurs européens, en invoquant
son « intérêt légitime », et en ne leur laissant que la possibilité de s'y opposer. En
novembre 2025, LinkedIn fait de même, notamment au Canada, en activant cette utilisation
par défaut. Ce que l'on a publié pour quelques contacts devient une donnée
d'entraînement pour un modèle qui servira des millions de personnes.

Un modèle peut aussi **déduire** ce que l'on n'a jamais dit. Il suffit de quelques
régularités dans des données ordinaires, comme des achats, des déplacements ou des
mentions « J'aime », pour estimer un état de santé, une orientation sexuelle ou des
opinions politiques. En 2017, une étude controversée de Stanford prétendait même
deviner l'orientation sexuelle à partir de photos de visages, ce que ses critiques ont
dénoncé comme une pseudoscience dangereuse.

## Ce que nous confions aux assistants

Des centaines de millions de personnes confient chaque jour aux assistants des
questions de santé, des problèmes de couple ou des documents de travail. Ces
conversations ne sont pas aussi privées qu'elles le paraissent.

- **Pas de secret professionnel.** En juillet 2025, Sam Altman reconnaît que les
  conversations avec ChatGPT ne bénéficient d'aucune protection juridique comparable à
  celle d'une consultation chez un médecin ou un avocat, et qu'OpenAI pourrait devoir les
  produire dans un procès.
- **Des conversations conservées.** En mai 2025, dans le procès du *New York Times*, une
  juge ordonne à OpenAI de conserver les conversations de ses utilisateurs, y compris
  celles qu'ils avaient supprimées. L'obligation est levée en octobre 2025, sauf pour
  certains comptes.
- **Des conversations publiées.** À l'été 2025, des conversations partagées par des
  utilisateurs de ChatGPT apparaissent dans les résultats de Google, et OpenAI retire la
  fonction. Chez Meta, des utilisateurs publient sans le savoir des conversations
  personnelles dans un fil public.
- **Une mémoire.** Les assistants qui se souviennent des conversations précédentes, comme
  le décrit le chapitre « [Des outils, un harnais et des agents](docs/module4/80-outils-et-agents) »,
  accumulent un portrait de plus en plus précis de leurs utilisateurs.
- **Des données envoyées à l'étranger.** Quand on utilise un assistant en ligne, ses
  conversations sont stockées chez son fournisseur, et soumises aux lois de son pays. En
  janvier 2025, l'autorité italienne de protection des données bloque l'application de
  DeepSeek, dont les données sont conservées en Chine. La Corée du Sud suspend son
  téléchargement, l'Australie, Taïwan et plusieurs administrations américaines l'interdisent
  sur les appareils de l'État, et le gouvernement fédéral canadien la bloque sur une partie
  de ses téléphones.

Les [modèles ouverts](docs/module5/54-la-richesse-et-le-pouvoir/#y-a-t-il-un-fossé-défensif)
offrent ici une solution : un modèle dont les poids sont publiés peut tourner sur ses
propres machines, sans qu'aucune donnée ne quitte l'organisation. En 2024, la Commission
nationale de l'informatique et des libertés, en France, recommande ainsi de privilégier des
systèmes locaux et sécurisés pour déployer une IA générative. Un modèle local garde
toutefois les valeurs et les biais qu'il a appris.

## Ce que dit la loi

Plusieurs lois encadrent ces usages.

- **L'AI Act européen** interdit depuis février 2025 la notation sociale, la
  reconnaissance des émotions au travail et à l'école, la constitution de bases de visages
  par la collecte indiscriminée d'images, et l'identification biométrique à distance en
  temps réel dans l'espace public par la police, sauf exceptions strictes, comme la
  recherche d'une personne disparue ou la prévention d'un attentat.
- **Au Québec**, la Loi 25 impose depuis 2023 une évaluation des facteurs relatifs à la
  vie privée avant tout projet qui touche des renseignements personnels, l'information des
  personnes quand une technologie permet de les identifier, de les localiser ou d'établir
  leur profil, et la transparence des décisions automatisées, présentée au chapitre
  « [Qui est responsable ?](docs/module5/40-qui-est-responsable/#le-droit-à-une-explication) ».
  Une base de données biométriques doit être déclarée à la Commission d'accès à
  l'information avant sa mise en service.
- **Au Canada**, la réforme fédérale de la protection des renseignements personnels,
  prévue dans le même projet de loi que l'encadrement de l'IA, est morte au feuilleton en
  janvier 2025.

La vie privée est un cas exemplaire de problème où les faits et les valeurs se mêlent.
Les faits sont connus : les données existent, et les modèles savent en tirer beaucoup. La
question est de savoir ce que l'on accepte d'échanger, en confort, en sécurité ou en
efficacité, contre une part de ce que l'on voudrait garder pour soi.
