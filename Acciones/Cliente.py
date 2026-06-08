class Cliente:

    def __init__(self, id_cliente, nombre, saldo):
        self.__id = id_cliente
        self.__nombre = nombre
        self.__saldo = saldo
        self.__portafolio = {}

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_saldo(self):
        return self.__saldo

    def get_portafolio(self):
        return self.__portafolio

    def comprar(self, accion, cantidad):

        costo = accion.get_precio() * cantidad

        if cantidad <= 0:
            print("Ingresar valores positivos.")
            return

        if self.__saldo >= costo:

            self.__saldo -= costo

            if accion in self.__portafolio:
                self.__portafolio[accion] += cantidad
            else:
                self.__portafolio[accion] = cantidad

            print("Compra realizada")

        else:
            print("Saldo insuficiente")

    def vender(self, accion, cantidad):
        nombre = accion.get_nombre()

        if cantidad > 0:

            if nombre in self.__portafolio and \
                    self.__portafolio[nombre] >= cantidad:

                self.__portafolio[nombre] -= cantidad
                self.__saldo += accion.get_precio() * cantidad

                if self.__portafolio[nombre] == 0:
                    del self.__portafolio[nombre]

                print("Venta realizada")

            else:
                print("No posee suficientes acciones")

        else:
            print("Ingresar valores positivos")

    def infoPortafolio(self):

        if not self.__portafolio:
            print("No posee acciones")
            return

        for accion, cantidad in self.__portafolio.items():
            print(
                f"{accion.get_nombre()} - "
                f"{cantidad} acciones - "
                f"${accion.get_precio()}"
            )

    def __str__(self):
        inf = "ID del cliente:: "+ str(self.__id)
        inf += "\nNombre: "+ str(self.__nombre)
        inf += "\nSaldo: "+ str(self.__saldo)
        return inf