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
