## Monitoratge amb while: Crea un bucle que simuli fer
# "ping" a un servidor cada 5 segons.
# El bucle només s'aturarà si el servidor "cau" (utilitzarem una probabilitat aleatòria amb el mòdul random).
# Demana la IP a l'usuari.
import random
import time

ip = input("Entra la IP on vols fer ping -> ")
print(f"Fent ping a {ip}")
probabilitat = random.randint(1, 10)
while probabilitat > 2:
    print(f"Resposta de {ip}")
    time.sleep(0.5)
    probabilitat = random.randint(1, 10)