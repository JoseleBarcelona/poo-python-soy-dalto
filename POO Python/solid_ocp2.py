# Definición de la clase Usuario
class Usuario:
    def __init__(self, email, sms, whatsapp):
        self.email = email
        self.sms = sms
        self.whatsapp = whatsapp

# Clases de notificación
class Notificador:
    def __init__(self, usuario):
        self.usuario = usuario

    def notificar(self):
        raise NotImplementedError

class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por email a {self.usuario.email}")

class NotificadorSMS(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por SMS a {self.usuario.sms}")

class NotificadorWhatsapp(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por whatsapp a {self.usuario.whatsapp}")

# Crear una instancia de Usuario
usuario = Usuario(email="usuario@example.com", sms="123456789", whatsapp="987654321")

# Crear instancias de las clases Notificador y llamar al método notificar
notificador_email = NotificadorEmail(usuario)
notificador_sms = NotificadorSMS(usuario)
notificador_whatsapp = NotificadorWhatsapp(usuario)

# Notificar usando los diferentes métodos
notificador_email.notificar()
notificador_sms.notificar()
notificador_whatsapp.notificar()


'''
Clases y Objetos

    Clase Usuario:
        Define una estructura para almacenar la información de un usuario, que incluye su email, número de SMS y número de WhatsApp.
        Cuando creas una instancia de Usuario, estás creando un objeto que contiene estos datos.

    Clase Notificador (y sus subclases):
        Notificador es una clase base abstracta que define una interfaz común para las notificaciones.
        Las subclases (NotificadorEmail, NotificadorSMS, NotificadorWhatsapp) implementan el método notificar específico para cada tipo de notificación.
        Al crear una instancia de una de estas subclases, se pasa un objeto Usuario a su constructor.

Pasar una instancia como parámetro

Cuando pasas una instancia de Usuario como parámetro al constructor de una subclase de Notificador, estás estableciendo una relación entre ese objeto Usuario y el notificador.
Explicación paso a paso

    Definición de la clase Usuario:

    python

class Usuario:
    def __init__(self, email, sms, whatsapp):
        self.email = email
        self.sms = sms
        self.whatsapp = whatsapp

Aquí defines una clase Usuario con un constructor que inicializa los atributos email, sms, y whatsapp.

Creación de una instancia de Usuario:

python

usuario = Usuario(email="usuario@example.com", sms="123456789", whatsapp="987654321")

Creas un objeto usuario de la clase Usuario con los datos de contacto del usuario.

Definición de la clase base Notificador:

python

class Notificador:
    def __init__(self, usuario):
        self.usuario = usuario

    def notificar(self):
        raise NotImplementedError

Aquí defines la clase Notificador con un constructor que acepta un objeto Usuario y lo almacena en el atributo self.usuario. El método notificar es abstracto y debe ser implementado por las subclases.

Definición de las subclases de Notificador:

python

class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por email a {self.usuario.email}")

class NotificadorSMS(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por SMS a {self.usuario.sms}")

class NotificadorWhatsapp(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por whatsapp a {self.usuario.whatsapp}")

Cada subclase de Notificador implementa el método notificar, utilizando el objeto Usuario pasado al constructor para acceder a los datos específicos de contacto.

Creación de instancias de las subclases de Notificador:

python

notificador_email = NotificadorEmail(usuario)
notificador_sms = NotificadorSMS(usuario)
notificador_whatsapp = NotificadorWhatsapp(usuario)

Aquí creas instancias de NotificadorEmail, NotificadorSMS, y NotificadorWhatsapp, pasando el objeto usuario como argumento. Cada instancia almacena una referencia a este objeto usuario.

Uso del método notificar:

python

    notificador_email.notificar()
    notificador_sms.notificar()
    notificador_whatsapp.notificar()

    Cuando llamas al método notificar en cada instancia, se accede a los atributos del objeto usuario a través del atributo self.usuario que se estableció en el constructor. Esto permite que cada notificador utilice los datos de contacto correspondientes para enviar el mensaje.

Resumen

    Al pasar una instancia de Usuario como parámetro a las subclases de Notificador, estás permitiendo que estas subclases accedan a los datos de contacto del usuario.
    El constructor de Notificador almacena una referencia a esta instancia, y las subclases usan esta referencia para acceder a los atributos específicos (email, sms, whatsapp) y enviar la notificación correspondiente.

Este enfoque permite reutilizar la lógica de acceso a los datos del usuario en diferentes tipos de notificadores, siguiendo el principio de herencia y polimorfismo en la programación orientada a objetos.

'''