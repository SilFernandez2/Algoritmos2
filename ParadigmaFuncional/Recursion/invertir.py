# Ejercicio 7- a) Implementa una función que invierta una
# cadena utilizando recursión de cola
# b) ahora con iteracion 
# def invertir_numero(n: int, invertido: int = 0) -> int:
#     # Caso base: cuando n es 0, retorna el número invertido acumulado
#     if n == 0:
#         return invertido
#     else:
#         # Toma el último dígito de n y lo añade al número invertido
#         invertido = invertido * 10 + n % 10
#         # Llama recursivamente eliminando el último dígito de n
#         return invertir_numero(n // 10, invertido)

# a)
# def invertir_cadena( a : str) -> str:
#     def invertir_cadena_(b : str, palabra : str = "") -> str:
#         if not b:
#             return palabra
#         else:
#             palabra_nueva = b[0] + palabra 
#             return(invertir_cadena_(b[1:], palabra_nueva))
#     return invertir_cadena_(a)
# print(invertir_cadena("Hola"))  # Debería devolver "aloH"

# #b)
def invertir_cadena_iterativa( a : str) -> str:
        palabra_invertida = ""
        for i in a:
             palabra_invertida = i + palabra_invertida
        return palabra_invertida
print(invertir_cadena_iterativa("Hola"))  # Debería devolver "aloH"