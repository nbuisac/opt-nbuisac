# Exercici 2
# Tenim una llista de contrasenyes que s'han de validar per a un grup d'usuaris:
# passwords = ["12345", "Admin2024!", "sol", "Password_Segur_99", "qwerty"]
# Crea un programa que classifiqui aquestes contrasenyes en una nova llista anomenada segures només si compleixen tots aquests requisits:
#     Tenir una longitud superior a 8 caràcters.
#     Contenir, almenys, un caràcter especial (comprova si conté algun d'aquests: !, @, #, $).
passwords = ["12345", "Admin2024!", "sol", "Password_Segur_99", "qwerty"]
segures = []
for p in passwords:
    if len(p) > 8:
        # if "!" in p or "@" in p or "#" in p or "$" in p:
        #     segures.append(p)
        ok = False
        for c in "!@#$":
            if c in p:
                ok = True
                break
        if ok:
            segures.append(p)
#     Al final, el programa ha de mostrar la llista de contrasenyes segures i el percentatge de seguretat de la mostra (ex: "El 40% de les contrasenyes són segures").
print(segures)
print(f"El {len(segures) / len(passwords):.0%} de les contrasenyes són segures")