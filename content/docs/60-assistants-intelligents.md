---
title: "Usage de l'IA (pour ce cours)"
weight: 60
slug: assistants-intelligents
---

# L'usage d'assistants intelligents

Étant donné qu'il s'agit d'un cours sur l'intelligence artificielle, l'usage
d'assistants intelligents (ChatGPT, Claude, Gemini, etc) est évidemment
encouragé ! Ceci s'applique autant aux travaux notés qu'au reste du contenu du
cours.

Par contre si vous utilisez un tel outil, nous vous conseillons de vous assurer
d'avoir une compréhension viscérale des réponses qu'il fournira, et de ne pas
hésiter à engager un dialogue avec l'agent, dans le but de clarifier des aspects
du problème qui pourraient rester obscurs pour vous. N'oubliez pas que le but de
ce cours est la construction de bons modèles mentaux pour penser à
l'intelligence artificielle, et comprendre son fonctionnement, au-delà de sa
surface applicative. L'agent possède déjà ces modèles mentaux, si vous avez
développé les vôtres à la fin de ce cours, le but aura clairement été atteint !

Voici un exemple d'interaction : supposons que j'ai de la difficulté à
comprendre un aspect des [mathématiques de la régression
logistique](module2/60-classer/#tracer-une-frontière--la-régression-logistique), je peux
faire une capture d'écran du texte et la donner à ChatGPT, et poser ma question
("je ne comprends pas pourquoi les deux dernières équations sont
équivalentes").. ChatGPT (ou un autre outil) se fera un plaisir de vous
expliquer avec une patience infinie :

{{< image src="/images/exemple-chatgpt.png" alt="ChatGPT" title="ChatGPT" loading="lazy" >}}

## Comment ce cours a été produit

Ce cours applique lui-même ce conseil. Son auteur l'a rédigé avec l'aide d'un agent de
programmation, Claude Code, du type présenté au chapitre
« [Programmer avec des agents](docs/module4/85-programmer-avec-des-agents) » du
Module 4. Le cours est un ensemble de fichiers texte, au format Markdown, transformés
en site Web par le programme Hugo et suivis par le logiciel de gestion de versions
git. L'agent lit et modifie ces fichiers, écrit les petits programmes Python qui
produisent les figures et les applets, vérifie qu'aucun lien n'est cassé, et fait
vérifier en ligne les faits récents. L'auteur décide du plan et du contenu, relit
chaque passage et valide chaque changement. Comme pour vos propres travaux, l'outil
aide, mais la responsabilité du contenu reste humaine.
