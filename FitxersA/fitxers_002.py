nom_fitxer = r"C:\Users\nbuisac\Desktop\APUNTS\opt-nbuisac\FitxersA\passwd.txt"

with open(nom_fitxer, "rt", encoding="utf8") as f:
    l = f.readline()
    while l != "":
        ## tractem les dades
        dades = l.strip('\n').split(":")
        ample = max(i[0] for i in dades)
        print(f"{dades[0]:<ample} ({dades[2]:>5}) - {dades[6]}")

        ## llegim la següent línia
        l = f.readline()
