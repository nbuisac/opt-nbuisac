# Escriu un programa que donat un radi, calculi l'àrea d'un cercle.
PI = 3.14159265
radi = float(input("Entra el valor del radi -> "))
perimetre = 2 * PI * radi
print("El perímetre d'una circumferència de radi", radi, "és", perimetre)
area = PI * (radi ** 2)
print("Àrea =", area)