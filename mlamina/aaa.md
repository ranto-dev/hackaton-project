### Structure du projet :

```
genetic_algorithm/
│
├── main.py
├── algorithm.py
├── utils.py
└── graph.py
```

### 1. `main.py` (Point d'entrée du programme)

Ce fichier sera responsable de l'exécution de l'algorithme génétique, en chargeant les modules nécessaires et en appelant les fonctions principales.

```python
from algorithm import genetic_algorithm
from graph import graph

# Paramètres de l'algorithme
START = 'Mopera'
END = 'SmartOne'
POPULATION_SIZE = 50
GENERATIONS = 100

def main():
    best_path, best_score = genetic_algorithm(graph, START, END, POPULATION_SIZE, GENERATIONS)
    print("Meilleur chemin :", best_path)
    print("Poids entre les nœuds :", best_score)

if __name__ == "__main__":
    main()
```

### 2. `algorithm.py` (Logique de l'algorithme génétique)

Ce fichier contient la logique principale de l'algorithme génétique, y compris la génération des chemins, la sélection des parents, le crossover, la mutation, et l'évaluation des scores.

```python
import random
from utils import path_length, selection, crossover, mutate, fix_path, extract_weights_from_path

def generate_random_path(graph, start, end):
    path = [start]
    current = start
    visited = set(path)

    while current != end:
        neighbors = [n for n in graph[current] if n not in visited]
        if not neighbors:
            return None  # chemin bloqué, on renvoie None
        current = random.choice(neighbors)
        path.append(current)
        visited.add(current)
    return path

def generate_initial_population(graph, start, end, size):
    population = []
    while len(population) < size:
        path = generate_random_path(graph, start, end)
        if path:
            population.append(path)
    return population

def genetic_algorithm(graph, start, end, pop_size, generations):
    population = generate_initial_population(graph, start, end, pop_size)

    for gen in range(generations):
        scores = [path_length(graph, p) for p in population]
        new_population = []

        for _ in range(pop_size):
            parent1 = selection(population, scores)
            parent2 = selection(population, scores)
            child = crossover(parent1, parent2)
            if child:
                child = mutate(child, graph)
            if child:
                new_population.append(child)

        population = new_population

    # Meilleur chemin trouvé
    best = min(population, key=lambda p: path_length(graph, p))
    return best, path_length(graph, best)
```

### 3. `utils.py` (Fonctions utilitaires)

Ce fichier contient des fonctions utilitaires, comme le calcul de la longueur d'un chemin, la sélection, la mutation, et la réparation des chemins.

```python
import random

# Évaluer la longueur d'un chemin
def path_length(graph, path):
    total = 0
    for i in range(len(path) - 1):
        current, nxt = path[i], path[i + 1]
        if nxt not in graph.get(current, {}):
            return float('inf')  # pénalise les chemins invalides
        total += graph[current][nxt]
    return total

# Sélection par tournoi
def selection(population, scores, k=3):
    selected = random.sample(list(zip(population, scores)), k)
    selected.sort(key=lambda x: x[1])
    return selected[0][0]

# Crossover entre deux chemins
def crossover(p1, p2):
    common = list(set(p1) & set(p2) - {'Mopera', 'SmartOne'})
    if not common:
        return p1  # pas de point commun, retour du parent
    cut = random.choice(common)
    i1 = p1.index(cut)
    i2 = p2.index(cut)
    new_path = p1[:i1] + p2[i2:]
    return fix_path(new_path)

# Mutation : supprimer ou échanger un nœud
def mutate(path, graph):
    if len(path) <= 2:
        return path
    i = random.randint(1, len(path) - 2)
    neighbors = list(graph[path[i-1]].keys())
    for n in neighbors:
        if n != path[i] and n not in path:
            new_path = path[:i] + [n] + path[i+1:]
            return fix_path(new_path)
    return path

# Réparer un chemin si jamais il est invalide
def fix_path(path):
    visited = set()
    new_path = []
    for node in path:
        if node in visited:
            break
        new_path.append(node)
        visited.add(node)
        if node == 'SmartOne':
            break
    if new_path[-1] != 'SmartOne':
        return None
    return new_path

# Extraire les poids d'un chemin
def extract_weights_from_path(graph, path):
    weights = []
    for i in range(len(path) - 1):
        current, nxt = path[i], path[i + 1]
        weight = graph[current][nxt]
        weights.append(weight)
    return weights
```

### 4. `graph.py` (Graphique et structure de données du graphe)

Ce fichier contient la représentation du graphe avec les carrefours et les distances entre eux.

```python
graph = {
    'Mopera': {'villa69': 6, 'C': 4},
    'villa69': {'Mopera': 6, 'C': 1, 'D': 7},
    'C': {'Mopera': 4, 'villa69': 1, 'D': 3},
    'D': {'villa69': 7, 'C': 3, 'SmartOne': 2},
    'SmartOne': {'D': 2}
}
```

### Explication de la structure des fichiers :

1. **`main.py`** :
   - Ce fichier est le point d’entrée du programme. Il importe l'algorithme génétique et le graphe, puis exécute l'algorithme et affiche le meilleur chemin trouvé.
2. **`algorithm.py`** :

   - Contient toute la logique de l'algorithme génétique, notamment la génération de la population, la sélection, le crossover, la mutation, et l'évaluation des chemins.

3. **`utils.py`** :

   - Contient les fonctions utilitaires comme la mesure de la longueur d’un chemin, la sélection par tournoi, le crossover, la mutation, et la réparation des chemins invalides.

4. **`graph.py`** :
   - Représente le graphe sous forme de dictionnaire et contient les informations sur les routes et les distances.

---

### Comment exécuter le programme :

1. Place les fichiers dans un dossier `genetic_algorithm/`.
2. Exécute le programme à partir du fichier `main.py` :

```bash
python main.py
```

Cela exécutera l'algorithme génétique et affichera le meilleur chemin et sa longueur.

---

### Conclusion :

Cette organisation rend le code plus modulaire, plus facile à maintenir et à étendre. Par exemple, tu peux facilement remplacer une fonction de sélection ou de mutation en modifiant uniquement `utils.py` sans toucher au reste du programme. Si tu veux ajouter des fonctionnalités comme une nouvelle méthode de sélection ou de crossover, tu peux les ajouter directement dans `algorithm.py`.
