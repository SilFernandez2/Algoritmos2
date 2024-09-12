class Marino:
    def hablar(self) -> None:
        print( "Hola soy un animal marino")
class Pulpo(Marino):
    def hablar(self) -> None:
        print( "Hola soy un pulpo")
    
#e Foca(), heredada de Marino, pero que tenga un
#atributo nuevo llamado mensaje y que muestre ese mensaje como parámetro

class Foca(Marino):
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje
    def hablar(self) -> None:
        print(self.mensaje)
animal_marino = Marino()
pulpo = Pulpo()
foca = Foca("Hola soy la foca")
animal_marino.hablar()
pulpo.hablar()
foca.hablar()
