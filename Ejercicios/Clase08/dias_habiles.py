# dias_habiles.py

import datetime as dt

def dias_habiles(inicio, fin, feriados = ['12/10/2020', '23/11/2020', '7/12/2020', '8/12/2020', '25/12/2020']):
    dias = []
    fecha = dt.datetime.strptime(inicio, '%d/%m/%Y')
    fecha_fin = dt.datetime.strptime(fin, '%d/%m/%Y')
    
    while fecha <= fecha_fin:
        fecha_str = fecha.strftime('%m/%d/%Y')
        if fecha_str not in feriados and fecha.weekday() < 5:
            dias.append(fecha_str)
            
        fecha += dt.timedelta(days=1)
    
    return dias
