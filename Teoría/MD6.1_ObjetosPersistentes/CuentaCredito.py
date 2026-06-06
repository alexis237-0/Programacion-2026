"""
Junio, 2026
autor: alexis237@ciencias.unam.mx
"""

from Cuenta import *

class CuentaCredito(Cuenta):
    def __init__(self, id_cuenta, tipo, valor, fecha1, m_sobregiro):
        super().__init__(id_cuenta, tipo, valor, fecha1)
        self.montoSobregiro = m_sobregiro

    def __str__(self):
        msg = super().__str__()
        msg += "\nMonto de Sobregiro: " + str(self.montoSobregiro)
        return msg

    def retirar(self, cantidad):
        saldo = self.get_valor()
        if saldo >= cantidad:
            return super().retirar(cantidad)

        sobregiro_necesario = cantidad - saldo

        if self.montoSobregiro >= sobregiro_necesario:
            super().retirar(saldo)
            self.montoSobregiro -= sobregiro_necesario
            return True

        else:
            print("No se pudo retirar")
            return False