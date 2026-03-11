#Probando comando class y la funcion del punto
#Alexis     cuenta.py
class Cuenta:
  def __init__(self, tipo, valor ,titular):
    self.tipo = tipo
    self.valor = float(valor)
    self.titular = titular

  def imprimirDetalles(self):
    print(self.tipo)
    print(self.valor)
    print(self.titular)

  def retirar(self, cantidad):
    self.valor = self.valor - cantidad
    print("Saldo nuevo de la cuenta: ", self.valor)

  def depositar(self, cantidad):
    self.valor = self.valor + cantidad
    print("Saldo nuevo de la cuenta: ", self.valor)