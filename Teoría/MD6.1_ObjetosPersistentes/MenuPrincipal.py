from Data1 import*
class MenuPrincipal:
    def __init__(self):
        self.banco = Data.cargar()

    def mostrar_menu_principal(self):
        while True:
            print("\n--Menú del Banco--")
            print("1. Nuevo Cliente")
            print("2. Mis cuentas")
            print("3. Salir del Menú")

            opcion = input("Ingrese opcion: ")

            if opcion == "1":
                nombre = input("Ingrese su nombre.")
                direccion = input("Ingrese su dirección")
                fecha_nac = input("Ingrese su fecha de cacimiento")

                cliente = self.banco.crear_cliente(nombre, direccion, fecha_nac)
                print(f"Información del cliente:\n{cliente}")

            elif opcion == "2":
                id_usuario = int(input("Ingrese su ID asociado"))
                cliente = self.banco.buscar_cliente(id_usuario)

                if cliente:
                    self.mostrar_menu_cliente(cliente)

                else:
                    print("Cliente no encontrado.")


            elif opcion == "3":
                Data.guardar(self.banco)
                print("Datos guardados correctamente.")
                break

            else:
                print("Opción inválida")

    def mostrar_menu_cliente(self, cliente):
        while True:
            print("1. Ver cuentas")
            print("2. Administrar cuenta")
            print("3. Crear cuenta")
            print("4. Eliminar cuenta")
            print("5. Salir")

            opcion = input("Opción: ")

            if opcion == "1":
                cliente.infoCuentas()

            elif opcion == "2":
                cuenta = self.seleccionar_cuenta(cliente)

                if cuenta:
                    self.mostrar_menu_cuenta(cuenta)

            elif opcion == "3":
                tipo = input("Ingrese el tipo de cuenta")
                valor = float(input("Ingrese el saldo de la cuenta"))
                fecha = input("Ingrese la fecha de hoy")

                self.banco.crear_cuenta(cliente, tipo, valor, fecha)
                print("Cuenta creada correctamente")

            elif opcion == "4":
                indice = int(input("índice de la cuenta a eliminar"))
                if cliente.eliminarCuenta(indice):
                    print("Cuenta eliminada correctamente")
                else:
                    print("Índice inválido")

            elif opcion == "5":
                break

            else:
                print("Opción inválida")

    def mostrar_menu_cuenta(self, cuenta):
        while True:
            print("\n--- Menú Cuenta ---")
            print("1. Datos de la cuenta")
            print("2. Depositar")
            print("3. Retirar")
            print("4. Volver")

            opcion = input("Opción: ")

            if opcion == "1":
                print(cuenta)

            elif opcion == "2":
                cantidad = float(input("Cantidad a depositar: "))

                if cuenta.depositar(cantidad):
                    print("Depósito exitoso")
                    print("Saldo:", cuenta.get_valor())
                else:
                    print("Cantidad inválida")

            elif opcion == "3":

                cantidad = float(input("Cantidad a retirar: "))

                if cuenta.retirar(cantidad):
                    print("Retiro exitoso")
                    print("Saldo:", cuenta.get_valor())
                else:
                    print("Fondos insuficientes")

            elif opcion == "4":
                break

            else:
                print("Opción inválida")

    def seleccionar_cuenta(self, cliente):
        cliente.infoCuentas()
        id_cuenta = int(input("Ingrese el ID de la cuenta: "))

        for cuenta in cliente.get_cuentas():
            if cuenta.get_id() == id_cuenta:
                return cuenta

        return None