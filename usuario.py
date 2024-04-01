class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_viajes = []

    def ver_lista_viajes(self):
        return self.lista_viajes
