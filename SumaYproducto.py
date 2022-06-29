from Producto2P import ProductoDosParametros
from Suma import Suma
from Resta import Resta


class SumaProducto:

    """
    9- función p1 (productoSuma), retorna el producto de los 2 primero más el 3er parámetros, usando las funciones anteriores.
    10- función p1 (sumaProducto), retorna la suma de los 2 primero por el 3er parámetros, usando las funciones anteriores.
    11- función p1 (restaProducto), retorna la resta de los 2 primero por el 3er parámetros, usando las funciones anteriores.
    """
    
    @staticmethod
    def productoSuma(num1, num2, num3):
        valor = ProductoDosParametros.Producto2P(num1, num2)
        return Suma.suma(valor, num3)
    
    @staticmethod
    def sumaProducto(num1, num2, num3):
        valor = Suma.suma(num1, num2)
        return ProductoDosParametros.Producto2P(valor, num3)


    @staticmethod
    def restaProducto(num1, num2, num3):
        valor = Resta.resta(num1, num2)
        return ProductoDosParametros.Producto2P(valor, num3)