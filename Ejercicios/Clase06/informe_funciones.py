# informe_funciones.py
from fileparse import parse_csv

def leer_camion(nombre_archivo = '../Data/camion.csv'):
    'Genera una lista de diccionarios a partir del archivo'
    camion = parse_csv(nombre_archivo)

    return camion


def leer_precios(nombre_archivo = '../Data/precios.csv'):
    'Genera un diccionario de precios a partir de un archivo'
    precios = dict(parse_csv(nombre_archivo, types = [str, float], has_headers = False))

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


def imprimir_informe(camion, precios, headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')):
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


def informe_camion(archivo_camion = '../Data/camion.csv', archivo_precios = '../Data/precios.csv'):
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)
    
    informe = imprimir_informe(camion, precios)

    for nombre, cajones, precio, cambio in informe:
        print(f"{nombre:>10} {cajones:>10} {'$'+str(round(precio,2)):>10} {cambio:>10.2f}")
    

# informe_camion()