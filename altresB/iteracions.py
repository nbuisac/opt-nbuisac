import time
llista = [34, 12,56,3,56,3,67,234,56,34]
print(llista)
busca = int(input("Quin numero vols buscar ->"))
inici = time.perf_counter()
# for n in llista:
#     if n == busca:
#         trobat = True
#         break
# else:
#     trobat = False
trobat =  busca in llista
final = time.perf_counter()
print(final - inici)
if trobat:
    print(f"{busca} està dins de {llista}")
else:
    print(f"{busca} no està dins de {llista}")