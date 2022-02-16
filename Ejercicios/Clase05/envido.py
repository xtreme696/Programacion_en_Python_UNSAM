# 5.4
import random

valores = list(range(1,8)) + list(range(10,13))
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]

def repartir_mano():
    return random.sample(naipes, k = 3)

def envido(mano = repartir_mano()):
    palos = ['oro', 'copa', 'espada', 'basto'] # En caso de que no estuviese declarado previamente
    puntos = 0
    for palo in palos:
        juego = [naipe for naipe in mano if naipe[1] == palo]
        if len(juego) > 1:
            for num in [12,11,10,1,2,3,4,5,6,7]:
                if (num,palo) in mano:
                    mano.remove((num, palo))
                if len(mano) < 3:
                    break
            puntos = 20 + sum([num for num, palo in juego if num < 10])
            break
    return puntos

def prob_envido(puntos, cant_casos):
    envidos = 0
    for i in range(cant_casos):
        mano = envido(repartir_mano())
        if mano == puntos:
            envidos += 1
    prob = envidos / cant_casos
    print(f'La probabilidad de sacar {puntos} es de {prob:.6f}.')