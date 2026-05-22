import csv
print("Entra les dades següents")
hostname = input("Entra el nom del host -> ").strip().upper().replace(" ", "_")
ip = input("Entra la IP del host -> ")
port = input("Entra elport per escoltar -> ")

nom_fitxer = f"config_{hostname}.txt"
with open(nom_fitxer, "w") as f:
    f.writelines(f"[SERVER_CONFIG]\n"
                 f'HOST_NAME = "{hostname}"\n'
                 f'IP_ADDRES = {ip}\n'
                 f'PORT = {port}\n'
                 f'STATUS = "active"'
    )
nom_fitxer = f"config_{hostname}.csv"
with open(nom_fitxer, "w", ) as f:
    escriptor = csv.writer(f)
    escriptor.writerow([hostname, ip, port])