nota = float(input("Entra una nota (0..10)-> "))
intents = 1
while nota < 0 or nota > 10:
    if intents >= 3:
        correcte = False
        break
    nota = float(input("ERROR: Entra una nota (0..10)-> "))
    intents = intents + 1
else:
    correcte = True
if correcte:
    print("La nota correcta és", nota)
else:
    print("Nota molt mal entrada")
