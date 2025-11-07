# Fes un programa que ens digui en quin ordre s'han introduït dos nombres pel teclat (creixent, decreixent o bé són iguals)
numero1 = float(input("Entra el primer número -> "))
numero2 = float(input("Entra el segon número  -> "))
if numero1 < numero2:
    print("has introduït els números en ordre creixent")
elif numero1 > numero2:
    print("has introduït els números en ordre decreixent")
else:
    print("els dos números són iguals")
