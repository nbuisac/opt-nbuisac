import csv

nom_fitxer = r".\Cost_campanyes_publicitat_2025.csv"
diccionari = dict() ## {}
with open(nom_fitxer, "rt", encoding="utf8")  as f:
    lectorCSV = csv.DictReader(f, delimiter = ";")
    for linia in lectorCSV:
        medi = linia[" Mitjà de comunicació"]
        medi = medi.strip()
        preu = linia[" Preu (IVA inclòs)"]
        preu = preu.replace(".", "").replace(",", ".")
        preu = float(preu)
        print(f"{medi:<25} -> {preu:10.2f}")
        if medi in diccionari:
            diccionari[medi]["preu"] = round(diccionari[medi]["preu"] + preu, 2)
            diccionari[medi]["vegades"] = diccionari[medi]["vegades"] + 1 
        else:
            diccionari[medi] = { "preu": preu, "vegades": 1 }

print(diccionari)
'''
{
'ARA': {'preu': 10186.62, 'vegades': 18},
'TOT OCI': {'preu': 1981.98, 'vegades': 9},
"L'ESPORTIU": {'preu': 5041.65, 'vegades': 5},
'GIDONA': {'preu': 1500.4, 'vegades': 4},
'VILAWEB': {'preu': 4500.0, 'vegades': 4},
'EL MÓN': {'preu': 4502.41, 'vegades': 5},
'EL NACIONAL': {'preu': 4840.0, 'vegades': 4}, 'EL GERIÓ': {'preu': 3310.31, 'vegades': 6}, 'RÀDIO GIRONA': {'preu': 10595.97, 'vegades': 8}, 'RAC1': {'preu': 5057.8, 'vegades': 7},
'''


