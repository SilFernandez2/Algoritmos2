#En este ejercicio se pide implementar Fibonacci pero con recursion de cola, es decir con contadores
# Fibonacci lo que hace es generar una secuencia de numeros donde cada numero es la suma de los anteriores
# Caso base:
# F(0) = 0
# F(1) = 1
# Relación recursiva:
# F(n) = F(n-1) + F(n-2) para n > 1
def figonacci_recursivo(n : int, b : int = 0, c : int = 1) -> int:
    if n == 0:
        return b
    elif n == 1:
        return c
    else:
        return figonacci_recursivo(n-1, c, b + c )
    
n = 10
prueba = figonacci_recursivo(n)
print(prueba)