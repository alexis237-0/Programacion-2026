from Control import Control
from Cliente import Cliente
from Accion import Accion
import pandas as pd

class Data:

    @staticmethod
    def guardar(control):

        clientes_data = []
        acciones_data = []

        for cliente in control.get_clientes():

            clientes_data.append({
                "id_cliente": cliente.get_id(),
                "nombre": cliente.get_nombre(),
                "saldo": cliente.get_saldo()
            })

            for accion, cantidad in cliente.get_portafolio().items():

                acciones_data.append({
                    "id_cliente": cliente.get_id(),
                    "id_accion": accion.get_id(),
                    "nombre_accion": accion.get_nombre(),
                    "precio": accion.get_precio(),
                    "cantidad": cantidad
                })

        pd.DataFrame(clientes_data).to_csv(
            "clientes.csv",
            index=False
        )

        pd.DataFrame(acciones_data).to_csv(
            "acciones.csv",
            index=False
        )

        print("Datos guardados correctamente.")

    @staticmethod
    def cargar():
        control = Control()

        try:

            df_clientes = pd.read_csv("clientes.csv")
            df_acciones = pd.read_csv("acciones.csv")

        except FileNotFoundError:

            print("No existen archivos.")
            return control

        clientes = {}

        for _, fila in df_clientes.iterrows():
            cliente = Cliente(
                int(fila["id_cliente"]),
                fila["nombre"],
                float(fila["saldo"])
            )

            control.agregar_cliente(cliente)

            clientes[cliente.get_id()] = cliente

        for _, fila in df_acciones.iterrows():
            accion = Accion(
                int(fila["id_accion"]),
                fila["nombre_accion"],
                float(fila["precio"])
            )

            cliente = clientes[
                int(fila["id_cliente"])
            ]

            cliente.get_portafolio()[accion] = \
                int(fila["cantidad"])

        print("Datos cargados correctamente.")

        return control