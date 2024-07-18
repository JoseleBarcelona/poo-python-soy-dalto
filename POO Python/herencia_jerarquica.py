class Persona:
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def hablar(self):
        print("\nHola, soy el jefe de José Antonio Guerrero")

class Empleado(Persona):
    def __init__(self, nombre, apellidos, edad, trabajo, salario):
        super().__init__(nombre, apellidos, edad)
        self.trabajo = trabajo
        self.salario = salario

class Estudiante(Persona):
    def __init__(self, nombre, apellidos, edad, notas, universidad):
        super().__init__(nombre, apellidos, edad)
        self.notas = notas
        self.universidad = universidad

class Jefe(Persona):
    def __init__(self, nombre, apellidos, edad, empresa, ganancias):
        super().__init__(nombre, apellidos, edad)
        self.empresa = empresa
        self.ganancias = ganancias

    def datos_de_jefe(self):
        print(f'''
    DATOS DEL JEFE
    Nombre: {jefe.nombre}
    Apellidos: {jefe.apellidos}
    Edad: {jefe.edad}
    Empresa: {jefe.empresa}
    Ganancias: {jefe.ganancias}€
    ''')

jefe = Jefe("Juan Carlos", "De la Rosa", 60, "MCM Obres i serveis", 25000000)

jefe.hablar()
jefe.datos_de_jefe()
