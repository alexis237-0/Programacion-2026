from Data import*
from AccionTecnologica import *
from AccionBancaria import *
from AccionMercado import *
class Menu:
    def __init__(self):
        self.control = Data.cargar()
        self.acciones_disponibles = [
            AccionTecnologica(1001,"Microsoft",500,"Software"),
            AccionBancaria(1002,"BBVA",120,"México"),
            AccionMercado(1003,"Amazon",180,"E-commerce")
        ]

    def mostrar_menu(self):

        while True:

            print("\n———— Menú Principal ————")
            print("1. Nuevo usuario")
            print("2. Ingresar a usuario")
            print("3. Guardar y salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":

                nombre = input("Nombre: ")
                saldo = float(input("Saldo inicial: "))

                cliente = self.control.crear_cliente(
                    nombre,
                    saldo
                )

                print(cliente)

            elif opcion == "2":

                id_cliente = int(
                    input("ID del cliente: ")
                )

                cliente = self.control.buscar_cliente(
                    id_cliente
                )

                if cliente:
                    self.menu_cliente(cliente)

                else:
                    print("Cliente no encontrado.")

            elif opcion == "3":

                Data.guardar(self.control)
                print("Datos guardados.")
                break

            else:
                print("Opción inválida.")

    def menu_cliente(self, cliente):

        while True:

            print("\n———— Menú Cliente ————")
            print("1. Ver portafolio")
            print("2. Comprar acción")
            print("3. Vender acción")
            print("4. Ver saldo")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":

                cliente.infoPortafolio()

            elif opcion == "2":

                self.comprar_accion(cliente)

            elif opcion == "3":

                self.vender_accion(cliente)

            elif opcion == "4":

                print(
                    f"Saldo disponible: "
                    f"${cliente.get_saldo()}"
                )

            elif opcion == "5":

                break

            else:

                print("Opción inválida.")

    def seleccionar_accion(self, cliente):
        cliente.infoPortafolio()
        id_accion = int(input("Ingrese el ID de la accion: "))

        for accion in cliente.get_Portafolio():
            if accion.get_id() == id_accion:
                return accion

        return None

    def comprar_accion(self, cliente):

        print("\nAcciones disponibles:\n")

        for accion in self.acciones_disponibles:
            print(
                f"ID: {accion.get_id()} | "
                f"{accion.get_nombre()} | "
                f"${accion.get_precio()}"
            )

        try:

            id_accion = int(
                input("\nIngrese ID de la acción: ")
            )

            cantidad = int(
                input("Cantidad: ")
            )

        except ValueError:

            print("Dato inválido.")
            return

        for accion in self.acciones_disponibles:

            if accion.get_id() == id_accion:
                cliente.comprar(
                    accion,
                    cantidad
                )

                return

        print("Acción no encontrada.")

    def vender_accion(self, cliente):

        portafolio = cliente.get_portafolio()

        if not portafolio:
            print("No posee acciones.")
            return

        print("\nSu portafolio:\n")

        for accion, cantidad in portafolio.items():
            print(
                f"ID: {accion.get_id()} | "
                f"{accion.get_nombre()} | "
                f"Cantidad: {cantidad}"
            )

        try:

            id_accion = int(
                input("\nID de la acción: ")
            )

            cantidad = int(
                input("Cantidad a vender: ")
            )

        except ValueError:

            print("Dato inválido.")
            return

        for accion in portafolio.keys():

            if accion.get_id() == id_accion:
                cliente.vender(
                    accion,
                    cantidad
                )

                return

        print("No posee una acción con ese ID.")