def validaIPv4(ipStr):
    ipStrList = ipStr.split(".")
    print(ipStr, ipStrList)
    if len(ipStrList) == 4:
        for element in ipStrList:
            if not (0 <= int(element) <= 255):
                valida = False
                break
        else:
            valida = True
    else:
        valida = False
    return valida


ip = input("Entra una IP i la validaré -> ")

if validaIPv4(ip):
    print(f"La IP {ip} és vàlida")
else:
    print(f"La IP {ip} NO és vàlida")