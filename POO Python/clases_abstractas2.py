from abc import ABC, abstractmethod
class Persona(ABC):

    @abstractmethod
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

    @abstractmethod
    def hablar(self):
        pass

    @abstractmethod
    def presentarse(self):
        pass

class Estudiante(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def hablar(self):
        print("estoy hablando")

    def presentarse(self):
        print(f"Me llamo {self.nombre} tengo {self.edad} años", end=" y ")

class Trabajador(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def hablar(self):
        print("estoy trabajando")

    def presentarse(self):
        print(f"Me llamo {self.nombre} tengo {self.edad} años", end=" y ")

jose=Estudiante("José", 52)
nuria=Trabajador("Núria", 36)
jose.hablar()
print(f"{jose.nombre}, {jose.edad}")

nuria.hablar()
print(f"{nuria.nombre}, {nuria.edad}\n")

jose.presentarse()
jose.hablar()
nuria.presentarse()
nuria.hablar()