# equacio de 2n grau
a = float(input("Entra el valor per la a -> "))
if a == 0:
    print("No es una equació de 2n grau")
else:
    b = float(input("Entra el valor per la b -> "))
    c = float(input("Entra el valor per la c -> "))
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        print("No hi ha solució")
    elif discriminant == 0:
        x = -b / (2 * a)
        print("x = ", x)
    else:
        x1 = (-b + discriminant ** 0.5) /  (2 * a)
        print("x1 = ", x1)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        print("x2 = ", x2)
print("FI")