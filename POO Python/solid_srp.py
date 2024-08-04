class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100

    def agregar_combustible(self, cantidad):
        self.combustible = cantidad

    def obtener_combustible(self): #getter
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad

class Auto():
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque

    def mover_auto(self, distancia):
        if self.tanque.obtener_combustible() >= distancia/2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia/2)
        else:
            print("No hay suficiente combustible")

    def obtener_posicion_auto(self):#getter
        return f"Distancia recorrida {self.posicion}km"
        


tanque = TanqueDeCombustible() #creamos un tanque
autito = Auto(tanque) #creamos un auto y le pasamos el tanque como parámetro, para usar los métodos del tanque

print(autito.obtener_posicion_auto())
autito.mover_auto(10)

print(autito.obtener_posicion_auto())
autito.mover_auto(20)

print(autito.obtener_posicion_auto())
autito.mover_auto(60)

print(autito.obtener_posicion_auto())
autito.mover_auto(90)

print(autito.obtener_posicion_auto())
autito.mover_auto(100)

print(autito.obtener_posicion_auto())
autito.mover_auto(100)

'''
Distancia recorrida 0km
Distancia recorrida 10km
Distancia recorrida 30km
Distancia recorrida 90km
Distancia recorrida 180km
No hay suficiente combustible
Distancia recorrida 180km
No hay suficiente combustible

'''