ips_reservades = ["192.168.1.1", "192.168.1.10", "192.168.1.50"]
def menu():
    print("1. Afegir una nova IP")
    print("2. Mostrar totes les IP")
    print("\n0. Sortir")
    opcio = input("\nEscull una opció -> ")
    return opcio
#Afegir una nova IP (però s'ha de comprovar que no existeixi prèviament a la llista). 
#En cas que la IP que volem afegir ja existeixi el programa ens ho comunicarà i no l'afegirà.
q=menu()
while q != "0":
    if q == "1":
        Escriu_ip=input("Posa IP que vols afegir->")
        trobat = False
        for i in ips_reservades:
            if i == Escriu_ip:
                trobat = True
                print(f"Ip que vols afegir ja existeix ->{Escriu_ip}")
                break
        if not trobat:
            ips_reservades.append(Escriu_ip)
    elif q == "2":
        print(f"Totes les IP que tenim->{ips_reservades}")
    q=menu()
print(f"Totes les IP que tenim->{ips_reservades}")

#Visualitzar totes les IP que tenim. El programa mostrarà les IP que tenim emmagatzemades.