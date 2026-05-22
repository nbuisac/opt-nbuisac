import paramiko
import argparse

## Recuperem paràmetres
# --host host de connexió
# --username -u Usuari de connexió
# --password -p clau de connexió
# -c comanda a executar (pot posar-se vàries vegades)
parser = argparse.ArgumentParser(prog="py clientSSH.py",description="Connexió i execució de comandes per SSH",
                                 epilog="""
                                Per met connectar-nos per SSH a un host i executar comandes
                                 """)
parser.add_argument('--host',type=str, default="172.17.100.199",
                    help="IP del host a conectar")
parser.add_argument("-u", "--username", type=str, default="alumne", help="Usuari per la connexió")
parser.add_argument("-p", "--password", type=str, default="clau", help="Password de l'usuari per la connexió")
parser.add_argument("-c", type=str, default=["ls -l"], nargs='+')

args = parser.parse_args()
print(args)
hostname = args.host
username = args.username
password = args.password
commands = args.c

## Connectem
client = paramiko.SSHClient()
client.load_system_host_keys()
client.connect(hostname, username=username, password=password)

## Executem les comandes
# if len(commands) > 1:
#     commands = commands[1:]
for command in commands:
    print(f"Comanda {command}")
    print("=" * len(f"Comanda {command}"))
    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read().decode("utf-8"))

## Desconnectem
client.close()
