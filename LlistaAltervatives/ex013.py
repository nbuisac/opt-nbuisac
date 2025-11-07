# Fes un programa que passi una lletra a majúscules.
# Si no és minúscula no ha de fer res.
lletra = input("Entra una lletra -> ")
majuscula = lletra
# OPCIÓ 1. versió de baix nivell, no té en compte acents, dièresis, ç, ñ
if lletra >= 'a' and lletra <= 'z':
    majuscula = chr(ord('A') + (ord(lletra) - ord('a')))
print(f"OPCIO 1 -> {lletra} -> {majuscula}")
# OPCIÓ 3. utilitzem funcions de Python. COMPTE α, ß ho troba com a lletra, i altres també.
majuscula = lletra.upper()
print(f"OPCIO 2 -> {lletra} -> {majuscula}")
