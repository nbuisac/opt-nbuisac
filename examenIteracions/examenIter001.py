# Exercici 1
# Aquest exercici demana comparar una llista de ports detectats amb una llista de ports "permesos".
# Enunciat: El departament de seguretat diu que només els ports [80, 443, 22] són segurs. Hem fet un escaneig i hem obtingut aquesta llista de ports oberts en un servidor:
# ports_escanejats = [22, 80, 443, 8080, 21, 22, 443] # (Nota: hi ha duplicats perquè l'escaneig ha passat dos cops).
# Escriu un programa que:

ports_escanejats = [22, 80, 443, 8080, 21, 22, 443] # (Nota: hi ha duplicats perquè l'escaneig ha passat dos cops).

#     Crei una nova llista sense duplicats de la llista de ports escanejats (sense usar set(), fent servir bucles).
#     i la mostri a continuació
ports_no_duplicats = []
for port in ports_escanejats:
    if port not in ports_no_duplicats:
        ports_no_duplicats.append(port)
print(ports_no_duplicats)
#     Identifiqui quins ports estan oberts i no són segurs.
#     i els mostri
ports_oberts_no_segurs = []
for port in ports_no_duplicats:
    if not port in [80, 443, 22]:
        ports_oberts_no_segurs.append(port)

#     Mostri un resum: "S'han trobat X ports insegurs: [llista_de_ports]".
print(f"S'han trobat {len(ports_oberts_no_segurs)} ports insegurs: {ports_oberts_no_segurs}")