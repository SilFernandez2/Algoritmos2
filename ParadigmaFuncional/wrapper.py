# wrapper que reciba por parámetro a otra función f sin argumentos,
#  la ejecute e imprima en pantalla el mensaje de ejecución: "Ejecutada f()".

from collections.abc import Callable
from typing import Any

def f(*args: Any, **kwargs: Any) -> str:
    return f"Argumentos posicionales: {args}, Argumentos con nombre: {kwargs}"

def wrapper(f: Callable[..., str], *args: Any, **kwargs: Any) -> str:

    resultado = f(*args, **kwargs)
    return f"Ejecutada f(): {resultado}"


print(wrapper(f, 'arg1', 'arg2', key1='valor1', key2='valor2'))
