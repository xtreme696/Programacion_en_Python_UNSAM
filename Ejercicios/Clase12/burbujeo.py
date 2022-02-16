# burbujeo.py

# La complejidad de procesamiento del algorítmo es cuadrática ya que recorre una lista
# ... de N elementos N cantidad de veces

# Para analizar el comportamiento utilicé una variable auxiliar e imprimí el proceso

# El tiempo en los casos más favorables podría acortarse agregando otra variable
# ... que almacenara un bool en función de si hay o no cambios realizados en la lista
# ... y que fuese condición para pasar al próximo paso de procesamiento

def ord_burbujeo(lista, debug = False):
    '''Ordena una lista de elementos.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada.'''
    
    n = len(lista)
    hay_cambios = True
    
    while n > 0 and hay_cambios:
        # Por cada elemento se procesa la función auxiliar
        # Invariante: en cada paso el último elemento de la lista será el más grande
        lista[:n], hay_cambios = _ord_burbujeo(lista[:n])
        n -= 1
        
        # El parámetro debug ordena imprimir la lista en cada paso
        if debug:
            print(f'Paso {len(lista) - n}', lista)
    
    return lista


def _ord_burbujeo(sublista):
    n = 0
    hay_cambios = False
    
    while n < len(sublista) - 1:
        # Compara cada elemento con el siguiente y, si es necesario, los ordena
        if sublista[n] > sublista[n+1]:
            sublista[n], sublista[n+1] = sublista[n+1], sublista[n]
            hay_cambios = True
        n += 1
    
    return sublista, hay_cambios
