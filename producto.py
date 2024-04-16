class Producto:

    def __init__(self, nombre, precio, stock = 0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        
    def get_nomrbe(self):
        return self.__nombre
    
    def get_precio(self):
        return self.__precio    
        
    def get_stock(self):
        return self.__stock
    if cantidad <  0:
        self.__stock = 0
    else:
        self.__stock = cantidad
            
            
            
    def __str__(self):
        return f'Nombre: {self.__nombre}. Precio:{self.__precio}, Stock: {self.__stocl}'
            
            
    def __eq__(self,otro_prod,):
        
        return self.nombre == otro_prod.nombre
    
    