def decorador(funcion):
    def funcion_interna(*args, **kwargs): #Le digo a la función que voy a recibir argumentos indeterminados key words (clave, valor).
        print("El resultado de la potencia es de", end=" ")
        funcion(*args, **kwargs) 
    return funcion_interna

@decorador
def potencia(base, exponente):
    print(pow(base, exponente))

potencia(base=5, exponente=2) #Por ejemplo, la clave es base y el valor es 5.
