# Iteracions ASIX Exercici 11
# Monitoratge de Consum i Seguretat de Processos:
# Tenim una llista dels processos que s'estan executant actualment en un servidor Linux.
# Cada procés està representat per una tupla amb la següent informació:
# (PID, Nom_Procés, Usuari, %_CPU, Estat).
processos = [
    (101, "systemd", "root", 0.5, "running"),
    (102, "apache2", "www-data", 12.5, "running"),
    (103, "mysql", "mysql", 45.8, "running"),
    (104, "python3", "alumne", 85.2, "running"),
    (105, "bash", "alumne", 1.2, "sleeping"),
    (106, "apache2", "www-data", 14.1, "running"),
    (107, "cryptominer", "alumne", 98.5, "running"),
    (108, "nginx", "www-data", 2.1, "running")
]

def opcio1():
    # Filtratge de Processos Crítics: Utilitza un bucle per identificar quins processos consumeixen més del 80%
    # de la CPU. El programa ha d'imprimir una alerta indicant el nom del procés i l'usuari que el va llançar.
    for element in processos:
        if element[3] > 80:
            print(f"CRITIC: {element[1]} - {element[2]}")

def opcio2():
    # Càlcul de Càrrega per Usuari: Cal recórrer la llista i sumar el consum de CPU total d'un usuari concret
    # (per exemple, www-data). Fem-ho demanant el nom de l'usuari que volem analitzar.
    usuari = input("Entra el nom de l'usuari -> ").strip().lower()
    cpu_total = 0
    for _, _, user, cpu, _ in processos:
        if user == usuari:
            cpu_total = cpu_total + cpu
    print(f"L'usuari {usuari} està utilitzant un {cpu_total:.2f}% de cpu")
    ## Posem les dades en un diccionari (clau = usuari)
    d = dict()
    for e in processos:
        if e[2] in d:
            d[e[2]].append(e)
        else:
            d[e[2]] = [e]
    print(d)

def opcio3():
    ## Simulació de "kill" de Processos: Si un procés té el nom "cryptominer",
    # el programa ha d'imprimir:
    # "[SEGURETAT] Aturant PID {pid} per alt consum no autoritzat".
    for pid, proces, *_ in processos:
        if proces == "cryptominer":
            print(f"[SEGURETAT] Aturant PID {pid} per alt consum no autoritzat")

def opcio4():
    # Resum de l'Estat: 
    # Compta quants processos estan en estat "running" i quants en "sleeping".
    q_running = 0
    q_sleeping = 0
    d = dict()
    d["running"] = 0
    d["sleeping"] = 0
    for e in processos:
        if e[4] == "running":
            q_running = q_running + 1
        else:
            q_sleeping = q_sleeping + 1
        d[e[4]] = d[e[4]] + 1
    print(f"Processos running -> {q_running}")
    print(f"Processos sleeping -> {q_sleeping}")
    for estat in d:
        print(f"Processos {estat} -> {d[estat]}")

def menu():
    print("MENU")
    print("=" * 4)
    print("1.- Filtratge processos crítics")
    print("2.- Càrrega per usuari")
    print("3.- Kill de processos")
    print("4.- Resum de l'estat")
    print()
    op = input("Quina opció vols? ")
    return (op)

que_vols_fer = menu()
while que_vols_fer != "0":
    if que_vols_fer == "1":
        opcio1()
    elif que_vols_fer == "2":
        opcio2()
    elif que_vols_fer == "3":
        opcio3()
    elif que_vols_fer == "4":
        opcio4()
    que_vols_fer = menu()