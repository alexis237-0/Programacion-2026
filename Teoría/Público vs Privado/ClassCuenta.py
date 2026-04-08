'''
Created on February, 2026
autor: alexis237@ciencias.unam.mx
'''
class Cuenta:
  def __init__(self, tipo, valor ,fecha):
    self.__tipo = tipo
    self.__valor = float(valor)
    self.__fecha = fecha

  def impInfo(self):
    print("Tipo de la cuenta: ", self.__tipo)
    print("Saldo de la cuenta: ", self.__valor)
    print("Fecha de Contratación: ", self.__fecha)
    return

  def retirar(self, cantidad):
    self.__valor = self.__valor - cantidad

  def depositar(self, cantidad):
    if cantidad > 0 :
      self.__valor = self.__valor + cantidad
      return True
    else:
      return False

  def get_valor(self):
    return self.__valor

  def get_valor(self):
    return self.__valor

  def get_fecha(self):
    return self.__fecha

  def __str__(self):
    return "saldo :: " + str(self.__valor) + " | tipo :: " + self.__tipo
