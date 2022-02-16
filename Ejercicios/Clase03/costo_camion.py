import csv

def costo_camion(nombre_archivo):
    'Imprime el costo total de la carga del camión'
    total = float(0)

    f = open(nombre_archivo, 'rt')
    rows = csv.reader(f)
    headers = next(rows)

    for n_row, row in enumerate(rows, start=1):
        record = dict(zip(headers, row))
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            total += ncajones * precio
            # Esto atrapa errores en los int() y float() de arriba.
        except ValueError:
            print(f'Fila {n_row}: No pude interpretar: {row}')

    f.close()

    return total

costo = costo_camion('../Data/missing.csv')
print(f'Costo total {costo:0.2f}')
