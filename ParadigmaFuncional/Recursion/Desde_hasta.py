# la funcion tiene que ser recursiva de cola, es decir tiene que tener un acumulador y se tiene 
# que armar de arriba hacia abajo
#recibe un entero a que es el inicio y un entero b que es el fin, donde los intermedios seran los consecutivos
# desde a hacia b


def desde_hasta( a : int, b : int) -> list[int]:

    def helper_(ini : int, fin : int, acum : list[int]) -> list[int]:
        if abs(fin) < abs(ini):
            return acum
        else:
            return helper_(ini + 1, fin, acum + [ini])
    return helper_(a, b, [])

print(desde_hasta(1,5))