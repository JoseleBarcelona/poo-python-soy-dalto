class Persona:
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def hablar(self):
        return "\n¡Escuchad mis palabras!"

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f"mi habilidad es {self.habilidad}"

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, apellidos, edad, habilidad, empresa, salario):
        Persona.__init__(self, nombre, apellidos, edad)
        Artista.__init__(self, habilidad)
        self.empresa = empresa
        self.salario = salario

    def mostrar_habilidad(self):
        return "El coño mi prima"
    
    #super().mostrar_habilidad() llama a los métodos de la clase padre
    #self.mostrar_habilidad() llama al método de su propia clase (Rescribe el método heredado)

    def presentarse(self):
        print(f"Hola soy {self.nombre}, {super().mostrar_habilidad()}, trabajo en {self.empresa} y gano {self.salario}€ al mes") 
        print(f"Hola soy {self.nombre}, {self.mostrar_habilidad()}, trabajo en {self.empresa} y gano {self.salario}€ al mes")

jose = EmpleadoArtista("José", "Guerrero", 52, "programar", "MCM Obres i serveis", 1800)

print(jose.hablar())
jose.presentarse()

#issubclass() te dice si una clase es hija de otra clase, de ser así, devuelve un True.

herencia = issubclass(EmpleadoArtista, Artista)
print(herencia)

# isinstance() te devuelve si un objeto es una instancia de alguna clase.

instancia = isinstance(jose, Artista)
print(instancia)