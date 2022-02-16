# camion.py

class Camion:

    def __init__(self, lotes):
        self.lotes = lotes
    
    def __iter__(self):
        return self.lotes.__iter__()
    
    def __contains__(self, nombre):
        return any(lote.nombre == nombre for lote in self.lotes)
    
    def __len__(self):
        return len(self.lotes)
    
    def __getitem__(self, index):
        return self.lotes[index]
    
    def __repr__(self):
        return f'Camion({[l for l in self.lotes]})'
    
    def __str__(self):
        s = f'Camion con {len(self)} lotes:'
        for l in self.lotes:
            s += f'\nLote de {l.cajones} cajones de \'{l.nombre}\', pagados a ${l.precio} cada uno.'
        
        return s
    
    def precio_total(self):
        return sum(l.costo() for l in self.lotes)

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total
    