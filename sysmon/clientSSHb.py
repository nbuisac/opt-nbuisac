import argparse
import paramiko

def main():
    ## Comprovarem els paràmetres
    # --host
    # -u --username
    # -p --password
    # -c command1 -c command2 -c command3 -c command4
    parser = argparse.ArgumentParser(
                        prog='py clientSSH.py',
                        description='Execució de comandes per SSH',
                        epilog='Execució de comandes per ssh a un servidor')

    parser.add_argument('--host', type=str, default="172.17.100.199",
                        help="Servidor on ens volem connectar")
    parser.add_argument('-u', '--username', type=str, default="alumne",
                        help="usuari de connexió")
    parser.add_argument('-p', '--password', type=str, default="clau",
                        help="clau de connexió")
    parser.add_argument('-c', '--command', default=["w"], nargs='+', type=str,
                        help="comanda que volem executar")

    # parser.add_argument('-c', '--command', default=["w"], action= 'append', type=str,
    #                     help="comanda que volem executar")

    args = parser.parse_args()
    print(args)
    host = args.host
    username = args.username
    password = args.password
    comandes = args.command ## Això és una llista de comandes

    ## Connexió
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host,username=username, password=password) 

    ## Execució de comandes
    if len(comandes) > 1:
        comandes = comandes[1:]
    for comanda in comandes:
        print(f"Comanda {comanda}")
        print("=" * len(f"Comanda {comanda}"))
        stdin, stdout, stderr = client.exec_command(comanda)
        print(stdout.read().decode("utf-8"))
        

    ## Finalització de connexió
    client.close()

if __name__ == '__main__':
    main()