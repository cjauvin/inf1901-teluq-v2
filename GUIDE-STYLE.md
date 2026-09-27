# Guide de style — INF1901 v2

Registre fixé le 2026-09-27 avec Christian, à partir de la réécriture de
*Capturer l'expertise* (`content/docs/module1/50-systemes-experts.md`), qui sert
de page modèle : **une écriture neutre, simple et directe**. On énonce les faits et
les idées directement, avec des phrases simples et des liens logiques explicites
(« parce que », « donc », « cependant », « par exemple »). Le texte reste clair et
agréable, mais sans mise en scène.

## À éliminer

- **Chutes et suspense** : « Alors : visons étroit. », « Verdict : … »,
  « Pire : … », « Sa spécialité : … », « Ce fut un triomphe : … », « Mais cette
  question-là devra attendre. », fins de paragraphe ou de page à effet.
- **Dramatisation** : superlatifs et mots chargés (« triomphe », « pharaonique »,
  « désespérant », « fascinant », « révolution » quand ce n'est pas un terme
  établi), « Et pourtant (c'est tout le paradoxe)… », « enfin », « pour une fois ».
- **Images décoratives** : métaphores qui n'expliquent rien (« revenu par la
  fenêtre », « il ne fléchit pas, il s'effondre », « le sommet d'où l'on commence
  à redescendre », « des fissures couraient sous l'édifice »).
- **Questions rhétoriques** et interpellations théâtrales (« Faut-il pour autant
  renoncer ? », « Et si l'on confiait… ? »). Une vraie question posée à
  l'étudiant (exercice, matière à réflexion) reste permise.
- **Italiques d'insistance** (« va *payer* », « ne sait *rien* »). Les italiques
  restent pour les termes étrangers, les titres d'œuvres, les mots cités ou
  employés comme mots, les faits et conclusions d'un exemple formel (règles,
  prédicats).
- **Deux-points à effet** et deux deux-points dans une même phrase. Le deux-points
  reste permis pour annoncer une liste, un bloc (citation, règles, code), une
  formule, une explication directe, et dans les étiquettes (« R1 : »,
  « Pour aller plus loin : », crédits).
- **Tirets cadratins** : en principe aucun ; virgule, parenthèses ou nouvelle
  phrase à la place (les tirets de dialogue restent).
- Tournures familières ou complices (« tâchons », « Voyons-le à l'œuvre »,
  « Mettez-vous à la place de… ») : les remplacer par une formulation directe.

## À garder

- Le **gras** sur les termes clés (repérage).
- Les **exemples et analogies qui expliquent** (la voiture en panne, la base de
  règles comparée à une cartouche) : on les garde, dits simplement.
- Les **consignes au lecteur** devant les applets et les activités (« Dans
  l'applet ci-dessous, choisissez… »), au vouvoiement.
- Tout le **contenu factuel**, les dates, les noms, les chiffres.
- Les règles déjà en vigueur : liens sur tout renvoi interne (slug + ancre, jamais
  de numéro de page), « sur-apprentissage (*overfitting*) » avec trait d'union et
  anglais entre parenthèses à chaque mention, terme anglais courant entre
  parenthèses, « geste » banni au sens figuré, `\\$` pour le dollar, espaces
  insécables (relancer `scripts/espaces_insecables.py`).

## Ne jamais toucher

Titres de sections `##`/`###` (leurs ancres sont liées ailleurs), front matter,
liens et ancres, shortcodes (`{{< image … >}}`, `{{< applet … >}}`,
`{{< youtube … >}}`, `{{% hint %}}`, `{{% details "…" %}}` dont le titre peut
toutefois être neutralisé), images et leurs attributs, blocs de code, formules
mathématiques, tableaux (sauf le texte des cellules, à neutraliser au besoin),
commentaires HTML.
