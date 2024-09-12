# Implementar una versión con recursión de
# cola que produzca el resultado esperado al
# pasar una lista: `suma_resta_alternada([1, 2,
# 3, 4, 5]) = 1 + 2 - 3 + 4 - 5

# Identar :  Ctrl + K, seguido de Ctrl + F.
# Comentar : Ctrl + K, seguido de Ctrl + C
# Descomentar Ctrl + K, seguido de Ctrl + U


# def suma_resta_alternada(lista: list[int]) -> str:
#     def suma_resta_alternada_interna( a : list[int], b : list[str], acum : str) -> str:
        
#        if not a:
#             return acum
#        #tomo el primer elemento de mi lista a y el primer operador de la lista b cmo acum nuevo
#        nuevo_acum = acum + f" {b[0]} {a[0]}" if acum else f"{a[0]}"

#       #armo mi nuebo b, concatenando los valores str de los lugares
#        nuevo_b = b[1:] + [b[0]]
#        #Llamo recursivamente, hasta completar el alternado 
#        return suma_resta_alternada_interna(a[1:], nuevo_b, nuevo_acum)
    
#     # Llamada inicial a la función interna
#     return suma_resta_alternada_interna(lista[1:], ["+", "-"], f"{lista[0]}")

# print(suma_resta_alternada([1, 2, 3, 4, 5]))

def suma_resta_alternada_no_recursiva(a: list[int]) -> str:
    
        if not a:
             return ""
        
        operadores = ["+" , "-"]
        b_nuevo = operadores
        acum = str(a[0])

        for i in range(1, len(a)):
             acum += f" {b_nuevo[0]} {a[i]}" 
             b_nuevo = b_nuevo[1:] + [b_nuevo[0]]
        return acum
print(suma_resta_alternada_no_recursiva([1, 2, 3, 4, 5]))
             
