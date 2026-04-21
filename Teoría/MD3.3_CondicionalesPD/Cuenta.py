'''
Febrero, 2026
autor: alexis237@ciencias.unam.mx
'''

class Cuenta:
    def __init__(self, tipo, valor, fecha1):
        self.tipo = tipo
        self.valor = valor
        self.fecha1 = fecha1

    def depositar(self, cantidad):
        if cantidad > 0:
            self.valor = self.valor + cantidad
            return True
        else:
            return False

    def retirar(self, cantidad):
        if cantidad <= self.valor :
            self.valor -= cantidad
            return True
        else:
            return False

    def __str__(self):
        det = "Tipo de cuenta::" + str(self.tipo)
        det += "\nSaldo en la cuenta::" + str(self.valor)
        det += "\nFecha de Contratación::" + str(self.fecha1)
        return det