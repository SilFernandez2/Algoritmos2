# vamos a hacer un quicksort donde tenemos un pivot 
# que vaya dividiendo la lista a la mitad y se compare 
# para retornar la lista ordenada
def quicksort(a : list[int]) -> list[int]:
     
    # Función que realiza la partición
    def pivot(b: list[int], menor: int, mayor: int) -> int:
        piv = b[mayor]  # Elegimos el último elemento como pivote
        i = menor - 1   # Índice del elemento más pequeño
        
        # Recorremos los elementos desde 'menor' hasta 'mayor - 1'
        for j in range(menor, mayor):
            if b[j] <= piv:
                i += 1
                # Intercambiamos elementos si son menores o iguales al pivote
                b[i], b[j] = b[j], b[i]
        
        # Colocamos el pivote en su posición correcta
        b[i + 1], b[mayor] = b[mayor], b[i + 1]
        return i + 1

    def recursion(b: list[int], menor: int, mayor: int):
        if menor < mayor:
            # Obtener la posición correcta del pivote después de la partición
            p = pivot(b, menor, mayor)
            
            # Ordenar recursivamente las sublistas a ambos lados del pivote
            recursion(b, menor, p - 1)
            recursion(b, p + 1, mayor)
    
    # Llamada inicial a la función recursiva
    recursion(a, 0, len(a) - 1)
    return a

lista = [10, 7, 8, 9, 1, 5]
resultado = quicksort(lista)
print(resultado)  # Salida: [1, 5, 7, 8, 9, 10]