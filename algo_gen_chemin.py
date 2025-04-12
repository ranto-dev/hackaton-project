import random

graph = {
    'Mopera': {'villa69': 6, 'C': 4},
    'villa69': {'Mopera': 6, 'C': 1, 'D': 7},
    'C': {'Mopera': 4, 'villa69': 1, 'D': 3},
    'D': {'villa69': 7, 'C': 3, 'SmartOne': 2},
    'SmartOne': {'D': 2}
}

START = 'Mopera'
END = 'SmartOne'
POPULATION_SIZE = 50
GENERATIONS = 100

# Générer un chemin aléatoire valide de START à END
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

# Générer la population initiale avec un size individu 
def generate_initial_population(graph, start, end, size):
    population = []
    while len(population) < size:
        path = generate_random_path(graph, start, end)
        if path:
            population.append(path)
    return population

# Évaluer le score, avec la fonction fitness, d'un chemin
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
    common = list(set(p1) & set(p2) - {START, END})
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
        if node == END:
            break
    if new_path[-1] != END:
        return None
    return new_path

def extract_weights_from_path(graph, path):
    weights = []
    for i in range(len(path) - 1):
        current, nxt = path[i], path[i + 1]
        weight = graph[current][nxt]
        weights.append(weight)
    return weights

# Algorithme génétique principal
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

# Exécution
best_path, best_score = genetic_algorithm(graph, START, END, POPULATION_SIZE, GENERATIONS)

weights = extract_weights_from_path(graph, best_path)

print("Meilleur chemin :", best_path)
print("Poids entre les nœuds :", weights)
print("Longueur du chemin :", best_score)

