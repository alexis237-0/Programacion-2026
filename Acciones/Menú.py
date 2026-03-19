from Class_accion import *
class Menu:
  def iniciar(self):
    id = input("ID de la accion: ")
    nombre = input("Nombre de la accion: ")
    tipo = input("Tipo de la cción: ")
    valor = float(input("Precio de la acción: "))
    accion = Accion(id, nombre, tipo, valor)

    while True:
      print("\nMENU")
      print("1. Ver informacion")
      print("2. Actualizar precio")
      print("3. Estado")
      print("4. Salir")

      opcion = input("Opcion: ")

      if opcion == "1":
        accion.mostrar_informacion()

      elif opcion == "2":
        nuevo = float(input("Nuevo precio: "))
        accion.actualizar_precio(nuevo)
        print("Precio actualizado")

      elif opcion == "3":
        print("Precio anterior:", accion.precio_anterior)
        print("Cambio porcentual:", accion.calcular_cambio_porcentual())
        print("Estado:", accion.estado())

      elif opcion == "4":
        break

      else:
        print("Opcion invalida")