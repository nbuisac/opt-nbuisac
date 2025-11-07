dia_mes_any = int(input("Entra la data DDMMAAAA -> "))

any = dia_mes_any % 10000
dia = dia_mes_any // 1000000
mes = dia_mes_any // 10000 % 100

data_correcte = True
if mes < 1 or mes > 12:
    data_correcte = False
else:
    if dia < 1:
        data_correcte = False
    elif dia > 31 and \
       (mes == 1 or mes == 3 or mes == 5 or mes == 7 or \
        mes == 8 or mes == 10 or mes == 12):
       data_correcte = False
    elif dia > 30 and \
        (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        data_correcte = False
    elif mes == 2:
        if (any % 400 == 0 or (any % 4 == 0 and any % 100 != 0)):
            if dia > 29:
                data_correcte = False
        elif dia > 28:
            data_correcte = False

print(f"{dia}/{mes}/{any}")
if data_correcte:
    print("Ok")
else:
    print("KO")