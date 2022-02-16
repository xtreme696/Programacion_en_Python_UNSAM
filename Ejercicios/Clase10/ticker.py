# ticker.py
from vigilante import vigilar
import csv
import informe_final
from formato_tabla import crear_formateador


def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))


def filtrar_datos(rows, nombres):
    for row in rows:
        if row['nombre'] in nombres:
            yield row


def parsear_datos(lines):
    rows = csv.reader(lines)
    # rows = elegir_columnas(rows, [0, 1, 2])
    rows = ((row[index] for index in [0, 1, 2]) for row in rows)
    # rows = cambiar_tipo(rows, [str, float, int])
    rows = ((func(val) for func, val in zip([str, float, int], row)) for row in rows)
    # rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    rows = ((dict(zip(['nombre', 'precio', 'volumen'], row))) for row in rows)
    
    return rows


def ticker(camion_file, log_file, fmt):
    camion = informe_final.leer_camion(camion_file)
    rows = parsear_datos(vigilar(log_file))
    # rows = filtrar_datos(rows, camion)
    rows = (row for row in rows if row['nombre'] in camion)
    
    formateador = crear_formateador(fmt)
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    for row in rows:
        rowdata = [row['nombre'], f"{row['precio']:0.2f}", f"{row['volumen']}"]
        formateador.fila(rowdata)


if __name__ == '__main__':
    lines = vigilar('../Data/mercadolog.csv')
    rows = parsear_datos(lines)
    for row in rows:
        print(row)
