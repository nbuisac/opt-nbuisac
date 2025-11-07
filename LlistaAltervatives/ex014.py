# Fes un programa que digui si un any és de traspàs o no.
# Ho serà quan sigui múltiple de 4, com el 2020.
# Compte, els múltiples de 100 no són tots de traspàs,
#         només aquells que són múltiples de 400 com el 2000 (1900 no va ser de traspàs).
anyo = int(input("Entra un any -> "))
if anyo % 4 == 0: # És múltiple de 4
    if anyo % 100 == 0: # És multiple de 100
        if anyo % 400 == 0: # És múltiple de 400
            print("Sí ÉS de TRASPÀS")
        else:
            print("No és de traspàs")
    else:
        print("Sí ÉS de TRASPÀS")
else:
    print("No és de traspàs")
# Amb una sola condició
if anyo % 400 == 0 or anyo % 4 == 0 and anyo % 100 != 0:
    print("Sí ÉS de TRASPÀS")
else:
    print("No és de traspàs")
