# Se crea la clase Alumno la cual contiene los atributos de nombre y nota.
class Alumno:
    
    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    # se crea la funcion imprimir los datos nombre y nota
    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("Nota: ",self.nota)

    # se crea la función resultado para obtener su nota y estado aprobado o no aprobado.
    def resultado(self):
        if self.nota < 5:
            print("El alumno No Aprobo la materia")
        else:
            print("El alumno Aprobo la materia")

# se crea los nuevos alumnos
alumno1=Alumno()
alumno2=Alumno()

#  Se inicializa los atributos de los nuevos alumnos
alumno1.inicializar("Carlos",2.5)
alumno2.inicializar("Marcela",4)

# Se imprime los datos y resultados de los nuevos alumnos.
alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()