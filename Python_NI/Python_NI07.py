# Ejemplo herencia múltiple
class A():
    def primera (self):
        return "La clase A"

class B():
    def segunda(self):
        return "La clase B"

class C(A, B):
    pass

a = A()
print(f"Esta es la clase: ", a.primera())
b = B()
print(f"Esta es la clase: ", b.segunda())

c = C()
print(f"Esta es la clase C con herencia de: ", c.primera())
print(f"Esta es la clase C con herencia de: ",c.segunda())