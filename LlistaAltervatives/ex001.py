# Fes un programa que calculi la solució de l'equació de primer grau ax + b = 0 on x = -b / a. Ha de controlar quan la a és zero.
a = float(input("Entra al valor de la a -> "))
if a != 0:
    b = float(input("Entra el valor de la b -> "))
    x = -b / a
    print("x val ", x)
else:
    print("a no pot valer 0")