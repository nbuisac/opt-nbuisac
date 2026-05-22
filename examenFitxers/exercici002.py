quants = int(input("Quants elements vols entrar? "))
nomFitxer = "inventari.txt"
i = 0
llista = []
with open(nomFitxer, "w", encoding="utf-8") as fw:
    for i in range(quants):
        tipus = input(f"Entra el tipus de l'element {i + 1} -> ")
        marca = input(f"Entra la marca de l'element {i + 1} -> ")
        ns = input(f"Entra el N/S de l'element {i + 1} -> ")
        llista.append([tipus, marca, ns])
        fw.write(f"{tipus} - {marca} - N/S: {ns}\n")
    fw.write("Fi de registre\n")
    
