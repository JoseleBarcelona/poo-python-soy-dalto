class Automovil:
    def __init__(self):
        self.__estado = "apagado"

    def __encender(self):
        self.__estado = "encendido"
        print("Encendemos el coche")

    def __conducir(self):
        if self.__estado == "apagado":
            self.__encender()
        print("El coche está en movimiento")

    def get_conducir(self):
        return self.__conducir()

auto = Automovil()
auto.get_conducir()
#Llamamos al método conducir, abstrayendonos de lo que tiene que hacer el auto para arrancar en caso de que esté apagado.
