# costo_camion
import informe_final

def costo_camion(nombre_archivo = '../Data/camion.csv'):
    'Imprime el costo total de la carga del camión'
    total = float(0)
    camion = informe_final.leer_camion(nombre_archivo)

    for s in camion:
        total += s['cajones'] * s['precio']

    return total


def f_principal(argv):
    if len(argv) == 2:
        archivo_py, archivo_camion = argv
        return costo_camion(archivo_camion)
    return False


if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
    