# 2.14
palabras = ['banana', 'manzana', 'mandarina']

def geringoso(cadena):
    capadepenapa = ''
    for c in cadena:
        capadepenapa += c
        if c in 'aeiou':
            capadepenapa += 'p' + c
    return capadepenapa

def diccionario_geringoso(lista):
    papalapabrapas = {}
    for palabra in lista:
        papalapabrapas[palabra] = geringoso(palabra)
    return papalapabrapas

print(diccionario_geringoso(palabras))
