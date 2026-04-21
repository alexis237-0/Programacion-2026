from Cuenta import *
from Cliente import *
class Main:
    pass

print ("Desde las pruebas\n")
cuenta1 = Cuenta("Crédito",3000,"02/03/2020")
cuenta1.impDetalles()
print("..........")
cuenta1.depositar(500)
cuenta1.impDetalles()
print("..........")
cliente1 = Cliente( "Alexis", "Ciudad de México", "02/03/2000", cuenta1)
cliente1.impInfo()