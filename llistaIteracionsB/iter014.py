## Programa que mostra els divisors d'un número donat

numero = int(input("Entra un nombre enter -> "))
llista_divisors = []
for i in range(1, numero + 1):
    if numero % i == 0:
        llista_divisors.append(i)
## Tinc els divisord desats a llista_divisors
if len(llista_divisors) == 2:
    print(f"{numero} Sí és primer")
else:
    print(f"{numero} No és primer")
print("Els divisors són:", end = " ")
for n in llista_divisors: 
    print(n, end=" ")
print()