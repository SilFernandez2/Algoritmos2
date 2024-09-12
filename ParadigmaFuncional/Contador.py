
#Funcion impura, cada vez que la uso se modifica la variable global con_
#tador.
contador = 0

def incrementar():
    global contador
    contador += 1
    return contador

print(incrementar()) # contador = 1
print(incrementar()) # contador  = 2
