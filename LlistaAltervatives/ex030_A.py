# Fes un programa que donada una data, digui a quina estació de l'any correspon:
# 21/03 – 20/06 	Primavera
# 21/06 – 20/09 	Estiu
# 21/09 – 20/12 	Tardor
# 21/12 – 20/03 	Hivern
dia = int(input("Entra el dia del mes -> "))
mes = int(input("Entra el mes -> "))

if mes < 1 or mes > 12:
    estacio = "ERROR"
elif mes == 3 and dia >= 21 or mes == 4 or mes == 5 or mes == 6 and dia < 21:
    estacio = "primavera"
elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia < 21:
    estacio = "estiu"
elif mes == 9 and dia >= 21 or mes == 10 or mes == 11 or mes == 12 and dia < 21:
    estacio = "tardor"
else:
    estacio = "hivern"

if mes <= 0:
    estacio = "ERROR"
elif mes <=2 :
    estacio = "hivern"
elif mes == 3:
    if dia < 21:
        estacio = "hivern"
    else:
        estacio = "primavera"
elif mes <= 5:
    estacio = "primavera"
elif mes == 6:
    if dia < 21:
        estacio = "primavera"
    else:
        estacio = "estiu"
elif mes <= 8:
    estacio = "estiu"
elif mes == 9:
    if dia < 21:
        estacio = "estiu"
    else:
        estacio = "tardor"
elif mes <= 11:
    estacio = "tardor"
elif mes == 12:
    if dia < 21:
        estacio = "tardor"
    else:
        estacio = "hivern"
else:
    estacio = "ERROR"

print(f"El {dia}/{mes} pertany a {estacio}")