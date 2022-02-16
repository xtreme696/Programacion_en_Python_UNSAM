# costo_camion
import informe_funciones

def costo_camion(nombre_archivo = '../Data/camion.csv'):
    'Imprime el costo total de la carga del camión'
    total = float(0)
    camion = informe_funciones.leer_camion(nombre_archivo)

    for s in camion:
        total += s['cajones'] * s['precio']

    return total
