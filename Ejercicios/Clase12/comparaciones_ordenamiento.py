# comparaciones_ordenamiento.py
import random
import matplotlib.pyplot as plt


def generar_lista(N):
    '''Genera una lista de largo N con números aleatorios entre 1 y 1000'''
    return [random.randint(1,1000) for i in range(N)]


#%% Ordenamiento por selección

def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    
    # Lista copiada para poder comparar sin modificar la original
    lista = lista.copy()

    # posición final del segmento a tratar
    n = len(lista) - 1
    comparaciones = 0

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p, c = buscar_max(lista, 0, n)
        comparaciones += c

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        # print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n = n - 1
    
    return comparaciones

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    c = 0
    
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
        c += 1
    return pos_max, c


#%% Ordenamiento por inserción

def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    
    # Lista copiada para poder comparar sin modificar la original
    lista = lista.copy()
    
    comparaciones = 0
    
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            # contando esta como una comparación
            # ... y adicionalmente las comparaciones internas de reubicar()
            comparaciones += reubicar(lista, i + 1) + 1
        # print("DEBUG: ", lista)

    return comparaciones

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]
    c = 0

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1
        c += 1

    lista[j] = v
    
    return c


#%% Ordenamiento por burbujeo

def ord_burbujeo(lista, debug = False):
    '''Ordena una lista de elementos.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada.'''

    # Lista copiada para poder comparar sin modificar la original
    lista = lista.copy()
    
    n = len(lista)
    hay_cambios = True
    comparaciones = 0
    
    while n > 0 and hay_cambios:
        # Por cada elemento se procesa la función auxiliar
        # Invariante: en cada paso el último elemento de la lista será el más grande
        lista[:n], hay_cambios, c = _ord_burbujeo(lista[:n])
        comparaciones += c
        n -= 1
        
        # El parámetro debug ordena imprimir la lista en cada paso
        if debug:
            print(f'Paso {len(lista) - n}', lista)
    
    return comparaciones


def _ord_burbujeo(sublista):
    n = 0
    hay_cambios = False
    c = 0
    
    while n < len(sublista) - 1:
        # Compara cada elemento con el siguiente y, si es necesario, los ordena
        if sublista[n] > sublista[n+1]:
            sublista[n], sublista[n+1] = sublista[n+1], sublista[n]
            hay_cambios = True
        c += 1
        n += 1
    
    return sublista, hay_cambios, c


#%% Merge Sort

def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    comparaciones = 0
    
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])['lista']
        der = merge_sort(lista[medio:])['lista']
        lista_nueva, c = merge(izq, der)
        comparaciones += c
    
    return {'lista': lista_nueva, 'comparaciones': comparaciones}


def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    c = 0

    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
        c += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado, c


#%% Experimentos

def experimento(N, k):
    ops_seleccion = []
    ops_insercion = []
    ops_burbujeo = []
    
    for i in range(k):
        lista = generar_lista(N)
        ops_seleccion.append(ord_seleccion(lista))
        ops_insercion.append(ord_insercion(lista))
        ops_burbujeo.append(ord_burbujeo(lista))
        
    prom_seleccion = sum(ops_seleccion) / len(ops_seleccion)
    prom_insercion = sum(ops_insercion) / len(ops_insercion)
    prom_burbujeo = sum(ops_burbujeo) / len(ops_burbujeo)
    
    return (prom_seleccion, prom_insercion, prom_burbujeo)


def experimento_vectores(Nmax):
    ops_seleccion = []
    ops_insercion = []
    ops_burbujeo  = []
    ops_mergesort = []
    
    for N in range(1, Nmax + 1):
        lista = generar_lista(N)
        ops_seleccion.append(ord_seleccion(lista))
        ops_insercion.append(ord_insercion(lista))
        ops_burbujeo.append(ord_burbujeo(lista))
        ops_mergesort.append(merge_sort(lista)['comparaciones'])
    
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
