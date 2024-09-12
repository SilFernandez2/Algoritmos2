# armo una funcion impura que tome una lista de int y al
#  ultimo elemento de la lista  lo duplique

def duplicar_impuro( lista : list[int]) -> None:
       lista[-1] *= 2
       
mi_lista = [1, 2, 3]
duplicar_impuro(mi_lista)
print(mi_lista)
duplicar_impuro(mi_lista)
print(mi_lista)
