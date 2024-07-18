
class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print("Has acertado en el verbo")

nombre = input('Dígame su nombre por favor:\n')
edad = input('Dígame su edad por favor:\n')
grado = input('¿En qué grado está?:\n')

objeto = Estudiante(nombre, edad, grado)

print(f'''
    DATOS DEL ESTUDIANTE 
    Su nombre es {objeto.nombre}
    Su edad es {objeto.edad}
    Su grado es {objeto.grado}
''')
while True:
    verbo = input("¿Qué verbo relaciona los estudios?:\n")
    if (verbo.lower() == "estudiar"):
        objeto.estudiar()
        break
    else:
        print("Verbo incorrecto, repita el verbo por favor")

