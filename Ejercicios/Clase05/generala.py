# 5.1
import random
from collections import Counter

def tirar(dados = 5):
    tirada = []
    for i in range(dados):
        tirada.append(random.randint(1,6)) 
    return tirada

def es_generala(tirada):
    
    if len(tirada) == 5 and tirada[0] == tirada[1] == tirada[2] == tirada[3] == tirada[4]:
        return True
    return False

def prob_generala_servida(N):
    G = sum([es_generala(tirar()) for i in range(N)])
    prob = G/N
    # print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
    print(f'Podemos estimar la probabilidad de sacar generala mediante {prob:.6f}.')# N = 1000000


#%% 5.2

def jugada(tira_todo = 0):
    jugada = tirar()
    for turno in range(2):
        guardado = dict(zip(["num", "cant"], Counter(jugada).most_common(1)[0]))
        for dado in jugada:
            if dado != guardado['num']:
                jugada.remove(dado)
        jugada += tirar(5 - len(jugada))
    
    return jugada

def prob_generala(N):
    G = sum([es_generala(jugada()) for i in range(N)])
    prob = G/N
    print(f'Podemos estimar la probabilidad de sacar generala mediante {prob:.6f}.')