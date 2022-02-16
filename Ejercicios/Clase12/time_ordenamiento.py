# time_ordenamiento.py
import random
import matplotlib.pyplot as plt
import numpy as np
import time
import timeit as tt


def generar_lista(N):
    '''Genera una lista de largo N con números aleatorios entre 1 y 1000'''
    return [random.randint(1,1000) for i in range(N)]


#%% Ordenamiento por selección

def ord_seleccion(lista):
    lista = lista
    n = len(lista) - 1
    while n > 0:
        p = buscar_max(lista, 0, n)
        lista[p], lista[n] = lista[n], lista[p]
        n = n - 1
    
    return lista

def buscar_max(lista, a, b):
    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max


#%% Ordenamiento por inserción

def ord_insercion(lista):
    lista = lista
    for i in range(len(lista) - 1):
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)

    return lista

def reubicar(lista, p):
    v = lista[p]
    j = p
    while j > 0 and v < lista[j - 1]:
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v
    
    return


#%% Ordenamiento por burbujeo

def ord_burbujeo(lista, debug = False):
    lista = lista
    n = len(lista)
    hay_cambios = True
    
    while n > 0 and hay_cambios:
        lista[:n], hay_cambios = _ord_burbujeo(lista[:n])
        n -= 1
    
    return lista


def _ord_burbujeo(sublista):
    n = 0
    hay_cambios = False
    
    while n < len(sublista) - 1:
        if sublista[n] > sublista[n+1]:
            sublista[n], sublista[n+1] = sublista[n+1], sublista[n]
            hay_cambios = True
        n += 1
    
    return sublista, hay_cambios


#%% Merge Sort

def merge_sort(lista):
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)
    
    return lista_nueva


def merge(lista1, lista2):
    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado

#%% Experimentos

def experimento_timeit_seleccion(listas, num):
    """
    Realiza un experimento usando timeit para evaluar el método
    de selección para ordenamiento de listas
    con las listas pasadas como entrada
    y devuelve los tiempos de ejecución para cada lista
    en un vector.
    El parámetro 'listas' debe ser una lista de listas.
    El parámetro 'num' indica el número de veces que repite el ordenamiento para cada lista.
    """
    tiempos_seleccion = []
    
    global lista
    
    for lista in listas:
     
        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempo_seleccion = tt.timeit('ord_seleccion(lista.copy())', number = num, globals = globals())
        
        # guardo el resultado
        tiempos_seleccion.append(tiempo_seleccion)
        
    # paso los tiempos a arrays
    tiempos_seleccion = np.array(tiempos_seleccion)
    
    return tiempos_seleccion


# listas = []
# for N in range(1, 256):
#     listas.append(generar_lista(N))

# tiempos_seleccion = experimento_timeit_seleccion(listas, 100)
# plt.plot(tiempos_seleccion)

def generar_listas(Nmax):
    listas = []
    for N in range(Nmax):
        listas.append(generar_lista(N + 1))
    return listas


def experimento_timeit(Nmax):
    ops_seleccion = []
    ops_insercion = []
    ops_burbujeo  = []
    ops_mergesort = []
    
    global lista
    
    for lista in generar_listas(Nmax):
        ops_seleccion.append(tt.timeit('ord_seleccion(lista.copy())', number = 1, globals = globals()))
        ops_insercion.append(tt.timeit('ord_insercion(lista.copy())', number = 1, globals = globals()))
        ops_burbujeo.append(tt.timeit('ord_burbujeo(lista.copy())', number = 1, globals = globals()))
        ops_mergesort.append(tt.timeit('merge_sort(lista.copy())', number = 1, globals = globals()))
    
    fig, ax = plt.subplots()
    
    plt.plot(range(Nmax), ops_seleccion, label='Selección', linestyle='dashed')
    plt.plot(range(Nmax), ops_insercion, label='Inserción')
    plt.plot(range(Nmax), ops_burbujeo, label='Burbujeo')
    plt.plot(range(Nmax), ops_mergesort, label='Merge Sort')
    
    plt.xlabel('Experimento')
    plt.ylabel('Comparaciones')
    plt.title('Métodos de Ordenamiento')
    plt.legend()
    plt.show()

    return
