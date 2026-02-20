def suma(a, b, *resta):
    print(resta)
    resultat = a + b 
    for valor in resta:
        resultat = resultat + valor
    return resultat

# for a in range(10):
#     print(suma(1, a))

print(suma(1, 2))
print(suma(1, 2, 3))
print(suma(1, 2, 3, 4))
print(suma(1, 2, 3, 4, 5))
print(suma(1, 2, 3, 4, 5, 6))