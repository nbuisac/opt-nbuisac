# Fes un programa que demani tres números introduïts per teclat i
# ens digui quin és el més gran.
numero1 = int(input("Entra el número 1 -> "))
numero2 = int(input("Entra el número 2 -> "))
numero3 = int(input("Entra el número 3 -> "))
# Comparant els tres de cop
if numero1 >= numero2 and numero1 >= numero3 :
    gran = numero1
elif numero2 >= numero1 and numero2 >= numero3 :
    gran = numero2
else:
    gran = numero3
print("El numero més gran és el", gran)
# Comparant de dos en dos
if numero1 >= numero2:
    if numero1 >= numero3:
        gran = numero1
    else:
        gran = numero3
elif numero2 >= numero3:
    gran = numero2
else:
    gran = numero3
print("El numero més gran és el", gran)
