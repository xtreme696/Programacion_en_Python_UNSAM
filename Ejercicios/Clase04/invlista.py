# -*- coding: utf-8 -*-
# 4.5

def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista
        invertida = [e] + invertida
    return invertida