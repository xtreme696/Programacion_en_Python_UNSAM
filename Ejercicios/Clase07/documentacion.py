# documentacion.py

def valor_absoluto(n):
    '''Calcula el valor absoluto de un número.
    
    Pre: n es un caracter numérico entero o de punto flotante.
    Pos: Se devuelve el valor absoluto.
    '''
    if n >= 0:
        return n
    else:
        return -n
    

def suma_pares(l):
    '''Calcula la suma de los elementos pares de un iterable.
    
    Pre: l es un iterable que contiene solo valores numéricos.
    Pos: Se devuelve la suma de sus elementos pares.
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0
    # invariante: res almacena el valor de la suma comenzando en 0
    return res


def veces(a, b):
    '''Calcula el valor de b veces a.
    
    Pre: a y b deben ser valores numéricos donde b es positivo.
    Pos: Se devuelve la multiplicación de los elementos.
    '''
    res = 0
    nb = int(b) # Solucionado un error de ejecución cuando b es de punto flotante
    if b > 0:   # Solucionado un error de ejecución cuando b es negativo
        while nb != 0:
            res += a
            nb -= 1
    # invariante: res almacena el valor de la suma por ciclo comenzando en 0
    #   nb es el contador del número de veces que el ciclo aplica
    return res


def collatz(n):
    '''https://es.wikipedia.org/wiki/Conjetura_de_Collatz
    
    Pre: n es un número entero positivo
    Pos: Se devuelve la conjetura de Collatz aplicada a n
    '''
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1
    # invariante: res almacena la respuesta a cada paso del ciclo comenzando en 1
    return res
