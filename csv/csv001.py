import csv
nom_fitxer = "Cost_campanyes_publicitat_2025.csv"
despeses = 0
with open(nom_fitxer, "rt", encoding="utf") as f:
    reader = csv.DictReader(f, delimiter=';')
    for linia in reader:
        preu = float(linia[' Preu (IVA inclòs)'].replace(".","").replace(",","."))
        print(linia[' Mitjà de comunicació'], preu)
        despeses = despeses + preu

print(f"S'han gastat {despeses:.2f}")












    # capcalera = f.readline()
    # linia = f.readline()
    # dades_capcalera = capcalera.split(";")
    # dades_linia = linia.split(";")
    # print(dades_capcalera[1], ":", dades_linia[1] )
    # preu = float(dades_linia[5].strip('"').replace(",","."))
    # print(dades_capcalera[5], ":", preu )
