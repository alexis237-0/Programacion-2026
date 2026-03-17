'''Created...
autor, alexis237@ciencias.unam.mx
'''

class Cliente:
    def __init__(self, nombre, cuenta, fechaNac):
        self.nombre = nombre
        self.cuenta = (cuenta)
        self.fechaNac = fechaNac

    def informacion(self):
        print("Nombre: ", self.nombre)
        self.cuenta.impInfo()
        print("Fecha de Nacimiento: ", self.fechaNac)