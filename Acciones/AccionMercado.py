from Accion import *

class AccionMercado(Accion):

    def __init__(self, id_accion, nombre, precio, mercado):
        super().__init__(id_accion, nombre, precio)
        self.__mercado = mercado

    def estado(self):
        return "Estado comercial → " + super().estado()

    def __str__(self):
        jtr = super().__str__()
        jtr += "\nSector Tecnológico: " + str(self.__mercado)
        return jtr