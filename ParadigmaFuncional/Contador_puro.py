# ahora voy a poner el parametro contador y que la funcion retorne 
# un nuevo contador incrementado en 1
def incrementar_puro( contador : int) -> int:
    return contador + 1


inicio = 0 # variable global

nuevo_coontador = incrementar_puro(inicio) #ahora inicio no cambia pero si se guarda su cambio en nuevo_contador
print(nuevo_coontador) # ahora nuevo_contador es quien incrementa 

nuevo_coontador = incrementar_puro(nuevo_coontador)
print(nuevo_coontador) # 2