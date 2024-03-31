import os


class Menu:
    def __init__(self) -> None:
        pass

    def draw_menu(self, opciones: str, titulo: str = "*****"):
        print("*" * 35)
        print("*{:^33}*".format(titulo))
        print("*" * 35)
        for opcion in opciones:
            print("*{:<33}*".format(opcion))
        print("*" * 35)

    def menu_inicial(self):
        opciones = [
            "  1. Ingresar como Usuario",
            "  2. Ingresar como Chofer",
            "  3. Ingresar como Administrador",
            "  4. Salir",
        ]
        os.system("cls" if os.name == "nt" else "clear")
        self.draw_menu(opciones, "Menú Inicial")

        opcion_elegida = 0
        while True:
            opcion_elegida = input("\nIngrese el número de la opción deseada: ")

            if opcion_elegida.isdigit() and 0 < int(opcion_elegida) <= len(opciones):
                break
            elif opcion_elegida.strip() == "":
                print("No ha ingresado nada. Por favor, ingrese un número.")
            else:
                print(
                    "La opción ingresada no es válida. Por favor, ingrese solo números."
                )
        return opcion_elegida

    def obtener_opcion_menu_usuario(self):
        opciones = [
            "  1. Solicitar un Viaje",
            "  2. Cancelar Viaje",
            "  3. Registro de Viaje",
            "  4. Mostrar Viaje",
            "  5. Salir",
        ]
        os.system("cls" if os.name == "nt" else "clear")
        self.draw_menu(opciones, "Menú Usuario")

        opcion_elegida = input("\nIngrese el número de la opción deseada: ")

        if opcion_elegida and len(opciones) >= int(opcion_elegida) > 0:
            return opcion_elegida
        else:
            print("La opción ingresada no es válida.")
            return None

    def obtener_opcion_menu_chofer(self):
        opciones = [
            "  1. Lista de Solicitudes de Viaje Pendientes",
            "  2. Cancelar Viaje",
            "  3. Registro de Viaje",
            "  4. Mostrar Viajes",
            "  5. Salir",
        ]
        os.system("cls" if os.name == "nt" else "clear")
        self.draw_menu(opciones, "Menú Chofer")

        opcion_elegida = input("\nIngrese el número de la opción deseada: ")

        if len(opciones) >= int(opcion_elegida) > 0:
            return opcion_elegida
        else:
            print("La opción ingresada no es válida.")
            return None

    def obtener_opcion_menu_administrador(self):
        opciones = [
            "  1. Cola de Choferes",
            "  2. Solicitudes de Viajes",
            "  3. Historial de Viajes",
            "  4. Salir",
        ]
        os.system("cls" if os.name == "nt" else "clear")
        self.draw_menu(opciones, "Menú Administrador")

        opcion_elegida = input("\nIngrese el número de la opción deseada: ")

        if len(opciones) >= int(opcion_elegida) > 0:
            return opcion_elegida
        else:
            print("La opción ingresada no es válida.")
            return None
