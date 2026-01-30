nom_fitxer = r".\dades.txt"
nom_fitxer = ".\\dades.txt"
nom_fitxer = "./FitxersB/dades.txt"
# nom_fitxer = r"C:\Users\nbuisac\Desktop\APUNTS\opt-nbuisac\FitxersB\dades.txt"
print(nom_fitxer)
with open(nom_fitxer,"rt", encoding="utf8") as f:
    t = f.read()
    if t != "":
        print(t)

