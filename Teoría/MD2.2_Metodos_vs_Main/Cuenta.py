'''
Febrero, 2026
autor: alexis237@ciencias.unam.mx
'''

class Cuenta:
    def __init__(self, nombre, valor, tipo):
        self.nombre = nombre
        self.valor = valor
        self.tipo = tipo

    def depositar(self, cantidad):
        self.valor += cantidad

    def retirar(self, cantidad):
        self.valor -= cantidad

    def impInfo(self):
        print("Nombre: ", self.nombre)
        print("Valor: ", self.valor)
        print("Tipo: ", self.tipo)