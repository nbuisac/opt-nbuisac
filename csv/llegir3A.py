import csv

nom_fitxer = r".\Cost_campanyes_publicitat_2025.csv"
diccionari = dict()
with open(nom_fitxer, "rt", encoding="utf8") as f:
    lectorCSV = csv.DictReader(f, delimiter=";")
    for linia in lectorCSV:
        medi = linia[' Mitjà de comunicació']
        medi = medi.strip()
        preu = linia[' Preu (IVA inclòs)']
        preu = preu.replace(".", "").replace(",",".")
        preu = float(preu)
        print(f"{medi:<25} -> {preu:10.2f}")
        if medi in diccionari:
            # total_preu, total_pagaments = diccionari[medi]
            # diccionari[medi] = (total_preu + preu, total_pagaments + 1)
            diccionari[medi]["pagat"] = round(diccionari[medi]["pagat"] + preu,2)
            diccionari[medi]["vegades"] = diccionari[medi]["vegades"] + 1
            pass
        else:
            diccionari[medi] = {"pagat" : preu, "vegades" : 1}

columnes = ["medi", "pagat", "vegades"]
with open("resum.csv", "wt", encoding="utf8", newline='') as f:
    escriptor = csv.DictWriter(f, columnes, quotechar='"', quoting=csv.QUOTE_STRINGS)
    escriptor.writeheader()
    for clau, valors in diccionari.items():
        escriptor.writerow({"medi":clau, "pagat": valors["pagat"], "vegades": valors["vegades"]})

