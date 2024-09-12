# Ahora voy a armar la funcion duplicar pura, esta me realiza una copia de la 
# lista original para que no se pierda la informacion 

def duplicar_pura( lista : list[int]) -> list[int]:
    nueva_lista = lista.copy()
    nueva_lista[-1] *= 2
    return nueva_lista

mi_lista = [1, 2, 3]
mi_nueva_lista = duplicar_pura(mi_lista)
print(mi_lista)
print(mi_nueva_lista)
print(mi_lista)
