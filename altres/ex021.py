# Fes un programa que donada una hora, minut i segon, incrementi un segon i
# mostri l'hora resultant.
# Cal verificar que l'hora estigui entre 0 i 23,
# els minuts entre 0 i 59 i els segons entre 0 i 59.
hora = int(input("Entra l'hora -> "))
if 0 <= hora <= 24:
    minuts = int(input("Entra els minuts -> "))
    if 0 <= minuts <= 60:
        segons = int(input("Entra els segons -> "))
        if 0 <= segons <= 60:
            segons = segons + 1
            if segons == 60:
                segons = 0
                minuts = minuts + 1
                if minuts == 60:
                    minuts = 0
                    hora = hora + 1
                    if hora == 24:
                        hora = 0
            print(f"{hora:02}:{minuts:02}:{segons:02}")
        else:
            print("Segons mal entrats")
    else:
        print("Minuts mal entrats")
else:
    print("Hora mal entrada")

