class A:
    def hablar(self):
        print("Hola desde A")

class B(A):
    def hablar(self):
        print("Hola desde B")

class C(A):
    def hablar(self):
        print("Hola desde C")

class D(B,C):
    def hablar(self):
        print("Hola desde D")

d = D()
d.hablar()

print(D.mro()) #D.mro() nos dice el orden en que python va a ir buscando métodos por las clases heredadas de la clase D.

'''
Hola desde D
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

'''
C.hablar(d) #Hola desde C

'''
Si quiero ejecutar un método de una clase específica, llamo al método de la clase y le paso el objeto de la clase
que más herencias tiene, para así poder acceder a los métodos de todas las clases heredadas que están por encima.

'''


