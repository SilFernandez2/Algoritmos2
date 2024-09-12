class Rectangulo:
    def __init__(self, base : float, altura : float) -> None:
        self.base = base
        self.altura = altura
  
    def area(self) -> None:
        area = self.base * self.altura
        print(f"El area del rectangulo es: {area}  m².")

    
    def perimetro(self) -> None:
        perimetro = (self.base + self.altura) * 2
        print(f"El perimetro del rectangulo es: {perimetro} m.")
#crear una instancia de la clase
rectangulo1 = Rectangulo(2,3)
# Probar los métodos de la clase
rectangulo1.area()
rectangulo1.perimetro()