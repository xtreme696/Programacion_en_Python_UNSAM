# 5.5

import random

def generar_punto():
    x = random.random()
    y = random.random()
    return x, y

N = 100000
M = 0
for i in range(N):
    punto = generar_punto()
    if punto[0]**2 + punto[1]**2 < 1:
        M += 1

print(f'Estimamos pi en {4*M/N}')