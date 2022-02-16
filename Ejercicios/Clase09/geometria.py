# geometria.py

class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'
    
    # Used with `repr()`
    def __repr__(self):
        return f'Punto({self.x}, {self.y})'
    
    def __add__(self, b):
        return Punto(self.x + b.x, self.y + b.y)
  
    def invertir(self):
        puntotemp = self
        self.x = puntotemp.y
        self.y = puntotemp.x


class Rectangulo:
    def __init__(self, punto_1, punto_2):
        self.punto_1 = punto_1
        self.punto_2 = punto_2

    def base(self):
        return abs(self.punto_2.x - self.punto_1.x)

    def altura(self):
        return abs(self.punto_2.y - self.punto_1.y)

    def area(self):
        return self.base() * self.altura()

    def desplazar(self, desplazamiento):
        self.punto_1 += desplazamiento
        self.punto_2 += desplazamiento
        
    def rotar(self):
        self.punto_1.invertir()
        self.punto_2.invertir()
