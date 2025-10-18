# Fes un programa que demani un caràcter i digui si és o no lletra.
lletra = input("Entra una lletra -> ")
# OPCIÓ 1. versió de baix nivell, no té en compte acents, dièresis, ç, ñ
if lletra >= 'A' and lletra <= 'Z' or lletra >= 'a' and lletra <= 'z':
    print("OPCIO 1 -> És una LLETRA")
else:
    print("OPCIO 1 -> No és lletra")
# OPCIÓ 2. definim els caràcters que identifiquem com a lletres. COMPTE amb la cadena buida.
LLETRES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÇÑÀÈÌÒÙÁÉÍÓÚÂÊÎÔÛÄËÏÖÜabcdefghijklmnopqrstuvwxyzçñàèìòùáéíóúâêîôûäëïöü'
if lletra in LLETRES:
    print("OPCIO 2 -> És una LLETRA")
else:
    print("OPCIO 2 -> No és lletra")
# OPCIÓ 3. utilitzem funcions de Python. COMPTE α, ß ho troba com a lletra, i altres també.
if lletra.isalpha():
    print("OPCIO 3 -> És una LLETRA")
else:
    print("OPCIO 3 -> No és lletra")