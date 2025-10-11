# Escriu un programa que donats els dos costats d'un triangle 
# rectangle en calculi la hipotenusa.
costat1 = float(input("Entra la mida del costat 1 del triangle -> "))
costat2 = float(input("Entra la mida del costat 2 del triangle -> "))
hipotenusa = (costat1 ** 2 + costat2 ** 2) ** 0.5
print("La hipotenusa és", hipotenusa)