# Escriu un programa que donat el nom i el cognom de l'usuari,
# els imprimeixi en ordre invers.
nom = input("Entra el teu nom -> ")
cognom = input("Entra el teu cognom -> ")
print(cognom, ',', nom)
print(nom[-1::-1], cognom[-1::-1])
print((nom + cognom)[-1::-1])
