import csv

def leer_camion(nombre_archivo = '../Data/camion.csv'):
    'Genera una lista de diccionarios a partir del archivo'
    camion = []

    f = open(nombre_archivo, 'rt')
    rows = csv.reader(f)
    headers = next(rows)

    # for row in rows:
    #     try:
    #         lote = {'nombre': row[col_nombre], 'cajones': int(row[col_cajones]), 'precio': float(row[col_precio])}
    #         camion.append(lote)
    #     except ValueError:
    #         print(f'No se pudo leer correctamente una fila: {row[col_nombre]}')

    for n_row, row in enumerate(rows, start=1):
        record = dict(zip(headers, row))
        try:
            lote = {'nombre': record['nombre'], 'cajones': int(record['cajones']), 'precio': float(record['precio'])}
            camion.append(lote)

        except ValueError:
            print(f'Fila {n_row}: No pude interpretar: {row}')

    f.close()

    return camion


# Función de prueba
def costo_camion(nombre_archivo = '../Data/camion.csv'):
    'Imprime el costo total de la carga del camión'
    total = float(0)
    camion = leer_camion(nombre_archivo)

    for s in camion:
        total += s['cajones'] * s['precio']

    return total


def leer_precios(nombre_archivo = '../Data/precios.csv'):
    'Genera un diccionario de precios a partir de un archivo'
    precios = {}

    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row):
                precios[row[0]] = float(row[1])

    return precios


def balance(precios_productor = '../Data/camion.csv', precios_venta = '../Data/precios.csv'):
    'Genera un balance de ventas entre los precios del productor y la ganancia total del camión'
    camion = leer_camion(precios_productor)
    precios = leer_precios(precios_venta)

    balance = float(0)

    for d in camion:
        try:
            precio_local = precios[d['nombre']]
            balance += (d['cajones'] * precio_local) - (d['cajones'] * d['precio'])
        except:
            print('Uno de los productos no pudo ser calculado')

    return balance


print(f'El balance del negocio es: {balance():0.2f}')
