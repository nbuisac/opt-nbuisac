nomFitxer = "inventari.txt"
quants = int(input("Quants elements vols entrar? "))
i = 0
llista = []
for i in range(quants):
    tipus = input(f"Entra el tipus de l'element {i + 1} -> ")
    marca = input(f"Entra la marca de l'element {i + 1} -> ")
    ns = input(f"Entra el N/S de l'element {i + 1} -> ")
    llista.append([tipus, marca, ns])

for i in llista:
    tipus, marca, ns = i
    print(f"{tipus} - {marca} - N/S: {ns}")
print("Fi de registre\n")
    
