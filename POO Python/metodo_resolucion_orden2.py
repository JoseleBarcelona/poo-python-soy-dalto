class A:
    def hablar(self):
        print("Hola desde A")

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

d = D()
d.hablar()
print(D.mro())

'''
Hola desde A
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

'''
