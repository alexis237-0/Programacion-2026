#Aquí se define la acción y todo lo relacionado con ella
class Accion:

  def __init__(self, ID, nombre, tipo, precio):
    self.ID = ID
    self.nombre = nombre
    self.tipo = tipo
    self.precio = precio
    self.precio_anterior = precio

  def actualizar_precio(self, nuevo_precio):
    self.precio_anterior = self.precio
    self.precio = float(nuevo_precio)

  def calcular_cambio_porcentual(self):
    cambio = ((self.precio - self.precio_anterior) / self.precio_anterior) * 100
    return cambio
  def mostrar_informacion(self):
    print("ID de la acción:", self.ID)
    print("Nombre:", self.nombre)
    print("Tipo de acción:", self.tipo)
    print("Precio actual:", self.precio)

  def estado(self):
    cambio = self.calcular_cambio_porcentual()
    if cambio > 0:
      return "En subida 📈"
    elif cambio < 0:
      return "En bajada 📉"
    else:
      return "Sin cambios"