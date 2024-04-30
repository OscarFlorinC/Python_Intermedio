class Universidad():
    def __init__(self, nombre):
        self.Nombre = nombre

class Carrera():
    def especialidad(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def datos(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print("Mi nombre es {}, \ntengo {} años, \nmi especialidad es {}, \nestudio en {}".format(self.nombre, self.edad, self.especialidad, self.Nombre))

persona = Estudiante("ESIME")
persona.especialidad("Ing. Comunicaciones y Electrónica")
persona.datos("Juan López", 20)