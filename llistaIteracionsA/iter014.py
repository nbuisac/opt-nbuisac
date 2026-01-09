def suma(**a):
    print(a)
    # print(a[0])
    print(a['sep'])



print(suma(1, 2, 3))


## Divisors d'un número donat
numero = int(input("Introdueix un número -> "))

llista_divisors = []
for i in range(1, numero // 2 + 1):
    if numero % i == 0:
        llista_divisors.append(i)
llista_divisors.append(numero)

print(llista_divisors)
for element in llista_divisors:
    print(element)

if len(llista_divisors) == 2:
    print(numero, "es primer")
