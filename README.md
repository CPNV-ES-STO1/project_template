# README

Projet STO1 - 2024-2025

## Intention pédagogique

Afin de réaliser une révision ainsi qu'un approfondissement des connaissances et compétences acquises durant le module, il vous est proposé de réaliser un projet en équipe de 2 ou 3 techniciens.

Vous recevrez une situation de départ et différentes étapes d'un scénario à réaliser. Des données vous seront confiées en début de projet. Il s'agira, à l'aide des différentes technologiques que nous avons vues, réaliser des migrations entre différents RAIDs et différents systèmes d'exploitation afin d'amener les données à bon "port".

C'est également l'occasion de travailler sur une infrastructure "réaliste" et ainsi vous confronter à des contraintes de performances et de sécurité sur un cloud industriel.

## Objectifs opérationnels

Le projet sera décomposé en 5 étapes principales:

|Etape num|Titre                           |Détails|
|:--      |:--                             |:--    |
|0        |Configuration des environnements|Prise en main de l'infrastructure cible|
|1        |Situation intiale|              |Mise en place du premier RAID et intégration des données       |
|2        |1ère migration                  |Migration RAID a à b       |
|3        |2ème migration                  |Migration OS x à y + RAID b à c       |
|4        |3ème migration                  |Migration RAID c à d       |
|5        |Nettoyage                       |Suppression des configuration et données produite par le travail de migration|

### FAQ

* Devons-nous utiliser des profiles pour configurer le CLI ?

Oui. Vous recevrez des accès différents pour votre bucket utile pour le travail de migration et celui qui exposera les données initiale à reprendre.

* Quel est le contenu (data) à migrer ?

Vos aurez environ 4 Go de données à intégrer (étape 01) et à migrer tout au long des étapes de modification de l'infrastructure.

Ces données vous seront livrées via un bucket S3.

Les données seront un mélange de différents types, tailles ordonnées dans une hiérarchie à plusieurs niveaux.

