from Cuenta import*
class Menu:

    def __init__(self, Bienvenida):
        self.mensajeDeBienvenida = Bienvenida
        self.cargaDatos()

    def cargaDatos(self):
        self.cuenta = Cuenta("Crédito",2000,"02/03/2020")

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

    def procesaOpcion(self, opcion):
        while True:
            if opcion == "1":
                print("---Información de la cuenta---")
                print(self.cuenta)
                break
            elif opcion == "2":
                cantidad = float(input("Cantidad a depositar: "))
                if self.cuenta.depositar(cantidad):
                    print("---Deposito exitoso---")
                    print("Saldo en la cuenta:",self.cuenta.valor)
                    break
                else:
                    print("Cantidad erronea.")
            elif opcion == "3":
                cantidad = float(input("Cantidad a retirar: "))
                if self.cuenta.retirar(cantidad):
                    print("---Retiro exitoso---")
                    print("Saldo en la cuenta:",self.cuenta.valor)
                    break
                else:
                    print("---Saldo insuficiente---")
                    print("Saldo en la cuenta:",self.cuenta.valor)
            elif opcion == "4":
                print("Gracias por usar el sistema.")
            else:
                print("Opcion invalida.")