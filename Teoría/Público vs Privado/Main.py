from Menu import *
from Teoría.ClassCuenta import Cuenta
from Teoría.Cliente import *

class Main:
    pass

print("Desde el main: ")
cuenta4 = Cuenta("D", 3000, "20/02/2000")
cliente1 = Cliente("Jimena", cuenta4, "25/02/1990")

menu = Menu("Bienvenido al banco")
menu.darBienvenida()
while True:
    opcion = menu.DespliegaMenu()
    menu.procesaOpcion(opcion, cuenta4)

    if opcion == "4":
        break