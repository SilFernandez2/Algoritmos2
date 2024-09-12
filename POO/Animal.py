from abc import ABC
class Animal(ABC):
    def hablar(self)-> None:
        pass
class Perro(Animal):
    def hablar(self) -> None:
        return "Guau"
class Gato(Animal):
    def hablar(self) -> None:
        return "Miauu"
class Pajaro(Animal):
    def hablar(self) -> None:
        return "Pio pio"
perro = Perro()
gato = Gato()
pajarito = Pajaro()
print( "El perro hace", perro.hablar())
print("El gato hace ", gato.hablar())
print("El pajato hace", pajarito.hablar())