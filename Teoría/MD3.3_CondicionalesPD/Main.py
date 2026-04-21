from Menu import*
class Main:
    pass

menu = Menu("Bienvenidos al Banco Pato")
menu.darBienvenida()
opcion = menu.DespliegaMenu()
menu.procesaOpcion(opcion)