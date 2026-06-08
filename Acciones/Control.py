from Cliente import*
from AccionTecnologica import *
from AccionBancaria import *
from AccionMercado import *
class Control:

    def __init__(self):
        self.__clientes = []
        self.__acciones = []
        self.acciones_disponibles = [
            AccionTecnologica(1001, "Microsoft", 500, "Software"),
            AccionBancaria(1002, "BBVA", 120, "México"),
            AccionMercado(1003, "Amazon", 180, "E-commerce")
        ]

    def get_clientes(self):
        return self.__clientes

    def agregar_cliente(self, cliente):
        self.__clientes.append(cliente)

    def crear_cliente(self, nombre, saldo):

        id_nuevo = self.generar_id_cliente()

        cliente = Cliente(
            id_nuevo,
            nombre,
            saldo
        )

        self.agregar_cliente(cliente)

        return cliente

    def buscar_cliente(self, id_cliente):

        for cliente in self.__clientes:

            if cliente.get_id() == id_cliente:
                return cliente

        return None

    def eliminar_cliente(self, id_cliente):

        cliente = self.buscar_cliente(id_cliente)

        if cliente:

            self.__clientes.remove(cliente)

            print("Cliente eliminado correctamente.")

        else:

            print("Cliente no encontrado.")

    def generar_id_cliente(self):

        if not self.__clientes:
            return 1

        return max(
            cliente.get_id()
            for cliente in self.__clientes
        ) + 1

    # -------------------------
    # ACCIONES DISPONIBLES
    # -------------------------

    def get_acciones(self):
        return self.__acciones

    def agregar_accion(self, accion):
        self.__acciones.append(accion)

    def buscar_accion(self, id_accion):

        for accion in self.__acciones:

            if accion.get_id() == id_accion:
                return accion

        return None