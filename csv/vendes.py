import csv

llista_ok= []
llista_ko = []
nom_fitxer = r"C:\Users\nbuisac\Desktop\APUNTS\opt-nbuisac\csv\dades_vendes.csv"
with open(nom_fitxer, "rt", encoding="utf8") as f:
    reader = csv.DictReader(f)
    for linia in reader:
        try:
            id = linia["id"]
            producte = linia["producte"]
            preu = float(linia["preu"])
            quantitat = int(linia["quantitat"])
            print(linia)

            ## transformació/Creació els nous camps total/estat
            total = round(preu * quantitat, 2)
            if total > 500:
                estat = 'PREMIUM'
            else:
                estat = 'ESTANDARD'
            estat = 'PREMIUM' if total > 500 else 'ESTANDARD'
            llista_ok.append((id, producte, total, estat))
        except Exception as e:
            llista_ko.append(linia)
            print(e)
print(llista_ko)
print(llista_ok)

if len(llista_ko) > 0:
    fitxer_sortida = "vendes_no_carregades.csv"
    with open(fitxer_sortida, "at", encoding="utf8",newline="") as f:
        escriptor = csv.DictWriter(f, llista_ko[0].keys(),delimiter=":",quoting=csv.QUOTE_STRINGS)
        escriptor.writerows(llista_ko)

import sqlite3
if len(llista_ok) > 0:
    conn = sqlite3.connect(r"C:\Users\nbuisac\Desktop\APUNTS\opt-nbuisac\csv\gestio_vendes.db")
    sql = "INSERT INTO comanda(id, producte, total, estat) VALUES(?, ?, ?, ?)"
    c = conn.cursor()
    c.executemany(sql, llista_ok)
    conn.commit()
    conn.close()

# import sqlite3
# if len(llista_ok) > 0:
#     conn = sqlite3.connect("gestio_vendes.db")
#     for element in llista_ok:
#         c = conn.cursor()
#         c.execute("INSERT INTO comanda(id, producte, total, estat) VALUES(?, ?, ?, ?)", element)
#     conn.commit()
#     conn.close()





