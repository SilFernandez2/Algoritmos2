class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
    
    def cumpleaños(self) :
        self.edad += 1
Juana = Persona("Juana", 23)
Juana.cumpleaños()
print(f"La edad que cumplio {Juana.nombre} fue {Juana.edad}.")