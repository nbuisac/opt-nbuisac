import csv

nom_fitxer = r".\Cost_campanyes_publicitat_2025.csv"
llista = []
with open(nom_fitxer, "rt", encoding="utf8") as f:
    lectorCSV = csv.DictReader(f, delimiter=";")
    for linia in lectorCSV:
        campanya = linia["Campanya"].strip()
        medi = linia[" Mitjà de comunicació"].strip()
        preu = float(linia[" Preu (IVA inclòs)"].replace(".","").replace(",","."))
        llista.append((campanya, medi, preu))
print(llista)
## Crearem un fitxer csv amb les dades de llista
nom_fitxer_sortida = "campanya.csv"
with open(nom_fitxer_sortida, "wt", encoding="utf8",newline="") as f:
    escriptorCSV= csv.writer(f, delimiter=",",quoting=csv.QUOTE_STRINGS)
    escriptorCSV.writerow(("campanya", "medi", "preu"))
    escriptorCSV.writerows(llista)

## Inserirem les dades de la llista a la base de dades
import sqlite3
conn = sqlite3.connect('baseDeDades.db')
c = conn.cursor()
for fila in llista:
    c.execute("INSERT INTO publicitat(campanya, medi, preu) VALUES (?, ?, ?)", fila)
conn.commit()
conn.close()
