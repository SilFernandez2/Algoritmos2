class Calculadora:
    def __init__(self, x : int, y : int) -> None:
        self.x = x
        self.y = y
    
    def suma(self) -> None:
        return self.x + self.y
    def resta(self )-> None:
        return self.x - self.y
    def multiplicacion(self) -> None:
        return self.x * self.y
    def division(self) -> None:
        if self.y !=0:
           return self.x/self.y
        else:
            return "Error: División por cero no permitida."
# Crear una instancia de la clase Calculadora
calc = Calculadora(10, 5)

# Probar los métodos de la clase
print(f"Suma: {calc.suma()}")
print(f"Resta: {calc.resta()}")
print(f"Multiplicación: {calc.multiplicacion()}")
print(f"División: {calc.division()}")