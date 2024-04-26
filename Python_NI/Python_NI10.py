class Estudiante():     #esta es la clase padre
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre: {} \nNota: {}".format(self.nombre, self.nota))

    def resultados(self):
        if self.nota < 7:
            print("Has REPROBADO")
        else:
            print("Has APROBADO")

estudiante1 = Estudiante("Juan" , 10)
estudiante1.imprimir()
estudiante1.resultados()

estudiante2 = Estudiante("Miguel", 6)
estudiante2.imprimir()
estudiante2.resultados()