import random
import time
import json

def generate_point():
    return {
        "latitude": round(random.uniform(-18.95, -18.80), 6),
        "longitude": round(random.uniform(47.45, 47.60), 6),
        "accuracy": round(random.uniform(5, 50), 2),
        "altitude": round(random.uniform(1200, 1500), 2),
        "timestamps": int(time.time()) + random.randint(-10000, 10000),
        "speed": round(random.uniform(0, 15), 2),
        "bearing": round(random.uniform(0, 360), 2)
    }

# Génération de 100 objets
data = [generate_point() for _ in range(100)]

# Optionnel : écrire dans un fichier JSON
with open("antananarivo_gps_data.json", "w") as f:
    json.dump(data, f, indent=4)

# Affichage des 3 premiers exemples
for d in data[:3]:
    print(d)