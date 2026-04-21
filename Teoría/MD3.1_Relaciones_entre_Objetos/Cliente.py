class Cliente:
    def __init__(self, nombre, direccion, fechaNac, cuenta):
        self.nombre = nombre
        self.direccion = direccion
        self.fechaNac = fechaNac
        self.cuenta = cuenta

    def impInfo(self):
        print("Nombre: ", self.nombre)
        print("Dirección: ", self.direccion)
        print("Fecha de Nacimiento: ", self.fechaNac)
        self.cuenta.impDetalles()