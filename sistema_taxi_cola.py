# from chofer import Chofer
from cola import Queue
from menus import Menu
from semillaQueue import QueueSemilla
from usuario import Usuario
from viaje import Viaje


class SistemaTaxiQueue:
    def __init__(self):
        self.__usuarios = QueueSemilla().cargar_usuarios_queue()
        self.__choferes_disponibles = QueueSemilla().cargar_choferes_disponibles_queue()
        self.__choferes_no_disponibles = (
            QueueSemilla().cargar_choferes_no_disponibles_queue()
        )
        self.__solicitudes = QueueSemilla().cargar_solicitudes_queue()
        self.__viajes_realizados = Queue()

    def pedir_origen_destino(self):
        origen_viaje = input("Ingrese el origen del viaje: ")
        destino_viaje = input("Ingrese el destino del viaje: ")
        return origen_viaje, destino_viaje

    def ingresar_como_usuario(self):
        while True:
            nombre_usuario = input("Ingrese su nombre para continuar\n=>\t")
            if self.__solicitudes.find_user_for_viaje(nombre_usuario):
                print(
                    f"\n\t\tSu Posición en la cola de solicitudes de viaje: {self.__solicitudes.find_position_user_for_viaje(nombre_usuario)}\n"
                )
                print("Ya tiene una solicitud de viaje pendiente.\n")
                input("Presione Enter para continuar...")
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
                    self.__usuarios.enqueue(usuario)
                    viaje = Viaje(usuario, origen_viaje, destino_viaje)
                    self.__solicitudes.enqueue(viaje)
                    print("\nSolicitud de viaje realizada con éxito.")
                    input("\n\nPresione Enter para continuar...")
                elif opcion_usuario == "2":
                    # Cancelar un Viaje
                    if not self.__solicitudes.find_user_for_viaje(nombre_usuario):
                        print("No hay solicitudes de viaje pendientes.\n")
                        input("Presione Enter para continuar...")
                    else:
                        nueva_lista_solicitudes = Queue()
                        current = self.__solicitudes.front
                        while current:
                            if current.data.usuario.nombre != nombre_usuario:
                                nueva_lista_solicitudes.enqueue(current.data)
                            current = current.next
                        # reemplazamos la lista original por la nueva lista
                        self.__solicitudes = nueva_lista_solicitudes
                        print("Viaje cancelado con éxito.\n")
                        input("Presione Enter para continuar...")
                        return
                elif opcion_usuario == "3":
                    # Registro de Viajes de un Usuario
                    if not self.__usuarios.find_user(nombre_usuario):
                        print("No hay viajes registrados para este usuario.\n")
                    else:
                        print(
                            f"\n\tUsuario: {nombre_usuario} - Posición en la cola de Usuarios: {self.__usuarios.find_position_user(nombre_usuario)}\n"
                        )
                    input("Presione Enter para continuar...")
                elif opcion_usuario == "4":
                    # Mostrar Viajes
                    if not self.__solicitudes.find_user_for_viaje(nombre_usuario):
                        print("Actualmente no tienes viajes.\n")
                    else:
                        current = self.__solicitudes.front
                        while current:
                            if current.data.usuario.nombre == nombre_usuario:
                                print("*" * 50)
                                print(
                                    "\t\tUsuario ~ "
                                    + current.data.obtener_nombre_usuario()
                                )
                                print(
                                    "  Origen ~ "
                                    + current.data.origen
                                    + "\t=>"
                                    + "\tDestino ~ "
                                    + current.data.destino
                                )
                                print("*" * 50, "\n")
                            current = current.next
                    input("Presione Enter para continuar...")
                elif opcion_usuario == "5":
                    return

    def ingresar_como_chofer(self):
        while True:
            identificacion_chofer = input(
                "Ingrese su identificación para continuar\nSOLO NUMEROS =>\t"
            )
            if self.__choferes_disponibles.find(
                identificacion_chofer
            ) or self.__choferes_no_disponibles.find(identificacion_chofer):
                while True:
                    opcion_chofer = Menu().obtener_opcion_menu_chofer()
                    print("\n\n")
                    while opcion_chofer not in ["1", "2", "3", "4", "5"]:
                        print("La opción ingresada no es válida.")
                        opcion_chofer = Menu().obtener_opcion_menu_chofer()
                    if opcion_chofer == "1":
                        # Lista de Solicitudes de Viaje Pendientes
                        if self.__solicitudes.is_empty():
                            print("No hay solicitudes de viaje pendientes.\n")
                            input("Presione Enter para continuar...")
                        else:
                            print("Solicitud de viaje pendiente:")
                            current = self.__solicitudes.front
                            while current:
                                print("\n")
                                print("*" * 50)
                                print(
                                    f"*   Origen: {current.data.origen}, Destino: {current.data.destino}, Usuario: {current.data.obtener_nombre_usuario()}   *"
                                )
                                print("*" * 50)
                                current = current.next
                            input("Presione Enter para continuar...")
                    elif opcion_chofer == "2":
                        # Cambiar de Estado
                        if self.__choferes_disponibles.find(identificacion_chofer):
                            self.__choferes_disponibles.dequeue()
                            self.__choferes_no_disponibles.enqueue(
                                identificacion_chofer
                            )
                        else:
                            self.__choferes_no_disponibles.dequeue()
                            self.__choferes_disponibles.enqueue(identificacion_chofer)
                        print(
                            f"{identificacion_chofer} (#) Su estado ha sido cambiado a: {self.__choferes_no_disponibles.find(identificacion_chofer)}"
                        )
                        input("Presione Enter para continuar...")

                    elif opcion_chofer == "3":
                        # Aceptar/Rechazr Solicitud
                        # reprogramar con la logica desde cero
                        # tenemos un queue de solicitudes
                        # tenemos el estado del chofer
                        # lo ideal es imprimir primero todas las solicitudes
                        # luego preguntar el numero de la solicitud que desea aceptar
                        # en realidad si esta disponible solo deberia aceptar, pero si esta ocupado solo deberia rechazar, tal vez ahora el metodo no cambie el estado del chofer, pero pensemos que si lo hace, entonces como primer paso tenemos que mostrar todas las solicitudes
                        if not self.__solicitudes.is_empty():
                            # si no esta vacio imprimimos las solicitudes
                            current = self.__solicitudes.front
                            contador = 1
                            while current:
                                print(
                                    f"{contador}. {current.data.origen} - {current.data.destino} - {current.data.obtener_nombre_usuario()}"
                                )
                                current = current.next
                                contador += 1
                            # luego preguntamos cual desea aceptar
                            numero_solicitud = int(
                                input(
                                    "Ingrese el número de la solicitud a aceptar\n=>\t"
                                )
                            )
                            # verificamos que el numero de solicitud sea valido ademas de que lo que haya ingresado sea un numero
                            while numero_solicitud < 1 or numero_solicitud > contador:
                                print("Número de solicitud inválido.")
                                numero_solicitud = int(
                                    input(
                                        "Ingrese el número de la solicitud a aceptar\n=>\t"
                                    )
                                )
                            # si el numero de solicitud es valido entonces lo aceptamos y modificamos el estado del chofer ademas que te tenemos que actualizar el queue de solicitudes y agregar el viaje a la lista de viajes realizados
                            nuevo_viaje = self.__solicitudes.remove_at_position(
                                numero_solicitud
                            )
                            self.__viajes_realizados.enqueue(nuevo_viaje)
                            # esta parte esta mal, puedo ver que no funciona pero lo arreglo mas tarde
                            if self.__choferes_no_disponibles.find(
                                identificacion_chofer
                            ):
                                self.__choferes_no_disponibles.dequeue()
                                self.__choferes_disponibles.enqueue(
                                    identificacion_chofer
                                )
                            print(
                                f"Viaje aceptado con éxito por {identificacion_chofer}"
                            )
                            input("Presione Enter para continuar...")

                    elif opcion_chofer == "4":
                        # Ver Choferes Disponibles
                        if not self.__choferes_disponibles.is_empty():
                            current = self.__choferes_disponibles.front
                            contador = 1
                            while current:
                                print(f"{contador}. {current.data} - Disponible")
                                current = current.next
                                contador += 1
                            input("Presione Enter para continuar...")
                        else:
                            print("No hay choferes disponibles.\n")
                            input("Presione Enter para continuar...")

                    elif opcion_chofer == "5":
                        return
            else:
                print("\n\tChofer no encontrado en la cola de choferes.\n")
                print("Ingrese su identificación nuevamente.\n")
                continue

    def ingresar_como_administrador(self):
        while True:
            opcion_administrador = Menu().obtener_opcion_menu_administrador()
            print("\n\n")
            while opcion_administrador not in ["1", "2", "3", "4"]:
                print("La opción ingresada no es válida.")
                opcion_administrador = Menu().obtener_opcion_menu_administrador()
            if opcion_administrador == "1":
                # Cola de Choferes
                print("\nChoferes Disponibles")
                print("-" * 50)
                contador = 1
                current = self.__choferes_disponibles.front
                while current:
                    print(
                        f"{contador}. {current.data.nombre} ♫ {current.data.identificacion} - Disponible"
                    )
                    current = current.next
                    contador += 1
                print("-" * 50)
                print("\nChoferes No Disponibles")
                print("-" * 50)
                contador = 1
                current = self.__choferes_no_disponibles.front
                while current:
                    print(
                        f"{contador}. {current.data.nombre} ♫ {current.data.identificacion} - No Disponible"
                    )
                    current = current.next
                    contador += 1
                print("-" * 50)
                input("\nPresione Enter para continuar...")
            elif opcion_administrador == "2":
                # Solicitudes de Viajes
                print("\t\tSolicitudes de Viaje\n")
                if not self.__solicitudes.is_empty():
                    current = self.__solicitudes.front
                    contador = 1
                    while current:
                        print(
                            f"{contador}. {current.data.obtener_nombre_usuario()} # {current.data.origen} - {current.data.destino} "
                        )
                        current = current.next
                        contador += 1
                    input("\nPresione Enter para continuar...")
                else:
                    print("\tNo hay solicitudes de viaje pendientes.\n")
                    input("\nPresione Enter para continuar...")
            elif opcion_administrador == "3":
                # Historial de Usuarios
                print("Usuarios Registrados\n")
                current = self.__usuarios.front
                contador = 1
                while current:
                    print(f"\t  {contador}. {current.data.nombre}")
                    current = current.next
                    contador += 1
                input("\nPresione Enter para continuar...")
            elif opcion_administrador == "4":
                return
            else:
                print("La opción ingresada no es válida.")
                input("Presione Enter para continuar...")


if __name__ == "__main__":
    sistema = SistemaTaxiQueue()
    menu = Menu()
    while True:
        opcion = menu.menu_inicial()
        if opcion == "1":
            sistema.ingresar_como_usuario()
        elif opcion == "2":
            sistema.ingresar_como_chofer()
        elif opcion == "3":
            sistema.ingresar_como_administrador()
        elif opcion == "4":
            break
        else:
            print("La opción ingresada no es válida.")
            continue
    print("Gracias por usar nuestro sistema de taxi.")
    exit()
