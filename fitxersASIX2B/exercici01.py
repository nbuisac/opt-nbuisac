# 1. Lectura: L'Auditoria de Seguretat
# # Objectiu: Utilitzar csv.reader per filtrar dades d'un fitxer existent.
# L'escenari: Tenim un fitxer anomenat accessos.csv amb les columnes:
#   data, usuari, ip, estat (on estat pot ser "èxit" o "fallida").
# L'exercici: Crea un programa que llegeixi el fitxer i mostri per pantalla
#   només els intents de connexió que han estat una "fallida".
# Al final, el programa ha de dir el número total d'intents fallits detectats.
import csv
nom_fitxer = "accessos.csv"
usuaris_exit = []
usuaris_fallida = []
with open(nom_fitxer,"r", encoding="utf-8") as f:
    lector = csv.reader(f,delimiter=",", quotechar='"')
    capçalera = next(lector)
    # print(capçalera)
    for dades in lector:
        data, usuari, ip, estat = dades
        if estat == "èxit":
            if usuari not in usuaris_exit:
                usuaris_exit.append(usuari)
        else:
            if usuari not in usuaris_fallida:
                usuaris_fallida.append(usuari)

for u in usuaris_exit:
    if not u in usuaris_fallida:
        print(u)