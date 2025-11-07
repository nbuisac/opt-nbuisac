# Fes un programa que donada una data, digui a quina estació de l'any correspon:
# 21/03 – 20/06 	Primavera
# 21/06 – 20/09 	Estiu
# 21/09 – 20/12 	Tardor
# 21/12 – 20/03 	Hivern
dia = int(input("Entra el dia del mes -> "))
mes = int(input("Entra el mes -> "))

if mes <= 0:
    estacio = "ERROR"
elif mes <=2 :
    estacio = "hivern"
elif 