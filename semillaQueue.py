from cola import Queue
from usuario import Usuario
from chofer import Chofer
from administrador import Administrador


class QueueSemilla:
    def cargar_usuarios_queue(self):
        primer_usuario = Usuario("Juan")
        segundo_usuario = Usuario("Nico")
        tercer_usuario = Usuario("Leon")
        cuarto_usuario = Usuario("Jose")
        usuarios = Queue()
        usuarios.enqueue(primer_usuario)
        usuarios.enqueue(segundo_usuario)
        usuarios.enqueue(tercer_usuario)
        usuarios.enqueue(cuarto_usuario)
        return usuarios

    def cargar_choferes_disponibles_queue(self):
        primer_chofer = Chofer("Pablo", 5200)
        primer_chofer.cambiar_estado()
        segundo_chofer = Chofer("Martin", 7880)
        segundo_chofer.cambiar_estado()
        choferes = Queue()
        choferes.enqueue(primer_chofer)
        choferes.enqueue(segundo_chofer)
        return choferes

    def cargar_choferes_no_disponibles_queue(self):
        primer_chofer = Chofer("Carlos", 4545)
        segundo_chofer = Chofer("Lucas", 1000)
        tercer_chofer = Chofer("Mateo", 2020)
        choferes = Queue()
        choferes.enqueue(primer_chofer)
        choferes.enqueue(segundo_chofer)
        choferes.enqueue(tercer_chofer)
        return choferes

    def cargar_administradores_queue(self):
        primer_administrador = Administrador("Darling")
        administradores = Queue()
        administradores.enqueue(primer_administrador)
        return administradores
