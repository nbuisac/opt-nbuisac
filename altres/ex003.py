# Calcula el valor absolut d'un número. i . (sempre positiu)
numero = float(input("Entra un numero -> "))
if numero >= 0:
    absolut = numero
else:
    absolut = -numero
print(f"|{numero}| = {absolut}")