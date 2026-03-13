# Exercici 3
# Simularem la lectura d'un fitxer de log. Cada línia és un string amb el format "DATA;IP_ORIGEN;IP_DESTI;PROTOCOL". 
logs = [
    "2030-07-01;192.168.1.5;10.0.0.1;HTTP",
    "2030-07-01;10.0.0.1;192.168.1.5;SSH",
    "2030-07-01;192.168.1.5;10.0.0.3;FTP",
    "2030-07-01;10.0.0.1;192.168.1.5;MYSQL",
    "2030-07-01;192.168.1.5;8.8.8.8;DNS",
    "2030-07-02;192.168.1.5;10.0.0.1;FTP",
    "2030-07-02;172.16.14.6;192.168.1.5;DNS",
    "2030-07-02;192.168.1.5;10.0.0.3;HTTP",
    "2030-07-02;172.16.14.6;192.168.1.5;SSH",
    "2030-07-02;192.168.1.5;8.8.8.8;MYSQL"
]
# Escriu un programa que:
#     Recorri la llista de logs i
#         Extregui la IP d'Origen de cada registre i la guardi en una llista nova.
llista = []
for l in logs:
    llista.append(l.split(";")[1])
print(llista)
#     Posteriorment, el programa demanarà una IP a l'usuari i dirà quantes vegades apareix aquesta IP com a origen en el log.
ip = input("Entra una IP -> ").strip()
vegades = 0
for adreca in llista:
    if adreca == ip:
        vegades += 1
if vegades > 0:
    print(f"La IP {ip} apareix {vegades} vegades a la llista")
else:
    print(f"La IP {ip} NO apareix a la llista")