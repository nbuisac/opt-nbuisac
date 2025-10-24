# Fes un programa que passi d'euros a pessetes i/o al revés.
# Ens ha de demanar quina operació volem fer i l'import pertinent.
# Cal aplicar el canvi que toqui (1€ = 166'386 ptes)
EUROS_A_PESSETES = 166.386
opcio = input("Escull una opcio\n\t1.- Euros a pessetes\n\t2.- Pessetes a euros\nQuè vols fer? ")
if opcio == "1":
    print("Has escollit Euros a pessetes")
    euros = float(input("Entra l'import en euros -> "))
    pessetes = round(euros * EUROS_A_PESSETES)
    print(f"{euros} euros son {pessetes} pessetes")
elif opcio == "2":
    print("Has escollit pessetes a euros")
    pessetes = int(input("Entra l'import en pessetes -> "))
    euros = round(pessetes / EUROS_A_PESSETES, 2)
    print(f"{pessetes} pessetes son {euros} euros")
else:
    print("Opcio erronia")