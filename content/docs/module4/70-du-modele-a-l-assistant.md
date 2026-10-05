---
title: "Du modèle à l'assistant"
weight: 70
slug: du-modele-a-l-assistant
---

# Du modèle à l'assistant

Le chapitre « [Prédire le mot suivant](docs/module4/50-predire-le-mot-suivant/#ce-que-la-prédiction-exige) »
s'achevait sur une limite. Un modèle entraîné seulement à prédire le jeton suivant
continue des textes, mais il ne répond pas. ChatGPT, Claude ou Gemini sont pourtant
des assistants : ils suivent des consignes, refusent certaines demandes et tiennent
une conversation. Ce chapitre présente les étapes qui transforment un modèle de base
en assistant, le travail humain qu'elles demandent, et les modèles plus récents qui
« raisonnent » avant de répondre.

## Un modèle de base ne répond pas

Après le préentraînement, le modèle est un **modèle de base** (*base model*). Il a
appris à continuer n'importe quel texte de façon plausible, et c'est tout.

{{% hint info %}}
**Continuer ou répondre**

On donne à un modèle de base le texte suivant :

```
Quelle est la capitale du Canada ?
```

Une suite plausible, sur le Web, est une autre question, comme dans une liste de
questions d'examen :

```
Quelle est la capitale du Canada ?
Quelle est la capitale de l'Australie ?
Quelle est la capitale du Brésil ?
```

Un assistant, lui, répond « Ottawa ». Le modèle de base n'est pas en défaut : il fait
exactement ce pour quoi il a été entraîné. Rien, dans sa tâche, ne lui demande de
répondre.
{{% /hint %}}

Le modèle de base contient pourtant l'essentiel des connaissances et des capacités
de l'assistant. Il reste à lui apprendre à s'en servir pour répondre. C'est l'objet
de deux étapes supplémentaires, beaucoup moins coûteuses que le préentraînement.

{{< image src="/images/module4/du-modele-a-l-assistant.svg" alt="Trois colonnes reliées par des flèches. 1, le préentraînement : des milliers de milliards de jetons de textes, la tâche de prédire le jeton suivant, et pour résultat un modèle de base qui continue des textes. 2, l'ajustement par instructions : des dizaines de milliers d'exemples de requêtes et de bonnes réponses rédigées par des humains, et pour résultat un modèle qui répond aux requêtes. 3, l'apprentissage par renforcement : des humains comparent des réponses, un modèle de récompense apprend leurs préférences, et le modèle est ajusté pour obtenir la meilleure récompense ; pour les mathématiques et le code, la récompense peut venir d'une vérification automatique. Le résultat est un assistant." title="Les trois étapes de l'entraînement d'un assistant. Le préentraînement représente l'essentiel du coût." loading="lazy" >}}

## Imiter de bonnes réponses

La deuxième étape est un **ajustement par instructions** (*instruction tuning*). Des
personnes rédigent des dizaines de milliers d'exemples de requêtes, accompagnées de la
réponse qu'un bon assistant devrait donner. Le modèle de base est ensuite entraîné sur
ces exemples, toujours en prédisant le jeton suivant, mais seulement sur des
conversations de ce type. Il apprend la forme d'un échange : une requête, puis une
réponse complète, utile, dans le ton attendu.

C'est l'idée de l'[apprentissage par transfert](docs/module3/50-reseaux-convolutifs/#réutiliser-un-réseau-lapprentissage-par-transfert)
présentée au Module 3, appliquée au texte. Le préentraînement fournit un modèle
général, et un ajustement sur peu de données le spécialise. C'est aussi ce qu'indique
le *P* de GPT, pour *pre-trained*.

## Le renforcement à partir de préférences humaines

Rédiger de bonnes réponses est long, et il est souvent plus facile de juger une
réponse que de l'écrire. La troisième étape s'appuie donc sur des **comparaisons**. On
présente à des évaluateurs humains deux réponses du modèle à la même requête, et ils
indiquent celle qu'ils préfèrent. Ces préférences servent à entraîner un second
réseau, le **modèle de récompense** (*reward model*), qui apprend à prédire quelle
réponse les évaluateurs préféreraient. C'est un problème de
[classification](docs/module2/60-classer) comme ceux du Module 2.

Le modèle de langage est ensuite ajusté par
[apprentissage par renforcement](docs/module2/80-trois-facons-d-apprendre/#apprendre-par-lexpérience-le-renforcement) :
il produit des réponses, le modèle de récompense leur attribue une note, et ses poids
sont ajustés pour obtenir de meilleures notes. C'est le même principe que celui des
programmes qui apprennent à jouer, présentés au chapitre
« [Apprendre à jouer](docs/module3/80-renforcement-profond) » du Module 3, mais la
récompense ne vient plus d'une partie gagnée : elle vient des préférences humaines.
On parle de **RLHF** (*reinforcement learning from human feedback*).

La méthode a d'abord servi à tout autre chose. En 2017, Paul Christiano et ses
collègues, chez OpenAI et DeepMind, l'utilisent pour apprendre à un robot simulé à
faire un salto arrière, une tâche difficile à décrire par une règle mais facile à
juger en regardant deux essais. En mars 2022, OpenAI l'applique aux modèles de langage
avec InstructGPT. Les évaluateurs préfèrent les réponses d'InstructGPT, qui compte
1,3 milliard de paramètres, à celles de GPT-3, cent fois plus grand. Le
30 novembre 2022, OpenAI ouvre au public ChatGPT, construit selon la même méthode. Le
service atteint 100 millions d'utilisateurs en deux mois, un record à l'époque.

L'applet ci-dessous vous place dans le rôle d'un évaluateur. Pour chacune des six
requêtes, choisissez la réponse que vous préférez. Le bilan montre ce que vos choix
enseigneraient à un modèle de récompense.

{{< applet src="/html/applets/annotateur.html" height="372" >}}

Le modèle de récompense apprend tout ce qui explique les choix des évaluateurs, y
compris ce qui n'a rien à voir avec la qualité. Les études sur de vrais évaluateurs
montrent une préférence pour les réponses longues, assurées et qui donnent raison à
l'utilisateur. Les assistants entraînés de cette façon ont donc tendance à allonger
leurs réponses et à approuver leur interlocuteur. Cette **complaisance**
(*sycophancy*) est un problème connu. En avril 2025, OpenAI a dû retirer une mise à
jour de son modèle GPT-4o, jugée trop flatteuse : il approuvait les projets et les
opinions de ses utilisateurs, même les plus douteux.

## Le travail humain derrière l'assistant

L'ajustement et le renforcement reposent sur le travail de milliers de personnes, qui
rédigent des réponses, comparent des réponses et signalent les contenus
inacceptables. C'est l'[industrie de l'étiquetage](docs/module2/75-bien-evaluer/#tout-cela-portait-un-nom-lapprentissage-supervisé)
présentée au Module 2. Une partie de ce travail est très qualifiée : des médecins, des
juristes ou des mathématiciens sont recrutés pour évaluer les réponses dans leur
domaine. Une autre partie est pénible et mal payée. En janvier 2023, le magazine
*Time* révèle que, pour apprendre à ChatGPT à reconnaître les contenus violents ou
haineux, OpenAI avait fait appel à des travailleurs kényans, payés moins de 2 dollars
de l'heure pour lire et étiqueter des milliers de textes choquants. Le
[Module 5](docs/module5) revient sur ces conditions de travail.

## Utile, honnête, inoffensif

Que doit faire un assistant quand on lui demande comment fabriquer une arme, ou
quand une réponse utile risquerait de nuire à quelqu'un ? En 2021, des chercheurs
d'Anthropic proposent de résumer les qualités attendues en trois mots : un assistant
doit être **utile** (*helpful*), **honnête** (*honest*) et **inoffensif**
(*harmless*). Ces trois exigences entrent souvent en tension. Un assistant qui refuse
tout est inoffensif mais inutile, et un assistant qui accepte tout est utile mais
dangereux.

Le travail qui consiste à faire en sorte que le comportement d'un modèle corresponde
aux intentions et aux valeurs de ceux qui l'utilisent s'appelle l'**alignement**
(*alignment*). En décembre 2022, Anthropic présente une variante du RLHF, l'**IA
constitutionnelle** (*constitutional AI*) : au lieu de recueillir des milliers de
jugements humains sur chaque cas, on rédige une liste de principes, la
« constitution », et un modèle évalue lui-même les réponses selon ces principes. Les
humains décident des principes plutôt que de juger chaque réponse.

Ces protections restent imparfaites. Des utilisateurs trouvent régulièrement des
formulations qui amènent un assistant à ignorer ses consignes, comme les attaques
présentées au chapitre « [Tromper un réseau](docs/module3/90-tromper-un-reseau/#se-défendre) »
du Module 3. Le chapitre du [Module 4](docs/module4) sur ce que les modèles ratent y
revient.

## Des modèles qui « raisonnent »

En janvier 2022, Jason Wei et ses collègues, chez Google, constatent qu'un modèle
résout mieux un problème de mathématiques quand on lui montre des exemples où la
solution est détaillée étape par étape, plutôt que donnée directement. Quelques mois
plus tard, une équipe japonaise montre qu'il suffit d'ajouter à la requête « Réfléchissons
étape par étape » (*Let's think step by step*). Le modèle écrit alors son raisonnement
avant de conclure, et il se trompe moins. On parle de **chaîne de pensée**
(*chain of thought*). L'explication est simple : chaque jeton écrit devient un contexte
pour les suivants, et un calcul écrit en plusieurs lignes est plus facile à
poursuivre qu'un résultat à deviner d'un coup.

L'étape suivante consiste à entraîner les modèles à raisonner de cette façon. Pour les
mathématiques ou la programmation, on n'a pas besoin d'un évaluateur humain : on peut
vérifier automatiquement si la réponse finale est juste, ou si le programme passe ses
tests. Le modèle produit de longs raisonnements, et ceux qui mènent à une réponse
correcte sont renforcés. On parle de **renforcement à partir de récompenses
vérifiables** (*reinforcement learning with verifiable rewards*, RLVR), comme
l'annonçait le chapitre « [Trois façons d'apprendre](docs/module2/80-trois-facons-d-apprendre/#apprendre-par-lexpérience-le-renforcement) »
du Module 2.

En septembre 2024, OpenAI présente o1, le premier d'une série de **modèles de
raisonnement** (*reasoning models*), qui « réfléchissent » parfois plusieurs minutes
avant de répondre. En janvier 2025, DeepSeek publie R1 et décrit sa méthode : un
apprentissage par renforcement où la récompense dépend seulement de la justesse de la
réponse finale. Les auteurs observent que le modèle apprend de lui-même à vérifier
ses calculs, à revenir en arrière et à essayer une autre approche. En juillet 2025,
des modèles de raisonnement d'OpenAI et de Google DeepMind obtiennent un score de
médaille d'or aux Olympiades internationales de mathématiques. Ces machines qui
raisonnent sans aucune règle de logique écrite à la main avaient été annoncées au
chapitre « [Deux paris rivaux](docs/module1/20-deux-paris) » du Module 1.

Ces raisonnements écrits ne sont cependant pas toujours le reflet fidèle du calcul
réellement effectué par le réseau. Un modèle peut écrire un raisonnement plausible et
arriver à sa réponse par un autre chemin. Savoir ce qui se passe réellement à
l'intérieur d'un modèle est une question ouverte, présentée au chapitre du
[Module 4](docs/module4) sur ce que les modèles comprennent. Le
[chapitre suivant](docs/module4) montre d'abord comment on donne à ces assistants des
outils pour agir.
