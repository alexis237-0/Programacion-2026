class Cliente:
    def __init__(self, nombre, direccion, fechaNac, cuenta):
        self.nombre = nombre
        self.direccion = direccion
        self.fechaNac = fechaNac
        self.cuenta = cuenta

    def __str__( self ):
        inf = "Nombre::" + str( self.nombre )
        inf += "\nDirección::" + str( self.direccion )
        inf += "\nFecha de Nacimiento::" + str( self.fechaNac )
        inf += "\n" + str( self.cuenta )
        return inf