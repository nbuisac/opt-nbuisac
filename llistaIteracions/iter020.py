numero = int(input("Entra un nombre enter -> "))

arrel = 0
while arrel * arrel <= numero:
    arrel = arrel + 1
arrel = arrel - 1
print(f"L'arrel quadrada de {numero} és {arrel}")

## Anem a afegir decimals
N_DECIMALS = 5
for i in range(N_DECIMALS):
    digit = 1
    arrel_amb_digit = arrel + digit * (10 ** (-1))
    

