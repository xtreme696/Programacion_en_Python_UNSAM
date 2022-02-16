# arboles.py
#%% 3.18
import csv
import statistics
from collections import Counter

archivo = '../Data/arbolado-en-espacios-verdes.csv'

def leer_parque(nombre_archivo, parque):
    lista = []
    with open(nombre_archivo, 'rt', encoding="utf-8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            if record['espacio_ve'] == parque:
                lista.append(record)
    
    return lista


parque = leer_parque(archivo, "GENERAL PAZ")

#%% 3.19

def especies(lista_arboles):
    lista = []
    for d in lista_arboles:
        lista.append(d['nombre_com'])
    
    return set(lista)

especies_gral_paz = especies(parque)

#%% 3.20

def contar_ejemplares(lista_arboles):
    diccionario = Counter()
    for d in lista_arboles:
        diccionario[d['nombre_com']] += 1
    
    return diccionario


cuenta_gral_paz = contar_ejemplares(parque)


def mas_comunes(lista_arboles):
    total = contar_ejemplares(lista_arboles)
    
    return total.most_common(5)
    

# print(mas_comunes(leer_parque(archivo, 'GENERAL PAZ')))
# print(mas_comunes(leer_parque(archivo, 'ANDES, LOS')))
# print(mas_comunes(leer_parque(archivo, 'CENTENARIO')))

#%% 3.21

def obtener_alturas(lista_arboles, especie):
    lista = []
    for d in lista_arboles:
        if d['nombre_com'] == especie:
            lista.append(float(d['altura_tot']))
    
    return lista


def altura_max(lista_arboles, especie):
    alturas = obtener_alturas(lista_arboles, especie)
    altura_max = max(alturas)
    return altura_max


def altura_prom(lista_arboles, especie, decimales = 2):
    alturas = obtener_alturas(lista_arboles, especie)
    altura_prom = statistics.mean(alturas)
    return round(altura_prom, decimales)


# print(altura_prom(leer_parque(archivo, 'GENERAL PAZ'), 'Jacarandá'))
# print(altura_prom(leer_parque(archivo, 'ANDES, LOS'), 'Jacarandá'))
# print(altura_prom(leer_parque(archivo, 'CENTENARIO'), 'Jacarandá'))

#%% 3.22

def obtener_inclinaciones(lista_arboles, especie):
    lista = []
    for d in lista_arboles:
        if d['nombre_com'] == especie:
            lista.append(float(d['inclinacio']))
    
    return lista

#%% 3.23

def especimen_mas_inclinado(lista_arboles):
    diccionario = Counter()
    for especie in especies(lista_arboles):
        diccionario[especie] = max(obtener_inclinaciones(lista_arboles, especie))
    
    mas_inclinado = {'especimen': '', 'angulo': 0}
    for especimen in diccionario:
        if diccionario[especimen] > mas_inclinado['angulo']:
            mas_inclinado = {'especimen': especimen, 'angulo': diccionario[especimen]}
    
    print(f'El {mas_inclinado["especimen"]} es el espécimen más inclinado del parque, con una inclinación de {mas_inclinado["angulo"]}º')
    
    return mas_inclinado


def especie_promedio_mas_inclinada(lista_arboles):
    diccionario = Counter()
    for especie in especies(lista_arboles):
        diccionario[especie] = statistics.mean(obtener_inclinaciones(lista_arboles, especie))
    
    mas_inclinado = {'especimen': '', 'angulo': 0}
    for especimen in diccionario:
        if diccionario[especimen] > mas_inclinado['angulo']:
            mas_inclinado = {'especimen': especimen, 'angulo': diccionario[especimen]}
    
    print(f'El {mas_inclinado["especimen"]} es la especie con mayor inclinación promedio del parque, con una inclinación de {mas_inclinado["angulo"]}º')
    
    return mas_inclinado

#%% 4.15

def leer_arboles(nombre_archivo):
    lista = []
    with open(nombre_archivo, 'rt', encoding="utf-8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            lista.append(record)
    
    return lista

arboleda = leer_arboles(archivo)

# 4.16
h_jacaranda = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

# 4.17
t_jacaranda = [tuple([float(arbol['altura_tot']), float(arbol['diametro'])]) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

# 4.18
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

def medidas_de_especies(especies, arboleda):
    return {especie: [tuple([float(arbol['altura_tot']), float(arbol['diametro'])]) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies}

#%% 5.25

import matplotlib.pyplot as plt
import numpy as np

# plt.hist(h_jacaranda,bins=100)

# 5.26
def scatter_hd(lista_de_pares, especie, nuevo_plot = True):
    h = [h for h, d in lista_de_pares]
    d = [d for h, d in lista_de_pares]
    if nuevo_plot:
        plt.figure()
        plt.scatter(d, h, color='green', alpha=0.1)
    else:
        plt.scatter(d, h, color=np.random.rand(3,), alpha=0.05)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title(f"Relación diámetro-alto para {especie}")
    # plt.xlim(0, 30) 
    # plt.ylim(0, 100)
    
# 5.27
medidas = medidas_de_especies(especies, arboleda)

# Gráficos separados
for especie in medidas:
    scatter_hd(medidas[especie], especie)

# Gráficos solapados
for especie in medidas:
    scatter_hd(medidas[especie], especie, False)
