def escriu_titol(missatge, subr="=", sobr=None,end="\n",upper=False):
    if upper == True:
        missatge = missatge.upper()
    if sobr != None:
        if sobr == True and subr != None:
            sobr = subr
        print(sobr * len(missatge), end=end)
    print(missatge, end = end)
    if subr != None:
        print(subr * len(missatge), end = end)

# nom = input("Entra el teu nom -> ")
escriu_titol("Hola")
escriu_titol("Hola", sobr='.', subr=None, upper= True)
escriu_titol("Hola", '.', True, end="<br />\n")
escriu_titol("Hola", '.', True, end="<br />\n", upper=True)
