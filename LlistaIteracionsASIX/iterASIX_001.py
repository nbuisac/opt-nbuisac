## Escaneig de subxarxa (Simulat): Demanem a l'usuari que introdueixi els tres primers octets d'una xarxa (ex: 192.168.1).
## El programa generarà i imprimirà totes les adreces IP possibles de la .1 a la .254.
ip3 = input("Entra els tres primers bytes de la IP (xxx.yyy.zzz) ->")
if ip3[-1] == ".":
    ip3 = ip3[:-1]
for i in range(1, 255):
    print(f"{ip3}.{i}")