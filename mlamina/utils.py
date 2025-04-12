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