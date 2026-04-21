import math
from boucle import boucle

def init_jobs():
    c1_dyn = boucle()

    if c1_dyn is None:
        print("Erreur : Lancer boucle.py avant.")
        return []

    taches = {
        1: {'C': c1_dyn, 'T': 10},
        2: {'C': 3.0,    'T': 10},
        3: {'C': 2.0,    'T': 20},
        4: {'C': 2.0,    'T': 20},
        5: {'C': 2.0,    'T': 40},
        6: {'C': 2.0,    'T': 40},
        7: {'C': 3.0,    'T': 80}
    }

    charge = sum(t['C'] / t['T'] for t in taches.values())
    print(f"Charge du CPU totale : {charge * 100:.1f}%")

    if charge > 1.0:
        print("Erreur : Charge > 100%")
        return []

    periodes = [t['T'] for t in taches.values()]
    hyper_P = math.lcm(*periodes)
    print(f"Hyperpériode : {hyper_P} ms")

    liste_jobs = []

    for id_tache, t in taches.items():
        nb_jobs = hyper_P // t['T']
        for i in range(nb_jobs):
            arrivee = i * t['T']
            deadline = arrivee + t['T']

            job = {
                'id_tache': id_tache,
                'num_instance': i + 1,
                'C': t['C'],
                'arrivée': arrivee,
                'deadline': deadline
            }
            liste_jobs.append(job)

    print(f"Nombre de jobs : {len(liste_jobs)}")
    return liste_jobs

if __name__ == "__main__":
    jobs = init_jobs()
    print("\nPremiers jobs :")
    for j in jobs[:5]:
        print(j)
