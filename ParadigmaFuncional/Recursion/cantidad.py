# Se pide una funcion con recursion de cola que dada una lista de enteros y un numero n, retorne la cantidad de 
# apariciones del numero n 

def cantidad(a : list[int], n: int) -> int:
    def cnt_busqueda(b: list[int], m: int, i: int, acum : int = 0) -> int:
      if i == len(b):
         return acum
      elif b[i] == m:
         return cnt_busqueda(b, m, i + 1, acum + 1)
      else:
         return cnt_busqueda(b, m,  i + 1, acum)
    return cnt_busqueda(a, n, 0, 0)  # inicio de la recursion 

a = [1, 2, 4, 2, 8]
n = 2
resultado = cantidad(a, n)
print(resultado)
      