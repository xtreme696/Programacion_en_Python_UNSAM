def buscar_precio(fruta):
    precio = 0
    mensaje = f'{fruta} no figura en el listado de precios'

    with open('../Data/precios.csv') as f:
        for line in f:
            data = line.split(',')
            if data[0].lower() == fruta.lower():
                precio = float(data[1])
                mensaje = f'El precio de lista de {fruta} es: {precio:0.2f}'

    print(mensaje)
