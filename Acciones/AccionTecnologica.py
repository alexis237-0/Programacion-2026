from Accion import *

class AccionTecnologica(Accion):

    def __init__(self, id_accion, nombre, precio, sector):
        super().__init__(id_accion, nombre, precio)
        self.__sector = sector

    def estado(self):
        return "Estado tecnológico → " + super().estado()

    def __str__(self):
        jtr = super().__str__()
        jtr += "\nSector Tecnológico: " + str(self.__sector)
        return jtr