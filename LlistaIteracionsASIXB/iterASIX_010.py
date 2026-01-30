# 10 Càlcul de consum mitjà: 
# Un bucle que demani a l'usuari el consum de RAM de diversos processos fins que s'escrigui "fi".
# Al final, ha de mostrar la mitjana de consum.
# Provarem de fer un programa que no peti... (try / except)

llista_consum = []

consum = input("Entra el consum (fi per acabar) -> ").strip().lower()
while consum != "fi":
    ## Tractem les dades
    try:
        consum_float = float(consum)
        llista_consum.append(consum_float)
    except ValueError:
        print("Error de format, dada no vàlida")
    except Exception:
        print("Error inesperat, continua...")
        raise Exception("programa abortat per error en les dades")
    ## Preparem la següent iteracio
    consum = input("Entra el consum (fi per acabar) -> ").strip().lower()

print(llista_consum)
mitjana = sum(llista_consum) / len(llista_consum)
print(f"La mitjana de consum és {mitjana:.2f}")
