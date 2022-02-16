# -*- coding: utf-8 -*-
# 4.3

def buscar_u_elemento(lista, elemento):
    '''Devuelve el índice de un elemento en una lista. 
    En caso de no existir devuelve -1.'''
    pos = -1
    for i, z in enumerate(lista):
        if z == elemento:
            pos = i
    return pos


def buscar_n_elemento(lista, elemento):
    '''Devuelve la cantidad de coincidencias de un elemento en una lista'''
    cant = 0
    for i in lista:
        if i == elemento:
            cant += 1
    return cant


#%% 4.4

def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía.'''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = lista[0] # Lo inicializo en el primer valor de la lista
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e
    return m

def minimo(lista):
    '''Devuelve el mínimo de una lista, 
    la lista debe ser no vacía.'''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = lista[0] # Lo inicializo en el primer valor de la lista
    for e in lista: # Recorro la lista y voy guardando el menor
        if e < m:
            m = e
    return m
