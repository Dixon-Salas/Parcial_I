# creamos la clase calculadora con su metodo init de vaalores 1 y 2.
class Calculadora:
	def __init__(self):
		self.valor_1=int(input("Digite  el valor 1: "))
		self.valor_2=int(input("Digite el valor 2: "))

	# Se crea la funcion de suma.esta me permite operar el valor 1 + 2.
	def suma(self):
		suma=self.valor_1+self.valor_2
		print("El resultado de la operacion suma de sus valores es: ",suma)

	# Se crea la funcion de resta.esta me permite operar el valor 1 - 2.
	def resta(self):
		resta=self.valor_1-self.valor_2
		print("El resultado de la operacion resta de sus valores es: ",resta)

	# Se crea la funcion multiplicacion esta me permite operar el valor 1 * 2.
	def multiplicacion(self):
		promedio=self.valor_1*self.valor_2
		print("El resultado de la operacion multiplicacion de sus valores es: ",promedio)

	# Se crea la funcion division.esta me permite operar el valor 1 / 2.
	def division(self):
		division=self.valor_1/self.valor_2
		print("El resultado de la operacion división de sus valores es: ",division)

	# se crea la función imprimir 
	def imprimir(self):
		print("Los valores son: ")
		print("Valor 1: ",self.valor_1)
		print("Valor 2: ",self.valor_2)

# Se crea la funcion divisionprincipal calcular.
calcular=Calculadora()
calcular.imprimir()
calcular.suma()
calcular.resta()
calcular.multiplicacion()
calcular.division()