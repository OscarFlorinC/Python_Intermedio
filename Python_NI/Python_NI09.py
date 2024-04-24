"""polimorfismo es la modificación de métodos de 
clases heredadas y también la ocupación de
objetos a partir de varios objetos."""

class Animales():
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)

class Perro(Animales):
    def hablar(self):
        print("Yo hago Guau")

class Pez(Animales):
    def hablar(self):
        print("Yo no hablo")

perro = Perro("Guau")
perro.hablar()

animal = Animales("Miau")
animal.hablar()

pez = Pez("Nada")
pez.hablar()