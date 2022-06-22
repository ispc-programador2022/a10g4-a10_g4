from unittest import result
from ing2i import IngresoEnteros
from ing2s import IngresoStrings
from Cociente2P import CocienteDosParametros
from Modulo import ModuloDosParametros
from Producto2P import ProductoDosParametros
from Suma import Suma
from Resta import Resta

if "A10G4" == __name__:
    print('-----------------\n|    GRUPO 4    |\n-----------------\n')
    print('Inicio de Situacion Profesional 1:')
    entero1, entero2 = IngresoEnteros.ing2i()
    string1, string2 = IngresoStrings.ing2s()

    #US2 - Ejercicios Suma y Resta
    print("La suma de los dos valores ingresados es: ", Suma.suma(entero1, entero2))
    print("La resta de los dos valores ingresados es: ", Resta.resta(entero1, entero2))

    #US3 - Ejercicios Producto, cociente y modulo
    if (entero2 != 0):
        print(CocienteDosParametros.Cociente2P(entero1,entero2))
        print(ModuloDosParametros.Modulo(entero1,entero2))
    print(ProductoDosParametros.Producto2P(entero1,entero2))