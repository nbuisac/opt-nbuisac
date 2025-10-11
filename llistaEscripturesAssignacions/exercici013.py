# Escriu un programa que et permeti calcular l'àrea d'un rectangle i el seu perímetre.
costat1 = float(input("Entra la mida del costat 1 del triangle -> "))
costat2 = float(input("Entra la mida del costat 2 del triangle -> "))
costat3 = float(input("Entra la mida del costat 3 del triangle -> "))
semiperimetre = (costat1 + costat2 + costat3 ) / 2
area = (semiperimetre * (semiperimetre - costat1) * (semiperimetre - costat2) * (semiperimetre - costat3)) ** 0.5
print("L'àrea d'un triangle de costats", costat1, "," , costat2, "i", costat3, "és", area)

