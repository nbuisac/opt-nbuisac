nom_fitxer = "dades.txt"

llista = ["taronja", "groc", "verd", "blau"]

with open(nom_fitxer, "at", encoding="utf8") as f:
    f.writelines(a + "\n" for a in llista)

