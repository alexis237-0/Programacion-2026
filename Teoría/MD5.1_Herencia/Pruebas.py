from CuentaAhorro import *
from CuentaCredito import *

class Pruebas:
	pass

	print ( "\t *********Un objeto Cuenta" )
	cuenta1 = Cuenta("Crédito",300,"02/03/2026" )
	print (cuenta1)
	cuenta1.depositar( 400 )
	print (cuenta1)

	print ( "\n\n\t *********La Cuenta de Ahorro" )
	cuenta2 = CuentaAhorro( "Ahorro",200, "02/02/2026",0.2 )
	print (cuenta2)
	cuenta2.depositar( 8000 )
	print (cuenta2)

	print ( "\n\n\t *********La cuenta de Credito" )
	cuenta3 = CuentaCredito( "Crédito",200, "02/01/2026",100 )
	print (cuenta3)
	cuenta3.depositar( 8000 )
	print (cuenta3)
	cuenta3.retirar(8250)
	print (cuenta3)
	cuenta3.retirar(150)
	print (cuenta3)