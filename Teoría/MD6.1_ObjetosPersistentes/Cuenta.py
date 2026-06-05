"""
Febrero, 2026
autor: alexis237@ciencias.unam.mx
"""

class Cuenta:
    def __init__(self, id_cuenta, tipo, valor, fecha1):
        self.__id = id_cuenta
        self.__tipo = tipo
        self.__valor = valor
        self.__fecha1 = fecha1

    def get_tipo(self):
        return self.__tipo

    def get_valor(self):
        return self.__valor

    def get_fecha(self):
        return self.__fecha1

    def get_id(self):
        return self.__id

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__valor = self.__valor + cantidad
            return True
        else:
            return False

    def retirar(self, cantidad):
        if cantidad <= self.__valor :
            self.__valor -= cantidad
            return True
        else:
            return False

    def __str__(self):
        det = " ID de la cuenta::" + str(self.__id)
        det += "\n\t\t\tTipo de cuenta::" + str(self.__tipo)
        det += "\n\t\t\tSaldo en la cuenta::" + str(self.__valor)
        det += "\n\t\t\tFecha de Contratación::" + str(self.__fecha1)
        return det