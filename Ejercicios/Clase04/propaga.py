# -*- coding: utf-8 -*-
# 4.6

def propagar(vector):
    nuevo_vector = vector
    encendido = False
    i = 0
    while i < len(nuevo_vector)-1:
        if nuevo_vector[i] == -1:
            encendido = False
        elif nuevo_vector[i] == 0 and encendido:
            nuevo_vector[i] = 1
        elif nuevo_vector[i] == 1:
            encendido = True
        i += 1
    while i >= 0:
        if nuevo_vector[i] == -1:
            encendido = False
        elif nuevo_vector[i] == 0 and encendido:
            nuevo_vector[i] = 1
        elif nuevo_vector[i] == 1:
            encendido = True
        i -= 1
    
    return nuevo_vector
