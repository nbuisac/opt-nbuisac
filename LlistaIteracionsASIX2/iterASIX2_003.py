# Filtrem IPs d'una xarxa.
# Tenim una llista d'adreces IP i volem trobar només les
# de la xarxa 192.168.1.x.
# Creem la llista
ips = ["192.168.1.10", "10.0.0.5", "192.168.12.25", "172.16.0.1", 
    "192.168.1.100", "8.8.8.8", "192.168.2.5"]
xarxa = input("De quina xarxa? -> ")
if xarxa[-1] != '.':
    xarxa = xarxa + "."
for e in ips:
    if e[:len(xarxa)] == xarxa:
        print(e)