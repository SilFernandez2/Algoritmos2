
class ConjuntoInmutable:
    def __init__(self, *elementos):
        self._elementos = tuple(elementos)
    
    @property
    def elementos(self):
        return self._elementos
    
contenedor = ConjuntoInmutable('a', 1, 3, 'b', 5)
print(contenedor.elementos)  
contenedor.elementos[2] = 10         # Error
contenedor.elementos = (1, 3, 'a')   # Error