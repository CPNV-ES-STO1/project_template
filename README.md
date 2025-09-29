# README

Projet STO1 - 2025.2026

## Intention pédagogique

Afin d'évaluer les compétences acquises durant le module, un projet en équipe de 2 techniciens vous est proposé.

Vous recevrez une situation de départ et différentes étapes d'un scénario à réaliser. Des données vous seront confiées en début de projet. Il s'agira, à l'aide des différentes technologiques que nous avons vues, de réaliser des migrations entre différents RAIDs et différents systèmes d'exploitation afin d'amener les données à bon "port".

---

## Objectifs opérationnels

Le projet sera décomposé en 6 étapes principales:

|Etape num|Titre                           |Détails|
|:--      |:--                             |:--    |
|0        |[Configuration des environnements](./Etape00_ConfigurationEnvironnement.md)|Prise en main de l'infrastructure cible|
|1        |[Situation intiale](./Etape01_SituationInitiale.md)          |Mise en place du premier RAID et intégration des données       |
|2        |[1ère migration](./Etape02_1ereMigration.md)                 |Migration RAID a à b       |
|3        |[2ème migration](./Etape03_2emeMigration.md)                 |Migration OS x à y + RAID b à c       |
|4        |[3ème migration](./Etape04_3emeMigration.md)                 |Migration RAID c à d       |
|5        |[Nettoyage](./Etape05_Nettoyage.md)                          |Suppression des configurations et données produites par le travail de migration|

![Overview](./appendices/excalidraw-sto1-project-overview.svg)

---

## Infrastucture cible

![InfraCible](./appendices/diagram-export.svg)

[Récupérer le code eraser](./appendices/infra.eraserdiagram)

---

### Informations complémentaires

* Les buckets s3 à utiliser sont les mêmes que ceux pour les laboratories. Cela étant dit, ne vous échangez pas les clés d'accès. Je peux au besoin adapter les droits d'accès pour vos collègues.

* Le bucket s3 livré (15 GBs de données) par le client porte le nom suivant:
    * sto1-project-data
    * [Pour récupérer les données](https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html)

---

## Livrables

Les devopsteams livrent le contenu suivant:

*Dépôt github*

* Chaque étape de la migration est documentée, en utilisant les modèles de fichiers livrés.
* La documentation technique, dédiée à un publique avertit, de pouvoir reproduire la même migration.

*Une caspule vidéo*

 * De 15 min max.
 * Votre écran et partagé en deux
    * La première moitié présente la documentation github
    * La seconde moitié présente l'accès soit en RDP, soit en SSH le serveur de fichier et le résultat des commandes.
    * (inutile de filmer votre visage)
 * Construite par tous les membres de l'équipe.
 * Prenez le temps de décrire chacune des commandes et d'expliquer le comportement de l'OS, du RAID.

--

## RoadMap

Voici le déroulement du projet ainsi que les délais à respecter:

|Délai|Livrable|
|:--|:--|
|Lundi, 29-SEP-2025, 18h00|Le dépôt de l'équipe a été créé et partagée avec l'enseignant.|
||Une discussion sur Teams a été initialisée et implique tous les membres de l'équipe, ainsi que l'enseignant.|
||L'analyse pour chacune des étapes a été publiée. Une notification dans le canal teams est adressée à l'enseignant.|
|Lundi, 27-OCT-2025, 21h00|Le dépôt de l'équipe est à jour.|
||La vidéo a été partagée via un lien oneDrive.|
||Une notification dans le canal teams est adressée à l'enseignant, annonçant la fin du projet.|

## Grille d'évaluation

|Critères|Points|
|:--|:--|
|La vidéo démontre l'entièreté du projet| 3pts * 5étapes = 15pts|
|Les commandes présentées sont similaires à celles de la documentation.| 5pts * 5étapes = 25pts|
|Les preuves techniques ont été faites pour valider le bon fonctionnement des RAID. |20pts|
|Les preuves métiers ont été faites pour valider que les données n'ont pas été altérées. |20pts|
|Lien entre analyse et implémentation (validation et/ou retour d'expérience). |20pts|
|Utilisation des moyens a été limitée au minimum nécessaire.|15pts|
|Un état clair du projet est présenté|15 pts|
|Les problèmes techniques non résolus sont documentés (issues)|15 pts|
|Qualité du travail collaboratif au sein de l'équipe, tout comme avec l'enseignant.|20 pts|

La note du projet comptera (pondération) pour 50% du module.

---

## FAQ

### Devons-nous utiliser des profils pour configurer le CLI ?

Oui.

### Quel est le contenu (data) à migrer ?

Vous aurez environ 15 Go de données à intégrer (étape 01) et à migrer tout au long des étapes de modification de l'infrastructure.
Ces données vous seront livrées via un bucket S3.
Les données seront un mélange de différents types, tailles ordonnées dans une hiérarchie à plusieurs niveaux. Il est possible que certains fichiers ne soient pas utilisable (image corrompue).

### Pouvons-nous utiliser autant de volumes que nous le désirons ?

Il vous est demandé d'utiliser le moins de moyens possible pour chaque étape.
   * Le moins de disque
   * Le moins d'opérations (les commandes pour valider, vérifier ne comptent pas dans le nombre)
   * Le moins de bande-passante (votre S3 ne doit être utilisé que si une migration n'est pas possible)
