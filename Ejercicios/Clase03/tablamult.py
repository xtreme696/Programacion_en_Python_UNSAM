# tablamult.py
# Como desafío personal quise flexibilizar la cantidad de filas y columnas de la tabla
# Al pasarle argumentos ([rows],[cols]) se modifica la impresión de la tabla

def tabla(num, cols):
    tabla = []
    suma = 0    # Evitando usar multiplicación
    for i in range(cols):
        tabla.append(suma)
        suma += num
    
    return tabla


def print_row(row):
    print(f'{row.pop(0):^4}',end='')
    for r in row:
        print(f'{r:>4}',end='')
    print('\n')


def print_tablas(rows = 10, cols = 10):
    header = ['']
    for c in range(cols):
        header.append(c)
    print_row(header)                       # Imprime Headers
    print(f'{"----"*(cols+1)}-')            # Imprime Separadores
    for r in range(rows):
        row = [f'{r}:'] + tabla(r, cols)
        print_row(row)                      # Imprime Fila


print_tablas()