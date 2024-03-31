from chofer import Chofer
from usuario import Usuario


class Administrador:
    def __init__(self) -> None:
        self.historial_general = []

    def visualizar_cola_choferes(self):
        pass

    def visualizar_historial_viajes(self):
        pass

    def buscar_viajes_chofer(self, chofer: Chofer):
        pass

    def buscar_viajes_usuario(self, usuario: Usuario):
        pass

    def mostrar_todas_las_solicitudes_de_viaje(self):
        return self.historial_general
