from turtle import *
def dibuixa_regular(costats, tamany = 100):
    angle = 180 - (180 * costats - 360) / costats
    for _ in range(costats):
       forward(tamany)
       left(angle)

n = int(input("Entra el nombre de costats -> "))
dibuixa_regular(n, 100)

goto(-100,-300)
clear()
colors = [ 'blue', 'orange', 'green', 'red', 'pink' ]
speed(0)
for i, a in enumerate(range(30, 2, -1)):
    color(colors[i % len(colors)] )
    begin_fill()
    dibuixa_regular(a, 60)
    end_fill()
