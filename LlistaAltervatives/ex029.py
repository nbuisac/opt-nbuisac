# Fes un programa que demani un número de 2 xifres màxim i l'escrigui en nombres romans. Per exemple el 49 s'escriu ajuntant el 40 i el 9: XLIX.

numero = int(input("Entra un nombre menor de 100 -> "))

if numero > 0 and numero <= 99:
    desena = numero // 10
    if desena >= 1 and desena <= 3:
        desenaRomana = "X" * desena
    elif desena == 4:
        desenaRomana = "XL"
    elif desena >= 5 and desena <= 8:
        desenaRomana = "L" + "X" * (desena - 5)
    elif desena == 9:
        desenaRomana = "XC"
    else:
        desenaRomana = ""
    
    unitats = numero % 10
    if unitats >= 1 and unitats <= 3:
        unitatsRomana = "I" * unitats
    elif unitats == 4:
        unitatsRomana = "IV"
    elif unitats >= 5 and unitats <= 8:
        unitatsRomana = "V" + "I" * (unitats- 5)
    elif unitats == 9:
        unitatsRomana = "IX"
    else:
        unitatsRomana = ""
    
    
    print(desenaRomana, unitatsRomana, sep="")
    print(desenaRomana + unitatsRomana)
    print(f"{desenaRomana}{unitatsRomana}")

else:
    print("Número incorrecte")
