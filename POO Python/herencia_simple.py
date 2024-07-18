class Padre:
    def __init__(self,nombre):
        self.nombre = nombre

    def llamar(self):
        print("Hola que ase")

class Hija(Padre):
    def __init__(self,nombre,apellido):
        super().__init__(nombre)
        self.apellido = apellido

objeto_padre = Padre("José")
objeto_hija = Hija("Neus","Guerrero")

objeto_padre.llamar()
objeto_hija.llamar()

print(f"{objeto_padre.nombre}")
print(f"{objeto_hija.nombre} {objeto_hija.apellido}")

