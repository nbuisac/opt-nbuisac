nom_fitxer = "a.txt"

with open(nom_fitxer, "wt", encoding="utf8") as f:
    for a in range(100):
        q = f.write(f"Anem per la línia {a}\n")
        print(q)

    f.write(12)
