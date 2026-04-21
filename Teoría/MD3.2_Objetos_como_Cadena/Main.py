from Cuenta import *
from Cliente import *
class Main:
    pass
Cuenta1 = Cuenta("Crédito",2000,"02/03/2020")
Cliente1 = Cliente("Alexis", "Ciudad de México","02/03/2000",Cuenta1)
print(Cuenta1)
print(".........") #Separación entre los str de ambas clases
print(Cliente1)