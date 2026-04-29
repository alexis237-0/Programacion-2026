class Cuenta:
    def __init__(self, nombre, fecha_acc):
        self.__nombre = nombre
        self.__fecha_acc = fecha_acc
        self.__acciones = []

    def get_nombre(self):
        return self.__nombre

    def get_fecha_acc(self):
        return self.__fecha_acc

    def get_acciones(self):
        return self.__acciones

    def agregarAccion(self, acc):
        self.__acciones.append(acc)

    def eliminarAccion(self, indice):
        self.__acciones.remove(indice - 1)

    def infoAcciones(self):
        print("----Información de las acciones----")
        print("Cantidad de Cuentas:" + str(len(self.__acciones)))
        for i, acc in enumerate(self.__acciones, start = 1):
            print(f" Cuenta {i}: {acc}\n")

    def __str__( self ):
        inf = "Nombre::" + str( self.__nombre )
        inf += "\nFecha de Creación::" + str( self.__fecha_acc )
        return inf