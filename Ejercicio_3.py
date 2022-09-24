# Se crea la clase principal llamada triangulo la cual contiene la funcion del los atributos de los lados.
class Triangulo:
	def inicializar(self):
		self.ladoA=int(input("Digite el valor del lado A: "))
		self.ladoB=int(input("Digite el valor del lado B: "))
		self.ladoC=int(input("Digite el valor del lado C: "))

	# se crea la funcio de imprimir de la clase triángulo.
	def imprimir(self):
		print("Los lados del triángulo tienen el valor de")
		print("Lado A: ",self.ladoA)
		print("Lado B: ",self.ladoB)
		print("Lado C: ",self.ladoC)

	# Se crea la funcion de lados del mayor
	def mayor(self):
		print("El lado mayor es")
		if self.ladoA>self.ladoB and self.ladoA>self.ladoC:
			print("Lado A: ",self.ladoA)
		elif self.ladoB>self.ladoC:
			print("Lado B: ",self.ladoB)
		else:
			print("Lado C: ",self.ladoC)

	# Se crea la  funcion tipo de triangulo  la cual permite clasificar el triángulo. 
	# equilátero = todos sus lados son iguales.
	# isósceles = dos de sus lados son iguales.
	# escaleno = todos sus lados son desiguales.

	def tipo(self):
		if self.ladoA==self.ladoB and self.ladoA==self.ladoC:
			print("Este es un triángulo equilátero")

		elif self.ladoA!=self.ladoB and self.ladoA!=self.ladoC:
			print("Este es un triángulo escaleno")

		else:
			print("Este es  un triángulo isósceles")

#Se creala variable figura la cual me hace el llamado a la clase triángulo y a los metodos:
#  inicaliza,imprimir,mayor y tipo.

figura=Triangulo()
figura.inicializar()
figura.imprimir()
figura.mayor()
figura.tipo()