# Se  clase principal Persona la cual contiene los atribudos nobre y edad 
class Persona:
	def inicializar(self,nombre,edad):
		self.nombre=nombre
		self.edad=edad

	# Se crea la funcio imprimir la cual permite capturar el nomre y edad de la persona a consultar.
	def imprimir(self):
		print("Nombre: ",self.nombre)
		print("Edad: ",self.edad)

	# Funcion para comprobar si la persona es mayor de edad o si es menor de edad.
	def mayor_edad(self):
		if self.edad >= 18:
			print("La Persona actual es Mayor de edad")
		else:
			print("La persona actual No es mayor de edad")

persona1=Persona()
persona1.inicializar("Jorge",25)
persona2=Persona()
persona2.inicializar("Marcela",17.5)

# imprimimos datos y comprobamos si es mayor de edad
persona1.imprimir()
persona1.mayor_edad()
persona2.imprimir()
persona2.mayor_edad()