# Exemple de trajets fixes pour chaque voiture
trajets = {
    'v1': [1, 2, 3],
    'v2': [2, 3, 4],
    'v3': [1, 4]
}

# Initialisation
# Réserve : {tronçon: {temps: nom_voiture}}
reservation = {}

# Stocker les temps de passage par véhicule
planification = {}

# Durée d'occupation d’un tronçon
temps_par_troncon = 1

# Algo : planifier séquentiellement
for vehicule, trajet in trajets.items():
    t_depart = 0  # essaie au plus tôt
    while True:
        conflit = False
        t_courant = t_depart
        # Tester si tous les tronçons sont libres à ces temps-là
        for troncon in trajet:
            if troncon in reservation and t_courant in reservation[troncon]:
                conflit = True
                break
            t_courant += temps_par_troncon

        if not conflit:
            # C’est bon, on peut réserver ce créneau
            planification[vehicule] = []
            t_courant = t_depart
            for troncon in trajet:
                if troncon not in reservation:
                    reservation[troncon] = {}
                reservation[troncon][t_courant] = vehicule
                planification[vehicule].append((troncon, t_courant))
                t_courant += temps_par_troncon
            break
        else:
            # Décaler le départ d'une unité de temps
            t_depart += 1

# Affichage du plan de circulation
print("Planification des trajets :")
for vehicule, plan in planification.items():
    print(f"{vehicule}:")
    for troncon, t in plan:
        print(f"  Tronçon {troncon} à t = {t}")
