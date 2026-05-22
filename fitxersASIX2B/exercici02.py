import csv
print("Entra les dades que et demanem:")

nom_servidor = input("Nom del servidor: ").strip().replace(" ", "_").upper()
ip = input("IP del servidor: ")
port = input("Port per escoltar: ")

nom_fitxer = f"config{nom_servidor}.txt" 

with open(nom_fitxer, "wt",encoding="utf-8") as f:
    f.writelines(f"[SERVER_CONFIG]\n"
                 f'HOST_NAME = "{nom_servidor}"\n'
                 f'IP_ADDRESS = "{ip}"\n'
                 f'PORT = {port}\n'
                  'estat = "active"'
                )
with open(nom_fitxer+".csv", "wt",encoding="utf-8") as f:
    escriptor = csv.writer(f)
    escriptor.writerow([nom_servidor, ip, port])

