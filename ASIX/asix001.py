import sys

print("asix001->", __name__)

if __name__ == "__main__":
    parametres = sys.argv[1:]
    if len(parametres) > 1:
        ## El missatge va després del -m
        # missatge = parametres[-1]
        if '-m' in parametres:
            pos_m = parametres.index('-m')
            missatge = parametres[pos_m + 1]
        
            parametres = parametres[:pos_m] + parametres[pos_m + 2:]
            if '-u' in parametres:
                missatge = missatge.upper()
            elif '-l' in parametres:
                missatge = missatge.lower()
            print(missatge)
        else:
            print(f"Syntax: py {sys.argv[0]} [-u|-l] -m message")
    else:
        print(f"Syntax: py {sys.argv[0]} [-u|-l] -m message")