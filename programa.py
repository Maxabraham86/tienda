from tienda import Tienda, Restaurante, Supermercado, Farmacia
from producto import Producto

def main():
    nombre_tienda =input ('Ingrese el nombre de la tienda: ')
    costo_delivery = float(input('Ingrese el costo de delivery '))
    
    tienda = Tienda(nombre_tienda, costo_delivery)
    
    while True:
        print("\n1. Ingresar producto")
        print("2. Listar productos")
        print ("3. Realizar venta")
        print("4. salir")
        opcion = input ('Selecciones una opcion: ')
        
        if opcion == '1':
            nombre_producto =input('Ingrese el nombre del producto: ')
            precio_producto = float(input('Ingrese el precio del producto: '))
            stock_producto = int(input('Ingrese el stock del producto: '))
            tienda.ingresar_producto(producto)
            print ('Producti ingresado exitosamente')
            
        elif opcion == '2':
            print('Productos disponibles')
            ptin (tienda.lista_productos())
            
        elif opcion =='3':
            nombre_producto = input('Ingrese el nombre del producto a vender: ')
            cantidad = int(input('Ingrese la cantidad a vender: '))
            tienda.realizar_venta(nombre_producto, cantidad)
            
        elif opcion == '4':
            print(' Saliendo del programa ...')
            break
        else:
            print (' Opcion no válida. Por favor, seleccione una opción válida')
            
if __name__ == '__main__':
    main()
    