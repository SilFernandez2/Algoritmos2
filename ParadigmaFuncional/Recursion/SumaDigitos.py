#Ejercicio 6- a) Realizar una función recursiva suma_digitos que, dado un número entero, retorne la suma de
#sus dígitos.
# b) Ahora hacerla iterativa 

# def SumaDigitos(n, suma: int = 0)-> int:
#     if n == 0:
#         return suma
#     else:
        
#         suma += n % 10
#         return SumaDigitos(n // 10, suma)
    
# resultado = SumaDigitos(4000)
# print(resultado)
# a)
# def suma_digitos(n : int) -> int:
#    def SumaDigitos(n, suma: int = 0)-> int:
#         if n == 0:
#             return suma
#         else:
            
#             suma += n % 10
#             return SumaDigitos(n // 10, suma)
#    return SumaDigitos(n, 0)

# print(suma_digitos(123))  # 6

#b)
def SumaDigitos_iterativa(a : int) -> int:
   suma = 0
   while a > 0:
        suma += a % 10
        a = a//10
   return suma
print(SumaDigitos_iterativa(123))  # 