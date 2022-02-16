# listar_imgs.py
import sys
import os


def archivos_png(directorio):
    '''Dado un directorio relativo,
    devuelve la lista de archivos .png en el árbol de subdirectorios'''
    return [name for name in os.listdir(directorio) if '.png' in name]


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(archivos_png(sys.argv[1]))
    else:
        print(archivos_png(os.getcwd()))
