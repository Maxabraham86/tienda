from producto import Producto
from abc import ABC, abstractmethod
#tipo = "supermercado" | 'farmacia' | 'restoran'


class Tienda():

        
    def __init__(self, nombre, costo_delivery, tipo):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos= []
        self.tipo = tipo
        
    def ingresar_producto (self,nombre, precio, stock):
        
        # profe
        # nuevo_producto= Producto(nombre,precio,stock)
        # for prod in self.__productos:
        #     if prod == nuevo_producto:
        #         prod.stock += nuevo_producto.stock
        #         return
        
        for prod in self.__productos:
            if prod.get_nombre == producto.get_nombre():
                prod.set_stock(prod.get_stock() + producto.get_stock)

# si llego a esta linea, quiere decir que nunca encontré el producto
        self.productos.append(nuevo_producto)

    def listar_productos(self):
        for producto in self.__productos:
            lista_productos += str(producto) +'\n'
        return lista_productos
        
        
    
    def realizar_venta(self, nombre_producto, cantidad):
        pass
    
class Restaurante(Tienda):
    def realizar_venta(self, nombre_producto, cantidad):
    #En el restaurante no se modifica el stock
    
        class Supermercado(Tienda):
            def listar_productos(self):
                lista_productos =''
                for producto in self.__tienda__productos:
                    if producto.get_stock() < 10:
                        lista_productos += f'{str(producto)}- Pocos productos disponibles \n'
                    else:
                        lista_productos += str(producto) + '\n'
                
                return listar_productos
            def realizar_venta(self, nombre_producto, cantidad):
                pass
            
class Farmacia(Tienda):
    def listar_productos(self):
        lista_productos =''
        for producto in self.__tienda__productos:
            if productos.get_precio() > 15000:
                lista_productos += f'{str(producto)} - Envío gratis al solicitar este producto \n'
                
    def realizar_venta(self, nombre_producto, cantidad):
        return            