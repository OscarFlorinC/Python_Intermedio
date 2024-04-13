'''
class <Nombre de la clase>(): #esta es la estructura de la clase,se recomienda que cuando se crea una clase la palabra inicie con mayuscula
    pass

'''

class FabricaTelefonos():       #FabricaTelefonos es la clase
    pass

print(type(FabricaTelefonos))

celular = FabricaTelefonos()    #Es un objeto
celular2 = FabricaTelefonos()

print(type(celular))
print(type(celular2))

def fabricaTelefonos():         #No poner el mismo nombre que la clase.
    pass

print(type(fabricaTelefonos()))