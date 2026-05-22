import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="asix003b",
                                     description="Escrivim un missatge per pantalla",
                                     epilog="""Permet mostar un missatge per pantalla
                                            normal, en majúscules o en minúscula"""
                                    )
    parser.add_argument("missatge")
    parser.add_argument('-c', '--count', required=False, type=int, default=1, 
                        help="Nombre de vegades que mostrarem el missatge")      # option that takes a value
    # grup_maj_min = parser.add_argument_group("Majuscula o Minuscula", "Escollim si volem majúscules o minuscules")
    grup_maj_min = parser.add_mutually_exclusive_group()
    grup_maj_min.add_argument("-l", "--lower", action='store_true')
    grup_maj_min.add_argument("-u", "--upper", action='store_true')
    args = parser.parse_args()
    print(args)
    missatge = args.missatge
    if args.lower == True:
        missatge = missatge.lower()
    elif args.upper:
        missatge = missatge.upper()
    for i in range(args.count):
        print(missatge)

    