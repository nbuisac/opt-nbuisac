nom_fitxer = ".\\dades.txt"
nom_fitxer = r".\dades.txt"
nom_fitxer = "./dades.txt"
nom_fitxer = r"C:\Users\nbuisac\Desktop\APUNTS\opt-nbuisac\FitxersA\dades.txt"

VOCALS = "aeiuouAEIOUàèìòùÀÈÌÒÙáéíóúÁÉÍÓÚäëïöüÄËÏÖÜ"
comptador = 0
with open(nom_fitxer, "rt", encoding="utf8") as f:
    c = f.read(1)
    while c != "":
        ## tractar les dades
        if c in VOCALS:
            print("a", end="")
        else:
            print(c, end="")
        ## accedim al següent
        c = f.read(1)
