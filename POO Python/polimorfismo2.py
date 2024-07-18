class Perro:
    def sonido(self):
        return "guauuu"

class Gato:
    def sonido(self):
        return "miauuuu"

def hacer_sonido(animal):
    print(animal.sonido())

gato = Gato()
perro = Perro()

hacer_sonido(perro)
hacer_sonido(gato)

print(perro.sonido())
print(gato.sonido())

