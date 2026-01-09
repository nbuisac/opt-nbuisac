## Generador de noms d'usuari:
# Donada una llista amb noms i cognoms reals (ex: ["Pere Pi", "Marta Mas"]),
# utilitza un bucle per generar noms d'usuari en format
# lowercase i sense espais (ex: ppi, mmas o pere.pi, marta.mas).

import unicodedata
import os

os.system("cls")

usuaris_nous = [
    ("Jordi", "Puigvert i Casals"),
    ("Montserrat", "Vila i Rovira"),
    ("Arnau", "Serra i Martí"),
    ("Laia", "Font i Capdevila"),
    ("Oriol", "Soler i Gual"),
    ("Meritxell", "Riba i Bosch"),
    ("Marc", "Prats i Roca"),
    ("Marc", "Prats i Roca"),
    ("Marc", "Prats i Roca"),
    ("Marc", "Prats i Roca"),
    ("Eulàlia", "Ventura i Grau"),
    ("Pol", "Sabaté i Solé"),
    ("Paula", "Sabaté i Bosc"),
    ("Pere", "Sabaté i Mar"),
    ("Aina", "Garriga i Cañellas")
]
usuaris_creats = []
for nom, cognoms in usuaris_nous:
    nom_normalitzat = unicodedata.normalize('NFKD', nom).encode('ascii', 'ignore').decode('ascii')
    cognoms_normalitzat = unicodedata.normalize('NFKD', cognoms).encode('ascii', 'ignore').decode('ascii')
    n = nom_normalitzat[0]
    c = cognoms_normalitzat.split()[0]
    usuari_inicial = (n + c).lower()
  
    usuari = usuari_inicial
    comptador = 0
    while usuari in usuaris_creats:
        comptador = comptador + 1
        usuari = usuari_inicial + str(comptador)

    usuaris_creats.append(usuari)
    print(f"{nom} {cognoms} ->  useradd -m -s /bin/bash {usuari}")
