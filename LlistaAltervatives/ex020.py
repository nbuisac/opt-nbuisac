#  Volem calcular el preu d'una entrada de cinema:
# Sabem que una entrada est├ándard val 5 €.
#     Si tens carnet jove et fan un 15% de descompte.
#     Els dimarts fan un 20%.
#     El cap de setmana no fan cap descompte a ningú.
#     Només et poden fer un descompte.
PREU = 5
descompte = 0
cap_de_setmana = input("És cap de setmana (s/n) ? ").casefold()
if not( cap_de_setmana == "s"):
    es_dimarts = input("És dimarts (s/n) ? ")
    if es_dimarts == "s":
        descompte = 0.20
    else:
        carnet_jove = input("Tens el Carnet jove (s/n) ? ")
        if carnet_jove == "s":
            descompte = 0.15
preu_final = PREU - PREU * descompte
print(f"{PREU:.2f} - {PREU * descompte:.2f} ({descompte :.0%}) = {preu_final}")