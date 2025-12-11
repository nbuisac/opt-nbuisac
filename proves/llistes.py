import random
notes = []

for i in range(14):
    nota = random.randint(1,10)
    notes.append(nota)

print(notes)
aprovats = 0
for nota in notes:
    if nota >= 5:
        aprovats = aprovats + 1
print(f"Han aprovat {aprovats} i han suspes {len(notes) - aprovats}")
    