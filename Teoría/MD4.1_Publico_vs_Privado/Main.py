from Cuenta import *
from Cliente import *
class Main:
    pass

print ("Desde las pruebas")

cuenta1 = Cuenta("Crédito",2000,"02/03/2020")
cliente1 = Cliente("Alexis", "Ciudad de México","02/03/2000",cuenta1)

print ("Imprimir un atributo privado")
#print ("El valor de la cuenta es::", cuenta1.__valor)
#El print anterior genera un error ya que no se puede acceder directamente al atributo
#Para solucionar el problema usamos el metodo get
print("\nEl saldo en la cuenta es:",cuenta1.get_valor())
print("Nombre asociado a la cuenta:",cliente1.get_nombre())

print(f"\n---Información del cliente---\n{cliente1}")

"""
El print usa el str de la cuenta, lo cual, a pesar de tener atributos privados
los puede imprimir sin ningun problema
"""