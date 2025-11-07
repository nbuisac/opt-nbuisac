# Fes un programa que donades dues notes amb decimals entre 0 i 10,
# corresponents a pràctiques (30%) i a teoria (70%),
# calculi la mitjana i expressi el resultat en lletres, tenint en compte la següent taula,
# i que si una nota qualsevol és inferior a 3 ja no fa mitjana (suspèn automàticament):
#   [0 .. 5) → suspès
#   [5 .. 7) → aprovat
#   [7 .. 9) → notable
#   [9 .. 10) → excel·lent
#   10 → MATRÍCULA D'HONOR
nota_practiques = float(input("Entra la nota de pràctiques (0..10) -> "))
nota_teoria = float(input("Entra la nota de teoria (0..10) -> "))
if nota_practiques < 3 or nota_teoria < 3:
    nota_escrita = "suspès"
else:
    nota_numerica = nota_practiques * 0.30 + nota_teoria * 0.70
    if nota_numerica < 5:
        nota_escrita = "suspès"
    elif nota_numerica < 7:
        nota_escrita = "aprovat"
    elif nota_numerica < 9:
        nota_escrita = "aprovat"
    elif nota_numerica < 10:
        nota_escrita = "excel·lent"
    else:
        nota_escrita = "MATRÍCULA D'HONOR"
print("La nota és -> ", nota_escrita)


