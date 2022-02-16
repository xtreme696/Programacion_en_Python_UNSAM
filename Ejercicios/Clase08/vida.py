# vida.py

from datetime import datetime

def segundos_vividos(string_time):
    nacimiento = datetime.strptime(string_time, '%d/%m/%Y')
    fecha_actual = datetime.now()
    diff = (fecha_actual - nacimiento).total_seconds()
    
    return diff


def vida_en_segundos(string_time):
    nacimiento = datetime.strptime(string_time, '%d/%m/%Y')
    fecha_actual = datetime.now()
    diff = (fecha_actual - nacimiento).total_seconds()
    
    return diff
