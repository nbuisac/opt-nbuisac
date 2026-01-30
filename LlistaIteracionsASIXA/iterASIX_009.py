# Llista Iteracions ASIX
# 9. Alertes de disc: Donada una llista o una tupla de tuples amb el
# nom del servidor i el percentatge de disc ocupat,
# l'alumne ha de recórrer la llista i mostrar un missatge d'alerta
# ("CRITICAL") només per a aquells que superin el 90%.
# A més pots fer:
# Calcula la mitjana d'ocupació.
# Crea una llista negra amb els servidors que estan en alerta.
LLISTA_TUPLES = [
    ("WEB-PROD-01", 45.2),
    ("DB-SQL-PRIMARY", 92.82),
    ("MAIL-SERVER", 15.0),
    ("BACKUP-NAS", 98.1),
    ("DEV-SANDBOX", 60.5)
]
print(f"{'HOST':^25} {'% Ocup.':>8}")
print(f"{'=' * 25} {'=' * 8}")
total_ocupacio = 0
for element in LLISTA_TUPLES:
    # element = ("WEB-PROD-01", 45.2)
    # element[0] = "WEB-PROD-01"
    # element[1] = 45.2
    total_ocupacio += element[1]
    if element[1] >= 90:
        print(f"{element[0]:<25} {element[1]:7.2f}%")
print('-' * 34)
mitjana_ocupacio = total_ocupacio / len(LLISTA_TUPLES)
print(f"Mitjana d'ocupacio {mitjana_ocupacio:5.2f}%")



TUPLA_TUPLES = (
    (1, "SVR-WEB", "192.168.1.10", 30),
    (2, "SVR-DB", "192.168.1.20", 95),
    (3, "SVR-APP", "192.168.1.30", 88)
)
print(f"{'HOST':^25} {'% Ocup.':>8}")
print(f"{'=' * 25} {'=' * 8}")
total_ocupacio = 0
for element in TUPLA_TUPLES:
    # element = ("SVR-WEB", 30)
    # element[1] = "SVR-WEB"
    # element[-1] = 30
    total_ocupacio += element[-1]
    if element[-1] >= 90:
        print(f"{element[1]:<25} {element[-1]:7.2f}%")
print('-' * 34)
mitjana_ocupacio = total_ocupacio / len(LLISTA_TUPLES)
print(f"Mitjana d'ocupacio {mitjana_ocupacio:5.2f}%")

