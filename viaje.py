from usuario import Usuario
from chofer import Chofer


class Viaje:
    def __init__(self, usuario: Usuario, origen: str, destino: str):
        self.origen: str = origen
        self.destino: str = destino
        self.usuario: Usuario = usuario

    def obtener_nombre_usuario(self):
        return self.usuario.nombre


class Viaje_Chofer:
    def __init__(self, viaje: Viaje, chofer: Chofer):
        self.viaje: Viaje = viaje
        self.chofer: Chofer = chofer

    def obtener_nombre_chofer(self):
        return self.chofer.nombre

    def obtener_nombre_usuario(self):
        return self.viaje.obtener_nombre_usuario()
