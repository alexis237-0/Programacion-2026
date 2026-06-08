from Accion import *
class MenuAccion:
  def __init__(self):
    self.bienvenida = "'''Menú Acción'''"
    self.accion = Accion("1", "Apple", "Comercial", 500)

  def despliega_menu(self):
    while True:
      print("\n''''''''MENU''''''''")
      print("1. Ver informacion")
      print("2. Actualizar precio")
      print("3. Estado")
      print("4. Salir")

      opcion = input("Seleccione una opción: ")

      if opcion == "1":
        print("---Información de la cuenta---")
        print(self.accion)

      elif opcion == "2":
        nuevo = float(input("Ingrese el nuevo precio: "))
        if nuevo > 0:
          self.accion.actualizar_precio(nuevo)
          print(f"Precio actualizado. Nuevo precio: {nuevo}")

        else:
          print("Precio erroneo.")

      elif opcion == "3":
        print("Precio anterior:", self.accion.get_precio())
        print("Cambio porcentual:", self.accion.calcular_cambio_porcentual())
        print("Estado:", self.accion.estado())

      elif opcion == "4":
        print("Gracias por usar el sistema.")
        break

      else:
        print("Opcion invalida.")