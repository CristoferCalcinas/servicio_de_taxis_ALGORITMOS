from usuario import Usuario


class Viaje:
    def __init__(self, usuario: Usuario, origen: str, destino: str):
        self.origen: str = origen
        self.destino: str = destino
        self.usuario: Usuario = usuario

    # def solicitar_viaje_usuario(self, usuario: Usuario, origen: str, destino: str):
    #     self.origen = origen
    #     self.destino = destino
    #     self.usuario = usuario

    def obtener_nombre_usuario(self):
        return self.usuario.nombre
