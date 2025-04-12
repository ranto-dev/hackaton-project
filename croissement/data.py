import json

# trajets = {
#     'V1': ['A', 'B', 'D', 'E'],
#     'V2': ['A', 'C', 'D', 'E'],
#     'V3': ['B', 'D', 'E'],
#     'V4': ['C', 'D'],
#     'V5': ['A', 'C', 'D', 'E'],
#     'V6': ['B', 'D', 'E'],
#     'V7': ['B', 'D', 'E'],
#     'V8': ['A', 'B', 'D', 'E'],
#     'V9': ['A', 'B', 'D', 'E'],
#     'V10': ['A', 'C', 'D', 'E'],
#     'V11': ['B', 'D', 'E'],
#     'V12': ['B', 'D', 'E'],
#     'V13': ['A', 'B', 'D', 'E'],
#     'V14': ['A', 'B', 'D', 'E'],
#     'V15': ['A', 'C', 'D', 'E'],
#     'V16': ['A', 'C', 'D', 'E'],
#     'V17': ['B', 'D', 'E'],
#     'V18': ['C', 'D'],
#     'V19': ['A', 'C', 'D', 'E'],
#     'V20': ['B', 'D', 'E'],
#     'V21': ['B', 'D', 'E'],
#     'V22': ['A', 'B', 'D', 'E'],
#     'V23': ['A', 'B', 'D', 'E'],
#     'V34': ['A', 'C', 'D', 'E'],
#     'V35': ['A', 'B', 'D', 'E'],  # Corrigé pour éviter doublons
#     'V36': ['B', 'D', 'E']
# }

temps_par_troncon = 1
reservation = []
planification = {}

with open('./data.json', 'r', encoding='utf-8') as file:
    res = json.load(file)

trajets = {}

for idx, value in enumerate(res):
    trajets[f'V{idx}'] = value['geometry']