"""
Junio, 2026
autor: alexis237@ciencias.unam.mx
"""

from Cuenta import *

class CuentaAhorro(Cuenta):

    def __init__(self, id_cuenta, tipo, valor, fecha1, t_interes):
        super().__init__(id_cuenta, tipo, valor, fecha1)
        self.tasaInteres = t_interes

    def __str__(self):
        msg = super().__str__()
        msg += "\nTasa de interes: " + str(self.tasaInteres)
        return msg