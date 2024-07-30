def decorador(funcion): 
    def funcion_interna(*args): #Le decimos a la función que va a recibir un número indeterminado de parámetros
        print("El resultado de la", end=" ")#end= "" le dice a python que concatene en la misma linea lo que sigua detrás.
        funcion(*args) 
    return funcion_interna

a= int(input("Dime el valor de a\n"))
b= int(input("Dime el valor de b\n"))

@decorador
def suma(a,b):
    print("suma de (a+b) es", a+b)

@decorador
def resta(a,b):
    print("resta de (a-b) es", a-b)

suma(a,b)
resta(a,b)
