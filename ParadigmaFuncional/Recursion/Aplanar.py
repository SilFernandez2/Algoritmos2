# DADA UNA LISTA DE ENTEROS RETORNE UNA LISTA DE ENTEROS RETORNE LA CONCATENACION DE LOS ELEMENTOS -LISTA ORIGINAL
# aplanar([[5,7], [], [3,4,5], [9]) = [5,6,7,8,9]

def aplanar(a: list[list[int]])-> list[int]:
   if not a:
      return []
   else:
      return a[0] + aplanar(a[1:])
print(aplanar([[5,7], [], [3,4,5], [9]]))  