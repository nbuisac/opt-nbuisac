import_base = float(input("Entra el preu de la casa -> "))
despeses = import_base * 0.12
total = import_base + despeses
import_a_tenir = import_base * 0.20 + despeses
print(f"Import base             -> {import_base:15.2f}")
print(f"Despeses                -> {despeses:15.2f}")
print(f"Preu total              -> {total:15.2f}")
print(f"has de tenir estalviat  -> {import_a_tenir:15.2f}")