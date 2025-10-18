# Fes un programa que demani tres números introduïts per teclat i digui si estan ordenats.
# (dos nombres entrats consecutivament iguals considerarem que no trenquen l'ordre).
numero1 = int(input("Entra el número 1 -> "))
numero2 = int(input("Entra el número 2 -> "))
numero3 = int(input("Entra el número 3 -> "))
if numero1 <= numero2 and numero2 <= numero3 or \
   numero1 >= numero2 and numero2 >= numero3 :
    print("SÍ estan ORDENATS")
else:
    print("No estan ordenats")
## En Python podem posar el següent
if numero1 <= numero2 <= numero3 or \
   numero1 >= numero2 >= numero3 :
    print("SÍ estan ORDENATS")
else:
    print("No estan ordenats")