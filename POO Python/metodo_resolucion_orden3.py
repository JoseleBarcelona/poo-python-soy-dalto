class Animal:
    def comer(self):
        print("El animal está comiendo")

class Ave(Animal):
    def volar(self):
        print("El animal está volando")

class Mamifero(Animal):
    def amamantar(self):
        print("El animal está amamantando")

class Murcielago(Ave, Mamifero):
    pass

murcielago = Murcielago()

murcielago.comer()
murcielago.volar()
murcielago.amamantar()

print(Murcielago.mro())

'''
El animal está comiendo
El animal está volando
El animal está amamantando
[<class '__main__.Murcielago'>, <class '__main__.Ave'>, <class '__main__.Mamifero'>, <class '__main__.Animal'>, <class 'object'>]

'''