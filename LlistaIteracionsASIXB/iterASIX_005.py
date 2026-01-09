# Validador de robustesa de contrasenyes:
# L'usuari introdueix una contrasenya i el programa la 
# recorre caràcter a caràcter per comprovar si té almenys 
# una majúscula, un número i un símbol.
# Al final ens ha de dir si compleix o no aquest requeriment.

password = input("Entra una contrasenya -> ")

hi_ha_majuscula = False
hi_ha_digit = False
hi_ha_simbol = False

for lletra in password:
    if lletra.isupper():
        hi_ha_majuscula = True
    elif lletra.isdigit():
        hi_ha_digit = True
    elif not lletra.isalpha():
        hi_ha_simbol = True

if hi_ha_simbol and hi_ha_digit and hi_ha_majuscula:
    print("OK")
else:
    print("KO")