from Cuenta import *

class CuentaAhorro(Cuenta):

    def __init__(self, tipo, valor, fecha1, tInteres):
        super().__init__(tipo, valor, fecha1)
        self.tasaInteres = tInteres

    def __str__(self):
        msg = super().__str__()
        msg += "\nTasa de interes: " + str(self.tasaInteres)
        return msg