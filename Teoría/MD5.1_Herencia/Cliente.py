class Cliente:
    def __init__(self, nombre, direccion, fecha_nac):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__fecha_nac = fecha_nac
        self.__cuentas = []

    def get_nombre(self):
        return self.__nombre

    def get_direccion(self):
        return self.__direccion

    def get_fecha_nac(self):
        return self.__fecha_nac

    def get_cuentas(self):
        return self.__cuentas

    def agregarCuenta(self, cta):
        self.__cuentas.append(cta)

    def eliminarCuenta(self, indice):
        self.__cuentas.remove(indice - 1)

    def infoCuentas(self):
        print("----Información de las cuentas----")
        print("Cantidad de Cuentas:" + str(len(self.__cuentas)))
        for i, cta in enumerate(self.__cuentas, start = 1):
            print(f" Cuenta {i}: {cta}\n")

    def __str__( self ):
        inf = "Nombre::" + str( self.__nombre )
        inf += "\nDirección::" + str( self.__direccion )
        inf += "\nFecha de Nacimiento::" + str( self.__fecha_nac )
        return inf