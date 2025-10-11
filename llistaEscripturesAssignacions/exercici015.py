# La nota final es calcula amb la nota de tres examens. N'hem fet dos.
# Escriu un programa que em pregunti les dues primeres notes per teclat i
# em determini quina nota haig de treure per arribar a 5 en la mitjana de tres exàmens.
nota1 = float(input("Entra la nota del primer examen -> "))
nota2 = float(input("Entra la nota del segon examen -> "))
aprovat = 15 - nota1 - nota2
if aprovat > 10:
    print("Impossible aprovar, necessites un", aprovat)
elif aprovat <= 0:
    print("Ja estàs aprovat i encara et sobren", -aprovat, "punts")
else:
    print("Cal que treguis, com a mínim, un", aprovat)