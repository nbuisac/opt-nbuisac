import csv
nom_fitxer = "equips.csv"

per_guardar = []
with open(nom_fitxer, mode="r", encoding="utf-8") as f:
    lector = csv.DictReader(f)
    for dades in lector:
        if dades["estat"] == "èxit":
            if dades["usuari"] not in per_guardar:
                per_guardar.append(dades["usuari"])
                print(dades["usuari"])
    
# print(per_guardar)