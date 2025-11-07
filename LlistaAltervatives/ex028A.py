# Calcul de la lletra del NIF
# TRWAGMYFPDXBNJZSQVHLCKE
lletres = "TRWAGMYFPDXBNJZSQVHLCKE"
dni = int(input("Entra el DNI sense lletra -> "))
posicio = dni % 23

# if posicio == 0:
#     lletra = "T"
# elif posicio == 1:
#     lletra = "R"
# elif posicio == 2:
#     lletra = "W"
# * * *
lletra = lletres[posicio]

print(f"{dni}{lletra}")

