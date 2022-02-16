# solucion_de_errores.py
'Ejercicios de errores en el código'

#%% 3.1. Función tiene_a()
# Comentarios:
# El error era de tipo semántico y estaba ubicado dentro del else.
# En la primer iteración la función pasaba de cualquier forma por un return, lo que evitaba que el loop siguiera su curso.
# Lo corregí desplazando ese return al final de la función.
# Adicionalmente agregué al condicional la detección de A mayúscula, considerando que la finalidad de la función lo justifica.

# Código corregido:
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' or expresion[i] == 'A':
            return True
        i += 1
    return false

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%% 3.2. Función tiene_a(), nuevamente
# Comentarios:
# Los errores eran de sintaxis.
# Estaban ubicados en las líneas 1, 4 y 5 (falta de :), y en el return final (Falso en lugar de False)
# Adicionalmente agregué al condicional la detección de A mayúscula, considerando que la finalidad de la función lo justifica.

# Código corregido:
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' or expresion[i] == 'A':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%% 3.3. Función tiene_uno()
# Comentarios:
# El error era de tipo TypeError (en tiempo de ejecución), y ocurría al pasar como argumentos valores que no fuesen strings
# Lo corregí agregando una línea para convertir la expresión a string

# Código corregido:
def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

#%% Función suma()
# Comentarios:
# El error era semántico, la función no devolvía nungún valor (None).
# Podríamos corregirlo devolviendo el valor de c (cuando c = a + b), o bien devolviendo la suma expresión

# Código corregido:
def suma(a,b):
    return a + b

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%% 3.5. Función leer_camion()
# Comentarios:
# El error era de tipo semántico.
# Al encontrarse la variable registro por fuera del with, su valor era reemplazado en cada iteración.
# Lo corregí moviendo la variable registro dentro del for, para utilizarla como una variable temporal en cada iteración.

# Código corregido:
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
