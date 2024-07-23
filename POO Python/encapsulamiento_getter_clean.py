class MiClase:
    def __init__(self):
        self.__atributo_privado = "Este es el valor del atributo"   

    def get_atributo(self):
        return self.__atributo_privado
    
    def __hablar(self):        
        return "Estoy hablando"

    def get_hablar(self):     
        return self.__hablar()

objeto = MiClase()
print(objeto.get_atributo())
print(objeto.get_hablar())