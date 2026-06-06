"""
Junio, 2026
autor: alexis237@ciencias.unam.mx
"""

from Banco import *
from Cliente import *
from Cuenta import *
import pandas as pd

class Data:
    @staticmethod
    def guardar(banco):

        clientes_data = []
        cuentas_data = []

        for cliente in banco.get_clientes():

            clientes_data.append({
                "id_cliente": cliente.get_id(),
                "nombre": cliente.get_nombre(),
                "direccion": cliente.get_direccion(),
                "fecha_nac": cliente.get_fecha_nac()
            })

            for cuenta in cliente.get_cuentas():

                cuentas_data.append({
                    "id_cuenta": cuenta.get_id(),
                    "id_cliente": cliente.get_id(),
                    "tipo": cuenta.get_tipo(),
                    "saldo": cuenta.get_valor(),
                    "fecha": cuenta.get_fecha()
                })

        df_clientes = pd.DataFrame(clientes_data)
        df_cuentas = pd.DataFrame(cuentas_data)

        df_clientes.to_csv(
            "clientes.csv",
            index=False
        )

        df_cuentas.to_csv(
            "cuentas.csv",
            index=False
        )

        print("Datos guardados correctamente.")

    @staticmethod
    def cargar():
        banco = Banco()

        try:
            df_clientes = pd.read_csv("clientes.csv", encoding="latin-1")
            df_cuentas = pd.read_csv("cuentas.csv", encoding="latin-1")

        except FileNotFoundError:
            print("No existen archivos CSV.")
            return banco

        clientes_dict = {}

        for _, fila in df_clientes.iterrows():
            cliente = Cliente(
                int(fila["id_cliente"]),
                fila["nombre"],
                fila["direccion"],
                fila["fecha_nac"]
            )

            banco.agregar_cliente(cliente)

            clientes_dict[
                int(fila["id_cliente"])
            ] = cliente

        for _, fila in df_cuentas.iterrows():
            cuenta = Cuenta(
                int(fila["id_cuenta"]),
                fila["tipo"],
                float(fila["saldo"]),
                fila["fecha"]
            )

            id_cliente = int(fila["id_cliente"])

            clientes_dict[id_cliente].agregarCuenta(
                cuenta
            )

        print("Datos cargados correctamente.")

        return banco