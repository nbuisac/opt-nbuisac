def valida_mask_v4(mask):
    valida = False
    mask_list = mask.split(".")
    mask_bin = ""
    mask_int = 0
    for e in mask_list:
        mask_bin += f"{int(e):08b}"
        mask_int = mask_int * 256 + int(e)
    print("*", mask_bin)
    print("#", mask_int, f"\n# {mask_int:032b}")
    if len(mask_bin) ==  (8 * 4):
        i = 0
        while i < len(mask_bin) and mask_bin[i] == "1":
            i = i + 1
        while i < len(mask_bin) and mask_bin[i] == "0":
            i = i + 1
        valida = (i == 32)
    else:
        valida = False
    return valida

def valida_ip_v4(ip):
    llistaIP = ip.split(".")
    if len(llistaIP) == 4:
        for element in llistaIP:
            if not 0<= int(element) <= 255:
                validaIP = False
                break
        else:
            validaIP = True
    else:
        validaIP = False
    return validaIP

print(valida_mask_v4("255.0.0.0"))
print(valida_mask_v4("0.0.0.0"))
print(valida_mask_v4("254.0.0.0"))
print(valida_mask_v4("255.253.0.0"))
print(valida_mask_v4("255.253.1.0"))
print(valida_mask_v4("255.253.0.1"))
print(valida_mask_v4("255.255.255.255"))