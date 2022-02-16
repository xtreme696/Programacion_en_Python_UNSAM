# random_walk.py

import numpy as np
import matplotlib.pyplot as plt


def randomwalk(largo):
    pasos = np.random.randint(-1,2,largo)
    return pasos.cumsum()


def mas_alejada(caminatas):
    'Devuelve la caminata que más difiere del eje X en su punto más lejano'
    caminata = caminatas[0]
    valor_mas_lejano = 0
    for c in caminatas:
        for i in c:
            if abs(i) > valor_mas_lejano:
                valor_mas_lejano = abs(i)
                caminata = c
    return caminata


def menos_alejada(caminatas):
    'Devuelve la caminata que menos difiere del eje X en su punto más lejano'
    caminata = caminatas[0]
    valor_menos_lejano = 100000
    for c in caminatas:
        valor_mas_lejano = 0
        for i in c:
            if abs(i) > valor_mas_lejano:
                valor_mas_lejano = abs(i)
        if valor_mas_lejano < valor_menos_lejano:
            valor_menos_lejano = valor_mas_lejano
            caminata = c
        print(valor_menos_lejano)
    return caminata


N = 100000
ncaminatas = 12
caminatas = []

for i in range(ncaminatas):
    caminatas.append(randomwalk(N))


# Figura superior
fig = plt.figure()
plt.subplot(2, 1, 1).set_title(f'{ncaminatas} Caminatas al azar')
for caminata in caminatas:
    plt.plot(caminata)
plt.xticks([]), plt.yticks([-500, 0, 500])

# Figura inferior izquierda
plt.subplot(2, 2, 3).set_title('La caminata que más se aleja')
plt.plot(mas_alejada(caminatas))
plt.xticks([]), plt.yticks([-500, 0, 500])

# Figura inferior derecha
plt.subplot(2, 2, 4).set_title('La caminata que menos se aleja')
plt.plot(menos_alejada(caminatas))
plt.xticks([]), plt.yticks([-500, 0, 500])

plt.show()