import argparse
import psutil
# L'script no pot tenir valors fixats dins el codi (hardcoded). Ha d'acceptar els següents arguments des de la terminal:
#     --ram-limit: Llindar d'ús de la RAM en percentatge (per defecte: 80).
#     --disk-limit: Llindar d'ús del disc principal en percentatge (per defecte: 85).
#     --webhook: URL opcional on enviar l'alerta. Si no s'indica, només guardarà l'alerta al fitxer de log.
parser = argparse.ArgumentParser(
                    prog='py sysmon.py',
                    description='Monitorització del Sistema',
                    epilog='Monitoritzem la RAM i el Disk i ho enviem a un servidor extern')

parser.add_argument('--ram-limit', type=float, default=80, help="indica el valor d'ocupació de RAM per mostrar l'avís")
parser.add_argument('--disk-limit', type=float, default=85, help="indica el valor d'ocupació de Disc per mostrar l'avís")
parser.add_argument('--webhook', required=False)

args = parser.parse_args()
## Recollim els valors i els guardem en variables
ram_limit = args.ram_limit
disk_limit = args.disk_limit
webhook = args.webhook
print(ram_limit, disk_limit, webhook)

## Comprovem el SO
import os
if os.name == 'nt':
    particio = "C:\\"
else:
    particio = '/'

# Dades de la memoria
memoria = psutil.virtual_memory()
print("MEMÒRIA\n=======",
      f"\n{"Total:":<13} {memoria.total / 1000000000:.2f} GBytes",
      f"\n{"Disponible:":<13} {memoria.available / 1000000000:.2f} GBytes",
      f"\n{"% ocupat:":<13} {memoria.percent} %")

# Dades del disc
disc = psutil.disk_usage(particio)
print("DISC\n====",
      f"\n{"Total:":<13} {disc.total / 1000000000:.2f} GBytes",
      f"\n{"Disponible:":<13} {disc.free / 1000000000:.2f} GBytes",
      f"\n{"% ocupat:":<13} {disc.percent} %")
