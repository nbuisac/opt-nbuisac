# Volem calcular el preu d'una entrada de cinema:
# Sabem que una entrada estàndard val 5 €.
#     Si tens carnet jove et fan un 15% de descompte.
#     Els dimarts fan un 20%.
#     El cap de setmana no fan cap descompte a ningú.
#     Només et poden fer un descompte.
PREU = 5
cap_de_setmana = input("És cap de setmana (s/n) ?")
if cap_de_setmana.lower() == 's':
    descompte = 0
else:
    es_dimarts = input("És dimarts (s/n) ?")
    if es_dimarts.lower() == 's':
        descompte = 0.20
    else:
        carnet_jove = input("Tens carnet Jove (s/n) ?")
        if carnet_jove.lower() == 's':
            descompte = 0.15
        else:
            descompte = 0
print(f"El preu final a pagar és {PREU - PREU * descompte:.2f} ({descompte:.0%} dcte)")
        
