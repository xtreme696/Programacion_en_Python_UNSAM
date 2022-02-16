# informe_final.py
from fileparse import parse_csv
import formato_tabla
from lote import Lote
from camion import Camion


def leer_camion(nombre_archivo = '../Data/camion.csv'):
    '''
    Lee un archivo con el contenido de un camión
    y lo devuelve como un objeto Camion.
    '''
    with open(nombre_archivo) as file:
        camiondicts = parse_csv(file,
                                        select = ['nombre', 'cajones', 'precio'],
                                        types = [str, int, float])

    camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camiondicts]
    return Camion(camion)


def leer_precios(nombre_archivo = '../Data/precios.csv'):
    'Genera un diccionario de precios a partir de un archivo'
    with open(nombre_archivo) as f:
        precios = dict(parse_csv(f, types = [str, float], has_headers = False))

    return precios


def balance(precios_productor = '../Data/camion.csv', precios_venta = '../Data/precios.csv'):
    'Genera un balance de ventas entre los precios del productor y la ganancia total del camión'
    camion = leer_camion(precios_productor)
    precios = leer_precios(precios_venta)

    balance = float(0)

    for d in camion:
        try:
            precio_local = precios[d.nombre]
            balance += (d.cajones * precio_local) - (d.cajones * d.precio)
        except:
            print('Uno de los productos no pudo ser calculado')

    return balance


# def imprimir_informe(camion, precios, headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')):
#     lista = []
#     print('%10s %10s %10s %10s' % headers) # Headers
#     print(f'{"-"*10} '*4)                  # Separadores
    
#     for d in camion:
#         try:
#             balance = precios[d.nombre] - d.precio
#             tupla = (d.nombre, d.cajones, d.precio, balance)
#             lista.append(tupla)
#         except:
#             print('Uno de los productos no pudo ser calculado')
    
#     return lista


# def informe_camion(archivo_camion = '../Data/camion.csv', archivo_precios = '../Data/precios.csv'):
#     camion = leer_camion(archivo_camion)
#     precios = leer_precios(archivo_precios)
    
#     informe = imprimir_informe(camion, precios)

#     for nombre, cajones, precio, cambio in informe:
#         print(f"{nombre:>10} {cajones:>10} {'$'+str(round(precio,2)):>10} {cambio:>10.2f}")


def hacer_informe(camion, precios):
    lista = []
    for l in camion:
        precio_venta = precios[l.nombre]
        cambio = precio_venta - l.precio
        t = (l.nombre, l.cajones, precio_venta, cambio)
        lista.append(t)
    return lista


def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)


def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es .txt
    Alternativas: .csv o .html
    '''
    # Lee archivos de datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Crea la data del informe
    data_informe = hacer_informe(camion, precios)

    # Imprime el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)

#%% 7.4

def f_principal(argv):
    if len(argv) == 4:
        archivo_py, archivo_camion, archivo_precios, fmt = argv
        return informe_camion(archivo_camion, archivo_precios, fmt)
    if len(argv) == 3:
        archivo_py, archivo_camion, archivo_precios = argv
        return informe_camion(archivo_camion, archivo_precios)
    return False


if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
    