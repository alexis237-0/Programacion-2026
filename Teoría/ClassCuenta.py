#Probando comando class y la función del punto
#Alexis     cuenta.py
class Cuenta:
  def __init__(self, tipo, valor ,fecha):
    self.tipo = tipo
    self.valor = float(valor)
    self.fecha = fecha

  def impInfo(self):
    print("Tipo de la cuenta: ", self.tipo)
    print("Saldo de la cuenta: ", self.valor)
    print("Fecha de Contratación: ", self.fecha)
    return

  def retirar(self, cantidad):
    self.valor = self.valor - cantidad

  def depositar(self, cantidad):
    if cantidad > 0 :
      self.valor = self.valor + cantidad
      return True
    else:
      return False

  def __str__(self):
    return "saldo :: " + str(self.valor) + " | tipo :: " + self.tipo
