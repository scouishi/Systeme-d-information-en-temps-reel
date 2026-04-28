from ordonnanceur import init_jobs

def algo_sans_depasse(jobs):
    temps = 0
    jobs_restants = jobs.copy()
    planning = []
    attente_totale = 0

    while len(jobs_restants) > 0:

        dispos = []
        for j in jobs_restants:
            if j['arrivée'] <= temps:
                dispos.append(j)

        if len(dispos) == 0:
            tps_suivat = 99999
            for j in jobs_restants:
                if j['arrivée'] < tps_suivat:
                    tps_suivat = j['arrivée']
            temps = tps_suivat
            continue

        dispos.sort(key=lambda x: x['deadline'])
        job = dispos[0]

        debut = temps
        fin = debut + job['C']

        if fin > job['deadline']:
            return None, 0

        attente = debut - job['arrivée']
        attente_totale = attente_totale + attente

        planning.append((job, debut, fin))
        jobs_restants.remove(job)
        temps = fin

    return planning, attente_totale

def algo_t5_depasse(jobs):
    temps = 0
    jobs_restants = jobs.copy()
    planning = []
    attente_totale = 0

    while len(jobs_restants) > 0:
        dispos = []
        for j in jobs_restants:
            if j['arrivée'] <= temps:
                dispos.append(j)

        if len(dispos) == 0:
            prochain_temps = 99999
            for j in jobs_restants:
                if j['arrivée'] < prochain_temps:
                    prochain_temps = j['arrivée']
            temps = prochain_temps
            continue

        for d in dispos:
            if d['id_tache'] == 5:
                d['deadline_fake'] = 99999
            else:
                d['deadline_fake'] = d['deadline']

        dispos.sort(key=lambda x: x['deadline_fake'])
        job = dispos[0]

        debut = temps
        fin = debut + job['C']

        if fin > job['deadline'] and job['id_tache'] != 5:
            return None, 0

        attente = debut - job['arrivée']
        attente_totale = attente_totale + attente

        planning.append((job, debut, fin))
        jobs_restants.remove(job)
        temps = fin

    return planning, attente_totale

def afficher_trace(planning):
    temps_precedent = 0
    dernier_arrivee = -1

    for job, debut, fin in planning:
        if debut > temps_precedent:
            print(f"(CPU Idle from {temps_precedent:.2f} ms to {debut:.2f} ms)")

        arrivee = job['arrivée']

        if arrivee != dernier_arrivee:
            if dernier_arrivee != -1 and arrivee < dernier_arrivee:
                print(f"\nPending from {arrivee} ms:\n")
            else:
                print(f"\nArrivals at {arrivee} ms:\n")
            dernier_arrivee = arrivee

        reponse = fin - arrivee
        status = "OK" if fin <= job['deadline'] else "LATE"

        print(f"t{job['id_tache']}_{job['num_instance']} | Finish: {fin:.2f} ms | Response: {reponse:.2f} ms | Deadline: {job['deadline']} ms ({status})")

        temps_precedent = fin

    if temps_precedent < 80:
        print(f"(CPU Idle from {temps_precedent:.2f} ms to 80.00 ms)")

if __name__ == "__main__":
    jobs = init_jobs()

    print("\n Test no deadlines miss")
    plan1, att1 = algo_sans_depasse(jobs)
    if plan1:
        afficher_trace(plan1)
        print(f"\nAttente totale : {att1:.2f} ms")
    else:
        print("Erreur")

    print("\n Test avec t5 qui dépasse")
    plan2, att2 = algo_t5_depasse(jobs)
    if plan2:
        print(f"Attente totale : {att2:.2f} ms")
    else:
        print("Erreur")

    if att1 < att2:
        print("\n Plus long avec t5 qui dépasse")
    else:
        print("\n Plus rapide avec t5 qui dépasse")
