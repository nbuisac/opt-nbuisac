def validaIP(ipStr):
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