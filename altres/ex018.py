# Fes un programa que a partir d'una nota numèrica entera entre 0 i 10 indiqui si correspon a:
#   [0 .. 4] → suspès
#   [5 .. 8] → aprovat
#   9 → excel·lent
#   10 → MATRÍCULA D'HONOR
#   altrament: error
nota_numerica = int(input("Entra una nota (1..10) -> "))
if nota_numerica < 0 or nota_numerica > 10:
    nota_escrita = "ERROR"
else:
    if nota_numerica <= 4:
        nota_escrita = "suspès"
    elif nota_numerica <= 8:
        nota_escrita = "aprovat"
    elif nota_numerica == 9:
        nota_escrita = "excel·lent"
    else:
        nota_escrita = "MATRÍCULA D'HONOR"
print("La nota és -> ", nota_escrita)


