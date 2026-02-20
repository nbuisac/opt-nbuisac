opcions = [
    "Filtratge processos crítics",
    "Càrrega per usuari",
    "Kill de processos",
    "Resum de l'estat"
]

def menu(op):
    print("MENU")
    print("=" * 4)
    for i, o in enumerate(opcions):
        print(f"{i + 1}.- {o}")

que_vols_fer = menu(opcions)