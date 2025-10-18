# Fes un programa que demani una lletra i digui si és majúscula, minúscula o no és lletra.
lletra = input("Entra una lletra -> ")
# OPCIÓ 1. versió de baix nivell, no té en compte acents, dièresis, ç, ñ
if lletra >= 'A' and lletra <= 'Z':
    print("OPCIO 1 -> És una MAJÚSCULA")
elif lletra >= 'a' and lletra <= 'z':
    print("OPCIO 1 -> És una minúscula")
else:
    print("OPCIO 1 -> No és lletra")
# OPCIÓ 2. definim les lletres que identifiquem com majúscules i minúscules
MAJUSCULES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÇÑÀÈÌÒÙÁÉÍÓÚÂÊÎÔÛÄËÏÖÜ'
MINUSCULES = 'abcdefghijklmnopqrstuvwxyzçñàèìòùáéíóúâêîôûäëïöü'
if lletra in MAJUSCULES:
    print("OPCIO 2 -> És una MAJÚSCULA")
elif lletra in MINUSCULES:
    print("OPCIO 2 -> És una minúscula")
else:
    print("OPCIO 2 -> No és lletra")
# OPCIÓ 3. utilitzem funcions de Python
if lletra.isupper():
    print("OPCIO 3 -> És una MAJÚSCULA")
elif lletra.islower():
    print("OPCIO 3 -> És una minúscula")
else:
    print("OPCIO 3 -> No és lletra")
