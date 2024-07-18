class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca + " Galaxy"
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f"Estás haciendo una llamada telefónica desde un {self.marca}")
    def colgar(self):
        print(f"Estás colgando el teléfono con cámara de resolución {self.camara}")

celular1 = Celular("Samsung", "Xtal", "48Mpx")
celular2 = Celular("Motorola", "h2o", "100Mpx")

print(celular1.marca)
celular2.llamar()
celular1.colgar()

