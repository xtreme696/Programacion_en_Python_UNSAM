import random
import numpy as np
import matplotlib.pyplot as plt

figus_total = 670
figus_paquete = 5

# 5.10
def crear_album(figus_total):
    return np.zeros(figus_total, dtype=np.int64)

# 5.11
def album_incompleto(A):
    return 0 in A

# 5.12
def comprar_figu(figus_total):
    return random.randint(0, figus_total - 1)

# 5.13
def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    compradas = 0
    while album_incompleto(album):
        compradas += 1
        album[comprar_figu(figus_total)] += 1
    return compradas

# 5.14
# n_repeticiones = 1000
# micro_album = 6
# promedio_micro_album = np.mean([cuantas_figus(micro_album) for n in range(n_repeticiones)])
# print(promedio_micro_album)

# 5.15
def experimento_figus(n_repeticiones, figus_total):
    exp = np.array([cuantas_figus(figus_total) for n in range(n_repeticiones)])
    
    plt.hist(exp,bins=n_repeticiones)
    plt.xlabel("Cantidad de figuritas comprados.")
    plt.ylabel("Cantidad de casos.")
    plt.show()
    
    return np.mean(exp)

#%% Paquetes

# 5.17
def comprar_paquete(figus_total, figus_paquete, tiene_repetidas = True):
    if tiene_repetidas:
        return random.choices(range(figus_total), k = figus_paquete)
    return random.sample(range(figus_total), k = figus_paquete)

# 5.18
def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    paquetes = 0
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        paquetes += 1
        for figu in paquete:
            album[figu] += 1
    return paquetes

# 5.19
def experimento_paquetes(n_repeticiones, figus_total, figus_paquete):
    exp = np.array([cuantos_paquetes(figus_total, figus_paquete) for n in range(n_repeticiones)])
    
    plt.hist(exp,bins=n_repeticiones)
    plt.xlabel("Cantidad de paquetes comprados.")
    plt.ylabel("Cantidad de casos.")
    plt.show()
    
    return np.mean(exp)

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

# plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
# plt.xlabel("Cantidad de paquetes comprados.")
# plt.ylabel("Cantidad de figuritas pegadas.")
# plt.title("La curva de llenado se desacelera al final")
# plt.show()

#%% Estadísticas

# 5.20
def probabilidad_comprando(n_paquetes, n_repeticiones, figus_total, figus_paquete):
    completo = []
    for i in range(n_repeticiones):
        completo += [(cuantos_paquetes(figus_total, figus_paquete) <= n_paquetes)]
    return sum(completo) / len(completo)

# 5.21
# Cambios realizados a las funciones de experimentos

# 5.22
def noventa_porciento():
    n_paquetes = 800
    while probabilidad_comprando(n_paquetes, 10, figus_total, figus_paquete) < 0.9:
        n_paquetes += 1
    return n_paquetes
