class MiClase:
    def __init__(self):
        self.__atributo_privado = "Este es el valor del atributo"   #Con dos guiones bajos, le decimos a python que el atributo es privado
                                            # y para acceder al él, tiene que ser con getters y setters.

    def get_atributo(self): #Esto es un getter. Puedo acceder al valor del atributo encapsulado a través de este método,
                            #siempre y cuando el método esté dentro de la clase donde se encuentra el atributo.
        return self.__atributo_privado
    
    def __hablar(self):        #También podemos hacer métodos encapsulados (privados)
        return "Estoy hablando"

    def get_hablar(self):      #Necesitamos este getter para acceder al método encapsulado __hablar().
        return self.__hablar()

objeto = MiClase()
print(objeto.get_atributo())

# print(objeto.__atributo_privado()) La forma convencional da error porque el atributo está encapsulado (privado)

print(objeto.get_hablar())