# import networkx as nx
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# # === Données de base ===
# trajets = {
#     'v1': [1, 2, 3],
#     'v2': [2, 3, 4],
#     'v3': [1, 4]
# }

# # Tronçons -> connexions entre noeuds (arêtes)
# # Pour simplifier, on suppose tronçon 1 = (A, B), 2 = (B, C), etc.
# troncons_graph = {
#     1: ('A', 'B'),
#     2: ('B', 'C'),
#     3: ('C', 'D'),
#     4: ('B', 'D')
# }

# # === Étape 1 : Planification simple sans conflits ===

# reservation = {}
# planification = {}
# temps_par_troncon = 1

# for vehicule, trajet in trajets.items():
#     t_depart = 0
#     while True:
#         conflit = False
#         t_courant = t_depart
#         for troncon in trajet:
#             if troncon in reservation and t_courant in reservation[troncon]:
#                 conflit = True
#                 break
#             t_courant += temps_par_troncon

#         if not conflit:
#             planification[vehicule] = []
#             t_courant = t_depart
#             for troncon in trajet:
#                 if troncon not in reservation:
#                     reservation[troncon] = {}
#                 reservation[troncon][t_courant] = vehicule
#                 planification[vehicule].append((troncon, t_courant))
#                 reservation[troncon][t_courant] = vehicule
#                 t_courant += temps_par_troncon
#             break
#         else:
#             t_depart += 1

# # === Étape 2 : Visualisation ===

# # Construire le graphe visuel
# G = nx.DiGraph()
# for troncon, (u, v) in troncons_graph.items():
#     G.add_edge(u, v, label=str(troncon))

# pos = nx.spring_layout(G)  # position automatique

# # Extraire tous les temps de passage
# t_max = max(max(t for _, t in traj) for traj in planification.values()) + 2

# fig, ax = plt.subplots(figsize=(8, 6))

# # Couleurs par véhicule
# couleurs = {
#     'v1': 'red',
#     'v2': 'blue',
#     'v3': 'green'
# }

# def get_voitures_sur_troncon(troncon, t):
#     voitures = []
#     for vehicule, plan in planification.items():
#         for t_id, t_time in plan:
#             if t_time == t and t_id == troncon:
#                 voitures.append(vehicule)
#     return voitures

# def update(frame):
#     ax.clear()
#     nx.draw(G, pos, with_labels=True, ax=ax, node_size=800, node_color="lightgray", font_weight='bold')
#     labels = nx.get_edge_attributes(G, 'label')
#     nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)

#     # Afficher les véhicules en transit à t = frame
#     for troncon_id, (u, v) in troncons_graph.items():
#         voitures = get_voitures_sur_troncon(troncon_id, frame)
#         for i, v_id in enumerate(voitures):
#             # Position intermédiaire entre u et v
#             x = (pos[u][0] + pos[v][0]) / 2
#             y = (pos[u][1] + pos[v][1]) / 2 + (i * 0.05)  # éviter chevauchement
#             ax.text(x, y, v_id, color=couleurs.get(v_id, 'black'),
#                     bbox=dict(facecolor='white', edgecolor='black', boxstyle='circle'))

#     ax.set_title(f"Temps t = {frame}")
#     ax.axis("off")

# ani = FuncAnimation(fig, update, frames=range(t_max), interval=1000, repeat=False)
# plt.tight_layout()
# plt.show()


import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# === Données de base ===
trajets = {
    'v1': [1, 2, 3],
    'v2': [2, 3, 4],
    'v3': [1, 4]
}

# Tronçons -> connexions entre noeuds (arêtes)
# Pour simplifier, on suppose tronçon 1 = (A, B), 2 = (B, C), etc.
troncons_graph = {
    1: ('A', 'B'),
    2: ('B', 'C'),
    3: ('C', 'D'),
    4: ('B', 'D')
}

# === Étape 1 : Planification simple sans conflits ===

reservation = {}
planification = {}
temps_par_troncon = 1

for vehicule, trajet in trajets.items():
    t_depart = 0
    while True:
        conflit = False
        t_courant = t_depart
        for troncon in trajet:
            if troncon in reservation and t_courant in reservation[troncon]:
                conflit = True
                break
            t_courant += temps_par_troncon

        if not conflit:
            planification[vehicule] = []
            t_courant = t_depart
            for troncon in trajet:
                if troncon not in reservation:
                    reservation[troncon] = {}
                reservation[troncon][t_courant] = vehicule
                planification[vehicule].append((troncon, t_courant))
                reservation[troncon][t_courant] = vehicule
                t_courant += temps_par_troncon
            break
        else:
            t_depart += 1

# === Étape 2 : Visualisation ===

# Construire le graphe visuel
G = nx.DiGraph()
for troncon, (u, v) in troncons_graph.items():
    G.add_edge(u, v, label=str(troncon))

pos = nx.spring_layout(G)  # position automatique

# Extraire tous les temps de passage
t_max = max(max(t for _, t in traj) for traj in planification.values()) + 2

fig, ax = plt.subplots(figsize=(8, 6))

# Couleurs par véhicule
couleurs = {
    'v1': 'red',
    'v2': 'blue',
    'v3': 'green'
}

def get_voitures_sur_troncon(troncon, t):
    voitures = []
    for vehicule, plan in planification.items():
        for t_id, t_time in plan:
            if t_time == t and t_id == troncon:
                voitures.append(vehicule)
    return voitures

def update(frame):
    ax.clear()
    nx.draw(G, pos, with_labels=True, ax=ax, node_size=800, node_color="lightgray", font_weight='bold')
    labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)

    # Afficher les véhicules en transit à t = frame
    for troncon_id, (u, v) in troncons_graph.items():
        voitures = get_voitures_sur_troncon(troncon_id, frame)
        for i, v_id in enumerate(voitures):
            # Position intermédiaire entre u et v
            x = (pos[u][0] + pos[v][0]) / 2
            y = (pos[u][1] + pos[v][1]) / 2 + (i * 0.05)  # éviter chevauchement
            ax.text(x, y, v_id, color=couleurs.get(v_id, 'black'),
                    bbox=dict(facecolor='white', edgecolor='black', boxstyle='circle'))

    ax.set_title(f"Temps t = {frame}")
    ax.axis("off")

ani = FuncAnimation(fig, update, frames=range(t_max), interval=1000, repeat=False)
plt.tight_layout()
plt.show()
