import random
from utils import path_length, selection, crossover, mutate, fix_path, extract_weights_from_path
import tqdm

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

    for gen in tqdm.tqdm(range(generations)):
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