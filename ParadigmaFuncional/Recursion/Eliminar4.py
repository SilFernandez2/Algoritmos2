#Vamos a eliminar recursion, recordando que podemos simplemente usando un acumulador, utilizando una iteracion 
# en vez de una recursion o una pila explicita

#Eliminar la recursión del siguiente código:

   

def longitud_no_recursiva(lista : list[int]) ->  int:
  
  if lista == []:
    return 0
  
  i = 0

  while i <  len(lista):

    i += 1

  return i
    
print(longitud_no_recursiva([10, 20, 30]))