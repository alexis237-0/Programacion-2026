from Class_accion import *
from Menú import *
accion1 = Accion("1", "Walmart", "Comercial", 220)

nuevo_precio = float(input("Nuevo precio de la acción:"))
accion1.actualizar_precio(nuevo_precio)
print(accion1.precio)
accion1.estado()
print(accion1.estado())
print(accion1.calcular_cambio_porcentual())

menu = Menu()
menu.iniciar()


