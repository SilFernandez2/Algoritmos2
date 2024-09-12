class Vehiculo:
    def __init__(self, color) -> None:
        self.color = color
    def info(self) -> None:
        print(f"Color: {self.color}")
class Coche(Vehiculo) :
    def __init__(self,color, marca) -> None:
        super().__init__(color)
        self.marca = marca
    def info(self) -> None:
        super().info()
        print(f" Marca: {self.marca}")
coche = Coche("Rojo", "Toyota")
coche.info()