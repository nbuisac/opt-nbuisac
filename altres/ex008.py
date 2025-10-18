# Fes un programa que ens demani la operació que volem fer (+, -, * ó /),
# dos valors i mostri el resultat pertinent.
opcio = input("Entra la opcio que vols fer\n\t(1) Sumar\n\t(2) Restar\n\t(3) Multiplicar\n\t(4) Dividir\n (1..4) -> ")
if len(opcio) == 1 and opcio in "1234": # Estem comprovant que sigui un dels caràcters demanats
    primer_numero = int(input("Entra el primer número -> "))
    segon_numero = int(input("Entra el segon número -> "))

    if opcio == "1":
        operacio = "+"
        resultat = primer_numero + segon_numero
    elif opcio == "2":
        operacio = "-"
        resultat = primer_numero - segon_numero
    elif opcio == "3":
        operacio = '*'
        resultat = primer_numero * segon_numero
    elif segon_numero != 0:
        operacio = '/'
        resultat = primer_numero / segon_numero
    else:
        operacio = ""
    if operacio == "":
        print("No es pot dividir per zero")
    else:
        print(f"{primer_numero} {operacio} {segon_numero} = {resultat}")
else:
    print("opció incorrecta")
