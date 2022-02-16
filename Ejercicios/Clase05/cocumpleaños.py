# 5.3
import random

def cocumple(personas = 30):
    fechas = []
    for i in range(personas):
        cumple_el_dia = random.randint(1,365)
        if cumple_el_dia in fechas:
            return True
        fechas += [cumple_el_dia]
    return False

def prob_cocumple(N):
    prob = sum([cocumple() for i in range(N)])/N
    print(f'Podemos estimar la probabilidad de cocumpleaños mediante {prob:.6f}.')
    
def hacen_falta():
    personas = 2
    while not cocumple(personas):
        personas += 1
    return personas

def mas_prob_cocumple(N):
    prob = sum([hacen_falta() for i in range(N)])/N
    print(f'Es más probable que exista cocumpleaños en un grupo de +{int(prob)} personas.')
