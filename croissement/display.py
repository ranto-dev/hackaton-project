from data import reservation, planification

def afficher_planification():
    print("\n=== PLANIFICATION DU TRAFIC ===\n")
    for voiture, plan in planification.items():
        print(f"{voiture} :")
        for troncon, t in plan:
            print(f"  - Passe sur {troncon[0]} ➝ {troncon[1]} à t = {t}")
        print("")

def afficher_occupation_par_temps():
    print("=== OCCUPATION DES TRONÇONS PAR TEMPS ===\n")
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
