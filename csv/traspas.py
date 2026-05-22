import csv

nom_fitxer = "dades_vendes.csv"

llista_ok = []
llista_ko = []
with open(nom_fitxer, "rt", encoding="utf8") as f:
    lector = csv.DictReader(f, delimiter=",")
    for fila in lector:
        try:
            ## Agafem les dades
            id = int(fila["id"])
            producte = fila["producte"]
            preu = float(fila["preu"])
            quantitat = int(fila["quantitat"])

            total = preu * quantitat
            if total > 500:
                estat = 'PREMIUM'
            else:
                estat = 'STANDARD'
            estat = 'PREMIUM' if total > 500 else 'STANDARD'
            llista_ok.append((id, producte, total, estat))

        except Exception as e:
            llista_ko.append(fila)
            
print(llista_ok)
print("-"*80)
print(llista_ko)

import sqlite3
fitxer_db = "gestio_vendes.db"
conn = sqlite3.connect(fitxer_db)
sql_insert = "INSERT INTO comanda(id, producte, total, estat) VALUES(?, ?, ?, ?)"
c = conn.cursor()
try:
    sql_insert = f"INSERT INTO comanda(id, producte, total, estat) VALUES(?, ?, ?, ?)"
    c.executemany(sql_insert, llista_ok)
    conn.commit()
except Exception as e:
    print(e)
conn.close()

if len(llista_ko) > 0:
    fitxer_sortida = "vendes_no_carregades.csv"
    with open(fitxer_sortida, "at", encoding="utf8", newline="") as f:
        escriptor = csv.DictWriter(f, llista_ko[0].keys(), delimiter=",",quoting=csv.QUOTE_STRINGS)
        escriptor.writerows(llista_ko)








