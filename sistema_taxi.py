import os
from viaje import Viaje
from menus import Menu
from usuario import Usuario


class SistemaTaxi:
    def __init__(self):
        self.__usuarios = []
        self.__choferes = []
        self.__solicitudes = []

    def pedir_origen_destino(self):
        origen_viaje = input("Ingrese el origen del viaje: ")
        destino_viaje = input("Ingrese el destino del viaje: ")
        return origen_viaje, destino_viaje

    def ingresar_como_usuario(self):
        nombre_usuario = input("Ingrese su nombre para continuar\n=>")
        if not self.__usuarios or nombre_usuario not in [
            usuario.nombre for usuario in self.__usuarios
        ]:
            while True:
                opcion_usuario = Menu().obtener_opcion_menu_usuario()
                print("\n\n")
                while opcion_usuario not in ["1", "2", "3", "4", "5"]:
                    print("La opción ingresada no es válida.")
                    opcion_usuario = Menu().obtener_opcion_menu_usuario()

                if opcion_usuario == "1":
                    # Solicitar un Viaje
                    origen_viaje, destino_viaje = self.pedir_origen_destino()
                    usuario = Usuario(nombre_usuario)
                    self.__usuarios.append(usuario)
                    viaje = Viaje(usuario, origen_viaje, destino_viaje)
                    self.__solicitudes.append(viaje)
                    print("\nSolicitud de viaje realizada con éxito.")
                    input("Presione Enter para continuar...")
                elif opcion_usuario == "2":
                    # Cancelar un Viaje
                    pass
                elif opcion_usuario == "3":
                    pass
                elif opcion_usuario == "4":
                    pass
                elif opcion_usuario == "5":
                    return
        else:
            for i, usuario in enumerate(self.__usuarios):
                if usuario.nombre == nombre_usuario:
                    print(
                        f"Bienvenido {nombre_usuario}, posición en la lista_enlazada: {i+1}"
                    )
                    break
            input("Presione Enter para continuar...")

    def ingresar_como_chofer(self):
        opcion_chofer = Menu().obtener_opcion_menu_chofer()
        print("\n\n")
        if opcion_chofer == "1":
            if not self.__solicitudes:
                print("No hay solicitudes de viaje pendientes.")
                input("Presione Enter para salir...")
                return

            print("Solicitudes de viaje pendientes: ")
            for solicitud in self.__solicitudes:
                print("\n")
                print("*" * 50)
                print(
                    f"*   Origen: {solicitud.origen}, Destino: {solicitud.destino}, Usuario: {solicitud.obtener_nombre_usuario()}   *"
                )
                print("*" * 50, "\n")
            input("Presione Enter para continuar...")

        elif opcion_chofer == "2":
            pass
        elif opcion_chofer == "3":
            pass
        elif opcion_chofer == "4":
            pass
        elif opcion_chofer == "5":
            return

    def ingresar_como_administrador(self):
        opcion_administrador = Menu().obtener_opcion_menu_administrador()
        print(opcion_administrador)
