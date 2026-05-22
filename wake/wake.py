import socket
import struct

def send_wol(mac_address):
    """
    Envia un paquet 'Magic Packet' a una adreça MAC específica per engegar un PC.
    """
    # 1. Netegem l'adreça MAC (traiem colons o guions)
    clean_mac = mac_address.replace(':', '').replace('-', '')
    
    if len(clean_mac) != 12:
        raise ValueError("L'adreça MAC no és vàlida.")

    # 2. Creem el 'Magic Packet'
    # El paquet consisteix en 6 bytes de 'FF' seguits de la MAC repetida 16 vegades.
    hex_mac = bytes.fromhex(clean_mac)
    magic_packet = b'\xff' * 6 + hex_mac * 16

    # 3. Enviem el paquet via UDP broadcast
    # Utilitzem l'adreça 255.255.255.255 per arribar a tota la xarxa local.
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # El port estàndard per a WoL sol ser el 7 o el 9
        s.sendto(magic_packet, ('255.255.255.255', 9))
        
    print(f"Paquet enviat amb èxit a la MAC: {mac_address}")

# --- CONFIGURACIÓ ---
# Posa aquí l'adreça MAC del PC que vols despertar
EL_MEU_PC_MAC = '38:14:28:67:63:87'

if __name__ == "__main__":
    send_wol(EL_MEU_PC_MAC)