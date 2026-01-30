## 10 Càlcul de consum mitjà:
# Un bucle que demani a l'usuari el consum de RAM de diversos processos
# fins que s'escrigui "fi".
# Al final, ha de mostrar la mitjana de consum.

llista_consums = []
consum = input("Entra el consum (fi per acabar) -> ").strip().lower()
while consum != "fi":
    ## tractem les dades
    try:
        consum_float = float(consum)
        llista_consums.append(consum_float)
    except ValueError as e:
        print(f"Dada mal introduïda. Error de Format! " + str(e))
    except Exception as e:
        print(e)
   
    ## preparem la següent interació
    consum = input("Entra el consum (fi per acabar) -> ").strip().lower()

print(llista_consums)
print(sum(llista_consums) / len(llista_consums))