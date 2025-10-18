# Fes un programa que ens digui si un número és parell o senar.
# Cal dividir per 2 i mirar el residu. Si el residu és 0 el nombre és parell i si el residu és 1 el nombre és senar.
numero = int(input("Entra un numero -> "))
if numero % 2 == 0:
    print(numero, "és parell")
else:
    print(f"{numero} és senar")