"""
Junio, 2026
autor: alexis237@ciencias.unam.mx
"""

from Cliente import *
from Cuenta import *
class Banco:
    def __init__(self):
        self.__clientes = []

    def get_clientes(self):
        return self.__clientes

    def agregar_cliente(self, cliente):
        self.__clientes.append(cliente)

    def crear_cliente(self, nombre, direccion, fecha_nac):
        id_new = self.generar_id_cliente()

        cliente = Cliente(id_new, nombre, direccion, fecha_nac)

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
        if len(self.__clientes) == 0:
            return 1

        mayor = max(cliente.get_id() for cliente in self.__clientes)

        return mayor + 1

    def crear_cuenta(self, cliente, tipo, valor, fecha):
        id_nuevo = self.generar_id_cuenta()
        cuenta_nueva = Cuenta(id_nuevo, tipo, valor, fecha)
        cliente.agregarCuenta(cuenta_nueva)
        return cuenta_nueva

    def generar_id_cuenta(self):
        ids = []
        for cliente in self.__clientes:
            for cuenta in cliente.get_cuentas():
                ids.append(cuenta.get_id())

        if len(ids) == 0:
            return 1001

        return max(ids) + 1

    def buscar_cuenta(self, id_cuenta):
        for cliente in self.__clientes:

            for cuenta in cliente.get_cuentas():

                if cuenta.get_id() == id_cuenta:
                    return cliente, cuenta

        return None, None