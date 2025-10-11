# Escriu un programa que determini aproximadament l'edat de l'usuari en dies,
# donada la seva data de naixement. Pots considerar que els mesos tenen 30 dies.
# Fes-ho a a partir del mes i l'any.
mes_actual = int(input("Entra el mes actual -> "))
any_actual = int(input("Entra l'any actual -> "))
mes_naixement = int(input("Entra el mes de naixement -> "))
any_naixement = int(input("Entra l'any de naixement -> "))
anys = any_actual - any_naixement
mesos = mes_actual - mes_naixement
mesos_totals = anys * 12 + mes_actual - mes_naixement
dies_totals = mesos_totals * 30
print("L'edat en dies és, aproximadament, de", dies_totals)
print(anys, mesos, mesos_totals)