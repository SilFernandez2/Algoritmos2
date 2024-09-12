from typing import Generic, TypeVar, Optional, TypeAlias
from copy import copy

T = TypeVar('T')
ListaGenerica: TypeAlias = "Lista[T]"

class Nodo(Generic[T]):
    def __init__(self, dato: T, sig: Optional[ListaGenerica] = None):
        self.dato = dato
        if sig is None:
            self.sig= Lista()
        else:
            self.sig = sig

class Lista(Generic[T]):
    def __init__(self):
        self._head: Optional[Nodo[T]] = None

    def es_vacia(self) -> bool:
        return self._head is None

    def head(self) -> T:
        if self.es_vacia():
            raise IndexError('lista vacia')
        else:
            return self._head.dato

    
        
    def tail(self) -> ListaGenerica:
        if self.es_vacia():
            raise IndexError('lista vacia')
        else:
            return self._head.sig.copy()

    def insertar(self, dato: T):
        actual = copy(self)
        self._head = Nodo(dato, actual)

    def eliminar(self, valor: T):
        def _eliminar_interna(actual: ListaGenerica, previo: ListaGenerica, valor: T):
            if not actual.es_vacia():
                if actual.head() == valor:
                    previo._head.sig = actual._head.sig
                else:
                    _eliminar_interna(actual._head.sig, actual, valor)

        if not self.es_vacia():
            if self.head() == valor:
                self._head = self._head.sig._head
            else:
                _eliminar_interna(self._head.sig, self, valor)
                
#  añado len para poder obtener ultimo 

    def __len__(self)  -> ListaGenerica:
        if self.es_vacia():
            return 0
        else:
           return 1 + self.tail().__len__()

    def __getitem__(self, index = None):
        
        if index == None: 
            raise IndexError("No hay un index")
        
        elif self._head is not None:
            print( index, self._head.dato )
            
            if index == 0:
              return self._head.dato      
            else:
             return self.tail().__getitem__(index = index -1)
        else:
             raise IndexError("Te pasaste del largo de la lista")
    
    def index(self, valor: T) -> int:
      if self.es_vacia():
        raise ValueError(f'{valor} no está en la lista')
      if valor == self._head.dato:  # Corregido aquí
        return 0
      else:
        return 1 + self.tail().index(valor)

    def ultimo(self) -> T:
        
     if self.es_vacia():
        raise IndexError("Lista vacía")
    
     if self._head.sig.es_vacia():
        return self._head.dato
     else:
        return self.tail().ultimo()
        

    def concat(self, ys: ListaGenerica) -> ListaGenerica:
        if self.es_vacia():
            return ys
        elif self._head is not None:
            actual = self.copy() #  copia de la lista A
            if self._head.sig is not None:
                actual._head.sig = self._head.sig.concat(ys)
            else:
                actual.head.sig = ys
            return actual
            
            
        
    def join(self, separador: str = '') -> str:
        if self.es_vacia():
            raise ValueError(" La lista esta vacia ")
        
        elif self._head.sig.es_vacia():
            #entra en este caso cuándo tiene  un elemento , si el siguiente si vacio (no hay más elem en la lista) ya retorna la lista
            return str(self._head.dato)
        else:
             #entra en este caso si las lista tiene más de un elemento 
             #str(self._head.dato) tomo la cabeza de la lista concateno el separador
             #self._head.sig.join(separador)agarro el siguiente del head y vuelvo a entrar en la recursión
             return str(self._head.dato) + separador + self._head.sig.join(separador)
        
        
   
            
        
    def existe(self, valor: T) -> bool:
     if self.es_vacia():
        return False
     
     elif self._head.dato == valor:  # Asegúrate de comparar con self._head.dato
        return True
     else: 
        return self._head.sig.existe(valor)  # Agrega return aquí

   
    def __hash__(self) -> int:
      if self.es_vacia(): # nuevamente si la lista es vacia me tiene que retornar 0
        return 0
      else: # sino calculo el valor hash del nodoo actual y se combina con operador XOR el valor (bit) hash de la lista 
             return hash(self.head()) ^ hash(self._head.sig)
  ## al finalizar me realiza la combinacion de bits de los valores de la lista y los retorna     

    def __eq__(self, otra: ListaGenerica) -> bool:
     if not isinstance(otra, Lista):  # Corregido aquí
        return False
    
     actual = self

     while not actual.es_vacia() and not otra.es_vacia():
        if actual.head() != otra.head():
            return False
        actual = actual._head.sig
        otra = otra._head.sig
     return actual.es_vacia() and otra.es_vacia()

     # return isinstance(otro, Persona) and self.nombre == otro.nombre and self.edad == otro.edad
   
    def __repr__(self) -> str:
        elementos = []
        actual = self
        while not actual.es_vacia():
            elementos.append(repr(actual.head()))
            actual = actual._head.sig

        return f'[{", ".join(elementos)}]'


if __name__ == '__main__':
    xs: Lista[int] = Lista()
    
    print(f'xs es vacia? {xs.es_vacia()}')	# True
    
    # Operaciones basicas
    xs.insertar(4)
    xs.insertar(10)
    xs.insertar(20)
    ys: Lista[int] = xs.tail()
    ys.insertar(9)
    ys.eliminar(10)
    ys.insertar(8)
    zs: Lista[int] = ys.copy()
    zs.eliminar(8)
    zs.eliminar(9)
    
    print(f'xs: {xs}')						# [20, 10, 4]
    print(f'ys: {ys}')						# [8, 9, 4]
    print(f'xs es vacia? {xs.es_vacia()}')	# False
    print(f'ultimo(xs): {xs.ultimo()}')		# 4
    print(f'len(xs): {len(ys)}')			# 3, ver __len__
    print(f'xs[1]: {xs[1]}')				# 10, ver __getitem__

    # Consumiendo como iterable
    for x in xs:
        print(x)	# 20 -> 10 -> 4

    # Otras operaciones
    print(f'xs.concat(ys): {xs.concat(ys)}')		# [20, 10, 4, 8, 9, 4]
    print(f'ys.join(" -> "): {ys.join(" -> ")}')	# 8 -> 9 -> 4
    print(f'xs.index(4): {xs.index(4)}')			# 2
    print(f'xs.existe(10): {xs.existe(10)}')        # True
    print(f'xs == zs? {xs == zs}')                  # False
    zs.insertar(10)
    zs.insertar(20)
    print(f'xs == zs? {xs == zs}')                  # True
    