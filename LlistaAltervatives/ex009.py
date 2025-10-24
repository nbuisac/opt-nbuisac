# Fes un programa que demani ufn angle en graus (0-360) i ens indiqui a quin quadrant es troba.
# Controla que l'angle que s'introdueixi sigui vàlid.
# Suposarem [0,90) és el 1rQ, [90,180) és el 2nQ, [180,270) és el 3rQ i [270,360) és el 4tQ. Pots fer l'exercici per qualsevol valor positiu (si és major que 360 també funcioni).
angle_usuari = float(input("Entra un angle -> "))

angle = angle_usuari % 360
if angle < 0:
    angle = 360 + angle

if angle < 90:
    print(f"{angle_usuari} ({angle}) graus estan al primer quadrant")
elif angle < 180:    
    print(f"{angle_usuari} ({angle}) graus estan al segon quadrant")
elif angle < 270:
    print(f"{angle_usuari} ({angle}) graus estan al tercer quadrant")
else:
    print(f"{angle_usuari} ({angle}) graus estan al quart quadrant")

