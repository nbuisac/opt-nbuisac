# La nota d'una assignatura és calcula en base als exàmens (e)
# i les proves pràctiques (p),
# es fa la mitjana ponderada al 40% i 60%.
# He tret un 7 de pràctiques (p), escriu un programa que em calculi quina és la nota final a patir d'una hipotètica nota d'examen introduïda per teclat.
PCT_EXAMEN = 0.40
PCT_PRACTIQUES = 0.60
nota_practiques = 7
nota_examen = float(input("Entra la nota de l'examen ->"))
nota_final = nota_practiques * PCT_PRACTIQUES + nota_examen * PCT_EXAMEN
print("La teva nota final serà :", nota_final)