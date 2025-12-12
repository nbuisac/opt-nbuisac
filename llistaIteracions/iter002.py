opcio = input("Vols continuar (s/n) -> ")
opcio = opcio.strip().lower()
while opcio not in ["s", "n"]:
    opcio = input("ERROR: Vols continuar (s/n) -> ")
    opcio = opcio.strip().lower()

print("L'usuari ha dit ->", opcio)

