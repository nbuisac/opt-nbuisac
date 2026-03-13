import csv

nom_fitxer = r".\Cost_campanyes_publicitat_2025.csv"

llista_medis = []
llista_pagaments = []
with open(nom_fitxer, "rt", encoding="utf8")  as f:
    # # El llegim tot dew cop
    # contingut = f.read()
    ## Llegim linia a linia
    f.readline()
    lectorCSV = csv.reader(f, delimiter = ";")
    for linia in lectorCSV:
        print(f"{linia[1]:<25} -> {linia[5]:>10}")
        medi = linia[1].strip()
        preu = float(linia[5].replace(".","").replace(",","."))
        if medi not in llista_medis:
            llista_medis.append(medi)
            llista_pagaments.append(preu)
        else:
            posicio = llista_medis.index(medi)
            llista_pagaments[posicio] = llista_pagaments[posicio] + preu
print("="* 80)
for medi, preu in zip(llista_medis, llista_pagaments):
    print(f"{medi:<25} -> {preu:>10.2f}")
        


