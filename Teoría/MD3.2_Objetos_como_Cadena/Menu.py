class Menu:

    def __init__(self, Bienvenida):
        self.mensajeDeBienvenida = Bienvenida

    def darBienvenida(self):
        print(self.mensajeDeBienvenida)

    def DespliegaMenu(self):
        print("\n--Menú del Banco--")
        print("1. Ver datos de cuenta")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")
        return opcion

    def procesaOpcion(self, opcion, cuenta):
        if opcion == "1":
            print(cuenta)
        elif opcion == "2":
            cantidad = float(input("Cantidad a depositar: "))
            cuenta.depositar(cantidad)
            print("Saldo en la cuenta:",cuenta.valor)
        elif opcion == "3":
            cantidad = float(input("Cantidad a retirar: "))
            cuenta.retirar(cantidad)
            print("Saldo en la cuenta:",cuenta.valor)
        elif opcion == "4":
            print("Gracias por usar el sistema.")
        else:
            print("Opcion invalida.")