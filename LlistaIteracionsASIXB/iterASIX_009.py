# Llista Iteracions ASIX
# 9.- Alertes de disc: Donada una llista o una tupla de tuples amb 
# el nom del servidor i el percentatge de disc ocupat,
# l'alumne ha de recórrer la llista i mostrar un missatge
# d'alerta ("CRITICAL") només per a aquells que superin el 90%.
# A més pots fer:
# Calcula la mitjana d'ocupació.
# Crea una llista negra amb els servidors que estan en alerta.
LLISTA_TUPLES = [
    ("WEB-PROD-01", 45.2),
    ("DB-SQL-PRIMARY", 92.8),
    ("MAIL-SERVER", 15.0),
    ("BACKUP-NAS", 98.1),
    ("DEV-SANDBOX", 60.5)
]
TUPLA_TUPLES = (
    (1, "SVR-WEB", "192.168.1.10", 30),
    (2, "SVR-DB", "192.168.1.20", 95),
    (3, "SVR-APP", "192.168.1.30", 88)
)
print("Tractem les dades de la LLISTA_TUPLES")
print(f"{'HOST':<20} {'%':>8}")
print(f"{('='*20)} {'='*8}")
suma_total = 0
for element in LLISTA_TUPLES:
    suma_total += element[1]
    if element[1] >= 90:
        print(f"{element[0]:<20} {element[1]:7.2f}%")

mitjana = round(suma_total / len(LLISTA_TUPLES), 2)
print("-" * 29)
print(f"{'Pct. d\'ocupacio ->':<20} {mitjana:7.2f}%")

print("Tractem les dades de la TUPLA_TUPLES")
print(f"{'HOST':<20} {'%':>8}")
print(f"{('='*20)} {'='*8}")
suma_total = 0
for element in TUPLA_TUPLES:
    suma_total += element[3]
    if element[3] >= 90:
        print(f"{element[1]:<20} {element[3]:7.2f}%")

mitjana = round(suma_total / len(TUPLA_TUPLES), 2)
print("-" * 29)
print(f"{'Pct. d\'ocupacio ->':<20} {mitjana:7.2f}%")