from producto import Producto
from abc import ABC, abstractmethod
#tipo = "supermercado" | 'farmacia' | 'restoran'


class ATienda(ABC):
    @abstractmethod
    def tipo_tienda(self, tipo = str):
        pass
    @abstractmethod
    def producto_tienda(self):
        return self.producto_tienda
        
        
    def __init__(self, nombre, costo_delivery, tipo):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.productos= []
        self.tipo = tipo
        
    def ingresar_producto (self,nombre, precio, stock):
        nuevo_producto= Producto(nombre,precio,stock)
        
        for prod in self.productos:
            if prod == nuevo_producto:
                prod.stock += nuevo_producto.stock
                return

# si llego a esta linea, quiere decir que nunca encontré el producto
        self.productos.append(nuevo_producto)
class Lista_prod(Atienda):
    def listar_productos(self):
        self.tipo_tienda("supermercado")
        nuevo_producto
        
        
        pass
    
    def realizar_venta(self):
        pass
    