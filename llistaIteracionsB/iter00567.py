print("Primers 20 números")
for i in range(20):
    print(i + 1, end=" ")
print()

numero = 0
mostrats = 0
while mostrats < 20:
    if numero % 2 == 0:
        print(numero, end = ' ')
        mostrats = mostrats + 1
    numero = numero + 1
print()

numero = 0
mostrats = 0
while mostrats < 20:
    if numero ** 0.5 == int(numero ** 0.5):
        print(numero, end = ' ')
        mostrats = mostrats + 1
    numero = numero + 1
print()

