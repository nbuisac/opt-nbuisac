import argparse
import pathlib

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="grep", description="comanda per buscar texte en fitxers",
                                     epilog="""Comanda que ens permet trobar les línies d'un fitxer
                                     que contenen un texte determinat""")

    parser.add_argument('nom_fitxer')           # positional argument
    parser.add_argument('-e',type=str)           # positional argument

    args = parser.parse_args()

    print(args)
    nom_fitxer_directori = args.nom_fitxer

    x = pathlib.Path(nom_fitxer_directori)
    if x.is_dir():
        print("M'has indicat un directori")
        for p in x.iterdir():
            print(f"{p}")
    elif x.is_file():
        print("M'has indicat un fitxer")
        with open(x, "rt") as f:
            linia = f.readline()
            while linia != "":
                if args.e in linia:
                    print(f"{x}:{linia}", end="")
                linia = f.readline()
    else:
        print("No ho trobo")

