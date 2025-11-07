lletres = "TRWAGMYFPDXBNJZSQV"
dni = int(input("Entra el teu DNI -> "))
posicio = dni % 23

# if posicio == 0:
#     lletra = "T"
# elif posicio == 1:
#     lletra = "R"
# * * *

lletra = lletres[posicio]
print(f"{dni}{lletra}")