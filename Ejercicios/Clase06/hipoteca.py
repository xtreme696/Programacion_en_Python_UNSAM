# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 1

pago_extra_primeros_12 = False # Considerar el primer año con extra de la consigna 1.8

pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    saldo *= 1 + tasa / 12 # Aplican tasas

    pago_del_mes = pago_mensual
    if (mes <= 12 and pago_extra_primeros_12) or (mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin):
        pago_del_mes += pago_extra
    if saldo < pago_del_mes:
        pago_del_mes = saldo

    # Actualiza los montos
    saldo -= pago_del_mes
    total_pagado += pago_del_mes

    print(mes, round(total_pagado, 2), round(saldo, 2))

    mes += 1

print('Total pagado:',  round(total_pagado, 2))
print('Meses:',  mes - 1)
