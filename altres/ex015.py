# Fes un programa que demani dos números qualssevol i després els mostri en ordre creixent.
# Demana a i b, i escriu a i b. Ha de permutar el valor de les variables si cal.
## Podem assignar, en una linia, el mateix valor a diverses variables
numero1_1 = numero1_2 = int(input("Entra el número 1 -> "))
numero2_1 = numero2_2 = int(input("Entra el número 2 -> "))
## En qualsevol llenguatge caldria una variable d'ajuda per intercanviar els valors de dues variables
if numero1_1 > numero2_1:
    ajuda = numero1_1
    numero1_1 = numero2_1
    numero2_1 = ajuda
print(f"Números ordenats {numero1_1}  {numero2_1}")
## En python podem assignar dues variables de cop assignant-li dos valors diferents
if numero1_2 > numero2_2:
    numero1_2, numero2_2 = numero2_2, numero1_2
print(f"Números ordenats {numero1_2}  {numero2_2}")
