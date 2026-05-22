import csv
nom_fitxer = "usuaris.csv"
inactius = []
alerta_seguretat = []
total = 0
with open(nom_fitxer, "r", encoding="utf-8") as f:
    lector = csv.reader(f)
    next(lector)
    for usuari, departament, claus, dies in lector:
        total += 1
        if int(dies) > 90:
            if not usuari in inactius:
                inactius.append(usuari)
        if departament == "IT" and claus == "no":
            alerta_seguretat.append(usuari)
print(f"Usuaris llegits: {total}")
if len(inactius) == 0:
    print("Sense usuaris inactius")
else:
    print("Usuaris sense activitat: ", ", ".join(inactius))

if len(alerta_seguretat) == 0:
    print("Sense usuaris amb alerta de seguretat")
else:
    print("Usuaris amb problemes de claus: ", ", ".join(alerta_seguretat))