class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    @property #Con este decorador le decimos a la función que implemente un getter
    def nombre(self):
        return self.__nombre
    
    @nombre.setter #Con este decorador le decimos a la función que implemente un setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @nombre.deleter #Con este decorador podemos borrar el valor de un atributo
    def nombre(self):
        del self.__nombre

objeto = Persona("José")
print(objeto.nombre)

objeto.nombre = "Núria" #Cambiamos el valor del atributo encapsulado self__nombre
print(objeto.nombre)

del objeto.nombre #Borramos el valor del atributo encapsulado self__nombre
try:
    print(objeto.nombre) #Lanza un error porque hemos borrado el valor del atributo encapsulado self__nombre
except:
    objeto.nombre = "Neus"
    print(objeto.nombre)
