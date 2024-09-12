# En este ejercicio se pide calcular el producto de dos numeros enteros utilizando recursion de cola
# cuando multipico axb  estoy sumando repetidamente a tantas veces b me pide

def producto( a: int, b: int) -> int:
    def producto_interno( n: int, m: int, acum: int = 0) -> int:
        if n == 0 or m == 0:
            return acum
        else: 
            return producto_interno(n , m - 1, acum + n) # sumo repetidamente a n tantas veces sea m, hasta que llega al paso base
        
        # salvo el resultado si uno de los dos es negativo
    if b < 0:
        return -producto_interno(a, -b)
    else:
        return producto_interno(a, b)
    
a = 5
b = -2

resultado = producto(a, b)
print(resultado)

        