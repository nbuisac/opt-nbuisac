# Exercici 4
# Tenim una llista on es guarda el trànsit de xarxa en MB rebut cada hora durant un dia (24 valors):
# trafic = [50, 45, 30, 20, 10, 5, 5, 15, 80, 120, 200, 150, 140, 130, 110, 100, 90, 150, 210, 180, 100, 80, 60, 40]
# Escriu un programa que:

trafic = [50, 45, 30, 20, 10, 5, 5, 15, 80, 120, 200, 150, 140, 130, 110, 100, 90, 150, 210, 180, 100, 80, 60, 40]
#     Detecti i mostri en quines hores (índex de la llista) el trànsit ha superat els 150 MB.
MAXIM = 150
hores = []
for i in range(len(trafic)):
    if trafic[i] > MAXIM:
        hores.append(i)
print(f"Hores en què s'ha superat els {MAXIM}MB -> {hores}")
#     Calculi i mostri el total de dades transferides en tot el dia.
print(f"Total de dades transferides -> {sum(trafic)}")
#     Trobi i mostri el "pic de pujada" més gran entre dues hores consecutives (ex: de l'hora 7 a la 8 hi ha una pujada de 65 MB).
maxima_diferencia = 0
hora_inferior = -1
for i in range(len(trafic) - 1):
    if trafic[i + 1] - trafic[i] > maxima_diferencia:
        maxima_diferencia = trafic[i + 1] - trafic[i]
        hora_inferior = i
print(f"de l'hora {hora_inferior} a la {hora_inferior + 1} hi ha una pujada de {maxima_diferencia} MB")