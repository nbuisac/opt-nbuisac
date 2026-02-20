# Alertes de disc: Donada una llista o una tupla de tuples amb el
# nom del servidor i el percentatge de disc ocupat,
# l'alumne ha de recórrer la llista i mostrar un
# missatge d'alerta ("CRITICAL") només per a aquells que superin el 90%.
# A més pots fer:
#    Calcula la mitjana d'ocupació.
#    Crea una llista negra amb els servidors que estan en alerta.

# LLISTA_TUPLES = [
#     ("WEB-PROD-01", 45.2),
#     ("DB-SQL-PRIMARY", 92.8),
#     ("MAIL-SERVER", 15.0),
#     ("BACKUP-NAS", 98.1),
#     ("DEV-SANDBOX", 60.5)
# ]

# for v in LLISTA_TUPLES:
#     if v[1] > 90:
#         print(f"CRITIC el servidor {v[0]} - {v[1]}")

# for servidor, capacitat in LLISTA_TUPLES:
#     if capacitat > 90:
#         print(f"CRITIC el servidor {servidor} - {capacitat}")



TUPLA_TUPLES = (
    (1, "SVR-WEB", "192.168.1.10", 30),
    (2, "SVR-DB", "192.168.1.20", 95),
    (3, "SVR-APP", "192.168.1.30", 88)
)

suma = 0
comptador = 0
llista_negra = []
for identificador, servidor, ip, capacitat in TUPLA_TUPLES:
    suma = suma + capacitat
    comptador = comptador + 1
    if capacitat < 90:
        print(f"CRITIC {servidor} - {capacitat}")
        llista_negra.append((servidor, capacitat))

print("Mitjana de capacitat -> ", suma / comptador)
print(llista_negra)

