# 6. Bloqueig per intents (Login):
# El programa ha de tenir un bucle while que demani una contrasenya.
# L'usuari té 3 intents per encertar-lo.
# Si falla els 3, el programa imprimeix "Compte bloquejat per seguretat".
# Posa el password a encertar en una variable, no cal demanar-lo.
MAX_INTENTS = 3
password = "123456"

for i in range(MAX_INTENTS):
    password_usuari = input("Entra el password -> ")
    if password_usuari == password:
        correcte = True
        break
else:
    correcte = False

if correcte:
    print("ok")
else:
    print("NO OK")