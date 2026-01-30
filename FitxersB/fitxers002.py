nom_fitxer = "passwd"
with open(nom_fitxer) as f:
    linia = f.readline()
    while linia != "":
        ## tractar les dades
        dades = linia.strip("\n").split(":")
        print(f"useradd -m -s {dades[6]} {dades[0]}")
        ## llegir la següent linia
        linia = f.readline()