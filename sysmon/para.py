import paramiko

# Configuració del servidor
hostname = "172.17.100.199"
username = "alumne"
password = "clau"  # Opcional si fas servir claus SSH

def comanda(quina):
    # 4. Executar la comanda 'ls'
    # stdin: entrada, stdout: sortida estàndard, stderr: errors
    stdin, stdout, stderr = client.exec_command(quina)
    
    # 5. Llegir la sortida
    resultat = stdout.read().decode('utf-8')
    errors = stderr.read().decode('utf-8')
    
    if resultat:
        print(f"Resultat de {quina}:")
        print(resultat)
    if errors:
        print(f"Errors trobats a {quina}:")
        print(errors)

try:
    # 1. Crear el client SSH
    client = paramiko.SSHClient()
    
    # 2. Afegir automàticament la clau del servidor (per evitar l'error de 'host key')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # 3. Connectar-se
    print(f"Connectant a {hostname}...")
    client.connect(hostname, username=username, password=password)
    
    comanda("ls -l")
    comanda("pwd")
finally:
    # 6. Tancar la connexió sempre
    client.close()
    print("Connexió tancada.")

## Per connexió per clau pública/clau privada
# import paramiko
# import os

# hostname = "la_teva_ip"
# username = "el_teu_usuari"
# # Ruta a la teva clau privada (sol ser id_rsa, id_ed25519, etc.)
# path_to_key = os.path.expanduser('~/.ssh/id_rsa') 

# try:
#     # 1. Carregar la clau privada
#     # Si la clau té contrasenya (passphrase), afegeix l'argument password='la_teva_passphrase'
#     key = paramiko.RSAKey.from_private_key_file(path_to_key)
#     key = paramiko.Ed25519Key.from_private_key_file(path_to_key)