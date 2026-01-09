import random

TIRADES = 2000000

quantes_cares = 0
quantes_creus = 0

for tirada in range(TIRADES):
    modeda = random.randint(0, 1)
    if modeda == 0: 
        quantes_cares = quantes_cares+ 1

quantes_creus = TIRADES - quantes_cares
print(quantes_cares, quantes_creus )
pct_cares = quantes_cares / TIRADES
pct_creus = 1 - pct_cares
print(f"{pct_cares:.2%}, {pct_creus:.2%}")
