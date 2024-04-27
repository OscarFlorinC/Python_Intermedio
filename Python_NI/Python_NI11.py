class Calculadora():
    def __init__(self):
        self.num1 = int(input("Ingresa el prime valor: "))
        self.num2 = int(input("Ingresa el segundo valor: "))
        
    def suma(self):
        self.suma = self.num1 + self.num2
        print( "La suma da como resultado: ", self.suma)
    
    def resta(self):
        self.resta = self.num1 - self.num2
        print( "La resta da como resultado: ", self.resta)

    def multiplicacion(self):
        self.multiplicacion = self.num1 * self.num2
        return "La multiplicación da como resultado: ", self.multiplicacion

    def division(self):
        self.division = self.num1 / self.num2
        return "La división da como resultado: ", self.division

calcular = Calculadora()
calcular.suma()
calcular.resta()
print(calcular.multiplicacion())
print(calcular.division())