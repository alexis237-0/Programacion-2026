class Menu:

    def __init__(self,Bienvenida):
        self.MensajeDeBienvenida = Bienvenida

    def darBienvenida(self, MensajeDeBienvenida):
        print(MensajeDeBienvenida)

    def DespliegaMenu(self):
        print("---- Menú ----")
        print("1. Retirar")
        print("2. Depositar")
        Opcion = input("Ingrese opción:")
        return Opcion

    def ProcesaOpción(self, Cuenta, Opcion):
        if Opcion == "1":
            Cantidad = float(input("Cantidad a retirar:"))
            Cuenta.retirar(Cantidad)
            print(Cuenta.valor)
        elif Opcion == "2":
            Cantidad = float(input("Cantidad a depositar:"))
            Cuenta.depositar(Cantidad)
            print(Cuenta.valor)
        else:
            print("Opción invalida")