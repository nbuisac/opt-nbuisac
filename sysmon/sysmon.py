import argparse
import psutil
import logging
import requests
import time

def main():
    GIGA = 1000000000
    # L'script no pot tenir valors fixats dins el codi (hardcoded). Ha d'acceptar els següents arguments des de la terminal:
    #     --ram-limit: Llindar d'ús de la RAM en percentatge (per defecte: 80).
    #     --disk-limit: Llindar d'ús del disc principal en percentatge (per defecte: 85).
    #     --webhook: URL opcional on enviar l'alerta. Si no s'indica, només guardarà l'alerta al fitxer de log.
    parser = argparse.ArgumentParser(
                        prog='py sysmon.py',
                        description='Monitorització del Sistema',
                        epilog='Monitoritzem la RAM i el Disk i ho enviem a un servidor extern')

    parser.add_argument('--ram-limit', type=float, default=80, 
                        help="indica el valor d'ocupació de RAM per mostrar l'avís (defecte %(default).2f%%)")
    parser.add_argument('--disk-limit', type=float, default=85,
                        help="indica el valor d'ocupació de Disc per mostrar l'avís (defecte %(default)s%%)")
    parser.add_argument('--webhook', type=str)

    args = parser.parse_args()
    ## Recollim els valors i els guardem en variables
    ram_limit = args.ram_limit
    disk_limit = args.disk_limit
    webhook = args.webhook

    logging.basicConfig(
        filename="log.log",
        encoding="utf8",
        format='%(asctime)s#%(name)s#%(levelname)s#%(message)s',
        level=logging.INFO
    )

    while True:
        alertes = []
        memoria = psutil.virtual_memory()
        if memoria.percent >= ram_limit:
            missatge = ("MEMORIA#"
                f"Total: {memoria.total/GIGA:.2f} GB#"
                f"Disponible: {memoria.available/GIGA:.2f} GB#"
                f"% utilitzat: {memoria.percent:.2f} %"
            )
            logging.warning(missatge)
            alertes.append(missatge)

        particions = psutil.disk_partitions()
        for particio in particions:
            disc = psutil.disk_usage(particio.mountpoint)
            if disc.percent >= disk_limit:
                missatge = (f"DISC ({particio.mountpoint})#" 
                    f"Total: {disc.total/GIGA:.2f} GB#"
                    f"Disponible: {disc.free/GIGA:.2f} GB#"
                    f"% utilitzat: {disc.percent:.2f} %"
                )
                logging.warning(missatge)
                alertes.append(missatge)

        if webhook:
            dades = "*** N A R C I S ***\n" + "\n".join(alertes)
            dades = {"content": dades}
            ## Enviem els missatges
            resposta = requests.post(webhook, json=dades)
            if resposta.status_code == 200:
                logging.info(f"Dades enviades al servidor {webhook}")
            else:
                logging.warning(f"Error en connectar amb el servidor {webhook}")
        time.sleep(1)

if __name__ == "__main__":
    main()