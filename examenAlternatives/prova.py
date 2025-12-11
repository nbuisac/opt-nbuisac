nota1 = float(input("Introdueix la primera nota: "))
nota2 = float(input("Introdueix la segona nota: "))

if nota1 < 3.5 or nota2 < 3.5:
    nota_final = nota1 if nota1 < nota2 else nota2
else:
    nota_final = (nota1 + nota2) / 2

nota_final = int(nota_final)
print("La nota final és:", nota_final)

