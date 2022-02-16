# torre_control.py

class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0


class TorreDeControl():
    def __init__(self):
        self.arribos = Cola()
        self.partidas = Cola()
        
    def nuevo_arribo(self, vuelo):
        self.arribos.encolar(vuelo)

    def nueva_partida(self, vuelo):
        self.partidas.encolar(vuelo)
        
    def ver_estado(self):
        print(f'Vuelos esperando para aterrizar: {", ".join(self.arribos.items)}')
        print(f'Vuelos esperando para despegar: {", ".join(self.partidas.items)}')
    
    def asignar_pista(self):
        if not self.arribos.esta_vacia():
            print(f'El vuelo {self.arribos.desencolar()} aterrizó con éxito.')
        elif not self.partidas.esta_vacia():
            print(f'El vuelo {self.partidas.desencolar()} despegó con éxito.')
        else:
            print('No hay vuelos en espera.')
