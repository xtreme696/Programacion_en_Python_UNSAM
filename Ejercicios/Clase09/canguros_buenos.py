# canguros_buenos.py

class Canguro:
    def __init__(self, nombre, lista = []):
        self.nombre = nombre
        self.contenido_marsupio = lista.copy()
    
    def __str__(self):
        t = [f'{self.nombre} tiene en su marsupio:']
        t += [object.__str__(obj) for obj in self.contenido_marsupio]
        
        return '\n    '.join(t)
        
    def meter_en_marsupio(self, obj):
        self.contenido_marsupio.append(obj)


#%% canguro_malo.py
# """Este código continene un 
# bug importante y dificil de ver
# """

# class Canguro:
#     """Un Canguro es un marsupial."""
    
#     def __init__(self, nombre, contenido=[]):
#         """Inicializar los contenidos del marsupio.

#         nombre: string
#         contenido: contenido inicial del marsupio, lista.
#         """
#         self.nombre = nombre
#         # self.contenido_marsupio = contenido
#         # ERROR: al vincular la variable contenido en cada instancia,
#         # cualquier modificación impacta en todas de igual manera
#         self.contenido_marsupio = contenido.copy() # FIX


#     def __str__(self):
#         """devuelve una representación como cadena de este Canguro.
#         """
#         t = [ self.nombre + ' tiene en su marsupio:' ]
#         for obj in self.contenido_marsupio:
#             s = '    ' + object.__str__(obj)
#             t.append(s)
#         return '\n'.join(t)

#     def meter_en_marsupio(self, item):
#         """Agrega un nuevo item al marsupio.

#         item: objecto a ser agregado
#         """
#         self.contenido_marsupio.append(item)