# costo_camion
import informe_final


def costo_camion(nombre_archivo = '../Data/camion.csv'):
    '''
    Computa el precio total (cantidad * precio) de un archivo camion
    '''
    camion = informe_final.leer_camion(nombre_archivo)
    return camion.precio_total()


def f_principal(argv):
    if len(argv) == 2:
        archivo_py, archivo_camion = argv
        return costo_camion(archivo_camion)
    return False


if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
    