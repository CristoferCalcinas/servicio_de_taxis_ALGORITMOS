class Chofer:
    def __init__(self, nombre: str, identificacion: int):
        self.nombre: str = nombre
        self.identificacion: int = identificacion
        self.estado: str = "Disponible"

    def cambiar_estado(self):
        return "Ocupado" if self.estado == "Disponible" else "Disponible"

    def identificar_chofer(self, identificacion: int):
        return self.identificacion == identificacion
