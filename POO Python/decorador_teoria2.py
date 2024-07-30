def decorador(funcion): #Le pasamos por parámetro una función
    def funcion_interna():
        print("Decorador antes de llamar a la función...")
        funcion() #Llamamos a la función que queremos decorar
        print("Decorador después de llamar a la función...")
    return funcion_interna

@decorador
def saludo():
    print("Hola tu que ase")

saludo()
