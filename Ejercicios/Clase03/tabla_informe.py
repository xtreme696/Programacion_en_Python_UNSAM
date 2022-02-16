import csv

def leer_camion(nombre_archivo = '../Data/camion.csv'):
    'Genera una lista de diccionarios a partir del archivo'
    camion = []

    f = open(nombre_archivo, 'rt')
    rows = csv.reader(f)
    headers = next(rows)

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


# print(f'El balance del negocio es: {balance():0.2f}')

#%%

camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')

def hacer_informe(camion, precios, headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')):
    lista = []
    print('%10s %10s %10s %10s' % headers) # Headers
    print(f'{"-"*10} '*4)                  # Separadores
    
    for d in camion:
        try:
            balance = precios[d['nombre']] - d['precio']
            tupla = (d['nombre'], d['cajones'], d['precio'], balance)
            lista.append(tupla)
        except:
            print('Uno de los productos no pudo ser calculado')
    
    return lista


informe = hacer_informe(camion, precios)

for nombre, cajones, precio, cambio in informe:
    print(f"{nombre:>10} {cajones:>10} {'$'+str(round(precio,2)):>10} {cambio:>10.2f}")
    