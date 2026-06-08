from Accion import *

class AccionBancaria(Accion):

    def __init__(self, id_accion, nombre, precio, banco):
        super().__init__(id_accion, nombre, precio)
        self.__banco = banco

    def estado(self):
        return "Estado bancario → " + super().estado()

    def __str__(self):
        jtr = super().__str__()
        jtr += "\nBanco asociado: " + str(self.__banco)
        return jtr