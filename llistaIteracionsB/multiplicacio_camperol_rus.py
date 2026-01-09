# Multiplicació russa

numero1 = int(input("Entra un númoer enter -> "))
numero2 = int(input("Entra un númoer enter -> "))

if numero1 <= numero2:
    petit = numero1
    gran = numero2
else:
    petit, gran = numero2, numero1

llista=[]
while petit >= 1:
    print(petit, gran, sep="\t")
    if petit % 2 == 1:
        llista.append(gran)
    petit = petit // 2
    gran = gran * 2

print(f"{numero1} x {numero2} = {sum(llista)}\t({numero1 * numero2})")