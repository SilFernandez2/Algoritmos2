from collections.abc import Iterator
import math

def es_primos(n: int) -> bool:
     if n < 2: # descato el 1
        return False
     for i in range(2, int(math.sqrt(n)) + 1): #En cada par (a, b), uno de los divisores a o b es menor o igual a la raíz cuadrada de n, y el otro es mayor o igual a la raíz cuadrada de n.
        if n % i == 0: # operador modulo 
            return False
     return True
 

def generador_primos(limite: int) -> Iterator[int]:
    for numero in range(2, limite + 1):
        if es_primos(numero):
            yield numero

for i in generador_primos(100):
    print(i)