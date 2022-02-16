precio = 0

with open('../Data/precios.csv') as f:
    for line in f:
        data = line.split(',')
        if data[0].lower() == 'naranja':
            precio = float(data[1])

print(f'El precio de la naranja es: {precio:0.2f}')
