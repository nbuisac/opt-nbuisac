diamesany = int(input("Entra una data (DDMMAAAA) -> "))

any = diamesany % 10000
dia = diamesany // 1000000
mes = diamesany % 1000000 // 10000
mes = diamesany // 10000 % 100

print(f"{dia:02}/{mes:02}/{any:04}")

data_correcte = True
if mes < 1 or mes > 12:
    data_correcte = False
else:
    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or \
        mes == 8 or mes == 10 or mes == 12) and dia > 31:
        data_correcte = False