import argparse
import psutil
import time
# L'script no pot tenir valors fixats dins el codi (hardcoded). Ha d'acceptar els següents arguments des de la terminal:
#     --ram-limit: Llindar d'ús de la RAM en percentatge (per defecte: 80).
#     --disk-limit: Llindar d'ús del disc principal en percentatge (per defecte: 85).
#     --webhook: URL opcional on enviar l'alerta. Si no s'indica, només guardarà l'alerta al fitxer de log.
parser = argparse.ArgumentParser(
                    prog='py sysmon.py',
                    description='Monitorització del Sistema',
                    epilog='Monitoritzem la RAM i el Disk i ho enviem a un servidor extern')

parser.add_argument('--ram-limit', type=float, default=80, help="indica el valor d'ocupació de RAM per mostrar l'avís (defecte %(default).2f%%)")
parser.add_argument('--disk-limit', type=float, default=85, help="indica el valor d'ocupació de Disc per mostrar l'avís (defecte %(default)s%%)")
parser.add_argument('--webhook', type=str)

args = parser.parse_args()
## Recollim els valors i els guardem en variables
ram_limit = args.ram_limit
disk_limit = args.disk_limit
webhook = args.webhook

while True:
    memoria = psutil.virtual_memory()
    if memoria.percent >= ram_limit:
        print("MEMORIA\n=======\n"
            f"\tTotal: {memoria.total/1000000000:.2f} GB\n"
            f"\tDisponible: {memoria.available/1000000000:.2f} GB\n"
            f"\t% usada: {memoria.percent:.2f} %")

    ## Comprovem el disk
    particions = psutil.disk_partitions()
    for particio in particions:
        disc = psutil.disk_usage(particio.mountpoint)
        if disc.percent >= disk_limit:
            print(f"DISC ({particio.mountpoint})\n{"=" * len(f'DISC ({particio.mountpoint})')}\n" 
                  f"\tTotal: {disc.total/1000000000:.2f} GB\n"
                  f"\tDisponible: {disc.free/1000000000:.2f} GB\n"
                  f"\t% usada: {disc.percent:.2f} %")
            
    

    break