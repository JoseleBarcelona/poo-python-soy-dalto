class Usuario:
    def __init__(self, email):
        self.email = email

class Notificador:
    def __init__(self, usuario):
        self.usuario = usuario

    def notificar(self):
        raise NotImplementedError

class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por mail a {self.usuario.email}")

# Ejemplo de uso:
usuario = Usuario("ejemplo@correo.com")
notificador = NotificadorEmail(usuario)
notificador.notificar()
