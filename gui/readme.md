# Interface graphique

## Format de données
Les données à tracer doivent être stockées dans une matrice de couples de coordonnées (x, y) :
```
data = {}
# ...
data[(x, y)] = value
```
Dans notre cas, une donnée peut correspondre à la moyenne des valeurs pour un critère sur un emplacement, au nombre de familles sur un emplacement, etc.
Les valeurs d'une matrice de données doivent être normalisées, i.e. comprisent entre 0 et 1. Utiliser la methode `normalize(data)` pour obtenir une matrice de valeurs normalisées à partir d'une matrice quelquonque.

## Utilisation
**TODO**
