#Aquí se define la acción y todo lo relacionado con ella
class Accion:

  def __init__(self, id, nombre, tipo, precio):
    self.__id = id
    self.__nombre = nombre
    self.__tipo = tipo
    self.__precio = precio
    self.__precio_anterior = precio

  def get_id(self):
    return self.__id

  def get_nombre(self):
    return self.__nombre

  def get_tipo(self):
    return self.__tipo

  def get_precio(self):
    return self.__precio

  def actualizar_precio(self, nuevo_precio):
    self.__precio_anterior = self.__precio
    self.__precio = float(nuevo_precio)

  def calcular_cambio_porcentual(self):
    cambio = ((self.__precio - self.__precio_anterior) / self.__precio_anterior) * 100
    return cambio

  def estado(self):
    cambio = self.calcular_cambio_porcentual()
    if cambio > 0:
      print(f"Cambio: {cambio}%")
      return "En subida 📈"
    elif cambio < 0:
      print(f"Cambio: {cambio}%")
      return "En bajada 📉"
    else:
      return "Sin cambios"

  def __str__(self):
    det = "Id asociada::" + str(self.__id)
    det += "\nNombre de la acción::" + str(self.__nombre)
    det += "\nTipo de acción::" + str(self.__tipo)
    det += "\nPrecio actual::" + str(self.__precio)
    return det