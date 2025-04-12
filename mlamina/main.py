from algo import genetic_algorithm
from utils import extract_weights_from_path
from graph import graph

START = "Mopera"
END = "SmartOne"

# Les hyper-paramètre
POPULATION_SIZE = 50
GENERATIONS = 10000 # 

def main():
    best_path, best_score = genetic_algorithm(graph, START, END, POPULATION_SIZE, GENERATIONS)
    weights = extract_weights_from_path(graph, best_path)
    print("Meilleur chemin: ", best_path)
    print("Les poids de chaque noeud: ", weights)
    print("Poids entre les neuds: ", best_score)

main()