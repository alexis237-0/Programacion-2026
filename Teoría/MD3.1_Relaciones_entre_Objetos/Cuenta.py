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
        self.valor += cantidad

    def retirar(self, cantidad):
        self.valor -= cantidad

    def impDetalles(self):
        print("Tipo de la cuenta:",self.tipo)
        print("Saldo disponible:",self.valor)
        print("Fecha de contratación:",self.fecha1)