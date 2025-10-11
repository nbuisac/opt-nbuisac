# Escriu un programa que determini el total d'IVA d'un producte donada una quantitat sense IVA i el % d'IVA.
preu = float(input("Entra el preu del producte -> "))
pct_iva = float(input("Entra el % d'IVA -> "))
## Cal deixar només dos decimals. Ho farem sense cap funció.
# Multipliquem per 100, agafem la part entera i dividim per 100
iva = int((preu * pct_iva / 100) * 100) / 100
preu_amb_iva = preu + iva
print("Preu s/iva", preu)
print("iva", iva)
print("Preu a/iva", preu_amb_iva)
