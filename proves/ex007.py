# Fes un programa que passi d'euros a pessetes i/o al revés.
# Ens ha de demanar quina operació volem fer i l'import pertinent. Cal aplicar el canvi que toqui (1€ = 166'386 ptes)
PESSETES_PER_EURO = 166.386
opcio = input("Què vols fer?\n\t1) Euros a pessetes\n\t2) Pessetes a euros\nEscull una opció -> ")
if opcio == "1":
    print("Has escollit Euros a pessetes")
    euros = float(input("Entra l'import en euros -> "))
    pessetes = round(euros * PESSETES_PER_EURO)
    print(euros, "euros son", pessetes, "pessetes")
elif opcio == "2":
    print("Has escollit pessetes a Euros")
    pessetes = int(input("Entra l'import en pessetes -> "))
    euros = round(pessetes / PESSETES_PER_EURO, 2)
    print(f"{pessetes} pessetes són {euros} euros")
else:
    print("Opció incorrecta")