from chofer import Chofer
from menus import Menu
from semilla import Semilla
from usuario import Usuario
from viaje import Viaje


class SistemaTaxi:
    def __init__(self):
        self.__usuarios = Semilla().cargar_usuarios()
        self.__choferes = Semilla().cargar_choferes()
        self.__solicitudes = []

    def pedir_origen_destino(self):
        origen_viaje = input("Ingrese el origen del viaje: ")
        destino_viaje = input("Ingrese el destino del viaje: ")
        return origen_viaje, destino_viaje

    def ingresar_como_usuario(self):
        while True:
            nombre_usuario = input("Ingrese su nombre para continuar\n=>")
            for i, solicitud in enumerate(self.__solicitudes):
                if solicitud.obtener_nombre_usuario() == nombre_usuario:
                    print(f"Su Ppsición en la lista_enlazada: {i+1}")
                    print("Ya tiene una solicitud de viaje pendiente.")
                    input("Presione Enter para continuar...")
                    break

            print("\n\n")
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
                    nueva_lista_solicitudes = list(
                        filter(
                            lambda x: x.usuario.nombre != nombre_usuario,
                            self.__solicitudes,
                        )
                    )
                    if len(nueva_lista_solicitudes) == len(self.__solicitudes):
                        print("No hay solicitudes de viaje pendientes.")
                    else:
                        self.__solicitudes = nueva_lista_solicitudes
                        print("Viaje cancelado con éxito.")
                        input("Presione Enter para continuar...")
                        return

                elif opcion_usuario == "3":
                    # Registro de Viajes de un Usuario
                    for i, usuario in enumerate(self.__usuarios):
                        if usuario.nombre == nombre_usuario:
                            print(
                                f"Usuario: {usuario.nombre} - Posición en la lista_enlazada: {i+1}"
                            )
                    input("Presione Enter para continuar...")

                elif opcion_usuario == "4":
                    # Mostrar Viajes
                    for solicitud in self.__solicitudes:
                        if solicitud.obtener_nombre_usuario() == nombre_usuario:
                            print("\n")
                            print("*" * 50)
                            print("\tUsuario ~ " + solicitud.obtener_nombre_usuario())
                            print("\tOrigen ~ " + solicitud.origen)
                            print("\tDestino ~ " + solicitud.destino)
                            print("*" * 50, "\n")
                    input("Presione Enter para continuar...")
                elif opcion_usuario == "5":
                    return

    def ingresar_como_chofer(self):
        while True:
            nombre_chofer = input("Ingrese su identificación para continuar\n=>")
            if nombre_chofer not in [
                chofer.identificacion for chofer in self.__choferes
            ]:
                self.__choferes.append(Chofer(nombre_chofer, nombre_chofer))

            print("\n\n")
            while True:
                opcion_chofer = Menu().obtener_opcion_menu_chofer()
                print("\n\n")
                while opcion_chofer not in ["1", "2", "3", "4", "5"]:
                    print("La opción ingresada no es válida.")
                    opcion_chofer = Menu().obtener_opcion_menu_chofer()

                if opcion_chofer == "1":
                    if not self.__solicitudes:
                        print("No hay solicitudes de viaje pendientes.")
                        input("Presione Enter para continuar...")
                        break
                    print("Solicitud de viaje pendiente:")
                    for solicitud in self.__solicitudes:
                        print("\n")
                        print("*" * 50)
                        print(
                            f"*   Origen: {solicitud.origen}, Destino: {solicitud.destino}, Usuario: {solicitud.obtener_nombre_usuario()}   *"
                        )
                        print("*" * 50)
                    input("Presione Enter para continuar...")

                elif opcion_chofer == "2":
                    for chofer in self.__choferes:
                        if chofer.identificacion == nombre_chofer:
                            chofer.estado = chofer.cambiar_estado()
                            print(
                                f"{nombre_chofer}(#) Su estado ha sido cambiado a: {chofer.estado}"
                            )
                            input("Presione Enter para continuar...")
                            break
                elif opcion_chofer == "3":
                    for i, solicitud in enumerate(self.__solicitudes):
                        print(
                            f"{i+1}. {solicitud.origen} - {solicitud.destino} - {solicitud.obtener_nombre_usuario()}"
                        )

                    input("Presione Enter para continuar...")

                elif opcion_chofer == "4":
                    for i, chofer in enumerate(self.__choferes):
                        if chofer.estado == "Disponible":
                            print(
                                f"Chofer: {chofer.nombre} - Posición en la lista_enlazada: {i+1}"
                            )
                    input("Presione Enter para continuar...")

                elif opcion_chofer == "5":
                    return

    def ingresar_como_administrador(self):
        while True:
            opcion_administrador = Menu().obtener_opcion_menu_administrador()
            print("\n\n")
            while opcion_administrador not in ["1", "2", "3", "4"]:
                print("La opción ingresada no es válida.")
                opcion_administrador = Menu().obtener_opcion_menu_administrador()
            if opcion_administrador == "1":
                print("\nChoferes Disponibles")
                print("-" * 50)
                for i, chofer in enumerate(self.__choferes):
                    if chofer.estado == "Disponible":
                        print(f"*\t{i+1}. {chofer.nombre} - {chofer.estado} \t*")
                print("-" * 50)
                print("\nChoferes No Disponibles")
                print("-" * 50)
                for i, chofer in enumerate(self.__choferes):
                    if chofer.estado == "Ocupado":
                        print(f"*\t{i+1}. {chofer.nombre} - {chofer.estado} \t*")
                print("-" * 50)
                input("\nPresione Enter para continuar...")

            elif opcion_administrador == "2":
                print("\t\tSolicitudes de Viaje\n")
                if not self.__solicitudes:
                    print("\tNo hay solicitudes de viaje pendientes.\n")
                    input("\nPresione Enter para continuar...")
                for i, solicitud in enumerate(self.__solicitudes):
                    print(
                        f"{i+1}. {solicitud.obtener_nombre_usuario()} # {solicitud.origen} - {solicitud.destino} "
                    )

            elif opcion_administrador == "3":
                print("Usuarios Registrados")
                for i, usuario in enumerate(self.__usuarios):
                    print(f"\t\t{i+1}. {usuario.nombre}")
                input("Presione Enter para continuar...")
            elif opcion_administrador == "4":
                return
            else:
                print("La opción ingresada no es válida.")
                input("Presione Enter para continuar...")
