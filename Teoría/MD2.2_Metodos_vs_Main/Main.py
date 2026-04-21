from Cuenta import*
from Menu import*
class Main:
    pass

Cuenta1 = Cuenta("Alexis", 4000, "D")

menu = Menu("Bienvenido al menú")
menu.darBienvenida("Bienvenido al menú")
Opción = menu.DespliegaMenu()
menu.ProcesaOpción(Cuenta1,Opción)