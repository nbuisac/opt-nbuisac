import argparse
import pathlib

parser = argparse.ArgumentParser(prog="py grepa.py",
                                 description="mostra les linies d'un fitxer que contenen un text que li passem")

parser.add_argument("-e", type=str, required=True, help="text a buscar")
parser.add_argument("nom_fitxer", type=str)

args = parser.parse_args()

nom_fitxer = args.nom_fitxer

q = pathlib.Path(nom_fitxer)
if q.exists():
    if q.is_dir():
        print(f"Path {nom_fitxer} és un directori")
        for f in q.iterdir():
            print(f)
    else:
        with open(q, "rt") as f:
            for linia in f:
                if args.e in linia:
                    print(f"{q}:{linia}", end="")
else:
    print(f"Path {nom_fitxer} inexistent")