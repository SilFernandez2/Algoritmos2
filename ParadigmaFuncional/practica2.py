

funciones = (lambda z: x * 2 + z for x in range(5))
# Los valores se generan solo cuando se solicita.
print(next(funciones)(10))  # Se evalúa el primer valor cuando se solicita.
print(next(funciones)(10))  # Se evalúa el segundo valor cuando se solicita.
print(next(funciones)(20))  # Se evalúa el tercer valor cuando se solicita.
print(next(funciones)(10))  # Se evalúa el cuarto valor cuando se solicita.