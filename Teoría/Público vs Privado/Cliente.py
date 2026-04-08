'''
Created on February, 2026
autor: alexis237@ciencias.unam.mx
'''
from ClassCuenta import *

class Cliente:
    def __init__(self, nombre, cuenta, fechaNac):
        self.__nombre = nombre
        self.__cuenta = (cuenta)
        self.__fechaNac = fechaNac

    def get_nombre(self):
        return self.__nombre

    def get_cuenta(self):
        return self.__cuenta

    def get_fechaNac(self):
        return self.__fechaNac

    def informacion(self):
        print("Nombre: ", self.__nombre)
        print("Fecha de Nacimiento: ", self.__fechaNac)
        self.__cuenta.impInfo()