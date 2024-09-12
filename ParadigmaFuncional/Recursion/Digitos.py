#digitos es recursiva, dependiendo n entero me retorna sus digitos
def digitos(n : int) -> int:
    if n < 10:
        return 1
    else:
        return 1 + digitos(n // 10)
    
print(digitos(6))
print(digitos(64))
print(digitos(67776))
print(digitos(0000))