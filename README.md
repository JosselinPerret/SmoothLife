## SmoothLifePlus

SmoothLife, créé par Stephan Rafler, est une variante du célèbre "Jeu de la vie" de John Conway qui repose sur des règles mathématiques définies pour modéliser des systèmes dynamiques complexes. Contrairement à ce dernier, qui repose sur une grille discrète et des règles basées sur des entiers (cellule vivante ou morte), SmoothLife introduit une continuité grâce à des valeurs flottantes et des fonctions de transition douces. Cette approche permet d'observer des phénomènes dynamiques plus complexes et plus réalistes, comme des structures mobiles (glisseurs) qui se déplacent dans toutes les directions, des paires de glisseurs rotatifs et des effets semblables à une tension élastique entre des "amas" de cellules.

L'un des principaux changements réside dans la définition des règles d'interaction, où des fonctions mathématiques (sigmoïdes) sont utilisées pour rendre les transitions fluides entre états. De plus, SmoothLife travaille dans un espace continu plutôt qu'une grille discrète, ce qui améliore la représentation des formes complexes et le comportement naturel des systèmes dynamiques.

Une des caractéristiques fondamentales qui différencie SmoothLife du Jeu de la vie de Conway est la manière dont les voisins sont sélectionnés pour influencer l'état d'une cellule. Dans le Jeu de la vie classique, seuls les huit voisins immédiats d'une cellule (sur une grille carrée) sont pris en compte. En revanche, SmoothLife utilise une sélection de voisins basée sur un cercle autour de chaque point. Cette approche, calculée par un produit de convolution, permet de considérer un voisinage continu et isotrope, sans biais lié à la structure en grille.

* Avantages de cette approche circulaire
    - Isotropie : Le choix circulaire élimine les effets directionnels liés à une grille carrée, permettant un comportement des structures plus naturel et plus uniforme dans toutes les directions.
    - Règles dynamiques : Les transitions entre cellules tiennent compte d’une moyenne pondérée sur une région donnée, rendant les changements d'état plus fluides et plus proches des phénomènes observés dans des systèmes naturels.
    - Modélisation réaliste : Cela permet de simuler des interactions où l'influence des voisins diminue de manière progressive avec la distance, comme dans de nombreux systèmes biologiques ou physiques.

Notre modèle SmoothLifePlus à la particularité supplémentaire de travailler sur un temps continu, en plus de se placer désormais dans un espace continu. Cette dernière modification améliore grandement la complexité du programme, et de fait améliore grandement la représentation des système dynamiques naturels puisque leur évolution s'inscrit également dans le cadre d'un temps continu.
    
      
  ![SmoothLife Animation](image/smoothlife.gif)


## Statut du projet

Statut : Pleinement fonctionnel
Version actuelle : v1.0

## Fonctionnalités

- Animation fluide en continu à la fois sur le plan temporel et spatial, inspirée du Jeu de la Vie de Conway.
- Personnalisation des nombreux paramètres initiaux - 20 au total - de simulation à travers une interface graphique claire (seuils de naissance, de mort, etc.).
- Ajout aléatoire ou structuré de configurations initiales (planeurs, taches aléatoires) comme paramètre à cocher sur l'interface graphique.
- Visualisation avec différentes palettes de couleurs à sélectionner sur l'interface graphique, telles que viridis, plasma, gray, binary, seismic, gnuplot proposées par matplotlib.
- Sauvegarde et manipulation des états initiaux via JSON.
- Simulation basée sur des calculs en transformée de Fourier pour une performance accrue.


## Installation : Les prérequis

- Python 3.8 ou plus
- Modules nécessaires : matplotlib, numpy, math

Concernant l'installation des dépendances :
```bash
 pip install -r requirements.txt
```


## Utilisation

Exécutez fichier smoothlife.py pour ajuster les différentes options de simulation selon vos préférences.
```py
python smoothlife.py
```
![SmoothLife settings](image/interface_graphique.png)



## Exemple de simulations 
    
Pour les différentes simulations, il suffit d'exécuter le code suivant puis d'établir les paramètres comme définit ci-dessous :
```py
python smoothlife.py 
```

* Simulation standard :
    resolution = "256,256", cmap = "viridis", speed = 60, B1 = 0.278, B2 = 0.365, D1 = 0.267, D2 = 0.445, alpha_n = 0.028, alpha_m = 0.147, count = 100, intensity = 1, inner_radius = 7, outer_radius = 21, glider = décoché

* Simulation avec planeurs :
    resolution = "256,256", cmap = "viridis", speed = 60, B1 = 0.278, B2 = 0.365, D1 = 0.267, D2 = 0.445, alpha_n = 0.028, alpha_m = 0.147, count = 100, intensity = 1, inner_radius = 7, outer_radius = 21, glider = coché

* Simulation plus artistique :
    resolution = "512,512", cmap = "plasma", speed = 30, B1 = 0.278, B2 = 0.365, D1 = 0.267, D2 = 0.445, alpha_n = 0.05, alpha_m = 0.2, count = 100, intensity = 1, inner_radius = 7, outer_radius = 21, glider = décoché


## Test Coverage

- Coverage du code : 88%
- Rapport généré en utilisant la commande suivante :
    ```py
    python -m pytest --cov=. --cov-report html test.py
    ```
    
      
![Coverage Report](image/coverage.png)


## Application concrète de SmoothLifePlus

SmoothLifePlus a des applications potentielles dans les domaines scientifiques où la simulation de systèmes dynamiques naturels est nécessaire, notamment en biologie computationnelle, en recherche sur les automates cellulaires continus et dans l'exploration des modèles de morphogenèse (formation des structures biologiques). Il peut également être utilisé dans des contextes artistiques et visuels pour générer des animations et des patterns organiques fascinants grâce à ses propriétés dynamiques.

Le développement de SmoothLifePlus s'inscrit dans la continuité des recherches sur les automates cellulaires pour modéliser des phénomènes complexes de manière élégante et computationnellement efficace, telle que le phénomène d'émergence, la sélection naturelle, où encore l'évolution des intéractions Prédateurs-proies.

## Crédits / Auteurs

* Développé par Josselin Perret, Oscar Eav, Antonioli Enzo, Arthur De Bom Van Driessche et Solène Zhang.
* Une mention spéciale à mikolalysenko pour son article intitulé Conway’s Game of Life for Curved Surfaces, qui reprend et améliore la théorie de SmoothLife développé par S.Rafler.
* Remerciements particuliers à John Conway ainsi qu'à Stéphane Rafler pour l'inspiration originelle.

Lien de l'article https://0fps.net/2012/11/19/conways-game-of-life-for-curved-surfaces-part-1/
