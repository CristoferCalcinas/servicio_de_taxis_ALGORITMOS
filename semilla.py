from usuario import Usuario
from chofer import Chofer
from administrador import Administrador


class Semilla:
    def cargar_usuarios(self):
        primer_usuario = Usuario("Juan")
        segundo_usuario = Usuario("Nico")
        tercer_usuario = Usuario("Leon")
        cuarto_usuario = Usuario("Jose")
        return [primer_usuario, segundo_usuario, tercer_usuario, cuarto_usuario]

    def cargar_choferes(self):
        primer_chofer = Chofer("Carlos", 4545)
        segundo_chofer = Chofer("Pablo", 5200)
        segundo_chofer.cambiar_estado()
        tercer_chofer = Chofer("Lucas", 1000)
        cuarto_chofer = Chofer("Martin", 7880)
        cuarto_chofer.cambiar_estado()
        quinto_chofer = Chofer("Mateo", 2020)
        return [
            primer_chofer,
            segundo_chofer,
            tercer_chofer,
            cuarto_chofer,
            quinto_chofer,
        ]

    def cargar_administradores(self):
        primer_administrador = Administrador("Darling")
        return [primer_administrador]


# if __name__ == "__main__":
#     semilla = Semilla()
#     user1 = semilla.cargar_usuarios()
#     user2 = semilla.cargar_choferes()
#     user3 = semilla.cargar_administradores()
#     print("Semilla cargada correctamente")
#     print(user1)
#     print(user2)
#     print(user3)
