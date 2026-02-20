# Iteracions ASIX Exercici 10
# Afegirem TOTA la informació en una llista!
llista = []

dada = input("Entra el consum de RAM -> ").strip().lower()
while dada != "fi":
    ## Tractem les dades
    llista.append(dada)

    ## Preparem la següent la iteració
    dada = input("Entra el consum de RAM -> ").strip().lower()