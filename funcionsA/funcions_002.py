def suma(a, b, *c):
    resultat = a + b
    for valor in c:
        resultat = resultat + valor
    return(resultat)

c = suma(1, 2)
print(c)
print(suma(c, 8, 9))
print(suma(c, 8, 9, 10))
print(suma(c, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 4,3, 2, 4, 5, 65, 6, 4,3 ))