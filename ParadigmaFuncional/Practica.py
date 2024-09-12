def func1():
    print('Evalua funcion 1')
    return 1
def func2():
    print('Evalua funcion 2')
    return 2
def sumaRara(x, y):
    print('Evalua funcion externa')
    return x if x == 1 else x + y

sumaRara(func1(), func2())