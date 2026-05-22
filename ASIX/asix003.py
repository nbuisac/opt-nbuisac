import argparse

parser = argparse.ArgumentParser(prog="py asix003.py",description="Mostra un missatge per pantalla",
                                 epilog="""
                                Mostra un amissatge per pantalla que pot ser en majúscules o en minúscules
                                 """)
parser.add_argument("missatge",type=str)
parser.add_argument('-c', '--count',help="Nombre de vegades que es mostra el missatge", type=int, default=1)
grup = parser.add_mutually_exclusive_group()
grup.add_argument("-l", "--lower", action='store_true')
grup.add_argument("-u", "--upper", action='store_true')


args = parser.parse_args()
print(args.missatge, args.lower, args.count, args.upper)

missatge = args.missatge
if args.lower == True:
    missatge = missatge.lower()
elif args.upper:
    missatge = missatge.upper()
for i in range(args.count):
    print(missatge)
