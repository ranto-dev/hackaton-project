from data import trajets
from planner import planifier_voiture
from display import afficher_planification, afficher_occupation_par_temps

def main():
    for voiture, chemin in trajets.items():
        planifier_voiture(voiture, chemin)

    afficher_planification()
    afficher_occupation_par_temps()

main()
