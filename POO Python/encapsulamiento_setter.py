class Persona:
    def __init__(self, nombre, edad, oficio):

        #atributos encapsulados __.
        self.__nombre = nombre
        self.__edad = edad
        self.__oficio = oficio

    #getter
    def get_nombre(self):
        return self.__nombre
    
    #getter
    def get_edad(self):
        return self.__edad
    
    #setter
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    #setter
    def set_edad(self, nueva_edad):
        self.__edad = nueva_edad

    #encapsulated method
    def __trabajar(self):
        return f"Trabajo de {self.__oficio}"
    
    #getter
    def get_trabajar(self):
        return self.__trabajar()
    
    #setter
    def set_trabajar(self, nuevo_oficio):
        self.__oficio = nuevo_oficio

objeto = Persona("Josele", 52, "programador")

print(f"Me llamo {objeto.get_nombre()}")
print(f"Tengo {objeto.get_edad()} años")
print(objeto.get_trabajar())

objeto.set_nombre("Núria")
objeto.set_edad(36)
objeto.set_trabajar("recepcionista")

print(f'''\nDATOS DEL EMPLEADO
Nombre: {objeto.get_nombre()}
Edad: {objeto.get_edad()}
Oficio: {objeto.get_trabajar()}
''')

nombre = objeto.get_nombre()
edad = objeto.get_edad()
oficio = objeto.get_trabajar()

print(nombre + "\n" + str(edad) + "\n" + oficio)