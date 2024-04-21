# Ejemplo de Encapsulamiento 
class Computer:
    def __init__(self):
        self.__maxprice = 900
    
    def sell(self):
        print(f"El precio de venta es: {self.__maxprice}")
    
    def set_maxprice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()                # El precio de venta es: 900

# Se cambia el precio
c.__maxprice = 1000     # El precio de venta es: 900
c.sell()

# Usamos la función setter 
c.set_maxprice(1000)
c.sell()                # El precio de venta es: 1000