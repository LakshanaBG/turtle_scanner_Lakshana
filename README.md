
# Turtle Scanner ROS 2 Project

Partie 0: Création du package et projet Git
We have already successfully created our package turtle scanner. We continue on with our project. 

## Authors
- Lakshana


## Partie 1 — Spawn d'une tortue cible aléatoire

Le nœud `spawn_target.py` utilise le service `/spawn` de `turtlesim/srv/Spawn`
pour créer une tortue nommée `turtle_target` à une position aléatoire.

### Screenshot
![Spawn target](/images/spawn_target.png)


## Partie 2 — Abonnement aux poses des deux tortues

Dans cette partie, un nœud ROS 2 nommé `turtle_scanner_node.py` a été implémenté afin de suivre en temps réel la position des deux tortues dans l’environnement TurtleSim.

### Objectif

L’objectif est de permettre au nœud principal de connaître en permanence :
- la position de la tortue scanner (`turtle1`)
- la position de la tortue cible (`turtle_target`)

### Implémentation

Deux abonnements ont été créés :

- `/turtle1/pose` (type : `turtlesim/msg/Pose`)  
  → met à jour `self.pose_scanner`

- `/turtle_target/pose` (type : `turtlesim/msg/Pose`)  
  → met à jour `self.pose_target`

À chaque réception de message, les attributs correspondants sont mis à jour avec les nouvelles coordonnées.

### Vérification

Le bon fonctionnement a été vérifié avec les commandes suivantes :

```bash
ros2 topic echo /turtle1/pose
ros2 topic echo /turtle_target/pose


### Screenshot
![Pose target](/images/pose_target.png)

