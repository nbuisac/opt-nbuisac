CODI_A_TROBAR = "404"
nom_fitxer = "altresB/fitxer.log"
comptador = 0
## Cal anar a buscar la info al fitxer.log
## for l in LINIES_A_ANALITZAR:
f = open(nom_fitxer)
linia = f.readline()
while linia != "":
    ## Tracto les dades
    if linia.split(" ")[8] == CODI_A_TROBAR:
        comptador = comptador + 1
        print(linia, end="")
    ## llegeixo la següent
    linia = f.readline()
f.close()
print(f"Hem trobat {comptador} linies amb codi {CODI_A_TROBAR}")