import csv
import sys

def costo_camion(nombre_archivo):
    'Imprime el costo total de la carga del camión'
    total = float(0)

    f = open(nombre_archivo, 'rt')
    rows = csv.reader(f)
    headers = next(rows)

    col_nombre = headers.index('nombre')
    col_cajones = headers.index('cajones')
    col_precio = headers.index('precio')

    for row in rows:
        try:
            total += int(row[col_cajones]) * float(row[col_precio])
        except ValueError:
            print(f'No se pudo calcular el valor de un producto: {row[col_nombre]}')

    return total

if len(sys.argv) == 2:
    print(sys.argv)
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print(f'Costo total {costo:0.2f}')
