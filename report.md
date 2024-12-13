# Rapport de Projet : Analyse des Performances et Styles de Jeu des Joueurs et Équipes de Football Européen

## 1. Introduction
Ce projet vise à analyser les données de football européen pour identifier des tendances de performance et des profils stratégiques à l’aide de techniques de clustering. En utilisant des données sur les joueurs, les équipes et les matchs, nous avons appliqué des algorithmes de clustering afin de regrouper les joueurs et équipes en fonction de leurs attributs physiques et de performance. L'objectif est de découvrir des patterns cachés, d’identifier des joueurs exceptionnels et de classer les équipes selon leurs styles de jeu. Ce rapport présente les méthodologies utilisées, les modèles appliqués, ainsi que les résultats obtenus.

## 2. Méthodologie

### 2.1. Préparation des Données
Les données utilisées dans ce projet proviennent de différentes tables liées entre elles :
- **Player** : Informations sur les joueurs 
- **Player_Attributes** : Attributs individuels des joueurs 
- **Team** : Informations sur les équipes 
- **Match** : Informations sur les matchs 

Les étapes de préparation des données comprenaient :
- **Exploration Initiale** : Identification des relations entre les différentes tables et sélection des attributs clés (comme la note globale et le potentiel des joueurs, ou encore la pression défensive des équipes).
- **Fusion des Tables** : Création d’une vue consolidée combinant les informations de Player, Player_Attributes, et Team.
- **Nettoyage des Données** : Gestion des valeurs manquantes, standardisation des unités  et traitement des valeurs aberrantes.

### 2.2. Modélisation et Clustering
Le clustering a été utilisé pour regrouper les joueurs et les équipes selon des critères pertinents :
- **Joueurs** : Les critères de clustering comprenaient la note globale, le potentiel, la taille, le poids, et le pied préféré.
- **Équipes** : Les critères incluaient la vitesse de construction, la pression défensive, la précision des passes, ainsi que des statistiques d’attaque et de défense comme les buts marqués et encaissés.

Trois algorithmes de clustering ont été utilisés pour la segmentation :
- **K-Means** : Un algorithme simple et efficace pour segmenter les joueurs et les équipes en fonction de leurs attributs.
- **DBSCAN** : Utile pour détecter les points atypiques et les groupes non linéaires.
- **Clustering Hiérarchique** : Permet une visualisation sous forme de dendrogramme, afin de mieux comprendre les relations entre les clusters.

### 2.3. Évaluation des Modèles
Les performances des modèles de clustering ont été évaluées à l’aide des scores suivants :
- **Silhouette Score** : Mesure de la cohérence des clusters, où une valeur proche de +1 indique des clusters bien définis.
- **Davies-Bouldin Index** : Mesure de la séparation entre les clusters, où une valeur plus faible indique une meilleure séparation.

## 3. Résultats des Modèles

### 3.1. Clustering des Joueurs
Les résultats des différents modèles appliqués au clustering des joueurs sont les suivants :
- **K-Means** :
  - Silhouette Score : 0.546
  - Davies-Bouldin Score : 0.675
  Le K-Means a montré un bon équilibre entre la cohésion des clusters et la séparation entre les groupes de joueurs, ce qui en fait un modèle robuste pour cette tâche.
  
- **DBSCAN** :
  - Silhouette Score : 0.252
  - Davies-Bouldin Score : 1.525
  DBSCAN a obtenu des résultats moins satisfaisants, notamment en raison de la difficulté à déterminer un bon paramètre de densité, ce qui a conduit à des clusters moins cohérents.
  
- **Hiérarchique** :
  - Silhouette Score : 0.531
  - Davies-Bouldin Score : 0.691
  Bien que similaire au K-Means, l’approche hiérarchique a montré une meilleure visualisation des relations entre les clusters.

Après avoir comparé les scores des différents modèles, le K-Means a été sélectionné comme modèle principal en raison de ses bonnes performances en termes de silhouette score et de séparation des clusters.

### 3.2. Clustering des Équipes
Pour le clustering des équipes, les résultats étaient les suivants :
- **K-Means** :
  - Silhouette Score : 0.482
  - Davies-Bouldin Score : 0.911
  Le K-Means a également performé de manière satisfaisante pour les équipes, permettant de bien séparer les équipes selon leur style de jeu.
  
- **DBSCAN** :
  - Silhouette Score : 0.154
  - Davies-Bouldin Score : 1.343
  Le modèle DBSCAN a encore montré une séparation faible, avec des difficultés à identifier des clusters bien définis dans le cas des équipes.
  
- **Hiérarchique** :
  - Silhouette Score : 0.482
  - Davies-Bouldin Score : 0.911
  Les résultats du clustering hiérarchique ont montré des performances similaires à celles du K-Means, mais la visualisation sous forme de dendrogramme a fourni une meilleure compréhension des relations entre les équipes.

Une fois encore, le K-Means a été choisi comme modèle final, car il a donné des résultats cohérents et interprétables pour les équipes.

## 4. Interprétation des Clusters

### 4.1. Clusters de Joueurs
Les résultats du clustering des joueurs ont permis d’identifier plusieurs profils :
- **Attaquants Prolifiques** : Joueurs avec une note élevée et un potentiel offensif élevé. Ces joueurs sont souvent les meilleurs buteurs de leurs équipes.
- **Défenseurs Robustes** : Joueurs avec une grande taille, un poids important, et des notes élevées en défense.
- **Milieux Équilibrés** : Joueurs ayant une répartition uniforme entre leurs attributs offensifs et défensifs, avec une note globale et un potentiel équilibrés.

### 4.2. Clusters d’Équipes
Les clusters d’équipes ont révélé plusieurs types de styles de jeu :
- **Équipes Offensives** : Ces équipes ont une grande vitesse de construction et un nombre élevé de buts marqués.
- **Équipes Défensives** : Elles se distinguent par une pression défensive élevée et une défense solide, encaissant peu de buts.
- **Équipes Équilibrées** : Ces équipes ont un style de jeu modéré, avec des performances équilibrées en attaque et en défense.


## 6. Conclusion
Le projet a utilisé le clustering (K-Means) pour analyser les performances et styles de jeu des joueurs et équipes de football européen. Ce modèle a permis d'identifier des profils de joueurs et des styles d'équipes, offrant des insights stratégiques.