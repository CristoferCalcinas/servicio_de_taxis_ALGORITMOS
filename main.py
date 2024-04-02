# import time
from menus import Menu

# from sistema_taxi import SistemaTaxi
from sistema_taxi_cola import SistemaTaxiQueue

# if __name__ == "__main__":
#     sistema = SistemaTaxi()
#     menu = Menu()
#     while True:
#         opcion = menu.menu_inicial()
#         if opcion == "1":
#             sistema.ingresar_como_usuario()
#         elif opcion == "2":
#             sistema.ingresar_como_chofer()
#         elif opcion == "3":
#             sistema.ingresar_como_administrador()
#         elif opcion == "4":
#             break
#         else:
#             print("La opción ingresada no es válida.")
#             # time.sleep(2)
#             # continue
#     print("Gracias por usar nuestro sistema de taxi.")
#     # time.sleep(2)
#     # exit()
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
