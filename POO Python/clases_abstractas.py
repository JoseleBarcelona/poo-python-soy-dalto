from abc import ABC, abstractmethod 
#ABC es la clase abstracta de python y abstractmethod se usa para decir qué función va a ser un método abstracto
#Una clase abstracta obliga a que la clase que la herede, tenga que implementar sus métodos y atributos abstractos

class Persona(ABC): #Con ABC decimos que esta clase va a ser abstracta (Plantilla para otras clases, como una interfaz en Java)

    @abstractmethod #Esto es un decorador para hacer el método abstracto
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractmethod
    def hacer_actividad(self):
        pass
    
    @abstractmethod
    def sexo_persona(self):
        pass

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Estoy estudiando {self.actividad}")

    def sexo_persona(self):
        print(f"Mi sexo es {self.sexo} ")

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Estoy trabajando en el sector de la {self.actividad}")

    def sexo_persona(self):
        print(f"Mi sexo es {self.sexo}")

jose = Estudiante("José", 52, "masculino", "programación")
nuria = Trabajador("Núria", 52, "femenino", "administración")

jose.presentarse()
jose.hacer_actividad()
jose.sexo_persona()

print("")

nuria.presentarse()
nuria.hacer_actividad()
nuria.sexo_persona()