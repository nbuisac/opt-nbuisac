import random

quantes_cares = 0
quantes_creus = 0
MINIM = 100
# Pararem quan tinguem més cares que creus
while quantes_cares <= quantes_creus or \
      (quantes_creus + quantes_cares <= MINIM):
    moneda = random.randint(0, 1)
    if moneda == 0:
        quantes_cares = quantes_cares + 1
    else:
        quantes_creus += 1
print(f"Fi: cares -> {quantes_cares}\tcreus -> {quantes_creus}")