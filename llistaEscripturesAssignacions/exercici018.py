# Et donen un número de 3 dígits. Es tracta d'invertir-lo. Per exemple 345 -> 543
numero = int(input("Entra un numero de 3 dígits -> "))
# anirem treient el dígit de la unitat % 10 i quedant-nos amb la resta // 10
d1 = numero % 10
n1 = numero // 10
d2 = n1 % 10
n1 = n1 // 10
d3 = n1 % 10
invers = d1 * 100 + d2 * 10 + d3
print(numero, invers)
# dígit a dígit amb altres fòrmules
d1 = numero % 10
d3 = numero // 100
# El segon dígit, el del mig, el podem calcular de diverses maneres
d2 = numero // 10 % 10
invers = d1 * 100 + d2 * 10 + d3
print(numero, invers)
# El segon dígit, el del mig, el podem calcular de diverses maneres
d2 = numero % 100 // 10
invers = d1 * 100 + d2 * 10 + d3
print(numero, invers)
