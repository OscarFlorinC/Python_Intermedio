'''
def Función():      # Estructura de una Función
    pass
    
'''

# Clase, lo de mas son su atributos
class FabricaCelulares():
    marca = "Marca: Texca"
    color = "Color: Negro"
    almacenamiento = "Almacenamiento: " + str(256) + "Gb"

    """ Método de instancia, el celular fue 
        creado para realizar llamadas """
    def llamar(self, mensaje):      
        return mensaje

    def escucharMusica(self):
        print("Estoy escuchando a Fobia")

# Celular es un objeto
celular = FabricaCelulares() 
print(celular.marca)
print(celular.color)
print(celular.almacenamiento)

print(celular.llamar("Hola, con quien quiere hablar?"))
celular.escucharMusica()