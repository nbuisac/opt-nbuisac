nota1 = float(input("Entra la primera nota -> "))
nota2 = float(input("Entra la segona  nota -> "))
if nota1 < 3.5 or nota2 < 3.5:
    if nota1 < nota2:
        mitjana = nota1
    else:
        mitjana = nota2
else:
    mitjana = (nota1 + nota2) / 2
mitjana = round(mitjana)
print(f"La nota final entre {nota1} i {nota2} és {mitjana}")