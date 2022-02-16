# 5.9
import numpy as np
import matplotlib.pyplot as plt

temperaturas = np.load('../Data/temperaturas.npy')
plt.hist(temperaturas,bins=999)
plt.show() #el show no hace falta en algunos entornos. A veces lo omitiremos.
