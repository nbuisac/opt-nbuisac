# Fes un programa que demani una lletra i digui si és o no una vocal.
lletra = input("Entra una lletra -> ")
# OPCIÓ 1. versió de baix nivell, no té en compte acents, dièresis, ç, ñ
if lletra == 'A' or lletra == 'E' or lletra == "I" or lletra == 'O' or lletra == "U" or \
   lletra == 'a' or lletra == 'e' or lletra == "i" or lletra == 'o' or lletra == "u":
    print("OPCIO 1 -> És una VOCAL")
else:
    print("OPCIO 1 -> No és vocal")
# OPCIÓ 2. definim les lletres que identifiquem com vocals
VOCALS = 'AEIOUÀÈÌÒÙÁÉÍÓÚÂÊÎÔÛÄËÏÖÜaeiouñàèìòùáéíóúâêîôûäëïöü'
if lletra in VOCALS:
    print("OPCIO 2 -> És una VOCAL")
else:
    print("OPCIO 2 -> No és vocal")
