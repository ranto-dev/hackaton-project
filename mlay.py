# Graphe : chaque carrefour est un noeud, chaque route est une arête dirigée
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

# Trajets prédéfinis (chaque voiture a sa liste de carrefours à suivre)
trajets = {
    'V1': ['A', 'B', 'D', 'E'],
    'V2': ['A', 'C', 'D', 'E'],
    'V3': ['B', 'D', 'E'],
    'V4': ['C', 'D'],
    'V5': ['A', 'C', 'D', 'E'],
    'V6': ['B', 'D', 'E'],
    'V7': ['B', 'D', 'E'],
    'V8': ['A', 'B', 'D', 'E'],
    'V9': ['A', 'B', 'D', 'E'],
    'V10': ['A', 'C', 'D', 'E'],
    'V11': ['B', 'D', 'E'],
    'V12': ['B', 'D', 'E'],
    'V13': ['A', 'B', 'D', 'E'],
    'V14': ['A', 'B', 'D', 'E'],
    'V15': ['A', 'C', 'D', 'E'],
    'V16': ['A', 'C', 'D', 'E'],
    'V17': ['B', 'D', 'E'],
    'V18': ['C', 'D'],
    'V19': ['A', 'C', 'D', 'E'],
    'V20': ['B', 'D', 'E'],
    'V21': ['B', 'D', 'E'],
    'V22': ['A', 'B', 'D', 'E'],
    'V23': ['A', 'B', 'D', 'E'],
    'V34': ['A', 'C', 'D', 'E'],
    'V35': ['B', 'D', 'E'],
    'V36': ['B', 'D', 'E'],
    'V35': ['A', 'B', 'D', 'E'],
}

# Temps qu'une voiture occupe un tronçon
temps_par_troncon = 1

# Réservation : {('A', 'B'): {0: 'V1', 3: 'V2'}, ...}
reservation = {}

# Résultat final : {V1: [(('A','B'), t), (('B','D'), t2), ...]}
planification = {}

# Fonction pour planifier une voiture sans conflit
def planifier_voiture(nom, chemin):
    t_depart = 0
    while True:
        conflit = False
        t_courant = t_depart
        traj_planifie = []

        for i in range(len(chemin) - 1):
            depart = chemin[i]
            arrivee = chemin[i + 1]
            troncon = (depart, arrivee)

            # Vérifier si ce tronçon est déjà réservé à ce moment
            if troncon in reservation and t_courant in reservation[troncon]:
                conflit = True
                break

            traj_planifie.append((troncon, t_courant))
            t_courant += temps_par_troncon

        if not conflit:
            # Réserver les tronçons
            for troncon, t in traj_planifie:
                if troncon not in reservation:
                    reservation[troncon] = {}
                reservation[troncon][t] = nom
            planification[nom] = traj_planifie
            break
        else:
            t_depart += 1

# Planification pour toutes les voitures
for voiture, chemin in trajets.items():
    planifier_voiture(voiture, chemin)

# === Affichage console ===
print("\n=== PLANIFICATION DU TRAFIC ===\n")

for voiture, plan in planification.items():
    print(f"{voiture} :")
    for troncon, t in plan:
        print(f"  - Passe sur {troncon[0]} ➝ {troncon[1]} à t = {t}")
    print("")

# Affichage globale par temps
print("=== OCCUPATION DES TRONÇONS PAR TEMPS ===\n")
# Regrouper toutes les réservations par temps
occup_par_temps = {}
for troncon, temps_dict in reservation.items():
    for t, v in temps_dict.items():
        if t not in occup_par_temps:
            occup_par_temps[t] = []
        occup_par_temps[t].append((v, troncon))

for t in sorted(occup_par_temps.keys()):
    print(f"Temps t = {t}:")
    for v, troncon in occup_par_temps[t]:
        print(f"  {v} circule sur {troncon[0]} ➝ {troncon[1]}")
    print("")
