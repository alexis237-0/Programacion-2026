class Cliente:
    def __init__(self, nombre, direccion, fecha_nac, cuenta):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__fecha_nac = fecha_nac
        self.__cuenta = cuenta

    def get_nombre(self):
        return self.__nombre

    def get_direccion(self):
        return self.__direccion

    def get_fecha_nac(self):
        return self.__fecha_nac

    def get_cuenta(self):
        return self.__cuenta

    def __str__( self ):
        inf = "Nombre::" + str( self.__nombre )
        inf += "\nDirección::" + str( self.__direccion )
        inf += "\nFecha de Nacimiento::" + str( self.__fecha_nac )
        inf += "\n" + str( self.__cuenta )
        return inf