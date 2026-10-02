# Plan — Refonte v2 du cours INF1901 (TELUQ)

> **Note de démarrage** — Ce document est le livrable d'une séance de brainstorm de conception. Il est conçu pour être **autosuffisant** : la rédaction de la v2 démarrera en **contexte neuf, avec ce plan comme seule entrée**. Les *pourquoi* et les alternatives écartées sont consignés exprès pour survivre sans le transcript.
> **Emplacement cible** : à déplacer à la **racine du dépôt sous `PLAN-v2.md`** dès la sortie du plan mode (versionné par git, voyage avec le cours).
> **Première cible de rédaction** : le **Module 1** (le plus défini et le plus vide actuellement).

---

## 1. Contexte

Refonte de la v2 du cours INF1901 (Hugo + thème hugo-book-teluq, contenu markdown sous `content/docs/moduleN/`). Quatre axes définis par Christian :

1. **Module 1** : refonte complète → IA classique (GOFAI), mélange d'histoire et d'idées algorithmiques/mathématiques, pour faire comprendre ce qui a précédé le ML.
2. **Modules 2-3-4** : compléter et uniformiser (très inégaux en v1 : M2 ≈ 17 000 mots, M3 ≈ 8 300, M4 ≈ 3 700).
3. **Module 5** : le rendre plus mordant, plus connecté à l'actualité récente.
4. **Travaux notés 1 et 5** : leur donner une forme *hands-on* comme les TN2-3-4.

## 2. Fondations

- **Structure macro inchangée** : M1 GOFAI → M2 ML → M3 réseaux/deep → M4 GenAI/LLM → M5 société/philo.
- **Public (inchangé vs v1)** : étudiants à distance de premier cycle, **non-informaticiens**. Cours de *littératie en IA* : comprendre ce qu'il y a sous le capot sans devenir praticien, pour finir capable de juger (M5). **Pas de programmation, pas de formalisme math lourd** ; vulgarisation appuyée (vidéos, outils interactifs, exemples à la main).
- **Retrait des deux livres** : la v2 élimine les deux ouvrages obligatoires de la v1 — *La plus belle histoire de l'intelligence* (Dehaene et al.) et *Quand la machine apprend* (Le Cun). Cours désormais **autonome**, sans achat obligatoire.
  - Supprimer `content/docs/30-livres.md` et les lectures/quiz du M1 actuel (`content/docs/module1/10-activités.md`) qui en dépendent.
  - **Détachement complet** côté Dehaene : sa substance M1 (nature de l'intelligence, limites du symbolique, sens commun) est déjà couverte par notre contenu original.
  - **Récupérer la matière Le Cun** (CNN, reconnaissance de chiffres/chèques, révolution du deep learning), actuellement mal placée au M1 → la **replacer au M3**.

## 3. Idées d'unification (le tissu conjonctif de la v2)

Ce qui donnera sa cohérence à la v2 — à exploiter activement comme liens entre modules.

- **Motif récurrent « semé → fleurit »** : un mécanisme est *introduit* dans un module, puis *fleurit* dans le suivant.
  - **Perceptron** : semé M1 → fleurit M3.
  - **RL** : semé M2 → fleurit M3 (deep RL) → réemployé M4 (RLHF).
  - **Transformer** : introduit M3 (architecture) → fleurit M4 (LLM).
- **Fil rouge des deux traditions** : GOFAI (symbolique) et ML (connexionnisme) n'ont **pas** évolué séquentiellement ; ils ont **co-évolué dans des univers parallèles** depuis les années 1950, s'éclipsant à tour de rôle. Posé au M1, dénoué au M3.
- **Fil transversal cerveau ↔ IA** (fond au M3) :
  - **M1 (origine)** : inspiration biologique fondatrice (McCulloch & Pitts 1943, cybernétique de Wiener, perceptron). Recoupe « l'esprit comme logique » (symbolique) vs « l'esprit comme cerveau » (connexionnisme). Touche légère.
  - **M3 (cœur — le piège technique)** : là où la métaphore est la plus séduisante et trompeuse. Encadré « la carte n'est pas le territoire » : le neurone artificiel est une caricature (pas de spikes, pas de neuromodulation, le cerveau ne fait pas de rétropropagation). Démystifiage à haute valeur, au moment de la tentation.
  - **M5 (la question profonde)** : reproduire le cerveau donnerait-il un esprit ? conscience, paradoxe de Moravec. Touche légère / terreau.
- **Fil transversal syntaxe → sémantique → pragmatique** (les trois niveaux du langage et du sens) — grille qui éclaire *pourquoi* le symbolique a plafonné.
  - **Posé au M1 (épisode 4)** : manipuler des symboles selon leur *forme* (**syntaxe**) ne donne pas le *sens* (**sémantique**), encore moins l'*usage en contexte* (**pragmatique**). Exemple incarnant les trois : « Pouvez-vous me passer le sel ? ». Regard rétrospectif léger : la logique/recherche/ELIZA des épisodes 1-3 relevaient de la syntaxe ; les réseaux *sémantiques* (ép. 4) visent la sémantique ; le mur du sens commun est d'ordre pragmatique. **Pas de rétro-couture dans les ép. 1-3** (introduit à neuf en ép. 4 + une phrase rétrospective).
  - **Fleurit au M4** : les LLM ont-ils de la sémantique, ou une syntaxe statistique très sophistiquée ?
  - **Dénoué au M5** : Chambre chinoise de Searle — la syntaxe ne suffit pas à produire la sémantique.
- **Principe d'interactivité** : *quand le sujet est un mécanisme, laisser l'étudiant le faire tourner* (vaut M1-M4). Constat clé : ce qui distingue les modules « riches » des « pauvres » n'est pas le volume de texte mais la **densité d'expériences manipulables**. Le M5 (philo) a un levier différent : engagement par le **débat et l'actualité**.

## 4. Gabarit de module (à appliquer uniformément)

Le squelette commun existe déjà en v1 ; il est **à appliquer partout**, pas à inventer.

> **Terminologie des unités textuelles (convention du cours)** : hiérarchie `Cours > Module > page > Section`. Un **Module** est l'une des 5 grandes divisions (M1…M5). Une **page** est un fichier `.md` (nommé `NN-titre.md`, où `NN` = `weight`). Une **Section** est un bloc `##` à l'intérieur d'une page — c'est l'unité de rédaction qu'on valide pas à pas. Le niveau « page » reçoit un nom thématique selon le format du module : au **M1**, les pages sont des **épisodes** (« épisode historique → idée technique ») ; au **M5**, ce seront des **dossiers** (chauds). Les mots *Module* et *Section* sont universels ; seul le nom du niveau intermédiaire varie.

1. **`_index.md`** — mise en contexte, objectifs (3-5), durée, aperçu de l'évaluation. (`bookCollapseSection: true`)
2. **Page « 10 »** — *premier contact concret* avant la théorie (ex. scénario d'assemblage de téléviseurs au M2).
3. **Pages « 20-90 »** — un concept par page, du simple au complexe. Éléments récurrents : applets `{{< applet src=… >}}`, vidéos `{{< youtube id=… >}}` (3Blue1Brown), encadrés `{{% hint %}}`, sections repliables `{{% details %}}` pour l'optionnel, LaTeX (`$$…$$`, `\(…\)`).
4. **Page « 99 »** — le travail noté.

Front matter : `title`, `weight` (ordonne le menu), `slug` optionnel. Fichiers nommés `NN-titre.md`. Pas d'accents dans les URLs.

---

## 5. Module 1 — GOFAI (refonte complète)

- **Format** : sections « épisode historique → idée technique » (**6 épisodes**). L'étudiant comprend l'*idée* et le *drame historique*, **pas** la technique fine (réservée aux M2-3-4).
- **Fil rouge** : les deux traditions parallèles (voir §3). Le M1 plante la tension fondatrice ; le M3 est le dénouement.

### Ossature (6 épisodes, à raffiner à la rédaction)
1. **Turing, la question fondatrice (1950)** — mécaniser la pensée ? Test de Turing, machine universelle. Idée : la pensée comme calcul.
2. **1956-58, deux paris rivaux** — Dartmouth / IA symbolique (règles, symboles) **vs** perceptron de Rosenblatt (apprendre d'exemples). Les deux grandes hypothèses sur l'intelligence, nées quasi simultanément.
3. **L'âge d'or symbolique : chercher et raisonner** — espaces d'états, minimax, explosion combinatoire (jusqu'à Deep Blue 1997). Idée : résoudre = explorer un arbre. **Y loger : ELIZA** (Weizenbaum 1966 — appariement de motifs, « effet ELIZA », rappel du test de Turing ép. 1, sème M4/M5) ; **Lisp** (McCarthy 1958 — la langue maternelle du GOFAI, *list processing* = manipulation de symboles ; résonne à l'ép. 6 avec le krach des machines Lisp).
4. **Représenter le monde** — réseaux sémantiques (Quillian), frames (Minsky 1974), scripts (Schank & Abelson), dépendance conceptuelle → mène au **problème du sens commun** (CYC de Lenat). Explique *pourquoi* le GOFAI a plafonné ; résonne avec ce que les LLM font « gratuitement » (contraste M4). **Y loger : SHRDLU** (Winograd 1970 — le sommet de l'ambition symbolique dans un « micro-monde de blocs », mais qui ne marche *que* là → bute pile sur le sens commun).
5. **Capturer l'expertise : les systèmes experts (70-80)** — l'intelligence comme règles d'experts (MYCIN), grandeur et fragilité (goulot d'étranglement de la connaissance). Idée : connaissance = règles explicites.
6. **Les hivers et la bascule** — Minsky & Papert tuent le perceptron (1969, 1er hiver) ; limites du symbolique (2e hiver). Le monde réel résiste aux règles → porte d'entrée du M2 (« et si on laissait les données parler ? »).

- Le perceptron apparaît 2× : **promesse** (ép. 2) et **victime** (ép. 6) — boucle le drame du M1 et arme le retour du M3. Traiter seulement l'*idée* (machine qui apprend de ses erreurs) et le *drame* (XOR, Minsky), pas la technique.
- **Arbres de décision (ID3, CART)** : placés au M1 comme **figure de transition** (règles lisibles mais *apprises* → illustre le pont GOFAI/ML).
- **Interactivité M1** : fortement candidat (minimax, A*, système expert qui déroule ses règles, perceptron qui ajuste ses poids). Nourrit directement le TN1.

### Catalogue de phares GOFAI (à trier par épisode — au moment de rédiger)
- **Recherche / résolution de problèmes** : espaces d'états, minimax, élagage alpha-bêta, A*, analyse moyens-fins (GPS, Newell & Simon), Deep Blue (1997)
- **Logique** : logique formelle (Boole, Frege), résolution et unification (Robinson), Prolog / programmation logique
- **Planification** : STRIPS, SHRDLU (Winograd, monde des blocs)
- **Contraintes** : satisfaction de contraintes (CSP)
- **Règles / expertise** : systèmes de production, algorithme RETE, systèmes experts (MYCIN), goulot d'étranglement de la connaissance
- **Représentation des connaissances** : réseaux sémantiques (Quillian), frames (Minsky), scripts (Schank), dépendance conceptuelle, CYC (Lenat), problème du sens commun
- **Langage / dialogue (illusion de compréhension)** : ELIZA (Weizenbaum 1966, « effet ELIZA » → ép. 3), PARRY (pendant paranoïaque), STUDENT (problèmes d'algèbre en mots), SHRDLU (Winograd, monde des blocs → ép. 4)
- **Outils / substrat** : Lisp (McCarthy 1958, langage du GOFAI → ép. 3) ; machines Lisp et leur krach (~1987, déclencheur du 2e hiver → ép. 6) ; Samuel's Checkers (1959, machine qui apprend aux dames — petite graine RL)
- **Zone-pont GOFAI ↔ ML** : arbres de décision ID3 (Quinlan) / CART (Breiman) [→ M1], réseaux bayésiens (Pearl 1988)
- **Fondations** : Turing (test, machine universelle), Dartmouth (1956), perceptron (Rosenblatt 1958), Minsky & Papert (1969), hivers de l'IA

## 6. Module 2 — Apprentissage automatique (refonte de fond)

> **Note de refonte (séance de conception M2)** — Le M2 est le module le plus riche en matériel *original* de Christian (≈17 000 mots, applets maison), mais son **fil conducteur est le maillon faible**. La refonte ci-dessous a été décidée après relecture intégrale de la v1 ; elle *réassemble* le matériel existant plutôt que de le jeter. Les pages dont Christian est fier (`30-les-données`, `35-kNN`) sont préservées et **mises en valeur**, pas diluées.

### Diagnostic v1 (établi à la relecture)
Beaucoup de bon matériel, mais cinq problèmes structurels concrets :
1. **La page 10 livre tout le pipeline d'un coup, en mots, sur le pire exemple.** Le scénario téléviseurs nomme déjà modèle/paramètres/erreur/entraînement/inférence/généralisation — mais abstraitement, sans rien à manipuler, et avec la **vision** (6 M de dimensions, le cas le plus dur) comme premier exemple. Puis ce pipeline n'est **jamais réutilisé comme colonne**.
2. **Le cœur conceptuel — la généralisation — est enterré et éparpillé.** Sur-apprentissage / biais-variance / erreur train-test est aujourd'hui une *sous-section de la page kNN (35)*, introduite avant tout modèle réellement entraîné. Aucun foyer propre.
3. **« Apprendre = minimiser une erreur par descente de gradient » arrive tard et en double** : enfoui dans les `details` optionnels de la page 60, **expliqué deux fois** (logistique + linéaire).
4. **Deux pages définitionnelles/taxonomiques tuent l'élan** juste avant la page-monstre : `40-modèles` (polysémie, jusqu'à la théorie des modèles en logique) et `50-paradigmes` (supervisé/non-sup., paramétrique/non-param., inductif/transductif) — exactement le classement « par paradigmes » rejeté, et trop académique pour des non-informaticiens.
5. **Redondance + matériel mal placé** : les **plongements lexicaux** sont traités deux fois (`30` et `37`) et renvoient eux-mêmes au M4 (→ ils y appartiennent) ; la descente bits → CPU → langages (`30`, applet `cpu-simulator`) est un long détour *non-ML* avant que le ML commence.

### Décision : refonte complète, colonne = **le flux de travail ML**
Principe organisateur : **données → modèle (fonction réglable) → entraînement par minimisation d'une erreur → vérification de la généralisation**. Enseigne un *modèle mental transférable* qui démystifie le ML en entier (mieux qu'une taxonomie « par paradigmes », un « zoo » d'algos, ou un narratif pur). Les algorithmes deviennent des *illustrations* dans ce squelette. Supervisé/non-supervisé = une **bifurcation** (la cible est présente ou absente), pas la colonne. **Raccord M1** : la dernière phrase du M1 (*« apprendre, c'est chercher dans l'immensité des réglages d'un modèle »*) annonce déjà la descente de gradient — l'épine dorsale du M2.

### Trois décisions de conception (forks tranchés)
1. **Exemple-fil** : la **vision en *bornes*** (accroche page 10 + ouverture vers les CNN du M3), pas comme substrat. Le fil de travail des étapes 20→70 est un **exemple tabulaire unique et réaliste — la maison** (déjà présente dans `30`), qui sert *à la fois* la régression (prédire le prix) et, étiqueté, la classification. Motif : la vision motive bien *pourquoi le ML existe*, mais sa donnée n'est pas intuitive, n'est pas manipulable dans les applets (tous en 2D), et force de toute façon un basculement vers le tabulaire.
2. **Plongements lexicaux → M4** : au M2 on ne plante que la **graine** (mots → vecteurs → sac de mots, juste ce qu'il faut pour le TN2 pourriels). Les embeddings denses sont au M4, qui les traite déjà.
3. **Niveau math** : **intuition géométrique + une seule** explication propre de la descente de gradient (à l'étape 50, réutilisée sans re-dérivation à l'étape 60). Le reste (entropie croisée, inversion de Bayes, formules de gradient) en optionnel clairement balisé ou en liens.

### Structure cible : **fil continu « construire en butant sur des obstacles »**
Pas de pages « préparatoires » abstraites : chaque concept **naît quand un obstacle le rend nécessaire**, et **la fin de chaque page motive la suivante**. Rédiger *dans l'ordre*, section (`##`) par section.

| Nouvelle page | Source v1 | Action | Obstacle qui motive la suite |
|---|---|---|---|
| `_index` | `_index` | mettre à jour (objectifs, éval. inchangée : TN2 Bayes pourriels) | — |
| `10` **Le problème** (accroche, sans déballer le vocabulaire) | `10-scénario` + contraste prog./ML de `20-différence` | réduire ; vision = image d'ouverture | « comment une machine pourrait-elle *prédire* ça ? » |
| `20` **Le modèle le plus bête** (prédire la moyenne/majorité — déjà un modèle ; *baseline*) | — | **nouveau** | il ignore l'entrée |
| `30` **Regarder les données** (attributs, vecteurs, espace haute-dim, table de maisons) | `30-données` | élaguer bits→CPU→langages ; sortir embeddings → M4 | comment se servir de ces attributs pour prédire ? |
| `40` **Prédire par ressemblance** (kNN + similarité/distance) | `35-kNN` + `37-similarité` | fusionner ; **sortir biais-variance → 70** ; embeddings → M4 | lourd à l'inférence, aucun « apprentissage », rien de compressé en paramètres |
| `50` **Un modèle qui s'entraîne** (régression linéaire + fonction d'erreur + **descente de gradient**) | moitié « régression » de `60` | **cœur** ; gradient expliqué **une seule fois** ici | et pour prédire une *catégorie* ? |
| `60` **Classer** (régression logistique, puis Bayes naïf génératif) | moitié « classif » de `60` | alléger la math ; réutilise la descente de gradient | marche-t-il sur des données *neuves* ? |
| `70` **Généraliser** (train/test, sur-/sous-apprentissage, biais-variance) | extrait de `35` | **nouveau foyer** (enfin à sa place) | de quel *signal* a-t-on appris ? |
| `80` **De quel signal apprend-on ?** (supervisé / non-supervisé `k-means` / **renforcement**) | `50-paradigmes` + `70-non-sup.` | remplacer la taxonomie par la bifurcation à 3 branches | (RL) → fleurit au M3 |
| `99` **TN2** (Bayes naïf / pourriels en Sheets) | `99` | garder | — |

- **Disparaissent comme pages autonomes** : `40-modèles` (la distinction utile *architecture / paramètres / hyperparamètres* → petit encadré à l'étape 50 ; le reste, polysémie stats/sciences/logique, coupé) et `50-paradigmes` (taxonomie → devient la bifurcation `80` ; paramétrique/non-param. et inductif/transductif **coupés** comme trop académiques).
- **Graine RL** (étape 80) : l'idée seulement (agent, action, récompense, essai-erreur, exploration), exemple simple **non-profond** (souris dans un labyrinthe / gridworld), tease AlphaGo. Pas d'algos (Q-learning, etc.). Fleurit au M3.
- **Applets réutilisés tels quels** : `knn` (40), `linear-regression` + `linear-regression-with-springs` (50), `logistic-regression` (60), `kmeans` (80). L'ossature interactive existe déjà ; le travail est surtout **rédactionnel**.

### État de la rédaction (mise à jour 2026-06-30)
**Pages rédigées, refondues et committées** (fichiers en `<poids>-<slug>` **sans accent**, slugs idem) :
- `10-le-probleme` ✅ · `20-modele-le-plus-bete` ✅ · `30-les-donnees` ✅ · `40-predire-par-ressemblance` ✅ · `50-entrainer-un-modele` ✅ · `60-classer` ✅ · `70-generaliser` ✅ · `80-trois-facons-d-apprendre` ✅
- **Restent** : `99` TN2 (renommage `99-travail-note-2.md`), `_index` (à rafraîchir). **Toutes les pages de contenu du M2 sont rédigées.**
- Anciennes pages *supprimées* : `60-apprentissage-supervisé.md`, `70-apprentissage-non-supervisé.md`. Encore en ancien format : `99-travail-noté-2.md`.
- L'ancienne `60-apprentissage-supervisé.md` est **supprimée** ; tous les liens entrants (assistants, module3, TN2) repointent vers `60-classer` (ancres : régression logistique `#tracer-une-frontière--la-régression-logistique`, NB gaussien `#renverser-le-problème--la-classification-bayésienne`, multinomial/pourriels `#le-cas-des-pourriels`).

**Conventions visuelles établies** : SVG parchemin maison (fond `#efe7d3`, accents teal `#2f6f6a` / brun `#9a5b33` / rouge erreur `#c4564a` ; bleu classif. `#3a6ea5`). **Aucun label texte ne touche un élément graphique** (voir mémoire). Fil maison (tabulaire) ; vision en bornes ; embeddings → M4 ; math en `{{% details %}}`. SVG complexes générables par script (cf. cuvette 3D, schémas `suivre-vs-separer` et `qui-je-ressemble` : `rsvg-convert` pour prévisualiser, pas de cairosvg).

**Page 60 « Classer » — telle que rédigée** : intro + schéma SVG `suivre-vs-separer` (droite qui suit vs sépare) ; §2 régression logistique (discriminatif, applet) ; §3 Bayes naïf (génératif, schéma SVG `qui-je-ressemble`, contraste discriminatif/génératif = **graine M4**) ; §4 « Le cas des pourriels » (sac de mots + multinomial, image `spam_vector_space.png`, pont TN2) ; §5 « Et sur des données neuves ? » (obstacle → page 70).

**Page 70 « Généraliser » — telle que rédigée** : §1 intro (appris vs retenu) ; §2 « Un modèle se juge sur ce qu'il n'a jamais vu » (jeu de test, analogie examen, encadré validation/hyperparam., SVG `jeu-de-test`) ; §3 « Trop coller, ou trop lisser : le compromis biais-variance » (applet kNN ré-embarqué + image `bias-vs-variance-with-errors.png`, courbe en U, universel, encadré énigme sur-paramétrisation → M3) ; §4 « Paramétrique ou non-paramétrique » (SVG `parametrique-vs-non`) ; §5 « Tout cela portait un nom : l'apprentissage supervisé » (nomme le supervisé, pont p.80 sur le **signal**). Question 3 du TN2 repointée vers `#paramétrique-ou-non-paramétrique`.

**Page 80 « Trois façons d'apprendre » — telle que rédigée** : §1 intro (le **signal** ; 3 familles) + opener SVG `trois-paradigmes` (3 panneaux) ; §2 le supervisé (récap) + **aparté info « l'étiquetage, une industrie »** (Mechanical Turk/Scale AI → M4/RLHF, M5 éthique) ; §3 le non-supervisé (k-means, applet `kmeans.html`, fléchages autoencodeurs M3 / plongements M4) ; §4 le renforcement (**nouvelle applet `reinforcement.html`** — gridworld Q-learning, testée : politique optimale en 10 pas ; rappel M1/AlphaGo ; deep RL → M3, RLHF → M4) ; §5 « Un même squelette, d'un bout à l'autre » (clôture du module, pont M3/M4).

**M2 — premier jet complet** ✅ — toutes les pages de contenu (10→80), l'`_index` et le TN2 sont en place et rendus en 200. ⚠️ **Mais le M2 est ré-ouvert** : décision du 2026-07-10 d'en faire le **socle théorique complet du cours** (voir la sous-section « Extension » en fin de §6). Le premier jet reste valide ; on l'**étend**, on ne le refait pas.
- **TN2** : conservé tel quel (exercice Sheets, Bayes multinomial) ; liens page 60 + question 3 (→ page 70) corrigés. **Décision : PAS de renommage** — les 5 travaux notés du cours partagent la convention accentuée `99-travail-noté-N.md` (cohérence de série > convention sans-accent des pages de contenu).

**`_index.md` du M2 — refondu, avec 3 visuels maison** :
1. `regles-vs-exemples.svg` — le **renversement** programmation classique / AA : à gauche `règles`+`données` → *programme (algorithme)* → `réponses` ; à droite `données`+`réponses` → *apprentissage (algorithme)* → `règles (le modèle)`. Codage couleur (règles brun / réponses teal permutent) ; `données` en haut des deux panneaux (invariant ancré). Précédé d'un § qui explicite l'inversion.
2. `fil-conducteur.svg` — **l'épine dorsale** : `données`(nuage) → `modèle`(boîte-fonction *f* + 2 sliders) → `erreur`(cible manquée) → `généraliser`(point neuf « ? »), avec **boucle d'entraînement** teal (erreur→modèle, « régler les paramètres pour minimiser — et répéter »). Placé sous la phrase-pipeline.
3. **Carte du cours (Venn imbriqué)** — après itérations, la piste `carte-ia.svg` (Euler générique) a été **abandonnée** au profit du diagramme fait main **`ai-venn.svg`** (maître, avec sigles « IA » / « AA » et labels aérés), décliné en **versions par module** ne gardant que le repère du module concerné : `module1/ai-venn.svg` (→ IA classique) dans l'`_index` M1, `module2/ai-venn.svg` (→ apprentissage automatique + méthodes d'AA diverses) dans l'`_index` M2 ; la page de présentation générale (`10-présentation`) pointe vers le maître `ai-venn.svg`. ✅ **FIL carte-IA : résolu.**

- **Reste, hors M2** : côté Christian, réétiqueter `nf_house.png` (`x1 prix` → `x1 superficie`). Prochaine grande étape du cours : **Module 3** (réseaux de neurones).

### Extension : le M2 comme **socle théorique complet du cours** (décidé 2026-07-10)

**Mandat (Christian)** : le M2 n'est pas qu'une galerie de modèles — c'est **la base théorique de tout le reste du cours**. Il doit exposer *tous* les concepts classiques du ML : capacité, généralisation, surapprentissage, **fuite de données**, etc.

**Audit de couverture** (grep sur tout le M2, 2026-07-10) :
- **Absents** : fuite de données (*data leakage*), régularisation, validation croisée, métriques (précision / rappel / matrice de confusion), normalisation / mise à l'échelle, arbres de décision ; le terme *non-linéaire* n'est **jamais** employé.
- **Présents mais implicites (à nommer/cadrer)** : capacité/expressivité (linéaire vs non-linéaire), hyperparamètre (vs paramètre), malédiction de la dimension.
- **Solidement couvert** : baseline, kNN, régression linéaire, régression logistique, Bayes naïf, k-means ; fonction d'erreur + descente de gradient ; train/test + ensemble de validation, biais-variance, sur-/sous-apprentissage ; supervisé/non-supervisé/renforcement.

**Cadre unificateur retenu** : une seule question — *quelle forme de frontière un modèle peut-il seulement dessiner ?* — à **deux facettes sœurs** : **expressivité** (peut-il se courber ? plafond = XOR, **indépendant** du bruit et de la quantité de données) et **réglage** (combien le laisser se courber ? biais-variance + régularisation).

**Décision de structure (option B — la méthodologie devient un bloc à part entière)** — refonte de la fin du M2 :
- **`70` « Généraliser »** regroupe désormais **le triptyque de la capacité** : (a) **capacité / expressivité — linéaire vs non-linéaire** (*nouveau* ; emblème = **XOR** ; nuance-clé : ≠ affaire de bruit, c'est un plafond d'expressivité) ; (b) biais-variance (déjà rédigé) ; (c) **régularisation** (*nouveau* — le **levier** qui déplace le modèle le long du U ; nuance-clé : garder le modèle riche mais **pénaliser** sa complexité, ≠ choisir un modèle plus simple ; ridge/lasso nommés en passant ; prépare *weight decay* / *dropout* / *early stopping* au M3, et l'énigme de la sur-paramétrisation déjà teasée p. 70).
- **Nouvelle page « Bien évaluer un modèle »** (méthodologie) : **fuite de données**, **validation croisée** (k-fold), **métriques** (précision / rappel / matrice de confusion — motivé par le **spam du TN2** : un faux positif ≫ un faux négatif). Distincte de « Généraliser ».
- **À placer/trancher** : normalisation / mise à l'échelle (p. 30 ou 40 ; importe pour la distance de kNN et la descente de gradient), **arbres de décision** (sous-section ? optionnel ; seul grand modèle classique manquant, et non-linéaire limpide), **hyperparamètre** (à nommer explicitement, lié à l'ensemble de validation).

**Arc XOR sur trois modules** (le « suivi approprié » du XOR évoqué au M1) :
1. **M1** (`60-hivers`) — le XOR tue le perceptron simple (1969) ; dette **explicitement ouverte** vers le M3 (empiler les couches + rétropropagation, 1986).
2. **M2** (p. 70, section capacité) — le XOR **nomme** la limite : *aucune droite ne sépare l'un-ou-l'autre-mais-pas-les-deux*, **même avec un jeu parfait et infini**. Échappatoire classique = kNN (frontière locale non-linéaire). Posé comme « pendant ce temps, du côté de l'AA classique… » — **pas** le dénouement.
3. **M3** — un réseau à **couche cachée** *apprend* la frontière non-linéaire et **solde la dette** (1969 → 1986). ← à honorer lors de la refonte du M3.

**Méthode de rédaction** : section par section, validée par Christian.

#### Avancement de l'extension

- ✅ **p. 70 § « Linéaire ou non-linéaire : ce qu'un modèle peut dessiner »** — rédigée (commit `1ad0d87`), insérée **entre** le jeu de test et le biais-variance (l'expressivité avant le réglage), avec le visuel `xor.svg` (deux droites qui traversent le plan et échouent). Contient les deux échappatoires classiques (modèle non-linéaire ; caractéristique fabriquée $x_1\cdot x_2$) et le renvoi au M3. L'ouverture du biais-variance a été raccordée à la capacité.
- ⏭️ **Reste sur la p. 70** : la **régularisation** (3ᵉ volet du triptyque), à souder juste après le biais-variance.
- ⏭️ **Puis** : la nouvelle page « Bien évaluer un modèle ».
- 🔚 **En dernier, une fois tout le M2 rédigé — refaire les « Objectifs » du `_index`** (demandé par Christian, 2026-07-29). Ils datent d'avant l'extension et ne mentionnent **rien** du socle théorique qu'on vient d'y installer : ni capacité / linéaire vs non-linéaire, ni surapprentissage, ni régularisation, ni fuite de données, ni validation croisée, ni métriques. Ils listent aussi « régression, classification » comme s'il s'agissait d'*algorithmes*, alors que le module en fait désormais deux **natures de tâche** (décidées par la cible, p. 30). À reprendre **à la fin**, quand le contenu réel sera figé — pas avant, sous peine de les réécrire deux fois. Vérifier du même coup la ligne « fil conducteur » (elle dit *généralisation* là où le schéma dit *généraliser*) et la section **Durée** (3 semaines / 27 h) si le module s'alourdit d'une page.

### Chantier parallèle : adoucir le passage régression → classification (2026-07-27)

**Problème signalé par Christian** (en relisant le M2 d'un trait) : la classification surgissait **trop brusquement** p. 40. Diagnostic sur pièces : la p. 10 ouvre pourtant sur des exemples qui sont *tous* de la classification (chat, pourriel), puis les catégories **disparaissent** des p. 20 et 30 (zéro occurrence), avant de resurgir p. 40 comme si elles allaient de soi. Le lecteur avait été formaté « prédire = un nombre » pendant deux pages.

**Solution retenue** (commit `b46c760`) — faire naître la dualité **avec le fil rouge**, et n'amener le vocabulaire que là où il sert :

1. **p. 10 — l'intuition, sans aucun mot technique.** Nouvelle section `##` « Une seconde question, d'une tout autre nature », placée **après** le nuage de la régression. Même table, une colonne de plus : **« Vendue en moins de 30 jours ? »**. Points-clés : mêmes maisons, mêmes renseignements, réponses de nature différente (« on ne peut pas faire la moyenne de *oui* et de *non* ») ; et **le prix devient une entrée** pour la seconde question — *ce qui était la réponse devient une description*. Visuel `maisons-vendues.svg` (points bleu/rouge) : « ce n'est plus la hauteur du point qu'on cherche, mais sa couleur ». La couleur est présentée comme un simple **expédient d'encombrement**, avec une amorce (« on verra bientôt qu'on peut faire mieux »). *(Les axes de ce visuel ont changé depuis — voir « Le jeu canonique de maisons » ci-dessous.)* **Le fil rouge lui-même a été recadré** (commit `9a6a26a`) : ce n'est plus « le prix » mais **le jeu de maisons** — section renommée « Notre fil rouge : des maisons à vendre », ouverture sur « un registre de ventes immobilières […] auquel nous poserons plus d'une question », le prix devenant « la première question » ; photo d'ouverture `maison-a-vendre.jpg` (Kindel Media / Pexels, crédit en légende) ; et correction d'une promesse **fausse** — le prix ne domine que les *prochains* chapitres, la classification prend le devant en p. 60 et porte le TN2.
2. **p. 20 — les deux bêtises jumelles** (commit `9a6a26a`). Nouvelle section « La même bêtise, pour l'autre question » : on ne peut pas moyenner *oui* et *non*, donc la bêtise équivalente est **la réponse la plus fréquente** — c'est la **baseline de classification**, qui manquait au module. Le jumeau a lui aussi **un unique paramètre** (obtenu en comptant plutôt qu'en moyennant) ; l'étalon vaut pour les deux tâches (60 % à battre) ; et un **encadré d'avertissement** montre que « ce n'est jamais un pourriel » obtient **99 %** de bonnes réponses dans une boîte à 99 % légitime — flatteur et parfaitement inutile. Cet encadré **sème le besoin de vraies métriques** : il motive d'avance la page « Bien évaluer un modèle ». Vocabulaire tenu — les deux tâches ne sont toujours pas nommées ici.
3. **p. 30 — le vocabulaire, à sa place.** Nouvelle sous-section `###` « Et quand la cible est une catégorie ? », juste après la définition de la **cible**. Encodage **oui = 1 / non = 0** (avec son arbitraire), puis visuel `troisieme-dimension.svg` (perspective : le plan du nuage colorié au sol — *distance × année* depuis le 30 juillet —, la cible sur un troisième axe **à deux barreaux** ; *depuis le 2026-09-10, la vue en perspective vit en p. 10, avec des barreaux « non » / « oui » (`troisieme-dimension-oui-non.svg`) et l'ombre des deux exceptions sur l'autre plan ; la reprise en p. 30 avec des barreaux 0 / 1, tentée deux jours, a été retirée le 09-12 — elle ne changeait que deux étiquettes, la p. 30 le dit en une phrase* ; *vu d'en haut, on retrouve le nuage colorié de la p. 10 — la couleur en était l'ombre portée*). **Garde-fou de vocabulaire** : « quand nous parlerons des *dimensions* d'un objet, il s'agira toujours des caractéristiques ». Enfin, **nomination des deux tâches : régression et classification**.
4. **p. 40 — pure reprise.** Le passage n'introduit plus rien (ni la dualité, ni les mots) : « Nous venons de faire une régression… Et pour une classification ? Il suffit de changer la toute dernière étape. »

**Décisions de conception à retenir** :
- **Choix de la cible catégorielle** : « vendue en moins de 30 jours » l'emporte sur « abordable/chère » (un prix mis en cases, donc une fausse catégorie), sur « maison/condo » (aucune motivation à la prédire) et sur « rénovations majeures » (signal porté par la seule année). Son apparent défaut — dépendre du prix — est **son atout** : le prix étant dans la table, il devient une *entrée*, ce qui illustre gratuitement la notion de variable cible. *(Depuis le 30 juillet, la catégorie n'est plus pilotée par le prix mais par la distance au centre et l'année — le prix reste une entrée « comme les autres », l'argument tient.)*
- **Où nommer** : les noms *régression/classification* appartiennent à la **nature de la cible** (p. 30, page du vocabulaire), **pas** à un algorithme (p. 40) — les y placer ferait croire à « les deux modes de kNN », et alourdirait justement la page dont on voulait adoucir l'entrée.
- **Cohérence** : « abordable/chère » a été **éliminé de tout le module** ; le visuel `knn-regression-vs-classification.svg` affiche désormais « vendue vite ».

**Corrections collatérales** (même vague, commits `123a3ae` → `d16f7ba`) :
- `module2/30` — **`nf_house.png` refait** : l'image présentait le **prix comme un axe de l'espace des caractéristiques**, en contradiction directe avec le paragraphe qui, quelques lignes plus haut, en fait la *cible*. Désormais `x1 = superficie`, `x3 = # de chambres`, `xn = # de salles de bain` (ordre de la table et de la notation vectorielle), plus deux maisons-exemples dont les vecteurs `{180, 1995, 4, … 2}` et `{220, 2010, 5, … 3}` sont **les lignes 1 et 3 de la table**. Texte alternatif refait (il annonçait encore « taille du terrain »).
- `10-présentation` — bascule vers `ai-venn.svg` + texte alternatif descriptif (vérifié **sur le rendu** : le Module 2 a deux flèches, le Module 5 vise tout le paysage).
- `25-professeurs` — photos des trois auteurs ; `module1/40` — incise « oui, je peux passer le sel! » ; `module2/_index` — généralisation nouée à l'intelligence + vache mieux amenée.
- ⚠️ **Le corpus n'a pas de convention arrêtée sur l'espace avant « ! »** (14 collées / 12 espacées) — si on uniformise un jour, c'est une passe unique sur tout le cours.

### Le jeu canonique de maisons (2026-07-30 → 08-01)

**Problème découvert** en traitant un point ouvert (le « 60 % » de la p. 20 ne collait pas au nuage) : les figures du fil rouge **ne partageaient pas les mêmes données**. `nuage`, `baseline`, `erreurs`, `droite`, `erreurs-droite` utilisaient dix maisons (celles des tables) ; `maisons-vendues` en avait vingt et une, inventées à part avec deux bandes de prix. Deux conséquences : la p. 10 disait « exactement le même dessin » à faux, et aucun découpage de 21 points ne donne 60 %.

**Solution** — `scripts/gen_maisons.py` est la **source de vérité unique** : 20 maisons `(superficie, année, distance au centre, prix, vendue vite)`, d'où sont régénérées **huit figures** (`maisons-nuage`, `-vendues`, `-baseline`, `-erreurs`, `-erreurs-oui-non`, `-droite`, `-erreurs-droite`, et `troisieme-dimension` via `gen_troisieme_dim.py` qui l'importe). Invariants garantis **par construction**, chacun correspondant à une affirmation du texte :
- les **quatre maisons des tables** de la p. 10 y sont avec leurs valeurs exactes (la p. 30 en reprend deux comme vecteurs dans `nf_house.png`) ;
- **prix moyen = 500 k$** pile (la droite plate de la p. 20) ;
- **12 maisons sur 20 vendues vite = 60 %** pile (l'étalon de la p. 20) ;
- la droite ajustée vaut ≈ 2,98 k$/m², écart max 34 k$ contre 260 k$ pour la droite plate (le contraste de la p. 50).

**Décision de conception centrale — deux plans, deux histoires** (demandée par Christian : « la vue superficie × prix doit rester une droite, et les clusters doivent apparaître avec d'autres variables ») :
- **superficie × prix** : une droite bruitée — le terrain de la régression (p. 10, 20, 50). La catégorie y est **indiscernable** (vérifié : résidus de prix des deux classes imbriqués, [-34, +20] contre [-27, +23]).
- **distance × année** : deux **amas compacts** en coins opposés (proche et récente / éloignée et ancienne), séparés par un large vide, avec **deux rebelles** qui le traversent. C'est le plan de `maisons-vendues` (p. 10), de `maisons-erreurs-oui-non` (p. 20) et du sol de `troisieme-dimension` (p. 30).
- **Pourquoi la distance a dû être ajoutée** : avec un seul renseignement discriminant (l'année), chaque groupe s'étale sur toute la largeur de l'autre axe → des **bandes**, pas des amas ; et resserrer les groupes en superficie trahirait la catégorie dans le plan des prix. Des amas compacts exigent **deux** renseignements discriminants. La colonne « Distance du centre (km) » n'apparaît que dans la **seconde table** de la p. 10, avec la seconde question — ce qui sert le propos : « un renseignement qui ne nous avait servi à rien jusqu'ici, et qui va se révéler décisif ».
- **Leçon rendue explicite** en p. 10 (nouveau paragraphe) : la seconde question ne se lit pas dans les mêmes axes que la première ; *la difficulté d'un problème tient souvent moins à la machinerie qu'au choix de ce qu'on décide de regarder* — graine pour la p. 30 (caractéristiques) et la capacité (p. 70).

**Figures et textes touchés** : `maisons-erreurs-oui-non.svg` (nouveau, p. 20 : le jumeau peint tout en « oui », ✗ rouges fins sur ses ratés — posés *sur* les points, sans halo, la légende dit « prédiction du modèle : « oui », vendue en moins de 30 jours ») ; p. 20 § « Leur défaut, et ce qu'il révèle » (pluriel — couvre les deux modèles ; nouveau paragraphe : *les erreurs ne sont pas dispersées au hasard*, donc prévisibles, donc corrigibles) ; passe de cohérence sur toute la p. 20 (contraste studio/manoir → neuve-près-du-centre/bicoque-en-banlieue pour la question oui/non ; « dépasse 250 000 $ » plutôt que « des centaines de milliers ») ; p. 10 « tirées du même registre » plutôt que « décrites par les mêmes renseignements » (devenu faux avec la distance).

**Aussi dans la même période** (`_index` du M2, 29 juillet) : le connexionnisme explicité avec renvoi au M1 ; nouveau visuel `memoriser-vs-apprendre.svg` (une image se présente → est-elle parmi les 1000 ? oui = trivial, non = tout l'enjeu ; une première version « classeur vs curseurs » a été écartée comme exigeant des métaphores absentes du texte) ; `fil-conducteur.svg` glosé aux quatre stations, recentré sur la *prédiction* ; l'énoncé de l'épine dorsale aligné à ses deux occurrences (`_index` et p. 80).

**Relecture complète du M2 par Christian (en cours depuis le 2026-09-09)**, page par page, avec corrections au fil de l'eau :
- **Style** : passe sur les **tirets cadratins** sur tout le M2 (314 → 41, ≈ 2 / 1 000 mots ; règle en mémoire). Le M1 (250 tirets) attend la même passe, à faire quand Christian le relira.
- **p. 10** : « se tromper » n'a pas le même sens en régression et en classification ; une catégorie n'a pas forcément deux valeurs ; la vue en perspective (`troisieme-dimension-oui-non.svg`) arrive dès la p. 10, avec l'ombre des deux exceptions sur l'autre plan.
- **p. 20** : figure des ratés du prédicteur majoritaire (`maisons-erreurs-oui-non.svg`) ; le paramètre du modèle bête n'est pas arbitraire, il est calculé et il fait sens ; section de clôture au pluriel (les deux modèles, et « les erreurs ne sont pas dispersées au hasard »).
- **p. 30** : schéma entrée → modèle → sortie **version classification** (`modele-entree-sortie-categorie.svg`, le prix passé côté entrée) ; la reprise du relief avec 0 / 1 a été **retirée** ; nouveau passage « et un texte ? » avec le plan de deux mots du vocabulaire (`courriels-deux-mots.svg`), puis l’espace complet du vocabulaire en éventail (`courriels-vocabulaire.svg`, généré par `scripts/gen_courriels_vocabulaire.py`) : vignette du courriel reliée à un panneau agrandi, calque exact de `nd_house.png` ; puis un paragraphe compte vs présence (axe entier vs axe 0/1) ; intuition préparant le sac de mots de la p. 60.
- ***Prédire par ressemblance*** (`40-…`) : la distance écrite, de Pythagore aux pixels (deux formules MathJax ; règle CSS pour que les formules affichées défilent dans leur cadre sur écran étroit) ; la **frontière de décision** nommée et définie sur nos maisons, avec le fond teinté par la réponse de kNN (`maisons-frontiere-k3.svg` avant l'applet, `maisons-frontiere-k1.svg` dans « Le choix de k » ; générateur `scripts/gen_maisons_frontiere.py`, importe le jeu canonique).
- ***Un modèle qui s’entraîne*** (`50-…`) : les prix du jeu canonique ont été **rebruités** (résidus de ±35 à ±60 k$ au lieu de ±20) pour que les écarts à la droite se voient ; la moyenne reste exactement 500 k$, les 4 maisons de la table sont inchangées, l’écart max du modèle plat reste > 250 k$ (303), pente ≈ 2,96 k$/m². Toutes les figures « maisons » regénérées.
- ***Classer*** (`60-…`) : l’approche générative mène explicitement aux LLM et à ChatGPT (portrait de la classe « texte écrit par des humains »).
- ***Généraliser*** (`70-…`) : encart *warning* « La règle d’or, à l’échelle d’aujourd’hui » : pour un LLM on ne sait plus ce qu’il a vu (données d’entraînement gigantesques, examens qui ont circulé sur le Web), donc méfiance devant les scores ; mémoire vs compréhension comme question ouverte, rappel de la 1001ᵉ image. **Fil à reprendre au M4** (contamination des bancs d’essai, « sait déjà » vs « apporte de nouveau »).
- ***Généraliser*** : nouvelle section **régularisation** entre biais-variance et paramétrique ; le polynôme (degré, un paramètre par terme) y est introduit en une phrase, la mention des arbres de décision a été retirée des curseurs de souplesse (notion jamais introduite) ; industrie de l’étiquetage (Scale AI, Appen, Sama, Labelbox, Mechanical Turk) dans la section supervisé.
- **Outillage** : thème hugo-book passé à `main` (sélecteur de thème, ancres qui ne dérivent plus grâce aux dimensions d'images et aux hauteurs d'applets, superviseur du serveur). Voir la mémoire.

**État au 2026-09-13** : arbre de travail **propre**, tout commité et poussé sur `v2`. Christian a relu jusqu’à *Prédire par ressemblance* inclus et attaque *Un modèle qui s’entraîne* ; restent ensuite *Classer*, *Généraliser*, *Trois façons d’apprendre*. La **régularisation** est écrite (section « Garder un modèle riche, mais le tenir en laisse », 3ᵉ volet du triptyque, figure `regularisation.svg` par `scripts/gen_regularisation.py` ; l’encart « énigme » la clôt). La page **« Bien évaluer un modèle »** (`75-bien-evaluer.md`, 2026-09-14) est écrite : fuite de données (+ encart mise à l’échelle), validation croisée (+ *hyperparamètre* nommé), métriques (matrice de confusion, précision/rappel, seuil, erreur absolue moyenne), puis **en / hors distribution** (parallèle avec l’échantillonnage des sondages et le *Literary Digest* 1936 ; extrapolation, changement de population, dérive dans le temps ; figure `hors-distribution.svg`) ; les deux erreurs rattachées à Neyman-Pearson, précision/rappel à la recherche d’information ; figure `precision-rappel.svg` ; la section « Tout cela portait un nom » y a migré depuis *Généraliser*. Figures : `fuite-de-donnees.svg` et `jeu-de-test.svg` (`gen_jeu_de_test.py`), `validation-croisee.svg`, `matrice-confusion.svg`. Normalisation et hyperparamètre sont donc placés. **Arbres de décision** : page à part **« Poser des questions : les arbres de décision »** (`65-arbres-de-decision.md`, 2026-09-14), entre *Classer* et *Généraliser* : une question suffit presque (les 20 maisons ; égalité distance/année révélée), comment l’arbre choisit (pureté, Gini en encart, recherche gloutonne = 3ᵉ façon d’apprendre), arbre de régression en escalier, profondeur et élagage + **applet `decision-tree.html`** (hauteur 605), l’arbre du *Titanic* (vraies données, `scripts/data/titanic3.csv`, 78,8 %), lisibilité / instabilité / forêts. Apprenant CART en Python pur : `scripts/arbre.py`. **La charnière « Et sur des données neuves ? » a migré de *Classer* à la fin de cette page** (continuité vers *Généraliser*) ; raccords posés dans *Généraliser* (XOR en deux questions, profondeur parmi les curseurs, élagage) et *Trois façons d’apprendre*. Ordre du M2 : 10 → 20 → 30 → 40 → 50 → 60 → **65** → 70 → **75** → 80 → TN2. La page des arbres est relue et validée (2026-09-15) ; explicabilité (XAI, boîte noire) et forêt aléatoire illustrée (`foret-aleatoire.svg`) ajoutées ; sur-apprentissage (*overfitting*) nommé aux endroits-clés ; *Bien évaluer* a reçu les erreurs asymétriques (détecteur de fumée, `erreurs-asymetriques.svg`). **Accueil du M2 refait (2026-09-16)** : parcours en dix pages liées, Objectifs couvrant tout le socle, durée portée à quatre semaines (36 h). Compléments du 2026-09-16 après le tour d’horizon : **auto-supervision** (sous-section de *Trois façons d’apprendre*), **malédiction de la dimension** (encart de *Prédire par ressemblance*), **biais des données** (fin de *Bien évaluer*), **parenté avec la statistique** (section de l’accueil + origine de chaque modèle + clôture de *Trois façons*), **angle des probabilités** (section « Sous les modèles, des probabilités » dans *Classer* : croyance, calibration, maximum de vraisemblance, apprentissage bayésien ; encart « Qu’est-ce que le bruit ? » dans *Généraliser*). Breiman (« Two Cultures », effet Rashomon) en encart dans la page des arbres ; Sutton (« The Bitter Lesson ») en graine à la clôture de *Trois façons d’apprendre*, **à traiter en plein à l’ouverture du M3** (recherche + apprentissage + calcul ; AlexNet/GPU ; rappel possible sur Deep Blue au M1). **Fils à reprendre au M5** (reprise, pas introduction) : Sutton et « l’intelligence n’est-elle que du calcul à grande échelle ? » ; Breiman/Rashomon et « qu’est-ce qu’expliquer ? » ; l’explicabilité et les boîtes noires ; le biais des données ; mémoire contre compréhension chez les LLM (encart de *Généraliser*) ; le socle humain de l’étiquetage. ⚠️ **À réviser avant le début du cours** : la phrase de *Deux paris rivaux* (M1) sur l’IA en mathématiques (IMO 2025, Fermat formalisé en sept. 2026, Navier-Stokes annoncé en sept. 2026 et encore en vérification) vieillira vite. 🔚 **Le Module 2 est bouclé.** Reste, hors M2 : la passe tirets sur le M1 quand Christian le relira ; les fils posés pour le M3 (XOR, régularisation des réseaux, énigme de la sur-paramétrisation, explicabilité) et le M4 (LLM comme portrait génératif, contamination des bancs d’essai, RLHF/RLVR, explicabilité).

**Relecture du Module 1 (en cours depuis le 2026-09-17)**, page par page, avec pour chaque page : passe sur les tirets cadratins (proposée en tableau, validée, puis appliquée), liens sur tous les renvois, et les ajouts demandés par Christian.
- ***Turing*** ✅ : tirets 35 → 10 ; vraie première page de *Mind* 1950 (`turing-mind-1950.jpg`, numérisation) ; le jeu d'abord entre un homme et une femme ; *halting problem* nommé ; machine de Turing complète n ↦ n+1 (`machine-turing-increment.svg`, `scripts/gen_machine_turing.py`) ; castor affairé (*busy beaver*, BB(5) = 47 176 870, Busy Beaver Challenge).
- ***Deux paris rivaux*** ✅ : tirets 17 → 6 ; encart cybernétique (Wiener, rétroaction, note Kubernetes) ; photo des participants de Dartmouth 1956 (IEEE Spectrum, famille Minsky) ; encart « Un mot qui a changé de sens » (IA de 1956 vs LLM) ; encart « Soixante-dix ans plus tard » (IMO 2025, Fermat formalisé, Navier-Stokes en vérification, **à revoir avant le cours**) ; tous les renvois liés.
- ***L'âge d'or symbolique*** ✅ : tirets 34 → 9 ; paragraphe sur la recherche réécrit plus sobre ; graine vers la malédiction de la dimension (et renvoi retour depuis le M2) ; figure minimax et élagage (`minimax-elagage.svg`) ; **applet A\*** contre recherche aveugle (`astar.html`, hauteur 557) ; vidéo de l'abandon de Kasparov (YouTube `EsMk1Nbcs-s`, démarrage à ajuster si demandé) ; renvoi vers Watson.
- ***Représenter le monde*** ✅ : tirets 37 hors dialogue → 7 ; bilan lié (Logic Theorist, Deep Blue, ELIZA) ; web sémantique nommé ; vidéo SHRDLU (`bo4RvYJYOzI`) avec l'image du micro-monde avant (boîte recentrée) ; *tractable* ; figure d'entrées CycL (`cyc-assertions.svg`, exemples réels de la doc CycL).
- ***Capturer l'expertise*** ✅ : lien Module 2 vers « Sous les modèles, des probabilités » ; **applet du moteur d'inférence** (`moteur-inference.html`, hauteur 640) ; encart **logique floue** (Zadeh, `logique-floue.svg`) ; figures des **chaînages avant et arrière** (`scripts/gen_chainages.py`). Page modèle du registre neutre.
- ***Les hivers et la bascule*** ✅ (relue le 2026-10-01) : *Les Chasseurs dans la neige* de Bruegel en ouverture ; **table de vérité du XOR** et renvoi vers *Généraliser* ; **déplacer les poteaux du but** (*moving the goalposts*, `poteaux-du-but.svg`), perroquet stochastique et autocomplétion glorifiée.
- ⬜ Restent à relire : le **travail noté 1** et l'**accueil** du M1.
- **Passes globales sur les modules 1 et 2 (fin septembre 2026)** : toutes les pages réécrites dans le **registre neutre** (`GUIDE-STYLE.md`, contrôle `scripts/verifier_invariants.py`) ; **liens sur tous les renvois** (`scripts/verifier_liens.py`, 0 lien cassé) ; encart **Lean** dans *Deux paris rivaux* ; **recherche** activée ; **livres PDF et EPUB** produits à chaque push (`scripts/livre/`, page « Télécharger le cours en livre ») ; v2 publiée dans `cjauvin/inf1901-teluq-v2`, modules 3 à 5 masqués en ligne.
- **Liens cassés relevés hors M1, non réparés** : 8 ancres mortes (TN2, TN3, TN4, M3 `10-réseaux-de-neurones` et `30-architectures-avancées`, `60-assistants-intelligents`), dont plusieurs dues aux identifiants changés par les espaces insécables (`--` devenu `-`) et à l'ancre Google Sheets (`#parametres-linguistiques` devenue `#paramètres-linguistiques`) ; 2 renvois du M3 vers une section « plongements lexicaux » qui n'existe plus au M2.

**Note d'outillage** : `rsvg-convert` n'est plus installé sur la machine (`brew install librsvg` pour le retrouver). Repli utilisé : `qlmanage -t -s 900 -o <dossier> fichier.svg` (natif macOS), qui produit `fichier.svg.png`. ⚠️ **Piège rencontré** : `python3 gen.py > cible.svg` **tronque la cible à 0 octet** avant même d'échouer si le script est absent — restaurer alors par `git checkout HEAD -- <fichier>`.

## 7. Module 3 — Réseaux de neurones et apprentissage profond

### Diagnostic v1
Contenu : `10-réseaux-de-neurones.md` (2872, **cœur solide** : neurone = généralisation de la régression logistique → pont M2, rétropropagation, deep learning, décomposition hiérarchique, GPU ; applet + hints), `20-3blue1brown.md` (vidéo), `30-architectures-avancées.md` (3610, **fourre-tout monolithe** : CNN, RNN, autoencodeurs, GNN, NTM), `40-aa-adverse.md` (628, mince), `99-travail-noté-3.md` (TF Playground). Problèmes : (1) **aucun Transformer/attention** ; (2) architectures déséquilibrées (exotique traité, essentiel manquant) ; (3) ne porte pas le deep RL ni la floraison du perceptron ; (4) adverse sous-développé.

### Décisions
- **Éclater** `30-architectures-avancées` en pages séparées (CNN | RNN | autoencodeurs | …). Élagage de l'exotique (GNN/NTM) à décider page par page.
- **Transformers : pont au M3, fond au M4.** M3 = *comment la machine est bâtie* : le Transformer en point d'orgue de la séquence **CNN → RNN → Transformer** (la limite du RNN motive l'attention : « regarder toute la séquence en parallèle »), traité **comme architecture**, pas comme chatbot. (Le fond LLM est au M4 ; le M4 ne ré-enseigne pas la mécanique de l'attention.)
- **Intégrer le deep RL** (AlphaGo, DQN/Atari) = floraison de la graine RL du M2.
- **Floraison du perceptron** : la revanche connexionniste (pas seulement « généralisation de la régression logistique », mais le retour de la tradition semée au M1).
- ⚠️ **DETTE À SOLDER — l'arc XOR** (détail complet au §6, « Arc XOR sur trois modules »). Le M1 (`60-hivers`) **ouvre** la dette : le XOR tue le perceptron simple en 1969, et le texte annonce qu'empiler les couches la lèvera en 1986. Le M2 (p. 70, § « Linéaire ou non-linéaire ») **nomme** la limite — *aucune droite ne sépare l'un-ou-l'autre-mais-pas-les-deux, même avec un jeu parfait et infini* — et montre les deux échappatoires **classiques** (modèle non-linéaire comme kNN ; caractéristique fabriquée $x_1\cdot x_2$, trouvée **par l'humain**). Le M3 doit **payer** : un réseau à **couche cachée** apprend *lui-même* la caractéristique qui rend le problème séparable — c'est là toute la raison d'être de la profondeur, et le dénouement 1969 → 1986. Ne pas traiter la rétropropagation sans refermer explicitement ce fil.
- **Récupérer la matière Le Cun** (CNN, deep learning) rapatriée depuis le M1.
- **Étoffer l'apprentissage adverse** (exemples adverses, duper un classifieur d'images).
- **Cœur du fil cerveau ↔ IA** (voir §3) : l'encadré « la carte n'est pas le territoire ».

### Découpage en pages (validé par Christian le 2026-10-01)
Même construction que le M2 : chaque page rencontre une limite qui mène à la suivante. Registre neutre (`GUIDE-STYLE.md`), liens sur tous les renvois, une page à la fois avec validation avant écriture. Module masqué en ligne jusqu'à décision de publication.

1. **Un neurone** — le retour du perceptron ; un neurone = une régression logistique ; applet du neurone ; sa limite (une droite).
2. **Une couche cachée** — le XOR résolu : le réseau fabrique lui-même la caractéristique (solde la dette XOR).
3. **Entraîner un réseau** — la rétropropagation (1986) ; vidéo 3Blue1Brown intégrée (plus de page à part).
4. **L'apprentissage profond** — pourquoi empiler ; hiérarchie, caractéristiques apprises, données, GPU ; ImageNet 2012 ; encadré « la carte n'est pas le territoire » ; **autoencodeurs en courte section** (renvoi vers le M4) ; **Sutton, « The Bitter Lesson »**, à côté des données et des GPU (décidé le 2026-10-02).
5. **Voir : les réseaux convolutifs** — Le Cun, chèques, convolution, ImageNet.
6. **Lire une séquence : les réseaux récurrents** — mémoire, limite sur les longues séquences.
7. **L'attention et le Transformer** — architecture seulement ; pont vers le M4.
8. **Apprendre à jouer : le renforcement profond** — Atari (DQN), AlphaGo (recherche du M1 + apprentissage du M2).
9. **Tromper un réseau** — exemples adverses, boîte noire (contraste avec arbres et systèmes experts).
- **Accueil du module** — à refaire à la fin, quand les neuf pages sont écrites (décidé le 2026-10-02).
- **Travail noté 3** — TensorFlow Playground, à revoir et à vérifier dans le navigateur comme le TN1.

Avancement (2026-10-02) : pages 1 *Un neurone*, 2 *Une couche cachée* et 3 *Entraîner un réseau* écrites (applets `neuron.html`, `xor-deux-droites.html`, `xor-entrainement.html`). Ancienne page 3Blue1Brown supprimée (vidéo de l'épisode 3 intégrée à la page 3) ; ancienne page *Les réseaux de neurones* masquée du menu (`bookHidden`), à supprimer après la page 4. Page 4 *L'apprentissage profond* écrite (2026-10-02), avec Sutton, la double descente, l'encadré sur le cerveau et l'autoencodeur. **Page ajoutée à la demande de Christian : *Le matériel et les outils*** (`42-materiel-et-outils.md`, historique des GPU et de la différentiation automatique, frise, exemple PyTorch), entre la page 4 et les réseaux convolutifs ; le module compte donc dix pages. Page *Voir : les réseaux convolutifs* écrite (applet `convolution.html`, vidéo de Le Cun 1989, photo de Le Cun, échantillon MNIST). Renvois encore sans lien, à relier quand la page existera : « Lire une séquence : les réseaux récurrents » (page des réseaux convolutifs). Règle des figures : tous les schémas de la v1 sont redessinés en SVG parchemin ; seules les photos, documents d'époque et exemples adverses restent tels quels.

Décisions : **GNN et NTM retirés** (au plus un encadré de trois lignes sur les NTM, clin d'œil à Turing) ; **exemple fil conducteur = les chiffres manuscrits** (Le Cun, 3Blue1Brown, exemples adverses). À faire en cours de route : rediriger les liens existants vers `30-architectures-avancées` et `40-aa-adverse` (M1, M2).

## 8. Module 4 — IA générative et LLM

### Diagnostic v1
**Promet plus qu'il ne livre.** `10-IA-générative.md` (288, survol), `20-grands-modèles-de-langage.md` (1020, narration n-grammes → word2vec → RNN/LSTM → Transformers → RLHF, mais 100 % texte, dense), `30-3blue1brown.md` (4 vidéos), `99-travail-noté-4.md` (mini-LLM bigramme en Sheets — déjà hands-on). Trous : (1) versant *génératif-média* (GANs, diffusion, image/vidéo) en un paragraphe ; (2) zéro interactivité ; (3) déséquilibre interne ; (4) possible obsolescence (écrit à l'ère ChatGPT 2022).

### Orientation retenue
- **Intro conceptuelle forte** : l'IA générative comme **paradigme qui transcende les LLM**. Idée unificatrice : au lieu de *discriminer* (classer, comme aux M2/M3), on **modélise la distribution des données pour en échantillonner de nouvelles** (« imiter la source, puis produire du neuf »). Couvre texte, image, vidéo, audio, code. L'image/vidéo (diffusion, GANs) = *illustration de l'ampleur du paradigme*, pas un bloc co-vedette.
- **Cœur = les LLM**, développés au maximum (dominent l'actualité, enchaînent vers le M5).
- **Profondeur LLM = trois aspects équilibrés** : (a) **mécanisme interne** (tokens, embeddings, attention, prédiction du mot suivant ; 3b1b en appui), (b) **du modèle à l'assistant** (pré-entraînement, fine-tuning, RLHF, alignement → pont M5), (c) **usages et phénomènes** (prompting, hallucinations, capacités émergentes, fenêtre de contexte, multimodal, agents — la face « vécue » en 2026).

### Ossature cible
1. `_index` — contexte.
2. **Page 10 — « L'IA générative, un paradigme »** : modéliser/échantillonner une distribution ; tour d'horizon des modalités (texte, image/diffusion, vidéo).
3. **Pages 20-50 — les LLM en profondeur** : éclater la page monolithique (mécanisme / entraînement-alignement / usages), aérer avec visuels + **au moins une expérience manipulable**.
4. **Page 99 — TN** (mini-LLM en Sheets, déjà hands-on).

## 9. Module 5 — IA et société (plus mordant)

### Diagnostic v1
Riche philosophiquement mais pas assez « mordant ». `_index.md` (194), `10-attitudes.md` (1119 — quatre attitudes : libérale / défaitiste-doomer / accélérationniste / transhumaniste), `20-conversation.md` (4521 — bâti autour de la **conversation vidéo de 2h** Lemire & Jauvin, minutée, + 9 sections thématiques), `99-travail-noté-5.md` (528, essai). Problèmes : (1) trop ancré sur un artefact fixe et passif (vidéo 2h) qui **vieillit** ; (2) attitudes intemporelles, pas branchées sur des controverses vives ; (3) engagement passif.

### Pivot retenu : **controverses = colonne, attitudes = lentilles**
Les quatre attitudes ne sont plus le *contenu* mais une **boîte à outils d'analyse** (quatre façons de *lire* un débat). Le contenu devient une série de **dossiers chauds** — points de friction où l'IA percute le réel *maintenant*.
- **Confronter des controverses vives** → les dossiers eux-mêmes.
- **Relief / provocation** → chaque dossier s'ouvre sur une question dérangeante + **prise de position assumée des profs** (fini la neutralité encyclopédique).
- **Actualité non-périssable** → le texte cadre la *tension durable*, l'**étudiant apporte l'instance récente** (veille). Rejoint le TN5.

### Dossiers chauds retenus (cœur du M5)
- **IA, vérité et démocratie** : deepfakes, désinformation, élections, confiance épistémique.
- **IA et travail** : automatisation, emplois, économie, gagnants/perdants.
- **IA, création et propriété** : art génératif, droit d'auteur, devenir de la créativité humaine.
- **Risque, pouvoir et alignement** : risque existentiel, concentration Big Tech, surveillance, sécurité.
- **IA et éducation** : méta/auto-référentiel (des étudiants TELUQ qui utilisent l'IA dans ce cours même : intégrité académique, apprendre avec/malgré l'IA, devenir de l'évaluation). Le seul dossier où l'étudiant est personnellement impliqué → particulièrement mordant.

### Conversation de 2h
Ne pas la jeter (riche, personnelle). La **repositionner** : découpée en segments thématiques branchés sur les dossiers (le minutage existant le permet), comme *une voix parmi d'autres*, pas la pièce maîtresse passive.

## 10. Travaux notés 1 et 5

**Esprit recherché** : la signature des TN2-3-4 est que l'étudiant *manipule le mécanisme lui-même* (calcule, triture, construit), au lieu de « produire un document ». **Forme commune réutilisée** : un « quelque chose » interactif + des **questions interprétatives**.

### TN1 — Système expert en Google Sheets
Substrat : **Google Sheets** (façon TN2/TN4). Mécanisme : **un système expert qu'on trace, casse et étend**.
- On fournit une base de règles `si… alors…` (p. ex. identifier un animal / diagnostiquer une panne).
- L'étudiant **joue le moteur d'inférence** sur des cas : quelles règles se déclenchent, dans quel ordre, jusqu'à la conclusion.
- Puis : **trouver un cas que le système rate** et **ajouter une règle pour le corriger** → fait vivre le *goulot d'étranglement de la connaissance* (porte le récit des épisodes 5-6 du M1).
- Le plus *purement* GOFAI **et** porteur de sa fragilité. (Alternatives écartées : minimax-Sheets, A*-applet.)

### TN5 — Expérience sur une IA réelle
Le M5 n'a **pas de mécanisme** → le « quelque chose » est **une vraie IA de pointe** (ChatGPT, Claude…) manipulée comme objet d'étude. Hands-on, maximalement actuel, non-périssable, méta.
- **Forme** : l'étudiant mène une **petite expérience sur une IA réelle, branchée sur un dossier chaud de son choix**, documente (transcription = artefact), puis **analyse via les lentilles des 4 attitudes** + questions interprétatives.
- Pistes : vérité/démocratie (désinformation, garde-fous) ; création/propriété (« à la manière de », originalité/droit d'auteur) ; éducation (lui faire « faire » un travail, critiquer la fiabilité). (Alternatives écartées : analyser une news ; débat dialectique.)

---

## 11. Démarrage de la rédaction (prochaines séances)

- **Approche** : contexte neuf à chaque séance, ce plan comme entrée. Rédiger **module par module**, en commençant par le **M1**.
- **Premières actions concrètes pour le M1** : (1) supprimer `30-livres.md` et l'ancien `module1/10-activités.md` ; (2) trier le catalogue de phares (§5) dans les 6 épisodes ; (3) rédiger épisode par épisode selon le gabarit (§4) ; (4) concevoir le gabarit Sheets du TN1.
- **Points laissés ouverts volontairement** : tri fin du catalogue M1 ; élagage de l'exotique au M3 (GNN/NTM) ; choix précis des applets/expériences manipulables à créer (M1, M4).
