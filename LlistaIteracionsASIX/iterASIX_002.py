## Comprovació de ports: Donada una llista de ports comuns (80, 443, 22, 3306, 8080), i una altra amb el nom dels serveis, cal recórrer una de les llistes i "simular" una connexió. De forma aleatòria determinarem si el port és OBERT o TANCAT i mostrarem un missatge com ara "Servei nom_del_servei OBERT" o bé "Servei nom_del_servei TANCAT", 
import random

PORTS = [20, 21, 22, 23, 25, 67, 68, 69, 80, 110, 443, 3306, 8000, 8080, 8888]
SERVEIS = ["FTP-DATA", "FTP", "SSH", "TELNET", "smtp", "dhcpS", "dhcpC", "TFTP", "HTTP", "POP3", "HTTPS", "mySQL", "HTTP", "HTTP", "HTTP"]

for i, port in enumerate(PORTS):
    # port = PORTS[i]
    servei = SERVEIS[i]
    if random.randint(1, 10) <= 2:
        estat = "TANCAT"
    else:
        estat = "OBERT"
    print(f"Servei {servei}:{port} {estat}")