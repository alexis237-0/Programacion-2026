from Menu import *

class Main:
	pass

print ("1. Imprimimos atributos desde el archivo principal")
cuenta3 = Cuenta("C", "500", "Juan Maldonado" )

print(cuenta3.tipo)
print(cuenta3.valor)
print(cuenta3.titular)

print ("\n2. Imprimimos atributos con el método")
cuenta3.imprimirDetalles()

cuenta1 = Cuenta("C", 1000, "María Hernandez")
cuenta2 = Cuenta("D", 2500, "Dulce Jimena")

menu = Menu("Bienvenido al banco")
menu.darBienvenida()
opcion = menu.DespliegaMenu()
menu.procesaOpcion(opcion, cuenta1)