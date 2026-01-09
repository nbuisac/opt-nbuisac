numero1 = int(input("Entra un numero enter -> "))
numero2 = int(input("Entra un numero enter -> "))

if numero1 < numero1:
    petit = numero1
    gran = numero2
else:
    petit, gran = numero2, numero1

llista = []
while petit >= 1:
    if petit % 2 == 1:
        llista.append(gran)
    petit = petit // 2
    gran = gran * 2

print(llista)
print(sum(llista))
