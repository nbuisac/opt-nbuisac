import csv
nom_fitxer = "Cost_campanyes_publicitat_2025.csv"
gastat = 0

llista_medis = []
llista_suma_despeses = []
with open(nom_fitxer, "rt", encoding="utf8") as f:
    reader = csv.reader(f, delimiter=";",)
    capcaleres = f.readline()
    for linia in reader:
        medi = linia[1].strip()
        preu = float(linia[5].replace(".", "").replace(",", "."))
        if medi in llista_medis:
            posicio = llista_medis.index(medi)
        else:
            llista_medis.append(medi)


print(llista_medis)
print(llista_suma_despeses)

## imprimim el valor de les dues llistes
# print(f"L'ajuntament de Girona ha gastat {gastat:.2f} en {'Temps de Flors '}")



# gastat = 0  
# with open(nom_fitxer, "rt", encoding="utf8") as f:
#     readerdict = csv.DictReader(f, delimiter=";")
#     for linia in readerdict:
#         apartat = linia[" Mitjà de comunicació"]
#         if apartat == en_que_s_ha_gastat:
#             preu = float(linia[" Preu (IVA inclòs)"].replace(".", "").replace(",", "."))
#             print(apartat, preu)
#             gastat = gastat + preu

# print(f"L'ajuntament de Girona ha gastat {gastat:.2f} en {en_que_s_ha_gastat}")









    # capcalera = f.readline().strip("\n")
    # linia = f.readline().strip("\n")
    # dades_linia = linia.split(";")
    # dades_capcalera = capcalera.split(";")
    # print(dades_capcalera)
    # print(dades_linia)

