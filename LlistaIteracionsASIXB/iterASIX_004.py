# 4. Generador de noms d'usuari: Donada una llista amb noms i cognoms reals (ex: ["Pere Pi", "Marta Mas"]),
# utilitza un bucle per generar noms d'usuari en format lowercase i
# sense espais (ex: ppi, mmas o pere.pi, marta.mas).

import unicodedata

usuaris_nous = [
    ("Jordi", "Puigvert i Casals"),
    ("Montserrat", "Vila i Rovira"),
    ("Montserrat", "Vila i Rovira"),
    ("Arnau", "Serra i Martí"),
    ("Aina", "Serra i Bosc"),
    ("Montserrat", "Vila i Rovira"),
    ("Aitana", "Serra i Mas"),
    ("Laia", "Font i Capdevila"),
    ("Oriol", "Soler i Gual"),
    ("Marc", "Prats"),
    ("Aitana", "Serra i Mas"),
    ("Meritxell", "Riba i Bosch"),
    ("Marc", "Prats"),
    ("Marc", "Prats"),
    ("Eulàlia", "Ventura i Grau"),
    ("Pol", "Sabaté i Solé"),
    ("Aina", "Garriga i Cañellas"),
]
usuaris_creats = []
for nom, cognoms in usuaris_nous:
    nom = unicodedata.normalize('NFKD', nom).encode('ascii', 'ignore').decode('ascii').strip()
    cognoms = unicodedata.normalize('NFKD', cognoms).encode('ascii', 'ignore').decode('ascii').strip()
    primeraPart = nom[0]
    segonaPart = cognoms.split()[0]
    # if " " in cognoms:
    #     segonaPart = cognoms[0:cognoms.find(" ")]
    # else:
    #     segonaPart = cognoms
    
    original = (primeraPart + segonaPart).lower()
    usuari = original
    comptador = 0
    while usuari in usuaris_creats:
        comptador = comptador + 1
        usuari = original  + str(comptador)
     
    
    usuaris_creats.append(usuari)
    print(nom, cognoms, "->", usuari, f" -> useradd -m -s /bin/bash {usuari}")

print(usuaris_creats)