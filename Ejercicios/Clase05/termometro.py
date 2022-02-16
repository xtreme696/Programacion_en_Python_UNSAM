# 5.6
# 5.8
import random
import numpy as np

def medir_temp(n):
    temps = [37.5 + random.normalvariate(0,0.2) for i in range(n)]
    np.save('../Data/temperaturas.npy', np.array(temps))
    return temps

def resumen_temp(n):
    temps = medir_temp(n)
    if len(temps) % 2 == 0:
        mediana = [temps[len(temps) // 2], temps[len(temps) // 2 - 1]]
    else:
        mediana = [temps[int(len(temps))]]
    return (max(temps), min(temps), sum(temps) / len(temps), sum(mediana) / len(mediana))

print(resumen_temp(1000))