import threading
from time import sleep

texte = "Hola"

def escriu(inici = 1, fi = 1000, pas = 1):
    global texte
    for i in range(inici, fi + 1, pas):
        print(i, end = " ")
        sleep(0.002)
    texte = "Final"

def escriu_mf(inici = 1, fi = 1000, pas = 1):
    escriu(inici, fi, pas)

x = threading.Thread(target = escriu_mf, name="Fil1", args = (10, 1000, 2))
x.start()
escriu(1000, 1300, 5)
x.join()
print("OOOOOOOOOOOOOOOOOOOOOOOHHHHHHHHHHHHHHHHHHHHHHH")
