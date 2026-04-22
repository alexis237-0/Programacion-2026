from Cuenta import*
from Cliente import*
class MenuCliente:
    def __init__(self):
        self.__bienvenida = "Menu usuario"
        self.__cliente = Cliente("Alexis Maldonado", "Ciudad de México","02/03/2000")

    def menuCuentas( self ):
        while True:
            opc = "\n´´´´´´´´´´ Menu Cuenta ´´´´´´´´´´\n"
            opc += "1. Agregar una Cuenta\n"
            opc += "2. Eliminar una Cuenta\n"
            opc += "3. Salir del menú\n"
            print( opc )
            opcion = input("Teclee la opcion deseada::")

            if opcion == "1":
                self.__agregarCuenta()
            elif opcion == "2":
                self.__eliminarCuenta()
            elif opcion == "3":
                break
            else:
                print ("Opcion invalida")

    def __agregarCuenta(self):
        print("Eligió la opción 'Agregar una Cuenta'")
        print("\tInserte los siguientes datos:")
        tipo_cuenta = input("\tTipo de la Cuenta::")
        saldo_inicial = float(input("\tEl saldo inicial::"))
        fecha_cuenta = input("\tFecha de la Cuenta::")
        cuenta1 = Cuenta(tipo_cuenta, saldo_inicial, fecha_cuenta)
        self.__cliente.agregarCuenta(cuenta1)
        print("\nLa cuenta se agregó con éxito\n")
        self.__cliente.infoCuentas()

    def __eliminarCuenta(self):
        print("Eligió la opción 'Eliminar una Cuenta'")
        indice = int(input("Cuenta que desea eliminar::"))
        indice -= 1
        if 0 <= indice < len(self.__cliente.get_cuentas()):
            cuenta_selec = self.__cliente.get_cuentas()[indice]
            print(f"\nInformación de la cuenta:\n")
            print(f" Cuenta {(indice + 1)}: {cuenta_selec}")
            opc1 = "\n¿Seguro que desea eliminar la cuenta?\n"
            opc1 += "1. Si, eliminar cuenta.\n"
            opc1 += "2. No, volver al menú."
            print( opc1 )
            opcion1 = input("Elija una opción: ")
            if opcion1 == "1":
                self.__cliente.get_cuentas().pop(indice)
                print("\nCuenta eliminada con éxito\n")
                self.__cliente.infoCuentas()
            elif opcion1 == "2":
                return
            else:
                print("Opcion invalida")
        else:
            print("Cuenta no encontrada.\n")
            self.__cliente.infoCuentas()