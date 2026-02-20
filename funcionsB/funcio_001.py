def escriu_titol(missatge, subr="=", sobr=None, end="\n", upper=False):
    if upper == True:
        missatge = missatge.upper()
    if sobr == True:
        print(str(subr) * len(missatge), end=end)
    elif sobr != None:
        print(str(sobr) * len(missatge), end=end)

    print(missatge, end=end)
    print(str(subr) * len(missatge), end=end)


titol = input("Entra un títol -> ") 
# escriu_titol(titol)
escriu_titol(titol)
print()
escriu_titol(titol, 4, True)
escriu_titol(titol, 4, True, upper=True)
print()
