altura_inicial = altura_temp = 100    # en metros
rebote = 3/5                          # fracción

max_rebotes = 10                      # cantidad de rebotes solicitada

for i in range(max_rebotes):
    altura_temp *= rebote
    print(i, round(altura_temp, 4))
