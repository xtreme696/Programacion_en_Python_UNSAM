# bbin_rec.py

def bbinaria_rec(lista, e):
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2

        if lista[medio] < e:
            return bbinaria_rec(lista[medio:], e)
        elif lista[medio] > e:
            return bbinaria_rec(lista[:medio], e)
        return True

    return res
