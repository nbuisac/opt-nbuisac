fruita = input("Vols treballar amb (p)eres o (c)astanyes? ")
correcte = True
if len(fruita) == 1 and fruita.lower() in "pc":
    if fruita.lower() == 'p':
        caixes = int(input("Entra el nombre de caixes -> "))
        preu_caixa = float(input("Entra el preu de  cada caixa -> "))
        dcte = float(input("Entra el % de  descompte -> "))
    else:
        qualitat = input("Entra la qualitat (a)lta (b)aixa -> ")
        caixes = int(input("Entra el nombre de sacs -> "))
        preu_caixa = float(input("Entra el preu de cada sac -> "))
        if len(qualitat) == 1 and qualitat.lower() == 'a' and caixes > 4:
            dcte = 15
        else:
            dcte = 0
else:
    correcte = False
if correcte:
    print(f"{caixes * preu_caixa * (1 - dcte / 100):.2f}")
else:
    print("ERROR")