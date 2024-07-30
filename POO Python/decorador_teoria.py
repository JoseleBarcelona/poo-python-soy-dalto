def decorador(funcion): #Le pasamos por parámetro una función
    def funcion_interna():
        print("Decorador antes de llamar a la función...")
        funcion() #Llamamos a la función que queremos decorar
        print("Decorador después de llamar a la función...")
    return funcion_interna

def saludo():
    print("Hola tu que ase")

variable_funcion = decorador(saludo) #Convierto una función en una variable función
variable_funcion() #Al tener una variable función, puedo llamar a la función desde la variable con ().
