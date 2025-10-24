# Fes un programa que donada una hora, minut i segon,
# incrementi un segon i mostri l'hora resultant.
# Cal verificar que l'hora estigui entre 0 i 23,
# els minuts entre 0 i 59 i els segons entre 0 i 59.
correcte = False
hora = int(input("Entra una hora -> "))
if hora >= 0 and hora <= 23:
    minut = int(input("Entra els minuts -> "))
    if minut >= 0 and minut <= 59:
        segon = int(input("Entra els segons -> "))
        if segon >= 0 and segon <= 59:
            correcte = True
            segon = segon + 1
            if segon == 60:
                segon = 0
                minut = minut + 1
                if minut == 60:
                    minut = 0
                    hora = hora + 1
                    if hora == 24:
                        hora = 0

            print(f"{hora:02}:{minut:02}:{segon:02}")
if not correcte:
    print("Hola mal entrada")
