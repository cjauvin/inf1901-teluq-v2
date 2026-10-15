---
title: "Une technologie normale, ou non ?"
weight: 15
slug: technologie-normale
---

# Une technologie normale, ou non ?

Le chapitre « [Sur quoi porte le débat ?](docs/module5/10-sur-quoi-porte-le-debat) »
distinguait six plans de désaccord sur l'IA. Le premier, celui des faits et des
prévisions, contient une question dont dépendent beaucoup d'autres : l'IA est-elle une
technologie comme les autres, ou une rupture sans précédent ? Selon la réponse, on ne
craint pas les mêmes dangers et on ne propose pas les mêmes remèdes.

Au printemps 2025, deux textes publiés à douze jours d'intervalle donnent à cette
question ses deux réponses les plus nettes. Le 3 avril paraît « *AI 2027* », un
scénario qui décrit l'arrivée d'une superintelligence en quelques années. Le 15 avril
paraît « *AI as Normal Technology* », un essai qui soutient que l'IA transformera la
société comme l'ont fait l'électricité ou Internet, c'est-à-dire lentement.

## Le scénario de la rupture

*AI 2027* est rédigé par Daniel Kokotajlo, un ancien chercheur d'OpenAI parti de
l'entreprise en 2024 en dénonçant ses pratiques de sécurité, avec trois autres
chercheurs et l'essayiste Scott Alexander. Il prend la forme d'un récit, mois par mois,
appuyé sur des projections chiffrées.

Le scénario repose sur une idée centrale. Les modèles deviennent d'abord de meilleurs
programmeurs que les humains, ce que les progrès des
[agents de programmation](docs/module4/85-programmer-avec-des-agents) rendent
plausible. Une fois capables de programmer et de mener des expériences, ils
accélèrent la recherche en IA elle-même : chaque génération aide à construire la
suivante, plus vite que ne le feraient des chercheurs humains. Cette **boucle
d'amélioration** (*recursive self-improvement*) mène, dans le récit, à une
superintelligence dès la fin de 2027. Le scénario propose deux fins. Dans la première,
une course entre les États-Unis et la Chine pousse à déployer des systèmes mal
contrôlés, et l'humanité perd la maîtrise de son avenir. Dans la seconde, un
ralentissement négocié permet de garder le contrôle.

Les auteurs ont eux-mêmes révisé leurs dates. Dès l'été 2025, Kokotajlo situe plutôt
l'arrivée d'une IA générale vers 2029, et une mise à jour de décembre 2025 décrit une
progression plus lente, vers le début des années 2030. En avril 2026, une nouvelle mise
à jour estime au contraire que les outils de programmation font repartir le rythme à
la hausse. Ces allers-retours montrent la difficulté de l'exercice, mais l'essentiel
de la thèse ne dépend pas de l'année exacte : une rupture rapide est possible, et il
faut s'y préparer dès maintenant.

Les partisans de cette lecture s'appuient sur plusieurs tendances présentées au
Module 4 :

- les [lois d'échelle](docs/module4/60-passer-a-l-echelle/#des-lois-déchelle), qui
  prédisent depuis 2020 l'amélioration des modèles en fonction du calcul investi ;
- la [durée des tâches](docs/module4/85-programmer-avec-des-agents/#mesurer-swe-bench-et-la-durée-des-tâches)
  qu'un agent mène à bien, qui double environ tous les sept mois ;
- les modèles qui [démontrent](docs/module4/87-demontrer) des résultats mathématiques
  nouveaux, un domaine longtemps jugé hors de portée ;
- les [incidents de 2026](docs/module4/85-programmer-avec-des-agents/#permissions-bac-à-sable-et-incidents),
  où des agents sont sortis de leur bac à sable, qui montrent des capacités qui
  dépassent déjà les moyens de les contenir.

## La thèse de la technologie normale

Arvind Narayanan et Sayash Kapoor, informaticiens à l'Université Princeton, sont
connus pour leur livre *AI Snake Oil* (2024), qui démonte les promesses exagérées de
certains produits d'IA. Leur essai de 2025 ne dit pas que l'IA est sans importance.
Une technologie « normale », au sens où ils l'entendent, peut être aussi profonde que
l'électricité. Elle reste cependant soumise aux mêmes mécanismes que les technologies
précédentes, et la société garde la maîtrise de son rythme.

Leur argument principal distingue trois étapes :

1. l'**invention** : de nouvelles méthodes, comme le Transformer ou l'apprentissage par
   renforcement ;
2. l'**innovation** : des applications concrètes construites avec ces méthodes ;
3. la **diffusion** : l'adoption de ces applications par les personnes, les
   entreprises et les institutions.

Selon eux, les débats se concentrent sur la première étape, qui va très vite, alors que
les effets sur la société dépendent surtout de la troisième, qui va lentement. Une
entreprise doit réorganiser son travail, former ses employés, revoir ses
responsabilités juridiques. Dans les domaines où une erreur coûte cher, comme la
médecine, le droit ou la finance, la diffusion est encore ralentie par les règles et la
prudence. L'histoire offre un précédent souvent cité : l'historien de l'économie Paul
David a montré, en 1990, que l'électricité avait mis une quarantaine d'années à
augmenter la productivité des usines américaines, le temps de les réorganiser autour
des moteurs électriques.

Leurs recommandations découlent de cette lecture. Plutôt que de chercher à empêcher la
diffusion des modèles les plus puissants, ce qui concentrerait le pouvoir entre les
mains de quelques entreprises et de quelques États, il faut renforcer la **résilience**
de la société : surveiller les usages, réduire l'incertitude par de meilleures
mesures, et encadrer chaque domaine d'application avec ses propres règles. Les auteurs
présentent leur thèse comme à la fois une description du présent, une prédiction et
une prescription.

## Ce que disent les indices

Aucun des deux camps ne peut encore prouver sa thèse, mais plusieurs faits pèsent dans
la balance, parfois des deux côtés à la fois.

- **La vitesse d'adoption.** ChatGPT a atteint 100 millions d'utilisateurs en deux
  mois, plus vite que tout service avant lui, comme le montrait le graphique du
  [Module 4](docs/module4). Les partisans de la rupture y voient une diffusion sans
  précédent. Ceux de la technologie normale répondent que l'usage individuel d'un
  assistant n'est pas la transformation des organisations, qui reste lente.
- **Les scores et le monde réel.** Les modèles réussissent des examens professionnels
  et des concours de mathématiques, mais les scores
  [mesurent mal](docs/module4/60-passer-a-l-echelle/#que-mesurent-les-scores) ce qu'un
  modèle saura faire dans une situation réelle, et le
  [défi ARC](docs/module4/88-le-defi-arc) montre ce qui leur résiste encore. Pour la
  technologie normale, l'écart entre l'examen et le métier est justement ce qui ralentit
  la diffusion.
- **La programmation.** C'est le domaine où l'adoption est la plus rapide, et où la
  boucle d'amélioration d'*AI 2027* pourrait commencer, puisque les modèles servent
  déjà à écrire le code des modèles suivants. Les deux camps le surveillent de près.
- **Les incidents.** Pour les uns, des agents qui s'échappent d'une évaluation et
  attaquent une plateforme réelle sont un avertissement. Pour les autres, l'incident
  montre aussi que les institutions réagissent : il a été détecté, contenu, puis
  analysé par un organisme indépendant.

## Ce qui dépend de la réponse

La réponse à cette question détermine presque tout le reste du débat, comme le montre
le tableau suivant.

| | Si l'IA est une technologie normale | Si l'IA est une rupture |
|---|---|---|
| Le danger principal | Les torts concrets : biais, surveillance, emplois, pouvoir concentré | La perte de contrôle de systèmes plus capables que nous |
| L'horizon | Des décennies | Quelques années |
| Ce qu'il faut réglementer | Les usages, domaine par domaine | Le développement des modèles les plus puissants |
| Les modèles ouverts | Un contrepoids utile à la concentration | Un risque, puisqu'on ne peut plus les retirer |
| La coopération internationale | Souhaitable | Indispensable, pour arrêter la course |

Certaines mesures conviennent aux deux lectures, et rallient parfois des camps opposés :
exiger des entreprises qu'elles publient leurs mesures de sécurité et signalent leurs
incidents, comme le fait la loi californienne de 2025, financer des évaluations
indépendantes, ou investir dans la recherche sur
l'[interprétabilité](docs/module4/93-regarder-a-l-interieur). Elles ont l'avantage de
réduire l'incertitude, quelle que soit la bonne réponse.

{{% hint info %}}
**Une question qui revient à chaque technologie**

Le débat n'est pas entièrement nouveau. L'électricité, l'automobile, l'énergie
nucléaire et Internet ont chacun suscité à la fois des promesses d'abondance et des
craintes de catastrophe. Pour les tenants de la technologie normale, cette histoire
montre que les prophéties extrêmes se réalisent rarement. Pour leurs adversaires,
l'énergie nucléaire montre au contraire qu'une technologie peut, pour la première
fois, menacer l'humanité entière, et qu'une technologie capable de concevoir la
suivante n'a pas de précédent.
{{% /hint %}}
