# Método ejecutor

class FabricaTelefonos():
    #init nos ahorra declarar los atributos
    def __init__(self , marca , color): 
        print("Estoy ejecutando el método Init.")
        print("Porque se creo un nuevo objeto")
        self.marca = marca
        self.color = color
        
telefonos = FabricaTelefonos("Texca","Negro")
print(telefonos.marca)
print(telefonos.color)