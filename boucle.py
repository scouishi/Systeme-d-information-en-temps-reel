import os
import subprocess
import time
import numpy as np

def boucle():
    compil = subprocess.run(["gcc", "tache_1.c", "-o", "tache_1"])

    mes_temps = []
    n_tests = 1000

    for i in range(n_tests):
        debut = time.perf_counter()
        subprocess.run(["./tache_1"], stdout=subprocess.DEVNULL)
        fin = time.perf_counter()
        mes_temps.append((fin - debut) * 1000)

    mini = np.min(mes_temps)
    wcet = np.max(mes_temps)
    q1 = np.percentile(mes_temps, 25)
    q2 = np.median(mes_temps) 
    q3 = np.percentile(mes_temps, 75)

    print(f"Tests: {n_tests}")
    print(f"Min: {mini:.3f} ms")
    print(f"Q1:  {q1:.3f} ms")
    print(f"Q2:  {q2:.3f} ms")
    print(f"Q3:  {q3:.3f} ms")
    print(f"WCET (C1): {wcet:.3f} ms")

    return wcet

if __name__ == "__main__":
    boucle()
