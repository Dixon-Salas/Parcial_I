# Aqui se creo la clase agenda.
class Agenda:
	# se inicializa  la clase agenda con --init--.
	def __init__(self):
		# se creo una lista la cual permite guardar  datos de nuestra agenda
		self.contactos=[]

	# Se creo menu principal  del programa
	def menu(self):
		print()
		menu=(
				
			['|---------------------------|'],
			['|******Agenda Personal******|'],
			['|1. Agregar Contacto        |',"|Agregar|"],
			['|2. Lista de contactos      |'],
			['|3. Buscar contacto         |'],
			['|4. Editar contacto         |'],
			['|5. Cerrar agenda           |'],
		)

		for x in range(6):
			print(menu[x][0])

		opcion=int(input("|   Digite la una opcion    |: "))
		if opcion==1:
			self.agregar()

		elif opcion==2:
			self.lista()

		elif opcion==3:
			self.buscar()

		elif opcion==4:
			self.editar()

		elif opcion==5:
			print("Salir de la agenda ...")
			exit()

		# Permite llamar la funcion del menú principal.
		self.menu()

	# Se creo la función agregar un contacto
	def agregar(self):
		print("---------------------")
		print("Agregar contacto nuevo")
		print("---------------------")
		nombre=input("Digite el nombre: ")
		telefono=int(input("Digite el teléfono: "))
		email=input("Digite el email: ")
		self.contactos.append({'nombre':nombre,'telefono':telefono,'email':email})
		

	# se crea la función para imprimit lista de contacto.
	def lista(self):
		print("------------------")
		print("Lista de contactos")
		print("------------------")
		if len(self.contactos) == 0:
			print("No hay contacto en la agenda")
		else:
			for x in range(len(self.contactos)):
				print(self.contactos[x]['nombre'])
		

	# Se crea la función buscar la cualpermite 
	def buscar(self):
		print("---------------------")
		print("Buscador de contactos")
		print("---------------------")
		nombre=input("Digite el nombre del contacto: ")
		for x in range(len(self.contactos)):
			if nombre == self.contactos[x]['nombre']:
				print("Datos del contacto")
				print("Nombre: ",self.contactos[x]['nombre'])
				print("Teléfono: ",self.contactos[x]['telefono'])
				print("E-mail: ",self.contactos[x]['email'])
				return x
		

	# Se crea esta función la cual permite  editar los datos de un contacto
	def editar(self):
		print("---------------")
		print("Editar contacto")
		print("---------------")
		data=self.buscar()
		condicion=False
		while condicion==False:
			print("Selecciona una opcion para editar: ")
			print("1. Nombre.")
			print("2. Teléfono.")
			print("3. E-mail.")
			print("4. Volver.")

			option=int(input("Digite la opción deseada: "))
			if option==1:
				nombre=input("Digite su nuevo nombre: ")
				self.contactos[data]['nombre']=nombre

			elif option==2:
				telefono=input("Digite el nuevo teléfono: ")
				self.contactos[data]['telefono']=telefono

			elif option==3:
				email=input("Digite el nuevo email: ")
				self.contactos[data]['email']=email
			elif option==4:
				condicion=True

# se crea la variable agenda la cual es = clse Agenda y metodo menu.
agenda=Agenda()
agenda.menu()

#Nota: Esos mmenu siempre me han dado duro para cuadrarlos.