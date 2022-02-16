# bbin.py

def donde_insertar(lista, x):
    '''Algoritmo binario
    Precondición: la lista está ordenada
    Devuelve la posición en donde x existe o podría existir
    '''
    izq = 0
    der = len(lista) - 1
    pos = (izq + der) // 2 # Inicializo respuesta
    while izq < der:
        if lista[pos] == x:
            break
        if lista[pos] > x:
            der = pos - 1 # descarto mitad derecha
        else:
            izq = pos + 1 # descarto mitad izquierda
        pos = (izq + der) // 2
    
    if lista[pos] < x:
        pos += 1
    
    return pos


def insertar(lista, x):
    '''Algoritmo binario
    Precondición: la lista está ordenada
    Devuelve la posición en donde x existe o lo inserta
    '''
    pos = donde_insertar(lista, x)
    lista.insert(pos, x)
    
    return pos